% ATM Expert Knowledge Base - Generated from JSON
:- dynamic fault_profile/5.
:- dynamic fault_description/2.
:- dynamic has_error_code/2.
:- dynamic has_symptom/2.
:- dynamic has_cause/2.
:- dynamic resolution_step/3.

:- discontiguous fault_profile/5.
:- discontiguous fault_description/2.
:- discontiguous has_error_code/2.
:- discontiguous has_symptom/2.
:- discontiguous has_cause/2.
:- discontiguous resolution_step/3.

fault_profile('C_CSH_000', 'Cash Handling', 'Cassette', 'Cash Cassette Empty', 'HIGH').
fault_description('C_CSH_000', 'Cash Cassette Empty').
has_error_code('C_CSH_000', 'CSH001').
has_symptom('C_CSH_000', 'Dispenser status: FAULT').
resolution_step('C_CSH_000', 1, 'Refill/Check Cassette').
resolution_step('C_CSH_000', 2, 'Balance').

fault_profile('C_CSH_001', 'Cash Handling', 'Cassette', 'Cash Cassette Low — Alert', 'MEDIUM').
fault_description('C_CSH_001', 'Cash Cassette Low — Alert').
has_error_code('C_CSH_001', 'CSH002').
has_symptom('C_CSH_001', 'Dispenser status: FAULT').
resolution_step('C_CSH_001', 1, 'Refill/Check Cassette').
resolution_step('C_CSH_001', 2, 'Balance').

fault_profile('C_CSH_002', 'Cash Handling', 'Cassette', 'Cassette Not Detected / Not Seated', 'HIGH').
fault_description('C_CSH_002', 'Cassette Not Detected / Not Seated').
has_error_code('C_CSH_002', 'CSH003').
has_symptom('C_CSH_002', 'Dispenser status: FAULT').
resolution_step('C_CSH_002', 1, 'Refill/Check Cassette').
resolution_step('C_CSH_002', 2, 'Balance').

fault_profile('C_CSH_003', 'Cash Handling', 'Cassette', 'Wrong Cassette Denomination Loaded', 'HIGH').
fault_description('C_CSH_003', 'Wrong Cassette Denomination Loaded').
has_error_code('C_CSH_003', 'CSH004').
has_symptom('C_CSH_003', 'Dispenser status: FAULT').
resolution_step('C_CSH_003', 1, 'Refill/Check Cassette').
resolution_step('C_CSH_003', 2, 'Balance').

fault_profile('C_CSH_004', 'Cash Handling', 'Cassette', 'Cassette Lock Fault', 'MEDIUM').
fault_description('C_CSH_004', 'Cassette Lock Fault').
has_error_code('C_CSH_004', 'CSH005').
has_symptom('C_CSH_004', 'Dispenser status: FAULT').
resolution_step('C_CSH_004', 1, 'Refill/Check Cassette').
resolution_step('C_CSH_004', 2, 'Balance').

fault_profile('C_CSH_005', 'Cash Handling', 'Note Handling', 'Note Jam in Transport Path', 'HIGH').
fault_description('C_CSH_005', 'Note Jam in Transport Path').
has_error_code('C_CSH_005', 'CSH010').
has_symptom('C_CSH_005', 'Dispenser status: FAULT').
resolution_step('C_CSH_005', 1, 'Refill/Check Cassette').
resolution_step('C_CSH_005', 2, 'Balance').

fault_profile('C_CSH_006', 'Cash Handling', 'Note Handling', 'Multiple Note Feed (Double Take)', 'HIGH').
fault_description('C_CSH_006', 'Multiple Note Feed (Double Take)').
has_error_code('C_CSH_006', 'CSH011').
has_symptom('C_CSH_006', 'Dispenser status: FAULT').
resolution_step('C_CSH_006', 1, 'Refill/Check Cassette').
resolution_step('C_CSH_006', 2, 'Balance').

fault_profile('C_CSH_007', 'Cash Handling', 'Note Handling', 'Torn / Mutilated Note Detected', 'MEDIUM').
fault_description('C_CSH_007', 'Torn / Mutilated Note Detected').
has_error_code('C_CSH_007', 'CSH012').
has_symptom('C_CSH_007', 'Dispenser status: FAULT').
resolution_step('C_CSH_007', 1, 'Refill/Check Cassette').
resolution_step('C_CSH_007', 2, 'Balance').

fault_profile('C_CSH_008', 'Cash Handling', 'Note Handling', 'High Reject Rate — Notes', 'HIGH').
fault_description('C_CSH_008', 'High Reject Rate — Notes').
has_error_code('C_CSH_008', 'CSH013').
has_symptom('C_CSH_008', 'Dispenser status: FAULT').
resolution_step('C_CSH_008', 1, 'Refill/Check Cassette').
resolution_step('C_CSH_008', 2, 'Balance').

fault_profile('C_CSH_009', 'Cash Handling', 'Counting', 'Dispense Count Mismatch', 'CRITICAL').
fault_description('C_CSH_009', 'Dispense Count Mismatch').
has_error_code('C_CSH_009', 'CSH020').
has_symptom('C_CSH_009', 'Dispenser status: FAULT').
resolution_step('C_CSH_009', 1, 'Refill/Check Cassette').
resolution_step('C_CSH_009', 2, 'Balance').

