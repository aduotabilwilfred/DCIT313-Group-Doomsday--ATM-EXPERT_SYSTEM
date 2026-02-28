"""
ATM-Expert Benchmark Scenario Generator
========================================
Generates 200 realistic ATM fault scenarios in JSON format
covering all five fault domains:
  1. Hardware (50 scenarios)
  2. Software (35 scenarios)
  3. Network (35 scenarios)
  4. Cash Handling (40 scenarios)
  5. Security / Fraud (40 scenarios)

Each scenario contains:
  - scenario_id
  - domain
  - atm_id
  - timestamp
  - error_codes        : list of raw ATM vendor error codes
  - sensor_readings    : dict of ATM sensor/state values
  - transaction_context: recent transaction metadata
  - facts              : normalised facts ready for inference engine
  - expected_diagnosis : ground-truth label for benchmark evaluation
  - expected_severity  : LOW | MEDIUM | HIGH | CRITICAL
  - expected_resolution: ordered list of resolution steps
  - notes              : human-readable explanation

Run:
    python generate_benchmark_scenarios.py
Output:
    atm_benchmark_scenarios.json        (all 200 scenarios)
    atm_benchmark_index.json            (index/summary only)
"""

import json
import random
from datetime import datetime, timedelta

random.seed(42)  # Reproducible output for benchmark consistency

ATM_IDS = [f"ATM-{str(i).zfill(4)}" for i in range(1, 21)]  # 20 ATM units


def rand_ts():
    base = datetime(2025, 1, 1)
    delta = timedelta(days=random.randint(0, 364),
                      hours=random.randint(0, 23),
                      minutes=random.randint(0, 59))
    return (base + delta).strftime("%Y-%m-%dT%H:%M:%SZ")


# ─────────────────────────────────────────────
# DOMAIN 1: HARDWARE (50 scenarios)
# ─────────────────────────────────────────────

