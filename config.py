#!/usr/bin/env python3
"""
Configuration Module
Centralized configuration for the Password Cracking Suite

This module contains all configurable settings for the application.
Modify these values to customize the behavior of the toolkit.
"""

import os
from pathlib import Path

# ==================== PROJECT PATHS ====================
# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent

# Output directories
OUTPUT_DIR = BASE_DIR / 'output'
WORDLIST_DIR = OUTPUT_DIR / 'wordlists'
CRACKED_DIR = OUTPUT_DIR / 'cracked'
REPORTS_DIR = OUTPUT_DIR / 'reports'
LOGS_DIR = OUTPUT_DIR / 'logs'

# Sample files directory
SAMPLES_DIR = BASE_DIR / 'samples'

# Ensure output directories exist
for directory in [OUTPUT_DIR, WORDLIST_DIR, CRACKED_DIR, REPORTS_DIR, LOGS_DIR]:
    directory.mkdir(parents=True, exist_ok=True)


# ==================== DICTIONARY GENERATION SETTINGS ====================

# Default year range for date patterns
DEFAULT_START_YEAR = 1990
DEFAULT_END_YEAR = 2024

# Maximum number of words to generate (0 = unlimited)
MAX_WORDLIST_SIZE = 100000

# Default base words if none provided
DEFAULT_BASE_WORDS = ['password', 'admin', 'user', 'test']

# Common passwords to include
COMMON_PASSWORDS = [
    "password", "123456", "password123", "admin", "letmein",
    "welcome", "monkey", "dragon", "master", "sunshine",
    "princess", "qwerty", "abc123", "111111", "iloveyou",
    "admin123", "password1", "12345678", "123456789", "1234567890"
]

# Keyboard patterns to include
KEYBOARD_PATTERNS = [
    "qwerty", "qwertyuiop", "asdfgh", "asdfghjkl", "zxcvbn",
    "1qaz2wsx", "qazwsx", "123qwe", "1q2w3e4r", "qweasd",
    "!qaz@wsx", "1234", "12345", "123456", "1234567", "12345678"
]

# Leet-speak character mappings
LEET_SPEAK_MAP = {
    'a': ['a', '@', '4'],
    'e': ['e', '3'],
    'i': ['i', '1', '!'],
    'o': ['o', '0'],
    's': ['s', '$', '5'],
    't': ['t', '7'],
    'l': ['l', '1'],
    'g': ['g', '9'],
    'b': ['b', '8']
}

# Special characters for mutations
SPECIAL_CHARACTERS = ['!', '@', '#', '$', '%', '&', '*', '?']


# ==================== HASH EXTRACTION SETTINGS ====================

# Supported hash algorithms
SUPPORTED_HASH_ALGORITHMS = [
    'MD5',          # $1$
    'SHA-256',      # $5$
    'SHA-512',      # $6$
    'NTLM',         # Windows
    'bcrypt',       # $2a$, $2b$, $2y$
]

# Linux shadow file default path (for reference only)
LINUX_SHADOW_PATH = '/etc/shadow'

# Windows SAM registry paths (for reference only)
WINDOWS_SAM_PATH = r'C:\Windows\System32\config\SAM'
WINDOWS_SYSTEM_PATH = r'C:\Windows\System32\config\SYSTEM'


# ==================== BRUTE-FORCE SETTINGS ====================

# Character sets for brute-force attacks
CHARSET_LOWERCASE = 'abcdefghijklmnopqrstuvwxyz'
CHARSET_UPPERCASE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
CHARSET_DIGITS = '0123456789'
CHARSET_SPECIAL = '!@#$%^&*()_+-=[]{}|;:,.<>?'

# Default character set combinations
CHARSET_ALPHA = CHARSET_LOWERCASE + CHARSET_UPPERCASE
CHARSET_ALPHANUMERIC = CHARSET_ALPHA + CHARSET_DIGITS
CHARSET_ALL = CHARSET_ALPHANUMERIC + CHARSET_SPECIAL

