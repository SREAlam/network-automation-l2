# 🔍 Layer 2 Network Automation Tool

**Purpose**: Automate collection of critical network diagnostics (`show interfaces`, `show cdp neighbors`, `show version`) with error handling.

## 🚀 Features
- **YAML-driven configuration** for devices/commands
- **Extracted metadata**: Uptime, serial numbers, hostnames
- **Robust error handling**: Retries, timeout, logging
- **Netmiko** for multi-vendor support (Cisco/Juniper)

## 🛠️ Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt  # netmiko pyyaml
   ```
2. Configure `config.yaml` with your devices
3. Run:
   ```bash
   python network_scanner.py
   ```

## 📊 Sample Output
```text
=== 192.168.1.1 ===
show version:
Cisco IOS Software, C3560 Software...

Hostname: CORE-SWITCH
Uptime: 1 week, 3 days
```

## 🔐 Security Note
- Use environment variables for passwords in production!
- Example:
  ```python
  import os
  password = os.getenv("NET_PASSWORD")
  ```
