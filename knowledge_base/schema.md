# Knowledge Base Schema Spec (Prolog)

This document defines the Prolog predicates used for **Fault Profiles** and **Diagnostic Rules** in the ATM-Expert system.

## 1. Fault Profiles

Fault profiles are represented as Prolog facts in `knowledge_base/atm_kb.pl`.

### Predicates

| Predicate | Arity | Description |
|---|---|---|
| `fault_profile/5` | `(ID, Domain, Subdomain, Title, Severity)` | Core identity of a fault. |
| `fault_description/2` | `(ID, Description)` | Detailed explanation of the fault. |
| `has_error_code/2` | `(ID, Code)` | Associated vendor-specific codes. |
| `has_symptom/2` | `(ID, Symptom)` | Observed behaviors that trigger this fault. |
| `has_cause/2` | `(ID, Cause)` | Potential root causes for the fault. |
| `resolution_step/3` | `(ID, Order, Step)` | Ordered list of recovery actions. |

### Example Fact Set

```prolog
fault_profile('HW_001', 'Hardware', 'Card Reader', 'Card Reader Jam', 'HIGH').
fault_description('HW_001', 'Physical obstruction in the card reader.').
has_error_code('HW_001', '3A1').
has_symptom('HW_001', 'Card not ejected').
resolution_step('HW_001', 1, 'Take ATM out of service').
```

---

## 2. Diagnostic Rules

Rules are implemented as Prolog predicates that perform logical matching between observations (symptoms/error codes) and fault profiles.

### Key Predicates

| Predicate | Usage | Description |
|---|---|---|
| `diagnose/2` | `diagnose(FID, Observations)` | Matches a list of observations (symptom/1 or error_code/1) to a fault. |
| `match_observation/2`| `match_observation(FID, Obs)` | Helper that matches single observations against KB facts (handles atoms and strings). |
| `get_fault_details/7`| `get_fault_details(FID, D, SD, T, S, Desc, RS)` | Retrieves all metadata and resolution steps for a specific Fault ID. |

### Example Query

```prolog
?- diagnose(FID, [symptom("Card not ejected"), error_code("3A1")]).
% FID = 'HW_001'
```