def hardware_scenarios():
    scenarios = []

    # H01–H08: Card Reader Faults
    for i in range(1, 9):
        jammed = i <= 4
        scenarios.append({
            "scenario_id": f"H{str(i).zfill(3)}",
            "domain": "Hardware",
            "sub_domain": "Card Reader",
            "atm_id": random.choice(ATM_IDS),
            "timestamp": rand_ts(),
            "error_codes": ["3A1" if jammed else "3A5",
                            "ICM001" if jammed else "ICM004"],
            "sensor_readings": {
                "card_reader_status": "JAMMED" if jammed else "DIRTY_SENSOR",
                "card_reader_cycles": random.randint(50000, 250000),
                "card_present_sensor": "STUCK" if jammed else "INTERMITTENT",
                "cash_level_pct": random.randint(20, 80),
                "temperature_c": random.randint(20, 35),
                "door_open": False
            },
            "transaction_context": {
                "last_transaction_status": "FAILED",
                "last_error": "CARD_NOT_EJECTED" if jammed else "READ_ERROR",
                "transactions_last_hour": random.randint(0, 5),
                "card_insertions_since_last_service": random.randint(100, 500)
            },
            "facts": {
                "card_reader_fault": True,
                "card_jammed": jammed,
                "dirty_reader": not jammed,
                "atm_operational": False,
                "requires_engineer": jammed,
                "self_recoverable": not jammed
            },
            "expected_diagnosis": "Card Reader Jam" if jammed else "Card Reader Dirty / Sensor Fault",
            "expected_severity": "HIGH" if jammed else "MEDIUM",
            "expected_resolution": (
                ["Take ATM out of service", "Open card reader access panel",
                 "Carefully remove jammed card using extraction tool",
                 "Inspect reader rollers for damage", "Run card reader self-test",
                 "Return ATM to service and monitor"] if jammed else
                ["Display maintenance alert to operator",
                 "Run card reader cleaning cycle using cleaning card",
                 "If cleaning fails, schedule engineer visit for sensor replacement",
                 "Log incident and monitor for recurrence"]
            ),
            "notes": f"Scenario {'H' + str(i).zfill(3)}: Card reader {'jam' if jammed else 'dirty sensor'} detected via ICM status code."
        })

    # H09–H16: Cash Dispenser Mechanical Faults
    fault_types = [
        ("DISPENSER_JAM", "4B1", "Cash Dispenser Jam", "HIGH",
         ["Take ATM out of service", "Open dispenser access panel",
          "Remove jammed notes carefully", "Check for torn notes in transport path",
          "Run dispenser self-test", "Return to service"]),
        ("ACTUATOR_WORN", "4B8", "Dispenser Actuator Wear Warning", "MEDIUM",
         ["Schedule preventive maintenance within 48 hours",
          "Log actuator cycle count", "Order replacement actuator",
          "Monitor dispense success rate closely"]),
        ("REJECT_BIN_FULL", "4C2", "Reject Bin Full", "MEDIUM",
         ["Alert branch staff to empty reject bin",
          "Verify reject bin sensor is functional after emptying",
          "Log rejected note count for audit"]),
        ("PRESENTER_FAULT", "4D1", "Cash Presenter Fault", "HIGH",
         ["Take ATM out of service",
          "Inspect presenter mechanism for obstruction",
          "Run presenter self-test", "If fault persists, escalate to Tier-2"]),
    ]
    for idx, (status, code, diag, sev, res) in enumerate(fault_types * 2):
        i = 9 + idx
        scenarios.append({
            "scenario_id": f"H{str(i).zfill(3)}",
            "domain": "Hardware",
            "sub_domain": "Cash Dispenser",
            "atm_id": random.choice(ATM_IDS),
            "timestamp": rand_ts(),
            "error_codes": [code, "DISP_ERR_" + str(random.randint(10, 99))],
            "sensor_readings": {
                "dispenser_status": status,
                "dispenser_cycles": random.randint(100000, 800000),
                "reject_bin_level_pct": 95 if status == "REJECT_BIN_FULL" else random.randint(10, 60),
                "cash_level_pct": random.randint(20, 90),
                "temperature_c": random.randint(20, 38)
            },
            "transaction_context": {
                "last_transaction_status": "FAILED",
                "last_error": status,
                "dispense_failures_today": random.randint(1, 15)
            },
            "facts": {
                "dispenser_fault": True,
                "dispenser_status": status,
                "atm_operational": status in ("ACTUATOR_WORN",),
                "requires_engineer": status in ("DISPENSER_JAM", "PRESENTER_FAULT"),
                "self_recoverable": status == "REJECT_BIN_FULL"
            },
            "expected_diagnosis": diag,
            "expected_severity": sev,
            "expected_resolution": res,
            "notes": f"Scenario H{str(i).zfill(3)}: {diag} detected via dispenser status sensor."
        })

    # H17–H25: Receipt Printer Faults
    printer_faults = [
        ("PAPER_OUT", "5E1", "Printer Paper Out", "LOW",
         ["Alert branch staff to reload receipt paper",
          "Confirm paper loaded correctly and sensor clears",
          "Print test receipt to verify"]),
        ("PAPER_JAM", "5E3", "Printer Paper Jam", "MEDIUM",
         ["Open printer access cover", "Remove jammed paper",
          "Check paper path for torn fragments",
          "Reload paper and run test print"]),
        ("PRINT_HEAD_FAIL", "5E7", "Print Head Failure", "HIGH",
         ["Take printer offline", "Schedule print head replacement",
          "ATM can continue operating in receipt-suppress mode if policy allows"]),
    ]
    for idx, (status, code, diag, sev, res) in enumerate(printer_faults * 3):
        i = 17 + idx
        if i > 25:
            break
        scenarios.append({
            "scenario_id": f"H{str(i).zfill(3)}",
            "domain": "Hardware",
            "sub_domain": "Receipt Printer",
            "atm_id": random.choice(ATM_IDS),
            "timestamp": rand_ts(),
            "error_codes": [code],
            "sensor_readings": {
                "printer_status": status,
                "paper_level_pct": 0 if status == "PAPER_OUT" else random.randint(10, 80),
                "print_head_temp_c": random.randint(40, 90),
                "temperature_c": random.randint(20, 35)
            },
            "transaction_context": {
                "last_transaction_status": "PARTIAL" if status == "PAPER_OUT" else "FAILED",
                "last_error": status
            },
            "facts": {
                "printer_fault": True,
                "printer_status": status,
                "atm_operational": status in ("PAPER_OUT",),
                "self_recoverable": status in ("PAPER_OUT", "PAPER_JAM"),
                "requires_engineer": status == "PRINT_HEAD_FAIL"
            },
            "expected_diagnosis": diag,
            "expected_severity": sev,
            "expected_resolution": res,
            "notes": f"Scenario H{str(i).zfill(3)}: {diag}."
        })

    # H26–H35: Sensor & Environmental Faults
    sensor_faults = [
        ("TEMP_HIGH", "9T1", "Overheating — Temperature Critical", "HIGH",
         ["Immediately take ATM out of service",
          "Check that ventilation slots are unobstructed",
          "Inspect cooling fan operation", "Do not restart until temperature normalises",
          "Escalate to Tier-2 if fan is faulty"]),
        ("DOOR_OPEN", "9D1", "ATM Enclosure Door Open", "CRITICAL",
         ["Immediately alert branch security and ATM operations team",
          "Do not process transactions", "Secure ATM physically",
          "Review CCTV footage", "Log security incident"]),
        ("SENSOR_FAULT", "9S2", "General Sensor Malfunction", "MEDIUM",
         ["Run ATM self-diagnostics", "Identify which sensor is reporting fault",
          "Schedule engineer visit if sensor cannot self-recover"]),
        ("VOLTAGE_UNSTABLE", "9V3", "Power / Voltage Instability", "HIGH",
         ["Take ATM out of service", "Check UPS unit and power supply",
          "Do not restart until power is stable",
          "Escalate to facilities/Tier-2"]),
        ("FAN_FAULT", "9F1", "Cooling Fan Failure", "HIGH",
         ["Take ATM out of service to prevent overheating",
          "Schedule immediate fan replacement",
          "Monitor temperature until engineer arrives"]),
    ]
    for idx, (status, code, diag, sev, res) in enumerate(sensor_faults * 2):
        i = 26 + idx
        if i > 35:
            break
        scenarios.append({
            "scenario_id": f"H{str(i).zfill(3)}",
            "domain": "Hardware",
            "sub_domain": "Sensors & Environment",
            "atm_id": random.choice(ATM_IDS),
            "timestamp": rand_ts(),
            "error_codes": [code],
            "sensor_readings": {
                "fault_type": status,
                "temperature_c": random.randint(55, 80) if "TEMP" in status or "FAN" in status else random.randint(20, 35),
                "door_open": status == "DOOR_OPEN",
                "voltage_v": random.uniform(10.5, 11.0) if "VOLTAGE" in status else 12.0,
                "fan_rpm": 0 if status == "FAN_FAULT" else random.randint(1800, 3000)
            },
            "transaction_context": {
                "last_transaction_status": "ABORTED",
                "last_error": status
            },
            "facts": {
                "environmental_fault": True,
                "fault_type": status,
                "atm_operational": False,
                "requires_engineer": status in ("DOOR_OPEN", "VOLTAGE_UNSTABLE", "FAN_FAULT", "TEMP_HIGH"),
                "security_alert": status == "DOOR_OPEN"
            },
            "expected_diagnosis": diag,
            "expected_severity": sev,
            "expected_resolution": res,
            "notes": f"Scenario H{str(i).zfill(3)}: {diag}."
        })

    # H36–H50: Keypad / Screen / Miscellaneous Hardware
    misc_faults = [
        ("PINPAD_UNRESPONSIVE", "6P1", "PIN Pad Unresponsive", "HIGH",
         ["Take ATM out of service", "Run PIN pad self-test",
          "Check PIN pad cable connections", "Replace PIN pad if self-test fails",
          "Log incident — treat as potential tamper until confirmed otherwise"]),
        ("SCREEN_BLANK", "6S2", "Display Screen Failure", "HIGH",
         ["Take ATM out of service", "Check display cable connection",
          "Run screen diagnostic", "Schedule screen replacement if fault persists"]),
        ("CAMERA_OFFLINE", "6C1", "ATM Camera Offline", "MEDIUM",
         ["Alert security/IT team", "ATM may continue operating subject to policy",
          "Schedule camera repair within 24 hours",
          "Review last recorded footage for anomalies"]),
        ("UPS_LOW", "9U1", "UPS Battery Low — Replace Soon", "MEDIUM",
         ["Schedule UPS battery replacement within 7 days",
          "Monitor for power fluctuations in the interim"]),
        ("BARCODE_READER_FAIL", "6B3", "Barcode / QR Reader Fault", "LOW",
         ["Run reader self-test", "Clean reader lens",
          "If fault persists, schedule replacement"]),
    ]
    for idx, (status, code, diag, sev, res) in enumerate(misc_faults * 3):
        i = 36 + idx
        if i > 50:
            break
        scenarios.append({
            "scenario_id": f"H{str(i).zfill(3)}",
            "domain": "Hardware",
            "sub_domain": "Peripherals",
            "atm_id": random.choice(ATM_IDS),
            "timestamp": rand_ts(),
            "error_codes": [code],
            "sensor_readings": {
                "peripheral_status": status,
                "temperature_c": random.randint(20, 35),
                "door_open": False
            },
            "transaction_context": {
                "last_transaction_status": "FAILED",
                "last_error": status
            },
            "facts": {
                "peripheral_fault": True,
                "peripheral_type": status.split("_")[0].lower(),
                "atm_operational": status in ("CAMERA_OFFLINE", "UPS_LOW", "BARCODE_READER_FAIL"),
                "requires_engineer": status in ("PINPAD_UNRESPONSIVE", "SCREEN_BLANK"),
                "security_alert": status == "PINPAD_UNRESPONSIVE"
            },
            "expected_diagnosis": diag,
            "expected_severity": sev,
            "expected_resolution": res,
            "notes": f"Scenario H{str(i).zfill(3)}: {diag}."
        })

    return scenarios[:50]


