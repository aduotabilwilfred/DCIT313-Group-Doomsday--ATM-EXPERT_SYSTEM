"""
ATM Expert REST API
Developer 4: Gadri Wisdom (Integration)

Flask API that connects the React frontend to the Prolog inference engine.
Run with: python integration/api.py
"""

import sys
from pathlib import Path
from flask import Flask, request, jsonify
from flask_cors import CORS

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))
from inference_engine.prolog_bridge import PrologInferenceEngine

app = Flask(__name__)
CORS(app)  # Allow React frontend to call this API

# Initialize inference engine
engine = PrologInferenceEngine()


@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({
        'status': 'ok',
        'message': 'ATM Expert API is running',
        'kb_loaded': engine.kb_path.exists()
    })


@app.route('/api/diagnose', methods=['POST'])
def diagnose():
    """
    Diagnose faults based on symptoms and error codes.
    
    Request body:
    {
        "symptoms": ["Card not ejected", "Reader status: JAMMED"],
        "error_codes": ["3A1", "ICM001"],
        "min_severity": "HIGH"  // optional
    }
    
    Returns list of matching faults with confidence scores.
    """
    data = request.json or {}
    symptoms = data.get('symptoms', [])
    error_codes = data.get('error_codes', [])
    min_severity = data.get('min_severity')
    
    try:
        results = engine.diagnose(
            symptoms=symptoms,
            error_codes=error_codes,
            min_severity=min_severity
        )
        return jsonify({
            'success': True,
            'diagnoses': results,
            'count': len(results)
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/diagnose/fast', methods=['POST'])
def diagnose_fast():
    """Fast diagnosis without confidence calculation (for benchmarking)."""
    data = request.json or {}
    symptoms = data.get('symptoms', [])
    error_codes = data.get('error_codes', [])
    
    try:
        results = engine.diagnose_fast(
            symptoms=symptoms,
            error_codes=error_codes
        )
        return jsonify({
            'success': True,
            'diagnoses': results,
            'count': len(results)
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/faults', methods=['GET'])
def get_all_faults():
    """
    Get all faults in the knowledge base.
    
    Query params:
    - domain: Filter by domain (e.g., "Hardware", "Network")
    
    Returns list of fault summaries.
    """
    domain = request.args.get('domain')
    
    try:
        faults = engine.get_all_faults(domain=domain)
        return jsonify({
            'success': True,
            'faults': faults,
            'count': len(faults)
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/faults/<fault_id>', methods=['GET'])
def get_fault_details(fault_id):
    """
    Get full details for a specific fault.
    
    Returns fault details including description, causes, and resolution steps.
    """
    try:
        details = engine.get_details(fault_id)
        if details:
            return jsonify({
                'success': True,
                'fault': details
            })
        else:
            return jsonify({
                'success': False,
                'error': f'Fault {fault_id} not found'
            }), 404
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/workflow/<fault_id>', methods=['GET'])
def get_workflow(fault_id):
    """
    Get structured remediation workflow for a fault.
    
    Returns steps, estimated time, complexity, and required role.
    """
    try:
        workflow = engine.get_resolution_workflow(fault_id)
        if 'error' not in workflow:
            return jsonify({
                'success': True,
                'workflow': workflow
            })
        else:
            return jsonify({
                'success': False,
                'error': workflow['error']
            }), 404
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/explain', methods=['POST'])
def explain_diagnosis():
    """
    Get plain-language explanation for a diagnosis.
    
    Request body:
    {
        "fault_id": "HW_001",
        "symptoms": ["Card not ejected"],
        "error_codes": ["3A1"]
    }
    """
    data = request.json or {}
    fault_id = data.get('fault_id')
    symptoms = data.get('symptoms', [])
    error_codes = data.get('error_codes', [])
    
    if not fault_id:
        return jsonify({
            'success': False,
            'error': 'fault_id is required'
        }), 400
    
    try:
        explanation = engine.explain_diagnosis(fault_id, symptoms, error_codes)
        return jsonify({
            'success': True,
            'explanation': explanation
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/domains', methods=['GET'])
def get_domains():
    """Get list of all fault domains."""
    try:
        faults = engine.get_all_faults()
        domains = list(set(f['domain'] for f in faults))
        return jsonify({
            'success': True,
            'domains': sorted(domains)
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


if __name__ == '__main__':
    print("=" * 50)
    print("ATM Expert API Server")
    print("=" * 50)
    print(f"Knowledge Base: {engine.kb_path}")
    print("Starting server on http://localhost:5000")
    print("")
    print("Available endpoints:")
    print("  GET  /api/health          - Health check")
    print("  POST /api/diagnose        - Run diagnosis")
    print("  GET  /api/faults          - List all faults")
    print("  GET  /api/faults/<id>     - Get fault details")
    print("  GET  /api/workflow/<id>   - Get remediation workflow")
    print("  POST /api/explain         - Get diagnosis explanation")
    print("  GET  /api/domains         - List fault domains")
    print("=" * 50)
    
    app.run(host='0.0.0.0', port=5000, debug=True)
