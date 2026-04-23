# ATM-Expert 🏧

> **Intelligent ATM Fault Diagnosis & Advisory System**  
> A rule-based expert system that diagnoses ATM faults, guides operators through resolution, and predicts failures before they cause downtime.

---
| No. | GitHub Username | Student ID |
| --: | --------------- | ---------- |
|   1 | `aduotabilwilfred`    | `22045896`    |
|   2 | `shadyOg`     | `22027811`    |
|   3 | `Didemudopeterpaul`     | `22046391`    |
|   4 | `Jerry-Kuake`     | `22020691`    |
|   5 | `Wgadri`     |   `22018743`  |
|   6 | `adom9`     |   `22117567`  |
|   7 | ``     |     |



## Table of Contents

- [Project Overview](#project-overview)
- [Team](#team)
- [Repository Structure](#repository-structure)
- [Getting Started](#getting-started)
- [Running the Benchmark](#running-the-benchmark)
- [Contributing](#contributing)

---

## Project Overview

ATM-Expert encodes the diagnostic knowledge of experienced ATM engineers into an intelligent decision-support engine. It uses a hybrid **Python-Prolog** architecture:

1. **Knowledge Base (Prolog):** 100+ fault profiles encoded as Prolog facts and modular diagnostic rules for high-performance symbolic reasoning.
2. **Inference Engine (Python-Prolog Bridge):** A Python-based bridge that interacts with the SWI-Prolog engine to perform diagnoses and retrieve resolution steps.

**Key capabilities:**

- Automated ingestion of ATM error logs, sensor data, and transaction failure codes
- 100+ fault profiles across hardware, software, network, cash handling, and security domains
- Symbolic reasoning engine with plain-language explanation of every diagnosis
- Step-by-step guided remediation workflows for branch staff and field engineers
- Fraud detection rules for card skimming, PIN pad tampering, and anomalous transactions
- Predictive maintenance alerts based on component usage thresholds
- Role-based access for operations teams, field engineers, branch staff, and management

---

## Team

| Role | Member | Component |
|---|---|---|
| Project Lead | Adu Kelvin Brobbey | Coordination, documentation, stakeholder liaison |
| Knowledge Engineer | Jerry Kuake Emmanuel| Knowledge elicitation & rule validation |
| Knowledge Engineer | Didemudo PeterPaul | Knowledge elicitation & rule validation |
| Developer 1 | Shadrack Dorkenoo | Inference Engine |
| Developer 2 | Otabil Wilfred Adu | Knowledge Base |
| Developer 3 | Joel Yaw Adom Opoku | User Interface |
| Developer 4 | Gadri Wisdom | Integration & Security |

---

## Repository Structure

```
atm-expert/
│
├── .github/                          # GitHub configuration
│   ├── workflows/                    # CI/CD and Benchmark workflows
│   ├── PULL_REQUEST_TEMPLATE.md      # Checklist for PRs
│   └── ISSUE_TEMPLATE.md             # Bug reports and feature requests
│
├── docs/                             # Project documentation
│   ├── architecture_overview.md      # System architecture and component description
│   ├── knowledge_base_schema.md      # Rule format specification
│   └── team_guidance.md              # [NEW] Developer handover & integration instructions
│
├── knowledge_base/                   # Dev 2 — Otabil Wilfred Adu
│   ├── fault_profiles/               # Source JSON fault profiles by domain
│   ├── atm_kb.pl                     # [GENERATED] Prolog facts (generated from JSON)
│   ├── rules.pl                      # Diagnostic logic and inference rules
│   ├── loader.pl                     # Master loader for facts and rules
│   ├── json_to_prolog.py             # Script to compile JSON profiles into atm_kb.pl
│   └── schema.md                     # Rule and fault profile schema documentation
│
├── inference_engine/                 # Dev 1 — Shadrack Dorkenoo
│   └── prolog_bridge.py              # Python bridge to the SWI-Prolog engine
│
├── integration/                      # Dev 4 — Gadri Wisdom
│   ├── api.py                        # [NEW] Flask REST API serving Prolog logic
│   └── .gitkeep                      # Integration scripts and log parsers
│
├── ui/                               # Dev 3 — Joel Adom Opoku
│   ├── src/                          # React source code
│   │   ├── components/               # UI components (DiagnosticConsole, etc.)
│   │   ├── services/                 # [NEW] Backend API integration (api.js)
│   │   ├── views/                    # Role-specific dashboard views
│   │   ├── App.jsx                   # Main application routing
│   │   └── main.jsx                  # Application entry point
│   ├── index.html                    # HTML template
│   ├── package.json                  # UI dependencies and scripts
│   └── vite.config.js                # [NEW] Build tool configuration
│
├── benchmark/                        # Accuracy testing
│   ├── atm_benchmark_scenarios.json  # 200-scenario benchmark dataset
│   └── generate_benchmark_scenarios.py # Scenario generation script
│
├── simulator/                        # ATM hardware simulator
│   ├── atm_simulator.py              # [NEW] CLI-based fault simulation tool
│   └── .gitkeep
│
├── .env.example                      # Environment variable template
├── .gitignore                        # Global ignore list
└── README.md                         # This file
```

---

## Getting Started

### Prerequisites

- **Python 3.10+**
- **SWI-Prolog 9.0+** (Ensure `swipl` is in your system PATH)
- **Node.js 18+** (for the UI)
- **Git**

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/owills004/DCIT313-Group-Doomsday--ATM-EXPERT_SYSTEM.git
cd DCIT313-Group-Doomsday--ATM-EXPERT_SYSTEM

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
