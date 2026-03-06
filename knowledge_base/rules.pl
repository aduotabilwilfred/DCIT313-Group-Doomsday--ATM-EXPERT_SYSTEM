% ATM Expert Diagnostic Rules
% This file contains the logic for diagnosing faults and retrieving details.
% Developer 1 (Inference Engine) & Developer 2 (Knowledge Base) collaboration

% =============================================================================
% CORE DIAGNOSIS PREDICATES
% =============================================================================

% Match a fault based on a list of observations.
% Observations can be symptom(S) or error_code(C)
diagnose(FaultID, Observations) :-
    fault_profile(FaultID, _, _, _, _),
    findall(Obs, (member(Obs, Observations), match_observation(FaultID, Obs)), Matches),
    Matches \= []. % At least one match

% Diagnose with confidence score (returns match count)
diagnose_with_confidence(FaultID, Observations, MatchCount) :-
    fault_profile(FaultID, _, _, _, _),
    findall(Obs, (member(Obs, Observations), match_observation(FaultID, Obs)), Matches),
    Matches \= [],
    length(Matches, MatchCount).

% Get all diagnoses ranked by confidence (highest match count first)
diagnose_ranked(Observations, RankedResults) :-
    findall(
        count_fault(Count, FID),
        diagnose_with_confidence(FID, Observations, Count),
        Unranked
    ),
    sort(0, @>=, Unranked, RankedResults).

% Helper to match observations (handles atoms and strings)
match_observation(FaultID, symptom(S)) :-
    (atom(S) -> has_symptom(FaultID, S) ; (string(S), atom_string(SA, S), has_symptom(FaultID, SA))).
match_observation(FaultID, error_code(C)) :-
    (atom(C) -> has_error_code(FaultID, C) ; (string(C), atom_string(CA, C), has_error_code(FaultID, CA))).

% =============================================================================
% FAULT DETAIL RETRIEVAL
% =============================================================================

% Get full details for a fault
get_fault_details(FaultID, Domain, Subdomain, Title, Severity, Description, ResolutionSteps) :-
    fault_profile(FaultID, Domain, Subdomain, Title, Severity),
    fault_description(FaultID, Description),
    findall(Step, resolution_step(FaultID, _, Step), ResolutionSteps).

% Get resolution steps in order
get_resolution_steps(FaultID, OrderedSteps) :-
    findall(Order-Step, resolution_step(FaultID, Order, Step), Pairs),
    keysort(Pairs, Sorted),
    pairs_values(Sorted, OrderedSteps).

% Get all causes for a fault
get_causes(FaultID, Causes) :-
    findall(Cause, has_cause(FaultID, Cause), Causes).

% Get all symptoms for a fault
get_symptoms(FaultID, Symptoms) :-
    findall(Symptom, has_symptom(FaultID, Symptom), Symptoms).

% Get all error codes for a fault
get_error_codes(FaultID, Codes) :-
    findall(Code, has_error_code(FaultID, Code), Codes).

% =============================================================================
% SEVERITY-BASED FILTERING
% =============================================================================

% Define severity order
severity_rank('LOW', 1).
severity_rank('MEDIUM', 2).
severity_rank('HIGH', 3).
severity_rank('CRITICAL', 4).

% Compare severity levels
severity_at_least(FaultSeverity, MinSeverity) :-
    severity_rank(FaultSeverity, FRank),
    severity_rank(MinSeverity, MRank),
    FRank >= MRank.

% Diagnose with minimum severity filter
diagnose_min_severity(FaultID, Observations, MinSeverity) :-
    diagnose(FaultID, Observations),
    fault_profile(FaultID, _, _, _, Severity),
    severity_at_least(Severity, MinSeverity).

% =============================================================================
% DOMAIN-BASED QUERIES
% =============================================================================

% Get faults by domain
faults_by_domain(Domain, FaultIDs) :-
    findall(FID, fault_profile(FID, Domain, _, _, _), FaultIDs).

% Get faults by subdomain
faults_by_subdomain(Subdomain, FaultIDs) :-
    findall(FID, fault_profile(FID, _, Subdomain, _, _), FaultIDs).

% Get faults by severity
faults_by_severity(Severity, FaultIDs) :-
    findall(FID, fault_profile(FID, _, _, _, Severity), FaultIDs).

% =============================================================================
% PREDICTIVE MAINTENANCE RULES
% =============================================================================

% Component usage threshold rules (for predictive maintenance)
% These can be extended with actual sensor data integration

% Predict failure risk based on usage cycles
predict_failure_risk(Component, high) :-
    Component = card_reader,
    % High risk if cycles exceed threshold (example: 100000)
    true. % Placeholder for actual sensor integration

predict_failure_risk(Component, medium) :-
    Component = cash_dispenser,
    true. % Placeholder

% Components requiring preventive maintenance
needs_maintenance(Component, Reason) :-
    Component = card_reader,
    Reason = 'High cycle count detected'.

needs_maintenance(Component, Reason) :-
    Component = receipt_printer,
    Reason = 'Paper supply low'.

% =============================================================================
% FRAUD DETECTION SUPPORT
% =============================================================================

% Fraud pattern detection (for security integration)
% These patterns coordinate with Dev 4's security rules

% Check if observations indicate potential fraud
is_fraud_indicator(symptom('Skimmer detected')).
is_fraud_indicator(symptom('PIN pad tampering')).
is_fraud_indicator(symptom('Unusual card activity')).
is_fraud_indicator(error_code('SEC001')).
is_fraud_indicator(error_code('SEC002')).
is_fraud_indicator(error_code('SEC003')).

% Check if any observation is a fraud indicator
has_fraud_indicators(Observations) :-
    member(Obs, Observations),
    is_fraud_indicator(Obs),
    !.

% Diagnose security faults specifically
diagnose_security(FaultID, Observations) :-
    diagnose(FaultID, Observations),
    fault_profile(FaultID, 'Security', _, _, _).

% =============================================================================
% EXPLANATION GENERATION SUPPORT
% =============================================================================

% Generate explanation data for a diagnosis
explain_match(FaultID, Observation, Explanation) :-
    Observation = symptom(S),
    match_observation(FaultID, Observation),
    atom_concat('Symptom matched: ', S, Explanation).

explain_match(FaultID, Observation, Explanation) :-
    Observation = error_code(C),
    match_observation(FaultID, Observation),
    atom_concat('Error code matched: ', C, Explanation).

% Get all explanations for a diagnosis
get_diagnosis_explanations(FaultID, Observations, Explanations) :-
    findall(Exp, (member(Obs, Observations), explain_match(FaultID, Obs, Exp)), Explanations).

% =============================================================================
% TEST PREDICATES
% =============================================================================

% Test predicate for verification
test_diagnose(FaultID) :-
    diagnose(FaultID, [symptom('Card not ejected'), error_code('3A1')]).

% Test confidence scoring
test_confidence(FaultID, Count) :-
    diagnose_with_confidence(FaultID, [symptom('Card not ejected'), error_code('3A1')], Count).

% Test ranking
test_ranking(Results) :-
    diagnose_ranked([symptom('Card not ejected'), error_code('3A1')], Results).
