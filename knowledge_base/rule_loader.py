import json
import os
from pathlib import Path

class RuleLoader:
    """Loads ATM fault profiles and inference rules from JSON files."""

    def __init__(self, base_path=None):
        if base_path is None:
            # Default to the directory where this script is located
            self.base_path = Path(__file__).parent
        else:
            self.base_path = Path(base_path)

    def load_fault_profiles(self):
        """Loads all fault profiles from the fault_profiles directory."""
        profiles = []
        profile_dir = self.base_path / "fault_profiles"
        
        if not profile_dir.exists():
            print(f"Warning: Profile directory {profile_dir} not found.")
            return profiles

        for file_path in profile_dir.glob("*.json"):
            try:
                with open(file_path, 'r') as f:
                    data = json.load(f)
                    if isinstance(data, list):
                        profiles.extend(data)
                    else:
                        profiles.append(data)
            except Exception as e:
                print(f"Error loading {file_path}: {e}")
        
        return profiles

    def load_rules(self):
        """Loads all inference rules from the rules directory."""
        rules = []
        rules_dir = self.base_path / "rules"
        
        if not rules_dir.exists():
            print(f"Warning: Rules directory {rules_dir} not found.")
            return rules

        for file_path in rules_dir.glob("*.json"):
            try:
                with open(file_path, 'r') as f:
                    data = json.load(f)
                    if isinstance(data, list):
                        rules.extend(data)
                    else:
                        rules.append(data)
            except Exception as e:
                print(f"Error loading {file_path}: {e}")
        
        return rules

if __name__ == "__main__":
    loader = RuleLoader()
    profiles = loader.load_fault_profiles()
    rules = loader.load_rules()
    
    print(f"Loaded {len(profiles)} fault profiles.")
    print(f"Loaded {len(rules)} inference rules.")
