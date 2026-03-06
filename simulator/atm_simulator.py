import json
import os
from pathlib import Path

class ATMSimulator:
    def __init__(self, profiles_dir=None):
        if profiles_dir is None:
            self.profiles_dir = Path(__file__).parent.parent / "knowledge_base" / "fault_profiles"
        else:
            self.profiles_dir = Path(profiles_dir)
        self.faults = {}
        self._load_profiles()

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
        print("Simulator: Signals injected. Awaiting Inference Engine diagnosis...")

def main():
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

if __name__ == "__main__":
    main()
