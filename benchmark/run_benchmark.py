"""
ATM Expert Benchmark Runner
Developer 1: Shadrack Dorkenoo

Evaluates the inference engine's diagnostic accuracy against 
200 pre-labelled ATM fault scenarios.

Target accuracy: >= 85%
"""

import json
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))
from inference_engine.prolog_bridge import PrologInferenceEngine


class BenchmarkRunner:
    """Runs benchmark scenarios against the inference engine."""
    
    def __init__(self, scenarios_path: Path = None, results_path: Path = None):
        self.scenarios_path = scenarios_path or (
            Path(__file__).parent / "atm_benchmark_scenarios.json"
        )
        self.results_path = results_path or (
            Path(__file__).parent / "benchmark_results.json"
        )
        self.engine = PrologInferenceEngine()
        
    def load_scenarios(self) -> List[Dict]:
        """Load benchmark scenarios from JSON file."""
        with open(self.scenarios_path, 'r') as f:
            data = json.load(f)
        return data.get('scenarios', [])
    
    def run_scenario(self, scenario: Dict) -> Dict[str, Any]:
        """
        Run a single benchmark scenario.
        
        Returns:
            Result dict with scenario_id, expected, actual, and match status
        """
        scenario_id = scenario.get('scenario_id', 'UNKNOWN')
        expected_diagnosis = scenario.get('expected_diagnosis', '')
        expected_severity = scenario.get('expected_severity', '')
        
        # Extract observations
        error_codes = scenario.get('error_codes', [])
        symptoms = self._extract_symptoms(scenario)
        
        # Run diagnosis
        try:
            diagnoses = self.engine.diagnose_fast(
                symptoms=symptoms,
                error_codes=error_codes
            )
        except Exception as e:
            return {
                'scenario_id': scenario_id,
                'status': 'ERROR',
                'error': str(e),
                'expected_diagnosis': expected_diagnosis,
                'actual_diagnosis': None,
                'matched': False
            }
        
        # Check for match
        primary_diagnosis = diagnoses[0] if diagnoses else None
        
        # Try to match by title (case-insensitive)
        matched = False
        matched_diagnosis = None
        
        for diag in diagnoses:
            if diag['title'].lower() == expected_diagnosis.lower():
                matched = True
                matched_diagnosis = diag
                break
        
        # If no exact match, check if expected is in top 3
        top_3_match = False
        if not matched and len(diagnoses) >= 1:
            for diag in diagnoses[:3]:
                if expected_diagnosis.lower() in diag['title'].lower():
                    top_3_match = True
                    break
        
        return {
            'scenario_id': scenario_id,
            'domain': scenario.get('domain', ''),
            'status': 'OK',
            'expected_diagnosis': expected_diagnosis,
            'expected_severity': expected_severity,
            'actual_diagnosis': primary_diagnosis['title'] if primary_diagnosis else None,
            'actual_severity': primary_diagnosis['severity'] if primary_diagnosis else None,
            'confidence': primary_diagnosis.get('confidence', 0) if primary_diagnosis else 0,
            'matched': matched,
            'top_3_match': matched or top_3_match,
            'total_diagnoses': len(diagnoses),
            'observations_used': {
                'symptoms': symptoms,
                'error_codes': error_codes
            }
        }
    
    def _extract_symptoms(self, scenario: Dict) -> List[str]:
        """Extract symptoms from scenario sensor readings and transaction context."""
        symptoms = []
        
        sensor_readings = scenario.get('sensor_readings', {})
        tx_context = scenario.get('transaction_context', {})
        
        # Map sensor readings to symptom strings
        status_fields = [
            ('card_reader_status', 'Reader status'),
            ('printer_status', 'Printer status'),
            ('dispenser_status', 'Dispenser status'),
            ('pin_pad_status', 'PIN pad status'),
        ]
        
        for field, prefix in status_fields:
            if field in sensor_readings:
                value = sensor_readings[field]
                if value and value not in ['OK', 'NORMAL', 'READY']:
                    symptoms.append(f"{prefix}: {value}")
        
        # Map specific sensor conditions
        if sensor_readings.get('card_present_sensor') == 'STUCK':
            symptoms.append('Card not ejected')
        
        if sensor_readings.get('network_status') == 'DOWN':
            symptoms.append('Network connection lost')
        
        if sensor_readings.get('cash_level_pct', 100) == 0:
            symptoms.append("'Out of Cash' screen")
        
        # Map transaction errors
        error_map = {
            'CARD_NOT_EJECTED': 'Card not ejected',
            'DISPENSE_FAILED': 'Dispense attempt fails',
            'RECEIPT_NOT_PRINTED': 'Receipt not printed',
            'NETWORK_TIMEOUT': 'Network timeout',
            'CARD_READ_ERROR': 'Intermittent read failures',
            'TRANSACTION_TIMEOUT': 'Transaction timeout',
            'PIN_ENTRY_FAILURE': 'PIN entry failed',
            'BALANCE_INQUIRY_FAILED': 'Balance inquiry failed',
        }
        
        last_error = tx_context.get('last_error', '')
        if last_error in error_map:
            symptoms.append(error_map[last_error])
        
        return symptoms
    
    def run_all(self) -> Dict[str, Any]:
        """
        Run all benchmark scenarios.
        
        Returns:
            Summary results with accuracy metrics
        """
        scenarios = self.load_scenarios()
        total = len(scenarios)
        
        print(f"Running {total} benchmark scenarios...")
        print("=" * 60)
        
        results = []
        correct = 0
        top_3_correct = 0
        errors = 0
        
        domain_stats = {}
        severity_stats = {}
        
        for i, scenario in enumerate(scenarios):
            result = self.run_scenario(scenario)
            results.append(result)
            
            # Track statistics
            if result['status'] == 'ERROR':
                errors += 1
            elif result['matched']:
                correct += 1
                top_3_correct += 1
            elif result.get('top_3_match'):
                top_3_correct += 1
            
            # Domain breakdown
            domain = result.get('domain', 'Unknown')
            if domain not in domain_stats:
                domain_stats[domain] = {'total': 0, 'correct': 0}
            domain_stats[domain]['total'] += 1
            if result['matched']:
                domain_stats[domain]['correct'] += 1
            
            # Severity breakdown
            severity = result.get('expected_severity', 'Unknown')
            if severity not in severity_stats:
                severity_stats[severity] = {'total': 0, 'correct': 0}
            severity_stats[severity]['total'] += 1
            if result['matched']:
                severity_stats[severity]['correct'] += 1
            
            # Progress indicator
            if (i + 1) % 20 == 0:
                print(f"  Processed {i + 1}/{total} scenarios...")
        
        # Calculate accuracy
        accuracy = (correct / total * 100) if total > 0 else 0
        top_3_accuracy = (top_3_correct / total * 100) if total > 0 else 0
        
        # Build summary
        summary = {
            'timestamp': datetime.now().isoformat(),
            'total_scenarios': total,
            'exact_matches': correct,
            'top_3_matches': top_3_correct,
            'errors': errors,
            'accuracy_exact': round(accuracy, 2),
            'accuracy_top_3': round(top_3_accuracy, 2),
            'target_accuracy': 85.0,
            'target_met': accuracy >= 85.0,
            'domain_breakdown': {
                domain: {
                    'total': stats['total'],
                    'correct': stats['correct'],
                    'accuracy': round(stats['correct'] / stats['total'] * 100, 2) if stats['total'] > 0 else 0
                }
                for domain, stats in domain_stats.items()
            },
            'severity_breakdown': {
                sev: {
                    'total': stats['total'],
                    'correct': stats['correct'],
                    'accuracy': round(stats['correct'] / stats['total'] * 100, 2) if stats['total'] > 0 else 0
                }
                for sev, stats in severity_stats.items()
            },
            'detailed_results': results
        }
        
        return summary
    
    def print_summary(self, summary: Dict):
        """Print a formatted summary of benchmark results."""
        print("\n" + "=" * 60)
        print("BENCHMARK RESULTS SUMMARY")
        print("=" * 60)
        
        print(f"\nTotal Scenarios: {summary['total_scenarios']}")
        print(f"Exact Matches:   {summary['exact_matches']}")
        print(f"Top-3 Matches:   {summary['top_3_matches']}")
        print(f"Errors:          {summary['errors']}")
        
        print(f"\n{'ACCURACY':=^60}")
        print(f"  Exact Match Accuracy: {summary['accuracy_exact']:.1f}%")
        print(f"  Top-3 Accuracy:       {summary['accuracy_top_3']:.1f}%")
        print(f"  Target:               {summary['target_accuracy']:.1f}%")
        
        status = "✓ PASSED" if summary['target_met'] else "✗ BELOW TARGET"
        print(f"\n  Status: {status}")
        
        print(f"\n{'BY DOMAIN':=^60}")
        for domain, stats in sorted(summary['domain_breakdown'].items()):
            print(f"  {domain:20} {stats['correct']:3}/{stats['total']:3} ({stats['accuracy']:5.1f}%)")
        
        print(f"\n{'BY SEVERITY':=^60}")
        for severity in ['LOW', 'MEDIUM', 'HIGH', 'CRITICAL']:
            if severity in summary['severity_breakdown']:
                stats = summary['severity_breakdown'][severity]
                print(f"  {severity:20} {stats['correct']:3}/{stats['total']:3} ({stats['accuracy']:5.1f}%)")
        
        # Show some failures for analysis
        failures = [r for r in summary['detailed_results'] if not r.get('matched') and r['status'] != 'ERROR']
        if failures:
            print(f"\n{'SAMPLE MISMATCHES (first 5)':=^60}")
            for fail in failures[:5]:
                print(f"\n  Scenario: {fail['scenario_id']}")
                print(f"    Expected: {fail['expected_diagnosis']}")
                print(f"    Got:      {fail['actual_diagnosis'] or 'No diagnosis'}")
                if fail.get('observations_used'):
                    print(f"    Symptoms: {fail['observations_used'].get('symptoms', [])[:2]}")
        
        print("\n" + "=" * 60)
    
    def save_results(self, summary: Dict):
        """Save detailed results to JSON file."""
        with open(self.results_path, 'w') as f:
            json.dump(summary, f, indent=2)
        print(f"\nDetailed results saved to: {self.results_path}")


def main():
    """Main entry point for benchmark runner."""
    print("ATM Expert - Inference Engine Benchmark")
    print("=" * 60)
    
    runner = BenchmarkRunner()
    
    try:
        summary = runner.run_all()
        runner.print_summary(summary)
        runner.save_results(summary)
        
        # Exit with appropriate code
        if summary['target_met']:
            sys.exit(0)
        else:
            sys.exit(1)
            
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