fault_profile('C_CSH_010', 'Cash Handling', 'Counting', 'Short Dispense Detected', 'CRITICAL').
fault_description('C_CSH_010', 'Short Dispense Detected').
has_error_code('C_CSH_010', 'CSH021').
has_symptom('C_CSH_010', 'Dispenser status: FAULT').
resolution_step('C_CSH_010', 1, 'Refill/Check Cassette').
resolution_step('C_CSH_010', 2, 'Balance').

fault_profile('C_CSH_011', 'Cash Handling', 'Counting', 'Over-Dispense Detected', 'CRITICAL').
fault_description('C_CSH_011', 'Over-Dispense Detected').
has_error_code('C_CSH_011', 'CSH022').
has_symptom('C_CSH_011', 'Dispenser status: FAULT').
resolution_step('C_CSH_011', 1, 'Refill/Check Cassette').
resolution_step('C_CSH_011', 2, 'Balance').

fault_profile('C_CSH_012', 'Cash Handling', 'Balancing', 'Cash Balance Discrepancy at EOD', 'HIGH').
fault_description('C_CSH_012', 'Cash Balance Discrepancy at EOD').
has_error_code('C_CSH_012', 'CSH030').
has_symptom('C_CSH_012', 'Dispenser status: FAULT').
resolution_step('C_CSH_012', 1, 'Refill/Check Cassette').
resolution_step('C_CSH_012', 2, 'Balance').

fault_profile('C_CSH_013', 'Cash Handling', 'Balancing', 'Cassette Inventory Mismatch', 'HIGH').
fault_description('C_CSH_013', 'Cassette Inventory Mismatch').
has_error_code('C_CSH_013', 'CSH031').
has_symptom('C_CSH_013', 'Dispenser status: FAULT').
resolution_step('C_CSH_013', 1, 'Refill/Check Cassette').
resolution_step('C_CSH_013', 2, 'Balance').

fault_profile('C_CSH_014', 'Cash Handling', 'Currency Detector', 'Counterfeit Note Detected', 'CRITICAL').
fault_description('C_CSH_014', 'Counterfeit Note Detected').
has_error_code('C_CSH_014', 'CSH040').
has_symptom('C_CSH_014', 'Dispenser status: FAULT').
resolution_step('C_CSH_014', 1, 'Refill/Check Cassette').
resolution_step('C_CSH_014', 2, 'Balance').

fault_profile('C_CSH_015', 'Cash Handling', 'Currency Detector', 'Currency Detector Fault', 'HIGH').
fault_description('C_CSH_015', 'Currency Detector Fault').
has_error_code('C_CSH_015', 'CSH041').
has_symptom('C_CSH_015', 'Dispenser status: FAULT').
resolution_step('C_CSH_015', 1, 'Refill/Check Cassette').
resolution_step('C_CSH_015', 2, 'Balance').

fault_profile('C_CSH_016', 'Cash Handling', 'Recycling', 'Recycler Module Fault', 'HIGH').
fault_description('C_CSH_016', 'Recycler Module Fault').
has_error_code('C_CSH_016', 'CSH050').
has_symptom('C_CSH_016', 'Dispenser status: FAULT').
resolution_step('C_CSH_016', 1, 'Refill/Check Cassette').
resolution_step('C_CSH_016', 2, 'Balance').

fault_profile('C_CSH_017', 'Cash Handling', 'Recycling', 'Recycled Note Rejected by Validator', 'MEDIUM').
fault_description('C_CSH_017', 'Recycled Note Rejected by Validator').
has_error_code('C_CSH_017', 'CSH051').
has_symptom('C_CSH_017', 'Dispenser status: FAULT').
resolution_step('C_CSH_017', 1, 'Refill/Check Cassette').
resolution_step('C_CSH_017', 2, 'Balance').

fault_profile('C_CSH_018', 'Cash Handling', 'Security', 'Cash Vault Door Open Alert', 'CRITICAL').
fault_description('C_CSH_018', 'Cash Vault Door Open Alert').
has_error_code('C_CSH_018', 'CSH060').
has_symptom('C_CSH_018', 'Dispenser status: FAULT').
resolution_step('C_CSH_018', 1, 'Refill/Check Cassette').
resolution_step('C_CSH_018', 2, 'Balance').

fault_profile('C_CSH_019', 'Cash Handling', 'Security', 'Cash Replenishment Anomaly', 'HIGH').
fault_description('C_CSH_019', 'Cash Replenishment Anomaly').
has_error_code('C_CSH_019', 'CSH061').
has_symptom('C_CSH_019', 'Dispenser status: FAULT').
resolution_step('C_CSH_019', 1, 'Refill/Check Cassette').
resolution_step('C_CSH_019', 2, 'Balance').

fault_profile('H_CR_001', 'Hardware', 'Card Reader', 'Card Reader Jam', 'HIGH').
fault_description('H_CR_001', 'Card Reader Jam').
has_error_code('H_CR_001', '3A1').
has_error_code('H_CR_001', 'ICM001').
has_symptom('H_CR_001', 'Reader status: JAMMED').
has_symptom('H_CR_001', 'Card not ejected').
resolution_step('H_CR_001', 1, 'Inspect component').
resolution_step('H_CR_001', 2, 'Test/Reset').

fault_profile('H_CR_002', 'Hardware', 'Card Reader', 'Card Reader Dirty / Sensor Fault', 'MEDIUM').
fault_description('H_CR_002', 'Card Reader Dirty / Sensor Fault').
has_error_code('H_CR_002', '3A5').
has_error_code('H_CR_002', 'ICM004').
has_symptom('H_CR_002', 'Reader status: DIRTY_SENSOR').
resolution_step('H_CR_002', 1, 'Inspect component').
resolution_step('H_CR_002', 2, 'Test/Reset').

