import json
import os
from pathlib import Path

def get_symptoms(status_type, status_val, last_error):
    symptoms = []
    prefixes = {
        'card_reader_status': 'Reader status',
        'printer_status': 'Printer status',
        'dispenser_status': 'Dispenser status',
        'pin_pad_status': 'PIN pad status',
        'software_status': 'Software status',
        'network_status': 'Network status'
    }
    if status_type in prefixes and status_val and status_val not in ['OK', 'NORMAL', 'READY']:
        symptoms.append(f"{prefixes[status_type]}: {status_val}")
    if status_val == 'STUCK' and status_type == 'card_present_sensor':
        symptoms.append('Card not ejected')
    if status_val == 'DOWN' and status_type == 'network_status':
        symptoms.append('Network connection lost')
    error_map = {
        'CARD_NOT_EJECTED': 'Card not ejected', 'DISPENSE_FAILED': 'Dispense attempt fails',
        'RECEIPT_NOT_PRINTED': 'Receipt not printed', 'NETWORK_TIMEOUT': 'Network timeout',
        'CARD_READ_ERROR': 'Intermittent read failures', 'TRANSACTION_TIMEOUT': 'Transaction timeout',
        'PIN_ENTRY_FAILURE': 'PIN entry failed', 'BALANCE_INQUIRY_FAILED': 'Balance inquiry failed',
        'DISPENSER_JAM': 'Dispense attempt fails', 'REJECT_BIN_FULL': 'Dispense attempt fails',
        'PRESENTER_FAULT': 'Dispense attempt fails'
    }
    if last_error in error_map:
        symptoms.append(error_map[last_error])
    return list(set(symptoms))