# Password length constraints
MIN_PASSWORD_LENGTH = 1
MAX_PASSWORD_LENGTH = 12  # Increase with caution - exponential growth!

# Attack timeout (seconds)
ATTACK_TIMEOUT = 3600  # 1 hour

# Maximum attempts before timeout warning
MAX_ATTEMPTS_WARNING = 1000000


# ==================== PASSWORD STRENGTH ANALYZER SETTINGS ====================

# Complexity requirements (for scoring)
MIN_LENGTH_WEAK = 8
MIN_LENGTH_MEDIUM = 12
MIN_LENGTH_STRONG = 16

# Entropy thresholds (bits)
ENTROPY_WEAK = 28      # < 28 bits = weak
ENTROPY_MEDIUM = 36    # 28-36 bits = medium
ENTROPY_STRONG = 60    # 36-60 bits = strong
ENTROPY_VERY_STRONG = 128  # > 60 bits = very strong

# Character class requirements
REQUIRE_UPPERCASE = True
REQUIRE_LOWERCASE = True
REQUIRE_DIGITS = True
REQUIRE_SPECIAL = True

# Common password lists to check against
COMMON_PASSWORDS_FILE = SAMPLES_DIR / 'common_passwords.txt'


# ==================== REPORT GENERATION SETTINGS ====================

# Report format
DEFAULT_REPORT_FORMAT = 'txt'  # Options: 'txt', 'json', 'html', 'pdf'

# Report sections to include
INCLUDE_EXECUTIVE_SUMMARY = True
INCLUDE_DETAILED_FINDINGS = True
INCLUDE_STATISTICS = True
INCLUDE_RECOMMENDATIONS = True
INCLUDE_METHODOLOGY = True

# Report templates
REPORT_TEMPLATE_DIR = BASE_DIR / 'reports' / 'templates'


# ==================== LOGGING SETTINGS ====================

# Logging level
# Options: 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'
LOG_LEVEL = 'INFO'

# Log file name
LOG_FILE = LOGS_DIR / 'password_cracking_suite.log'

# Log format
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOG_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

# Console output
VERBOSE_OUTPUT = True
SHOW_PROGRESS_BAR = True


# ==================== PERFORMANCE SETTINGS ====================

# Multi-threading settings
USE_MULTIPROCESSING = True
MAX_WORKERS = 4  # Number of parallel processes

# Memory management
MAX_MEMORY_MB = 2048  # Maximum memory usage in MB

# Batch processing
BATCH_SIZE = 1000  # Process passwords in batches


# ==================== SECURITY SETTINGS ====================

# Ethical use disclaimer
REQUIRE_DISCLAIMER_ACCEPTANCE = True

# Disclaimer text
DISCLAIMER_TEXT = """
⚠️  ETHICAL USE DISCLAIMER ⚠️

This tool is designed for EDUCATIONAL PURPOSES and AUTHORIZED SECURITY TESTING ONLY.

By using this tool, you acknowledge and agree that:
1. You will only use this tool on systems you own or have explicit written permission to test
2. Unauthorized access to computer systems is illegal and punishable by law
3. The developers assume no liability for misuse of this tool
4. You are solely responsible for ensuring compliance with all applicable laws

Do you understand and agree to use this tool ethically and legally?
"""

# Sensitive data handling
CLEAR_MEMORY_ON_EXIT = True
ENCRYPT_STORED_RESULTS = False  # Future feature


# ==================== APPLICATION SETTINGS ====================

# Application metadata
APP_NAME = "Password Cracking & Credential Attack Suite"
APP_VERSION = "1.0.0"
APP_AUTHOR = "Security Research Team"
APP_DESCRIPTION = "Educational toolkit for password policy testing and security assessment"

