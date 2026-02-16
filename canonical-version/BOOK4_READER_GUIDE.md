# Blood Craft Book 4 Interactive Reader Guide

## 📖 Overview

The Book 4 Interactive Reader provides an immersive reading experience for "Blood Craft: Book Four - Legacy of Blood" (Chapters 39-50). This is the sequel to the original trilogy, set five years after the events of Book Three.

## 🚀 Quick Start

### Reading Book 4

1. **Open the Reader**: Navigate to `canonical-version/Book4-Reader.html` in your web browser
2. **Start Reading**: The reader will open to where you left off (or Chapter 39 on first visit)
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
- 12 chapters (Chapters 39-50)
- 62 pages with ~1000 words per page
- Total: ~55,060 words
- Unique IDs for each chapter and page

🎯 **Smart Features**
- Automatic bookmark - saves your reading position
- Chapter and page information on each page
- Responsive design for all devices
- Beautiful dark theme with purple accents

## 📋 Book Details

### Statistics
- **Title**: Blood Craft: Book Four - Legacy of Blood
- **Chapters**: 39-50 (12 chapters total)
- **Pages**: 62 pages
- **Words**: ~55,060 words
- **Reading Time**: ~3.5-4 hours at average reading speed

### Chapter List
- Chapter 39 (4 pages) - Echoes of the Past
- Chapter 40 (4 pages) - The Sanctum
- Chapter 41 (5 pages) - Shadows Rising
- Chapter 42 (6 pages) - The Council's Choice
- Chapter 43 (6 pages) - Ancient Powers
- Chapter 44 (5 pages) - Fractured Alliances
- Chapter 45 (6 pages) - The Price of Power
- Chapter 46 (6 pages) - Into the Abyss
- Chapter 47 (5 pages) - The Devourer's Hunger
- Chapter 48 (5 pages) - Desperate Measures
- Chapter 49 (5 pages) - The Final Stand
- Chapter 50 (5 pages) - Legacy

### Story Overview
Set five years after Book Three, the sequel follows Riven and Raechelle as they face a new threat: an ancient entity called the Devourer that awakens when two Prime Archons exist simultaneously. With their daughter Elena now 15 and training as a Blood Archon, the family must confront this existential threat while navigating the political complexities of the supernatural world.

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
- Global page number (e.g., "Page 15 of 62")
- Unique page ID (e.g., `ch40_p2`)

## 🔧 Regenerating the Reader

If you make changes to the Book 4 chapter files, regenerate the reader:

```bash
cd /home/runner/work/BloodCraft/BloodCraft

# First, consolidate the individual chapter files
python3 scripts/consolidate_book4.py

# Then generate the reader
python3 scripts/book4_reader_generator.py
```

This will:
1. Consolidate all chapter files from `new-chapters/book4/` into `Book4-Full.md`
2. Parse the consolidated file
3. Regenerate `canonical-version/Book4-Reader.html`
4. Update `canonical-version/book4-structure.json`

### What Gets Updated
- Chapter content and structure
- Page divisions (~1000 words per page)
- Chapter and page IDs
- Word counts and statistics

## 📊 Technical Details

### File Structure
```
canonical-version/
├── Book4-Full.md              # Consolidated narrative (Chapters 39-50)
├── Book4-Reader.html          # Interactive reader (generated)
└── book4-structure.json       # Book metadata (generated)

new-chapters/book4/
├── Chapter-39.md              # Individual chapter files
├── Chapter-40.md
├── ...
└── Chapter-50.md
```

### Generator Scripts
1. **`scripts/consolidate_book4.py`** - Combines individual chapter files into Book4-Full.md
   - Reads all Chapter-XX.md files from new-chapters/book4/
   - Creates a single consolidated markdown file
   - Preserves chapter structure and content

2. **`scripts/book4_reader_generator.py`** - Generates the interactive reader
   - Parses Book4-Full.md
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
- Stored under key: `bloodcraft_book4_current_page`
- Separate from other book bookmarks (uses different key)
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

1. **First Time Reading**: Start from Chapter 39, Page 1 and enjoy the sequel!
2. **Returning Reader**: The reader remembers where you left off
3. **Quick Reference**: Use the page selector to jump to specific moments
4. **Chapter Browsing**: Use the sidebar to get an overview of all chapters
5. **Mobile Reading**: The reader works great on phones and tablets

## 🔍 Finding Specific Content

### Using Chapter IDs
Chapter IDs follow this format:
- Chapters 39-50: `ch39`, `ch40`, ..., `ch50`
- Format: `ch{number}`

### Using Page IDs
Each page has a unique ID combining chapter ID and page number:
- Format: `{chapter_id}_p{page_number}`
- Examples: `ch39_p1`, `ch40_p2`, `ch50_p5`

The metadata file (`book4-structure.json`) can be queried programmatically to find specific page IDs.

## 📞 Support

For issues or questions about the Book 4 reader:
- Ensure your browser is up to date
- Try clearing your browser cache
- Regenerate the reader with the generator scripts
- Check that Book4-Full.md and chapter files haven't been corrupted

## 🔄 Related Files

- **Book 1 Reader**: `canonical-version/Blood-Craft-Reader.html`
- **Book 1 Guide**: See `BOOK_READER_GUIDE.md` in root directory
- **Source Content**: `canonical-version/new-chapters/book4/Chapter-XX.md`
- **Consolidation Script**: `scripts/consolidate_book4.py`
- **Generator Script**: `scripts/book4_reader_generator.py`

## 🌟 What Makes Book 4 Special

Book 4 is the sequel that takes place five years after the original trilogy. Key features:

- **Mature Characters**: Riven and Raechelle have established themselves as leaders
- **New Generation**: Elena (age 15) represents the next generation of Blood Archons
- **Epic Threat**: The Devourer is an ancient, reality-consuming entity
- **Prime Archon Lore**: Deep dive into Prime Archon history and powers
- **Higher Stakes**: Not just Nocturne, but the entire supernatural world at risk

---

**Enjoy reading Book 4: Legacy of Blood!** 📚✨