# ─────────────────────────────────────────────
# DOMAIN 2: SOFTWARE (35 scenarios)
# ─────────────────────────────────────────────

def software_scenarios():
    scenarios = []

    sw_faults = [
        # (sub_domain, error_code, diagnosis, severity, resolution)
        ("OS", "SW001", "OS Kernel Panic / Blue Screen", "CRITICAL",
         ["Immediately take ATM out of service",
          "Attempt controlled restart via remote management console",
          "If restart fails, escalate to Tier-2 for on-site OS recovery",
          "Review kernel crash dump logs"]),
        ("OS", "SW002", "OS Disk Space Critical", "HIGH",
         ["Clear ATM transaction log archives beyond retention policy",
          "Delete temporary files", "Alert Tier-2 to expand disk allocation",
          "Monitor disk usage after cleanup"]),
        ("Application", "SW010", "ATM Application Crash", "HIGH",
         ["Restart ATM application via remote console",
          "Review application error log for root cause",
          "If crash recurs within 1 hour, escalate to Tier-2",
          "Check for pending application updates"]),
        ("Application", "SW011", "Application Version Mismatch", "MEDIUM",
         ["Verify which ATM firmware/application version is installed",
          "Push correct version via remote update",
          "Restart ATM application after update",
          "Confirm version matches fleet baseline"]),
        ("Application", "SW012", "Application Deadlock Detected", "HIGH",
         ["Restart ATM application",
          "Review deadlock trace log",
          "Report to software vendor if recurring"]),
        ("Application", "SW013", "Configuration File Corrupt", "HIGH",
         ["Restore last known good configuration from backup",
          "Restart ATM application",
          "Verify configuration values match expected"]),
        ("Firmware", "SW020", "Firmware Update Failed", "HIGH",
         ["Do not restart ATM mid-update",
          "Attempt update retry via remote console",
          "If retry fails, escalate to Tier-2 for manual firmware recovery"]),
        ("Firmware", "SW021", "Firmware Version Mismatch", "MEDIUM",
         ["Push correct firmware version remotely",
          "Verify firmware signature before applying",
          "Restart ATM after firmware update"]),
        ("Database", "SW030", "Transaction Database Unreachable", "CRITICAL",
         ["Check database server connectivity",
          "Verify ATM can reach bank core system",
          "If DB server is down, escalate to IT/Tier-2 immediately",
          "ATM must remain out of service until DB is restored"]),
        ("Database", "SW031", "Transaction Log Full", "HIGH",
         ["Archive and purge old transaction logs",
          "Confirm log rotation policy is active",
          "Resume ATM operation after log space freed"]),
        ("Security Software", "SW040", "Anti-Tamper Software Alert", "CRITICAL",
         ["Immediately take ATM out of service",
          "Alert fraud and security team",
          "Do not restart without security team clearance",
          "Preserve all logs for forensic review"]),
        ("Security Software", "SW041", "Certificate / TLS Expiry", "HIGH",
         ["Renew TLS certificate via certificate management system",
          "Restart ATM network services after renewal",
          "Verify all communications are re-encrypted"]),
        ("Security Software", "SW042", "Encryption Key Rotation Overdue", "HIGH",
         ["Initiate key rotation via HSM management console",
          "Verify new key is distributed to ATM",
          "Log key rotation completion for compliance"]),
        ("Diagnostics", "SW050", "Self-Test Failure at Startup", "HIGH",
         ["Review self-test failure log",
          "Identify failing component (hardware or software)",
          "Resolve underlying component fault before returning ATM to service"]),
        ("Diagnostics", "SW051", "Scheduled Maintenance Mode Stuck", "MEDIUM",
         ["Force-exit maintenance mode via remote console",
          "Verify ATM returns to operational state",
          "Review maintenance schedule configuration"]),
        ("Remote Management", "SW060", "Remote Management Agent Offline", "MEDIUM",
         ["Attempt to ping ATM from operations centre",
          "If unreachable, dispatch field engineer to restart remote agent",
          "Review network path for connectivity issues"]),
        ("Remote Management", "SW061", "Software Patch Failed to Apply", "MEDIUM",
         ["Retry patch deployment from software distribution server",
          "Review patch compatibility with current ATM version",
          "Escalate to vendor if patch repeatedly fails"]),
        ("Watchdog", "SW070", "Watchdog Timer Restart Loop", "HIGH",
         ["Identify which process is causing watchdog resets",
          "Review application and OS logs",
          "Escalate to Tier-2 if loop continues after restart"]),
        ("Watchdog", "SW071", "Memory Leak Detected", "HIGH",
         ["Schedule ATM restart during low-traffic window",
          "Report memory leak to application vendor",
          "Monitor memory usage after restart"]),
        ("Startup", "SW080", "ATM Failed to Boot", "CRITICAL",
         ["Check power supply and UPS",
          "Attempt remote restart",
          "If no response, dispatch field engineer",
          "Check for disk errors and OS integrity on-site"]),
    ]

    for idx, (sub, code, diag, sev, res) in enumerate(sw_faults):
        i = idx + 1
        scenarios.append({
            "scenario_id": f"S{str(i).zfill(3)}",
            "domain": "Software",
            "sub_domain": sub,
            "atm_id": random.choice(ATM_IDS),
            "timestamp": rand_ts(),
            "error_codes": [code, f"SYS_{random.randint(100,999)}"],
            "sensor_readings": {
                "software_status": "FAULT",
                "cpu_usage_pct": random.randint(60, 100) if "DEADLOCK" in diag or "MEMORY" in diag else random.randint(10, 60),
                "memory_usage_pct": random.randint(85, 100) if "MEMORY" in diag else random.randint(30, 75),
                "disk_usage_pct": random.randint(90, 99) if "DISK" in diag else random.randint(40, 80),
                "uptime_hours": random.randint(1, 720),
                "temperature_c": random.randint(20, 35)
            },
            "transaction_context": {
                "last_transaction_status": "FAILED",
                "last_error": code,
                "transactions_last_hour": random.randint(0, 3)
            },
            "facts": {
                "software_fault": True,
                "sub_domain": sub.lower().replace(" ", "_"),
                "error_code": code,
                "atm_operational": sev in ("LOW", "MEDIUM"),
                "requires_remote_action": True,
                "requires_engineer": sev == "CRITICAL",
                "security_alert": sub == "Security Software"
            },
            "expected_diagnosis": diag,
            "expected_severity": sev,
            "expected_resolution": res,
            "notes": f"Scenario S{str(i).zfill(3)}: {diag}. Sub-domain: {sub}."
        })

    # Top-up to 35 by repeating with varied ATM IDs
    while len(scenarios) < 35:
        template = random.choice(scenarios[:20])
        clone = dict(template)
        clone["scenario_id"] = f"S{str(len(scenarios)+1).zfill(3)}"
        clone["atm_id"] = random.choice(ATM_IDS)
        clone["timestamp"] = rand_ts()
        scenarios.append(clone)

    return scenarios[:35]


