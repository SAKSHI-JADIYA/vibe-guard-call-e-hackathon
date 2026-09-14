# frontend/dashboard.py
import streamlit as st
import requests
import hashlib
import json
import time

# Enforce Premium Slate/Dark Cyberpunk Dashboard Theme Configuration
st.set_page_config(
    page_title="AirGap Call • Security Hub",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <style>
    .block-container { padding-top: 2rem; padding-bottom: 2rem; background-color: #0b0f19; }
    h1, h2, h3, h4 { font-family: 'Plus Jakarta Sans', sans-serif; color: #ffffff !important; }
    .stButton>button { width: 100%; border-radius: 8px; font-weight: 600; transition: all 0.2s; }
    .mono-text { font-family: 'JetBrains Mono', monospace; font-size: 0.85rem; }
    div[data-testid="stMetricValue"] { font-size: 1.8rem !important; font-weight: 700 !important; font-family: 'JetBrains Mono', monospace; }
    div.stTextArea textarea { background-color: #05070c !important; color: #cbd5e1 !important; border: 1px solid #1e293b !important; }
    </style>
""", unsafe_allow_html=True)

BACKEND_URL = "http://127.0.0.1:8000"

def calculate_integrity_hash(state_dict: dict) -> str:
    """Generates a SHA-256 cryptographic seal proving data integrity."""
    clean_state = {k: v for k, v in state_dict.items() if k != "attack_logs"}
    serialized_state = json.dumps(clean_state, sort_keys=True)
    return hashlib.sha256(serialized_state.encode('utf-8')).hexdigest()

st.title("🛡️ AirGap Call Admin Command Center")
st.caption("Zero-Latency Inline Prompt Firewall with Out-of-Band Conversational Telephony Containment")
st.markdown("---")

# Telemetry Sync Layer
backend_live = True
try:
    response = requests.get(f"{BACKEND_URL}/incidents", timeout=1)
    state_matrix = response.json()
except Exception:
    backend_live = False
    state_matrix = {"is_frozen": False, "rls_enforced": False, "agent_token_active": True, "attack_logs": []}

col_left, col_right = st.columns(2)

with col_right:
    st.subheader(" Attack Simulation & Macro Controls")
    if not backend_live:
        st.error(" Backend Core Offline. Please launch main.py on Port 8000 first!")

    st.markdown("### 💬 Live AI Agent Prompt Window")
    user_prompt = st.text_area(
        "Enter message to Agent 4:", 
        placeholder="Type something benign or malicious to test the firewall...",
        height=100
    )
    
    if st.button("💬 Send Prompt to Agent", disabled=not backend_live):
        if user_prompt.strip() == "":
            st.warning("Please type a prompt message first.")
        else:
            try:
                st.info(f"Streaming prompt data to /api/chat...")
                res = requests.post(
                    f"{BACKEND_URL}/api/chat", 
                    json={"message": user_prompt, "agent_id": "agent_4"}
                )
                
                # FIX: Catch and format the successful response lists accurately
                if res.status_code == 200:
                    data_payload = res.json()
                    extracted_rows = data_payload.get('data', [])
                    st.success(f"🌐 200 OK Response Received:\n{extracted_rows}")
                elif res.status_code == 423:
                    st.error("🚨 HTTP 423 LOCKED: Anomaly detected! Stream frozen and call triggered.")
                    time.sleep(1)
                    st.rerun()
                elif res.status_code == 401:
                    st.error(" HTTP 401 UNAUTHORIZED: Agent token has been revoked.")
            except Exception as e:
                st.error(f"Network exception: {str(e)}")

    st.markdown("---")

    st.markdown("### ⚡ System Interrupt Macro")
    if st.button("🚨 Trigger Simulation Macro (Error 404/HTTP 423 Test)", type="primary", disabled=not backend_live):
        try:
            st.warning("Firing macro payload to backend root gateway...")
            requests.post(f"{BACKEND_URL}/")
            time.sleep(1.5)
            st.rerun()
        except Exception as e:
            st.error(f"Execution Exception: {str(e)}")

    st.markdown("---")
    
    st.subheader("🔐 Record Cryptographic Chain")
    computed_signature = calculate_integrity_hash(state_matrix)
    if state_matrix["is_frozen"]:
        st.markdown(f"""
            <div style="background-color: rgba(239, 68, 68, 0.1); border: 1px solid rgba(239, 68, 68, 0.2); padding: 12px; border-radius: 8px;">
                <span style="color: #ef4444; font-size: 11px; font-weight: bold; uppercase;">⚠️ INTENT MISMATCH DETECTED</span>
                <p style="color: #cbd5e1; font-size: 11px; margin-top: 4px; font-family: monospace; word-break: break-all;">BLOCK_HASH: {computed_signature}</p>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
            <div style="background-color: rgba(16, 185, 129, 0.1); border: 1px solid rgba(16, 185, 129, 0.2); padding: 12px; border-radius: 8px;">
                <span style="color: #10b981; font-size: 11px; font-weight: bold; uppercase;">💚 POSTURE VALID</span>
                <p style="color: #cbd5e1; font-size: 11px; margin-top: 4px; font-family: monospace; word-break: break-all;">BLOCK_HASH: {computed_signature}</p>
            </div>
        """, unsafe_allow_html=True)

with col_left:
    m_col1, m_col2, m_col3 = st.columns(3)
    if state_matrix["is_frozen"]:
        m_col1.metric("System Posture", "STREAM FROZEN", delta="- HTTP 423 ACTIVE", delta_color="inverse")
        m_col2.metric("Threat Matrix Status", "CRITICAL", delta="INJECTION SHIELDED", delta_color="inverse")
    else:
        m_col1.metric("System Posture", "OPERATIONAL", delta="STREAM OPEN", delta_color="normal")
        m_col2.metric("Threat Matrix Status", "LOW SECURE", delta="SCANNING DATA", delta_color="normal")
        
    if state_matrix["rls_enforced"]:
        m_col3.metric("Remediation State", "RLS ENFORCED", delta="DATABASE SECURED", delta_color="normal")
    elif not state_matrix["agent_token_active"]:
        m_col3.metric("Remediation State", "TOKEN BURNT", delta="AGENT LOCKED OUT", delta_color="inverse")
    else:
        m_col3.metric("Remediation State", "STANDBY", delta="AWAITING TRIAGE", delta_color="off")

    st.markdown("### ⏳ Incident Response & Remediation Timeline")
    if not state_matrix["is_frozen"]:
        st.info("🟢 Monitoring Active: Data pipe is green. Type a malicious payload query on the right workspace to simulate a breach.")
    else:
        st.markdown("####  1. Anomaly Intercepted")
        st.error(" **Exploit Blocked:** Malicious string input pattern caught inline. FastAPI proxy immediately terminated connection returning an explicit `HTTP 423 Locked` status.")
        
        st.markdown("#### 2. Out-of-Band Call Dispatched")
        st.warning(" **Alert Noise Isolation:** System shifted escalation completely off the web lines. Programmatic background thread sent session payload to **CALL-E servers**.")
        
        st.markdown("####  3. Keypad Remediation Response Matrix")
        if state_matrix["rls_enforced"]:
            st.success(" **Resolution Complete (Key 1 Received):** Physical button press tone decoded. System configuration modified: **Database Row-Level Security Enforced** successfully.")
        elif not state_matrix["agent_token_active"]:
            st.success(" **Resolution Complete (Key 2 Received):** Physical button press tone decoded. System configuration modified: **Compromised Agent Authentication Token completely revoked**.")
        else:
            st.info(" **Session Active:** Phone line is open. Awaiting dial pad button interaction values...")

# Dynamic 1-second auto-refresh polling loop engine matching standard specifications
time.sleep(1)
st.rerun()