fault_profile('H_CD_001', 'Hardware', 'Cash Dispenser', 'Cash Dispenser Jam', 'HIGH').
fault_description('H_CD_001', 'Cash Dispenser Jam').
has_error_code('H_CD_001', '4B1').
has_symptom('H_CD_001', 'Dispense attempt fails').
has_symptom('H_CD_001', 'Dispenser status: DISPENSER_JAM').
resolution_step('H_CD_001', 1, 'Inspect component').
resolution_step('H_CD_001', 2, 'Test/Reset').

fault_profile('H_CD_002', 'Hardware', 'Cash Dispenser', 'Dispenser Actuator Wear Warning', 'MEDIUM').
fault_description('H_CD_002', 'Dispenser Actuator Wear Warning').
has_error_code('H_CD_002', '4B8').
has_symptom('H_CD_002', 'Dispenser status: ACTUATOR_WORN').
resolution_step('H_CD_002', 1, 'Inspect component').
resolution_step('H_CD_002', 2, 'Test/Reset').

fault_profile('H_CD_003', 'Hardware', 'Cash Dispenser', 'Reject Bin Full', 'MEDIUM').
fault_description('H_CD_003', 'Reject Bin Full').
has_error_code('H_CD_003', '4C2').
has_symptom('H_CD_003', 'Dispenser status: REJECT_BIN_FULL').
has_symptom('H_CD_003', 'Dispense attempt fails').
resolution_step('H_CD_003', 1, 'Inspect component').
resolution_step('H_CD_003', 2, 'Test/Reset').

fault_profile('H_CD_004', 'Hardware', 'Cash Dispenser', 'Cash Presenter Fault', 'HIGH').
fault_description('H_CD_004', 'Cash Presenter Fault').
has_error_code('H_CD_004', '4D1').
has_symptom('H_CD_004', 'Dispenser status: PRESENTER_FAULT').
has_symptom('H_CD_004', 'Dispense attempt fails').
resolution_step('H_CD_004', 1, 'Inspect component').
resolution_step('H_CD_004', 2, 'Test/Reset').

fault_profile('H_PR_001', 'Hardware', 'Receipt Printer', 'Printer Paper Out', 'LOW').
fault_description('H_PR_001', 'Printer Paper Out').
has_error_code('H_PR_001', '5E1').
has_symptom('H_PR_001', 'Printer status: PAPER_OUT').
resolution_step('H_PR_001', 1, 'Inspect component').
resolution_step('H_PR_001', 2, 'Test/Reset').

fault_profile('H_PR_002', 'Hardware', 'Receipt Printer', 'Printer Paper Jam', 'MEDIUM').
fault_description('H_PR_002', 'Printer Paper Jam').
has_error_code('H_PR_002', '5E3').
has_symptom('H_PR_002', 'Printer status: PAPER_JAM').
resolution_step('H_PR_002', 1, 'Inspect component').
resolution_step('H_PR_002', 2, 'Test/Reset').

fault_profile('H_PR_003', 'Hardware', 'Receipt Printer', 'Print Head Failure', 'HIGH').
fault_description('H_PR_003', 'Print Head Failure').
has_error_code('H_PR_003', '5E7').
has_symptom('H_PR_003', 'Printer status: PRINT_HEAD_FAIL').
resolution_step('H_PR_003', 1, 'Inspect component').
resolution_step('H_PR_003', 2, 'Test/Reset').

fault_profile('H_ENV_001', 'Hardware', 'Sensors & Environment', 'Overheating — Temperature Critical', 'HIGH').
fault_description('H_ENV_001', 'Overheating — Temperature Critical').
has_error_code('H_ENV_001', '9T1').
resolution_step('H_ENV_001', 1, 'Inspect component').
resolution_step('H_ENV_001', 2, 'Test/Reset').

fault_profile('H_ENV_002', 'Hardware', 'Sensors & Environment', 'ATM Enclosure Door Open', 'CRITICAL').
fault_description('H_ENV_002', 'ATM Enclosure Door Open').
has_error_code('H_ENV_002', '9D1').
resolution_step('H_ENV_002', 1, 'Inspect component').
resolution_step('H_ENV_002', 2, 'Test/Reset').

fault_profile('H_ENV_003', 'Hardware', 'Sensors & Environment', 'General Sensor Malfunction', 'MEDIUM').
fault_description('H_ENV_003', 'General Sensor Malfunction').
has_error_code('H_ENV_003', '9S2').
resolution_step('H_ENV_003', 1, 'Inspect component').
resolution_step('H_ENV_003', 2, 'Test/Reset').

fault_profile('H_ENV_004', 'Hardware', 'Sensors & Environment', 'Power / Voltage Instability', 'HIGH').
fault_description('H_ENV_004', 'Power / Voltage Instability').
has_error_code('H_ENV_004', '9V3').
resolution_step('H_ENV_004', 1, 'Inspect component').
resolution_step('H_ENV_004', 2, 'Test/Reset').

fault_profile('H_ENV_005', 'Hardware', 'Sensors & Environment', 'Cooling Fan Failure', 'HIGH').
fault_description('H_ENV_005', 'Cooling Fan Failure').
has_error_code('H_ENV_005', '9F1').
resolution_step('H_ENV_005', 1, 'Inspect component').
resolution_step('H_ENV_005', 2, 'Test/Reset').

