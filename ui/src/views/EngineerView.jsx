import DiagnosticConsole from "../components/DiagnosticConsole";
import AlertBanner from "../components/AlertBanner";
import ExplanationPanel from "../components/ExplanationPanel";
import EscalationScreen from "../components/EscalationScreen";
import { useState } from "react";

const EngineerView = () => {
  const [showEscalation, setShowEscalation] = useState(false);

  const technicalDetails = {
    atmId: "ATM-001",
    model: "NCR SelfServ 87",
    location: "Branch A - Accra Central",
    lastService: "2026-01-15",
    errorCode: "CR-404",
    firmwareVersion: "v3.2.1",
    uptime: "99.2%",
    lastTransaction: "2026-03-01 06:45 AM",
  };

  const engineerExplanation = [
    "Error code CR-404 triggered by card reader firmware",
    "Sensor polling returned NULL for card reader module",
    "Hardware fault profile HW-012 matched with 94% confidence",
    "Component usage threshold exceeded — card reader at 98% wear",
    "Predictive maintenance alert was ignored 3 days ago",
    "Full hardware replacement recommended",
  ];

  return (
    <div style={{
      backgroundColor: "#1a1a2e",
      minHeight: "100vh",
      fontFamily: "monospace",
      color: "#cdd6f4",
    }}>
      {/* Header */}
      <div style={{
        backgroundColor: "#16213e",
        padding: "16px 24px",
        display: "flex",
        alignItems: "center",
        justifyContent: "space-between",
        borderBottom: "1px solid #0f3460",
      }}>
        <div style={{ display: "flex", alignItems: "center", gap: "12px" }}>
          <span style={{ fontSize: "24px" }}>🔧</span>
          <div>
            <h2 style={{ margin: 0, color: "#89b4fa" }}>
              ATM Expert — Field Engineer Console
            </h2>
            <p style={{ margin: 0, fontSize: "12px", color: "#6c7086" }}>
              Full technical diagnostic access
            </p>
          </div>
        </div>
        <button
          onClick={() => setShowEscalation(!showEscalation)}
          style={{
            padding: "8px 16px",
            backgroundColor: "#dc3545",
            color: "white",
            border: "none",
            borderRadius: "6px",
            cursor: "pointer",
            fontSize: "13px",
          }}>
          🚨 Escalate to Tier-2
        </button>
      </div>

      <div style={{ padding: "24px" }}>
        <AlertBanner
          severity="critical"
          message="CR-404: Card reader hardware failure — immediate attention required"
        />

        {/* Technical Details Table */}
        <div style={{
          backgroundColor: "#16213e",
          borderRadius: "8px",
          padding: "20px",
          marginBottom: "24px",
          border: "1px solid #0f3460",
        }}>
          <h4 style={{ color: "#89b4fa", marginBottom: "16px" }}>
            🖥️ ATM Technical Details
          </h4>
          <table style={{ width: "100%", borderCollapse: "collapse" }}>
            <tbody>
              {Object.entries(technicalDetails).map(([key, value]) => (
                <tr key={key} style={{ borderBottom: "1px solid #0f3460" }}>
                  <td style={{
                    padding: "8px 12px",
                    color: "#6c7086",
                    textTransform: "capitalize",
                    width: "40%",
                  }}>
                    {key.replace(/([A-Z])/g, " $1")}
                  </td>
                  <td style={{ padding: "8px 12px", color: "#cdd6f4" }}>
                    {value}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>

        {/* Explanation Panel */}
        <div style={{ marginBottom: "24px" }}>
          <ExplanationPanel explanation={engineerExplanation} />
        </div>

        {/* Escalation Screen */}
        {showEscalation && (
          <div style={{ marginBottom: "24px" }}>
            <EscalationScreen
              atmId={technicalDetails.atmId}
              faultSummary="CR-404 card reader hardware failure. Component at 98% wear. Full replacement required."
            />
          </div>
        )}

        {/* Diagnostic Console */}
        <DiagnosticConsole atmId={technicalDetails.atmId} />
      </div>
    </div>
  );
};

export default EngineerView;