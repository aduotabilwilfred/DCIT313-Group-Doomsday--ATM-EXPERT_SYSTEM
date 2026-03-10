/**
 * ATM Expert API Service
 * 
 * Handles communication between React frontend and Flask backend.
 * Backend runs on http://localhost:5000
 */

const API_BASE = 'http://localhost:5000/api';

/**
 * Generic fetch wrapper with error handling
 */
async function fetchApi(endpoint, options = {}) {
  try {
    const response = await fetch(`${API_BASE}${endpoint}`, {
      headers: {
        'Content-Type': 'application/json',
        ...options.headers,
      },
      ...options,
    });
    
    const data = await response.json();
    
    if (!response.ok) {
      throw new Error(data.error || `HTTP error ${response.status}`);
    }
    
    return data;
  } catch (error) {
    console.error(`API Error [${endpoint}]:`, error);
    throw error;
  }
}

/**
 * ATM Expert API functions
 */
export const api = {
  /**
   * Health check - verify backend is running
   */
  async healthCheck() {
    return fetchApi('/health');
  },

  /**
   * Run diagnosis based on symptoms and error codes
   * @param {string[]} symptoms - Array of symptom strings
   * @param {string[]} errorCodes - Array of error code strings
   * @param {string} minSeverity - Optional minimum severity filter
   * @returns {Promise<{success: boolean, diagnoses: Array, count: number}>}
   */
  async diagnose(symptoms = [], errorCodes = [], minSeverity = null) {
    const body = {
      symptoms,
      error_codes: errorCodes,
    };
    if (minSeverity) {
      body.min_severity = minSeverity;
    }
    
    return fetchApi('/diagnose', {
      method: 'POST',
      body: JSON.stringify(body),
    });
  },

  /**
   * Get all faults in the knowledge base
   * @param {string} domain - Optional domain filter
   * @returns {Promise<{success: boolean, faults: Array, count: number}>}
   */
  async getAllFaults(domain = null) {
    const endpoint = domain ? `/faults?domain=${encodeURIComponent(domain)}` : '/faults';
    return fetchApi(endpoint);
  },

  /**
   * Get detailed information about a specific fault
   * @param {string} faultId - Fault ID (e.g., "HW_001")
   * @returns {Promise<{success: boolean, fault: Object}>}
   */
  async getFaultDetails(faultId) {
    return fetchApi(`/faults/${encodeURIComponent(faultId)}`);
  },

  /**
   * Get remediation workflow for a fault
   * @param {string} faultId - Fault ID
   * @returns {Promise<{success: boolean, workflow: Object}>}
   */
  async getWorkflow(faultId) {
    return fetchApi(`/workflow/${encodeURIComponent(faultId)}`);
  },

  /**
   * Get plain-language explanation for a diagnosis
   * @param {string} faultId - Fault ID
   * @param {string[]} symptoms - Symptoms that led to diagnosis
   * @param {string[]} errorCodes - Error codes that led to diagnosis
   * @returns {Promise<{success: boolean, explanation: string[]}>}
   */
  async getExplanation(faultId, symptoms = [], errorCodes = []) {
    return fetchApi('/explain', {
      method: 'POST',
      body: JSON.stringify({
        fault_id: faultId,
        symptoms,
        error_codes: errorCodes,
      }),
    });
  },

  /**
   * Get list of all fault domains
   * @returns {Promise<{success: boolean, domains: string[]}>}
   */
  async getDomains() {
    return fetchApi('/domains');
  },
};

export default api;
