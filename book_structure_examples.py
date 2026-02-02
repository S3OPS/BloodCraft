#!/usr/bin/env python3
"""
Example script showing how to use the book structure programmatically.

This demonstrates how to work with chapter IDs and page IDs.
"""

import json

def load_book_structure(json_path='canonical-version/book-structure.json'):
    """Load the book structure from JSON."""
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def find_chapter_by_id(book_data, chapter_id):
    """Find a chapter by its ID."""
    for chapter in book_data['chapters']:
        if chapter['id'] == chapter_id:
            return chapter
    return None


def find_page_by_id(book_data, page_id):
    """Find a page by its ID (returns chapter and page info)."""
    chapter_id = page_id.split('_p')[0]
    chapter = find_chapter_by_id(book_data, chapter_id)
    
    if not chapter:
        return None, None
    
    for page in chapter['page_ids']:
        if page == page_id:
            page_number = int(page.split('_p')[1])
            return chapter, page_number
    
    return None, None


def get_chapter_range(book_data, start_chapter_id, end_chapter_id):
    """Get all chapters in a range."""
    chapters = []
    collecting = False
    
    for chapter in book_data['chapters']:
        if chapter['id'] == start_chapter_id:
            collecting = True
        
        if collecting:
            chapters.append(chapter)
        
        if chapter['id'] == end_chapter_id:
            break
    
    return chapters


def list_all_raechelle_pov_chapters(book_data):
    """Find all Raechelle POV chapters (numbered with .5)."""
    raechelle_chapters = []
    for chapter in book_data['chapters']:
        if "Raechelle" in chapter['title'] or "_5" in chapter['id']:
            raechelle_chapters.append(chapter)
    return raechelle_chapters


def get_reading_statistics(book_data):
    """Calculate reading statistics."""
    total_pages = book_data['total_pages']
    total_chapters = book_data['total_chapters']
    
    # Estimate reading time (250 words per minute, avg 1000 words per page)
    estimated_minutes = (total_pages * 1000) / 250
    estimated_hours = estimated_minutes / 60
    
    return {
        'total_chapters': total_chapters,
        'total_pages': total_pages,
        'estimated_reading_time_hours': round(estimated_hours, 1),
        'average_pages_per_chapter': round(total_pages / total_chapters, 1)
    }


def main():
    """Demo the usage of chapter IDs and page IDs."""
    
    # Load the book structure
    print("Loading book structure...")
    book = load_book_structure()
    
    print(f"\n{'='*60}")
    print(f"BLOOD CRAFT BOOK STRUCTURE")
    print(f"{'='*60}\n")
    
    # Display basic info
    print(f"Title: {book['title']}")
    stats = get_reading_statistics(book)
    print(f"Chapters: {stats['total_chapters']}")
    print(f"Pages: {stats['total_pages']}")
    print(f"Estimated Reading Time: {stats['estimated_reading_time_hours']} hours")
    print(f"Average Pages per Chapter: {stats['average_pages_per_chapter']}")
    
    # Example 1: Find a specific chapter by ID
    print(f"\n{'-'*60}")
    print("EXAMPLE 1: Find Chapter by ID")
    print(f"{'-'*60}")
    chapter = find_chapter_by_id(book, 'ch1')
    if chapter:
        print(f"Chapter ID: {chapter['id']}")
        print(f"Title: {chapter['title']}")
        print(f"Pages: {chapter['page_count']}")
        print(f"Page IDs: {', '.join(chapter['page_ids'])}")
    
    # Example 2: Find a specific page by ID
    print(f"\n{'-'*60}")
    print("EXAMPLE 2: Find Page by ID")
    print(f"{'-'*60}")
    chapter, page_num = find_page_by_id(book, 'ch2_p3')
    if chapter:
        print(f"Page ID: ch2_p3")
        print(f"Chapter: {chapter['title']}")
        print(f"Page {page_num} of {chapter['page_count']} in this chapter")
    
    # Example 3: List all Raechelle POV chapters
    print(f"\n{'-'*60}")
    print("EXAMPLE 3: All Raechelle POV Chapters")
    print(f"{'-'*60}")
    raechelle_chapters = list_all_raechelle_pov_chapters(book)
    print(f"Found {len(raechelle_chapters)} Raechelle POV chapters:\n")
    for ch in raechelle_chapters:
        print(f"  • {ch['id']}: {ch['title']} ({ch['page_count']} pages)")
    
    # Example 4: Get a range of chapters
    print(f"\n{'-'*60}")
    print("EXAMPLE 4: Chapter Range (Book 1 - Chapters 1-5)")
    print(f"{'-'*60}")
    chapters = get_chapter_range(book, 'ch1', 'ch5')
    print(f"Chapters {chapters[0]['id']} to {chapters[-1]['id']}:\n")
    for ch in chapters:
        print(f"  • {ch['id']}: {ch['title']} ({ch['page_count']} pages)")
    
    # Example 5: Show all chapters with IDs
    print(f"\n{'-'*60}")
    print("EXAMPLE 5: Complete Chapter Listing")
    print(f"{'-'*60}\n")
    for i, ch in enumerate(book['chapters'], 1):
        print(f"{i:2}. ID: {ch['id']:8} | {ch['title'][:50]:50} | {ch['page_count']} pages")
    
    print(f"\n{'='*60}")
    print("For more information, see BOOK_READER_GUIDE.md")
    print(f"{'='*60}\n")


if __name__ == '__main__':
    main()