# ─────────────────────────────────────────────
# DOMAIN 3: NETWORK (35 scenarios)
# ─────────────────────────────────────────────

def network_scenarios():
    scenarios = []

    net_faults = [
        ("Connectivity", "NET001", "ATM Offline — No Network Response", "CRITICAL",
         ["Ping ATM from operations centre", "Check LAN cable and switch port",
          "Verify router/firewall rules allow ATM traffic",
          "If physically unreachable, dispatch engineer"]),
        ("Connectivity", "NET002", "Intermittent Network Drops", "HIGH",
         ["Review ATM connection logs for drop frequency",
          "Check LAN cable for damage",
          "Test switch port and replace if faulty",
          "Monitor stability after fix"]),
        ("Connectivity", "NET003", "High Network Latency", "MEDIUM",
         ["Run traceroute from ATM to bank core system",
          "Identify bottleneck hop",
          "Escalate to network team to investigate"]),
        ("Connectivity", "NET004", "DNS Resolution Failure", "HIGH",
         ["Verify DNS server IP configured on ATM",
          "Test DNS resolution from ATM",
          "Update DNS settings if misconfigured"]),
        ("TLS/Security", "NET010", "TLS Handshake Failure", "HIGH",
         ["Check ATM TLS certificate validity",
          "Verify cipher suite compatibility with bank server",
          "Renew certificate if expired",
          "Test TLS connection after fix"]),
        ("TLS/Security", "NET011", "SSL Certificate Mismatch", "HIGH",
         ["Identify certificate mismatch details",
          "Push correct certificate to ATM",
          "Restart network services"]),
        ("TLS/Security", "NET012", "Man-in-the-Middle Warning", "CRITICAL",
         ["Immediately take ATM out of service",
          "Alert security and fraud teams",
          "Do not resume until network path is verified clean",
          "Preserve all network logs"]),
        ("Host Connectivity", "NET020", "Cannot Reach Bank Core System", "CRITICAL",
         ["Verify bank core system is online",
          "Check firewall rules between ATM and core",
          "Test connectivity to core system IP directly",
          "Escalate to IT if core is unreachable"]),
        ("Host Connectivity", "NET021", "Connection Timeout to Core System", "HIGH",
         ["Increase ATM timeout setting temporarily",
          "Investigate core system load",
          "Monitor for resolution or escalate to IT"]),
        ("Host Connectivity", "NET022", "Authentication Rejected by Core", "HIGH",
         ["Verify ATM authentication credentials",
          "Re-register ATM with core system if credentials expired",
          "Escalate to Tier-2 if re-registration fails"]),
        ("VPN", "NET030", "VPN Tunnel Down", "CRITICAL",
         ["Restart VPN client on ATM",
          "Verify VPN server availability",
          "Re-authenticate VPN session",
          "Escalate to network team if tunnel fails to re-establish"]),
        ("VPN", "NET031", "VPN Authentication Failed", "HIGH",
         ["Check VPN credentials and certificate",
          "Renew VPN certificate if expired",
          "Escalate to network team"]),
        ("Firewall", "NET040", "ATM Traffic Blocked by Firewall", "HIGH",
         ["Review firewall logs for ATM IP",
          "Identify which port/protocol is blocked",
          "Update firewall rule to allow ATM traffic",
          "Test ATM connectivity after rule change"]),
        ("Firewall", "NET041", "IP Address Conflict", "MEDIUM",
         ["Identify conflicting device on network",
          "Assign unique static IP to ATM",
          "Update DNS/DHCP records",
          "Test ATM connectivity"]),
        ("Switch/Router", "NET050", "Network Switch Port Down", "HIGH",
         ["Check switch port status remotely",
          "Re-enable port or migrate ATM to working port",
          "Replace switch if port failure is hardware-related"]),
        ("Switch/Router", "NET051", "Router Unreachable", "CRITICAL",
         ["Attempt to reach router management interface",
          "If router is down, escalate to network team immediately",
          "ATM will remain offline until router is restored"]),
        ("Bandwidth", "NET060", "Bandwidth Saturation", "MEDIUM",
         ["Review network utilisation on ATM segment",
          "Identify other devices consuming excessive bandwidth",
          "Implement QoS to prioritise ATM traffic"]),
        ("Bandwidth", "NET061", "Packet Loss Exceeding Threshold", "HIGH",
         ["Run packet loss test from ATM to core",
          "Check for faulty cable or switch",
          "Escalate to ISP if loss is on WAN link"]),
        ("NTP", "NET070", "Clock Sync Failure (NTP)", "MEDIUM",
         ["Verify NTP server is reachable from ATM",
          "Update NTP server IP if changed",
          "Force NTP sync and verify ATM clock"]),
        ("NTP", "NET071", "ATM Clock Drift Detected", "MEDIUM",
         ["Force NTP resync",
          "If drift recurs, check NTP configuration",
          "Alert compliance team if clock drift exceeds regulatory threshold"]),
    ]

    for idx, (sub, code, diag, sev, res) in enumerate(net_faults):
        i = idx + 1
        scenarios.append({
            "scenario_id": f"N{str(i).zfill(3)}",
            "domain": "Network",
            "sub_domain": sub,
            "atm_id": random.choice(ATM_IDS),
            "timestamp": rand_ts(),
            "error_codes": [code, f"NET_ERR_{random.randint(10, 99)}"],
            "sensor_readings": {
                "network_status": "FAULT",
                "ping_latency_ms": random.randint(500, 5000) if "LATENCY" in diag else None,
                "packet_loss_pct": random.randint(20, 100) if "PACKET" in diag else 0,
                "vpn_status": "DOWN" if "VPN" in sub else "UP",
                "last_successful_ping_mins_ago": random.randint(5, 120),
                "temperature_c": random.randint(20, 35)
            },
            "transaction_context": {
                "last_transaction_status": "FAILED",
                "last_error": code,
                "transactions_last_hour": 0
            },
            "facts": {
                "network_fault": True,
                "sub_domain": sub.lower().replace("/", "_").replace(" ", "_"),
                "atm_operational": False,
                "requires_network_team": True,
                "requires_engineer": sev == "CRITICAL" and sub == "Connectivity",
                "security_alert": "MAN-IN-THE-MIDDLE" in diag.upper()
            },
            "expected_diagnosis": diag,
            "expected_severity": sev,
            "expected_resolution": res,
            "notes": f"Scenario N{str(i).zfill(3)}: {diag}. Sub-domain: {sub}."
        })

    while len(scenarios) < 35:
        template = random.choice(scenarios[:20])
        clone = dict(template)
        clone["scenario_id"] = f"N{str(len(scenarios)+1).zfill(3)}"
        clone["atm_id"] = random.choice(ATM_IDS)
        clone["timestamp"] = rand_ts()
        scenarios.append(clone)

    return scenarios[:35]


