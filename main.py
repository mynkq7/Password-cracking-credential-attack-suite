#!/usr/bin/env python3
"""
Password Cracking & Credential Attack Suite
Main Application Entry Point

This is the primary interface for the password cracking toolkit.
It provides an interactive menu system for all features.

Usage:
    python3 main.py              # Interactive mode
    python3 main.py --demo       # Demo mode with sample data
    python3 main.py --help       # Show help
"""

import sys
import os
import json
import argparse
from datetime import datetime
from pathlib import Path

# Import configuration
import config

# Import modules
from dictionary_generator.generator import DictionaryGenerator


class PasswordCrackingSuite:
    """
    Main Application Controller
    
    Coordinates all modules and provides user interface
    """
    
    def __init__(self):
        """Initialize the application"""
        self.config_data = {}
        self.current_wordlist = None
    
    def print_banner(self):
        """Display application banner with ASCII art"""
        banner = f"""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║   PASSWORD CRACKING & CREDENTIAL ATTACK SUITE                ║
║   Version {config.APP_VERSION:50s}║
║                                                              ║
║   ⚠️  Educational Use Only - Authorized Testing Required    ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝

Current Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Project Directory: {config.BASE_DIR}
"""
        print(banner)
        print("="*60)
    
    def show_disclaimer(self) -> bool:
        """
        Show ethical use disclaimer and get user agreement
        
        Returns:
            True if user agrees, False otherwise
        """
        if not config.REQUIRE_DISCLAIMER_ACCEPTANCE:
            return True
        
        print("\n" + config.DISCLAIMER_TEXT)
        
        while True:
            response = input("\nType 'I AGREE' to continue: ").strip().upper()
            if response == 'I AGREE':
                return True
            elif response in ['NO', 'N', 'EXIT', 'QUIT']:
                return False
            else:
                print("Invalid response. Please type 'I AGREE' or 'NO'")
    
    def show_main_menu(self):
        """Display main menu and get user choice"""
        menu = """
╔══════════════════════════════════════════════════════════════╗
║                         MAIN MENU                            ║
╚══════════════════════════════════════════════════════════════╝

📚 DICTIONARY GENERATION
  1. Generate Custom Dictionary
  2. Quick Generate (Default Settings)

🔐 HASH OPERATIONS (Coming Soon)
  3. Extract Linux Hashes (/etc/shadow)
  4. Extract Windows Hashes (SAM)

⚔️  ATTACK SIMULATION (Coming Soon)
  5. Dictionary Attack
  6. Brute-Force Attack
  7. Hybrid Attack

📊 ANALYSIS & REPORTING (Coming Soon)
  8. Analyze Password Strength
  9. Generate Security Report

⚙️  CONFIGURATION
  10. Load Configuration from File
  11. Show Current Configuration
  12. View Sample Files

❌ EXIT
  0. Exit Application

Select an option (0-12): """
        
        return input(menu).strip()
    
    def get_dictionary_config(self):
        """
        Interactive configuration for dictionary generation
        
        Returns:
            Dictionary with user preferences
        """
        print("\n" + "="*60)
        print("DICTIONARY GENERATION CONFIGURATION")
        print("="*60)
        
        cfg = {}
        
        # Base words - THE MOST IMPORTANT INPUT
        print("\n[Step 1] Enter base words (comma-separated):")
        print("  Examples: admin,password,company,employee,2024")
        print("  Tip: Use company name, common usernames, department names")
        base_input = input("  > ").strip()
        
        if base_input:
            cfg['base_words'] = [w.strip() for w in base_input.split(',')]
        else:
            print("  Using default words...")
            cfg['base_words'] = config.DEFAULT_BASE_WORDS
        
        print(f"  ✓ Using {len(cfg['base_words'])} base words")
        
        # Username file (optional)
        print("\n[Step 2] Username file (optional, press Enter to skip):")
        username_file = input("  Path: ").strip()
        cfg['username_file'] = username_file if os.path.exists(username_file) else ''
        
        # Date patterns
        print("\n[Step 3] Include date patterns? (y/n)")
        print("  Creates: password2024, admin2023, etc.")
        if input("  > ").lower() in ['y', 'yes']:
            cfg['use_dates'] = True
            cfg['start_year'] = int(input("  Start year (default 2020): ") or "2020")
            cfg['end_year'] = int(input("  End year (default 2024): ") or "2024")
        else:
            cfg['use_dates'] = False
        
        # Common passwords
        print("\n[Step 4] Include common weak passwords? (y/n)")
        print("  Adds: 123456, password123, qwerty, etc.")
        cfg['use_common'] = input("  > ").lower() in ['y', 'yes']
        
        # Keyboard patterns
        print("\n[Step 5] Include keyboard patterns? (y/n)")
        print("  Adds: qwerty, asdfgh, 1qaz2wsx, etc.")
        cfg['use_keyboard'] = input("  > ").lower() in ['y', 'yes']
        
        # Mutations
        print("\n[Step 6] Enable mutations:")
        cfg['mutations'] = {}
        
        print("  • Leet-speak (a→@, e→3, i→1)? (y/n)")
        cfg['mutations']['leetspeak'] = input("    > ").lower() in ['y', 'yes']
        
        print("  • Uppercase variations (Password, PASSWORD)? (y/n)")
        cfg['mutations']['uppercase'] = input("    > ").lower() in ['y', 'yes']
        
        print("  • Number suffixes (password123)? (y/n)")
        cfg['mutations']['numbers'] = input("    > ").lower() in ['y', 'yes']
        
        print("  • Special characters (password!)? (y/n)")
        cfg['mutations']['special'] = input("    > ").lower() in ['y', 'yes']
        
        # Output settings
        print("\n[Step 7] Output settings:")
        default_output = str(config.WORDLIST_DIR / 'custom_wordlist.txt')
        output_file = input(f"  Filename (default: {default_output}): ").strip()
        cfg['output_file'] = output_file if output_file else default_output
        
        max_words = input("  Max words (0=unlimited, default=10000): ").strip()
        cfg['max_words'] = int(max_words) if max_words else 10000
        
        return cfg
    
    def run_dictionary_generation(self, custom_config=None):
        """
        Execute dictionary generation
        
        Args:
            custom_config: Optional pre-configured settings
        """
        print("\n" + "="*60)
        print("DICTIONARY GENERATION MODULE")
        print("="*60)
        
        # Get configuration
        if custom_config is None:
            cfg = self.get_dictionary_config()
        else:
            cfg = custom_config
        
        # Save config
        self.config_data['dictionary'] = cfg
        
        # Create generator
        generator = DictionaryGenerator()
        
        # Generate
        try:
            word_count = generator.generate_dictionary(cfg)
            
            if word_count > 0:
                # Show statistics
                generator.print_statistics()
                
                # Show samples
                print("\n" + "="*60)
                print("SAMPLE PREVIEW")
                print("="*60)
                generator.print_sample(20)
                
                # Save
                generator.save_to_file(cfg['output_file'], cfg.get('max_words', 0))
                
                # Store for later use
                self.current_wordlist = cfg['output_file']
                
                print("\n✅ SUCCESS! Dictionary generation completed.")
                print(f"   Wordlist saved to: {cfg['output_file']}")
            else:
                print("\n❌ FAILED! No words generated.")
        
        except Exception as e:
            print(f"\n❌ ERROR: {e}")
            import traceback
            traceback.print_exc()
    
    def quick_generate(self):
        """Quick generation with default settings"""
        print("\n[Quick Generate] Using default settings...")
        
        default_cfg = {
            'base_words': ['admin', 'password', 'user', 'test', '2024'],
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
            'output_file': str(config.WORDLIST_DIR / 'quick_wordlist.txt'),
            'max_words': 5000
        }
        
        self.run_dictionary_generation(default_cfg)
    
    def load_config_file(self):
        """Load configuration from JSON file"""
        print("\n[Load Configuration]")
        filepath = input("Enter config file path: ").strip()
        
        try:
            with open(filepath, 'r') as f:
                self.config_data = json.load(f)
            print(f"✓ Configuration loaded from {filepath}")
            self.show_current_config()
        except FileNotFoundError:
            print(f"❌ File not found: {filepath}")
        except json.JSONDecodeError:
            print(f"❌ Invalid JSON format")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def show_current_config(self):
        """Display current configuration"""
        if not self.config_data:
            print("\n❌ No configuration loaded")
            return
        
        print("\n" + "="*60)
        print("CURRENT CONFIGURATION")
        print("="*60)
        print(json.dumps(self.config_data, indent=2))
        print("="*60)
    
    def show_sample_files(self):
        """Show available sample files"""
        print("\n" + "="*60)
        print("SAMPLE FILES")
        print("="*60)
        
        samples_dir = config.SAMPLES_DIR
        if samples_dir.exists():
            files = list(samples_dir.glob('*'))
            if files:
                for i, f in enumerate(files, 1):
                    size = f.stat().st_size / 1024
                    print(f"{i:2d}. {f.name} ({size:.1f} KB)")
            else:
                print("No sample files found")
        else:
            print("Samples directory not found")
        
        print("="*60)
    
    def placeholder_feature(self, feature_name):
        """Placeholder for features under development"""
        print(f"\n{'='*60}")
        print(f"⚙️  {feature_name}")
        print(f"{'='*60}")
        print("This feature is currently under development.")
        print("It will be available in a future release.")
        print("\nPlanned features:")
        print("  • Hash extraction from Linux/Windows")
        print("  • Dictionary and brute-force attacks")
        print("  • Password strength analysis")
        print("  • Comprehensive security reports")
        print(f"{'='*60}")
    
    def run(self):
        """Main application loop"""
        # Show banner
        self.print_banner()
        
        # Show disclaimer
        if not self.show_disclaimer():
            print("\n❌ You must agree to the terms to use this tool.")
            print("Exiting...")
            return
        
        print("\n✅ Agreement accepted. Welcome!")
        
        # Main loop
        while True:
            try:
                choice = self.show_main_menu()
                
                if choice == '1':
                    self.run_dictionary_generation()
                elif choice == '2':
                    self.quick_generate()
                elif choice in ['3', '4', '5', '6', '7', '8', '9']:
                    self.placeholder_feature("Feature Coming Soon")
                elif choice == '10':
                    self.load_config_file()
                elif choice == '11':
                    self.show_current_config()
                elif choice == '12':
                    self.show_sample_files()
                elif choice == '0':
                    print("\n" + "="*60)
                    print("Thank you for using Password Cracking Suite!")
                    print("Remember: Use ethically and legally! 🔐")
                    print("="*60)
                    break
                else:
                    print("\n❌ Invalid choice. Please select 0-12.")
                
                input("\nPress Enter to continue...")
                
            except KeyboardInterrupt:
                print("\n\n⚠️  Interrupted by user")
                if input("Exit? (y/n): ").lower() == 'y':
                    break
            except Exception as e:
                print(f"\n❌ Unexpected error: {e}")
                import traceback
                traceback.print_exc()


def main():
    """Entry point with argument parsing"""
    parser = argparse.ArgumentParser(
        description='Password Cracking & Credential Attack Suite',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument(
        '--demo',
        action='store_true',
        help='Run in demo mode with sample data'
    )
    
    parser.add_argument(
        '--config',
        type=str,
        help='Load configuration from file'
    )
    
    args = parser.parse_args()
    
    # Create and run application
    app = PasswordCrackingSuite()
    
    if args.demo:
        print("[DEMO MODE] Running with sample configuration...")
        app.print_banner()
        app.quick_generate()
    else:
        app.run()


if __name__ == "__main__":
    main()
