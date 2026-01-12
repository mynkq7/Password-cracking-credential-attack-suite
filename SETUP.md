# Setup and Usage Guide

## 🚀 Quick Start

### 1. Clone or Download

```bash
# If using git
git clone <your-repo-url>
cd password-cracking-suite

# Or download and extract the ZIP file
```

### 2. Verify Python

```bash
# Check Python version (3.8+ required)
python3 --version

# Should output: Python 3.8.x or higher
```

### 3. Install Dependencies

```bash
# Currently uses only standard library
# Future: pip install -r requirements.txt
```

### 4. Run the Application

```bash
# Interactive mode
python3 main.py

# Quick demo
python3 main.py --demo
```

## 📋 Detailed Setup Instructions

### For Windows Users

1. **Install Python**
   - Download from: https://www.python.org/downloads/
   - During installation, CHECK "Add Python to PATH"
   - Verify: Open CMD and type `python --version`

2. **Extract the Project**
   - Extract ZIP to: `C:\Projects\password-cracking-suite`

3. **Run**
   ```cmd
   cd C:\Projects\password-cracking-suite
   python main.py
   ```

### For Linux/Mac Users

1. **Python is usually pre-installed**
   ```bash
   python3 --version
   ```

2. **Make scripts executable** (optional)
   ```bash
   chmod +x main.py
   chmod +x dictionary_generator/generator.py
   ```

3. **Run**
   ```bash
   ./main.py
   # or
   python3 main.py
   ```

### For VS Code Users

1. **Open Folder**
   - File → Open Folder
   - Select `password-cracking-suite`

2. **Set Python Interpreter**
   - Ctrl+Shift+P (Cmd+Shift+P on Mac)
   - Type: "Python: Select Interpreter"
   - Choose Python 3.8+

3. **Run**
   - Open `main.py`
   - Press F5 or click Run button
   - Or use integrated terminal: `python3 main.py`

## 🎯 Usage Examples

### Example 1: Generate Simple Dictionary

```bash
# Run main.py
python3 main.py

# Select: 1 (Generate Custom Dictionary)

# Enter when prompted:
Base words: admin,password,company
Use dates: n
Common passwords: y
Keyboard patterns: n
Leet-speak: y
Uppercase: y
Numbers: y
Special chars: y
Output file: [press Enter for default]
Max words: 1000

# Result: Creates wordlist with ~1000 variations
```

### Example 2: Quick Generation

```bash
# Run with demo mode
python3 main.py --demo

# Automatically creates wordlist with default settings
# Output: output/wordlists/quick_wordlist.txt
```

### Example 3: Company Security Audit

```bash
python3 main.py

# Select: 1

# Configuration:
Base words: acmecorp,acme,employee,dept,2024
Use dates: y
  Start year: 2020
  End year: 2024
Common passwords: y
Keyboard patterns: y
Enable all mutations: y
Max words: 50000

# Creates comprehensive wordlist for Acme Corp audit
```

### Example 4: Using Username File

```bash
# Create username file
echo "john.smith
jane.doe
admin" > users.txt

# Run main.py
python3 main.py

# Select: 1

# When prompted for username file:
Username file: users.txt

# Generator will create variations:
# john.smith, john.smith123, johnsmith, etc.
```

### Example 5: Programmatic Usage

```python
#!/usr/bin/env python3
# my_generator.py

from dictionary_generator.generator import DictionaryGenerator

# Create generator
gen = DictionaryGenerator()

# Configure
config = {
    'base_words': ['mycompany', 'secure', 'access'],
    'use_dates': True,
    'start_year': 2022,
    'end_year': 2024,
    'use_common': True,
    'use_keyboard': False,
    'mutations': {
        'leetspeak': True,
        'uppercase': True,
        'numbers': True,
        'special': True
    },
    'output_file': 'my_custom_wordlist.txt',
    'max_words': 5000
}

# Generate
count = gen.generate_dictionary(config)
print(f"Generated {count} passwords")

# Save
gen.save_to_file(config['output_file'], config['max_words'])
```

Then run:
```bash
python3 my_generator.py
```

## 🔧 Configuration

### config.py Settings

Edit `config.py` to customize defaults:

```python
# Default year range
DEFAULT_START_YEAR = 1990  # Change to 2000
DEFAULT_END_YEAR = 2024    # Change to 2025

# Max wordlist size
MAX_WORDLIST_SIZE = 100000  # Change to 50000

# Output directory
OUTPUT_DIR = Path('./output')  # Change path
```

### Environment-Specific Settings

**For Testing:**
```python
MAX_WORDLIST_SIZE = 1000
MAX_PASSWORD_LENGTH = 8
USE_MULTIPROCESSING = False
```

**For Production:**
```python
MAX_WORDLIST_SIZE = 100000
MAX_PASSWORD_LENGTH = 12
USE_MULTIPROCESSING = True
MAX_WORKERS = 8
```

## 📁 Project Structure

```
password-cracking-suite/
│
├── main.py                  ← Start here!
├── config.py                ← Configuration settings
├── README.md                ← Project overview
├── SETUP.md                 ← This file
├── LICENSE                  ← Legal information
├── requirements.txt         ← Dependencies
├── .gitignore              ← Git ignore rules
│
├── dictionary_generator/    ← Dictionary module
│   ├── __init__.py
│   ├── generator.py        ← Main generator
│   └── patterns.py         ← Pattern generation
│
├── hash_extraction/         ← Hash extraction (future)
│   └── __init__.py
│
├── brute_force/            ← Attack simulation (future)
│   └── __init__.py
│
├── strength_analyzer/       ← Password analysis (future)
│   └── __init__.py
│
├── reports/                 ← Report generation (future)
│   └── __init__.py
│
├── samples/                 ← Test files
│   ├── README.txt
│   ├── sample_passwords.txt
│   ├── sample_hashes.txt
│   └── test_usernames.txt
│
└── output/                  ← Generated files
    ├── wordlists/          ← Dictionary output
    ├── cracked/            ← Cracked passwords
    ├── reports/            ← Security reports
    └── logs/               ← Application logs
```

