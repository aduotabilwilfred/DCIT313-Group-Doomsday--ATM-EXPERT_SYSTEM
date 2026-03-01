import { useState } from "react";
import AlertBanner from "./AlertBanner";
import ExplanationPanel from "./ExplanationPanel";
import RemediationWorkflow from "./RemediationWorkflow";

const DiagnosticConsole = ({ atmId = "ATM-001" }) => {
  const [running, setRunning] = useState(false);
  const [diagnosed, setDiagnosed] = useState(false);

  const mockDiagnosis = {
    severity: "critical",
    message: "Card reader hardware failure detected on ATM-001",
    explanation: [
      "Error code CR-404 received from card reader module",
      "Sensor data shows card reader is unresponsive",
      "Cross-referenced with hardware fault profile HW-012",
      "Diagnosis: Physical card reader failure confirmed",
    ],
    remediationSteps: [
      "Power off the ATM using the main switch",
      "Open the ATM front panel using the engineer key",
      "Locate the card reader module behind the card slot",
      "Disconnect and reconnect the card reader cable",
      "If issue persists, replace the card reader module",
      "Power the ATM back on and run a self-test",
    ],
    faultTitle: "Card Reader Hardware Failure",
  };

  const handleRunDiagnosis = () => {
    setRunning(true);
    setTimeout(() => {
      setRunning(false);
      setDiagnosed(true);
    }, 2000);
  };

  const handleReset = () => {
    setDiagnosed(false);
    setRunning(false);
  };

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
        <p style={{ color: "#6c757d", marginBottom: "24px" }}>
          ATM ID: <strong>{atmId}</strong>
        </p>

        {!diagnosed && !running && (
          <button onClick={handleRunDiagnosis} style={{
            padding: "12px 28px",
            backgroundColor: "#007bff",
            color: "white",
            border: "none",
            borderRadius: "8px",
            fontSize: "16px",
            cursor: "pointer",
            marginBottom: "24px",
          }}>
            ▶ Run Diagnosis
          </button>
        )}

        {running && (
          <p style={{
            color: "#007bff",
            fontSize: "16px",
            marginBottom: "24px",
          }}>
            ⏳ Running diagnosis on {atmId}...
          </p>
        )}

        {diagnosed && (
          <div>
            <AlertBanner
              severity={mockDiagnosis.severity}
              message={mockDiagnosis.message}
            />

            <div style={{ marginBottom: "24px" }}>
              <ExplanationPanel explanation={mockDiagnosis.explanation} />
            </div>

            <div style={{ marginBottom: "24px" }}>
              <RemediationWorkflow
                steps={mockDiagnosis.remediationSteps}
                faultTitle={mockDiagnosis.faultTitle}
              />
            </div>

            <button onClick={handleReset} style={{
              padding: "10px 20px",
              backgroundColor: "#6c757d",
              color: "white",
              border: "none",
              borderRadius: "6px",
              cursor: "pointer",
              fontSize: "14px",
            }}>
              🔄 Reset Console
            </button>
          </div>
        )}
      </div>
    </div>
  );
};

export default DiagnosticConsole;