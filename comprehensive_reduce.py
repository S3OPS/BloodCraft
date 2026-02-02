#!/usr/bin/env python3
"""
Comprehensive script to reduce "Blood Archon" usage with more patterns.
"""

import re
from pathlib import Path

def reduce_blood_archon_comprehensive(filepath):
    """Process a file with comprehensive replacements."""
    print(f"Processing: {filepath}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_count = len(re.findall(r'Blood Archon', content))
    print(f"  Original count: {original_count}")
    
    # Patterns to preserve - keep these exact phrases
    preserve_patterns = [
        # Meta/documentation
        r'heir to the Blood Archon bloodline',
        r'About This Version.*?Blood Archon',
        r'"Blood Archon.*?Paradox"',
        r'ALTERNATE storyline.*?Blood Archon',
        
        # Direct identity statements
        r'(I\'m|you\'re|he\'s|she\'s|I am|you are|he is|she is) a Blood Archon',
        r'called a Blood Archon',
        r'known as a Blood Archon',
        
        # First introductions to characters
        r'".*?Reluctant Blood Archon.*?"',
        r'introduced himself as.*?Blood Archon',
        
        # Title discussions
        r'title.*?Blood Archon',
        r'Blood Archon.*?title',
        
        # Geographical/historical specifics  
        r'Blood Archon (from|of|in) the',
        r'American Blood Archons',
        r'European Blood Archons',
        r'named Sanguis.*?Blood Archon',
        
        # Explanatory contexts
        r'what (is|are) (a )?Blood Archons?',
        r'explained.*?Blood Archon',
        r'definition.*?Blood Archon',
        
        # Historical records/formal language
        r'the last Blood Archon, whose',
        r'return of a Blood Archon has',
        r'Blood Archon lineage may have',
        
        # Direct address
        r'"Blood Archon," (she|he|they)',
        r'"Blood Archon\."',
        
        # Bloodline references  
        r'Blood Archon blood',
        r'As in the Blood Archon bloodline',
        r'Sixxx.*?Blood Archon bloodline',
    ]
    
    # Mark lines to preserve
    lines = content.split('\n')
    processed_lines = []
    
    for line in lines:
        # Check if line should be preserved
        should_preserve = False
        for pattern in preserve_patterns:
            if re.search(pattern, line, re.IGNORECASE):
                should_preserve = True
                break
        
        if should_preserve:
            processed_lines.append(line)
            continue
        
        # Apply replacements to this line
        modified = line
        
        # Specific phrase replacements
        replacements = [
            # Descriptive uses with articles
            (r'\bthe powerful Blood Archon\b', 'the powerful mage'),
            (r'\ba powerful Blood Archon\b', 'a powerful mage'),
            (r'\bthe confident Blood Archon\b', 'the confident mage'),
            (r'\ba vampire Blood Archon\b', 'a vampire mage'),
            
            # Possessive forms
            (r'\ba Blood Archon\'s (power|abilities|strength)\b', r'the ancient \1'),
            (r'\bthe Blood Archon\'s (power|abilities|strength)\b', r'the power within'),
            (r'\bBlood Archon\'s first awakening\b', 'such a powerful awakening'),
            
            # With "who/that" clauses
            (r'\bA Blood Archon who\b', 'An heir who'),
            (r'\ba Blood Archon who\b', 'an heir who'),
            (r'\bthe Blood Archon who\b', 'the heir who'),
            (r'\bThe Blood Archon who\b', 'The heir who'),
            
            # Plural forms
            (r'\bAll Blood Archons of\b', 'All heirs of'),
            (r'\ball Blood Archons of\b', 'all heirs of'),
            (r'\bMost Blood Archons\b', 'Most heirs of your lineage'),
            (r'\bmost Blood Archons\b', 'most heirs of your lineage'),
            (r'\bEvery Blood Archon\b', 'Every heir'),
            (r'\bevery Blood Archon\b', 'every heir'),
            (r'\bBlood Archons always\b', 'Heirs of his line always'),
            (r'\bBlood Archons of old\b', 'Those of your lineage'),
            (r'\bThe Blood Archons of old\b', 'Those of your lineage'),
            (r'\bwhen all Blood Archons\b', 'when heirs of the bloodline'),
            
            # "to kill/destroy" patterns
            (r'\bto kill Blood Archons\b', 'to kill those of his lineage'),
            (r'\bkill Blood Archons\b', 'kill those of his lineage'),
            (r'\bdestroy Blood Archons\b', 'destroy those of his lineage'),
            
            # State of being
            (r'\bThe Blood Archon had awakened\b', 'The ancient power had awakened'),
            (r'\bthe Blood Archon had awakened\b', 'the ancient power had awakened'),
            (r'\bBlood Archon has awakened\b', 'heir has awakened'),
            (r'\ba Blood Archon has awakened\b', 'an heir has awakened'),
            
            # Becoming/transformation
            (r'\bpowerful Blood Archon through\b', 'powerful mage through'),
            (r'\bbecome the Blood Archon\b', 'embrace the power within'),
            (r'\bbecoming a Blood Archon\b', 'embracing your true nature'),
            
            # With "destined"
            (r'\bBlood Archon he was destined\b', 'mage he was destined'),
            (r'\bBlood Archon she was destined\b', 'mage she was destined'),
            
            # Relationship patterns
            (r'\bloved her Blood Archon\b', 'loved her charge'),
            (r'\bher Blood Archon too\b', 'her charge too'),
            (r'\bhis Blood Archon\b', 'his charge'),
            (r'\btheir Blood Archon\b', 'their charge'),
            (r'\bmy Blood Archon\b', 'my charge'),
            
            # Comparative forms
            (r'\bnot just a Blood Archon\b', 'not just the power within'),
            (r'\bNot just a Blood Archon\b', 'Not just the power within'),
            (r'\bmore than a Blood Archon\b', 'more than just power'),
            
            # Training/guidance contexts
            (r'\bguiding a newly awakened Blood Archon\b', 'guiding a newly awakened heir'),
            (r'\bguide a Blood Archon\b', 'guide an heir'),
            (r'\bawakened Blood Archon\b', 'awakened heir'),
            
            # Generic references
            (r'\bthe Blood Archon\b', 'the heir'),
            (r'\ba Blood Archon\b', 'an heir'),
            (r'\bA Blood Archon\b', 'An heir'),
            
            # Lineage (when not part of "Blood Archon bloodline")
            (r'\bBlood Archon lineages\b', 'the lineages'),
            (r'\bBlood Archon lineage\b', 'the lineage'),
            
            # Single/only references
            (r'\bonly Blood Archon\b', 'last of my line'),
            (r'\bthe only Blood Archon\b', 'the last of my line'),
            (r'\blast Blood Archon I\b', 'last mage I'),
        ]
        
        for pattern, replacement in replacements:
            modified = re.sub(pattern, replacement, modified)
        
        processed_lines.append(modified)
    
    new_content = '\n'.join(processed_lines)
    new_count = len(re.findall(r'Blood Archon', new_content))
    
    print(f"  New count: {new_count}")
    print(f"  Reduced by: {original_count - new_count}")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return original_count, new_count

def main():
    filepath = Path('/home/runner/work/BloodCraft/BloodCraft/canonical-version/Blood-Craft-Canonical.md')
    
    print("=== Comprehensive Blood Archon Reduction ===\n")
    orig, new = reduce_blood_archon_comprehensive(filepath)
    
    print(f"\n=== FINAL RESULT ===")
    print(f"Reduced from {orig} to {new} instances")
    print(f"Total reduction: {orig - new} ({((orig - new) / orig * 100):.1f}%)")

if __name__ == '__main__':
    main()
