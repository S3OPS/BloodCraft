#!/usr/bin/env python3
"""
Consolidate Book 4 chapters into a single markdown file.

This script reads all chapter files from canonical-version/new-chapters/book4/
and creates a consolidated Book4-Full.md file for use with the book reader.
"""

import os
import re
from pathlib import Path


def consolidate_book4():
    """Consolidate all Book 4 chapter files into a single markdown file."""
    
    # Paths
    book4_dir = Path('canonical-version/new-chapters/book4')
    output_file = Path('canonical-version/Book4-Full.md')
    
    if not book4_dir.exists():
        print(f"❌ Error: {book4_dir} not found!")
        return False
    
    # Get all chapter files (Chapter-39.md through Chapter-50.md)
    chapter_files = []
    for i in range(39, 51):
        chapter_file = book4_dir / f'Chapter-{i}.md'
        if chapter_file.exists():
            chapter_files.append(chapter_file)
        else:
            print(f"⚠️  Warning: {chapter_file} not found")
    
    if not chapter_files:
        print("❌ Error: No chapter files found!")
        return False
    
    print(f"📚 Found {len(chapter_files)} chapter files")
    
    # Create consolidated file
    with open(output_file, 'w', encoding='utf-8') as out_f:
        # Write header
        out_f.write("# Blood Craft: Book Four - Legacy of Blood\n")
        out_f.write("**Chapters 39-50**\n\n")
        out_f.write("---\n\n")
        out_f.write("> **📖 NOTE:** This is Book Four of the Blood Craft series - The Sequel\n")
        out_f.write("> \n")
        out_f.write("> For Book One (Chapters 1-13), see: `Book1.md`\n")
        out_f.write("> For Book Two (Chapters 14-26), see: `Book2.md`\n")
        out_f.write("> For Book Three (Chapters 27-38), see: `Book3.md`\n\n")
        out_f.write("---\n\n")
        
        # Process each chapter file
        for chapter_file in chapter_files:
            print(f"  Processing {chapter_file.name}...")
            
            with open(chapter_file, 'r', encoding='utf-8') as in_f:
                content = in_f.read()
            
            # Extract chapter number from filename
            match = re.search(r'Chapter-(\d+)', chapter_file.name)
            if match:
                chapter_num = match.group(1)
                
                # Find the actual chapter content (skip the header metadata)
                # Look for the first occurrence of substantial narrative text
                lines = content.split('\n')
                
                # Skip header lines until we find the actual narrative
                start_idx = 0
                for i, line in enumerate(lines):
                    # Skip empty lines, headers, metadata
                    if line.strip() and not line.startswith('#') and not line.startswith('**') and not line.startswith('---') and not line.startswith('>') and not line.startswith('*'):
                        # Check if this looks like narrative text (not just a label)
                        if len(line.strip()) > 50 or (i < len(lines) - 1 and len(lines[i+1].strip()) > 50):
                            start_idx = i
                            break
                
                # Write chapter header
                out_f.write(f"# **Chapter {chapter_num}**\n\n")
                
                # Write chapter content (from first narrative line onward)
                chapter_content = '\n'.join(lines[start_idx:])
                out_f.write(chapter_content.strip())
                out_f.write("\n\n")
                out_f.write("---\n\n")
    
    print(f"\n✅ Consolidated Book 4 created: {output_file}")
    
    # Get file size
    file_size = output_file.stat().st_size
    print(f"   File size: {file_size / 1024:.1f} KB")
    
    return True


def main():
    """Main function."""
    print("🔍 Consolidating Book 4 chapters...\n")
    
    if consolidate_book4():
        print("\n✨ Done! Book4-Full.md is ready for the reader generator.")
    else:
        print("\n❌ Failed to consolidate Book 4 chapters.")
        return 1
    
    return 0


if __name__ == '__main__':
    exit(main())
