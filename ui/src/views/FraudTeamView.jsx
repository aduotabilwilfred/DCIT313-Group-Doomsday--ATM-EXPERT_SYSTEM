import AlertBanner from "../components/AlertBanner";
import { useState } from "react";

const FraudTeamView = () => {
  const [selectedAlert, setSelectedAlert] = useState(null);

  const fraudAlerts = [
    {
      id: "FA-001",
      atmId: "ATM-003",
      type: "Card Skimming",
      severity: "critical",
      time: "2026-03-01 05:12 AM",
      location: "Branch B - Kumasi",
      description: "Foreign device detected on card reader slot. Possible skimmer attached.",
      status: "Open",
    },
    {
      id: "FA-002",
      atmId: "ATM-007",
      type: "PIN Pad Tampering",
      severity: "critical",
      time: "2026-03-01 04:45 AM",
      location: "Branch C - Takoradi",
      description: "PIN pad overlay detected by tamper sensor. ATM locked down automatically.",
      status: "Open",
    },
    {
      id: "FA-003",
      atmId: "ATM-011",
      type: "Anomalous Transactions",
      severity: "high",
      time: "2026-03-01 03:30 AM",
      location: "Branch D - Tema",
      description: "15 consecutive max withdrawals from different cards within 10 minutes.",
      status: "Under Review",
    },
    {
      id: "FA-004",
      atmId: "ATM-015",
      type: "Physical Attack",
      severity: "high",
      time: "2026-03-01 02:10 AM",
      location: "Branch E - Accra North",
      description: "Vibration sensor triggered. Possible forced entry attempt on ATM cabinet.",
      status: "Escalated",
    },
  ];

  return (
    <div style={{
      backgroundColor: "#1a0a0a",
      minHeight: "100vh",
      fontFamily: "Arial, sans-serif",
      color: "#f8d7da",
    }}>
      {/* Header */}
      <div style={{
        backgroundColor: "#2d0a0a",
        padding: "16px 24px",
        display: "flex",
        alignItems: "center",
        justifyContent: "space-between",
        borderBottom: "2px solid #dc3545",
      }}>
        <div style={{ display: "flex", alignItems: "center", gap: "12px" }}>
          <span style={{ fontSize: "24px" }}>🛡️</span>
          <div>
            <h2 style={{ margin: 0, color: "#ff6b6b" }}>
              ATM Expert — Fraud & Security Monitor
            </h2>
            <p style={{ margin: 0, fontSize: "13px", color: "#6c7086" }}>
              Real-time fraud detection and security alerts
            </p>
          </div>
        </div>
        <div style={{
          backgroundColor: "#dc3545",
          borderRadius: "20px",
          padding: "6px 16px",
          fontSize: "13px",
          fontWeight: "bold",
        }}>
          🔴 {fraudAlerts.filter(a => a.status === "Open").length} Active Threats
        </div>
      </div>

      <div style={{ padding: "24px" }}>
        <AlertBanner
          severity="critical"
          message="2 critical fraud threats detected across the ATM network. Immediate action required!"
        />

        {/* Fraud Alerts List */}
        <div style={{ marginBottom: "24px" }}>
          <h4 style={{ color: "#ff6b6b", marginBottom: "16px" }}>
            🚨 Active Fraud Alerts
          </h4>
          {fraudAlerts.map((alert) => (
            <div
              key={alert.id}
              onClick={() => setSelectedAlert(
                selectedAlert?.id === alert.id ? null : alert
              )}
              style={{
                backgroundColor: "#2d0a0a",
                border: `1px solid ${alert.severity === "critical" ? "#dc3545" : "#ffc107"}`,
                borderRadius: "8px",
                padding: "16px",
                marginBottom: "12px",
                cursor: "pointer",
                transition: "opacity 0.2s",
              }}
            >
              <div style={{
                display: "flex",
                justifyContent: "space-between",
                alignItems: "center",
              }}>
                <div>
                  <span style={{
                    fontWeight: "bold",
                    color: alert.severity === "critical" ? "#ff6b6b" : "#ffc107",
                    marginRight: "12px",
                  }}>
                    {alert.severity === "critical" ? "🔴" : "🟡"} {alert.type}
                  </span>
                  <span style={{ color: "#6c7086", fontSize: "13px" }}>
                    {alert.atmId} — {alert.location}
                  </span>
                </div>
                <span style={{
                  padding: "4px 10px",
                  borderRadius: "12px",
                  fontSize: "12px",
                  fontWeight: "bold",
                  backgroundColor:
                    alert.status === "Open" ? "#dc3545" :
                    alert.status === "Escalated" ? "#ffc107" : "#6c757d",
                  color: "white",
                }}>
                  {alert.status}
                </span>
              </div>
              <p style={{
                color: "#6c7086",
                fontSize: "12px",
                margin: "8px 0 0 0",
              }}>
                {alert.time}
              </p>

              {/* Expanded Details */}
              {selectedAlert?.id === alert.id && (
                <div style={{
                  marginTop: "16px",
                  padding: "12px",
                  backgroundColor: "#1a0a0a",
                  borderRadius: "6px",
                  borderLeft: "4px solid #dc3545",
                }}>
                  <p style={{ color: "#f8d7da", marginBottom: "8px" }}>
                    <strong>Alert ID:</strong> {alert.id}
                  </p>
                  <p style={{ color: "#f8d7da", marginBottom: "8px" }}>
                    <strong>Description:</strong> {alert.description}
                  </p>
                  <p style={{ color: "#f8d7da", margin: 0 }}>
                    <strong>Status:</strong> {alert.status}
                  </p>
                </div>
              )}
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default FraudTeamView;