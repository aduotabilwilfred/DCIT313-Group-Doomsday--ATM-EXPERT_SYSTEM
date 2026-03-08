# ATM Expert - User Interface

> **Intelligent ATM Fault Diagnosis Dashboard**  
> A React-based frontend for the ATM Expert system that provides role-based diagnostic interfaces for ATM fault detection and resolution.

---

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Quick Start](#quick-start)
- [User Roles](#user-roles)
- [Using the Diagnostic Console](#using-the-diagnostic-console)
- [API Integration](#api-integration)
- [Troubleshooting](#troubleshooting)

---

## Overview

The ATM Expert UI connects to a Flask backend which interfaces with a Prolog-based inference engine. The system diagnoses ATM faults based on observed symptoms and error codes, providing:

- **Real-time fault diagnosis** with confidence scoring
- **Plain-language explanations** of why a fault was identified
- **Step-by-step remediation workflows** tailored to each fault
- **Role-based dashboards** for different user types

### Architecture

```
┌─────────────────┐      HTTP/JSON       ┌─────────────────┐      Subprocess      ┌─────────────────┐
│   React UI      │  ◄──────────────►    │   Flask API     │  ◄──────────────►    │  SWI-Prolog     │
│   (Port 5173)   │                      │   (Port 5000)   │                      │  Knowledge Base │
└─────────────────┘                      └─────────────────┘                      └─────────────────┘
```

---

## Prerequisites

Before running the application, ensure you have:

- **Node.js 18+** - For the React frontend
- **Python 3.10+** - For the Flask backend
- **SWI-Prolog 9.0+** - For the inference engine (must be in PATH)
- **pip packages**: `flask`, `flask-cors`

---

## Quick Start

### 1. Start the Backend API

Open a terminal in the project root and run:

```bash
# Install Python dependencies (first time only)
pip install flask flask-cors

# Start the API server
python integration/api.py
```

You should see:
```
==================================================
ATM Expert API Server
==================================================
Starting server on http://localhost:5000
...
```

### 2. Start the Frontend

Open a **new terminal** and run:

```bash
cd ui

# Install dependencies (first time only)
npm install

# Start the development server
npm run dev
```

You should see:
```
VITE ready in 986 ms
➜  Local:   http://localhost:5173/
```

### 3. Open the Application

Navigate to **http://localhost:5173** in your web browser.

---

## User Roles

The application provides four role-based views:

| Role | Icon | Description |
|------|------|-------------|
| **Branch Staff** | 🏦 | Front-line staff at bank branches who handle basic ATM issues |
| **Field Engineer** | 🔧 | Technical engineers who perform physical repairs and maintenance |
| **Management** | 📊 | Operations managers who monitor ATM fleet health and KPIs |
| **Fraud Team** | 🛡️ | Security specialists who investigate suspicious activity |

Select your role from the main menu to access the appropriate dashboard.

---

## Using the Diagnostic Console

The Diagnostic Console is the primary interface for fault diagnosis.

### Step 1: Check Connection Status

At the top of the console, verify the backend connection:

- 🟢 **Backend Connected** - Ready to diagnose
- 🔴 **Backend Disconnected** - Start the API server first

### Step 2: Enter Observations

You can input observations in two ways:

#### Manual Entry

1. **Symptoms** - Enter observed symptoms, separated by commas:
   ```
   Card not ejected, Reader status: JAMMED
   ```

2. **Error Codes** - Enter ATM error codes, separated by commas:
   ```
   3A1, ICM001
   ```

#### Quick Test Scenarios

Click any of the pre-configured test buttons:

| Button | Symptom | Error Code |
|--------|---------|------------|
| Card Reader Jam | Card not ejected | 3A1 |
| Cash Dispenser Jam | Dispense attempt fails | 4B1 |
| Paper Jam | Receipt not printed | 5E3 |
| Network Issue | Network connection lost | NET001 |

### Step 3: Run Diagnosis

Click **▶ Run Diagnosis** to query the inference engine.

### Step 4: Review Results

The diagnosis result includes:

1. **Alert Banner** - Shows fault severity (LOW/MEDIUM/HIGH/CRITICAL)
2. **Confidence Score** - How certain the system is (0-100%)
3. **Fault Details** - ID, domain, and category
4. **Explanation Panel** - Why this fault was identified:
   - Which symptoms matched
   - Which error codes matched
   - Possible root causes
5. **Remediation Workflow** - Step-by-step resolution guide
6. **Other Diagnoses** - Alternative faults that also matched

### Step 5: Reset

Click **🔄 New Diagnosis** to clear results and start over.

---

## API Integration

The frontend communicates with the backend via REST API:

### Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/health` | GET | Check if backend is running |
| `/api/diagnose` | POST | Run fault diagnosis |
| `/api/faults` | GET | List all known faults |
| `/api/faults/:id` | GET | Get fault details |
| `/api/workflow/:id` | GET | Get remediation steps |
| `/api/explain` | POST | Get diagnosis explanation |
| `/api/domains` | GET | List fault domains |

### Example Diagnosis Request

```javascript
POST http://localhost:5000/api/diagnose
Content-Type: application/json

{
  "symptoms": ["Card not ejected", "Reader status: JAMMED"],
  "error_codes": ["3A1", "ICM001"]
}
```

### Example Response

```json
{
  "success": true,
  "count": 1,
  "diagnoses": [
    {
      "fault_id": "HW_001",
      "title": "Card Reader Jam",
      "domain": "Hardware",
      "severity": "HIGH",
      "confidence": 1.0,
      "matched_observations": [
        {"type": "symptom", "value": "Card not ejected"},
        {"type": "error_code", "value": "3A1"}
      ]
    }
  ]
}
```

---

## Troubleshooting

### Backend Disconnected

**Problem:** UI shows "Backend Disconnected"

**Solution:**
1. Ensure the Flask API is running: `python integration/api.py`
2. Check it's on port 5000: http://localhost:5000/api/health
3. Verify no firewall is blocking the connection

### No Diagnoses Found

**Problem:** System returns "No matching faults found"

**Solution:**
1. Check spelling of symptoms (must match exactly)
2. Verify error codes are correct
3. The knowledge base may not contain the fault - contact Dev 2

### SWI-Prolog Not Found

**Problem:** Backend throws "swipl not found in PATH"

**Solution:**
1. Install SWI-Prolog: https://www.swi-prolog.org/download/stable
2. Add to PATH:
   - Windows: Add `C:\Program Files\swipl\bin` to PATH
   - Mac: `brew install swi-prolog`
   - Linux: `sudo apt install swi-prolog`

### Port Already in Use

**Problem:** "Address already in use" error

**Solution:**
```bash
# Find and kill process on port 5000
# Windows PowerShell:
Get-NetTCPConnection -LocalPort 5000 | Select-Object -Property OwningProcess

# Then kill the process:
Stop-Process -Id <PID>
```

---

## Development

### Tech Stack

- **Frontend:** React 18 + Vite
- **Backend:** Flask + Flask-CORS
- **Inference Engine:** SWI-Prolog
- **Styling:** Inline CSS (no external framework)

### File Structure

```
ui/
├── src/
│   ├── components/
│   │   ├── AlertBanner.jsx         # Severity alert display
│   │   ├── DiagnosticConsole.jsx   # Main diagnosis interface
│   │   ├── ExplanationPanel.jsx    # Diagnosis explanation
│   │   ├── RemediationWorkflow.jsx # Step-by-step guide
│   │   └── ...
│   ├── services/
│   │   └── api.js                  # Backend API client
│   ├── views/
│   │   ├── BranchStaffView.jsx
│   │   ├── EngineerView.jsx
│   │   ├── FraudTeamView.jsx
│   │   └── ManagementView.jsx
│   ├── App.jsx                     # Main app with role selection
│   └── main.jsx                    # Entry point
├── package.json
└── vite.config.js
```

---

## License

This project is part of DCIT313 coursework - University of Ghana, Computer Science Department.

---

**Team Doomsday** | ATM Expert System | 2026
