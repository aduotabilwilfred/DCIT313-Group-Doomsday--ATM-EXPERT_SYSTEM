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

fault_profile('SEC_003', 'Security', 'Unauthorized Access', 'Unauthorized Admin Access Attempt', 'CRITICAL').
fault_description('SEC_003', 'Multiple failed attempts to access administrative functions without valid credentials.').
has_error_code('SEC_003', 'SEC020').
has_error_code('SEC_003', 'AUTH_FAIL_001').
has_symptom('SEC_003', 'Invalid admin credentials detected').
has_symptom('SEC_003', 'Repeated access denied logs').
has_symptom('SEC_003', 'Authentication threshold exceeded').
has_cause('SEC_003', 'Brute force attack').
has_cause('SEC_003', 'Credential compromise').
has_cause('SEC_003', 'Malicious insider attempt').
resolution_step('SEC_003', 1, 'Lock ATM admin functions immediately').
resolution_step('SEC_003', 2, 'Alert security operations center').
resolution_step('SEC_003', 3, 'Review access logs for last 24 hours').
resolution_step('SEC_003', 4, 'Verify admin credential integrity').
resolution_step('SEC_003', 5, 'Change all admin passwords').
resolution_step('SEC_003', 6, 'Investigate source IP if remotely attempted').

fault_profile('SEC_004', 'Security', 'Encryption', 'Encryption/Communication Failure', 'CRITICAL').
fault_description('SEC_004', 'SSL/TLS encryption has failed or been compromised during network communication.').
has_error_code('SEC_004', 'SEC030').
has_error_code('SEC_004', 'SSL_ERR_001').
has_error_code('SEC_004', 'TLS_FAIL_002').
has_symptom('SEC_004', 'Encryption handshake failure').
has_symptom('SEC_004', 'Certificate validation error').
has_symptom('SEC_004', 'Secure communication channel lost').
has_cause('SEC_004', 'Expired SSL certificate').
has_cause('SEC_004', 'Man-in-the-middle attack').
has_cause('SEC_004', 'Network interface compromise').
has_cause('SEC_004', 'Firewall interference').
resolution_step('SEC_004', 1, 'Disconnect ATM from network immediately').
resolution_step('SEC_004', 2, 'Do not process any transactions').
resolution_step('SEC_004', 3, 'Alert network security team').
resolution_step('SEC_004', 4, 'Verify SSL certificate validity').
resolution_step('SEC_004', 5, 'Check for unauthorized network devices').
resolution_step('SEC_004', 6, 'Review network traffic logs').

fault_profile('SEC_005', 'Security', 'Fraud Detection', 'Suspicious Transaction Pattern Detected', 'HIGH').
fault_description('SEC_005', 'Unusual transaction patterns detected that may indicate fraud or money laundering.').
has_error_code('SEC_005', 'SEC040').
has_error_code('SEC_005', 'FRAUD_ALERT_001').
has_symptom('SEC_005', 'Multiple rapid withdrawals').
has_symptom('SEC_005', 'Unusual withdrawal amounts').
has_symptom('SEC_005', 'Transactions from unfamiliar cards').
has_symptom('SEC_005', 'Late-night high-value withdrawals').
has_cause('SEC_005', 'Compromised card credentials').
has_cause('SEC_005', 'Money laundering attempt').
has_cause('SEC_005', 'Organized fraud ring').
has_cause('SEC_005', 'Testing stolen card details').
resolution_step('SEC_005', 1, 'Flag all cards used in suspicious transactions').
resolution_step('SEC_005', 2, 'Alert fraud investigation team').
resolution_step('SEC_005', 3, 'Review transaction history for patterns').
resolution_step('SEC_005', 4, 'Contact cardholders for verification').
resolution_step('SEC_005', 5, 'Block cards in real-time if confirmed').
resolution_step('SEC_005', 6, 'Report to financial intelligence unit').

fault_profile('SEC_006', 'Security', 'Network', 'Network Interface Tampering Detected', 'HIGH').
fault_description('SEC_006', 'Physical or logical tampering with network interfaces detected.').
has_error_code('SEC_006', 'SEC050').
has_error_code('SEC_006', 'NET_TAMPER_001').
has_symptom('SEC_006', 'Network cable detached').
has_symptom('SEC_006', 'Unauthorized device connected').
has_symptom('SEC_006', 'Network interface disabled').
has_symptom('SEC_006', 'Routing configuration altered').
has_cause('SEC_006', 'Physical cable removal').
has_cause('SEC_006', 'Unauthorized network tap installed').
has_cause('SEC_006', 'Configuration tampering').
has_cause('SEC_006', 'Malicious network access').
resolution_step('SEC_006', 1, 'Verify physical network cable connections').
resolution_step('SEC_006', 2, 'Check for unauthorized devices on network').
resolution_step('SEC_006', 3, 'Review network configuration').
resolution_step('SEC_006', 4, 'Inspect network ports for tampering').
resolution_step('SEC_006', 5, 'Contact IT security to audit network').
resolution_step('SEC_006', 6, 'Restore network configuration from backup').

