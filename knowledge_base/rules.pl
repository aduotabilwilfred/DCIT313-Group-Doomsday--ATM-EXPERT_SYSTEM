% ATM Expert Diagnostic Rules
% This file contains the logic for diagnosing faults and retrieving details.

% Match a fault based on a list of observations.
% Observations can be symptom(S) or error_code(C)
diagnose(FaultID, Observations) :-
    fault_profile(FaultID, _, _, _, _),
    findall(Obs, (member(Obs, Observations), match_observation(FaultID, Obs)), Matches),
    Matches \= []. % At least one match

% Helper to match observations (handles atoms and strings)
match_observation(FaultID, symptom(S)) :-
    (atom(S) -> has_symptom(FaultID, S) ; (string(S), atom_string(SA, S), has_symptom(FaultID, SA))).
match_observation(FaultID, error_code(C)) :-
    (atom(C) -> has_error_code(FaultID, C) ; (string(C), atom_string(CA, C), has_error_code(FaultID, CA))).

% Get full details for a fault
get_fault_details(FaultID, Domain, Subdomain, Title, Severity, Description, ResolutionSteps) :-
    fault_profile(FaultID, Domain, Subdomain, Title, Severity),
    fault_description(FaultID, Description),
    findall(Step, resolution_step(FaultID, _, Step), ResolutionSteps).

% Test predicate for verification
test_diagnose(FaultID) :-
    diagnose(FaultID, [symptom('Card not ejected'), error_code('3A1')]).
