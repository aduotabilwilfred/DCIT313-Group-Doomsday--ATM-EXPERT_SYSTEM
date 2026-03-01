import { useState } from "react";

const EscalationScreen = ({ faultSummary = "", atmId = "ATM-001" }) => {
  const [notes, setNotes] = useState("");
  const [submitted, setSubmitted] = useState(false);

  const handleSubmit = () => {
    if (notes.trim() === "") {
      alert("Please add some notes before escalating.");
      return;
    }
    setSubmitted(true);
  };

  return (
    <div style={{
      backgroundColor: "#fff3cd",
      border: "1px solid #ffc107",
      borderRadius: "8px",
      padding: "24px",
      maxWidth: "600px",
    }}>
      <h3 style={{ color: "#856404", marginBottom: "8px" }}>
        🚨 Escalate to Tier-2 Engineering
      </h3>
      <p style={{ color: "#6c757d", marginBottom: "16px" }}>
        ATM ID: <strong>{atmId}</strong>
      </p>

      {submitted ? (
        <div style={{ textAlign: "center" }}>
          <p style={{ color: "#28a745", fontSize: "18px", fontWeight: "bold" }}>
            ✅ Escalation submitted successfully!
          </p>
          <p style={{ color: "#6c757d" }}>
            A Tier-2 engineer will be notified shortly.
          </p>
        </div>
      ) : (
        <div>
          <div style={{
            backgroundColor: "#ffffff",
            border: "1px solid #ced4da",
            borderRadius: "6px",
            padding: "12px",
            marginBottom: "16px",
          }}>
            <p style={{ fontWeight: "bold", marginBottom: "4px" }}>
              Fault Summary:
            </p>
            <p style={{ color: "#495057" }}>
              {faultSummary || "No fault summary provided."}
            </p>
          </div>

          <label style={{ fontWeight: "bold", display: "block", marginBottom: "8px" }}>
            Additional Notes:
          </label>
          <textarea
            rows={4}
            value={notes}
            onChange={(e) => setNotes(e.target.value)}
            placeholder="Describe what you observed before escalating..."
            style={{
              width: "100%",
              padding: "10px",
              borderRadius: "6px",
              border: "1px solid #ced4da",
              fontSize: "14px",
              marginBottom: "16px",
              boxSizing: "border-box",
            }}
          />

          <button onClick={handleSubmit} style={{
            padding: "10px 24px",
            backgroundColor: "#dc3545",
            color: "white",
            border: "none",
            borderRadius: "6px",
            cursor: "pointer",
            fontSize: "14px",
          }}>
            Submit Escalation 🚨
          </button>
        </div>
      )}
    </div>
  );
};

export default EscalationScreen;