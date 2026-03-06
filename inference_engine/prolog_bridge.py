"""
ATM Expert Inference Engine - Prolog Bridge
Developer 1: Shadrack Dorkenoo

This module provides the Python interface to the SWI-Prolog knowledge base.
It handles diagnosis, explanation generation, and fault retrieval.
"""

import subprocess
import re
import json
from pathlib import Path
from typing import List, Dict, Optional, Any, Tuple


class PrologInferenceEngine:
    """
    Python bridge to the SWI-Prolog based ATM fault diagnosis engine.
    
    Features:
    - Fault diagnosis from symptoms and error codes
    - Confidence scoring based on observation matches
    - Plain-language explanation generation
    - Severity-based filtering
    - Benchmark scenario support
    """
    
    # Severity levels for filtering (ordered from lowest to highest)
    SEVERITY_LEVELS = ['LOW', 'MEDIUM', 'HIGH', 'CRITICAL']
    
    def __init__(self, kb_path: Optional[Path] = None):
        """
        Initialize the inference engine.
        
        Args:
            kb_path: Path to the Prolog knowledge base loader.
                     Defaults to knowledge_base/loader.pl
        """
        if kb_path is None:
            # Use loader.pl which imports both facts and rules
            kb_path = Path(__file__).parent.parent / "knowledge_base" / "loader.pl"
        self.kb_path = Path(kb_path)
        
        if not self.kb_path.exists():
            raise FileNotFoundError(f"Knowledge base not found: {self.kb_path}")

    def _escape_prolog_string(self, s: str) -> str:
        """Escape a string for safe use in Prolog queries."""
        # Escape single quotes by doubling them
        return s.replace("'", "''")

    def _query(self, query_str: str, timeout: int = 10) -> str:
        """
        Run a Prolog query via CLI and return the output.
        
        Args:
            query_str: The Prolog query to execute
            timeout: Maximum seconds to wait for query completion
            
        Returns:
            Query output as string, or error message
        """
        try:
            cmd = [
                "swipl", "-q",           # Quiet mode
                "-s", str(self.kb_path), # Load KB
                "-g", query_str,         # Execute goal
                "-t", "halt"             # Exit after goal
            ]
            result = subprocess.run(
                cmd, 
                capture_output=True, 
                text=True, 
                timeout=timeout
            )
            
            # Check for Prolog errors in stderr
            if result.stderr and "ERROR" in result.stderr:
                return f"ERROR: {result.stderr.strip()}"
                
            return result.stdout.strip()
            
        except subprocess.TimeoutExpired:
            return "ERROR: Query timed out"
        except FileNotFoundError:
            return "ERROR: SWI-Prolog (swipl) not found in PATH"
        except Exception as e:
            return f"ERROR: {str(e)}"

    def diagnose(
        self, 
        symptoms: Optional[List[str]] = None, 
        error_codes: Optional[List[str]] = None,
        min_severity: Optional[str] = None,
        include_details: bool = True
    ) -> List[Dict[str, Any]]:
        """
        Diagnose faults based on symptoms and error codes.
        
        Args:
            symptoms: List of observed symptoms (e.g., ['Card not ejected'])
            error_codes: List of error codes (e.g., ['3A1', 'ICM001'])
            min_severity: Minimum severity level to include ('LOW', 'MEDIUM', 'HIGH', 'CRITICAL')
            include_details: Whether to fetch full details (slower but more info)
            
        Returns:
            List of diagnosis results with fault_id, confidence, and matched observations
        """
        symptoms = symptoms or []
        error_codes = error_codes or []
        
        if not symptoms and not error_codes:
            return []
        
        # Build observation list for Prolog
        observations = []
        for s in symptoms:
            escaped = self._escape_prolog_string(s)
            observations.append(f"symptom('{escaped}')")
        for c in error_codes:
            escaped = self._escape_prolog_string(c)
            observations.append(f"error_code('{escaped}')")
        
        obs_list = "[" + ", ".join(observations) + "]"
        
        # Query for all matching faults with their details in one go
        query = (
            f"diagnose(FID, {obs_list}), "
            f"fault_profile(FID, D, SD, T, S), "
            f"format('~w|~w|~w|~w|~w~n', [FID, D, SD, T, S]), fail"
        )
        output = self._query(query)
        
        if output.startswith("ERROR"):
            return []
        
        # Parse results
        seen = set()
        results = []
        
        for line in output.split("\n"):
            line = line.strip()
            if not line:
                continue
            parts = line.split("|")
            if len(parts) < 5:
                continue
            
            fid = parts[0]
            if fid in seen:
                continue
            seen.add(fid)
            
            severity = parts[4]
            
            # Apply severity filter
            if min_severity:
                if self._severity_rank(severity) < self._severity_rank(min_severity):
                    continue
            
            # Calculate confidence based on matched observations
            matched = self._get_matched_observations_fast(fid, symptoms, error_codes)
            total_obs = len(symptoms) + len(error_codes)
            confidence = len(matched) / total_obs if total_obs > 0 else 0
            
            results.append({
                'fault_id': fid,
                'title': parts[3],
                'severity': severity,
                'domain': parts[1],
                'sub_domain': parts[2],
                'confidence': round(confidence, 2),
                'matched_observations': matched
            })
        
        # Sort by confidence (highest first), then severity
        results.sort(
            key=lambda x: (x['confidence'], self._severity_rank(x['severity'])),
            reverse=True
        )
        
        return results
    
    def _get_matched_observations_fast(
        self, 
        fault_id: str, 
        symptoms: List[str], 
        error_codes: List[str]
    ) -> List[Dict[str, str]]:
        """Find which observations matched a specific fault (optimized version)."""
        matched = []
        escaped_id = self._escape_prolog_string(fault_id)
        
        # Check all symptoms in one query
        for symptom in symptoms:
            escaped = self._escape_prolog_string(symptom)
            query = f"has_symptom('{escaped_id}', '{escaped}')"
            output = self._query(query)
            if not output.startswith("ERROR") and "true" not in output.lower() and output != "false":
                # Prolog succeeded (no output means success for simple query)
                if not output or output == "":
                    pass  # Need to verify differently
            # Simple check - if query doesn't error and doesn't say false
            if not output.startswith("ERROR"):
                query2 = f"has_symptom('{escaped_id}', '{escaped}'), writeln(yes)"
                output2 = self._query(query2)
                if 'yes' in output2:
                    matched.append({'type': 'symptom', 'value': symptom})
        
        # Check all error codes
        for code in error_codes:
            escaped = self._escape_prolog_string(code)
            query = f"has_error_code('{escaped_id}', '{escaped}'), writeln(yes)"
            output = self._query(query)
            if 'yes' in output:
                matched.append({'type': 'error_code', 'value': code})
        
        return matched

    def diagnose_fast(
        self, 
        symptoms: Optional[List[str]] = None, 
        error_codes: Optional[List[str]] = None
    ) -> List[Dict[str, Any]]:
        """
        Fast diagnosis without detailed observation matching.
        Optimized for benchmark testing.
        
        Returns only fault_id, title, severity, domain (no confidence calculation).
        """
        symptoms = symptoms or []
        error_codes = error_codes or []
        
        if not symptoms and not error_codes:
            return []
        
        # Build observation list for Prolog
        observations = []
        for s in symptoms:
            escaped = self._escape_prolog_string(s)
            observations.append(f"symptom('{escaped}')")
        for c in error_codes:
            escaped = self._escape_prolog_string(c)
            observations.append(f"error_code('{escaped}')")
        
        obs_list = "[" + ", ".join(observations) + "]"
        
        # Query for all matching faults with basic details in one go
        query = (
            f"diagnose(FID, {obs_list}), "
            f"fault_profile(FID, D, SD, T, S), "
            f"format('~w|~w|~w|~w|~w~n', [FID, D, SD, T, S]), fail"
        )
        output = self._query(query)
        
        if output.startswith("ERROR"):
            return []
        
        # Parse results
        seen = set()
        results = []
        
        for line in output.split("\n"):
            line = line.strip()
            if not line:
                continue
            parts = line.split("|")
            if len(parts) < 5:
                continue
            
            fid = parts[0]
            if fid in seen:
                continue
            seen.add(fid)
            
            results.append({
                'fault_id': fid,
                'title': parts[3],
                'severity': parts[4],
                'domain': parts[1],
                'sub_domain': parts[2]
            })
        
        return results
    
    def _severity_rank(self, severity: str) -> int:
        """Convert severity string to numeric rank."""
        try:
            return self.SEVERITY_LEVELS.index(severity.upper())
        except (ValueError, AttributeError):
            return 0
    
    def _get_matched_observations(
        self, 
        fault_id: str, 
        symptoms: List[str], 
        error_codes: List[str]
    ) -> List[Dict[str, str]]:
        """Find which observations matched a specific fault."""
        matched = []
        
        # Check symptoms
        for symptom in symptoms:
            escaped = self._escape_prolog_string(symptom)
            query = f"has_symptom('{fault_id}', '{escaped}'), writeln(matched), fail"
            output = self._query(query)
            if 'matched' in output:
                matched.append({'type': 'symptom', 'value': symptom})
        
        # Check error codes
        for code in error_codes:
            escaped = self._escape_prolog_string(code)
            query = f"has_error_code('{fault_id}', '{escaped}'), writeln(matched), fail"
            output = self._query(query)
            if 'matched' in output:
                matched.append({'type': 'error_code', 'value': code})
        
        return matched

    def get_details(self, fault_id: str) -> Optional[Dict[str, Any]]:
        """
        Get full details for a specific fault ID.
        
        Args:
            fault_id: The fault identifier (e.g., 'HW_001')
            
        Returns:
            Dictionary with fault details or None if not found
        """
        escaped_id = self._escape_prolog_string(fault_id)
        
        # Query for basic details
        query = (
            f"get_fault_details('{escaped_id}', D, SD, T, S, Desc, RS), "
            f"format('~w|~w|~w|~w|~w|~w', [D, SD, T, S, Desc, RS])"
        )
        output = self._query(query)
        
        if output.startswith("ERROR") or not output:
            return None
        
        parts = output.split("|")
        if len(parts) < 6:
            return None
        
        # Parse resolution steps from Prolog list format
        resolution_raw = parts[5]
        resolution_steps = self._parse_prolog_list(resolution_raw)
        
        # Get causes
        causes = self._get_causes(fault_id)
        
        # Get all symptoms for this fault
        all_symptoms = self._get_fault_symptoms(fault_id)
        
        # Get all error codes for this fault
        all_error_codes = self._get_fault_error_codes(fault_id)
        
        return {
            "fault_id": fault_id,
            "domain": parts[0],
            "sub_domain": parts[1],
            "title": parts[2],
            "severity": parts[3],
            "description": parts[4],
            "resolution_steps": resolution_steps,
            "causes": causes,
            "symptoms": all_symptoms,
            "error_codes": all_error_codes
        }
    
    def _parse_prolog_list(self, prolog_list: str) -> List[str]:
        """Parse a Prolog list string into Python list."""
        # Handle format like [Step1,Step2,Step3]
        if not prolog_list or prolog_list == '[]':
            return []
        
        # Remove brackets and split
        content = prolog_list.strip('[]')
        if not content:
            return []
        
        # Simple split - may need refinement for complex cases
        return [s.strip().strip("'\"") for s in content.split(',')]
    
    def _get_causes(self, fault_id: str) -> List[str]:
        """Get all causes for a fault."""
        escaped_id = self._escape_prolog_string(fault_id)
        query = f"has_cause('{escaped_id}', C), writeln(C), fail"
        output = self._query(query)
        
        if output.startswith("ERROR") or not output:
            return []
        
        return [line.strip() for line in output.split("\n") if line.strip()]
    
    def _get_fault_symptoms(self, fault_id: str) -> List[str]:
        """Get all symptoms for a fault."""
        escaped_id = self._escape_prolog_string(fault_id)
        query = f"has_symptom('{escaped_id}', S), writeln(S), fail"
        output = self._query(query)
        
        if output.startswith("ERROR") or not output:
            return []
        
        return [line.strip() for line in output.split("\n") if line.strip()]
    
    def _get_fault_error_codes(self, fault_id: str) -> List[str]:
        """Get all error codes for a fault."""
        escaped_id = self._escape_prolog_string(fault_id)
        query = f"has_error_code('{escaped_id}', C), writeln(C), fail"
        output = self._query(query)
        
        if output.startswith("ERROR") or not output:
            return []
        
        return [line.strip() for line in output.split("\n") if line.strip()]

    def get_all_faults(self, domain: Optional[str] = None) -> List[Dict[str, str]]:
        """
        Get a summary of all faults in the knowledge base.
        
        Args:
            domain: Optional filter by domain (e.g., 'Hardware', 'Network')
            
        Returns:
            List of fault summaries with id, title, domain, severity
        """
        if domain:
            escaped_domain = self._escape_prolog_string(domain)
            query = (
                f"fault_profile(ID, '{escaped_domain}', SD, T, S), "
                f"format('~w|~w|~w|~w|~w~n', [ID, '{escaped_domain}', SD, T, S]), fail"
            )
        else:
            query = (
                "fault_profile(ID, D, SD, T, S), "
                "format('~w|~w|~w|~w|~w~n', [ID, D, SD, T, S]), fail"
            )
        
        output = self._query(query)
        
        if output.startswith("ERROR") or not output:
            return []
        
        faults = []
        for line in output.split("\n"):
            line = line.strip()
            if not line:
                continue
            parts = line.split("|")
            if len(parts) >= 5:
                faults.append({
                    'fault_id': parts[0],
                    'domain': parts[1],
                    'sub_domain': parts[2],
                    'title': parts[3],
                    'severity': parts[4]
                })
        
        return faults

    def explain_diagnosis(
        self, 
        fault_id: str, 
        symptoms: List[str], 
        error_codes: List[str]
    ) -> List[str]:
        """
        Generate plain-language explanation for why a fault was diagnosed.
        
        Args:
            fault_id: The diagnosed fault ID
            symptoms: The observed symptoms
            error_codes: The observed error codes
            
        Returns:
            List of explanation strings
        """
        details = self.get_details(fault_id)
        if not details:
            return ["Unable to retrieve fault details."]
        
        matched = self._get_matched_observations(fault_id, symptoms, error_codes)
        
        explanations = []
        
        # Opening statement
        explanations.append(
            f"Diagnosis: {details['title']} ({fault_id})"
        )
        explanations.append(
            f"Severity: {details['severity']} | Domain: {details['domain']} > {details['sub_domain']}"
        )
        
        # Matched observations
        if matched:
            explanations.append("")
            explanations.append("Evidence supporting this diagnosis:")
            for i, obs in enumerate(matched, 1):
                if obs['type'] == 'symptom':
                    explanations.append(f"  {i}. Symptom matched: \"{obs['value']}\"")
                else:
                    explanations.append(f"  {i}. Error code matched: {obs['value']}")
        
        # Possible causes
        if details.get('causes'):
            explanations.append("")
            explanations.append("Possible root causes:")
            for cause in details['causes']:
                explanations.append(f"  • {cause}")
        
        # Description
        explanations.append("")
        explanations.append(f"Description: {details['description']}")
        
        return explanations

    def run_benchmark_scenario(self, scenario: Dict[str, Any]) -> Dict[str, Any]:
        """
        Run a single benchmark scenario and return the diagnosis result.
        
        Args:
            scenario: Benchmark scenario dict with error_codes, sensor_readings, etc.
            
        Returns:
            Result dict with diagnosis, match status, and details
        """
        # Extract observations from scenario
        error_codes = scenario.get('error_codes', [])
        
        # Convert sensor readings to symptoms
        symptoms = []
        sensor_readings = scenario.get('sensor_readings', {})
        
        # Map sensor readings to symptom strings
        sensor_symptom_map = {
            'card_reader_status': lambda v: f"Reader status: {v}" if v != "OK" else None,
            'printer_status': lambda v: f"Printer status: {v}" if v != "OK" else None,
            'dispenser_status': lambda v: f"Dispenser status: {v}" if v != "OK" else None,
            'network_status': lambda v: f"Network status: {v}" if v != "DOWN" and v != "OK" else ("Network connection lost" if v == "DOWN" else None),
        }
        
        for sensor, mapper in sensor_symptom_map.items():
            if sensor in sensor_readings:
                symptom = mapper(sensor_readings[sensor])
                if symptom:
                    symptoms.append(symptom)
        
        # Extract transaction context symptoms
        tx_context = scenario.get('transaction_context', {})
        if tx_context.get('last_error'):
            error_map = {
                'CARD_NOT_EJECTED': 'Card not ejected',
                'DISPENSE_FAILED': 'Dispense attempt fails',
                'RECEIPT_NOT_PRINTED': 'Receipt not printed',
                'NETWORK_TIMEOUT': 'Network timeout',
            }
            symptom = error_map.get(tx_context['last_error'])
            if symptom:
                symptoms.append(symptom)
        
        # Run diagnosis
        diagnoses = self.diagnose(symptoms=symptoms, error_codes=error_codes)
        
        # Compare with expected
        expected_title = scenario.get('expected_diagnosis', '')
        expected_severity = scenario.get('expected_severity', '')
        
        # Check if any diagnosis matches
        matched = False
        matched_diagnosis = None
        
        for diag in diagnoses:
            if diag['title'].lower() == expected_title.lower():
                matched = True
                matched_diagnosis = diag
                break
        
        return {
            'scenario_id': scenario.get('scenario_id', ''),
            'expected_diagnosis': expected_title,
            'expected_severity': expected_severity,
            'actual_diagnoses': diagnoses,
            'primary_diagnosis': diagnoses[0] if diagnoses else None,
            'matched': matched,
            'matched_diagnosis': matched_diagnosis,
            'observations_used': {
                'symptoms': symptoms,
                'error_codes': error_codes
            }
        }

    def get_resolution_workflow(self, fault_id: str) -> Dict[str, Any]:
        """
        Get a structured remediation workflow for a fault.
        
        Args:
            fault_id: The fault identifier
            
        Returns:
            Workflow dict with steps, estimated time, and required tools
        """
        details = self.get_details(fault_id)
        if not details:
            return {'error': 'Fault not found'}
        
        # Estimate complexity based on step count
        steps = details.get('resolution_steps', [])
        step_count = len(steps)
        
        if step_count <= 3:
            complexity = 'LOW'
            est_time = '5-15 minutes'
        elif step_count <= 5:
            complexity = 'MEDIUM'
            est_time = '15-30 minutes'
        else:
            complexity = 'HIGH'
            est_time = '30-60 minutes'
        
        # Determine required role based on severity
        severity = details.get('severity', 'MEDIUM')
        if severity == 'CRITICAL':
            required_role = 'Field Engineer'
        elif severity == 'HIGH':
            required_role = 'Branch Staff or Field Engineer'
        else:
            required_role = 'Branch Staff'
        
        return {
            'fault_id': fault_id,
            'title': details['title'],
            'severity': severity,
            'complexity': complexity,
            'estimated_time': est_time,
            'required_role': required_role,
            'steps': [
                {'step_number': i+1, 'action': step}
                for i, step in enumerate(steps)
            ],
            'causes': details.get('causes', []),
            'domain': details['domain'],
            'sub_domain': details['sub_domain']
        }