fault_profile('H_PER_001', 'Hardware', 'Peripherals', 'PIN Pad Unresponsive', 'HIGH').
fault_description('H_PER_001', 'PIN Pad Unresponsive').
has_error_code('H_PER_001', '6P1').
has_symptom('H_PER_001', 'PIN pad status: PINPAD_UNRESPONSIVE').
resolution_step('H_PER_001', 1, 'Inspect component').
resolution_step('H_PER_001', 2, 'Test/Reset').

fault_profile('H_PER_002', 'Hardware', 'Peripherals', 'Display Screen Failure', 'HIGH').
fault_description('H_PER_002', 'Display Screen Failure').
has_error_code('H_PER_002', '6S2').
resolution_step('H_PER_002', 1, 'Inspect component').
resolution_step('H_PER_002', 2, 'Test/Reset').

fault_profile('H_PER_003', 'Hardware', 'Peripherals', 'ATM Camera Offline', 'MEDIUM').
fault_description('H_PER_003', 'ATM Camera Offline').
has_error_code('H_PER_003', '6C1').
resolution_step('H_PER_003', 1, 'Inspect component').
resolution_step('H_PER_003', 2, 'Test/Reset').

fault_profile('H_PER_004', 'Hardware', 'Peripherals', 'UPS Battery Low — Replace Soon', 'MEDIUM').
fault_description('H_PER_004', 'UPS Battery Low — Replace Soon').
has_error_code('H_PER_004', '9U1').
resolution_step('H_PER_004', 1, 'Inspect component').
resolution_step('H_PER_004', 2, 'Test/Reset').

fault_profile('H_PER_005', 'Hardware', 'Peripherals', 'Barcode / QR Reader Fault', 'LOW').
fault_description('H_PER_005', 'Barcode / QR Reader Fault').
has_error_code('H_PER_005', '6B3').
resolution_step('H_PER_005', 1, 'Inspect component').
resolution_step('H_PER_005', 2, 'Test/Reset').

fault_profile('N_NET_000', 'Network', 'Connectivity', 'ATM Offline — No Network Response', 'CRITICAL').
fault_description('N_NET_000', 'ATM Offline — No Network Response').
has_error_code('N_NET_000', 'NET001').
has_symptom('N_NET_000', 'Network status: DOWN').
has_symptom('N_NET_000', 'Network connection lost').
resolution_step('N_NET_000', 1, 'Check LAN').
resolution_step('N_NET_000', 2, 'Network Reset').

fault_profile('N_NET_001', 'Network', 'Connectivity', 'Intermittent Network Drops', 'HIGH').
fault_description('N_NET_001', 'Intermittent Network Drops').
has_error_code('N_NET_001', 'NET002').
has_symptom('N_NET_001', 'Network status: FAULT').
resolution_step('N_NET_001', 1, 'Check LAN').
resolution_step('N_NET_001', 2, 'Network Reset').

fault_profile('N_NET_002', 'Network', 'Connectivity', 'High Network Latency', 'MEDIUM').
fault_description('N_NET_002', 'High Network Latency').
has_error_code('N_NET_002', 'NET003').
has_symptom('N_NET_002', 'Network status: FAULT').
resolution_step('N_NET_002', 1, 'Check LAN').
resolution_step('N_NET_002', 2, 'Network Reset').

fault_profile('N_NET_003', 'Network', 'Connectivity', 'DNS Resolution Failure', 'HIGH').
fault_description('N_NET_003', 'DNS Resolution Failure').
has_error_code('N_NET_003', 'NET004').
has_symptom('N_NET_003', 'Network status: FAULT').
resolution_step('N_NET_003', 1, 'Check LAN').
resolution_step('N_NET_003', 2, 'Network Reset').

fault_profile('N_NET_004', 'Network', 'TLS/Security', 'TLS Handshake Failure', 'HIGH').
fault_description('N_NET_004', 'TLS Handshake Failure').
has_error_code('N_NET_004', 'NET010').
has_symptom('N_NET_004', 'Network status: FAULT').
resolution_step('N_NET_004', 1, 'Check LAN').
resolution_step('N_NET_004', 2, 'Network Reset').

fault_profile('N_NET_005', 'Network', 'TLS/Security', 'SSL Certificate Mismatch', 'HIGH').
fault_description('N_NET_005', 'SSL Certificate Mismatch').
has_error_code('N_NET_005', 'NET011').
has_symptom('N_NET_005', 'Network status: FAULT').
resolution_step('N_NET_005', 1, 'Check LAN').
resolution_step('N_NET_005', 2, 'Network Reset').

fault_profile('N_NET_006', 'Network', 'TLS/Security', 'Man-in-the-Middle Warning', 'CRITICAL').
fault_description('N_NET_006', 'Man-in-the-Middle Warning').
has_error_code('N_NET_006', 'NET012').
has_symptom('N_NET_006', 'Network status: FAULT').
resolution_step('N_NET_006', 1, 'Check LAN').
resolution_step('N_NET_006', 2, 'Network Reset').

fault_profile('N_NET_007', 'Network', 'Host Connectivity', 'Cannot Reach Bank Core System', 'CRITICAL').
fault_description('N_NET_007', 'Cannot Reach Bank Core System').
has_error_code('N_NET_007', 'NET020').
has_symptom('N_NET_007', 'Network status: FAULT').
resolution_step('N_NET_007', 1, 'Check LAN').
resolution_step('N_NET_007', 2, 'Network Reset').

