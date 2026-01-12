# Password Cracking & Credential Attack Suite

![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-Educational-green.svg)
![Status](https://img.shields.io/badge/status-Active-success.svg)

## Project Overview

A comprehensive educational toolkit for password policy testing and credential security assessment. This project demonstrates how password cracking works, how credentials are stored, and how security teams can reinforce authentication mechanisms.

**WARNING: ETHICAL USE ONLY** - This tool is designed for educational purposes and authorized security testing. Unauthorized access to computer systems is illegal.

## Development Notes

This project was built using AI-assisted tooling to accelerate implementation. The primary objective is to demonstrate understanding of credential attack workflows, tooling integration, and security analysis—not custom cryptographic engineering.

## Features

- Custom dictionary generation with mutations and patterns
- Hash extraction from Linux/Windows systems
- Brute-force simulation for password testing
- Password strength analysis with complexity evaluation
- Comprehensive security audit report generation

## Quick Start

### Prerequisites
```bash
# Python 3.8 or higher required
python3 --version

# Install dependencies
pip install -r requirements.txt
```

### Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/password-cracking-suite.git
cd password-cracking-suite

# Run the application
python3 main.py
```

### Basic Usage
```bash
# Interactive mode
python3 main.py

# Generate dictionary only
python3 -m dictionary_generator.generator

# Quick test with sample data
python3 main.py --demo
```

## Project Structure
```
password-cracking-suite/
├── main.py                      # Main application entry point
├── config.py                    # Configuration management
├── requirements.txt             # Python dependencies
├── README.md                    # This file
├── LICENSE                      # License information
│
├── dictionary_generator/        # Dictionary generation module
│   ├── __init__.py
│   ├── generator.py            # Core dictionary generator
│   └── patterns.py             # Pattern definitions
│
├── hash_extraction/             # Hash extraction module
│   ├── __init__.py
│   ├── linux_extractor.py      # Linux shadow file extraction
│   └── windows_extractor.py    # Windows SAM extraction
│
├── brute_force/                 # Brute-force simulation module
│   ├── __init__.py
│   ├── simulator.py            # Attack simulator
│   └── hash_cracker.py         # Hash cracking logic
│
├── strength_analyzer/           # Password strength analysis
│   ├── __init__.py
│   ├── analyzer.py             # Strength analyzer
│   └── entropy.py              # Entropy calculator
│
├── reports/                     # Report generation
│   ├── __init__.py
│   └── generator.py            # Report generator
│
├── samples/                     # Sample files for testing
│   ├── sample_hashes.txt
│   ├── sample_passwords.txt
│   └── test_shadow.txt
│
└── output/                      # Generated outputs
    ├── wordlists/
    ├── cracked/
    └── reports/
```

## Usage Examples

### 1. Generate Custom Dictionary
```python
from dictionary_generator.generator import DictionaryGenerator

gen = DictionaryGenerator()
config = {
    'base_words': ['admin', 'password', 'company'],
    'use_dates': True,
    'start_year': 2020,
    'end_year': 2024,
    'mutations': {
        'leetspeak': True,
        'uppercase': True,
        'numbers': True,
        'special': True
    }
}
gen.generate_dictionary(config)
gen.save_to_file('output/wordlists/custom.txt')
```

### 2. Extract Password Hashes
```python
from hash_extraction.linux_extractor import LinuxHashExtractor

extractor = LinuxHashExtractor()
hashes = extractor.extract_from_shadow('/tmp/shadow')
extractor.save_hashes('output/extracted_hashes.txt')
```

### 3. Run Attack Simulation
```python
from brute_force.simulator import AttackSimulator

simulator = AttackSimulator()
results = simulator.dictionary_attack(
    hash_file='output/extracted_hashes.txt',
    wordlist='output/wordlists/custom.txt'
)
```

### 4. Analyze Password Strength
```python
from strength_analyzer.analyzer import PasswordAnalyzer

analyzer = PasswordAnalyzer()
result = analyzer.analyze_password('P@ssw0rd123')
print(f"Strength: {result['strength']}")
print(f"Entropy: {result['entropy']} bits")
```

## Configuration

Edit `config.py` to customize default settings:
```python
# Dictionary generation settings
DEFAULT_START_YEAR = 1990
DEFAULT_END_YEAR = 2024
MAX_WORDLIST_SIZE = 100000

# Brute-force settings
MAX_PASSWORD_LENGTH = 12
TIMEOUT_SECONDS = 3600

# Output settings
OUTPUT_DIR = './output'
LOG_LEVEL = 'INFO'
```

## Example Output

### Dictionary Generation
```
[+] Dictionary Generation Started
[+] Adding 3 base words...
[+] Generating date combinations (2020-2024)...
    Generated 180 date combinations
[+] Applying leet-speak mutations...
    Generated 45 leet variants
[+] Total words generated: 1,247
[+] Saved to: output/wordlists/custom.txt
```

### Attack Simulation
```
[+] Starting dictionary attack...
[+] Testing 1,247 passwords against 5 hashes...
[+] Cracked: user1:password123 (0.3s)
[+] Cracked: user2:admin2024 (1.2s)
[!] Not cracked: user3 (strong password)
[+] Success rate: 40% (2/5)
```

### Password Analysis
```
Password: P@ssw0rd123
├─ Length: 11 characters
├─ Complexity: Medium
├─ Entropy: 52.4 bits
├─ Dictionary: Contains common word
└─ Recommendation: Add more entropy, avoid dictionary words
```

## Learning Objectives

This project teaches:
- How password hashes are stored and protected
- Common password cracking methodologies
- Password strength evaluation techniques
- Security policy implementation
- Red team vs blue team perspectives

## Legal and Ethical Guidelines

### Permitted Uses
- Educational learning and research
- Authorized security testing with written permission
- Personal password strength assessment
- Security policy development and testing

### Prohibited Uses
- Unauthorized access to any computer system
- Testing systems without explicit permission
- Malicious activities or criminal intent
- Distribution of cracked credentials

**Important**: Unauthorized computer access is illegal under laws like the Computer Fraud and Abuse Act (CFAA) in the US and similar laws worldwide.

## Development

### Running Tests
```bash
python3 -m pytest tests/
```

### Code Style
```bash
# Format code
black .

# Lint code
pylint *.py
```

### Contributing
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Documentation

- **Full Documentation**: See [docs/](docs/) folder
- **API Reference**: See [docs/api.md](docs/api.md)
- **Tutorials**: See [docs/tutorials/](docs/tutorials/)

## Known Issues

- Hash extraction requires root/admin privileges
- Large wordlists may require significant memory
- Brute-force attacks are computationally intensive

## Roadmap

- GPU acceleration for hash cracking
- Web interface for remote access
- Database storage for results
- Integration with John the Ripper/Hashcat
- Real-time progress monitoring
- Multi-threaded processing

## Acknowledgments

- Inspired by industry-standard tools like John the Ripper and Hashcat
- Built for educational purposes in cybersecurity training
- Thanks to the security research community

## License

This project is licensed for **Educational Use Only**. See [LICENSE](LICENSE) file for details.

**Disclaimer**: The authors are not responsible for any misuse of this tool. Users are solely responsible for ensuring their usage complies with applicable laws and regulations.

## Contact

- **Author**: Your Name
- **Email**: your.email@example.com
- **GitHub**: [@yourusername](https://github.com/yourusername)
- **Project Link**: [https://github.com/yourusername/password-cracking-suite](https://github.com/yourusername/password-cracking-suite)

---

**Built for cybersecurity education**
