#!/usr/bin/env python3
"""
tabla-abbrv.py - Python script to convert Tabla notation shorthand to long-form notation

Description: This script takes an input abbreviated Tabla bole sentence
             and converts it to the proper long-form notation.

Usage: $ python tabla-abbrv.py "dt dgtkt"
         DhaTi DhaTiGeTuNaKaTa
       
       $ python tabla-abbrv.py "dtdgtkt dtdttkttkttkt"
         DhaTiDhaGeTuNaKaTa DhaTiDhaTheTeKeTeTeKaTeTheTeKeTe
"""

import sys
import re

def convert_to_longform(shorthand_text):
    """
    Convert abbreviated Tabla notation to long-form notation.
    
    Args:
        shorthand_text (str): The abbreviated Tabla notation
        
    Returns:
        str: The converted long-form notation
    """
    # Define the conversion mapping based on the original sed script
    conversions = [
        # Longer patterns first to avoid partial matches
        (r'ttkt', 'TheTeKeTe'),
        (r'dn', 'DhinNa'),
        (r'dd', 'DhaDha'),
        (r'dt', 'DhaTi'),
        (r'tt', 'TheTe'),
        (r'gn', 'GeNa'),
        (r'dg', 'DhaGe'),
        (r'tk', 'TaKe'),
        (r'tn', 'TuNa'),
        (r'kt', 'KaTa'),
        (r'gg', 'GeGe'),
        # Special case for characters after 'd'
        (r'd([A-Za-z])', r'Dha\1'),
        # Single character replacements
        (r'k', 'Ka'),
        (r's', 'S'),
        (r't', 'Ti'),  # Not in original sed but implied for correctness
        (r'd', 'Dha'),  # If 'd' is alone (not followed by a character)
        (r'g', 'Ge'),   # Not in original sed but implied for correctness
        (r'n', 'Na')    # Not in original sed but implied for correctness
    ]
    
    # Apply each conversion rule sequentially
    result = shorthand_text
    for pattern, replacement in conversions:
        result = re.sub(pattern, replacement, result)
    
    return result

def main():
    """Main function to handle command-line arguments and process the shorthand text."""
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <abbreviated notation>")
        print(f"  example: {sys.argv[0]} 'dt dgtkt'")
        print("           DhaTi DhaGeTuNaKaTa")
        sys.exit(1)
    
    shorthand_text = sys.argv[1]
    longform_text = convert_to_longform(shorthand_text)
    print(longform_text)

if __name__ == "__main__":
    main()
