# # backend/main.py
import time
import threading
import uvicorn
from dotenv import load_dotenv

load_dotenv()

def run_web_server_thread():
    """Launches the guard service engine isolated inside its own thread."""
    print("[THREAD] Launching isolated ASGI Web Server Application...")
    # Changed log_level to "warning" to prevent clean standard HTTP lines from cluttering your dramatic judges console output
    uvicorn.run("guard_service:app", host="127.0.0.1", port=8000, log_level="warning")

def run_wake_word_telemetry_loop():
    """
    Simulates your ongoing background system wake-word tracking loop.
    Runs concurrently with the web server without causing processing locks.
    """
    print("[THREAD] Starting background wake-word system diagnostics...")
    loop_count = 0
    while True:
        loop_count += 1
        # Periodically prints status indicators to confirm execution pathways are open
        if loop_count % 10 == 0:
            print("[DIAGNOSTIC LOG] Background wake-word listening loop active and green...")
        time.sleep(1)

if __name__ == "__main__":
    print("=================== INITIALIZING VIBEGUARD CORE ===================")
    
    server_thread = threading.Thread(target=run_web_server_thread, daemon=True)
    server_thread.start()
    
    # Give the network socket a brief window to capture binding access paths safely
    time.sleep(2)
    
    try:
        run_wake_word_telemetry_loop()
    except KeyboardInterrupt:
        print("\n[SHUTDOWN] Exiting VibeGuard processing loops cleanly.")
