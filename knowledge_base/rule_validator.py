import json
from pathlib import Path
from rule_loader import RuleLoader

class RuleValidator:
    """Validates Knowledge Base data against schema and logical constraints."""

    def __init__(self):
        self.loader = RuleLoader()

    def validate_all(self):
        """Runs all validations."""
        profiles = self.loader.load_fault_profiles()
        rules = self.loader.load_rules()

        errors = []
        errors.extend(self.validate_profiles(profiles))
        errors.extend(self.validate_rules(rules, profiles))

        return errors

    def validate_profiles(self, profiles):
        """Checks for missing fields and duplicate IDs in profiles."""
        errors = []
        seen_ids = set()
        required_fields = ["fault_id", "domain", "title", "severity", "resolution_steps"]

        for p in profiles:
            fid = p.get("fault_id")
            if not fid:
                errors.append("Profile missing fault_id")
                continue
            
            if fid in seen_ids:
                errors.append(f"Duplicate fault_id found: {fid}")
            seen_ids.add(fid)

            for field in required_fields:
                if field not in p:
                    errors.append(f"Profile {fid} missing required field: {field}")

        return errors

    def validate_rules(self, rules, profiles):
        """Checks for rule structure and references to non-existent faults."""
        errors = []
        seen_ids = set()
        profile_ids = {p["fault_id"] for p in profiles}
        required_fields = ["rule_id", "conditions", "actions"]

        for r in rules:
            rid = r.get("rule_id")
            if not rid:
                errors.append("Rule missing rule_id")
                continue
            
            if rid in seen_ids:
                errors.append(f"Duplicate rule_id found: {rid}")
            seen_ids.add(rid)

            for field in required_fields:
                if field not in r:
                    errors.append(f"Rule {rid} missing required field: {field}")

            # Check actions for diagnosis assertions
            for action in r.get("actions", []):
                if action.get("fact") == "diagnosis":
                    val = action.get("value")
                    if val not in profile_ids:
                        errors.append(f"Rule {rid} asserts unknown diagnosis: {val}")

        return errors

if __name__ == "__main__":
    validator = RuleValidator()
    errors = validator.validate_all()
    
    if not errors:
        print("Knowledge Base validation successful! No errors found.")
    else:
        print(f"Validation failed with {len(errors)} errors:")
        for err in errors:
            print(f"  - {err}")
