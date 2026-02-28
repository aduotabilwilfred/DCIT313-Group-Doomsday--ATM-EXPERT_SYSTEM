from rule_loader import RuleLoader
from rule_validator import RuleValidator

def main():
    """Seeds and validates the ATM-Expert Knowledge Base."""
    print("--- ATM-Expert Knowledge Base Seeding ---")
    
    # 1. Validate the existing data
    validator = RuleValidator()
    errors = validator.validate_all()
    
    if errors:
        print(f"Aborting: Knowledge Base contains {len(errors)} errors.")
        for err in errors:
            print(f"  - {err}")
        return

    # 2. Load the data to show summary
    loader = RuleLoader()
    profiles = loader.load_fault_profiles()
    rules = loader.load_rules()
    
    print("Success: Knowledge Base is valid and ready.")
    print(f"\nSummary:")
    print(f"  Fault Profiles: {len(profiles)}")
    print(f"  Inference Rules: {len(rules)}")
    
    # Domain breakdown
    domains = {}
    for p in profiles:
        dom = p.get("domain", "Unknown")
        domains[dom] = domains.get(dom, 0) + 1
    
    print("\nProfiles by Domain:")
    for dom, count in domains.items():
        print(f"  - {dom}: {count}")

if __name__ == "__main__":
    main()
