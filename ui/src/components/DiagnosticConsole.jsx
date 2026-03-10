import { useState, useEffect } from "react";
import AlertBanner from "./AlertBanner";
import ExplanationPanel from "./ExplanationPanel";
import RemediationWorkflow from "./RemediationWorkflow";
import { api } from "../services/api";

const DiagnosticConsole = ({ atmId = "ATM-001" }) => {
  const [running, setRunning] = useState(false);
  const [diagnosed, setDiagnosed] = useState(false);
  const [diagnosis, setDiagnosis] = useState(null);
  const [symptoms, setSymptoms] = useState("");
  const [errorCodes, setErrorCodes] = useState("");
  const [apiStatus, setApiStatus] = useState("checking");
  const [allFaults, setAllFaults] = useState([]);
  const [error, setError] = useState(null);

  // Check API health on mount
  useEffect(() => {
    checkApiHealth();
    loadFaults();
  }, []);

  const checkApiHealth = async () => {
    try {
      await api.healthCheck();
      setApiStatus("connected");
    } catch (err) {
      setApiStatus("disconnected");
    }
  };

  const loadFaults = async () => {
    try {
      const result = await api.getAllFaults();
      if (result.success) {
        setAllFaults(result.faults);
      }
    } catch (err) {
      console.error("Failed to load faults:", err);
    }
  };

  const handleRunDiagnosis = async () => {
    setRunning(true);
    setError(null);
    
    // Parse comma-separated inputs
    const symptomList = symptoms
      .split(',')
      .map(s => s.trim())
      .filter(Boolean);
    const codeList = errorCodes
      .split(',')
      .map(c => c.trim())
      .filter(Boolean);

    if (symptomList.length === 0 && codeList.length === 0) {
      setError("Please enter at least one symptom or error code");
      setRunning(false);
      return;
    }

    try {
      const result = await api.diagnose(symptomList, codeList);
      
      if (result.success && result.diagnoses.length > 0) {
        const topFault = result.diagnoses[0];
        
        // Get workflow for remediation steps
        const workflowResult = await api.getWorkflow(topFault.fault_id);
        
        // Get explanation
        const explainResult = await api.getExplanation(
          topFault.fault_id,
          symptomList,
          codeList
        );

        setDiagnosis({
          severity: topFault.severity?.toLowerCase() || "medium",
          message: `${topFault.title} detected on ${atmId}`,
          explanation: explainResult.success 
            ? explainResult.explanation 
            : [`Fault ID: ${topFault.fault_id}`, `Confidence: ${topFault.confidence * 100}%`],
          remediationSteps: workflowResult.success 
            ? workflowResult.workflow.steps.map(s => s.action)
            : ["Contact support for resolution steps"],
          faultTitle: topFault.title,
          faultId: topFault.fault_id,
          confidence: topFault.confidence,
          domain: topFault.domain,
          allDiagnoses: result.diagnoses
        });
        setDiagnosed(true);
      } else {
        setDiagnosis({
          severity: "low",
          message: "No matching faults found",
          explanation: [
            "The provided symptoms and error codes did not match any known fault patterns.",
            "Suggestions:",
            "• Verify the symptoms are entered correctly",
            "• Check the error codes against the ATM display",
            "• Try adding more observations"
          ],
          remediationSteps: [
            "Review ATM error display for additional codes",
            "Check ATM physical condition",
            "Contact technical support if issue persists"
          ],
          faultTitle: "No Matching Fault",
          confidence: 0,
          allDiagnoses: []
        });
        setDiagnosed(true);
      }
    } catch (err) {
      console.error("Diagnosis error:", err);
      setError(`API Error: ${err.message}. Make sure the backend is running on localhost:5000`);
    }
    
    setRunning(false);
  };

  const handleReset = () => {
    setDiagnosed(false);
    setRunning(false);
    setDiagnosis(null);
    setError(null);
  };

  const handleQuickFill = (symptom, code) => {
    setSymptoms(symptom);
    setErrorCodes(code);
  };

  // Quick test scenarios
  const testScenarios = [
    { label: "Card Reader Jam", symptom: "Card not ejected", code: "3A1" },
    { label: "Cash Dispenser Jam", symptom: "Dispense attempt fails", code: "4B1" },
    { label: "Paper Jam", symptom: "Receipt not printed", code: "5E3" },
    { label: "Network Issue", symptom: "Network connection lost", code: "NET001" },
  ];

  return (
    <div style={{
      backgroundColor: "#f1f3f5",
      minHeight: "100vh",
      padding: "24px",
      fontFamily: "Arial, sans-serif",
    }}>
      <div style={{
        maxWidth: "800px",
        margin: "0 auto",
      }}>
        <h2 style={{ color: "#212529", marginBottom: "4px" }}>
          🏧 ATM Diagnostic Console
        </h2>
        <p style={{ color: "#6c757d", marginBottom: "8px" }}>
          ATM ID: <strong>{atmId}</strong>
        </p>
        
        {/* API Status Indicator */}
        <div style={{ 
          marginBottom: "24px",
          display: "flex",
          alignItems: "center",
          gap: "8px"
        }}>
          <span style={{
            width: "10px",
            height: "10px",
            borderRadius: "50%",
            backgroundColor: apiStatus === "connected" ? "#28a745" : 
                           apiStatus === "disconnected" ? "#dc3545" : "#ffc107"
          }}></span>
          <span style={{ color: "#6c757d", fontSize: "14px" }}>
            {apiStatus === "connected" ? "Backend Connected" :
             apiStatus === "disconnected" ? "Backend Disconnected - Start with: python integration/api.py" :
             "Checking connection..."}
          </span>
          {apiStatus === "connected" && allFaults.length > 0 && (
            <span style={{ color: "#6c757d", fontSize: "14px" }}>
              ({allFaults.length} faults loaded)
            </span>
          )}
        </div>

        {!diagnosed && (
          <div style={{
            backgroundColor: "white",
            padding: "24px",
            borderRadius: "8px",
            boxShadow: "0 2px 4px rgba(0,0,0,0.1)",
            marginBottom: "24px"
          }}>
            <h3 style={{ margin: "0 0 16px 0", color: "#212529" }}>
              Enter Observations
            </h3>
            
            {/* Symptoms Input */}
            <div style={{ marginBottom: "16px" }}>
              <label style={{ 
                display: "block", 
                marginBottom: "6px", 
                color: "#495057",
                fontWeight: "500"
              }}>
                Symptoms (comma-separated)
              </label>
              <input
                type="text"
                value={symptoms}
                onChange={(e) => setSymptoms(e.target.value)}
                placeholder="e.g., Card not ejected, Reader status: JAMMED"
                style={{
                  width: "100%",
                  padding: "10px 12px",
                  border: "1px solid #ced4da",
                  borderRadius: "6px",
                  fontSize: "14px",
                  boxSizing: "border-box"
                }}
              />
            </div>

            {/* Error Codes Input */}
            <div style={{ marginBottom: "16px" }}>
              <label style={{ 
                display: "block", 
                marginBottom: "6px", 
                color: "#495057",
                fontWeight: "500"
              }}>
                Error Codes (comma-separated)
              </label>
              <input
                type="text"
                value={errorCodes}
                onChange={(e) => setErrorCodes(e.target.value)}
                placeholder="e.g., 3A1, ICM001"
                style={{
                  width: "100%",
                  padding: "10px 12px",
                  border: "1px solid #ced4da",
                  borderRadius: "6px",
                  fontSize: "14px",
                  boxSizing: "border-box"
                }}
              />
            </div>

            {/* Quick Test Scenarios */}
            <div style={{ marginBottom: "16px" }}>
              <label style={{ 
                display: "block", 
                marginBottom: "6px", 
                color: "#6c757d",
                fontSize: "13px"
              }}>
                Quick Test Scenarios:
              </label>
              <div style={{ display: "flex", gap: "8px", flexWrap: "wrap" }}>
                {testScenarios.map((scenario, idx) => (
                  <button
                    key={idx}
                    onClick={() => handleQuickFill(scenario.symptom, scenario.code)}
                    style={{
                      padding: "6px 12px",
                      backgroundColor: "#e9ecef",
                      border: "1px solid #ced4da",
                      borderRadius: "4px",
                      fontSize: "12px",
                      cursor: "pointer",
                      color: "#495057"
                    }}
                  >
                    {scenario.label}
                  </button>
                ))}
              </div>
            </div>

            {/* Error Message */}
            {error && (
              <div style={{
                padding: "12px",
                backgroundColor: "#f8d7da",
                border: "1px solid #f5c6cb",
                borderRadius: "6px",
                color: "#721c24",
                marginBottom: "16px",
                fontSize: "14px"
              }}>
                ⚠️ {error}
              </div>
            )}

            {/* Run Button */}
            <button 
              onClick={handleRunDiagnosis}
              disabled={running || apiStatus !== "connected"}
              style={{
                padding: "12px 28px",
                backgroundColor: apiStatus === "connected" ? "#007bff" : "#6c757d",
                color: "white",
                border: "none",
                borderRadius: "8px",
                fontSize: "16px",
                cursor: apiStatus === "connected" ? "pointer" : "not-allowed",
                opacity: running ? 0.7 : 1
              }}
            >
              {running ? "⏳ Analyzing..." : "▶ Run Diagnosis"}
            </button>
          </div>
        )}

        {running && (
          <div style={{
            textAlign: "center",
            padding: "40px",
            backgroundColor: "white",
            borderRadius: "8px"
          }}>
            <div style={{ fontSize: "48px", marginBottom: "16px" }}>🔍</div>
            <p style={{ color: "#007bff", fontSize: "16px" }}>
              Analyzing observations for {atmId}...
            </p>
            <p style={{ color: "#6c757d", fontSize: "14px" }}>
              Querying Prolog inference engine
            </p>
          </div>
        )}

        {diagnosed && diagnosis && (
          <div>
            <AlertBanner
              severity={diagnosis.severity}
              message={diagnosis.message}
            />

            {/* Confidence Score */}
            {diagnosis.confidence > 0 && (
              <div style={{
                backgroundColor: "white",
                padding: "16px",
                borderRadius: "8px",
                marginBottom: "16px",
                display: "flex",
                justifyContent: "space-between",
                alignItems: "center"
              }}>
                <div>
                  <span style={{ color: "#6c757d", fontSize: "14px" }}>
                    Fault ID: <strong>{diagnosis.faultId}</strong>
                  </span>
                  <span style={{ 
                    marginLeft: "16px", 
                    color: "#6c757d", 
                    fontSize: "14px" 
                  }}>
                    Domain: <strong>{diagnosis.domain}</strong>
                  </span>
                </div>
                <div style={{
                  backgroundColor: diagnosis.confidence >= 0.8 ? "#d4edda" : 
                                  diagnosis.confidence >= 0.5 ? "#fff3cd" : "#f8d7da",
                  padding: "6px 12px",
                  borderRadius: "4px",
                  fontSize: "14px",
                  fontWeight: "bold",
                  color: diagnosis.confidence >= 0.8 ? "#155724" : 
                         diagnosis.confidence >= 0.5 ? "#856404" : "#721c24"
                }}>
                  Confidence: {Math.round(diagnosis.confidence * 100)}%
                </div>
              </div>
            )}

            <div style={{ marginBottom: "24px" }}>
              <ExplanationPanel explanation={diagnosis.explanation} />
            </div>

            <div style={{ marginBottom: "24px" }}>
              <RemediationWorkflow
                steps={diagnosis.remediationSteps}
                faultTitle={diagnosis.faultTitle}
              />
            </div>

            {/* Other Possible Diagnoses */}
            {diagnosis.allDiagnoses && diagnosis.allDiagnoses.length > 1 && (
              <div style={{
                backgroundColor: "white",
                padding: "16px",
                borderRadius: "8px",
                marginBottom: "24px"
              }}>
                <h4 style={{ margin: "0 0 12px 0", color: "#495057" }}>
                  Other Possible Diagnoses
                </h4>
                {diagnosis.allDiagnoses.slice(1, 4).map((d, idx) => (
                  <div key={idx} style={{
                    padding: "8px 12px",
                    backgroundColor: "#f8f9fa",
                    borderRadius: "4px",
                    marginBottom: "8px",
                    fontSize: "14px"
                  }}>
                    <strong>{d.title}</strong>
                    <span style={{ color: "#6c757d", marginLeft: "12px" }}>
                      ({d.domain}) - {Math.round(d.confidence * 100)}% confidence
                    </span>
                  </div>
                ))}
              </div>
            )}

            <button onClick={handleReset} style={{
              padding: "10px 20px",
              backgroundColor: "#6c757d",
              color: "white",
              border: "none",
              borderRadius: "6px",
              cursor: "pointer",
              fontSize: "14px",
            }}>
              🔄 New Diagnosis
            </button>
          </div>
        )}
      </div>
    </div>
  );
};

export default DiagnosticConsole;