fault_profile('SEC_007', 'Security', 'Physical Security', 'Cash Box Breach Attempt', 'CRITICAL').
fault_description('SEC_007', 'Physical security sensors indicate attempted breach of cash cassette compartment.').
has_error_code('SEC_007', 'SEC060').
has_error_code('SEC_007', 'CASH_BREACH_001').
has_symptom('SEC_007', 'Cash box tamper switch triggered').
has_symptom('SEC_007', 'Forcible entry detected').
has_symptom('SEC_007', 'Lock integrity compromised').
has_symptom('SEC_007', 'Access panel forced open').
has_cause('SEC_007', 'Armed robbery attempt').
has_cause('SEC_007', 'Forced entry for theft').
has_cause('SEC_007', 'Technical malfunction of lock').
resolution_step('SEC_007', 1, 'Cease all cash dispensing immediately').
resolution_step('SEC_007', 2, 'Alert police and branch security').
resolution_step('SEC_007', 3, 'Lock down ATM physical access').
resolution_step('SEC_007', 4, 'Document all visible damage with photos').
resolution_step('SEC_007', 5, 'Retrieve cash box and secure in vault').
resolution_step('SEC_007', 6, 'Investigate if cash is missing or tampered').
resolution_step('SEC_007', 7, 'Schedule engineer for lock system repair').

fault_profile('SEC_008', 'Security', 'Authentication', 'Biometric Authentication Failure', 'HIGH').
fault_description('SEC_008', 'Fingerprint or other biometric authentication system malfunction or compromise.').
has_error_code('SEC_008', 'SEC070').
has_error_code('SEC_008', 'BIO_AUTH_FAIL').
has_symptom('SEC_008', 'Fingerprint sensor not responding').
has_symptom('SEC_008', 'Biometric read errors').
has_symptom('SEC_008', 'Authentication consistently failing').
has_symptom('SEC_008', 'Sensor cover damaged or dirty').
has_cause('SEC_008', 'Sensor hardware failure').
has_cause('SEC_008', 'Damaged fingerprint reader').
has_cause('SEC_008', 'Spoofing attempt with fake fingerprint').
has_cause('SEC_008', 'Contaminated sensor surface').
resolution_step('SEC_008', 1, 'Disable biometric authentication temporarily').
resolution_step('SEC_008', 2, 'Switch to PIN-only mode').
resolution_step('SEC_008', 3, 'Clean biometric sensor with appropriate material').
resolution_step('SEC_008', 4, 'Test sensor functionality').
resolution_step('SEC_008', 5, 'If still failing, schedule engineer replacement').
resolution_step('SEC_008', 6, 'Notify branch staff of authentication method change').

fault_profile('SEC_009', 'Security', 'Software', 'Malware/Software Tampering Detected', 'CRITICAL').
fault_description('SEC_009', 'Suspicious code execution, unauthorized software, or signs of malware detected.').
has_error_code('SEC_009', 'SEC080').
has_error_code('SEC_009', 'MALWARE_ALERT').
has_symptom('SEC_009', 'Unexpected process execution').
has_symptom('SEC_009', 'Memory corruption detected').
has_symptom('SEC_009', 'Unauthorized file modifications').
has_symptom('SEC_009', 'Checksum verification failed').
has_cause('SEC_009', 'Malware infection').
has_cause('SEC_009', 'Unauthorized software installation').
has_cause('SEC_009', 'Rootkit attack').
has_cause('SEC_009', 'Software injection attack').
resolution_step('SEC_009', 1, 'Take ATM offline immediately').
resolution_step('SEC_009', 2, 'Isolate from network').
resolution_step('SEC_009', 3, 'Do not process any transactions').
resolution_step('SEC_009', 4, 'Alert information security team').
resolution_step('SEC_009', 5, 'Perform full integrity scan').
resolution_step('SEC_009', 6, 'Restore from verified clean image if compromised').
resolution_step('SEC_009', 7, 'Investigate all recent network access logs').

