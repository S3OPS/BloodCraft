#!/usr/bin/env python3
"""
Blood Craft Book Reader Generator

This script parses the Blood-Craft-Canonical.md file and generates an interactive
HTML book reader with chapter IDs and page IDs for easy navigation.
"""

import re
import json
import os
from typing import List, Dict, Tuple


class BookStructure:
    """Represents the structure of the book with chapters and pages."""
    
    def __init__(self, title: str = "Blood Craft: Canonical Version"):
        self.title = title
        self.chapters: List[Dict] = []
        self.total_pages = 0
        
    def add_chapter(self, chapter_id: str, chapter_title: str, content: str, line_number: int):
        """Add a chapter to the book structure."""
        # Split content into pages (approximately 1000 words per page)
        pages = self._split_into_pages(content)
        
        chapter = {
            'id': chapter_id,
            'title': chapter_title,
            'line_number': line_number,
            'pages': [],
            'page_start_index': self.total_pages
        }
        
        for i, page_content in enumerate(pages):
            page_id = f"{chapter_id}_p{i+1}"
            chapter['pages'].append({
                'id': page_id,
                'page_number': i + 1,
                'global_page_number': self.total_pages + 1,
                'content': page_content,
                'word_count': len(page_content.split())
            })
            self.total_pages += 1
        
        self.chapters.append(chapter)
    
    def _split_into_pages(self, content: str, words_per_page: int = 1000) -> List[str]:
        """Split content into pages based on word count and paragraph boundaries."""
        if not content.strip():
            return [content]
        
        paragraphs = content.split('\n\n')
        pages = []
        current_page = []
        current_word_count = 0
        
        for para in paragraphs:
            para_word_count = len(para.split())
            
            # If adding this paragraph exceeds the page limit and we have content
            if current_word_count + para_word_count > words_per_page and current_page:
                pages.append('\n\n'.join(current_page))
                current_page = [para]
                current_word_count = para_word_count
            else:
                current_page.append(para)
                current_word_count += para_word_count
        
        # Add the last page
        if current_page:
            pages.append('\n\n'.join(current_page))
        
        return pages if pages else [content]
    
    def get_chapter_by_id(self, chapter_id: str) -> Dict:
        """Get chapter by ID."""
        for chapter in self.chapters:
            if chapter['id'] == chapter_id:
                return chapter
        return None
    
    def get_page_by_global_number(self, page_number: int) -> Tuple[Dict, Dict]:
        """Get page and its chapter by global page number."""
        for chapter in self.chapters:
            for page in chapter['pages']:
                if page['global_page_number'] == page_number:
                    return chapter, page
        return None, None


