# 🛡️ Cyber Analyzer Dashboard

A lightweight, high-performance, and multi-language network discovery and cyber security risk analysis tool. This project combines the speed of **Rust** for low-level socket scanning, the analytical power of **Python** for security vulnerability evaluation, and a modern **TypeScript/HTML/CSS** dashboard for visual representation.

---

## 🚀 Features

* **Fast Core Scanner (Rust):** Leverages native TCP socket connections with strict timeout handles to actively probe common cyber security test ports (21, 22, 23, 25, 53, 80, 443, 8080).
* **Risk Evaluation Engine (Python):** Automatically parses discovered ports and generates critical security risk assessments, potential threat scenarios (e.g., Brute Force, MitM), and mitigation strategies.
* **Minimalist Dashboard (TypeScript/CSS):** A sleek hacker-style dark-mode interface built to visualize scanning statuses and compile live multi-language log outputs.

---

## 🛠️ Project Architecture

```text
cyber-analyzer/
├── core_engine/         # Rust TCP Scanner
│   ├── src/main.rs
│   └── Cargo.toml
├── analyzer/            # Python Risk Assessment Module
│   └── app.py
└── interface/           # TS/HTML/CSS Frontend UI
    ├── index.html
    ├── style.css
    ├── app.ts
    └── app.js


🔧 Installation & Usage
1. Prerequisites
Ensure you have the following packages installed on your Linux ecosystem (Optimized for Kali Linux):

rustc & cargo

python3

typescript (tsc)


2. Running the Core Scanner (Rust)

cd core_engine
cargo run -- 127.0.0.1



3. Running the Analyzer (Python)

cd ..
python3 analyzer/app.py 22,80

4. Compiling and Launching the UI

cd interface
tsc app.ts
firefox index.html



📜 Mitigation & Security Insights Built-in
Port 22 (SSH): Critical risk mitigation advice regarding Brute Force vectors and SSH key management.

Port 80/8080 (HTTP): High-level mitigation plans addressing unencrypted traffic and cleartext data transmission risks (MitM).

Port 21 (FTP): Insights into anonymous login exploits and secure SFTP alternatives.

Developed as a minimalist, modular, and high-performance digital footprint security asset.