# ─────────────────────────────────────────────
# DOMAIN 4: CASH HANDLING (40 scenarios)
# ─────────────────────────────────────────────

def cash_scenarios():
    scenarios = []

    cash_faults = [
        ("Cassette", "CSH001", "Cash Cassette Empty", "HIGH",
         ["Alert branch staff and ATM operations team",
          "Take ATM out of service",
          "Replenish cash cassette following dual-control procedures",
          "Verify cassette is correctly seated and locked",
          "Return ATM to service and verify dispense test"]),
        ("Cassette", "CSH002", "Cash Cassette Low — Alert", "MEDIUM",
         ["Schedule cash replenishment within 2 hours",
          "Monitor transaction count to estimate time-to-empty",
          "Alert cash-in-transit team"]),
        ("Cassette", "CSH003", "Cassette Not Detected / Not Seated", "HIGH",
         ["Check cassette is correctly inserted and locked",
          "Remove and re-seat cassette",
          "If not detected after re-seating, run cassette sensor test",
          "Escalate to Tier-2 if sensor fault"]),
        ("Cassette", "CSH004", "Wrong Cassette Denomination Loaded", "HIGH",
         ["Immediately take ATM out of service",
          "Remove and verify cassette contents",
          "Reload correct denomination cassette",
          "Update cassette denomination record in ATM system",
          "Perform balancing check"]),
        ("Cassette", "CSH005", "Cassette Lock Fault", "MEDIUM",
         ["Do not operate ATM with unsecured cassette",
          "Inspect cassette lock mechanism",
          "Replace cassette if lock is damaged",
          "Escalate if ATM enclosure integrity is compromised"]),
        ("Note Handling", "CSH010", "Note Jam in Transport Path", "HIGH",
         ["Take ATM out of service",
          "Open access panel and clear note jam",
          "Inspect transport rollers for damage",
          "Run self-test after clearing jam",
          "Return to service and monitor"]),
        ("Note Handling", "CSH011", "Multiple Note Feed (Double Take)", "HIGH",
         ["Take ATM out of service",
          "Run note thickness calibration",
          "Inspect separator rollers for wear",
          "Test with known note count before returning to service"]),
        ("Note Handling", "CSH012", "Torn / Mutilated Note Detected", "MEDIUM",
         ["Rejected notes are placed in reject bin automatically",
          "Review reject bin contents during next cassette replenishment",
          "Remove mutilated notes from circulation"]),
        ("Note Handling", "CSH013", "High Reject Rate — Notes", "HIGH",
         ["Inspect note quality in cassette",
          "Remove worn or damaged notes",
          "Run note acceptor calibration",
          "If reject rate persists, escalate to Tier-2"]),
        ("Counting", "CSH020", "Dispense Count Mismatch", "CRITICAL",
         ["Immediately take ATM out of service",
          "Do not process further transactions",
          "Alert operations and compliance teams",
          "Initiate cash balancing investigation",
          "Preserve all transaction logs for audit"]),
        ("Counting", "CSH021", "Short Dispense Detected", "CRITICAL",
         ["Take ATM out of service immediately",
          "Review dispense log for affected transactions",
          "Initiate customer dispute and refund process",
          "Inspect dispenser for mechanical cause",
          "Report to compliance team"]),
        ("Counting", "CSH022", "Over-Dispense Detected", "CRITICAL",
         ["Take ATM out of service immediately",
          "Alert operations and compliance teams",
          "Preserve logs",
          "Initiate loss investigation and cash balancing"]),
        ("Balancing", "CSH030", "Cash Balance Discrepancy at EOD", "HIGH",
         ["Run end-of-day balancing report",
          "Cross-reference with transaction log",
          "Identify discrepant transactions",
          "Escalate to operations if discrepancy exceeds threshold"]),
        ("Balancing", "CSH031", "Cassette Inventory Mismatch", "HIGH",
         ["Verify physical cassette contents against system record",
          "Correct inventory record if loading error occurred",
          "Investigate if notes are missing beyond loading variance"]),
        ("Currency Detector", "CSH040", "Counterfeit Note Detected", "CRITICAL",
         ["ATM should automatically reject and retain detected note",
          "Alert branch security and operations team",
          "Do not return note to circulation",
          "Submit note to bank's currency verification team",
          "Log incident for regulatory reporting"]),
        ("Currency Detector", "CSH041", "Currency Detector Fault", "HIGH",
         ["Take ATM out of service",
          "Run currency detector self-test",
          "If test fails, schedule replacement of detector module",
          "ATM must not accept deposits until detector is verified"]),
        ("Recycling", "CSH050", "Recycler Module Fault", "HIGH",
         ["Take recycler offline",
          "Run recycler self-test",
          "If test fails, escalate to Tier-2 for module replacement"]),
        ("Recycling", "CSH051", "Recycled Note Rejected by Validator", "MEDIUM",
         ["Inspect recycled note quality",
          "Run validator calibration",
          "Remove poor-quality notes from recycler"]),
        ("Security", "CSH060", "Cash Vault Door Open Alert", "CRITICAL",
         ["Immediately alert branch security",
          "Do not process transactions",
          "Verify physical security of vault",
          "Review CCTV footage",
          "Escalate to security team and log incident"]),
        ("Security", "CSH061", "Cash Replenishment Anomaly", "HIGH",
         ["Verify replenishment was authorised and followed dual-control",
          "Cross-check replenishment record against physical count",
          "Escalate to operations and compliance if anomaly confirmed"]),
    ]

    for idx, (sub, code, diag, sev, res) in enumerate(cash_faults):
        i = idx + 1
        scenarios.append({
            "scenario_id": f"C{str(i).zfill(3)}",
            "domain": "Cash Handling",
            "sub_domain": sub,
            "atm_id": random.choice(ATM_IDS),
            "timestamp": rand_ts(),
            "error_codes": [code, f"CASH_{random.randint(10,99)}"],
            "sensor_readings": {
                "cash_level_pct": 0 if "EMPTY" in diag else random.randint(5, 95),
                "cassette_seated": "NO" if "NOT SEATED" in diag.upper() else "YES",
                "reject_bin_level_pct": random.randint(10, 90),
                "vault_door_open": sub == "Security" and "VAULT" in diag.upper(),
                "currency_detector_status": "FAULT" if "DETECTOR" in diag.upper() else "OK",
                "temperature_c": random.randint(20, 35)
            },
            "transaction_context": {
                "last_transaction_status": "FAILED" if sev in ("HIGH", "CRITICAL") else "SUCCESS",
                "last_error": code,
                "dispense_attempts_today": random.randint(50, 300),
                "reject_count_today": random.randint(0, 20)
            },
            "facts": {
                "cash_handling_fault": True,
                "sub_domain": sub.lower().replace(" ", "_"),
                "atm_operational": sev == "LOW",
                "requires_cash_replenishment": "EMPTY" in diag.upper() or "LOW" in diag.upper(),
                "requires_engineer": sev == "CRITICAL" or "DETECTOR" in diag.upper(),
                "security_alert": sub == "Security" or "COUNTERFEIT" in diag.upper(),
                "compliance_alert": sev == "CRITICAL"
            },
            "expected_diagnosis": diag,
            "expected_severity": sev,
            "expected_resolution": res,
            "notes": f"Scenario C{str(i).zfill(3)}: {diag}. Sub-domain: {sub}."
        })

    while len(scenarios) < 40:
        template = random.choice(scenarios[:20])
        clone = dict(template)
        clone["scenario_id"] = f"C{str(len(scenarios)+1).zfill(3)}"
        clone["atm_id"] = random.choice(ATM_IDS)
        clone["timestamp"] = rand_ts()
        scenarios.append(clone)

    return scenarios[:40]


