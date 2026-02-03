#!/usr/bin/env python3
"""
Script to reduce usage of "Blood Archon" in narrative files.
Replaces with varied alternatives while keeping contextually important uses.
"""

import re
import sys
from pathlib import Path

# Patterns to KEEP "Blood Archon" - these are contextually important
KEEP_PATTERNS = [
    r'heir to the Blood Archon bloodline',  # About bloodline itself
    r'About This Version.*Blood Archon',  # Documentation
    r'"Blood Archon.*Paradox"',  # Alternate version reference
    r'I\'m a Blood Archon',  # Self-introduction
    r'you\'re a Blood Archon',  # Direct statement of identity
    r'He\'s a Blood Archon',  # Direct statement
    r'She\'s a Blood Archon',  # Direct statement  
    r'called? a Blood Archon',  # Explanation of title
    r'known as? a Blood Archon',  # Explanation of title
    r'title.*Blood Archon',  # Discussion of the title itself
    r'Blood Archon.*title',  # Discussion of the title itself
    r'named Sanguis',  # Historical figure
    r'Blood Archon from the',  # Geographic/historical context
    r'American Blood Archons',  # Geographic description
    r'European Blood Archons',  # Geographic description
    r'what is a Blood Archon',  # Explanatory
    r'what are Blood Archons',  # Explanatory
]

# Replacement patterns with varied alternatives
REPLACEMENTS = [
    # Pattern: "a Blood Archon's power" -> varied alternatives
    (r'\ba Blood Archon\'s power\b', 'the ancient power'),
    (r'\bthe Blood Archon\'s power\b', 'the power within'),
    
    # Pattern: "Blood Archon's first awakening"
    (r'\ba Blood Archon\'s first awakening\b', 'such a powerful first awakening'),
    (r'\bthe Blood Archon\'s first awakening\b', 'the first awakening'),
    
    # Pattern: "Blood Archon who/that"
    (r'\bA Blood Archon who\b', 'An heir who'),
    (r'\ba Blood Archon who\b', 'an heir who'),
    (r'\bThe Blood Archon who\b', 'The heir who'),
    (r'\bthe Blood Archon who\b', 'the heir who'),
    
    # Pattern: "Most Blood Archons"
    (r'\bMost Blood Archons\b', 'Most heirs of your lineage'),
    (r'\bmost Blood Archons\b', 'most heirs of your lineage'),
    
    # Pattern: "Every Blood Archon"
    (r'\bEvery Blood Archon\b', 'Every heir'),
    (r'\bevery Blood Archon\b', 'every heir'),
    
    # Pattern: "Blood Archon had awakened"
    (r'\bThe Blood Archon had awakened\b', 'The ancient power had awakened'),
    (r'\bthe Blood Archon had awakened\b', 'the ancient power had awakened'),
    
    # Pattern: "to kill Blood Archons"
    (r'\bto kill Blood Archons\b', 'to kill those of his lineage'),
    
    # Pattern: "Blood Archon lineages" (not preceded by "to the" or "heir to")
    (r'(?<!to the )(?<!heir to the )\bBlood Archon lineages\b', 'the lineages'),
    
    # Pattern: "Only Blood Archon" / "last Blood Archon"
    (r'\bonly Blood Archon\b', 'last of my line'),
    (r'\blast Blood Archon\b', 'last mage'),
    
    # Pattern: "Blood Archons of old"
    (r'\bBlood Archons of old\b', 'Those of your lineage'),
    (r'\bThe Blood Archons of old\b', 'Those of your lineage'),
    
    # Pattern: "powerful Blood Archon"
    (r'\bpowerful Blood Archon\b', 'powerful mage'),
    
    # Pattern: "confident Blood Archon"
    (r'\bconfident Blood Archon\b', 'confident mage'),
    
    # Pattern: "Blood Archons always"
    (r'\bBlood Archons always\b', 'Heirs of his line always'),
    
    # Pattern: "loved her Blood Archon"
    (r'\bloved her Blood Archon\b', 'loved her charge'),
    
    # Pattern: "not just a Blood Archon"
    (r'\bnot just a Blood Archon\b', 'not just the power within'),
    (r'\bNot just a Blood Archon\b', 'Not just the power within'),
    
    # Pattern: "when familiars fell"
    (r'\btheir charges\. I\'d watched the tragedy unfold with my own mentor, Serafine, who\'d loved her Blood Archon\b', 
     'their charges. I\'d watched the tragedy unfold with my own mentor, Serafine, who\'d loved her charge'),
]

def should_keep_line(line):
    """Check if a line contains a pattern we want to keep."""
    for pattern in KEEP_PATTERNS:
        if re.search(pattern, line, re.IGNORECASE):
            return True
    return False

def reduce_blood_archon_in_file(filepath):
    """Process a single file to reduce Blood Archon usage."""
    print(f"Processing: {filepath}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_count = len(re.findall(r'Blood Archon', content))
    print(f"  Original count: {original_count}")
    
    # Split into lines for context-aware processing
    lines = content.split('\n')
    modified_lines = []
    
    for line in lines:
        # Check if this line should be preserved
        if should_keep_line(line):
            modified_lines.append(line)
            continue
        
        # Apply replacements
        modified_line = line
        for pattern, replacement in REPLACEMENTS:
            modified_line = re.sub(pattern, replacement, modified_line)
        
        modified_lines.append(modified_line)
    
    new_content = '\n'.join(modified_lines)
    new_count = len(re.findall(r'Blood Archon', new_content))
    print(f"  New count: {new_count}")
    print(f"  Reduced by: {original_count - new_count}")
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return original_count, new_count

def main():
    if len(sys.argv) > 1:
        files = [Path(arg) for arg in sys.argv[1:]]
    else:
        # Default: process all narrative files
        base_path = Path('/home/runner/work/BloodCraft/BloodCraft/canonical-version')
        files = []
        files.extend(base_path.glob('Book*.md'))
        files.append(base_path / 'Blood-Craft-Canonical.md')
        files.extend((base_path / 'new-chapters').glob('Chapter*.md'))
        files.extend((base_path / 'new-chapters').glob('chapter*.md'))
    
    total_original = 0
    total_new = 0
    
    for filepath in files:
        if filepath.exists():
            orig, new = reduce_blood_archon_in_file(filepath)
            total_original += orig
            total_new += new
        else:
            print(f"File not found: {filepath}")
    
    print(f"\n=== SUMMARY ===")
    print(f"Total original count: {total_original}")
    print(f"Total new count: {total_new}")
    print(f"Total reduced by: {total_original - total_new}")
    print(f"Reduction rate: {((total_original - total_new) / total_original * 100):.1f}%")

if __name__ == '__main__':
    main()
