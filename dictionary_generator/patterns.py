#!/usr/bin/env python3
"""
Pattern Generator Module

This module contains classes and functions for generating various password patterns:
- Date patterns (years, months, days)
- Keyboard walking patterns
- Number sequences
- Common substitutions

These patterns are used by the DictionaryGenerator to create comprehensive wordlists.
"""

from typing import List, Set
import config


class PatternGenerator:
    """
    Generates various password patterns based on common password creation habits
    
    This class is responsible for creating predictable patterns that users
    commonly incorporate into their passwords.
    """
    
    def __init__(self):
        """Initialize the pattern generator with default settings"""
        self.patterns: Set[str] = set()
    
    # ==================== DATE PATTERNS ====================
    
    def generate_year_patterns(self, start_year: int, end_year: int) -> List[str]:
        """
        Generate year-based patterns
        
        Users often append years to passwords (e.g., password2024)
        This function generates both 4-digit and 2-digit year formats.
        
        Args:
            start_year: Starting year (e.g., 1990)
            end_year: Ending year (e.g., 2024)
        
        Returns:
            List of year strings in both formats
            
        Example:
            >>> gen = PatternGenerator()
            >>> years = gen.generate_year_patterns(2023, 2024)
            >>> print(years)
            ['2023', '23', '2024', '24']
        """
        years = []
        
        for year in range(start_year, end_year + 1):
            # Full year format (e.g., 2024)
            years.append(str(year))
            
            # Two-digit year format (e.g., 24)
            years.append(str(year)[2:])
        
        return years
    
    def generate_month_patterns(self) -> List[str]:
        """
        Generate month-based patterns
        
        Returns months in various formats:
        - Single digit (1-9)
        - Zero-padded (01-12)
        - Month names (january, jan, etc.)
        
        Returns:
            List of month patterns
            
        Example:
            >>> gen = PatternGenerator()
            >>> months = gen.generate_month_patterns()
            >>> '01' in months and 'january' in months
            True
        """
        months = []
        
        # Numeric months
        for month in range(1, 13):
            months.append(str(month))          # 1, 2, 3...
            months.append(f"{month:02d}")      # 01, 02, 03...
        
        # Month names (optional - can be added if needed)
        month_names = [
            'january', 'february', 'march', 'april', 'may', 'june',
            'july', 'august', 'september', 'october', 'november', 'december'
        ]
        
        # Short month names
        month_short = ['jan', 'feb', 'mar', 'apr', 'may', 'jun',
                      'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
        
        # Uncomment to include month names
        # months.extend(month_names)
        # months.extend(month_short)
        
        return months
    
    def generate_day_patterns(self) -> List[str]:
        """
        Generate day-based patterns
        
        Returns days in formats commonly used in passwords:
        - Single digit (1-9)
        - Zero-padded (01-31)
        
        Returns:
            List of day patterns
            
        Example:
            >>> gen = PatternGenerator()
            >>> days = gen.generate_day_patterns()
            >>> '01' in days and '31' in days
            True
        """
        days = []
        
        for day in range(1, 32):
            days.append(str(day))          # 1, 2, 3...
            days.append(f"{day:02d}")      # 01, 02, 03...
        
        return days
    
    # ==================== NUMBER SEQUENCES ====================
    
    def generate_number_sequences(self, max_length: int = 6) -> List[str]:
        """
        Generate common number sequences
        
        Creates predictable number patterns like:
        - Sequential: 123, 1234, 12345
        - Repeated: 111, 222, 1111
        - Common: 007, 420, 666
        
        Args:
            max_length: Maximum length of sequences
        
        Returns:
            List of number sequence patterns
            
        Example:
            >>> gen = PatternGenerator()
            >>> seqs = gen.generate_number_sequences(4)
            >>> '123' in seqs and '1111' in seqs
            True
        """
        sequences = []
        
        # Sequential numbers (123, 1234, 12345...)
        for length in range(1, max_length + 1):
            sequences.append(''.join(str(i) for i in range(length)))
        
        # Repeated digits (111, 222, 1111, 2222...)
        for digit in range(10):
            for length in range(2, max_length + 1):
                sequences.append(str(digit) * length)
        
        # Common significant numbers
        common_numbers = [
            '007', '69', '420', '666', '777', '888', '999',
            '000', '101', '143', '1337'  # 1337 = "leet"
        ]
        sequences.extend(common_numbers)
        
        return sequences
    
    # ==================== KEYBOARD PATTERNS ====================
    
    def generate_keyboard_walking_patterns(self) -> List[str]:
        """
        Generate keyboard walking patterns
        
        "Keyboard walking" is when users type adjacent keys in sequence.
        Examples: qwerty (top row), asdf (home row), zxcv (bottom row)
        
        These are surprisingly common in weak passwords!
        
        Returns:
            List of keyboard walking patterns
            
        Example:
            >>> gen = PatternGenerator()
            >>> patterns = gen.generate_keyboard_walking_patterns()
            >>> 'qwerty' in patterns and 'asdfgh' in patterns
            True
        """
        patterns = []
        
        # QWERTY keyboard rows
        keyboard_rows = [
            'qwertyuiop',    # Top row
            'asdfghjkl',     # Home row
            'zxcvbnm',       # Bottom row
        ]
        
        # Add full rows and substrings
        for row in keyboard_rows:
            patterns.append(row)
            
            # Add substrings (minimum 4 characters)
            for i in range(len(row) - 3):
                for j in range(i + 4, len(row) + 1):
                    patterns.append(row[i:j])
        
        # Common keyboard walks
        common_walks = [
            '1qaz2wsx',      # Left hand vertical walk
            'qazwsx',        # Diagonal walk
            '!qaz@wsx',      # With shift
            '1q2w3e4r',      # Alternating pattern
            'qweasd',        # Two rows
            '123qwe',        # Numbers to letters
        ]
        patterns.extend(common_walks)
        
        return patterns
    
    # ==================== SPECIAL PATTERNS ====================
    
    def generate_leet_speak_patterns(self, word: str) -> List[str]:
        """
        Generate leet-speak (1337 5p34k) variations of a word
        
        Leet-speak replaces letters with numbers/symbols:
        - a → @, 4
        - e → 3
        - i → 1, !
        - o → 0
        - s → $, 5
        
        Args:
            word: Word to convert to leet-speak
        
        Returns:
            List of leet-speak variations
            
        Example:
            >>> gen = PatternGenerator()
            >>> variations = gen.generate_leet_speak_patterns('password')
            >>> 'p@ssw0rd' in variations
            True
        """
        variations = [word]  # Include original
        word_lower = word.lower()
        
        # Simple single-character replacements
        # We limit to basic substitutions to avoid exponential growth
        
        leet_map = config.LEET_SPEAK_MAP
        
        for char, replacements in leet_map.items():
            if char in word_lower:
                # Try each replacement
                for replacement in replacements[1:]:  # Skip original character
                    variant = word_lower.replace(char, replacement)
                    variations.append(variant)
        
        return variations
    
    def generate_case_variations(self, word: str) -> List[str]:
        """
        Generate case variations of a word
        
        Creates different capitalization patterns:
        - All lowercase: password
        - All uppercase: PASSWORD
        - First letter capital: Password
        - Alternating: PaSsWoRd
        
        Args:
            word: Word to vary
        
        Returns:
            List of case variations
            
        Example:
            >>> gen = PatternGenerator()
            >>> variations = gen.generate_case_variations('password')
            >>> 'Password' in variations and 'PASSWORD' in variations
            True
        """
        variations = []
        
        # All lowercase
        variations.append(word.lower())
        
        # All uppercase
        variations.append(word.upper())
        
        # First letter uppercase (Title case)
        variations.append(word.capitalize())
        
        # Alternating case (for shorter words only)
        if len(word) <= 10:
            alternating = ''.join(
                c.upper() if i % 2 == 0 else c.lower()
                for i, c in enumerate(word)
            )
            variations.append(alternating)
        
        return variations
    
    def generate_special_char_variations(self, word: str) -> List[str]:
        """
        Generate variations with special characters appended/prepended
        
        Users often add special characters to meet password requirements:
        - password! → meets "needs special char" requirement
        - @password → prepended special char
        
        Args:
            word: Base word
        
        Returns:
            List of variations with special characters
            
        Example:
            >>> gen = PatternGenerator()
            >>> variations = gen.generate_special_char_variations('password')
            >>> 'password!' in variations and '@password' in variations
            True
        """
        variations = []
        
        special_chars = config.SPECIAL_CHARACTERS
        
        for char in special_chars:
            # Append special character
            variations.append(f"{word}{char}")
            
            # Prepend special character
            variations.append(f"{char}{word}")
        
        return variations
    
    # ==================== COMBINATION PATTERNS ====================
    
    def generate_word_number_combinations(
        self, 
        words: List[str], 
        numbers: List[str],
        max_combinations: int = 100
    ) -> List[str]:
        """
        Generate combinations of words and numbers
        
        Creates patterns like:
        - admin123
        - password2024
        - user01
        
        Args:
            words: List of base words
            numbers: List of numbers to append
            max_combinations: Maximum combinations to generate
        
        Returns:
            List of word+number combinations
            
        Example:
            >>> gen = PatternGenerator()
            >>> combos = gen.generate_word_number_combinations(
            ...     ['admin'], ['123', '2024']
            ... )
            >>> 'admin123' in combos and 'admin2024' in combos
            True
        """
        combinations = []
        count = 0
        
        for word in words:
            for number in numbers:
                if count >= max_combinations:
                    break
                    
                # Word + Number
                combinations.append(f"{word}{number}")
                count += 1
                
            if count >= max_combinations:
                break
        
        return combinations


# ==================== HELPER FUNCTIONS ====================

def get_common_passwords() -> List[str]:
    """
    Return list of commonly used passwords
    
    These are passwords found in data breaches and should
    NEVER be used in real systems.
    
    Returns:
        List of common passwords
    """
    return config.COMMON_PASSWORDS.copy()


def get_keyboard_patterns() -> List[str]:
    """
    Return list of keyboard walking patterns
    
    Returns:
        List of keyboard patterns
    """
    return config.KEYBOARD_PATTERNS.copy()


# ==================== TESTING ====================

if __name__ == "__main__":
    """Test the pattern generator"""
    
    print("Testing Pattern Generator\n")
    print("="*60)
    
    gen = PatternGenerator()
    
    # Test year patterns
    print("\n1. Year Patterns (2022-2024):")
    years = gen.generate_year_patterns(2022, 2024)
    print(f"   Generated: {years[:10]}")
    
    # Test keyboard patterns
    print("\n2. Keyboard Patterns:")
    keyboard = gen.generate_keyboard_walking_patterns()
    print(f"   Generated: {keyboard[:10]}")
    
    # Test leet-speak
    print("\n3. Leet-Speak ('password'):")
    leet = gen.generate_leet_speak_patterns('password')
    print(f"   Generated: {leet[:10]}")
    
    # Test case variations
    print("\n4. Case Variations ('admin'):")
    cases = gen.generate_case_variations('admin')
    print(f"   Generated: {cases}")
    
    # Test special char variations
    print("\n5. Special Char Variations ('test'):")
    special = gen.generate_special_char_variations('test')
    print(f"   Generated: {special[:10]}")
    
    print("\n" + "="*60)
    print("Pattern Generator Test Complete!")
