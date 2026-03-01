const ExplanationPanel = ({ explanation = [] }) => {
  return (
    <div style={{
      backgroundColor: "#1e1e2e",
      color: "#cdd6f4",
      padding: "20px",
      borderRadius: "8px",
      fontFamily: "monospace",
      fontSize: "14px",
    }}>
      <h3 style={{ color: "#89b4fa", marginBottom: "12px" }}>
        🔍 Diagnosis Explanation
      </h3>
      {explanation.length === 0 ? (
        <p style={{ color: "#6c7086" }}>No explanation available yet.</p>
      ) : (
        <ol style={{ paddingLeft: "20px" }}>
          {explanation.map((step, index) => (
            <li key={index} style={{ marginBottom: "8px" }}>
              {step}
            </li>
          ))}
        </ol>
      )}
    </div>
  );
};

export default ExplanationPanel;