## 🐛 Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'config'"

**Solution:**
```bash
# Make sure you're in the project root
cd password-cracking-suite
pwd  # Should end with /password-cracking-suite

# Run from project root
python3 main.py
```

### Issue: "Permission denied"

**Solution (Linux/Mac):**
```bash
chmod +x main.py
chmod +x dictionary_generator/generator.py
```

**Solution (Windows):**
- Run as Administrator
- Or use: `python main.py` instead of `./main.py`

### Issue: "Python not found"

**Solution:**
```bash
# Windows: Use 'python' instead of 'python3'
python main.py

# Linux/Mac: Install Python 3.8+
sudo apt install python3  # Ubuntu/Debian
brew install python3       # Mac
```

### Issue: Empty or small wordlist

**Cause:** Not enough base words or mutations disabled

**Solution:**
- Provide more base words
- Enable all mutations
- Increase date range
- Enable common passwords and keyboard patterns

### Issue: "File not found" error

**Solution:**
```bash
# Check your current directory
pwd

# Ensure output directories exist
python3 -c "import config"

# This will create output directories automatically
```

## 📊 Understanding Output

### Wordlist Format

```
password
password1
password123
password2024
p@ssw0rd
P@ssw0rd
PASSWORD
...
```

- One password per line
- Sorted by length, then alphabetically
- All unique (no duplicates)

### Statistics Output

```
============================================================
DICTIONARY STATISTICS
============================================================
Total words:        10,247
Unique words:       10,247
Min length:         4
Max length:         16
Average length:     8.34
============================================================
```

**What it means:**
- **Total words**: How many passwords generated
- **Unique words**: All are unique (set removes duplicates)
- **Min/Max length**: Shortest and longest passwords
- **Average length**: Mean password length

## 🎓 Learning Path

### Beginner Level

1. **Run Demo Mode**
   ```bash
   python3 main.py --demo
   ```

2. **Generate Simple Dictionary**
   - Use 2-3 base words
   - Disable mutations
   - Observe output

3. **Experiment with Mutations**
   - Enable one mutation at a time
   - See how wordlist grows

### Intermediate Level

1. **Create Targeted Wordlist**
   - Use company-specific words
   - Enable all mutations
   - Analyze results

2. **Use Username Files**
   - Create username list
   - Generate personalized passwords

3. **Understand Patterns**
   - Read `patterns.py`
   - Understand each pattern type

### Advanced Level

1. **Modify Code**
   - Add custom mutations
   - Create new patterns
   - Optimize generation

2. **Integrate with Tools**
   - Export for John the Ripper
   - Use with Hashcat
   - Automate testing

3. **Contribute**
   - Implement missing modules
   - Improve algorithms
   - Add features

## 🔐 Security Best Practices

### When Using This Tool

1. ✅ **Always get written permission**
2. ✅ **Use in isolated lab environment**
3. ✅ **Document all activities**
4. ✅ **Follow responsible disclosure**
5. ✅ **Respect privacy and laws**

### When Creating Wordlists

1. **Don't include:**
   - Real user passwords
   - Actual system credentials
   - Personal information
   - Proprietary data

2. **Do include:**
   - Generic patterns
   - Common weaknesses
   - Test data only

### When Testing

1. **Test only:**
   - Systems you own
   - Systems you have permission to test
   - In isolated environments

2. **Never test:**
   - Production systems without approval
   - Third-party systems
   - Public services

## 📚 Additional Resources

### Documentation

- `README.md` - Project overview
- `config.py` - Configuration reference
- Code comments - Extensive inline documentation

### Learning Resources

- **OWASP Password Guidelines**: https://owasp.org/
- **NIST Password Standards**: https://pages.nist.gov/
- **Python Security**: https://python.readthedocs.io/

### Tools Integration

- **John the Ripper**: https://www.openwall.com/john/
- **Hashcat**: https://hashcat.net/
- **CrackStation**: https://crackstation.net/

## 🤝 Contributing

### How to Contribute

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

### Development Setup

```bash
# Clone your fork
git clone https://github.com/yourusername/password-cracking-suite.git

# Create virtual environment (optional)
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Install dev dependencies (when added)
pip install -r requirements-dev.txt

# Run tests (when implemented)
python3 -m pytest
```

## ❓ FAQ

**Q: Is this legal to use?**
A: Yes, when used ethically on systems you own or have permission to test.

**Q: Can I use this for penetration testing?**
A: Yes, but only with proper authorization and legal agreements.

**Q: Why use this instead of existing tools?**
A: This is educational. It helps you understand how password cracking works.

**Q: Can I add this to my portfolio?**
A: Yes! It demonstrates security knowledge and Python skills.

**Q: Is this suitable for students?**
A: Yes, perfect for cybersecurity courses and learning.

## 📧 Support

- **Issues**: Open an issue on GitHub
- **Questions**: Check FAQ or documentation
- **Security**: Report responsibly

---

**Ready to start? Run:** `python3 main.py`

**Need help? Read:** `README.md`

**Want to learn? Study:** Code comments in `generator.py`
