# 🛡️ Log Sentinel (Log Parser Engine)

> A high-performance, object-oriented log parsing engine written in Python, designed to analyze security logs with algorithmic efficiency.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active_Development-orange)

## 📖 Overview

**Log Sentinel** is a modular framework for parsing raw server logs (like Linux `auth.log`). Unlike simple regex scripts, this project uses **Abstract Base Classes (ABC)** to enforce a strict contract for log processing, ensuring scalability and type safety.

## 🚀 Key Features

* **OOP Architecture:** Implements the *Template Method Pattern* using Python's `abc` module.
* **Polymorphic Design:** Easily extensible. Create a new class (e.g., `NginxLogEntry`), define the regex patterns, and the engine handles the rest.
* **Algorithmic Optimization:** Uses direct group index access instead of linear iteration, significantly reducing parsing time for complex logs.
* **Security Focused:** Originally designed to detect unauthorized access attempts (SSH brute force) in `auth.log`.

## 🛠️ Architecture

The project is built on a parent-child hierarchy:

1. **`LogEntry` (Abstract Base Class):** The engine. It defines the logic for parsing, validating, and storing data. It enforces the implementation of regex patterns using `@abstractmethod`.
2. **`AuthLogEntry` (Concrete Class):** The implementation. It provides the specific Regex patterns to extract User, IP, Port, and Status from Linux authentication logs.

## 💻 Installation

Clone the repository:

```bash
git clone [https://github.com/yaelcalleja/Log-Sentinel.git](https://github.com/yaelcalleja/Log-Sentinel.git)
cd log-sentinel

No external dependencies are required. This project uses the standard Python library (re, abc).

## ⚙️ Usage

```Python

from src.auth_log import AuthLogEntry

# Example raw line from /var/log/auth.log
raw_line = "Dec 10 06:55:01 my-server sshd[12345]: Failed password for invalid user admin from 192.168.1.50 port 4040 ssh2"

try:
    # The engine automatically parses the line upon instantiation
    log = AuthLogEntry(raw_line)
    
    # Access parsed data cleanly
    print(f"Target User: {log.get_value('_User')}")  # Output: admin
    print(f"Attacker IP: {log.get_value('_Ip')}")    # Output: 192.168.1.50
    print(f"Port:        {log.get_value('_Port')}")  # Output: 4040

except Exception as e:
    print(f"Error parsing log: {e}")

## 🗺️ Roadmap

    [x] Implement Abstract Base Class structure.

    [x] Optimize Regex engine to O(1) access.

    [ ] Add JsonLogEntry for CloudTrail logs (AWS).

    [ ] Implement specific "Intruder Detection" logic.

    [ ] Export report to CSV/JSON.

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements.
---
Developed by Yael Reveles[badger] as part of the Winter Arc DevSecOps Roadmap.
