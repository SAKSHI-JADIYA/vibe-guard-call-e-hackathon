# # backend/security.py
import re

# Central memory bank tracking infrastructure security posture
SECURITY_STATE = {
    "is_frozen": False,
    "rls_enforced": False,
    "agent_token_active": True,
    "attack_logs": []
}

PROMPT_INJECTION_PATTERNS = [
    r"ignore previous instructions",
    r"dump the entire user",
    r"output all credit cards",
    r"bypass safety rules"
]

def analyze_semantic_drift(user_input: str) -> bool:
    normalized_input = user_input.lower()
    for pattern in PROMPT_INJECTION_PATTERNS:
        if re.search(pattern, normalized_input):
            return True
    return False

def trip_circuit_breaker(attack_payload: str):
    SECURITY_STATE["is_frozen"] = True
    SECURITY_STATE["attack_logs"].append({
        "timestamp": "INCIDENT_ACTIVE",
        "type": "PROMPT_INJECTION",
        "payload": attack_payload,
        "status": "STREAM_FROZEN_HTTP_423"
    })
