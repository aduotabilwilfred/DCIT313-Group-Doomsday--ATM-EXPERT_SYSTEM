import subprocess
import re
from pathlib import Path

class PrologInferenceEngine:
    def __init__(self, kb_path=None):
        if kb_path is None:
            # Default to the master KB loader
            kb_path = Path(__file__).parent.parent / "knowledge_base" / "loader.pl"
        self.kb_path = kb_path

    def _query(self, query_str):
        """Run a Prolog query via CLI and return the output."""
        try:
            # -q to suppress welcome message
            # -s to load file
            # -g for goal
            # -t halt to exit after goal
            cmd = [
                "swipl", "-q", "-s", str(self.kb_path),
                "-g", query_str, "-t", "halt"
            ]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=5)
            return result.stdout.strip()
        except subprocess.TimeoutExpired:
            return "ERROR: Query timed out"
        except Exception as e:
            return f"ERROR: {str(e)}"

    def diagnose(self, symptoms=None, error_codes=None):
        """Diagnose faults based on symptoms and error codes."""
        observations = []
        if symptoms:
            for s in symptoms:
                observations.append(f"symptom('{s.replace("'", "''")}')")
        if error_codes:
            for c in error_codes:
                observations.append(f"error_code('{c.replace("'", "''")}')")
        
        obs_list = "[" + ", ".join(observations) + "]"
        # We use write_canonical or writeq to get easily parsable output
        query = f"diagnose(FID, {obs_list}), writeln(FID), fail"
        
        output = self._query(query)
        if output.startswith("ERROR"):
            return []
        
        # Split output by lines and filter empty
        fids = [line.strip() for line in output.split("\n") if line.strip()]
        return list(set(fids)) # Unique FIDs

    def get_details(self, fault_id):
        """Get full details for a specific fault ID."""
        # Using write_canonical to ensure strings are quoted correctly for parsing
        query = f"get_fault_details('{fault_id}', D, SD, T, S, Desc, RS), format('~w|~w|~w|~w|~w|~w', [D, SD, T, S, Desc, RS])"
        output = self._query(query)
        
        if output.startswith("ERROR") or not output:
            return None
            
        parts = output.split("|")
        if len(parts) < 6:
            return None
            
        return {
            "fault_id": fault_id,
            "domain": parts[0],
            "sub_domain": parts[1],
            "title": parts[2],
            "severity": parts[3],
            "description": parts[4],
            "resolution_steps": parts[5] # This will be string representation of list
        }

if __name__ == "__main__":
    # Quick test
    engine = PrologInferenceEngine()
    print("Testing diagnosis for 'Card not ejected' and '3A1'...")
    results = engine.diagnose(symptoms=["Card not ejected"], error_codes=["3A1"])
    print(f"Diagnosed Faults: {results}")
    
    if results:
        print(f"\nDetails for {results[0]}:")
        print(engine.get_details(results[0]))
