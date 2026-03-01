import { useState } from "react";
import BranchStaffView from "./views/BranchStaffView";
import EngineerView from "./views/EngineerView";
import ManagementView from "./views/ManagementView";
import FraudTeamView from "./views/FraudTeamView";

const App = () => {
  const [role, setRole] = useState(null);

  if (!role) {
    return (
      <div style={{
        backgroundColor: "#1a1a2e",
        minHeight: "100vh",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        fontFamily: "Arial, sans-serif",
      }}>
        <div style={{
          backgroundColor: "#16213e",
          borderRadius: "12px",
          padding: "40px",
          textAlign: "center",
          width: "400px",
          boxShadow: "0 8px 32px rgba(0,0,0,0.4)",
        }}>
          <span style={{ fontSize: "48px" }}>🏧</span>
          <h2 style={{ color: "#89b4fa", marginBottom: "8px" }}>ATM Expert</h2>
          <p style={{ color: "#6c7086", marginBottom: "32px" }}>
            Select your role to continue
          </p>
          {[
            { role: "branch", label: "🏦 Branch Staff", color: "#007bff" },
            { role: "engineer", label: "🔧 Field Engineer", color: "#28a745" },
            { role: "management", label: "📊 Management", color: "#6f42c1" },
            { role: "fraud", label: "🛡️ Fraud Team", color: "#dc3545" },
          ].map((item) => (
            <button
              key={item.role}
              onClick={() => setRole(item.role)}
              style={{
                display: "block",
                width: "100%",
                padding: "12px",
                marginBottom: "12px",
                backgroundColor: item.color,
                color: "white",
                border: "none",
                borderRadius: "8px",
                fontSize: "15px",
                cursor: "pointer",
              }}
            >
              {item.label}
            </button>
          ))}
        </div>
      </div>
    );
  }

  return (
    <div>
      <button
        onClick={() => setRole(null)}
        style={{
          position: "fixed",
          top: "12px",
          right: "16px",
          padding: "8px 16px",
          backgroundColor: "#343a40",
          color: "white",
          border: "none",
          borderRadius: "6px",
          cursor: "pointer",
          fontSize: "13px",
          zIndex: 1000,
        }}
      >
        ← Switch Role
      </button>

      {role === "branch" && <BranchStaffView />}
      {role === "engineer" && <EngineerView />}
      {role === "management" && <ManagementView />}
      {role === "fraud" && <FraudTeamView />}
    </div>
  );
};

export default App;