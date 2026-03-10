import json
import os
from pathlib import Path

# Try to import the inference engine
try:
    import sys
    sys.path.append(str(Path(__file__).parent.parent))
    from inference_engine.prolog_bridge import PrologInferenceEngine
    ENGINE_AVAILABLE = True
except ImportError:
    ENGINE_AVAILABLE = False

class ATMSimulator:
    def __init__(self, profiles_dir=None):
        if profiles_dir is None:
            self.profiles_dir = Path(__file__).parent.parent / "knowledge_base" / "fault_profiles"
        else:
            self.profiles_dir = Path(profiles_dir)
        
        self.faults = {}
        self._load_profiles()
        
        # Initialize Inference Engine
        self.engine = None
        if ENGINE_AVAILABLE:
            try:
                self.engine = PrologInferenceEngine()
                print(f"✓ Inference Engine integrated successfully.")
            except Exception as e:
                print(f"⚠ Warning: Could not initialize Inference Engine: {e}")
        else:
            print(f"⚠ Warning: Inference Engine module not found. Diagnosis will be offline.")

        if self.faults:
            print(f"✓ Total of {len(self.faults)} fault profiles loaded from: {self.profiles_dir}")
        else:
            print(f"⚠ Warning: No fault profiles found in {self.profiles_dir}")

    def _load_profiles(self):
        """Load all fault profiles from JSON files."""
        for json_file in self.profiles_dir.glob("*.json"):
            try:
                with open(json_file, 'r') as f:
                    profiles = json.load(f)
                    for p in profiles:
                        self.faults[p['fault_id']] = p
            except Exception as e:
                print(f"Error loading {json_file.name}: {e}")

    def list_faults(self):
        """List all available faults organized by domain."""
        print("\n--- Available ATM Fault Scenarios ---")
        domains = {}
        for fid, data in self.faults.items():
            domain = data.get('domain', 'Unknown')
            if domain not in domains:
                domains[domain] = []
            domains[domain].append((fid, data.get('title', 'No Title')))

        for domain, items in sorted(domains.items()):
            print(f"\n[{domain}]")
            for fid, title in sorted(items):
                print(f"  {fid}: {title}")

    def simulate(self, fault_id):
        """Simulate a specific fault by outputting its characteristic 'signals'."""
        if fault_id not in self.faults:
            print(f"Error: Fault ID '{fault_id}' not found.")
            return

        fault = self.faults[fault_id]
        print(f"\n>>> SIMULATING FAULT: {fault.get('title')} ({fault_id})")
        print("-" * 50)
        
        # Simulated Hardware Signals
        error_codes = fault.get('error_codes', [])
        symptoms = fault.get('symptoms', [])

        print(f"EMITTING HARDWARE SIGNALS:")
        for code in error_codes:
            print(f"  [SIGNAL] ERROR_CODE: {code}")
        for symptom in symptoms:
            print(f"  [SIGNAL] SYMPTOM:    {symptom}")
        
        print("-" * 50)
        print("Simulator: Signals injected.")
        
        if self.engine:
            print("Simulator: Running REAL-TIME Inference Engine diagnosis...")
            results = self.engine.diagnose(symptoms=symptoms, error_codes=error_codes)
            
            if results:
                print(f"\n✅ Diagnostic Match Found: {results[0]['title']} (Confidence: {results[0]['confidence']})")
                print("-" * 30)
                explanation = self.engine.explain_diagnosis(results[0]['fault_id'], symptoms, error_codes)
                for line in explanation:
                    print(line)
                
                print("\nREMEDIATION WORKFLOW:")
                workflow = self.engine.get_resolution_workflow(results[0]['fault_id'])
                for step in workflow['steps']:
                    print(f"  {step['step_number']}. {step['action']}")
            else:
                print("\n✗ No clear diagnosis found in Knowledge Base for these signals.")
        else:
            print("Simulator: [OFFLINE MODE] Inference Engine not connected. Cannot perform diagnosis.")
        
        print("-" * 50)

def main():
    try:
        simulator = ATMSimulator()
        
        while True:
            simulator.list_faults()
            print("\nEnter a Fault ID to simulate (or 'q' to quit):")
            choice = input("> ").strip().upper()
            
            if choice == 'Q':
                break
            
            simulator.simulate(choice)
            print("\nPress Enter to continue...")
            input()
    except KeyboardInterrupt:
        print("\n\nExiting simulator. Goodbye!")

if __name__ == "__main__":
    main()