# ─────────────────────────────────────────────
# DOMAIN 5: SECURITY / FRAUD (40 scenarios)
# ─────────────────────────────────────────────

def security_scenarios():
    scenarios = []

    sec_faults = [
        ("Card Skimming", "SEC001", "Card Skimmer Device Detected", "CRITICAL",
         ["Immediately take ATM out of service",
          "Alert fraud team and branch security",
          "Do not remove skimmer — preserve for forensics",
          "Secure ATM perimeter",
          "Alert police if appropriate",
          "Identify potentially compromised cards from transaction log",
          "Initiate card re-issuance process for affected customers"]),
        ("Card Skimming", "SEC002", "Card Reader Depth Anomaly (Possible Skimmer)", "CRITICAL",
         ["Take ATM out of service",
          "Physically inspect card reader for overlay device",
          "Alert fraud team",
          "If skimmer found, treat as SEC001"]),
        ("Card Skimming", "SEC003", "Unusual Card Read Failures — Possible Shimmer", "HIGH",
         ["Alert fraud team for inspection",
          "Review card read error rate trend",
          "Inspect card reader internally if error rate is abnormal",
          "Take ATM out of service if shimmer is suspected"]),
        ("PIN Pad Tampering", "SEC010", "PIN Pad Cover Removal Detected", "CRITICAL",
         ["Immediately take ATM out of service",
          "Alert fraud team and branch security",
          "Treat as confirmed tamper attempt",
          "Preserve PIN pad for forensic examination",
          "Identify transactions processed since last verified inspection"]),
        ("PIN Pad Tampering", "SEC011", "PIN Pad Enclosure Breach Sensor Triggered", "CRITICAL",
         ["Take ATM out of service",
          "Alert security team immediately",
          "Do not attempt to operate ATM",
          "Log time and alert security/police if appropriate"]),
        ("PIN Pad Tampering", "SEC012", "Suspicious PIN Pad Overlay Pattern", "HIGH",
         ["Alert fraud team for physical inspection",
          "Compare PIN pad appearance to reference photos",
          "If overlay confirmed, treat as SEC010"]),
        ("Transaction Fraud", "SEC020", "Unusual Transaction Volume — Velocity Alert", "HIGH",
         ["Review transaction log for the flagged ATM",
          "Identify if a single card or multiple cards triggered the alert",
          "Alert fraud monitoring team",
          "Temporarily block suspicious cards if fraud is confirmed"]),
        ("Transaction Fraud", "SEC021", "Repeated Declined Transactions — Brute Force", "HIGH",
         ["Alert fraud team",
          "Identify source card(s)",
          "Temporarily block card if brute force is confirmed",
          "Review CCTV footage of ATM at time of incident"]),
        ("Transaction Fraud", "SEC022", "High-Value Withdrawal Cluster", "HIGH",
         ["Alert fraud team",
          "Cross-reference with known compromise patterns",
          "Contact cardholder to verify if transactions are genuine"]),
        ("Transaction Fraud", "SEC023", "Card Present + Geolocation Mismatch", "HIGH",
         ["Alert fraud team",
          "Verify with card issuer if card has been reported lost/stolen",
          "Block card if confirmed fraudulent"]),
        ("Physical Attack", "SEC030", "ATM Anti-Ram Sensor Triggered", "CRITICAL",
         ["Immediately alert police and security",
          "Do not approach ATM",
          "ATM auto-locks and inks cash (if ink cartridge fitted)",
          "Preserve CCTV footage",
          "Notify bank operations centre"]),
        ("Physical Attack", "SEC031", "Explosive Gas Detection Alert", "CRITICAL",
         ["Immediately evacuate branch",
          "Alert police and fire services",
          "Do not approach ATM",
          "Notify bank security and operations centre"]),
        ("Physical Attack", "SEC032", "ATM Enclosure Vibration Alert", "HIGH",
         ["Alert security team",
          "Review CCTV footage",
          "Dispatch engineer to inspect ATM enclosure",
          "Take ATM out of service if structural damage suspected"]),
        ("Physical Attack", "SEC033", "Safe Door Tamper Sensor Triggered", "CRITICAL",
         ["Alert security and police immediately",
          "Treat as active attack",
          "Do not approach"]),
        ("CCTV / Surveillance", "SEC040", "ATM Camera Offline — Security Risk", "HIGH",
         ["Alert security team",
          "ATM should not operate without surveillance if policy requires it",
          "Dispatch engineer to restore camera",
          "Review last available footage for anomalies"]),
        ("CCTV / Surveillance", "SEC041", "Camera View Obstruction Detected", "HIGH",
         ["Alert security team",
          "Review CCTV footage — possible deliberate obstruction",
          "If obstruction is intentional, treat as fraud risk"]),
        ("Logical Security", "SEC050", "Failed Admin Login Attempts Threshold", "HIGH",
         ["Lock admin account after threshold breached",
          "Alert IT security team",
          "Review audit log for source of attempts",
          "Reset credentials through secure process"]),
        ("Logical Security", "SEC051", "Unauthorised Remote Access Attempt", "CRITICAL",
         ["Alert IT security team immediately",
          "Review firewall and access logs",
          "Block source IP if identified",
          "Conduct full security audit of ATM"]),
        ("Logical Security", "SEC052", "Malware Signature Detected on ATM OS", "CRITICAL",
         ["Immediately take ATM out of service",
          "Alert security and IT teams",
          "Isolate ATM from network",
          "Initiate malware removal and OS integrity verification",
          "Do not return to service until clean bill of health"]),
        ("Compliance", "SEC060", "PCI-DSS Compliance Check Failed", "HIGH",
         ["Identify which PCI control has failed",
          "Alert compliance team",
          "Remediate failed control",
          "Re-run compliance check before returning ATM to full service"]),
    ]

    for idx, (sub, code, diag, sev, res) in enumerate(sec_faults):
        i = idx + 1
        scenarios.append({
            "scenario_id": f"F{str(i).zfill(3)}",
            "domain": "Security",
            "sub_domain": sub,
            "atm_id": random.choice(ATM_IDS),
            "timestamp": rand_ts(),
            "error_codes": [code, f"SEC_ERR_{random.randint(10,99)}"],
            "sensor_readings": {
                "tamper_sensor": "TRIGGERED" if any(x in diag.upper() for x in ["TAMPER", "SKIMMER", "BREACH", "ATTACK", "EXPLOSIVE"]) else "OK",
                "door_open": "DOOR" in diag.upper(),
                "camera_status": "OFFLINE" if "CAMERA" in diag.upper() else "ONLINE",
                "anti_skimming_module": "ALERT" if "SKIMM" in diag.upper() else "OK",
                "pinpad_integrity": "FAIL" if "PIN PAD" in diag.upper() else "OK",
                "temperature_c": random.randint(20, 35)
            },
            "transaction_context": {
                "last_transaction_status": "ABORTED",
                "last_error": code,
                "transactions_last_hour": random.randint(0, 50),
                "declined_transactions_last_hour": random.randint(0, 30),
                "suspicious_cards_flagged": random.randint(0, 5)
            },
            "facts": {
                "security_fault": True,
                "sub_domain": sub.lower().replace("/", "_").replace(" ", "_"),
                "atm_operational": False,
                "security_alert": True,
                "fraud_alert": sub in ("Card Skimming", "PIN Pad Tampering", "Transaction Fraud"),
                "physical_attack_alert": sub == "Physical Attack",
                "police_notification_required": any(x in diag.upper() for x in ["EXPLOSIVE", "RAM", "SAFE DOOR"]),
                "compliance_alert": sub == "Compliance"
            },
            "expected_diagnosis": diag,
            "expected_severity": sev,
            "expected_resolution": res,
            "notes": f"Scenario F{str(i).zfill(3)}: {diag}. Sub-domain: {sub}."
        })

    while len(scenarios) < 40:
        template = random.choice(scenarios[:20])
        clone = dict(template)
        clone["scenario_id"] = f"F{str(len(scenarios)+1).zfill(3)}"
        clone["atm_id"] = random.choice(ATM_IDS)
        clone["timestamp"] = rand_ts()
        scenarios.append(clone)

    return scenarios[:40]