def seed():
    kb_path = Path(__file__).parent
    profiles_dir = kb_path / "fault_profiles"
    profiles_dir.mkdir(exist_ok=True)

    # --- HARDWARE ---
    hardware = [
        ("H_CR_001", "Card Reader", "Card Reader Jam", "HIGH", ["3A1", "ICM001"], "JAMMED", "CARD_NOT_EJECTED"),
        ("H_CR_002", "Card Reader", "Card Reader Dirty / Sensor Fault", "MEDIUM", ["3A5", "ICM004"], "DIRTY_SENSOR", "READ_ERROR"),
        ("H_CD_001", "Cash Dispenser", "Cash Dispenser Jam", "HIGH", ["4B1"], "DISPENSER_JAM", "DISPENSER_JAM"),
        ("H_CD_002", "Cash Dispenser", "Dispenser Actuator Wear Warning", "MEDIUM", ["4B8"], "ACTUATOR_WORN", "ACTUATOR_WORN"),
        ("H_CD_003", "Cash Dispenser", "Reject Bin Full", "MEDIUM", ["4C2"], "REJECT_BIN_FULL", "REJECT_BIN_FULL"),
        ("H_CD_004", "Cash Dispenser", "Cash Presenter Fault", "HIGH", ["4D1"], "PRESENTER_FAULT", "PRESENTER_FAULT"),
        ("H_PR_001", "Receipt Printer", "Printer Paper Out", "LOW", ["5E1"], "PAPER_OUT", "PAPER_OUT"),
        ("H_PR_002", "Receipt Printer", "Printer Paper Jam", "MEDIUM", ["5E3"], "PAPER_JAM", "PAPER_JAM"),
        ("H_PR_003", "Receipt Printer", "Print Head Failure", "HIGH", ["5E7"], "PRINT_HEAD_FAIL", "PRINT_HEAD_FAIL"),
        ("H_ENV_001", "Sensors & Environment", "Overheating — Temperature Critical", "HIGH", ["9T1"], "TEMP_HIGH", "TEMP_HIGH"),
        ("H_ENV_002", "Sensors & Environment", "ATM Enclosure Door Open", "CRITICAL", ["9D1"], "DOOR_OPEN", "DOOR_OPEN"),
        ("H_ENV_003", "Sensors & Environment", "General Sensor Malfunction", "MEDIUM", ["9S2"], "SENSOR_FAULT", "SENSOR_FAULT"),
        ("H_ENV_004", "Sensors & Environment", "Power / Voltage Instability", "HIGH", ["9V3"], "VOLTAGE_UNSTABLE", "VOLTAGE_UNSTABLE"),
        ("H_ENV_005", "Sensors & Environment", "Cooling Fan Failure", "HIGH", ["9F1"], "FAN_FAULT", "FAN_FAULT"),
        ("H_PER_001", "Peripherals", "PIN Pad Unresponsive", "HIGH", ["6P1"], "PINPAD_UNRESPONSIVE", "PINPAD_UNRESPONSIVE"),
        ("H_PER_002", "Peripherals", "Display Screen Failure", "HIGH", ["6S2"], "SCREEN_BLANK", "SCREEN_BLANK"),
        ("H_PER_003", "Peripherals", "ATM Camera Offline", "MEDIUM", ["6C1"], "CAMERA_OFFLINE", "CAMERA_OFFLINE"),
        ("H_PER_004", "Peripherals", "UPS Battery Low — Replace Soon", "MEDIUM", ["9U1"], "UPS_LOW", "UPS_LOW"),
        ("H_PER_005", "Peripherals", "Barcode / QR Reader Fault", "LOW", ["6B3"], "BARCODE_READER_FAIL", "BARCODE_READER_FAIL"),
    ]
    hw_json = []
    for fid, sub, diag, sev, codes, status, err in hardware:
        hw_json.append({"fault_id": fid, "domain": "Hardware", "sub_domain": sub, "title": diag, "severity": sev, 
                        "description": diag, "error_codes": codes, "resolution_steps": ["Inspect component", "Test/Reset"],
                        "symptoms": get_symptoms("dispenser_status" if "Dispenser" in sub else "card_reader_status" if "Reader" in sub else "printer_status" if "Printer" in sub else "pin_pad_status" if "PIN" in diag else "status", status, err)})
    with open(profiles_dir / "hardware_faults.json", "w") as f: json.dump(hw_json, f, indent=2)

    # --- SOFTWARE ---
    software = [
        ("OS", "SW001", "OS Kernel Panic / Blue Screen", "CRITICAL"),
        ("OS", "SW002", "OS Disk Space Critical", "HIGH"),
        ("Application", "SW010", "ATM Application Crash", "HIGH"),
        ("Application", "SW011", "Application Version Mismatch", "MEDIUM"),
        ("Application", "SW012", "Application Deadlock Detected", "HIGH"),
        ("Application", "SW013", "Configuration File Corrupt", "HIGH"),
        ("Firmware", "SW020", "Firmware Update Failed", "HIGH"),
        ("Firmware", "SW021", "Firmware Version Mismatch", "MEDIUM"),
        ("Database", "SW030", "Transaction Database Unreachable", "CRITICAL"),
        ("Database", "SW031", "Transaction Log Full", "HIGH"),
        ("Security Software", "SW040", "Anti-Tamper Software Alert", "CRITICAL"),
        ("Security Software", "SW041", "Certificate / TLS Expiry", "HIGH"),
        ("Security Software", "SW042", "Encryption Key Rotation Overdue", "HIGH"),
        ("Diagnostics", "SW050", "Self-Test Failure at Startup", "HIGH"),
        ("Diagnostics", "SW051", "Scheduled Maintenance Mode Stuck", "MEDIUM"),
        ("Remote Management", "SW060", "Remote Management Agent Offline", "MEDIUM"),
        ("Remote Management", "SW061", "Software Patch Failed to Apply", "MEDIUM"),
        ("Watchdog", "SW070", "Watchdog Timer Restart Loop", "HIGH"),
        ("Watchdog", "SW071", "Memory Leak Detected", "HIGH"),
        ("Startup", "SW080", "ATM Failed to Boot", "CRITICAL"),
    ]
    sw_json = []
    for idx, (sub, code, diag, sev) in enumerate(software):
        sw_json.append({"fault_id": f"S_SW_{idx:03}", "domain": "Software", "sub_domain": sub, "title": diag, "severity": sev,
                        "description": diag, "error_codes": [code], "resolution_steps": ["Restart", "Remote Maintenance"],
                        "symptoms": get_symptoms("software_status", "FAULT", code)})
    with open(profiles_dir / "software_faults.json", "w") as f: json.dump(sw_json, f, indent=2)

    # --- NETWORK ---
    network = [
        ("Connectivity", "NET001", "ATM Offline — No Network Response", "CRITICAL"),
        ("Connectivity", "NET002", "Intermittent Network Drops", "HIGH"),
        ("Connectivity", "NET003", "High Network Latency", "MEDIUM"),
        ("Connectivity", "NET004", "DNS Resolution Failure", "HIGH"),
        ("TLS/Security", "NET010", "TLS Handshake Failure", "HIGH"),
        ("TLS/Security", "NET011", "SSL Certificate Mismatch", "HIGH"),
        ("TLS/Security", "NET012", "Man-in-the-Middle Warning", "CRITICAL"),
        ("Host Connectivity", "NET020", "Cannot Reach Bank Core System", "CRITICAL"),
        ("Host Connectivity", "NET021", "Connection Timeout to Core System", "HIGH"),
        ("Host Connectivity", "NET022", "Authentication Rejected by Core", "HIGH"),
        ("VPN", "NET030", "VPN Tunnel Down", "CRITICAL"),
        ("VPN", "NET031", "VPN Authentication Failed", "HIGH"),
        ("Firewall", "NET040", "ATM Traffic Blocked by Firewall", "HIGH"),
        ("Firewall", "NET041", "IP Address Conflict", "MEDIUM"),
        ("Switch/Router", "NET050", "Network Switch Port Down", "HIGH"),
        ("Switch/Router", "NET051", "Router Unreachable", "CRITICAL"),
        ("Bandwidth", "NET060", "Bandwidth Saturation", "MEDIUM"),
        ("Bandwidth", "NET061", "Packet Loss Exceeding Threshold", "HIGH"),
        ("NTP", "NET070", "Clock Sync Failure (NTP)", "MEDIUM"),
        ("NTP", "NET071", "ATM Clock Drift Detected", "MEDIUM"),
    ]
    net_json = []
    for idx, (sub, code, diag, sev) in enumerate(network):
        net_json.append({"fault_id": f"N_NET_{idx:03}", "domain": "Network", "sub_domain": sub, "title": diag, "severity": sev,
                         "description": diag, "error_codes": [code], "resolution_steps": ["Check LAN", "Network Reset"],
                         "symptoms": get_symptoms("network_status", "FAULT" if "Offline" not in diag else "DOWN", code)})
    with open(profiles_dir / "network_faults.json", "w") as f: json.dump(net_json, f, indent=2)

    # --- CASH HANDLING ---
    cash = [
        ("Cassette", "CSH001", "Cash Cassette Empty", "HIGH"),
        ("Cassette", "CSH002", "Cash Cassette Low — Alert", "MEDIUM"),
        ("Cassette", "CSH003", "Cassette Not Detected / Not Seated", "HIGH"),
        ("Cassette", "CSH004", "Wrong Cassette Denomination Loaded", "HIGH"),
        ("Cassette", "CSH005", "Cassette Lock Fault", "MEDIUM"),
        ("Note Handling", "CSH010", "Note Jam in Transport Path", "HIGH"),
        ("Note Handling", "CSH011", "Multiple Note Feed (Double Take)", "HIGH"),
        ("Note Handling", "CSH012", "Torn / Mutilated Note Detected", "MEDIUM"),
        ("Note Handling", "CSH013", "High Reject Rate — Notes", "HIGH"),
        ("Counting", "CSH020", "Dispense Count Mismatch", "CRITICAL"),
        ("Counting", "CSH021", "Short Dispense Detected", "CRITICAL"),
        ("Counting", "CSH022", "Over-Dispense Detected", "CRITICAL"),
        ("Balancing", "CSH030", "Cash Balance Discrepancy at EOD", "HIGH"),
        ("Balancing", "CSH031", "Cassette Inventory Mismatch", "HIGH"),
        ("Currency Detector", "CSH040", "Counterfeit Note Detected", "CRITICAL"),
        ("Currency Detector", "CSH041", "Currency Detector Fault", "HIGH"),
        ("Recycling", "CSH050", "Recycler Module Fault", "HIGH"),
        ("Recycling", "CSH051", "Recycled Note Rejected by Validator", "MEDIUM"),
        ("Security", "CSH060", "Cash Vault Door Open Alert", "CRITICAL"),
        ("Security", "CSH061", "Cash Replenishment Anomaly", "HIGH"),
    ]
    cash_json = []
    for idx, (sub, code, diag, sev) in enumerate(cash):
        cash_json.append({"fault_id": f"C_CSH_{idx:03}", "domain": "Cash Handling", "sub_domain": sub, "title": diag, "severity": sev,
                          "description": diag, "error_codes": [code], "resolution_steps": ["Refill/Check Cassette", "Balance"],
                          "symptoms": get_symptoms("dispenser_status", "FAULT", code)})
    with open(profiles_dir / "cash_handling_faults.json", "w") as f: json.dump(cash_json, f, indent=2)

    # --- SECURITY ---
    security = [
        ("Card Skimming", "SEC001", "Card Skimmer Device Detected", "CRITICAL"),
        ("Card Skimming", "SEC002", "Card Reader Depth Anomaly (Possible Skimmer)", "CRITICAL"),
        ("Card Skimming", "SEC003", "Unusual Card Read Failures — Possible Shimmer", "HIGH"),
        ("PIN Pad Tampering", "SEC010", "PIN Pad Cover Removal Detected", "CRITICAL"),
        ("PIN Pad Tampering", "SEC011", "PIN Pad Enclosure Breach Sensor Triggered", "CRITICAL"),
        ("PIN Pad Tampering", "SEC012", "Suspicious PIN Pad Overlay Pattern", "HIGH"),
        ("Transaction Fraud", "SEC020", "Unusual Transaction Volume — Velocity Alert", "HIGH"),
        ("Transaction Fraud", "SEC021", "Repeated Declined Transactions — Brute Force", "HIGH"),
        ("Transaction Fraud", "SEC022", "High-Value Withdrawal Cluster", "HIGH"),
        ("Transaction Fraud", "SEC023", "Card Present + Geolocation Mismatch", "HIGH"),
        ("Physical Attack", "SEC030", "ATM Anti-Ram Sensor Triggered", "CRITICAL"),
        ("Physical Attack", "SEC031", "Explosive Gas Detection Alert", "CRITICAL"),
        ("Physical Attack", "SEC032", "ATM Enclosure Vibration Alert", "HIGH"),
        ("Physical Attack", "SEC033", "Safe Door Tamper Sensor Triggered", "CRITICAL"),
        ("CCTV / Surveillance", "SEC040", "ATM Camera Offline — Security Risk", "HIGH"),
        ("CCTV / Surveillance", "SEC041", "Camera View Obstruction Detected", "HIGH"),
        ("Logical Security", "SEC050", "Failed Admin Login Attempts Threshold", "HIGH"),
        ("Logical Security", "SEC051", "Unauthorised Remote Access Attempt", "CRITICAL"),
        ("Logical Security", "SEC052", "Malware Signature Detected on ATM OS", "CRITICAL"),
        ("Compliance", "SEC060", "PCI-DSS Compliance Check Failed", "HIGH"),
    ]
    sec_json = []
    for idx, (sub, code, diag, sev) in enumerate(security):
        sec_json.append({"fault_id": f"SEC_{idx:03}", "domain": "Security", "sub_domain": sub, "title": diag, "severity": sev,
                         "description": diag, "error_codes": [code], "resolution_steps": ["Security Alert", "Forensics"],
                         "symptoms": get_symptoms("tamper_sensor", "TRIGGERED", code)})
    with open(profiles_dir / "security_faults.json", "w") as f: json.dump(sec_json, f, indent=2)

    print(f"Seeded {profiles_dir} with 100+ unique fault profiles.")

if __name__ == "__main__":
    seed()
