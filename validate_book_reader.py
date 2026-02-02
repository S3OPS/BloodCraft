#!/usr/bin/env python3
"""
Validation script for the Blood Craft book reader system.

This script validates that:
1. The book structure is correctly generated
2. All chapters are properly parsed
3. All page IDs are unique
4. The HTML reader file exists and is valid
"""

import json
import os
import re


def validate_book_structure():
    """Validate the book structure JSON."""
    json_path = 'canonical-version/book-structure.json'
    
    print("="*70)
    print("VALIDATING BOOK STRUCTURE")
    print("="*70)
    
    # Check if file exists
    if not os.path.exists(json_path):
        print("❌ FAIL: book-structure.json not found")
        return False
    
    print(f"✅ Found: {json_path}")
    
    # Load JSON
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print("✅ Valid JSON format")
    except json.JSONDecodeError as e:
        print(f"❌ FAIL: Invalid JSON - {e}")
        return False
    
    # Check required fields
    required_fields = ['title', 'total_chapters', 'total_pages', 'chapters']
    for field in required_fields:
        if field not in data:
            print(f"❌ FAIL: Missing required field '{field}'")
            return False
    print("✅ All required fields present")
    
    # Validate chapter count
    if len(data['chapters']) != data['total_chapters']:
        print(f"❌ FAIL: Chapter count mismatch")
        print(f"   Expected: {data['total_chapters']}, Found: {len(data['chapters'])}")
        return False
    print(f"✅ Chapter count correct: {data['total_chapters']}")
    
    # Validate page count
    total_pages = sum(ch['page_count'] for ch in data['chapters'])
    if total_pages != data['total_pages']:
        print(f"❌ FAIL: Page count mismatch")
        print(f"   Expected: {data['total_pages']}, Calculated: {total_pages}")
        return False
    print(f"✅ Page count correct: {data['total_pages']}")
    
    # Check for unique chapter IDs
    chapter_ids = [ch['id'] for ch in data['chapters']]
    if len(chapter_ids) != len(set(chapter_ids)):
        print("❌ FAIL: Duplicate chapter IDs found")
        return False
    print("✅ All chapter IDs are unique")
    
    # Check for unique page IDs
    all_page_ids = []
    for ch in data['chapters']:
        all_page_ids.extend(ch['page_ids'])
    
    if len(all_page_ids) != len(set(all_page_ids)):
        print("❌ FAIL: Duplicate page IDs found")
        return False
    print(f"✅ All {len(all_page_ids)} page IDs are unique")
    
    # Validate chapter ID format
    chapter_id_pattern = re.compile(r'^ch\d+(_\d+)?$')
    invalid_ids = [ch['id'] for ch in data['chapters'] 
                   if not chapter_id_pattern.match(ch['id'])]
    if invalid_ids:
        print(f"❌ FAIL: Invalid chapter ID format: {invalid_ids}")
        return False
    print("✅ All chapter IDs follow correct format (ch#, ch#_#)")
    
    # Validate page ID format
    page_id_pattern = re.compile(r'^ch\d+(_\d+)?_p\d+$')
    invalid_page_ids = [pid for pid in all_page_ids 
                        if not page_id_pattern.match(pid)]
    if invalid_page_ids:
        print(f"❌ FAIL: Invalid page ID format: {invalid_page_ids[:5]}")
        return False
    print("✅ All page IDs follow correct format (ch#_p#, ch#_#_p#)")
    
    return True