# ─────────────────────────────────────────────
# ASSEMBLE & EXPORT
# ─────────────────────────────────────────────

def main():
    print("Generating ATM-Expert benchmark scenarios...")

    all_scenarios = []
    all_scenarios.extend(hardware_scenarios())
    all_scenarios.extend(software_scenarios())
    all_scenarios.extend(network_scenarios())
    all_scenarios.extend(cash_scenarios())
    all_scenarios.extend(security_scenarios())

    assert len(all_scenarios) == 200, f"Expected 200 scenarios, got {len(all_scenarios)}"

    output = {
        "meta": {
            "project": "ATM-Expert — Intelligent ATM Fault Diagnosis & Advisory System",
            "file": "atm_benchmark_scenarios.json",
            "description": "200 benchmark ATM fault scenarios for inference engine evaluation",
            "generated": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
            "total_scenarios": 200,
            "domain_breakdown": {
                "Hardware": 50,
                "Software": 35,
                "Network": 35,
                "Cash Handling": 40,
                "Security": 40
            },
            "severity_breakdown": {
                s: sum(1 for sc in all_scenarios if sc["expected_severity"] == s)
                for s in ["LOW", "MEDIUM", "HIGH", "CRITICAL"]
            },
            "schema_version": "1.0",
            "usage": (
                "Each scenario contains 'facts' (normalised ATM state facts) "
                "to be injected into the inference engine's working memory. "
                "The 'expected_diagnosis', 'expected_severity', and 'expected_resolution' "
                "fields are the ground-truth labels for accuracy evaluation."
            )
        },
        "scenarios": all_scenarios
    }

    # Full scenarios file
    with open("atm_benchmark_scenarios.json", "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"  -> atm_benchmark_scenarios.json  ({len(all_scenarios)} scenarios)")

    # Lightweight index file (no resolution steps — faster to browse)
    index = {
        "meta": output["meta"],
        "scenarios": [
            {
                "scenario_id": sc["scenario_id"],
                "domain": sc["domain"],
                "sub_domain": sc["sub_domain"],
                "atm_id": sc["atm_id"],
                "timestamp": sc["timestamp"],
                "error_codes": sc["error_codes"],
                "expected_diagnosis": sc["expected_diagnosis"],
                "expected_severity": sc["expected_severity"],
                "notes": sc["notes"]
            }
            for sc in all_scenarios
        ]
    }
    with open("atm_benchmark_index.json", "w", encoding="utf-8") as f:
        json.dump(index, f, indent=2, ensure_ascii=False)
    print(f"  -> atm_benchmark_index.json      (lightweight index)")

    print("\nDomain breakdown:")
    for domain, count in output["meta"]["domain_breakdown"].items():
        print(f"  {domain:<18} {count} scenarios")
    print("\nSeverity breakdown:")
    for sev, count in output["meta"]["severity_breakdown"].items():
        print(f"  {sev:<12} {count} scenarios")
    print("\nDone! All files ready for the ATM-Expert inference engine benchmark.")


if __name__ == "__main__":
    main()
