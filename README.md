# Password Cracking & Credential Attack Suite

![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-Educational-green.svg)
![Status](https://img.shields.io/badge/status-Active-success.svg)

## Project Overview

A comprehensive educational toolkit for password policy testing and credential security assessment.  
This project demonstrates how password cracking workflows operate, how credentials are stored on systems, and how security teams evaluate and strengthen authentication mechanisms.

**Ethical Use Only**  
This tool is intended strictly for educational purposes and authorized security testing. Unauthorized access to computer systems is illegal.

---

## Features

- **Dictionary Generator** – Create custom wordlists using mutations and patterns  
- **Hash Extraction** – Extract password hashes from Linux and Windows systems  
- **Brute-Force Simulator** – Simulate password attacks to test credential strength  
- **Password Analyzer** – Evaluate complexity, entropy, and common weaknesses  
- **Report Generator** – Produce structured security assessment reports  

---

## Quick Start

### Prerequisites

```bash
python3 --version
pip install -r requirements.txt

Installation

git clone https://github.com/yourusername/password-cracking-suite.git
cd password-cracking-suite
python3 main.py

Basic Usage

# Interactive mode
python3 main.py

# Dictionary generation only
python3 -m dictionary_generator.generator

# Demo mode with sample data
python3 main.py --demo


---

Project Structure

password-cracking-suite/
├── main.py
├── config.py
├── requirements.txt
├── README.md
├── LICENSE
│
├── dictionary_generator/
│   ├── generator.py
│   └── patterns.py
│
├── hash_extraction/
│   ├── linux_extractor.py
│   └── windows_extractor.py
│
├── brute_force/
│   ├── simulator.py
│   └── hash_cracker.py
│
├── strength_analyzer/
│   ├── analyzer.py
│   └── entropy.py
│
├── reports/
│   └── generator.py
│
├── samples/
│   ├── sample_hashes.txt
│   ├── sample_passwords.txt
│   └── test_shadow.txt
│
└── output/
    ├── wordlists/
    ├── cracked/
    └── reports/


---

Usage Examples

Dictionary Generation

from dictionary_generator.generator import DictionaryGenerator

gen = DictionaryGenerator()
config = {
    "base_words": ["admin", "password", "company"],
    "use_dates": True,
    "start_year": 2020,
    "end_year": 2024,
    "mutations": {
        "leetspeak": True,
        "uppercase": True,
        "numbers": True,
        "special": True
    }
}

gen.generate_dictionary(config)
gen.save_to_file("output/wordlists/custom.txt")

Hash Extraction (Linux)

from hash_extraction.linux_extractor import LinuxHashExtractor

extractor = LinuxHashExtractor()
extractor.extract_from_shadow("/tmp/shadow")
extractor.save_hashes("output/extracted_hashes.txt")

Attack Simulation

from brute_force.simulator import AttackSimulator

simulator = AttackSimulator()
results = simulator.dictionary_attack(
    hash_file="output/extracted_hashes.txt",
    wordlist="output/wordlists/custom.txt"
)

Password Strength Analysis

from strength_analyzer.analyzer import PasswordAnalyzer

analyzer = PasswordAnalyzer()
result = analyzer.analyze_password("P@ssw0rd123")
print(result)


---

Configuration

Edit config.py to modify default behavior:

DEFAULT_START_YEAR = 1990
DEFAULT_END_YEAR = 2024
MAX_WORDLIST_SIZE = 100000

MAX_PASSWORD_LENGTH = 12
TIMEOUT_SECONDS = 3600

OUTPUT_DIR = "./output"
LOG_LEVEL = "INFO"


---

Learning Objectives

This project focuses on:

Understanding how password hashes are stored and attacked

Common credential attack methodologies

Password entropy and strength evaluation

Practical red-team and blue-team considerations

Security policy validation and reporting



---

Legal and Ethical Guidelines

Permitted Uses

Educational learning and research

Authorized security testing with written permission

Password policy evaluation

Defensive security training


Prohibited Uses

Unauthorized system access

Testing without explicit permission

Malicious or criminal activity

Distribution of compromised credentials


Users are responsible for complying with all applicable laws and regulations.


---

Development Notes

This project was built using AI-assisted tooling to accelerate implementation.
The primary objective is to demonstrate understanding of credential attack workflows, tooling integration, and security analysis—not custom cryptographic engineering.


---

Known Limitations

Hash extraction requires elevated privileges

Large wordlists can consume significant memory

Brute-force simulations are computationally intensive



---

Roadmap

GPU-based cracking integration

Hashcat and John the Ripper integration

Multi-threaded processing

Improved reporting formats

Web-based interface



---

License

This project is licensed for Educational Use Only.
See the LICENSE file for details.


---

Contact

Author: Mayank Naithani
Email: mynkq7@gmail.com
GitHub: https://github.com/mynkq7
Project: https://github.com/mynkq7/Password-cracking-credential-attack-suite