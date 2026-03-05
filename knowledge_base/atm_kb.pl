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

fault_profile('CSH_001', 'Cash Handling', 'Cassette', 'Cash Cassette Empty', 'HIGH').
fault_description('CSH_001', 'One or more cash cassettes have run out of banknotes.').
has_error_code('CSH_001', 'CSH001').
has_symptom('CSH_001', '''Out of Cash'' screen').
has_symptom('CSH_001', 'Cassette status: EMPTY').
has_cause('CSH_001', 'High transaction volume').
has_cause('CSH_001', 'Delayed replenishment').
resolution_step('CSH_001', 1, 'Alert branch staff').
resolution_step('CSH_001', 2, 'Replenish cash following dual-control procedures').
resolution_step('CSH_001', 3, 'Verify cassette is correctly seated').
resolution_step('CSH_001', 4, 'Return to service').

fault_profile('CSH_002', 'Cash Handling', 'Detection', 'Counterfeit Note Detected', 'CRITICAL').
fault_description('CSH_002', 'The ATM''s currency detector has identified a suspect banknote during deposit.').
has_error_code('CSH_002', 'CSH040').
has_symptom('CSH_002', 'Note retained by ATM').
has_symptom('CSH_002', 'Fraud alert triggered').
has_cause('CSH_002', 'Attempted fraud').
resolution_step('CSH_002', 1, 'Retain suspect note in secure bin').
resolution_step('CSH_002', 2, 'Alert security and branch manager').
resolution_step('CSH_002', 3, 'Provide incident receipt to customer').
resolution_step('CSH_002', 4, 'Submit note for verification').

fault_profile('CSH_003', 'Cash Handling', 'Counting', 'Dispense Count Mismatch', 'CRITICAL').
fault_description('CSH_003', 'The number of notes dispensed does not match the system request.').
has_error_code('CSH_003', 'CSH020').
has_symptom('CSH_003', 'Customer reported short-change').
has_symptom('CSH_003', 'Journal mismatch').
has_cause('CSH_003', 'Note jam after counting').
has_cause('CSH_003', 'Sensor error').
has_cause('CSH_003', 'Mechanical wear').
resolution_step('CSH_003', 1, 'Take ATM out of service').
resolution_step('CSH_003', 2, 'Perform physical cash count').
resolution_step('CSH_003', 3, 'Review dispense logs').
resolution_step('CSH_003', 4, 'Initiate dispute resolution').

fault_profile('HW_001', 'Hardware', 'Card Reader', 'Card Reader Jam', 'HIGH').
fault_description('HW_001', 'Physical obstruction in the card reader preventing card movement.').
has_error_code('HW_001', '3A1').
has_error_code('HW_001', 'ICM001').
has_symptom('HW_001', 'Card not ejected').
has_symptom('HW_001', 'Reader status: JAMMED').
has_cause('HW_001', 'Damaged card').
has_cause('HW_001', 'Sticky rollers').
has_cause('HW_001', 'Foreign object').
resolution_step('HW_001', 1, 'Take ATM out of service').
resolution_step('HW_001', 2, 'Open card reader access panel').
resolution_step('HW_001', 3, 'Carefully remove jammed card').
resolution_step('HW_001', 4, 'Run card reader self-test').
resolution_step('HW_001', 5, 'Return to service').

fault_profile('HW_002', 'Hardware', 'Card Reader', 'Card Reader Dirty / Sensor Fault', 'MEDIUM').
fault_description('HW_002', 'Optical sensors in the reader are obscured by dust or dirt.').
has_error_code('HW_002', '3A5').
has_error_code('HW_002', 'ICM004').
has_symptom('HW_002', 'Intermittent read failures').
has_symptom('HW_002', 'Reader status: DIRTY_SENSOR').
has_cause('HW_002', 'Accumulated dust').
has_cause('HW_002', 'Worn cleaning pads').
resolution_step('HW_002', 1, 'Display maintenance alert').
resolution_step('HW_002', 2, 'Run card reader cleaning cycle using cleaning card').
resolution_step('HW_002', 3, 'If cleaning fails, schedule engineer visit for sensor replacement').

fault_profile('HW_003', 'Hardware', 'Cash Dispenser', 'Cash Dispenser Jam', 'HIGH').
fault_description('HW_003', 'Banknotes are stuck in the transport path of the dispenser.').
has_error_code('HW_003', '4B1').
has_error_code('HW_003', 'DISP_ERR_10').
has_symptom('HW_003', 'Dispense attempt fails').
has_symptom('HW_003', 'Dispenser status: DISPENSER_JAM').
has_cause('HW_003', 'Poor note quality').
has_cause('HW_003', 'Mechanical misalignment').
has_cause('HW_003', 'Overfilled cassette').
resolution_step('HW_003', 1, 'Take ATM out of service').
resolution_step('HW_003', 2, 'Open dispenser access panel').
resolution_step('HW_003', 3, 'Remove jammed notes').
resolution_step('HW_003', 4, 'Check transport path').
resolution_step('HW_003', 5, 'Run dispenser self-test').
resolution_step('HW_003', 6, 'Return to service').

fault_profile('HW_004', 'Hardware', 'Receipt Printer', 'Printer Paper Jam', 'MEDIUM').
fault_description('HW_004', 'Receipt paper has crumpled or stuck in the printer rollers.').
has_error_code('HW_004', '5E3').
has_symptom('HW_004', 'Receipt not printed').
has_symptom('HW_004', 'Printer status: PAPER_JAM').
has_cause('HW_004', 'Incorrect paper loading').
has_cause('HW_004', 'Damaged paper roll').
has_cause('HW_004', 'High humidity').
resolution_step('HW_004', 1, 'Open printer access cover').
resolution_step('HW_004', 2, 'Remove jammed paper').
resolution_step('HW_004', 3, 'Check for torn fragments').
resolution_step('HW_004', 4, 'Reload paper and run test print').

fault_profile('HW_005', 'Hardware', 'Sensors', 'ATM Enclosure Door Open', 'CRITICAL').
fault_description('HW_005', 'The main security door of the ATM is open or the sensor is triggered.').
has_error_code('HW_005', '9D1').
has_symptom('HW_005', 'Security alarm triggered').
has_symptom('HW_005', 'ATM status: DOOR_OPEN').
has_cause('HW_005', 'Unauthorised access').
has_cause('HW_005', 'Maintenance in progress').
has_cause('HW_005', 'Sensor failure').
resolution_step('HW_005', 1, 'Immediately alert branch security').
resolution_step('HW_005', 2, 'Verify physical security').
resolution_step('HW_005', 3, 'Review CCTV footage').
resolution_step('HW_005', 4, 'Log security incident').

fault_profile('NET_001', 'Network', 'Connectivity', 'ATM Offline', 'CRITICAL').
fault_description('NET_001', 'The ATM has no network connectivity and cannot reach the bank server.').
has_error_code('NET_001', 'NET001').
has_symptom('NET_001', 'System status: OFFLINE').
has_symptom('NET_001', 'Ping timeouts').
has_cause('NET_001', 'Faulty LAN cable').
has_cause('NET_001', 'Switch port failure').
has_cause('NET_001', 'Router misconfiguration').
resolution_step('NET_001', 1, 'Ping ATM from operations centre').
resolution_step('NET_001', 2, 'Check physical LAN cable').
resolution_step('NET_001', 3, 'Verify router settings').
resolution_step('NET_001', 4, 'Dispatch engineer if cable/port is damaged').

fault_profile('NET_002', 'Network', 'Security', 'TLS Handshake Failure', 'HIGH').
fault_description('NET_002', 'Secure communication cannot be established due to certificate or cipher issues.').
has_error_code('NET_002', 'NET010').
has_error_code('NET_002', 'TLS_ERR_403').
has_symptom('NET_002', 'Connection rejected by core').
has_symptom('NET_002', 'Cert expiry warnings').
has_cause('NET_002', 'Expired SSL certificate').
has_cause('NET_002', 'Incompatible cipher suite').
resolution_step('NET_002', 1, 'Check certificate validity').
resolution_step('NET_002', 2, 'Renew TLS certificate').
resolution_step('NET_002', 3, 'Restart network services').

fault_profile('NET_003', 'Network', 'VPN', 'VPN Tunnel Down', 'CRITICAL').
fault_description('NET_003', 'The secure VPN tunnel used for ATM-to-bank communication has collapsed.').
has_error_code('NET_003', 'NET030').
has_symptom('NET_003', 'Remote management unreachable').
has_symptom('NET_003', 'VPN status: DOWN').
has_cause('NET_003', 'VPN credential expiry').
has_cause('NET_003', 'ISP outage').
has_cause('NET_003', 'Server-side tunnel termination').
resolution_step('NET_003', 1, 'Restart VPN client on ATM').
resolution_step('NET_003', 2, 'Verify VPN server status').
resolution_step('NET_003', 3, 'Re-authenticate VPN session').

fault_profile('SEC_001', 'Security', 'Card Skimming', 'Card Skimmer Device Detected', 'CRITICAL').
fault_description('SEC_001', 'Anti-skimming sensors have detected an overlay or insert device on the card reader.').
has_error_code('SEC_001', 'SEC001').
has_symptom('SEC_001', 'Skimmer alert triggered').
has_symptom('SEC_001', 'Anomalous card insert depth').
has_cause('SEC_001', 'Physical tampering').
resolution_step('SEC_001', 1, 'Take ATM out of service immediately').
resolution_step('SEC_001', 2, 'Alert fraud team and police').
resolution_step('SEC_001', 3, 'Do not touch device (preserve forensics)').
resolution_step('SEC_001', 4, 'Review CCTV footage').

fault_profile('SEC_002', 'Security', 'Tampering', 'PIN Pad Cover Removal', 'CRITICAL').
fault_description('SEC_002', 'The security shield over the PIN pad has been removed or tampered with.').
has_error_code('SEC_002', 'SEC010').
has_symptom('SEC_002', 'Tamper sensor active').
has_symptom('SEC_002', 'Visible damage to PIN pad').
has_cause('SEC_002', 'Vandalism').
has_cause('SEC_002', 'Skimming preparation').
resolution_step('SEC_002', 1, 'Take ATM out of service').
resolution_step('SEC_002', 2, 'Alert branch security').
resolution_step('SEC_002', 3, 'Inspect for hidden cameras').
resolution_step('SEC_002', 4, 'Replace PIN pad shield').

fault_profile('SW_001', 'Software', 'OS', 'OS Kernel Panic / Blue Screen', 'CRITICAL').
fault_description('SW_001', 'Operating system has crashed and is unresponsive.').
has_error_code('SW_001', 'SW001').
has_error_code('SW_001', 'SYS_500').
has_symptom('SW_001', 'ATM screen frozen/blank').
has_symptom('SW_001', 'System ping timeout').
has_cause('SW_001', 'Driver conflict').
has_cause('SW_001', 'Hardware failure').
has_cause('SW_001', 'Memory corruption').
resolution_step('SW_001', 1, 'Attempt remote restart via management console').
resolution_step('SW_001', 2, 'If restart fails, dispatch engineer for on-site recovery').
resolution_step('SW_001', 3, 'Review crash dump logs').

fault_profile('SW_002', 'Software', 'Application', 'ATM Application Crash', 'HIGH').
fault_description('SW_002', 'The primary ATM user interface software has terminated unexpectedly.').
has_error_code('SW_002', 'SW010').
has_error_code('SW_002', 'SYS_123').
has_symptom('SW_002', 'Welcome screen not visible').
has_symptom('SW_002', 'App logs show segfault').
has_cause('SW_002', 'Software bug').
has_cause('SW_002', 'Missing configuration file').
has_cause('SW_002', 'Resource exhaustion').
resolution_step('SW_002', 1, 'Restart ATM application via remote console').
resolution_step('SW_002', 2, 'Review application error logs').
resolution_step('SW_002', 3, 'Check for pending updates').

fault_profile('SW_003', 'Software', 'Database', 'Transaction Database Unreachable', 'CRITICAL').
fault_description('SW_003', 'ATM cannot connect to the local or central transaction database.').
has_error_code('SW_003', 'SW030').
has_symptom('SW_003', 'Transactions declined').
has_symptom('SW_003', 'Connection timeout logs').
has_cause('SW_003', 'Network failure').
has_cause('SW_003', 'Database service down').
has_cause('SW_003', 'Credential expiry').
resolution_step('SW_003', 1, 'Check database server connectivity').
resolution_step('SW_003', 2, 'Verify network path to bank core').
resolution_step('SW_003', 3, 'Escalate to IT if server is down').
