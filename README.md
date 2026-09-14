# 🛡️ AirGap Call

An out-of-band proxy firewall and multi-threaded circuit breaker designed to isolate compromised LLM applications and execute infrastructure triage over standard cellular telephony lines.

---

## 💡 Inspiration
As AI agents gain direct access to enterprise infrastructures via tools and function-calling, prompt text essentially becomes executable code. This opens up a catastrophic structural security void:
* **The Exploit:** The **OWASP Top 10 for LLMs** ranks Prompt Injection (LLM01) as the #1 active threat vector. Attackers can easily trick AI agents into running unauthorized backend commands to drain data.
* **The Detection Void:** The **IBM Cost of a Data Breach Report** reveals that organizations take an average of **over 200 days to detect a breach**. For an autonomous agent, an entire corporate database can be exfiltrated in seconds.
* **Alert Fatigue:** **Gartner** research highlights that **62% of critical security alerts are missed** or ignored because they are buried inside noisy digital communication channels like Slack or email. 

We built **AirGap Call** because passive monitoring dashboard panels and easy-to-mute browser pop-ups cannot contain a machine-speed breach. DevSecOps teams require an immediate, un-ignorable, and human-verified defense circuit breaker.

---

## 🚀 What It Does
AirGap Call acts as an inline proxy firewall for AI applications. The split-second it detects a prompt injection attack or an unauthorized semantic drift attempt, it instantly freezes the active connection data pipe (`HTTP 423 Locked`), completely cutting off the attacker mid-stream.

Simultaneously, the engine bypasses digital noise entirely. An isolated backend thread dispatches a physical phone call straight to the administrator's mobile device via the **CALL-E Goal API**. 

To clear telephony anti-fraud filters, a synthetic voice reads a transparent, safety-approved status notification script clearly identifying the application domain and the active breach status. The administrator handles triage directly from their phone's keypad:
* **Pressing 1:** Mutates memory variables to instantly enforce **Database Row-Level Security (RLS)** filters to safeguard isolated data pools.
* **Pressing 2:** Executes an immediate credential teardown, **completely revoking the compromised AI agent's authentication token** to permanently lock the attacker out of the grid.

---

## 🛠️ How We Built It
We engineered a production-grade, concurrent prototype built for data integrity and low-latency network performance:
* **FastAPI Middleware Security Core:** Built a low-latency proxy app handler that screens inbound prompt text streams, tracks semantic anomalies, and enforces the strict `HTTP 423` stream-freeze state machine.
* **CALL-E SDK Drivers:** Programmed structured conversational and digit-extraction task scripts that pass identity verification checks natively without tripping carrier anti-fraud filters.
* **Streamlit Control Panel Dashboard:** Engineered a sleek dark cyberpunk administrative console that performs high-frequency loop polling to sync backend variable state changes in near-real-time.
* **SHA-256 Cryptographic Chain:** Implemented a built-in cryptographic hashing loop that continuously seals the log parameters, providing a tamper-evident audit trail for forensics teams.
* **Multi-Threaded Concurrency Engine:** Configured isolated Python executors (`run_in_executor`) to keep heavy, blocking telephony network operations completely separated from the web framework layer, preventing application stalls.

---

## ⚡ Challenges We Ran Into
* **Asynchronous Thread Stalls:** Bridging asynchronous API web streams with an external synchronous telephony channel inside background tasks originally caused network timeout blocks, halting the call. We resolved this by stripping away standard blocking wait scripts, re-architecting handlers using asynchronous `asyncio` loops, and forcing the CALL-E communication logic to run inside an isolated thread executor pool.
* **Telephony Phishing Restrictions:** Passing raw "panic-inducing" terminal keywords like *"Malicious payload intercept"* caused CALL-E's built-in real-time safety guardrails to auto-reject the request to prevent vishing fraud. We resolved this by drafting a transparent, non-deceptive alert script that clearly declares the platform's identity (**AirGap Call**) and intent up front, clearing the validation gates cleanly.

---

## 🏆 Accomplishments That We're Proud Of
* **True Out-of-Band Containment:** Successfully bridged physical telecommunication routing networks with automated edge computing security policies.
* **Tamper-Evident Seals:** Successfully integrated an live hashing loop that proves data ledger integrity on a 1-second auto-refresh scale.
* **Zero-Downtime Triage:** Proved that organizations can isolate compromised AI modules and revoke credentials mid-attack without causing a full system crash or forcing total network downtime.

---

## 🧠 What We Learned
* **The Power of Physical Friction:** Shifting critical alerts out of the browser changes response rates. A ringing phone on a desk commands immediate operational focus.
* **Asynchronous Architecture is Mandatory:** When an enterprise app relies on real-time external network APIs, strict multi-threaded separation is an absolute system requirement, not an optional optimization.

---

## 🔮 What's Next for AirGap Call
* **Edge Routing Migration:** Move the FastAPI proxy middleware logic to globally distributed edge workers (like Cloudflare Workers) to minimize intercept latency down to microseconds.
* **Dynamic Embedding Thresholds:** Implement lightweight local vector embeddings to calculate multi-dimensional semantic drift dynamically rather than relying on fixed regular expression classification maps.
* **Multi-Admin Escalation Trees:** Build an automated failover routing system so that if the primary administrator misses the CALL-E security phone call, it automatically dials alternative members of the DevOps team in order of priority.