def parse_narrative(file_path: str) -> BookStructure:
    """Parse the Blood Craft narrative markdown file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lines = content.split('\n')
    book = BookStructure()
    
    # Pattern to match chapter headers
    chapter_pattern = re.compile(r'^#\s*\*\*Chapter\s+(.+?)\*\*')
    
    current_chapter_id = None
    current_chapter_title = None
    current_chapter_content = []
    current_chapter_line = 0
    
    for i, line in enumerate(lines):
        match = chapter_pattern.match(line)
        
        if match:
            # Save previous chapter if exists
            if current_chapter_id:
                content_text = '\n'.join(current_chapter_content)
                book.add_chapter(current_chapter_id, current_chapter_title, 
                               content_text, current_chapter_line)
            
            # Start new chapter
            chapter_num = match.group(1).strip()
            current_chapter_title = f"Chapter {chapter_num}"
            
            # Create clean chapter ID
            clean_num = re.sub(r'[^0-9.]', '', chapter_num.split('-')[0].strip())
            current_chapter_id = f"ch{clean_num.replace('.', '_')}"
            current_chapter_content = []
            current_chapter_line = i + 1
        elif current_chapter_id:
            current_chapter_content.append(line)
    
    # Add the last chapter
    if current_chapter_id:
        content_text = '\n'.join(current_chapter_content)
        book.add_chapter(current_chapter_id, current_chapter_title, 
                       content_text, current_chapter_line)
    
    return book


def generate_html_reader(book: BookStructure, output_path: str):
    """Generate an interactive HTML book reader."""
    
    # Convert book structure to JSON for JavaScript
    book_data = {
        'title': book.title,
        'total_chapters': len(book.chapters),
        'total_pages': book.total_pages,
        'chapters': [
            {
                'id': ch['id'],
                'title': ch['title'],
                'page_count': len(ch['pages']),
                'page_start_index': ch['page_start_index'],
                'pages': [
                    {
                        'id': p['id'],
                        'page_number': p['page_number'],
                        'global_page_number': p['global_page_number'],
                        'content': p['content'],
                        'word_count': p['word_count']
                    }
                    for p in ch['pages']
                ]
            }
            for ch in book.chapters
        ]
    }
    
    html_template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ TITLE }} - Interactive Reader</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Georgia', 'Times New Roman', serif;
            line-height: 1.8;
            background: linear-gradient(135deg, #1e1e2e 0%, #2d1b3d 100%);
            color: #e0e0e0;
            min-height: 100vh;
        }
        
        .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 20px;
            display: grid;
            grid-template-columns: 280px 1fr;
            gap: 30px;
            min-height: 100vh;
        }
        
        /* Sidebar */
        .sidebar {
            background: rgba(0, 0, 0, 0.4);
            padding: 25px;
            border-radius: 12px;
            backdrop-filter: blur(10px);
            height: fit-content;
            position: sticky;
            top: 20px;
            max-height: calc(100vh - 40px);
            overflow-y: auto;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        }
        
        .sidebar h2 {
            color: #b794f6;
            margin-bottom: 20px;
            font-size: 1.3em;
            text-align: center;
            border-bottom: 2px solid #8b5cf6;
            padding-bottom: 10px;
        }
        
        .chapter-list {
            list-style: none;
        }
        
        .chapter-item {
            margin-bottom: 8px;
        }
        
        .chapter-link {
            display: block;
            padding: 10px 12px;
            color: #c4b5fd;
            text-decoration: none;
            border-radius: 6px;
            transition: all 0.3s;
            font-size: 0.95em;
            border-left: 3px solid transparent;
        }
        
        .chapter-link:hover {
            background: rgba(139, 92, 246, 0.2);
            border-left-color: #8b5cf6;
            transform: translateX(5px);
        }
        
        .chapter-link.active {
            background: rgba(139, 92, 246, 0.3);
            border-left-color: #a78bfa;
            font-weight: bold;
        }
        
        .chapter-pages {
            font-size: 0.85em;
            color: #9ca3af;
            margin-left: 12px;
        }
        
        /* Main Content */
        .main-content {
            background: rgba(255, 255, 255, 0.05);
            padding: 50px;
            border-radius: 12px;
            backdrop-filter: blur(10px);
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
            min-height: 600px;
        }
        
        .book-header {
            text-align: center;
            margin-bottom: 40px;
            padding-bottom: 25px;
            border-bottom: 3px solid #8b5cf6;
        }
        
        .book-title {
            font-size: 2.5em;
            color: #b794f6;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
        }
        
        .book-stats {
            color: #9ca3af;
            font-size: 0.95em;
        }
        
        .page-header {
            margin-bottom: 30px;
            padding-bottom: 15px;
            border-bottom: 2px solid rgba(139, 92, 246, 0.3);
        }
        
        .chapter-title {
            font-size: 2em;
            color: #a78bfa;
            margin-bottom: 8px;
        }
        
        .page-info {
            color: #9ca3af;
            font-size: 0.9em;
        }
        
        .page-content {
            font-size: 1.1em;
            line-height: 1.9;
            white-space: pre-wrap;
            text-align: justify;
            color: #e5e7eb;
        }
        
        /* Navigation */
        .navigation {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: 40px;
            padding-top: 30px;
            border-top: 2px solid rgba(139, 92, 246, 0.3);
        }
        
        .nav-button {
            padding: 12px 25px;
            background: linear-gradient(135deg, #8b5cf6 0%, #6d28d9 100%);
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-size: 1em;
            transition: all 0.3s;
            box-shadow: 0 4px 15px rgba(139, 92, 246, 0.3);
        }
        
        .nav-button:hover:not(:disabled) {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(139, 92, 246, 0.5);
        }
        
        .nav-button:disabled {
            background: #4b5563;
            cursor: not-allowed;
            opacity: 0.5;
        }
        
        .page-selector {
            display: flex;
            align-items: center;
            gap: 15px;
        }
        
        .page-selector label {
            color: #c4b5fd;
            font-weight: 500;
        }
        
        .page-selector select {
            padding: 8px 15px;
            background: rgba(139, 92, 246, 0.2);
            color: #e5e7eb;
            border: 1px solid #8b5cf6;
            border-radius: 6px;
            font-size: 0.95em;
            cursor: pointer;
        }
        
        /* Responsive */
        @media (max-width: 1024px) {
            .container {
                grid-template-columns: 1fr;
            }
            
            .sidebar {
                position: static;
                max-height: 400px;
            }
            
            .main-content {
                padding: 30px;
            }
        }
        
        @media (max-width: 640px) {
            .book-title {
                font-size: 1.8em;
            }
            
            .chapter-title {
                font-size: 1.5em;
            }
            
            .page-content {
                font-size: 1em;
            }
            
            .navigation {
                flex-direction: column;
                gap: 15px;
            }
        }
        
        /* Loading */
        .loading {
            text-align: center;
            padding: 60px;
            color: #9ca3af;
            font-size: 1.2em;
        }
        
        /* Scrollbar */
        .sidebar::-webkit-scrollbar {
            width: 8px;
        }
        
        .sidebar::-webkit-scrollbar-track {
            background: rgba(0, 0, 0, 0.2);
            border-radius: 4px;
        }
        
        .sidebar::-webkit-scrollbar-thumb {
            background: #8b5cf6;
            border-radius: 4px;
        }
        
        .sidebar::-webkit-scrollbar-thumb:hover {
            background: #a78bfa;
        }
    </style>
</head>
<body>
    <div class="container">
        <aside class="sidebar">
            <h2>📚 Table of Contents</h2>
            <ul class="chapter-list" id="chapterList"></ul>
        </aside>
        
        <main class="main-content">
            <div class="book-header">
                <h1 class="book-title">{{ TITLE }}</h1>
                <div class="book-stats">
                    <span id="totalChapters"></span> chapters • 
                    <span id="totalPages"></span> pages • 
                    <span id="totalWords"></span> words
                </div>
            </div>
            
            <div id="pageContent">
                <div class="loading">Loading book...</div>
            </div>
            
            <div class="navigation">
                <button class="nav-button" id="prevButton" onclick="previousPage()">
                    ← Previous
                </button>
                
                <div class="page-selector">
                    <label for="pageSelect">Jump to page:</label>
                    <select id="pageSelect" onchange="jumpToPage(this.value)"></select>
                </div>
                
                <button class="nav-button" id="nextButton" onclick="nextPage()">
                    Next →
                </button>
            </div>
        </main>
    </div>
    
    <script>
        // Book data embedded in JavaScript
        const bookData = {{ BOOK_DATA }};
        let currentPageIndex = 0;
        
        // Initialize the reader
        function init() {
            // Set book stats
            document.getElementById('totalChapters').textContent = bookData.total_chapters;
            document.getElementById('totalPages').textContent = bookData.total_pages;
            
            // Calculate total words
            let totalWords = 0;
            bookData.chapters.forEach(ch => {
                ch.pages.forEach(p => totalWords += p.word_count);
            });
            document.getElementById('totalWords').textContent = totalWords.toLocaleString();
            
            // Build chapter list
            buildChapterList();
            
            // Build page selector
            buildPageSelector();
            
            // Load saved position or start from beginning
            const savedPage = localStorage.getItem('bloodcraft_current_page');
            if (savedPage) {
                currentPageIndex = parseInt(savedPage) - 1;
            }
            
            // Display first page
            displayPage(currentPageIndex);
        }
        
        function buildChapterList() {
            const list = document.getElementById('chapterList');
            list.innerHTML = '';
            
            bookData.chapters.forEach((chapter, chIndex) => {
                const li = document.createElement('li');
                li.className = 'chapter-item';
                
                const link = document.createElement('a');
                link.href = '#';
                link.className = 'chapter-link';
                link.dataset.chapterId = chapter.id;
                link.innerHTML = `
                    ${chapter.title}
                    <div class="chapter-pages">${chapter.page_count} page${chapter.page_count > 1 ? 's' : ''}</div>
                `;
                
                link.onclick = (e) => {
                    e.preventDefault();
                    jumpToChapter(chIndex);
                };
                
                li.appendChild(link);
                list.appendChild(li);
            });
        }
        
        function buildPageSelector() {
            const select = document.getElementById('pageSelect');
            select.innerHTML = '';
            
            for (let i = 0; i < bookData.total_pages; i++) {
                const option = document.createElement('option');
                option.value = i;
                option.textContent = `Page ${i + 1}`;
                select.appendChild(option);
            }
        }
        
        function displayPage(pageIndex) {
            if (pageIndex < 0 || pageIndex >= bookData.total_pages) return;
            
            currentPageIndex = pageIndex;
            
            // Find the chapter and page
            let chapter, page;
            for (const ch of bookData.chapters) {
                const pageInChapter = ch.pages.find(p => p.global_page_number === pageIndex + 1);
                if (pageInChapter) {
                    chapter = ch;
                    page = pageInChapter;
                    break;
                }
            }
            
            if (!chapter || !page) return;
            
            // Update content
            const contentDiv = document.getElementById('pageContent');
            contentDiv.innerHTML = `
                <div class="page-header">
                    <h2 class="chapter-title">${chapter.title}</h2>
                    <div class="page-info">
                        Page ${page.page_number} of ${chapter.page_count} in this chapter • 
                        Page ${page.global_page_number} of ${bookData.total_pages} overall • 
                        ID: <code>${page.id}</code>
                    </div>
                </div>
                <div class="page-content">${escapeHtml(page.content)}</div>
            `;
            
            // Update navigation buttons
            document.getElementById('prevButton').disabled = pageIndex === 0;
            document.getElementById('nextButton').disabled = pageIndex === bookData.total_pages - 1;
            
            // Update page selector
            document.getElementById('pageSelect').value = pageIndex;
            
            // Highlight current chapter in sidebar
            document.querySelectorAll('.chapter-link').forEach(link => {
                link.classList.remove('active');
                if (link.dataset.chapterId === chapter.id) {
                    link.classList.add('active');
                }
            });
            
            // Save current position
            localStorage.setItem('bloodcraft_current_page', page.global_page_number);
            
            // Scroll to top
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }
        
        function escapeHtml(text) {
            const div = document.createElement('div');
            div.textContent = text;
            return div.innerHTML;
        }
        
        function nextPage() {
            if (currentPageIndex < bookData.total_pages - 1) {
                displayPage(currentPageIndex + 1);
            }
        }
        
        function previousPage() {
            if (currentPageIndex > 0) {
                displayPage(currentPageIndex - 1);
            }
        }
        
        function jumpToPage(pageIndex) {
            displayPage(parseInt(pageIndex));
        }
        
        function jumpToChapter(chapterIndex) {
            const chapter = bookData.chapters[chapterIndex];
            if (chapter && chapter.pages.length > 0) {
                displayPage(chapter.pages[0].global_page_number - 1);
            }
        }
        
        // Keyboard navigation
        document.addEventListener('keydown', (e) => {
            if (e.key === 'ArrowRight' || e.key === 'PageDown') {
                e.preventDefault();
                nextPage();
            } else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {
                e.preventDefault();
                previousPage();
            }
        });
        
        // Initialize on load
        window.addEventListener('DOMContentLoaded', init);
    </script>
</body>
</html>'''
    
    # Replace template variables
    html_content = html_template.replace('{{ TITLE }}', book.title)
    html_content = html_content.replace('{{ BOOK_DATA }}', json.dumps(book_data, ensure_ascii=False))
    
    # Write HTML file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✅ HTML reader generated: {output_path}")
    print(f"   Total chapters: {len(book.chapters)}")
    print(f"   Total pages: {book.total_pages}")


def generate_metadata(book: BookStructure, output_path: str):
    """Generate metadata JSON file for the book structure."""
    metadata = {
        'title': book.title,
        'total_chapters': len(book.chapters),
        'total_pages': book.total_pages,
        'chapters': [
            {
                'id': ch['id'],
                'title': ch['title'],
                'line_number': ch['line_number'],
                'page_count': len(ch['pages']),
                'page_start_index': ch['page_start_index'],
                'page_ids': [p['id'] for p in ch['pages']]
            }
            for ch in book.chapters
        ]
    }
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Metadata generated: {output_path}")


def main():
    """Main function to generate the book reader."""
    # Paths
    narrative_path = 'canonical-version/Blood-Craft-Canonical.md'
    output_dir = 'canonical-version'
    html_output = os.path.join(output_dir, 'Blood-Craft-Reader.html')
    metadata_output = os.path.join(output_dir, 'book-structure.json')
    
    print("🔍 Parsing Blood Craft narrative...")
    book = parse_narrative(narrative_path)
    
    print(f"\n📊 Book Structure:")
    print(f"   Title: {book.title}")
    print(f"   Chapters: {len(book.chapters)}")
    print(f"   Total Pages: {book.total_pages}")
    print(f"   Average Pages per Chapter: {book.total_pages / len(book.chapters):.1f}")
    
    print(f"\n🎨 Generating HTML reader...")
    generate_html_reader(book, html_output)
    
    print(f"\n📋 Generating metadata...")
    generate_metadata(book, metadata_output)
    
    print(f"\n✨ Done! Open '{html_output}' in your browser to read the book.")
    print(f"   The reader supports:")
    print(f"   • Chapter navigation via sidebar")
    print(f"   • Page-by-page reading")
    print(f"   • Jump to any page")
    print(f"   • Keyboard navigation (arrow keys)")
    print(f"   • Automatic bookmark (saves your position)")


if __name__ == '__main__':
    main()