fault_profile('N_NET_008', 'Network', 'Host Connectivity', 'Connection Timeout to Core System', 'HIGH').
fault_description('N_NET_008', 'Connection Timeout to Core System').
has_error_code('N_NET_008', 'NET021').
has_symptom('N_NET_008', 'Network status: FAULT').
resolution_step('N_NET_008', 1, 'Check LAN').
resolution_step('N_NET_008', 2, 'Network Reset').

fault_profile('N_NET_009', 'Network', 'Host Connectivity', 'Authentication Rejected by Core', 'HIGH').
fault_description('N_NET_009', 'Authentication Rejected by Core').
has_error_code('N_NET_009', 'NET022').
has_symptom('N_NET_009', 'Network status: FAULT').
resolution_step('N_NET_009', 1, 'Check LAN').
resolution_step('N_NET_009', 2, 'Network Reset').

fault_profile('N_NET_010', 'Network', 'VPN', 'VPN Tunnel Down', 'CRITICAL').
fault_description('N_NET_010', 'VPN Tunnel Down').
has_error_code('N_NET_010', 'NET030').
has_symptom('N_NET_010', 'Network status: FAULT').
resolution_step('N_NET_010', 1, 'Check LAN').
resolution_step('N_NET_010', 2, 'Network Reset').

fault_profile('N_NET_011', 'Network', 'VPN', 'VPN Authentication Failed', 'HIGH').
fault_description('N_NET_011', 'VPN Authentication Failed').
has_error_code('N_NET_011', 'NET031').
has_symptom('N_NET_011', 'Network status: FAULT').
resolution_step('N_NET_011', 1, 'Check LAN').
resolution_step('N_NET_011', 2, 'Network Reset').

fault_profile('N_NET_012', 'Network', 'Firewall', 'ATM Traffic Blocked by Firewall', 'HIGH').
fault_description('N_NET_012', 'ATM Traffic Blocked by Firewall').
has_error_code('N_NET_012', 'NET040').
has_symptom('N_NET_012', 'Network status: FAULT').
resolution_step('N_NET_012', 1, 'Check LAN').
resolution_step('N_NET_012', 2, 'Network Reset').

fault_profile('N_NET_013', 'Network', 'Firewall', 'IP Address Conflict', 'MEDIUM').
fault_description('N_NET_013', 'IP Address Conflict').
has_error_code('N_NET_013', 'NET041').
has_symptom('N_NET_013', 'Network status: FAULT').
resolution_step('N_NET_013', 1, 'Check LAN').
resolution_step('N_NET_013', 2, 'Network Reset').

fault_profile('N_NET_014', 'Network', 'Switch/Router', 'Network Switch Port Down', 'HIGH').
fault_description('N_NET_014', 'Network Switch Port Down').
has_error_code('N_NET_014', 'NET050').
has_symptom('N_NET_014', 'Network status: FAULT').
resolution_step('N_NET_014', 1, 'Check LAN').
resolution_step('N_NET_014', 2, 'Network Reset').

fault_profile('N_NET_015', 'Network', 'Switch/Router', 'Router Unreachable', 'CRITICAL').
fault_description('N_NET_015', 'Router Unreachable').
has_error_code('N_NET_015', 'NET051').
has_symptom('N_NET_015', 'Network status: FAULT').
resolution_step('N_NET_015', 1, 'Check LAN').
resolution_step('N_NET_015', 2, 'Network Reset').

fault_profile('N_NET_016', 'Network', 'Bandwidth', 'Bandwidth Saturation', 'MEDIUM').
fault_description('N_NET_016', 'Bandwidth Saturation').
has_error_code('N_NET_016', 'NET060').
has_symptom('N_NET_016', 'Network status: FAULT').
resolution_step('N_NET_016', 1, 'Check LAN').
resolution_step('N_NET_016', 2, 'Network Reset').

fault_profile('N_NET_017', 'Network', 'Bandwidth', 'Packet Loss Exceeding Threshold', 'HIGH').
fault_description('N_NET_017', 'Packet Loss Exceeding Threshold').
has_error_code('N_NET_017', 'NET061').
has_symptom('N_NET_017', 'Network status: FAULT').
resolution_step('N_NET_017', 1, 'Check LAN').
resolution_step('N_NET_017', 2, 'Network Reset').

fault_profile('N_NET_018', 'Network', 'NTP', 'Clock Sync Failure (NTP)', 'MEDIUM').
fault_description('N_NET_018', 'Clock Sync Failure (NTP)').
has_error_code('N_NET_018', 'NET070').
has_symptom('N_NET_018', 'Network status: FAULT').
resolution_step('N_NET_018', 1, 'Check LAN').
resolution_step('N_NET_018', 2, 'Network Reset').

fault_profile('N_NET_019', 'Network', 'NTP', 'ATM Clock Drift Detected', 'MEDIUM').
fault_description('N_NET_019', 'ATM Clock Drift Detected').
has_error_code('N_NET_019', 'NET071').
has_symptom('N_NET_019', 'Network status: FAULT').
resolution_step('N_NET_019', 1, 'Check LAN').
resolution_step('N_NET_019', 2, 'Network Reset').

