# Knowledge Base Schema Spec

This document defines the JSON structure for **Fault Profiles** and **Inference Rules** used by the ATM-Expert system.

## 1. Fault Profiles

Fault profiles represent the canonical definition of a specific ATM issue.

**Path:** `knowledge_base/fault_profiles/*.json`

| Field | Type | Description |
|---|---|---|
| `fault_id` | String | Unique identifier (e.g., `HW_001`, `SW_002`) |
| `domain` | String | One of: `Hardware`, `Software`, `Network`, `Cash Handling`, `Security` |
| `sub_domain` | String | Specific component (e.g., `Card Reader`, `VPN`) |
| `title` | String | Human-readable name of the fault |
| `description` | String | Detailed explanation of the fault |
| `severity` | String | `LOW`, `MEDIUM`, `HIGH`, `CRITICAL` |
| `error_codes` | Array[String] | Vendor-specific codes associated with this fault |
| `symptoms` | Array[String] | Observables (e.g., "dispenser shutter stuck") |
| `causes` | Array[String] | Potential root causes |
| `resolution_steps` | Array[String] | Ordered list of actions to resolve the fault |

### Example Fault Profile

```json
{
  "fault_id": "HW_001",
  "domain": "Hardware",
  "sub_domain": "Card Reader",
  "title": "Card Reader Jam",
  "description": "A physical obstruction (usually a card) is stuck in the reader mechanism.",
  "severity": "HIGH",
  "error_codes": ["3A1", "ICM001"],
  "symptoms": ["Card not ejected", "Reader status: JAMMED"],
  "causes": ["Damaged card", "Sticky rollers", "Foreign object insertion"],
  "resolution_steps": [
    "Take ATM out of service",
    "Open card reader access panel",
    "Carefully remove jammed card using extraction tool",
    "Inspect reader rollers for damage",
    "Run card reader self-test",
    "Return ATM to service and monitor"
  ]
}
```

---

## 2. Inference Rules

Rules are `IF-THEN` statements processed by the forward-chaining engine.

**Path:** `knowledge_base/rules/*.json`

| Field | Type | Description |
|---|---|---|
| `rule_id` | String | Unique identifier (e.g., `RULE_HW_001`) |
| `description` | String | What this rule detects |
| `priority` | Integer | Salience (higher numbers fire first) |
| `conditions` | Array[Object] | List of facts that must be true (AND logic) |
| `actions` | Array[Object] | List of facts to assert or actions to take if conditions are met |

### Example Rule

```json
{
  "rule_id": "RULE_HW_001",
  "description": "Diagnose Card Reader Jam",
  "priority": 10,
  "conditions": [
    { "fact": "error_code", "operator": "contains", "value": "3A1" },
    { "fact": "card_reader_status", "operator": "eq", "value": "JAMMED" }
  ],
  "actions": [
    { "action": "assert", "fact": "diagnosis", "value": "HW_001" },
    { "action": "assert", "fact": "requires_engineer", "value": true }
  ]
}
```
