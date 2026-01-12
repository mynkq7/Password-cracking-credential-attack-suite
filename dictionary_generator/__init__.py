"""
Dictionary Generator Module

This module provides functionality for generating custom password dictionaries
based on various patterns, mutations, and user-provided inputs.
"""

from .generator import DictionaryGenerator
from .patterns import PatternGenerator

__all__ = ['DictionaryGenerator', 'PatternGenerator']
__version__ = '1.0.0'