fault_profile('SEC_000', 'Security', 'Card Skimming', 'Card Skimmer Device Detected', 'CRITICAL').
fault_description('SEC_000', 'Card Skimmer Device Detected').
has_error_code('SEC_000', 'SEC001').
resolution_step('SEC_000', 1, 'Security Alert').
resolution_step('SEC_000', 2, 'Forensics').

fault_profile('SEC_001', 'Security', 'Card Skimming', 'Card Reader Depth Anomaly (Possible Skimmer)', 'CRITICAL').
fault_description('SEC_001', 'Card Reader Depth Anomaly (Possible Skimmer)').
has_error_code('SEC_001', 'SEC002').
resolution_step('SEC_001', 1, 'Security Alert').
resolution_step('SEC_001', 2, 'Forensics').

fault_profile('SEC_002', 'Security', 'Card Skimming', 'Unusual Card Read Failures — Possible Shimmer', 'HIGH').
fault_description('SEC_002', 'Unusual Card Read Failures — Possible Shimmer').
has_error_code('SEC_002', 'SEC003').
resolution_step('SEC_002', 1, 'Security Alert').
resolution_step('SEC_002', 2, 'Forensics').

fault_profile('SEC_003', 'Security', 'PIN Pad Tampering', 'PIN Pad Cover Removal Detected', 'CRITICAL').
fault_description('SEC_003', 'PIN Pad Cover Removal Detected').
has_error_code('SEC_003', 'SEC010').
resolution_step('SEC_003', 1, 'Security Alert').
resolution_step('SEC_003', 2, 'Forensics').

fault_profile('SEC_004', 'Security', 'PIN Pad Tampering', 'PIN Pad Enclosure Breach Sensor Triggered', 'CRITICAL').
fault_description('SEC_004', 'PIN Pad Enclosure Breach Sensor Triggered').
has_error_code('SEC_004', 'SEC011').
resolution_step('SEC_004', 1, 'Security Alert').
resolution_step('SEC_004', 2, 'Forensics').

fault_profile('SEC_005', 'Security', 'PIN Pad Tampering', 'Suspicious PIN Pad Overlay Pattern', 'HIGH').
fault_description('SEC_005', 'Suspicious PIN Pad Overlay Pattern').
has_error_code('SEC_005', 'SEC012').
resolution_step('SEC_005', 1, 'Security Alert').
resolution_step('SEC_005', 2, 'Forensics').

fault_profile('SEC_006', 'Security', 'Transaction Fraud', 'Unusual Transaction Volume — Velocity Alert', 'HIGH').
fault_description('SEC_006', 'Unusual Transaction Volume — Velocity Alert').
has_error_code('SEC_006', 'SEC020').
resolution_step('SEC_006', 1, 'Security Alert').
resolution_step('SEC_006', 2, 'Forensics').

fault_profile('SEC_007', 'Security', 'Transaction Fraud', 'Repeated Declined Transactions — Brute Force', 'HIGH').
fault_description('SEC_007', 'Repeated Declined Transactions — Brute Force').
has_error_code('SEC_007', 'SEC021').
resolution_step('SEC_007', 1, 'Security Alert').
resolution_step('SEC_007', 2, 'Forensics').

fault_profile('SEC_008', 'Security', 'Transaction Fraud', 'High-Value Withdrawal Cluster', 'HIGH').
fault_description('SEC_008', 'High-Value Withdrawal Cluster').
has_error_code('SEC_008', 'SEC022').
resolution_step('SEC_008', 1, 'Security Alert').
resolution_step('SEC_008', 2, 'Forensics').

fault_profile('SEC_009', 'Security', 'Transaction Fraud', 'Card Present + Geolocation Mismatch', 'HIGH').
fault_description('SEC_009', 'Card Present + Geolocation Mismatch').
has_error_code('SEC_009', 'SEC023').
resolution_step('SEC_009', 1, 'Security Alert').
resolution_step('SEC_009', 2, 'Forensics').

fault_profile('SEC_010', 'Security', 'Physical Attack', 'ATM Anti-Ram Sensor Triggered', 'CRITICAL').
fault_description('SEC_010', 'ATM Anti-Ram Sensor Triggered').
has_error_code('SEC_010', 'SEC030').
resolution_step('SEC_010', 1, 'Security Alert').
resolution_step('SEC_010', 2, 'Forensics').

fault_profile('SEC_011', 'Security', 'Physical Attack', 'Explosive Gas Detection Alert', 'CRITICAL').
fault_description('SEC_011', 'Explosive Gas Detection Alert').
has_error_code('SEC_011', 'SEC031').
resolution_step('SEC_011', 1, 'Security Alert').
resolution_step('SEC_011', 2, 'Forensics').

fault_profile('SEC_012', 'Security', 'Physical Attack', 'ATM Enclosure Vibration Alert', 'HIGH').
fault_description('SEC_012', 'ATM Enclosure Vibration Alert').
has_error_code('SEC_012', 'SEC032').
resolution_step('SEC_012', 1, 'Security Alert').
resolution_step('SEC_012', 2, 'Forensics').

fault_profile('SEC_013', 'Security', 'Physical Attack', 'Safe Door Tamper Sensor Triggered', 'CRITICAL').
fault_description('SEC_013', 'Safe Door Tamper Sensor Triggered').
has_error_code('SEC_013', 'SEC033').
resolution_step('SEC_013', 1, 'Security Alert').
resolution_step('SEC_013', 2, 'Forensics').

