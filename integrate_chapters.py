#!/usr/bin/env python3
"""
Script to integrate 4 new chapters into Blood-Craft-Canonical.md at strategic points.
This will:
1. Insert new chapters at specific locations
2. Renumber all subsequent chapters
3. Update chapter references in "End of Chapter" markers
"""

import re
import sys

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filename, content):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

def renumber_chapters(content, start_line_num, increment, skip_first_instance=False):
    """Renumber chapters starting from start_line_num by adding increment
    
    Args:
        content: The file content
        start_line_num: Chapter number to start renumbering from
        increment: Amount to add to chapter numbers
        skip_first_instance: If True, skip the first instance of start_line_num (both header and end marker)
    """
    lines = content.split('\n')
    modified = False
    seen_start_num_header = False
    seen_start_num_end = False
    
    for i in range(len(lines)):
        # Match chapter headings like "# **Chapter 15**"
        match = re.match(r'^# \*\*Chapter (\d+)\*\*$', lines[i])
        if match:
            old_num = int(match.group(1))
            if old_num >= start_line_num:
                # If skip_first_instance and this is the first time we see start_line_num, skip it
                if skip_first_instance and old_num == start_line_num and not seen_start_num_header:
                    seen_start_num_header = True
                    continue
                    
                new_num = old_num + increment
                lines[i] = f'# **Chapter {new_num}**'
                modified = True
                print(f"  Renumbered Chapter {old_num} -> {new_num}")
        
        # Match end markers like "*End of Chapter 15*"
        match = re.match(r'^\*End of Chapter (\d+)\*$', lines[i])
        if match:
            old_num = int(match.group(1))
            if old_num >= start_line_num:
                # If skip_first_instance and this is the first time we see start_line_num end marker, skip it
                if skip_first_instance and old_num == start_line_num and not seen_start_num_end:
                    seen_start_num_end = True
                    continue
                    
                new_num = old_num + increment
                lines[i] = f'*End of Chapter {new_num}*'
                modified = True
    
    return '\n'.join(lines)

def insert_chapter_after(content, after_chapter_num, new_chapter_file, new_chapter_num):
    """Insert a new chapter after the specified chapter number"""
    
    # Read the new chapter content
    new_chapter = read_file(new_chapter_file)
    
    # Find the insertion point (after "*End of Chapter X*")
    search_pattern = f'*End of Chapter {after_chapter_num}*'
    
    lines = content.split('\n')
    insertion_index = None
    
    for i, line in enumerate(lines):
        if line.strip() == search_pattern:
            # Found the end marker, insert after the next blank line
            insertion_index = i + 1
            # Skip any blank lines after the marker
            while insertion_index < len(lines) and lines[insertion_index].strip() == '':
                insertion_index += 1
            break
    
    if insertion_index is None:
        print(f"ERROR: Could not find insertion point after Chapter {after_chapter_num}")
        return content
    
    # Insert the new chapter
    print(f"\nInserting new Chapter {new_chapter_num} after old Chapter {after_chapter_num} at line {insertion_index}")
    
    # Add blank lines before and after for spacing
    lines.insert(insertion_index, '')
    lines.insert(insertion_index + 1, new_chapter.strip())
    lines.insert(insertion_index + 2, '')
    
    return '\n'.join(lines)

def main():
    print("=" * 60)
    print("Blood Craft Chapter Integration Script")
    print("=" * 60)
    
    original_file = 'canonical-version/Blood-Craft-Canonical.md'
    backup_file = 'canonical-version/Blood-Craft-Canonical.md.backup'
    
    # Read original content
    print(f"\n1. Reading {original_file}...")
    content = read_file(original_file)
    
    # Create backup
    print(f"2. Creating backup at {backup_file}...")
    write_file(backup_file, content)
    
    # Integration plan:
    # - Insert NEW Ch 4 after old Ch 3  -> Renumber old 4+ to 5+
    # - Insert NEW Ch 7 after new Ch 6 (old 5) -> Renumber old 6+ to 8+
    # - Insert NEW Ch 11 after new Ch 10 (old 8) -> Renumber old 9+ to 12+
    # - Insert NEW Ch 15 after new Ch 14 (old 11) -> Renumber old 12+ to 16+
    
    print("\n" + "=" * 60)
    print("Step 1: Insert NEW Chapter 4 after old Chapter 3")
    print("=" * 60)
    content = insert_chapter_after(content, 3, 'NEW_CHAPTER_4_FAMILIAR_BOND.md', 4)
    print("Renumbering old chapters 4+ to 5+ (skip the new Ch 4)...")
    content = renumber_chapters(content, 4, 1, skip_first_instance=True)
    
    print("\n" + "=" * 60)
    print("Step 2: Insert NEW Chapter 7 after new Chapter 6 (old 5)")
    print("=" * 60)
    content = insert_chapter_after(content, 6, 'NEW_CHAPTER_7_TRAINING_IN_SHADOWS.md', 7)
    print("Renumbering chapters 7+ to 8+ (but skip the new Ch 7)...")
    content = renumber_chapters(content, 7, 1, skip_first_instance=True)
    
    print("\n" + "=" * 60)
    print("Step 3: Insert NEW Chapter 11 after new Chapter 10 (old 8)")
    print("=" * 60)
    content = insert_chapter_after(content, 10, 'NEW_CHAPTER_11_GATEWAY_CITY.md', 11)
    print("Renumbering chapters 11+ to 12+ (but skip the new Ch 11)...")
    content = renumber_chapters(content, 11, 1, skip_first_instance=True)
    
    print("\n" + "=" * 60)
    print("Step 4: Insert NEW Chapter 15 after new Chapter 14 (old 11)")
    print("=" * 60)
    content = insert_chapter_after(content, 14, 'NEW_CHAPTER_15_ACADEMY_TRIALS.md', 15)
    print("Renumbering chapters 15+ to 16+ (but skip the new Ch 15)...")
    content = renumber_chapters(content, 15, 1, skip_first_instance=True)
    
    # Write the integrated content
    print(f"\n5. Writing integrated content to {original_file}...")
    write_file(original_file, content)
    
    print("\n" + "=" * 60)
    print("Integration Complete!")
    print("=" * 60)
    print(f"\nBackup saved at: {backup_file}")
    print(f"Updated file: {original_file}")
    print("\nNew chapter structure:")
    print("  Chapters 1-3: Original")
    print("  Chapter 4: NEW - The Familiar Bond")
    print("  Chapters 5-6: Original 4-5")
    print("  Chapter 7: NEW - Training in Shadows")
    print("  Chapters 8-10: Original 6-8")
    print("  Chapter 11: NEW - The Gateway City")
    print("  Chapters 12-14: Original 9-11")
    print("  Chapter 15: NEW - The Academy Trials")
    print("  Chapters 16-30: Original 12-26")

if __name__ == '__main__':
    main()
