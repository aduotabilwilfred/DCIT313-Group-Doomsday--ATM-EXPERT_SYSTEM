import DiagnosticConsole from "../components/DiagnosticConsole";
import AlertBanner from "../components/AlertBanner";

const BranchStaffView = () => {
  return (
    <div style={{
      backgroundColor: "#ffffff",
      minHeight: "100vh",
      fontFamily: "Arial, sans-serif",
    }}>
      {/* Header */}
      <div style={{
        backgroundColor: "#007bff",
        padding: "16px 24px",
        color: "white",
        display: "flex",
        alignItems: "center",
        gap: "12px",
      }}>
        <span style={{ fontSize: "24px" }}>🏧</span>
        <div>
          <h2 style={{ margin: 0 }}>ATM Expert — Branch Staff Portal</h2>
          <p style={{ margin: 0, fontSize: "13px", opacity: 0.8 }}>
            Guided ATM fault resolution for branch staff
          </p>
        </div>
      </div>

      {/* Alert */}
      <div style={{ padding: "16px 24px 0 24px" }}>
        <AlertBanner
          severity="high"
          message="ATM-001 has reported a fault. Please follow the steps below."
        />
      </div>

      {/* Instructions */}
      <div style={{
        padding: "0 24px 16px 24px",
        backgroundColor: "#e9f7ef",
        margin: "16px 24px",
        borderRadius: "8px",
        border: "1px solid #28a745",
      }}>
        <h4 style={{ color: "#155724" }}>📋 Instructions for Branch Staff</h4>
        <ul style={{ color: "#155724", lineHeight: "1.8" }}>
          <li>Do NOT attempt hardware repairs yourself</li>
          <li>Follow the guided steps shown below</li>
          <li>If the issue is not resolved, use the Escalate button</li>
          <li>Always record the ATM ID when reporting issues</li>
        </ul>
      </div>

      {/* Diagnostic Console */}
      <DiagnosticConsole atmId="ATM-001" />
    </div>
  );
};

export default BranchStaffView;