import json
import os
from pathlib import Path

def sanitize(text):
    """Sanitize text for Prolog atoms."""
    if not text:
        return ""
    return text.replace("'", "''").replace("\n", " ")

def json_to_prolog():
    kb_path = Path("knowledge_base")
    profiles_dir = kb_path / "fault_profiles"
    output_file = kb_path / "atm_kb.pl"

    facts = []
    
    # Header
    facts.append("% ATM Expert Knowledge Base - Generated from JSON")
    facts.append(":- dynamic fault_profile/5.")
    facts.append(":- dynamic fault_description/2.")
    facts.append(":- dynamic has_error_code/2.")
    facts.append(":- dynamic has_symptom/2.")
    facts.append(":- dynamic has_cause/2.")
    facts.append(":- dynamic resolution_step/3.")
    facts.append("")
    facts.append(":- discontiguous fault_profile/5.")
    facts.append(":- discontiguous fault_description/2.")
    facts.append(":- discontiguous has_error_code/2.")
    facts.append(":- discontiguous has_symptom/2.")
    facts.append(":- discontiguous has_cause/2.")
    facts.append(":- discontiguous resolution_step/3.")
    facts.append("")

    for json_file in profiles_dir.glob("*.json"):
        with open(json_file, 'r') as f:
            profiles = json.load(f)
            for p in profiles:
                fid = p['fault_id']
                domain = p['domain']
                sub_domain = p['sub_domain']
                title = sanitize(p['title'])
                desc = sanitize(p['description'])
                severity = p['severity']

                facts.append(f"fault_profile('{fid}', '{domain}', '{sub_domain}', '{title}', '{severity}').")
                facts.append(f"fault_description('{fid}', '{desc}').")

                for code in p.get('error_codes', []):
                    facts.append(f"has_error_code('{fid}', '{code}').")

                for symptom in p.get('symptoms', []):
                    facts.append(f"has_symptom('{fid}', '{sanitize(symptom)}').")

                for cause in p.get('causes', []):
                    facts.append(f"has_cause('{fid}', '{sanitize(cause)}').")

                for i, step in enumerate(p.get('resolution_steps', [])):
                    facts.append(f"resolution_step('{fid}', {i+1}, '{sanitize(step)}').")
                
                facts.append("")

    # Append Diagnostic Rules
    facts.append("")
    facts.append("% --- Diagnostic Rules ---")
    facts.append("")
    facts.append("% Match a fault based on a list of observations.")
    facts.append("% Observations can be symptom(S) or error_code(C)")
    facts.append("diagnose(FaultID, Observations) :-")
    facts.append("    fault_profile(FaultID, _, _, _, _),")
    facts.append("    findall(Obs, (member(Obs, Observations), match_observation(FaultID, Obs)), Matches),")
    facts.append("    Matches \\= []. % At least one match")
    facts.append("")
    facts.append("% Helper to match observations (handles atoms and strings)")
    facts.append("match_observation(FaultID, symptom(S)) :-")
    facts.append("    (atom(S) -> has_symptom(FaultID, S) ; (string(S), atom_string(SA, S), has_symptom(FaultID, SA))).")
    facts.append("match_observation(FaultID, error_code(C)) :-")
    facts.append("    (atom(C) -> has_error_code(FaultID, C) ; (string(C), atom_string(CA, C), has_error_code(FaultID, CA))).")
    facts.append("")
    facts.append("% Get full details for a fault")
    facts.append("get_fault_details(FaultID, Domain, Subdomain, Title, Severity, Description, ResolutionSteps) :-")
    facts.append("    fault_profile(FaultID, Domain, Subdomain, Title, Severity),")
    facts.append("    fault_description(FaultID, Description),")
    facts.append("    findall(Step, resolution_step(FaultID, _, Step), ResolutionSteps).")
    facts.append("")
    facts.append("% Test predicate for verification")
    facts.append("test_diagnose(FaultID) :-")
    facts.append("    diagnose(FaultID, [symptom('Card not ejected'), error_code('3A1')]).")
    facts.append("")

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("\n".join(facts))
    
    print(f"Successfully generated {output_file}")

if __name__ == "__main__":
    json_to_prolog()
