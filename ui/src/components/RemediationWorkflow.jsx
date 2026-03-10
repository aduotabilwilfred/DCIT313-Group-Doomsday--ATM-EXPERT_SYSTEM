import { useState } from "react";

const RemediationWorkflow = ({ steps = [], faultTitle = "Unknown Fault" }) => {
  const [currentStep, setCurrentStep] = useState(0);
  const [completed, setCompleted] = useState(false);

  const handleNext = () => {
    if (currentStep + 1 >= steps.length) {
      setCompleted(true);
    } else {
      setCurrentStep(currentStep + 1);
    }
  };

  const handleReset = () => {
    setCurrentStep(0);
    setCompleted(false);
  };

  return (
    <div style={{
      backgroundColor: "#f8f9fa",
      border: "1px solid #dee2e6",
      borderRadius: "8px",
      padding: "24px",
      maxWidth: "600px",
    }}>
      <h3 style={{ color: "#212529", marginBottom: "8px" }}>
        🔧 Remediation Workflow
      </h3>
      <p style={{ color: "#6c757d", marginBottom: "20px" }}>
        Fault: <strong>{faultTitle}</strong>
      </p>

      {completed ? (
        <div style={{ textAlign: "center" }}>
          <p style={{ color: "#28a745", fontSize: "18px", fontWeight: "bold" }}>
            ✅ All steps completed!
          </p>
          <button onClick={handleReset} style={{
            marginTop: "12px",
            padding: "10px 20px",
            backgroundColor: "#007bff",
            color: "white",
            border: "none",
            borderRadius: "6px",
            cursor: "pointer",
          }}>
            Start Again
          </button>
        </div>
      ) : (
        <div>
          <p style={{ color: "#6c757d", fontSize: "13px" }}>
            Step {currentStep + 1} of {steps.length}
          </p>
          <div style={{
            backgroundColor: "#ffffff",
            border: "1px solid #ced4da",
            borderRadius: "6px",
            padding: "16px",
            marginBottom: "16px",
            fontSize: "15px",
            color: "red"
          }}>
            {steps[currentStep] || "No steps available."}
          </div>
          <button onClick={handleNext} style={{
            padding: "10px 24px",
            backgroundColor: "#28a745",
            color: "white",
            border: "none",
            borderRadius: "6px",
            cursor: "pointer",
            fontSize: "14px",
          }}>
            {currentStep + 1 >= steps.length ? "Finish ✅" : "Next Step →"}
          </button>
        </div>
      )}
    </div>
  );
};

export default RemediationWorkflow;