# Convenience function for quick diagnosis
def quick_diagnose(symptoms: List[str] = None, error_codes: List[str] = None) -> List[Dict]:
    """Quick diagnosis without instantiating engine manually."""
    engine = PrologInferenceEngine()
    return engine.diagnose(symptoms=symptoms, error_codes=error_codes)


if __name__ == "__main__":
    import sys
    
    print("=" * 60)
    print("ATM Expert Inference Engine - Test Suite")
    print("=" * 60)
    
    try:
        engine = PrologInferenceEngine()
        print(f"✓ Knowledge base loaded: {engine.kb_path}")
    except FileNotFoundError as e:
        print(f"✗ Failed to load knowledge base: {e}")
        sys.exit(1)
    
    print("\n" + "-" * 60)
    print("Test 1: Basic Diagnosis")
    print("-" * 60)
    
    test_symptoms = ["Card not ejected"]
    test_codes = ["3A1"]
    
    print(f"Symptoms: {test_symptoms}")
    print(f"Error codes: {test_codes}")
    
    results = engine.diagnose(symptoms=test_symptoms, error_codes=test_codes)
    
    if results:
        print(f"\n✓ Found {len(results)} diagnosis(es):")
        for r in results:
            print(f"  - {r['fault_id']}: {r['title']} "
                  f"(Confidence: {r['confidence']}, Severity: {r['severity']})")
    else:
        print("✗ No diagnoses found")
    
    print("\n" + "-" * 60)
    print("Test 2: Explanation Generation")
    print("-" * 60)
    
    if results:
        explanation = engine.explain_diagnosis(
            results[0]['fault_id'], 
            test_symptoms, 
            test_codes
        )
        for line in explanation:
            print(line)
    
    print("\n" + "-" * 60)
    print("Test 3: Get All Faults")
    print("-" * 60)
    
    all_faults = engine.get_all_faults()
    print(f"Total faults in KB: {len(all_faults)}")
    
    # Group by domain
    domains = {}
    for f in all_faults:
        d = f['domain']
        domains[d] = domains.get(d, 0) + 1
    
    print("By domain:")
    for domain, count in sorted(domains.items()):
        print(f"  - {domain}: {count}")
    
    print("\n" + "-" * 60)
    print("Test 4: Resolution Workflow")
    print("-" * 60)
    
    if results:
        workflow = engine.get_resolution_workflow(results[0]['fault_id'])
        print(f"Fault: {workflow['title']}")
        print(f"Complexity: {workflow['complexity']}")
        print(f"Estimated time: {workflow['estimated_time']}")
        print(f"Required role: {workflow['required_role']}")
        print("Steps:")
        for step in workflow['steps']:
            print(f"  {step['step_number']}. {step['action']}")
    
    print("\n" + "=" * 60)
    print("Test suite complete!")
    print("=" * 60)
