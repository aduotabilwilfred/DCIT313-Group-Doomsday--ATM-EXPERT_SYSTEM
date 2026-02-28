# ATM-Expert 🏧

> **Intelligent ATM Fault Diagnosis & Advisory System**  
> A rule-based expert system that diagnoses ATM faults, guides operators through resolution, and predicts failures before they cause downtime.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Team](#team)
- [Repository Structure](#repository-structure)
- [Getting Started](#getting-started)
- [Running the Benchmark](#running-the-benchmark)
- [Contributing](#contributing)

---

## Project Overview

ATM-Expert encodes the diagnostic knowledge of experienced ATM engineers into an intelligent decision-support engine. It uses a structured knowledge base of 100+ fault profiles processed through a forward-chaining inference engine to deliver real-time fault diagnosis, guided remediation, and predictive maintenance alerts — without requiring a physical ATM to develop or test against.

**Key capabilities:**

- Automated ingestion of ATM error logs, sensor data, and transaction failure codes
- 100+ fault profiles across hardware, software, network, cash handling, and security domains
- Forward-chaining inference engine with plain-language explanation of every diagnosis
- Step-by-step guided remediation workflows for branch staff and field engineers
- Fraud detection rules for card skimming, PIN pad tampering, and anomalous transactions
- Predictive maintenance alerts based on component usage thresholds
- Role-based access for operations teams, field engineers, branch staff, and management
- Escalation logic to route unresolved faults to Tier-2 engineering teams

---

## Team

| Role | Member | Component |
|---|---|---|
| Project Lead | Adu Kelvin Brobbey | Coordination, documentation, stakeholder liaison |
| Knowledge Engineer | Jerry Kuake | Knowledge elicitation & rule validation |
| Knowledge Engineer | Emmanuel | Knowledge elicitation & rule validation |
| Knowledge Engineer | Didemudo PeterPaul | Knowledge elicitation & rule validation |
| Developer 1 | Shadrack Dorkenoo | Inference Engine |
| Developer 2 | Otabil Wilfred du | Knowledge Base |
| Developer 3 | Joel Adom Opoku | User Interface |
| Developer 4 | Gadri Wisdom | Integration & Security |

---

## Repository Structure

```
atm-expert/
│
├── .github/                          # GitHub configuration
│   ├── workflows/
│   │   ├── ci.yml                    # Runs tests on every push and pull request
│   │   └── benchmark.yml             # Runs the 200-scenario accuracy benchmark
│   ├── PULL_REQUEST_TEMPLATE.md      # Checklist every PR must complete before merge
│   └── ISSUE_TEMPLATE.md             # Template for bug reports and feature requests
│
├── docs/                             # All project documentation
│   ├── project_brief.pdf             # Original ATM-Expert project brief
│   ├── task_breakdown.docx           # Developer task breakdown and role responsibilities
│   ├── knowledge_base_schema.md      # Knowledge base schema and rule format specification
│   ├── inference_engine_api.md       # Inference engine session API specification (Dev 1)
│   ├── integration_api.md            # ATM data feed and RBAC API specification (Dev 4)
│   ├── user_guide.md                 # Branch staff and field engineer user guide (Dev 3)
│   ├── maintenance_manual.md         # System maintenance and rule update procedures
│   └── architecture_overview.md      # System architecture diagram and component description
│
├── knowledge_base/                   # Dev 2 — Otabil Wilfred du
│   ├── fault_profiles/               # Encoded ATM fault profiles by domain
│   │   ├── hardware_faults.json      # Card reader, dispenser, printer, and sensor faults
│   │   ├── software_faults.json      # OS, application, firmware, and database faults
│   │   ├── network_faults.json       # Connectivity, TLS, VPN, and firewall faults
│   │   ├── cash_handling_faults.json # Cassette, note jam, and dispense mismatch faults
│   │   └── security_faults.json      # Skimming, tamper, fraud, and physical attack faults
│   ├── rules/                        # IF-THEN rule definitions consumed by the engine
│   │   ├── hardware_rules.json
│   │   ├── software_rules.json
│   │   ├── network_rules.json
│   │   ├── cash_rules.json
│   │   └── security_rules.json
│   ├── rule_loader.py                # Loads and parses rules into engine-ready format
│   ├── rule_validator.py             # Checks rule syntax, conflicts, and circular dependencies
│   ├── seed.py                       # Seeds the knowledge base from fault profile JSON files
│   └── schema.md                     # Rule and fault profile schema documentation
│
├── inference_engine/                 # Dev 1 — Shadrack Dorkenoo
│   ├── engine.py                     # Main forward-chaining inference engine
│   ├── working_memory.py             # Dynamic fact store for a diagnostic session
│   ├── conflict_resolver.py          # Salience and priority-based conflict resolution
│   ├── explanation.py                # Builds plain-language explanation traces per diagnosis
│   ├── session.py                    # Session lifecycle: assertFact(), run(), getDiagnosis()
│   ├── escalation.py                 # Triggers escalation facts when no diagnosis is reached
│   └── tests/
│       ├── test_engine.py            # Unit tests for rule matching and firing cycles
│       ├── test_working_memory.py    # Fact store unit tests
│       ├── test_conflict_resolver.py # Conflict resolution strategy tests
│       └── test_harness.py           # Seeded diagnostic scenario test runner
│
├── integration/                      # Dev 4 — Gadri Wisdom
│   ├── data_ingestion.py             # Normalises ATM feed data into inference engine facts
│   ├── error_code_parser.py          # Translates vendor error codes into canonical fact schema
│   ├── rbac.py                       # Role-based access control and token issuer
│   ├── fraud_detection.py            # Injects skimming, tamper, and anomaly facts into engine
│   ├── predictive_alerts.py          # Component usage thresholds and maintenance alert generator
│   ├── escalation_router.py          # Routes Tier-2 handovers via email, ticket, or SMS
│   ├── audit_log.py                  # Records all sessions, resolutions, and escalations
│   ├── api.py                        # Secure REST API endpoints for the UI and engine
│   └── tests/
│       ├── test_ingestion.py         # Data normalisation and fact mapping tests
│       ├── test_rbac.py              # Role access control tests
│       └── test_escalation_router.py # Escalation routing logic tests
│
├── ui/                               # Dev 3 — Joel Adom Opoku
│   ├── src/
│   │   ├── components/               # Reusable UI components
│   │   │   ├── DiagnosticConsole.jsx # Main ATM diagnostic session screen
│   │   │   ├── RemediationWorkflow.jsx # Step-by-step guided resolution interface
│   │   │   ├── ExplanationPanel.jsx  # Plain-language reasoning display from engine trace
│   │   │   ├── EscalationScreen.jsx  # Tier-2 handover summary form
│   │   │   ├── KPIDashboard.jsx      # Management analytics and KPI view
│   │   │   └── AlertBanner.jsx       # Critical and high severity alert banner
│   │   ├── views/                    # Role-based page views
│   │   │   ├── BranchStaffView.jsx   # Simplified guided workflow for branch staff
│   │   │   ├── EngineerView.jsx      # Full technical detail view for field engineers
│   │   │   ├── ManagementView.jsx    # KPI-only view for bank management
│   │   │   └── FraudTeamView.jsx     # Security and fraud monitoring view
│   │   ├── App.jsx                   # Root app component and role-based routing
│   │   └── api.js                    # API call helpers to the integration layer
│   ├── public/                       # Static assets (icons, logos)
│   └── package.json                  # UI dependencies
│
├── benchmark/                        # Accuracy testing — shared by all developers
│   ├── generate_benchmark_scenarios.py # Script that generated the 200 test scenarios
│   ├── atm_benchmark_scenarios.json  # Full 200-scenario benchmark dataset with ground truth
│   ├── atm_benchmark_index.json      # Lightweight scenario index for quick browsing
│   ├── run_benchmark.py              # Runs all 200 scenarios and reports accuracy percentage
│   └── benchmark_results.json        # Latest benchmark run output
│
├── simulator/                        # ATM hardware simulator — no physical ATM required
│   ├── atm_simulator.py              # Simulates live ATM error feeds from scenario files
│   ├── scenario_player.py            # Injects scenario facts into the engine on demand
│   └── mock_atm_config.json          # Configuration for 20 virtual ATM unit definitions
│
├── .env.example                      # Environment variable template — copy to .env to configure
├── .gitignore                        # Ignores .env, __pycache__, node_modules, and build output
├── requirements.txt                  # Python dependencies for the backend
└── README.md                         # This file
```

---

## Getting Started

### Prerequisites

- Python 3.10+
- Node.js 18+ (for the UI)
- Git

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/your-org/atm-expert.git
cd atm-expert

# 2. Install Python dependencies
pip install -r requirements.txt

# 3. Set up environment variables
cp .env.example .env
# Edit .env with your configuration

# 4. Seed the knowledge base
python knowledge_base/seed.py

# 5. Install UI dependencies
cd ui && npm install && cd ..
```

### Running the Simulator (no ATM required)

```bash
# Start the ATM simulator — injects fake ATM fault data into the engine
python simulator/atm_simulator.py

# Or manually play a specific scenario
python simulator/scenario_player.py --scenario H001
```

---

## Running the Benchmark

The benchmark evaluates the inference engine's diagnostic accuracy against 200 pre-labelled ATM fault scenarios spanning all five fault domains.

```bash
python benchmark/run_benchmark.py
```

The target accuracy rate is **≥ 85%**. Results are saved to `benchmark/benchmark_results.json`.

---

## Contributing

Each developer works within their assigned folder and opens a **Pull Request** to `main` when a feature is ready. Direct pushes to `main` are not allowed.

| Branch naming | Purpose |
|---|---|
| `dev1/feature-name` | Inference engine work (Shadrack) |
| `dev2/feature-name` | Knowledge base work (Otabil) |
| `dev3/feature-name` | UI work (Joel) |
| `dev4/feature-name` | Integration work (Gadri) |

All PRs must pass CI checks and be reviewed by at least one other team member before merging.

---
