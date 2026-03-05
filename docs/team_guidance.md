# ATM-Expert Developer Handover & Coordination

This document outlines the interfaces and steps needed from each team member following the Knowledge Base (KB) refactor.

**Owner:** Otabil Wilfred Adu (Dev 2 - KB)

---

## 🏗️ Knowledge Base Structure (NEW)

The KB is now modular. Do not load `atm_kb.pl` directly. Instead, point to `loader.pl`.

- `knowledge_base/rules.pl`: Contains diagnostic logic (Static).
- `knowledge_base/atm_kb.pl`: Contains fault facts (Generated from JSON).
- `knowledge_base/loader.pl`: Master file that loads both.

---

## 🛠️ Action Items for Team Members

### 👨‍💻 Dev 1: Inference Engine (Shadrack)

**Goal:** Update the Python-Prolog bridge to use the new loader.

1. Open `inference_engine/prolog_bridge.py`.
2. Update the `kb_path` logic to point to `knowledge_base/loader.pl` instead of `atm_kb.pl`.
3. Verify that the `diagnose` and `get_details` methods still work as expected.

### 🎨 Dev 3: User Interface (Joel)

**Goal:** Ensure symptoms and error codes are captured correctly.

The KB expects observations in the following format:

- **Symptoms:** Simple strings like `'Card not ejected'` or `'Out of Cash screen'`.
- **Error Codes:** Vendor-specific codes like `'3A1'` or `'CSH001'`.

The `get_details` query returns these fields which your UI should display:

- `domain`, `sub_domain`, `title`, `severity`, `description`, `resolution_steps` (as a list).

### 🛡️ Dev 4: Integration & Security (Gadri)

**Goal:** Hook security-specific logic into the diagnostic rules.

If you have specific security sensors or protocols to add:

1. Add new JSON profiles to `knowledge_base/fault_profiles/`.
2. If you need custom Prolog rules for complex security logic (e.g., "if 3 failed PINs AND card is foreign"), we can add them to `knowledge_base/rules.pl`.

---

## ✅ Verification

Otabil has verified that running `python knowledge_base/json_to_prolog.py` now generated a clean fact file, and the rules are safely modularized.