fault_profile('SEC_010', 'Security', 'Access Control', 'Door Lock Status Anomaly', 'HIGH').
fault_description('SEC_010', 'ATM access panel or service door lock is in an unexpected state.').
has_error_code('SEC_010', 'SEC090').
has_error_code('SEC_010', 'DOOR_LOCK_FAIL').
has_symptom('SEC_010', 'Service door lock disengaged unexpectedly').
has_symptom('SEC_010', 'Door ajar sensor triggered').
has_symptom('SEC_010', 'Lock actuator failure').
has_symptom('SEC_010', 'Security panel opened without authorization').
has_cause('SEC_010', 'Attempted unauthorized access').
has_cause('SEC_010', 'Lock mechanism failure').
has_cause('SEC_010', 'Electronic lock failure').
has_cause('SEC_010', 'Forced entry attempt').
resolution_step('SEC_010', 1, 'Verify no unauthorized access occurred').
resolution_step('SEC_010', 2, 'Check all security seals and tape').
resolution_step('SEC_010', 3, 'Inspect for signs of forced entry').
resolution_step('SEC_010', 4, 'Test door lock mechanism').
resolution_step('SEC_010', 5, 'If lock faulty, schedule replacement').
resolution_step('SEC_010', 6, 'Review CCTV footage').
resolution_step('SEC_010', 7, 'Document all findings in maintenance log').

fault_profile('SEC_011', 'Security', 'Authentication', 'Invalid PIN Length Detected', 'MEDIUM').
fault_description('SEC_011', 'Cardholder attempted to enter a PIN with incorrect length (not 4 digits).').
has_error_code('SEC_011', 'SEC_PIN_INVALID').
has_error_code('SEC_011', 'PIN_LEN_ERR').
has_symptom('SEC_011', 'PIN entry attempt with 3 digits').
has_symptom('SEC_011', 'PIN entry attempt with more than 4 digits').
has_symptom('SEC_011', 'PIN format validation failed').
has_symptom('SEC_011', 'Invalid PIN length error').
has_cause('SEC_011', 'User input error').
has_cause('SEC_011', 'PIN pad malfunction sending incorrect input').
has_cause('SEC_011', 'Card cloning with altered PIN requirements').
has_cause('SEC_011', 'System accepting invalid PIN format').
resolution_step('SEC_011', 1, 'Prompt user to re-enter PIN with exactly 4 digits').
resolution_step('SEC_011', 2, 'Verify PIN pad is functioning correctly').
resolution_step('SEC_011', 3, 'If repeated failures, inspect PIN pad for hardware issues').
resolution_step('SEC_011', 4, 'Check system logs for PIN entry validation errors').
resolution_step('SEC_011', 5, 'Alert user of correct PIN format if needed').
resolution_step('SEC_011', 6, 'Consider temporary PIN format override if legitimately needed').

fault_profile('SEC_012', 'Security', 'Card Validation', 'Foreign Or Unrecognized Card Used', 'HIGH').
fault_description('SEC_012', 'Cardholder used a card that is not recognized by the system or issued by an unauthorized card network.').
has_error_code('SEC_012', 'SEC_CARD_UNKNOWN').
has_error_code('SEC_012', 'CARD_NOT_RECOGNIZED').
has_error_code('SEC_012', 'FOREIGN_CARD_DETECTED').
has_symptom('SEC_012', 'Card not recognized by system').
has_symptom('SEC_012', 'Card issuer not in accepted network list').
has_symptom('SEC_012', 'Card type not supported').
has_symptom('SEC_012', 'Card validation check failed').
has_symptom('SEC_012', 'Unknown card BIN detected').
has_cause('SEC_012', 'Counterfeit card used').
has_cause('SEC_012', 'Card from unsupported issuer').
has_cause('SEC_012', 'Card from different country not accepted').
has_cause('SEC_012', 'Card network not provisioned in ATM').
has_cause('SEC_012', 'Card data has been forged or altered').
resolution_step('SEC_012', 1, 'Retain card in secure bin immediately').
resolution_step('SEC_012', 2, 'Display message: Card cannot be processed').
resolution_step('SEC_012', 3, 'Alert fraud team if suspected counterfeit').
resolution_step('SEC_012', 4, 'Record card details in security log').
resolution_step('SEC_012', 5, 'Check card network provisioning settings').
resolution_step('SEC_012', 6, 'Verify against card issuer database if available').
resolution_step('SEC_012', 7, 'Contact cardholder to verify card legitimacy').
resolution_step('SEC_012', 8, 'Report to card network if fraud suspected').

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
