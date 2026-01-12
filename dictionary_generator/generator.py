#!/usr/bin/env python3
"""
Dictionary Generator Module

This is the main dictionary generation engine. It takes user configuration
and generates a comprehensive wordlist by combining:
1. Base words provided by the user
2. Pattern variations (dates, numbers, keyboard walks)
3. Mutations (leet-speak, case changes, special characters)

The generator uses a set to ensure all passwords are unique.
"""

import os
import sys
from typing import List, Set, Dict
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import config
from dictionary_generator.patterns import PatternGenerator


class DictionaryGenerator:
    """
    Main Dictionary Generator Class
    
    This class orchestrates the entire dictionary generation process:
    1. Accepts user configuration
    2. Generates base passwords
    3. Applies mutations and patterns
    4. Saves results to file
    
    Usage:
        >>> gen = DictionaryGenerator()
        >>> config = {'base_words': ['admin', 'password'], ...}
        >>> gen.generate_dictionary(config)
        >>> gen.save_to_file('wordlist.txt')
    """
    
    def __init__(self):
        """
        Initialize the dictionary generator
        
        Sets up:
        - Empty wordlist (using set for uniqueness)
        - Pattern generator instance
        - Configuration defaults
        """
        # Use a set to automatically handle duplicates
        self.wordlist: Set[str] = set()
        
        # Initialize pattern generator
        self.pattern_gen = PatternGenerator()
        
        # Statistics tracking
        self.stats = {
            'base_words': 0,
            'date_patterns': 0,
            'mutations': 0,
            'total_generated': 0
        }
    
    # ==================== CORE GENERATION METHODS ====================
    
    def add_word(self, word: str):
        """
        Add a single word to the wordlist
        
        Args:
            word: Password string to add
            
        Note:
            Empty strings and None values are automatically filtered out
        """
        if word and len(word) > 0:
            self.wordlist.add(word)
    
    def add_words(self, words: List[str]):
        """
        Add multiple words to the wordlist
        
        Args:
            words: List of password strings to add
        """
        for word in words:
            self.add_word(word)
    
    # ==================== BASE WORD GENERATION ====================
    
    def generate_base_words(self, base_words: List[str]):
        """
        Add user-provided base words to the dictionary
        
        Base words are the foundation of the wordlist. Users typically provide:
        - Company names
        - Common usernames
        - Department names
        - Product names
        
        Args:
            base_words: List of base words from user
            
        Example:
            >>> gen = DictionaryGenerator()
            >>> gen.generate_base_words(['admin', 'company', 'user'])
            [+] Adding 3 base words...
        """
        print(f"[+] Adding {len(base_words)} base words...")
        self.add_words(base_words)
        self.stats['base_words'] = len(base_words)
    
    # ==================== DATE PATTERN GENERATION ====================
    
    def generate_with_dates(
        self, 
        base_words: List[str], 
        start_year: int, 
        end_year: int
    ):
        """
        Generate combinations of words with date patterns
        
        Creates patterns like:
        - admin2024 (full year)
        - admin24 (2-digit year)
        - admin01 (month)
        - admin31 (day)
        
        Why this matters:
        Users commonly append years, birth dates, or hire dates to passwords.
        This is a very predictable pattern that makes passwords weak.
        
        Args:
            base_words: List of base words
            start_year: Starting year (e.g., 1990)
            end_year: Ending year (e.g., 2024)
            
        Example:
            >>> gen = DictionaryGenerator()
            >>> gen.generate_with_dates(['password'], 2023, 2024)
            [+] Generating date combinations (2023-2024)...
                Generated 4 date combinations
        """
        print(f"[+] Generating date combinations ({start_year}-{end_year})...")
        count = 0
        
        # Generate year patterns using PatternGenerator
        years = self.pattern_gen.generate_year_patterns(start_year, end_year)
        
        for word in base_words:
            # Combine with years
            for year in years:
                self.add_word(f"{word}{year}")
                count += 1
            
            # Optional: Add month patterns (01-12)
            for month in range(1, 13):
                self.add_word(f"{word}{month:02d}")
                count += 1
            
            # Optional: Add day patterns (01-31)
            for day in range(1, 32):
                self.add_word(f"{word}{day:02d}")
                count += 1
        
        print(f"    Generated {count} date combinations")
        self.stats['date_patterns'] = count
    
    # ==================== NUMBER PATTERN GENERATION ====================
    
    def generate_with_numbers(
        self, 
        base_words: List[str], 
        max_number: int = 999
    ):
        """
        Generate combinations with number suffixes
        
        Creates patterns like:
        - password1, password2, password3
        - admin123
        - user0, user00, user000
        
        Why this matters:
        Users often add simple numbers to meet password requirements or
        create multiple accounts (user1, user2, etc.)
        
        Args:
            base_words: List of base words
            max_number: Maximum number to append (default: 999)
            
        Example:
            >>> gen = DictionaryGenerator()
            >>> gen.generate_with_numbers(['admin'], 10)
            [+] Generating number combinations...
                Generated 11 number combinations
        """
        print(f"[+] Generating number combinations...")
        count = 0
        
        # Common number patterns that users add
        common_numbers = [
            '1', '12', '123', '1234', '12345', '123456',
            '0', '00', '000', 
            '01', '001', '0001',
            '!', '!!', '!!!',
            '@', '@@'
        ]
        
        for word in base_words:
            # Add common number patterns
            for num in common_numbers:
                self.add_word(f"{word}{num}")
                count += 1
            
            # Add sequential numbers (0-max_number)
            # But limit to prevent explosion of combinations
            for i in range(min(100, max_number + 1)):
                self.add_word(f"{word}{i}")
                count += 1
        
        print(f"    Generated {count} number combinations")
    
    # ==================== COMMON PASSWORDS ====================
    
    def generate_common_passwords(self):
        """
        Add commonly used passwords from breached databases
        
        These are passwords that appear frequently in data breaches:
        - password, password123
        - 123456, qwerty
        - admin, letmein
        
        Why include these:
        Even though everyone knows these are weak, people still use them!
        Including them tests if users are following basic security practices.
        
        Example:
            >>> gen = DictionaryGenerator()
            >>> gen.generate_common_passwords()
            [+] Adding 20 common passwords...
        """
        print(f"[+] Adding {len(config.COMMON_PASSWORDS)} common passwords...")
        self.add_words(config.COMMON_PASSWORDS)
    
    # ==================== KEYBOARD PATTERNS ====================
    
    def generate_keyboard_patterns(self):
        """
        Add keyboard walking patterns
        
        "Keyboard walking" is when users type adjacent keys:
        - qwerty (top row)
        - asdfgh (home row)
        - 1qaz2wsx (vertical walk)
        
        Why include these:
        These feel random to users but are actually very predictable
        and easy for attackers to guess.
        
        Example:
            >>> gen = DictionaryGenerator()
            >>> gen.generate_keyboard_patterns()
            [+] Adding 16 keyboard patterns...
        """
        print(f"[+] Adding {len(config.KEYBOARD_PATTERNS)} keyboard patterns...")
        self.add_words(config.KEYBOARD_PATTERNS)
    
    # ==================== MUTATION METHODS ====================
    
    def apply_leet_speak(self, base_words: List[str]):
        """
        Apply leet-speak (1337 speak) transformations
        
        Leet-speak substitutes letters with similar-looking numbers/symbols:
        - password → p@ssw0rd
        - admin → adm1n
        - leetspeak → 1337sp34k
        
        Why apply this:
        Users think this makes passwords stronger, but it's a well-known
        pattern that cracking tools automatically check.
        
        Args:
            base_words: Words to transform
            
        Example:
            >>> gen = DictionaryGenerator()
            >>> gen.apply_leet_speak(['password', 'admin'])
            [+] Applying leet-speak mutations...
                Generated 10 leet-speak variants
        """
        print("[+] Applying leet-speak mutations...")
        count = 0
        new_words = set()
        
        for word in base_words:
            # Use PatternGenerator to create leet variants
            variants = self.pattern_gen.generate_leet_speak_patterns(word)
            new_words.update(variants)
            count += len(variants)
        
        self.add_words(list(new_words))
        print(f"    Generated {count} leet-speak variants")
        self.stats['mutations'] += count
    
    def apply_uppercase_variations(self, base_words: List[str]):
        """
        Apply case variations to words
        
        Creates different capitalization patterns:
        - password → Password, PASSWORD, password, PaSsWoRd
        
        Why apply this:
        Password policies often require mixed case, so users typically
        just capitalize the first letter. This checks those variations.
        
        Args:
            base_words: Words to vary
            
        Example:
            >>> gen = DictionaryGenerator()
            >>> gen.apply_uppercase_variations(['password'])
            [+] Applying uppercase variations...
                Generated 4 case variations
        """
        print("[+] Applying uppercase variations...")
        count = 0
        new_words = set()
        
        for word in base_words:
            # Use PatternGenerator to create case variants
            variants = self.pattern_gen.generate_case_variations(word)
            new_words.update(variants)
            count += len(variants)
        
        self.add_words(list(new_words))
        print(f"    Generated {count} case variations")
        self.stats['mutations'] += count
    
    def apply_special_characters(self, base_words: List[str]):
        """
        Add special character variations
        
        Appends or prepends special characters:
        - password → password!, @password, password#
        
        Why apply this:
        Password policies often require special characters.
        Users typically just add one at the end (password!).
        
        Args:
            base_words: Words to modify
            
        Example:
            >>> gen = DictionaryGenerator()
            >>> gen.apply_special_characters(['admin'])
            [+] Applying special character mutations...
                Generated 16 special character variations
        """
        print("[+] Applying special character mutations...")
        count = 0
        
        for word in base_words:
            # Use PatternGenerator to create special char variants
            variants = self.pattern_gen.generate_special_char_variations(word)
            self.add_words(variants)
            count += len(variants)
        
        print(f"    Generated {count} special character variations")
        self.stats['mutations'] += count
    
    # ==================== USERNAME FILE PROCESSING ====================
    
    def generate_from_username_file(self, filepath: str):
        """
        Generate passwords from a username file
        
        Reads a file containing usernames and generates password
        variations based on those names. Common pattern: username = password!
        
        File format:
            john.smith
            admin
            j.doe
        
        Generates:
            john.smith, john.smith123, johnsmith, j.smith, etc.
        
        Args:
            filepath: Path to username file (one username per line)
            
        Example:
            >>> gen = DictionaryGenerator()
            >>> gen.generate_from_username_file('usernames.txt')
            [+] Reading usernames from usernames.txt...
                Found 50 usernames
        """
        if not os.path.exists(filepath):
            print(f"[-] Username file not found: {filepath}")
            return
        
        print(f"[+] Reading usernames from {filepath}...")
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                usernames = [line.strip() for line in f if line.strip()]
            
            print(f"    Found {len(usernames)} usernames")
            
            # Add usernames as-is
            self.add_words(usernames)
            
            # Generate common username-based passwords
            for username in usernames:
                # Common patterns
                self.add_word(f"{username}123")
                self.add_word(f"{username}@123")
                self.add_word(f"{username}!")
                self.add_word(f"{username}2024")
                
                # Remove dots and underscores
                cleaned = username.replace('.', '').replace('_', '')
                if cleaned != username:
                    self.add_word(cleaned)
                    self.add_word(f"{cleaned}123")
                
        except Exception as e:
            print(f"[-] Error reading username file: {e}")
    
    # ==================== MAIN GENERATION ORCHESTRATOR ====================
    
    def generate_dictionary(self, user_config: Dict) -> int:
        """
        Main method that orchestrates the entire generation process
        
        This is the primary entry point. It:
        1. Extracts configuration from user input
        2. Generates base words
        3. Applies patterns (dates, numbers, keyboard)
        4. Applies mutations (leet, case, special chars)
        5. Returns the total count
        
        Args:
            user_config: Dictionary containing user preferences
                {
                    'base_words': ['admin', 'password'],
                    'use_dates': True,
                    'start_year': 2020,
                    'end_year': 2024,
                    'use_common': True,
                    'use_keyboard': True,
                    'mutations': {
                        'leetspeak': True,
                        'uppercase': True,
                        'numbers': True,
                        'special': True
                    },
                    'username_file': '',
                    'output_file': 'wordlist.txt',
                    'max_words': 10000
                }
        
        Returns:
            int: Total number of unique passwords generated
            
        Example:
            >>> gen = DictionaryGenerator()
            >>> config = {'base_words': ['test'], 'use_dates': False, ...}
            >>> count = gen.generate_dictionary(config)
            >>> print(f"Generated {count} passwords")
        """
        print("\n" + "="*60)
        print("DICTIONARY GENERATION STARTED")
        print("="*60)
        
        # Extract configuration
        base_words = user_config.get('base_words', [])
        mutations = user_config.get('mutations', {})
        
        # Validate input
        if not base_words:
            print("[-] No base words provided!")
            return 0
        
        # STEP 1: Add base words
        self.generate_base_words(base_words)
        
        # STEP 2: Process username file if provided
        username_file = user_config.get('username_file')
        if username_file and os.path.exists(username_file):
            self.generate_from_username_file(username_file)
        
        # STEP 3: Generate date patterns
        if user_config.get('use_dates'):
            self.generate_with_dates(
                base_words,
                user_config.get('start_year', config.DEFAULT_START_YEAR),
                user_config.get('end_year', config.DEFAULT_END_YEAR)
            )
        
        # STEP 4: Add common passwords
        if user_config.get('use_common'):
            self.generate_common_passwords()
        
        # STEP 5: Add keyboard patterns
        if user_config.get('use_keyboard'):
            self.generate_keyboard_patterns()
        
        # STEP 6: Add number combinations
        if mutations.get('numbers', True):
            self.generate_with_numbers(base_words)
        
        # STEP 7: Apply mutations to base words
        # Create a snapshot of current words to mutate
        current_words = list(self.wordlist)[:len(base_words) * 10]  # Limit to prevent explosion
        
        if mutations.get('leetspeak'):
            self.apply_leet_speak(base_words)
        
        if mutations.get('uppercase'):
            self.apply_uppercase_variations(base_words)
        
        if mutations.get('special'):
            self.apply_special_characters(base_words)
        
        # Update statistics
        self.stats['total_generated'] = len(self.wordlist)
        
        print("\n" + "="*60)
        print(f"GENERATION COMPLETE: {len(self.wordlist):,} unique words")
        print("="*60)
        
        return len(self.wordlist)
    
    # ==================== OUTPUT METHODS ====================
    
    def save_to_file(self, filepath: str, max_words: int = 0):
        """
        Save the generated wordlist to a file
        
        The wordlist is saved with one password per line.
        Passwords are sorted by length then alphabetically for better organization.
        
        Args:
            filepath: Output file path
            max_words: Maximum words to save (0 = save all)
            
        Example:
            >>> gen = DictionaryGenerator()
            >>> gen.save_to_file('wordlist.txt', max_words=10000)
            [+] Saving dictionary to wordlist.txt...
            [✓] Saved 10000 words to wordlist.txt
                File size: 85.3 KB
        """
        print(f"\n[+] Saving dictionary to {filepath}...")
        
        try:
            # Convert set to list and sort
            words_to_save = list(self.wordlist)
            
            # Sort by length first, then alphabetically
            # This makes the file more organized and easier to analyze
            words_to_save.sort(key=lambda x: (len(x), x))
            
            # Limit if specified
            if max_words > 0 and len(words_to_save) > max_words:
                words_to_save = words_to_save[:max_words]
                print(f"    Limited to {max_words:,} words")
            
            # Write to file
            with open(filepath, 'w', encoding='utf-8') as f:
                for word in words_to_save:
                    f.write(word + '\n')
            
            # Show success message with file size
            file_size_kb = os.path.getsize(filepath) / 1024
            print(f"[✓] Saved {len(words_to_save):,} words to {filepath}")
            print(f"    File size: {file_size_kb:.2f} KB")
            
        except Exception as e:
            print(f"[-] Error saving file: {e}")
    
    # ==================== STATISTICS AND REPORTING ====================
    
    def get_statistics(self) -> Dict:
        """
        Get statistics about the generated dictionary
        
        Returns:
            Dictionary containing statistics:
            - total_words: Total unique passwords
            - min_length: Shortest password length
            - max_length: Longest password length
            - avg_length: Average password length
        
        Example:
            >>> gen = DictionaryGenerator()
            >>> stats = gen.get_statistics()
            >>> print(stats['total_words'])
        """
        words = list(self.wordlist)
        
        if not words:
            return {}
        
        return {
            'total_words': len(words),
            'min_length': min(len(w) for w in words),
            'max_length': max(len(w) for w in words),
            'avg_length': sum(len(w) for w in words) / len(words),
            'unique_words': len(set(words))
        }
    
    def print_statistics(self):
        """
        Print formatted statistics about the generated dictionary
        
        Example output:
            ============================================================
            DICTIONARY STATISTICS
            ============================================================
            Total words:        10,247
            Unique words:       10,247
            Min length:         4
            Max length:         16
            Average length:     8.34
            ============================================================
        """
        stats = self.get_statistics()
        
        if not stats:
            print("[-] No statistics available")
            return
        
        print("\n" + "="*60)
        print("DICTIONARY STATISTICS")
        print("="*60)
        print(f"Total words:        {stats['total_words']:,}")
        print(f"Unique words:       {stats['unique_words']:,}")
        print(f"Min length:         {stats['min_length']}")
        print(f"Max length:         {stats['max_length']}")
        print(f"Average length:     {stats['avg_length']:.2f}")
        print("="*60)
    
    def print_sample(self, count: int = 20):
        """
        Print a sample of generated passwords
        
        Useful for previewing the wordlist before saving.
        Shows the first N passwords (sorted).
        
        Args:
            count: Number of samples to show
            
        Example output:
            [+] Sample words (20 of 1,247):
                  1. !admin
                  2. !password
                  3. #admin
                  ... and 1,227 more
        """
        words = list(self.wordlist)
        
        if not words:
            print("[-] No words in dictionary")
            return
        
        print(f"\n[+] Sample words ({min(count, len(words))} of {len(words):,}):")
        for i, word in enumerate(sorted(words)[:count], 1):
            print(f"    {i:3d}. {word}")
        
        if len(words) > count:
            print(f"    ... and {len(words) - count:,} more")


# ==================== STANDALONE USAGE ====================

def main():
    """
    Example usage when running this file directly
    
    Demonstrates how to use the DictionaryGenerator programmatically.
    """
    # Example configuration
    example_config = {
        'base_words': ['admin', 'password', 'user', 'test'],
        'username_file': '',
        'use_dates': True,
        'start_year': 2020,
        'end_year': 2024,
        'use_common': True,
        'use_keyboard': True,
        'mutations': {
            'leetspeak': True,
            'uppercase': True,
            'numbers': True,
            'special': True
        },
        'output_file': 'wordlist.txt',
        'max_words': 5000
    }
    
    # Create generator
    generator = DictionaryGenerator()
    
    # Generate dictionary
    word_count = generator.generate_dictionary(example_config)
    
    # Show statistics
    generator.print_statistics()
    
    # Show samples
    generator.print_sample(30)
    
    # Save to file
    generator.save_to_file(
        example_config['output_file'],
        example_config['max_words']
    )
    
    print("\n[✓] Dictionary generation complete!")


if __name__ == "__main__":
    main()
