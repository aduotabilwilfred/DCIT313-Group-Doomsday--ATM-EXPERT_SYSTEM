const KPIDashboard = ({ stats = {} }) => {
  const defaultStats = {
    totalATMs: stats.totalATMs || 20,
    onlineATMs: stats.onlineATMs || 17,
    offlineATMs: stats.offlineATMs || 3,
    faultsToday: stats.faultsToday || 12,
    resolvedToday: stats.resolvedToday || 9,
    escalatedToday: stats.escalatedToday || 2,
    avgResolutionTime: stats.avgResolutionTime || "14 mins",
  };

  const cards = [
    { label: "Total ATMs", value: defaultStats.totalATMs, icon: "🏧", color: "#007bff" },
    { label: "Online", value: defaultStats.onlineATMs, icon: "🟢", color: "#28a745" },
    { label: "Offline", value: defaultStats.offlineATMs, icon: "🔴", color: "#dc3545" },
    { label: "Faults Today", value: defaultStats.faultsToday, icon: "⚠️", color: "#ffc107" },
    { label: "Resolved Today", value: defaultStats.resolvedToday, icon: "✅", color: "#28a745" },
    { label: "Escalated", value: defaultStats.escalatedToday, icon: "🚨", color: "#dc3545" },
    { label: "Avg Resolution Time", value: defaultStats.avgResolutionTime, icon: "⏱️", color: "#6f42c1" },
  ];

  return (
    <div style={{ padding: "24px" }}>
      <h2 style={{ color: "#212529", marginBottom: "24px" }}>
        📊 ATM Network KPI Dashboard
      </h2>
      <div style={{
        display: "grid",
        gridTemplateColumns: "repeat(auto-fit, minmax(160px, 1fr))",
        gap: "16px",
      }}>
        {cards.map((card, index) => (
          <div key={index} style={{
            backgroundColor: "#ffffff",
            border: `2px solid ${card.color}`,
            borderRadius: "10px",
            padding: "20px",
            textAlign: "center",
            boxShadow: "0 2px 8px rgba(0,0,0,0.08)",
          }}>
            <div style={{ fontSize: "28px", marginBottom: "8px" }}>
              {card.icon}
            </div>
            <div style={{
              fontSize: "28px",
              fontWeight: "bold",
              color: card.color,
              marginBottom: "4px",
            }}>
              {card.value}
            </div>
            <div style={{ fontSize: "13px", color: "#6c757d" }}>
              {card.label}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default KPIDashboard;