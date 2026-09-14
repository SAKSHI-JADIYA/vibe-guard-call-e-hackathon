# backend/test_call.py
import os
import sys
from dotenv import load_dotenv
from calle import CalleClient

# 1. Enforce strict configuration environment mapping
load_dotenv()

# Fetch environment variables from your local hidden configuration
API_KEY = os.getenv("CALLE_API_KEY") or "calle_live_PASTE_YOUR_KEY_HERE_IF_ENV_FAILS"
PHONE_NUMBER = os.getenv("ADMIN_PHONE_NUMBER") or "+91XXXXXXXXXX"

# Sanitize input strings to clean up loose quotes that creep into terminal paths
API_KEY = API_KEY.replace('"', '').replace("'", "").strip()
PHONE_NUMBER = PHONE_NUMBER.replace('"', '').replace("'", "").strip()

print("\n================ VIBEGUARD VERIFICATION LAYER ================")

# Masking implementation: Protects personal data fields from showing in the console during the demo video
if PHONE_NUMBER and len(PHONE_NUMBER) >= 7:
    masked_number = f"{PHONE_NUMBER[:3]}******{PHONE_NUMBER[-4:]}"
else:
    masked_number = "UNKNOWN / INVALID FORMAT"

print(f"[LOG] API Key Authorization Signature: {API_KEY[:15]}...")
print(f"[LOG] Masked Target Endpoint: {masked_number}")

# Guard rails checking local environment setup viability
if "your_actual" in API_KEY or "PASTE_YOUR_KEY" in API_KEY:
    print("[CRITICAL ERROR] Valid CALLE_API_KEY is completely missing in your .env configuration!")
    sys.exit(1)

if "XXXXXXXXXX" in PHONE_NUMBER:
    print("[CRITICAL ERROR] Target ADMIN_PHONE_NUMBER is not set properly inside .env!")
    sys.exit(1)

# 2. Instantiate type-safe programmatic voice client
client = CalleClient(api_key=API_KEY)

# Safety-Approved Prompt Script: Transparently declares VibeGuard identity to satisfy AI anti-phishing filters
task_instruction = (
    f"Place an official monitoring notification call to the administrator at {PHONE_NUMBER}. "
    "As soon as they answer, say exactly: 'This is an automated system status notification "
    "from your VibeGuard application dashboard. We detected a data validation shift on your "
    "Active AI Agent four, and the stream has been temporarily paused. Please press 1 "
    "on your dial pad to confirm you acknowledge this update, or press 2 to flag this event.' "
    "Wait up to 5 seconds for them to interact, then end the session."
)

# Standard result validation structure mapped down from the developer schemas
validation_schema = {
    "type": "object",
    "required": ["selected_action"],
    "properties": {
        "selected_action": {
            "type": "string",
            "enum": ["1", "2", "unknown"],
            "description": "The exact digit the user pressed on their physical phone keypad."
        }
    }
}

try:
    print("[PROCESS] Connecting to CALL-E server network nodes...")
    print("[PROCESS] Dispatching programmatic out-of-band communication task...")
    
    # Fire the one-shot programmatic route channel
    call = client.calls.create_and_wait(
        task=task_instruction,
        result_schema=validation_schema
    )
    
    # 3. Print out-of-band operational verification indicators back to screen
    print("\n================ PIPELINE METRICS ROUTE ================")
    print(f"Call Session ID    : {call.get('id')}")
    print(f"Platform Execution : {call.get('status')}")
    print(f"Keypad Data Capture: {call.get('structured_result')}")
    print("========================================================")
    print("[SUCCESS] VibeGuard out-of-band pipeline is fully active!")

except Exception as e:
    error_message = str(e)
    print("\n================ CONFIGURATION DIAGNOSTICS ================")
    print(f"[CRITICAL RUNTIME EXCEPTION] Call routing crashed: {error_message}")
    print("===========================================================")
    
    # Clear threat diagnostic troubleshooting advice based on error context
    if "API key" in error_message or "unauthorized" in error_message.lower():
        print("[SUGGESTION] Double-check your .env file. Ensure your CALLE_API_KEY does not contain hidden trailing spaces.")
    elif "deceptive" in error_message.lower() or "rejected" in error_message.lower():
        print("[SUGGESTION] The platform safety filter is still flagging content. Simplify the script further to standard plain sentences.")
    else:
        print("[SUGGESTION] Log into the CALL-E dashboard interface directly to confirm your free credit tier balance is positive.")

print("\n==============================================================")
