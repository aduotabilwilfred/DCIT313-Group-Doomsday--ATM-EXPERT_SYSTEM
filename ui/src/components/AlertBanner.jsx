const AlertBanner = ({ severity = "info", message = "No alerts at this time." }) => {
  const colors = {
    critical: "background-color: #ff4444; color: white;",
    high: "background-color: #ff8800; color: white;",
    medium: "background-color: #ffcc00; color: black;",
    info: "background-color: #2196F3; color: white;",
  };

  const icons = {
    critical: "🚨",
    high: "⚠️",
    medium: "ℹ️",
    info: "✅",
  };

  return (
    <div style={{
      padding: "12px 20px",
      borderRadius: "6px",
      marginBottom: "16px",
      fontWeight: "bold",
      fontSize: "14px",
      display: "flex",
      alignItems: "center",
      gap: "10px",
      backgroundColor:
        severity === "critical" ? "#ff4444" :
        severity === "high" ? "#ff8800" :
        severity === "medium" ? "#ffcc00" : "#2196F3",
      color: severity === "medium" ? "black" : "white",
    }}>
      <span>{icons[severity] || "ℹ️"}</span>
      <span>{message}</span>
    </div>
  );
};

export default AlertBanner;