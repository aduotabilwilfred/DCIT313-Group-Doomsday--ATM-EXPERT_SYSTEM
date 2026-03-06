# ATM-Expert Developer Handover & Coordination

This document outlines the interfaces and steps needed from each team member following the Knowledge Base (KB) refactor.

**Owner:** Otabil Wilfred Adu (Dev 2 - KB)

---

## Knowledge Base Structure (NEW)

The KB is now modular. Do not load `atm_kb.pl` directly. Instead, point to `loader.pl`.

- `knowledge_base/rules.pl`: Contains diagnostic logic (Static).
- `knowledge_base/atm_kb.pl`: Contains fault facts (Generated from JSON).
- `knowledge_base/loader.pl`: Master file that loads both.

---

## Action Items for Team Members

### Dev 1: Inference Engine (Shadrack)

**Goal:** Update the Python-Prolog bridge to use the new loader.

1. Open `inference_engine/prolog_bridge.py`.
2. Update the `kb_path` logic to point to `knowledge_base/loader.pl` instead of `atm_kb.pl`.
3. Verify that the `diagnose` and `get_details` methods still work as expected.

### Dev 3: User Interface (Joel)

**Goal:** Ensure symptoms and error codes are captured correctly.

The KB expects observations in the following format:

- **Symptoms:** Simple strings like `'Card not ejected'` or `'Out of Cash screen'`.
- **Error Codes:** Vendor-specific codes like `'3A1'` or `'CSH001'`.

The `get_details` query returns these fields which your UI should display:

- `domain`, `sub_domain`, `title`, `severity`, `description`, `resolution_steps` (as a list).

### Dev 4: Integration & Security (Gadri)

**Goal:** Integrate security-specific faults into the system.

If you have new security sensors or fraud-detection scenarios:

1. **Data:** Add new JSON profiles to `knowledge_base/fault_profiles/`. Otabil's generator will automatically ingest these into the KB.
2. **Logic:** If your security scenarios require complex logic (e.g., cross-referencing multiple failed PINs), **coordinate with Otabil (Dev 2)**. He will implement the necessary Prolog rules in `rules.pl`.

**New Tool: ATM Simulator (`simulator/atm_simulator.py`)**
I have built a foundation for the ATM Simulator to help you with integration testing.

- **Usage:** Run `python simulator/atm_simulator.py`.
- **Function:** It allows you to select a fault profile and "emits" the hardware signals (error codes and symptoms) that your integration scripts should be processing.
- **Your Task:** Expand this simulator if you need it to talk to your log-processing scripts or the API layer Shadrack is building.

*Note: Otabil maintains ownership of the Knowledge Base scripts and core logic.*

---

## Verification

Otabil has verified that running `python knowledge_base/json_to_prolog.py` now generated a clean fact file, and the rules are safely modularized.