# Default configuration for new users
DEFAULT_CONFIG = {
    'dictionary': {
        'base_words': DEFAULT_BASE_WORDS,
        'use_dates': True,
        'start_year': DEFAULT_START_YEAR,
        'end_year': DEFAULT_END_YEAR,
        'use_common': True,
        'use_keyboard': True,
        'mutations': {
            'leetspeak': True,
            'uppercase': True,
            'numbers': True,
            'special': False
        },
        'output_file': str(WORDLIST_DIR / 'wordlist.txt'),
        'max_words': MAX_WORDLIST_SIZE
    },
    'hash_extraction': {
        'enabled': False,
        'hash_type': 'linux_shadow',
        'hash_source': '',
        'output_file': str(CRACKED_DIR / 'extracted_hashes.txt')
    },
    'attack_simulation': {
        'mode': 'dictionary',
        'hash_file': '',
        'dictionary_file': str(WORDLIST_DIR / 'wordlist.txt'),
        'charset': CHARSET_ALPHANUMERIC,
        'min_length': MIN_PASSWORD_LENGTH,
        'max_length': 8,
        'output_file': str(CRACKED_DIR / 'cracked.txt')
    },
    'analysis': {
        'enabled': True,
        'input_type': 'file',
        'source': '',
        'check_complexity': True,
        'calculate_entropy': True,
        'check_dictionary': True,
        'report_file': str(REPORTS_DIR / 'analysis_report.txt')
    }
}


# ==================== HELPER FUNCTIONS ====================

def get_config_value(key, default=None):
    """
    Get a configuration value by key
    
    Args:
        key: Configuration key (e.g., 'MAX_WORDLIST_SIZE')
        default: Default value if key not found
    
    Returns:
        Configuration value or default
    """
    return globals().get(key, default)


def set_config_value(key, value):
    """
    Set a configuration value
    
    Args:
        key: Configuration key
        value: Value to set
    """
    globals()[key] = value


def load_custom_config(config_file):
    """
    Load custom configuration from file
    
    Args:
        config_file: Path to configuration file
    """
    import json
    try:
        with open(config_file, 'r') as f:
            custom_config = json.load(f)
            for key, value in custom_config.items():
                if key in globals():
                    globals()[key] = value
        print(f"[✓] Loaded custom configuration from {config_file}")
    except Exception as e:
        print(f"[!] Error loading custom configuration: {e}")


def print_config():
    """Print current configuration"""
    print("\n" + "="*60)
    print("CURRENT CONFIGURATION")
    print("="*60)
    
    config_items = {
        'Application': {
            'Name': APP_NAME,
            'Version': APP_VERSION,
            'Author': APP_AUTHOR
        },
        'Paths': {
            'Base Directory': BASE_DIR,
            'Output Directory': OUTPUT_DIR,
            'Wordlist Directory': WORDLIST_DIR,
            'Reports Directory': REPORTS_DIR
        },
        'Dictionary Generation': {
            'Default Year Range': f"{DEFAULT_START_YEAR}-{DEFAULT_END_YEAR}",
            'Max Wordlist Size': MAX_WORDLIST_SIZE,
            'Common Passwords': len(COMMON_PASSWORDS),
            'Keyboard Patterns': len(KEYBOARD_PATTERNS)
        },
        'Attack Settings': {
            'Max Password Length': MAX_PASSWORD_LENGTH,
            'Attack Timeout': f"{ATTACK_TIMEOUT}s",
            'Use Multiprocessing': USE_MULTIPROCESSING,
            'Max Workers': MAX_WORKERS
        },
        'Analysis Settings': {
            'Min Length (Strong)': MIN_LENGTH_STRONG,
            'Entropy Threshold (Strong)': f"{ENTROPY_STRONG} bits",
            'Log Level': LOG_LEVEL
        }
    }
    
    for section, items in config_items.items():
        print(f"\n{section}:")
        for key, value in items.items():
            print(f"  {key}: {value}")
    
    print("\n" + "="*60)


if __name__ == "__main__":
    """Print configuration when run directly"""
    print_config()