def validate_html_reader():
    """Validate the HTML reader file."""
    html_path = 'canonical-version/Blood-Craft-Reader.html'
    
    print("\n" + "="*70)
    print("VALIDATING HTML READER")
    print("="*70)
    
    # Check if file exists
    if not os.path.exists(html_path):
        print("❌ FAIL: Blood-Craft-Reader.html not found")
        return False
    
    print(f"✅ Found: {html_path}")
    
    # Check file size
    file_size = os.path.getsize(html_path)
    if file_size < 100000:  # Should be at least 100KB
        print(f"❌ FAIL: File too small ({file_size} bytes)")
        return False
    print(f"✅ File size OK: {file_size / 1024 / 1024:.2f} MB")
    
    # Read and validate HTML
    try:
        with open(html_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"❌ FAIL: Could not read file - {e}")
        return False
    
    # Check for essential HTML elements
    essential_elements = [
        '<!DOCTYPE html>',
        '<html',
        '<head>',
        '<title>',
        '<body>',
        'bookData = ',
        'function init()',
        'displayPage',
        'nextPage',
        'previousPage'
    ]
    
    for element in essential_elements:
        if element not in content:
            print(f"❌ FAIL: Missing essential element: {element}")
            return False
    print("✅ All essential HTML elements present")
    
    # Check if book data is embedded
    if 'bookData = {' not in content:
        print("❌ FAIL: Book data not properly embedded")
        return False
    print("✅ Book data properly embedded")
    
    # Check for navigation elements
    navigation_elements = [
        'prevButton',
        'nextButton',
        'pageSelect',
        'chapterList'
    ]
    
    for element in navigation_elements:
        if element not in content:
            print(f"❌ FAIL: Missing navigation element: {element}")
            return False
    print("✅ All navigation elements present")
    
    return True


def validate_source_file():
    """Validate the source markdown file."""
    md_path = 'canonical-version/Blood-Craft-Canonical.md'
    
    print("\n" + "="*70)
    print("VALIDATING SOURCE MARKDOWN")
    print("="*70)
    
    # Check if file exists
    if not os.path.exists(md_path):
        print("❌ FAIL: Blood-Craft-Canonical.md not found")
        return False
    
    print(f"✅ Found: {md_path}")
    
    # Read file
    try:
        with open(md_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"❌ FAIL: Could not read file - {e}")
        return False
    
    # Count chapters
    chapter_pattern = re.compile(r'^#\s*\*\*Chapter\s+', re.MULTILINE)
    chapters = chapter_pattern.findall(content)
    print(f"✅ Found {len(chapters)} chapters in source markdown")
    
    # Check file size
    file_size = os.path.getsize(md_path)
    print(f"✅ Source file size: {file_size / 1024 / 1024:.2f} MB")
    
    # Count words
    word_count = len(content.split())
    print(f"✅ Approximate word count: {word_count:,}")
    
    return True


def validate_generator_script():
    """Validate that the generator script exists and is executable."""
    script_path = 'book_reader_generator.py'
    
    print("\n" + "="*70)
    print("VALIDATING GENERATOR SCRIPT")
    print("="*70)
    
    # Check if file exists
    if not os.path.exists(script_path):
        print("❌ FAIL: book_reader_generator.py not found")
        return False
    
    print(f"✅ Found: {script_path}")
    
    # Check if executable
    if not os.access(script_path, os.R_OK):
        print("❌ FAIL: Script not readable")
        return False
    print("✅ Script is readable")
    
    # Check for essential functions
    try:
        with open(script_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"❌ FAIL: Could not read script - {e}")
        return False
    
    essential_functions = [
        'def parse_narrative',
        'def generate_html_reader',
        'def generate_metadata',
        'class BookStructure'
    ]
    
    for func in essential_functions:
        if func not in content:
            print(f"❌ FAIL: Missing function: {func}")
            return False
    print("✅ All essential functions present")
    
    return True


def main():
    """Run all validations."""
    print("\n" + "="*70)
    print("BLOOD CRAFT BOOK READER VALIDATION")
    print("="*70 + "\n")
    
    results = {
        'Book Structure': validate_book_structure(),
        'HTML Reader': validate_html_reader(),
        'Source Markdown': validate_source_file(),
        'Generator Script': validate_generator_script()
    }
    
    print("\n" + "="*70)
    print("VALIDATION SUMMARY")
    print("="*70)
    
    all_passed = True
    for name, passed in results.items():
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{status} - {name}")
        if not passed:
            all_passed = False
    
    print("="*70)
    
    if all_passed:
        print("\n🎉 ALL VALIDATIONS PASSED!")
        print("\nThe book reader system is working correctly.")
        print("\nNext steps:")
        print("  1. Open canonical-version/Blood-Craft-Reader.html in a browser")
        print("  2. Test navigation between chapters and pages")
        print("  3. Verify bookmark functionality")
        return 0
    else:
        print("\n❌ SOME VALIDATIONS FAILED")
        print("\nPlease review the errors above and fix them.")
        print("\nTo regenerate the reader:")
        print("  python3 book_reader_generator.py")
        return 1


if __name__ == '__main__':
    exit(main())