fault_profile('SEC_014', 'Security', 'CCTV / Surveillance', 'ATM Camera Offline — Security Risk', 'HIGH').
fault_description('SEC_014', 'ATM Camera Offline — Security Risk').
has_error_code('SEC_014', 'SEC040').
resolution_step('SEC_014', 1, 'Security Alert').
resolution_step('SEC_014', 2, 'Forensics').

fault_profile('SEC_015', 'Security', 'CCTV / Surveillance', 'Camera View Obstruction Detected', 'HIGH').
fault_description('SEC_015', 'Camera View Obstruction Detected').
has_error_code('SEC_015', 'SEC041').
resolution_step('SEC_015', 1, 'Security Alert').
resolution_step('SEC_015', 2, 'Forensics').

fault_profile('SEC_016', 'Security', 'Logical Security', 'Failed Admin Login Attempts Threshold', 'HIGH').
fault_description('SEC_016', 'Failed Admin Login Attempts Threshold').
has_error_code('SEC_016', 'SEC050').
resolution_step('SEC_016', 1, 'Security Alert').
resolution_step('SEC_016', 2, 'Forensics').

fault_profile('SEC_017', 'Security', 'Logical Security', 'Unauthorised Remote Access Attempt', 'CRITICAL').
fault_description('SEC_017', 'Unauthorised Remote Access Attempt').
has_error_code('SEC_017', 'SEC051').
resolution_step('SEC_017', 1, 'Security Alert').
resolution_step('SEC_017', 2, 'Forensics').

fault_profile('SEC_018', 'Security', 'Logical Security', 'Malware Signature Detected on ATM OS', 'CRITICAL').
fault_description('SEC_018', 'Malware Signature Detected on ATM OS').
has_error_code('SEC_018', 'SEC052').
resolution_step('SEC_018', 1, 'Security Alert').
resolution_step('SEC_018', 2, 'Forensics').

fault_profile('SEC_019', 'Security', 'Compliance', 'PCI-DSS Compliance Check Failed', 'HIGH').
fault_description('SEC_019', 'PCI-DSS Compliance Check Failed').
has_error_code('SEC_019', 'SEC060').
resolution_step('SEC_019', 1, 'Security Alert').
resolution_step('SEC_019', 2, 'Forensics').

fault_profile('S_SW_000', 'Software', 'OS', 'OS Kernel Panic / Blue Screen', 'CRITICAL').
fault_description('S_SW_000', 'OS Kernel Panic / Blue Screen').
has_error_code('S_SW_000', 'SW001').
has_symptom('S_SW_000', 'Software status: FAULT').
resolution_step('S_SW_000', 1, 'Restart').
resolution_step('S_SW_000', 2, 'Remote Maintenance').

fault_profile('S_SW_001', 'Software', 'OS', 'OS Disk Space Critical', 'HIGH').
fault_description('S_SW_001', 'OS Disk Space Critical').
has_error_code('S_SW_001', 'SW002').
has_symptom('S_SW_001', 'Software status: FAULT').
resolution_step('S_SW_001', 1, 'Restart').
resolution_step('S_SW_001', 2, 'Remote Maintenance').

fault_profile('S_SW_002', 'Software', 'Application', 'ATM Application Crash', 'HIGH').
fault_description('S_SW_002', 'ATM Application Crash').
has_error_code('S_SW_002', 'SW010').
has_symptom('S_SW_002', 'Software status: FAULT').
resolution_step('S_SW_002', 1, 'Restart').
resolution_step('S_SW_002', 2, 'Remote Maintenance').

fault_profile('S_SW_003', 'Software', 'Application', 'Application Version Mismatch', 'MEDIUM').
fault_description('S_SW_003', 'Application Version Mismatch').
has_error_code('S_SW_003', 'SW011').
has_symptom('S_SW_003', 'Software status: FAULT').
resolution_step('S_SW_003', 1, 'Restart').
resolution_step('S_SW_003', 2, 'Remote Maintenance').

fault_profile('S_SW_004', 'Software', 'Application', 'Application Deadlock Detected', 'HIGH').
fault_description('S_SW_004', 'Application Deadlock Detected').
has_error_code('S_SW_004', 'SW012').
has_symptom('S_SW_004', 'Software status: FAULT').
resolution_step('S_SW_004', 1, 'Restart').
resolution_step('S_SW_004', 2, 'Remote Maintenance').

fault_profile('S_SW_005', 'Software', 'Application', 'Configuration File Corrupt', 'HIGH').
fault_description('S_SW_005', 'Configuration File Corrupt').
has_error_code('S_SW_005', 'SW013').
has_symptom('S_SW_005', 'Software status: FAULT').
resolution_step('S_SW_005', 1, 'Restart').
resolution_step('S_SW_005', 2, 'Remote Maintenance').

fault_profile('S_SW_006', 'Software', 'Firmware', 'Firmware Update Failed', 'HIGH').
fault_description('S_SW_006', 'Firmware Update Failed').
has_error_code('S_SW_006', 'SW020').
has_symptom('S_SW_006', 'Software status: FAULT').
resolution_step('S_SW_006', 1, 'Restart').
resolution_step('S_SW_006', 2, 'Remote Maintenance').

fault_profile('S_SW_007', 'Software', 'Firmware', 'Firmware Version Mismatch', 'MEDIUM').
fault_description('S_SW_007', 'Firmware Version Mismatch').
has_error_code('S_SW_007', 'SW021').
has_symptom('S_SW_007', 'Software status: FAULT').
resolution_step('S_SW_007', 1, 'Restart').
resolution_step('S_SW_007', 2, 'Remote Maintenance').

