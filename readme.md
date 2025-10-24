# Low-Interaction Honeypot for Intrusion Detection

This project implements a low-interaction honeypot that simulates SSH and HTTP services to collect malicious traffic. The captured traffic is analyzed to identify common attack patterns.

## Features
- Listens on SSH (22) and HTTP (80) ports.
- Logs incoming connection attempts with timestamps, IPs, and ports.
- Analyzes logs to identify top attacking IPs and ports.
- Generates an Excel report with attack metrics.

## Tools & Libraries
- Python 3.x
- `socket`, `threading`
- `pandas` for analysis
- `openpyxl` for Excel export
- Wireshark (optional) for packet-level analysis

## Setup & Usage
1. Clone the repo:
```bash
git clone <repo-url>
cd honeypot

2.
pip install -r requirements.txt

3.
python honeypot.py

4.
nmap -sS -p22,80 <honeypot-ip>

5.
python analyze_logs.py
