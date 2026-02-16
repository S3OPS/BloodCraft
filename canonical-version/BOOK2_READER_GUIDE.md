# Blood Craft Book 2 Interactive Reader Guide

## 📖 Overview

The Book 2 Interactive Reader provides an immersive reading experience for "Blood Craft: Book Two - The Rising Conflict" (Chapters 14-26). This guide explains how to use the reader and regenerate it if needed.

## 🚀 Quick Start

### Reading Book 2

1. **Open the Reader**: Navigate to `canonical-version/Book2-Reader.html` in your web browser
2. **Start Reading**: The reader will open to where you left off (or Chapter 14 on first visit)
3. **Navigate**: Use the navigation buttons, sidebar, or keyboard shortcuts
4. **Enjoy**: The reader automatically saves your position

### Features

✨ **Interactive Navigation**
- Chapter-based navigation via sidebar
- Page-by-page reading with Previous/Next buttons
- Jump to any page using the page selector dropdown
- Keyboard shortcuts (Arrow keys, PageUp/PageDown)
- Active chapter highlighting in sidebar

📚 **Book Structure**
- 13 chapters (Chapters 14-26)
- 56 pages with ~1000 words per page
- Total: ~49,695 words
- Unique IDs for each chapter and page

🎯 **Smart Features**
- Automatic bookmark - saves your reading position
- Chapter and page information on each page
- Responsive design for all devices
- Beautiful dark theme with purple accents

## 📋 Book Details

### Statistics
- **Title**: Blood Craft: Book Two - The Rising Conflict
- **Chapters**: 14-26 (13 chapters total)
- **Pages**: 56 pages
- **Words**: ~49,695 words
- **Reading Time**: ~3-4 hours at average reading speed

### Chapter List
- Chapter 14 (4 pages) - The Crimson Ball
- Chapter 15 (3 pages) - Shadows and Sleep
- Chapter 16 (3 pages)
- Chapter 17 (5 pages)
- Chapter 18 (5 pages)
- Chapter 19 (3 pages)
- Chapter 20 (4 pages)
- Chapter 21 (9 pages)
- Chapter 22 (4 pages)
- Chapter 23 (5 pages)
- Chapter 24 (3 pages)
- Chapter 25 (2 pages)
- Chapter 26 (6 pages)

## 🎮 Navigation Guide

### Using the Reader Interface

1. **Sidebar Navigation**
   - Click any chapter title to jump to that chapter
   - Active chapter is highlighted
   - Shows page count for each chapter

2. **Page Navigation**
   - **Previous Button**: Go to the previous page
   - **Next Button**: Go to the next page
   - **Page Selector**: Dropdown to jump to any page number

3. **Keyboard Shortcuts**
   - `→` or `PageDown`: Next page
   - `←` or `PageUp`: Previous page

### Page Information Display

Each page shows:
- Chapter title
- Current page number within the chapter (e.g., "Page 2 of 5")
- Global page number (e.g., "Page 15 of 56")
- Unique page ID (e.g., `ch15_p2`)

## 🔧 Regenerating the Reader

If you make changes to `Book2.md`, regenerate the reader:

```bash
cd /home/runner/work/BloodCraft/BloodCraft
python3 scripts/book2_reader_generator.py
```

This will:
1. Parse the updated `Book2.md` file
2. Regenerate `canonical-version/Book2-Reader.html`
3. Update `canonical-version/book2-structure.json`

### What Gets Updated
- Chapter content and structure
- Page divisions (~1000 words per page)
- Chapter and page IDs
- Word counts and statistics

## 📊 Technical Details

### File Structure
```
canonical-version/
├── Book2.md                   # Source narrative (Chapters 14-26)
├── Book2-Reader.html          # Interactive reader (generated)
└── book2-structure.json       # Book metadata (generated)
```

### Generator Script
`scripts/book2_reader_generator.py` - Python script that:
- Parses the Book2.md markdown file
- Identifies chapters using regex patterns
- Splits chapters into pages (~1000 words each)
- Assigns unique IDs to chapters and pages
- Generates the HTML reader with embedded data
- Creates the metadata JSON file

### Browser Compatibility
The reader works in all modern browsers:
- Chrome/Edge (recommended)
- Firefox
- Safari
- Opera

### Data Storage
- Your reading position is saved in browser localStorage
- Stored under key: `bloodcraft_book2_current_page`
- Separate from Book 1 bookmark (uses different key)
- Persists across browser sessions
- No external dependencies required

## 🎨 Design Features

### Visual Design
- Dark theme optimized for long reading sessions
- Purple gradient scheme matching Blood Craft aesthetic
- Comfortable serif font (Georgia) for extended reading
- Clean, distraction-free interface
- Smooth transitions and animations

### User Experience
- Responsive design for all screen sizes
- Auto-save bookmark feature
- Accessible navigation
- Fast loading (all content embedded)
- Works offline once loaded

## 📝 Reading Tips

1. **First Time Reading**: Start from Chapter 14, Page 1 and enjoy the journey
2. **Returning Reader**: The reader remembers where you left off
3. **Quick Reference**: Use the page selector to jump to specific moments
4. **Chapter Browsing**: Use the sidebar to get an overview of all chapters
5. **Mobile Reading**: The reader works great on phones and tablets

## 🔍 Finding Specific Content

### Using Chapter IDs
Chapter IDs follow this format:
- Regular chapters: `ch14`, `ch15`, `ch26`
- Format: `ch{number}`

### Using Page IDs
Each page has a unique ID combining chapter ID and page number:
- Format: `{chapter_id}_p{page_number}`
- Examples: `ch14_p1`, `ch15_p2`, `ch26_p6`

The metadata file (`book2-structure.json`) can be queried programmatically to find specific page IDs.

## 📞 Support

For issues or questions about the Book 2 reader:
- Ensure your browser is up to date
- Try clearing your browser cache
- Regenerate the reader with the generator script
- Check that Book2.md hasn't been corrupted

## 🔄 Related Files

- **Book 1 Reader**: `canonical-version/Blood-Craft-Reader.html`
- **Book 1 Guide**: See `BOOK_READER_GUIDE.md` in root directory
- **Source Content**: `canonical-version/Book2.md`
- **Generator Script**: `scripts/book2_reader_generator.py`

---

**Enjoy reading Book 2: The Rising Conflict!** 📚✨