fault_profile('S_SW_008', 'Software', 'Database', 'Transaction Database Unreachable', 'CRITICAL').
fault_description('S_SW_008', 'Transaction Database Unreachable').
has_error_code('S_SW_008', 'SW030').
has_symptom('S_SW_008', 'Software status: FAULT').
resolution_step('S_SW_008', 1, 'Restart').
resolution_step('S_SW_008', 2, 'Remote Maintenance').

fault_profile('S_SW_009', 'Software', 'Database', 'Transaction Log Full', 'HIGH').
fault_description('S_SW_009', 'Transaction Log Full').
has_error_code('S_SW_009', 'SW031').
has_symptom('S_SW_009', 'Software status: FAULT').
resolution_step('S_SW_009', 1, 'Restart').
resolution_step('S_SW_009', 2, 'Remote Maintenance').

fault_profile('S_SW_010', 'Software', 'Security Software', 'Anti-Tamper Software Alert', 'CRITICAL').
fault_description('S_SW_010', 'Anti-Tamper Software Alert').
has_error_code('S_SW_010', 'SW040').
has_symptom('S_SW_010', 'Software status: FAULT').
resolution_step('S_SW_010', 1, 'Restart').
resolution_step('S_SW_010', 2, 'Remote Maintenance').

fault_profile('S_SW_011', 'Software', 'Security Software', 'Certificate / TLS Expiry', 'HIGH').
fault_description('S_SW_011', 'Certificate / TLS Expiry').
has_error_code('S_SW_011', 'SW041').
has_symptom('S_SW_011', 'Software status: FAULT').
resolution_step('S_SW_011', 1, 'Restart').
resolution_step('S_SW_011', 2, 'Remote Maintenance').

fault_profile('S_SW_012', 'Software', 'Security Software', 'Encryption Key Rotation Overdue', 'HIGH').
fault_description('S_SW_012', 'Encryption Key Rotation Overdue').
has_error_code('S_SW_012', 'SW042').
has_symptom('S_SW_012', 'Software status: FAULT').
resolution_step('S_SW_012', 1, 'Restart').
resolution_step('S_SW_012', 2, 'Remote Maintenance').

fault_profile('S_SW_013', 'Software', 'Diagnostics', 'Self-Test Failure at Startup', 'HIGH').
fault_description('S_SW_013', 'Self-Test Failure at Startup').
has_error_code('S_SW_013', 'SW050').
has_symptom('S_SW_013', 'Software status: FAULT').
resolution_step('S_SW_013', 1, 'Restart').
resolution_step('S_SW_013', 2, 'Remote Maintenance').

fault_profile('S_SW_014', 'Software', 'Diagnostics', 'Scheduled Maintenance Mode Stuck', 'MEDIUM').
fault_description('S_SW_014', 'Scheduled Maintenance Mode Stuck').
has_error_code('S_SW_014', 'SW051').
has_symptom('S_SW_014', 'Software status: FAULT').
resolution_step('S_SW_014', 1, 'Restart').
resolution_step('S_SW_014', 2, 'Remote Maintenance').

fault_profile('S_SW_015', 'Software', 'Remote Management', 'Remote Management Agent Offline', 'MEDIUM').
fault_description('S_SW_015', 'Remote Management Agent Offline').
has_error_code('S_SW_015', 'SW060').
has_symptom('S_SW_015', 'Software status: FAULT').
resolution_step('S_SW_015', 1, 'Restart').
resolution_step('S_SW_015', 2, 'Remote Maintenance').

fault_profile('S_SW_016', 'Software', 'Remote Management', 'Software Patch Failed to Apply', 'MEDIUM').
fault_description('S_SW_016', 'Software Patch Failed to Apply').
has_error_code('S_SW_016', 'SW061').
has_symptom('S_SW_016', 'Software status: FAULT').
resolution_step('S_SW_016', 1, 'Restart').
resolution_step('S_SW_016', 2, 'Remote Maintenance').

fault_profile('S_SW_017', 'Software', 'Watchdog', 'Watchdog Timer Restart Loop', 'HIGH').
fault_description('S_SW_017', 'Watchdog Timer Restart Loop').
has_error_code('S_SW_017', 'SW070').
has_symptom('S_SW_017', 'Software status: FAULT').
resolution_step('S_SW_017', 1, 'Restart').
resolution_step('S_SW_017', 2, 'Remote Maintenance').

fault_profile('S_SW_018', 'Software', 'Watchdog', 'Memory Leak Detected', 'HIGH').
fault_description('S_SW_018', 'Memory Leak Detected').
has_error_code('S_SW_018', 'SW071').
has_symptom('S_SW_018', 'Software status: FAULT').
resolution_step('S_SW_018', 1, 'Restart').
resolution_step('S_SW_018', 2, 'Remote Maintenance').

fault_profile('S_SW_019', 'Software', 'Startup', 'ATM Failed to Boot', 'CRITICAL').
fault_description('S_SW_019', 'ATM Failed to Boot').
has_error_code('S_SW_019', 'SW080').
has_symptom('S_SW_019', 'Software status: FAULT').
resolution_step('S_SW_019', 1, 'Restart').
resolution_step('S_SW_019', 2, 'Remote Maintenance').
