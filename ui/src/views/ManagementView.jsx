import KPIDashboard from "../components/KPIDashboard";
import AlertBanner from "../components/AlertBanner";

const ManagementView = () => {
  const networkStats = {
    totalATMs: 20,
    onlineATMs: 17,
    offlineATMs: 3,
    faultsToday: 12,
    resolvedToday: 9,
    escalatedToday: 2,
    avgResolutionTime: "14 mins",
  };

  return (
    <div style={{
      backgroundColor: "#f8f9fa",
      minHeight: "100vh",
      fontFamily: "Arial, sans-serif",
    }}>
      {/* Header */}
      <div style={{
        backgroundColor: "#1a1a2e",
        padding: "16px 24px",
        color: "white",
        display: "flex",
        alignItems: "center",
        gap: "12px",
      }}>
        <span style={{ fontSize: "24px" }}>📊</span>
        <div>
          <h2 style={{ margin: 0 }}>ATM Expert — Management Portal</h2>
          <p style={{ margin: 0, fontSize: "13px", opacity: 0.8 }}>
            Network performance overview for bank management
          </p>
        </div>
      </div>

      <div style={{ padding: "24px" }}>
        {/* Alert for offline ATMs */}
        <AlertBanner
          severity="high"
          message="3 ATMs are currently offline across the network. Engineering teams have been notified."
        />

        {/* KPI Dashboard */}
        <KPIDashboard stats={networkStats} />

        {/* Summary Table */}
        <div style={{
          backgroundColor: "#ffffff",
          borderRadius: "8px",
          padding: "24px",
          marginTop: "24px",
          boxShadow: "0 2px 8px rgba(0,0,0,0.08)",
        }}>
          <h4 style={{ color: "#212529", marginBottom: "16px" }}>
            📋 Today's Fault Summary
          </h4>
          <table style={{ width: "100%", borderCollapse: "collapse" }}>
            <thead>
              <tr style={{ backgroundColor: "#f1f3f5" }}>
                <th style={{ padding: "10px 12px", textAlign: "left", color: "#495057" }}>ATM ID</th>
                <th style={{ padding: "10px 12px", textAlign: "left", color: "#495057" }}>Fault Type</th>
                <th style={{ padding: "10px 12px", textAlign: "left", color: "#495057" }}>Status</th>
                <th style={{ padding: "10px 12px", textAlign: "left", color: "#495057" }}>Resolution Time</th>
              </tr>
            </thead>
            <tbody>
              {[
                { id: "ATM-001", fault: "Card Reader Failure", status: "Resolved", time: "12 mins" },
                { id: "ATM-005", fault: "Cash Jam", status: "Resolved", time: "8 mins" },
                { id: "ATM-009", fault: "Network Timeout", status: "Escalated", time: "Pending" },
                { id: "ATM-013", fault: "Printer Fault", status: "In Progress", time: "—" },
                { id: "ATM-017", fault: "Software Crash", status: "Resolved", time: "22 mins" },
              ].map((row, index) => (
                <tr key={index} style={{ borderBottom: "1px solid #dee2e6" }}>
                  <td style={{ padding: "10px 12px", color: "#212529" }}>{row.id}</td>
                  <td style={{ padding: "10px 12px", color: "#495057" }}>{row.fault}</td>
                  <td style={{ padding: "10px 12px" }}>
                    <span style={{
                      padding: "4px 10px",
                      borderRadius: "12px",
                      fontSize: "12px",
                      fontWeight: "bold",
                      backgroundColor:
                        row.status === "Resolved" ? "#d4edda" :
                        row.status === "Escalated" ? "#f8d7da" : "#fff3cd",
                      color:
                        row.status === "Resolved" ? "#155724" :
                        row.status === "Escalated" ? "#721c24" : "#856404",
                    }}>
                      {row.status}
                    </span>
                  </td>
                  <td style={{ padding: "10px 12px", color: "#495057" }}>{row.time}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};

export default ManagementView;