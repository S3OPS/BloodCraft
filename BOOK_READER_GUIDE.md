# Blood Craft Interactive Book Reader

## 📖 Overview

The Blood Craft narrative is now available as an interactive book reader with chapter IDs and page IDs for easy navigation. This system makes reading the 48-chapter, 221-page novel as simple and enjoyable as reading a physical book.

## 🚀 Quick Start

### Reading the Book

1. **Open the Reader**: Navigate to `canonical-version/Blood-Craft-Reader.html` in your web browser
2. **Start Reading**: The reader will open to where you left off (or Page 1 on first visit)
3. **Navigate**: Use the navigation buttons or keyboard shortcuts to move through pages
4. **Jump Around**: Use the sidebar or page selector to jump to any chapter or page

### Features

✨ **Interactive Navigation**
- Chapter-based navigation via sidebar
- Page-by-page reading with Previous/Next buttons
- Jump to any page using the page selector
- Keyboard shortcuts (Arrow keys, PageUp/PageDown)

📚 **Book Structure**
- 48 chapters with unique chapter IDs (e.g., `ch1`, `ch2_5`, `ch15`)
- 221 pages with unique page IDs (e.g., `ch1_p1`, `ch2_p3`)
- Approximately 1000 words per page for comfortable reading
- Total: ~197,000 words

🎯 **Smart Features**
- Automatic bookmark - your reading position is saved
- Chapter highlighting - see which chapter you're currently reading
- Page information - know exactly where you are in the book
- Responsive design - works on desktop, tablet, and mobile

## 📋 Book Structure

### Chapter IDs

Each chapter has a unique ID based on its chapter number:
- `ch1` - Chapter 1
- `ch2` - Chapter 2
- `ch2_5` - Chapter 2.5 (Raechelle's Perspective)
- `ch15_5` - Chapter 15.5 (Raechelle's Perspective)

### Page IDs

Each page has a unique ID combining chapter ID and page number:
- `ch1_p1` - Chapter 1, Page 1
- `ch1_p2` - Chapter 1, Page 2
- `ch2_5_p3` - Chapter 2.5, Page 3

### Metadata File

The `canonical-version/book-structure.json` file contains the complete structure:
```json
{
  "title": "Blood Craft: Canonical Version",
  "total_chapters": 48,
  "total_pages": 221,
  "chapters": [
    {
      "id": "ch1",
      "title": "Chapter 1",
      "line_number": 18,
      "page_count": 4,
      "page_start_index": 0,
      "page_ids": ["ch1_p1", "ch1_p2", "ch1_p3", "ch1_p4"]
    },
    ...
  ]
}
```

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
- Global page number (e.g., "Page 15 of 221")
- Unique page ID (e.g., `ch3_p2`)

## 🔧 Regenerating the Reader

If you make changes to the source narrative (`Blood-Craft-Canonical.md`), regenerate the reader:

```bash
cd /home/runner/work/BloodCraft/BloodCraft
python3 book_reader_generator.py
```

This will:
1. Parse the updated narrative
2. Regenerate `canonical-version/Blood-Craft-Reader.html`
3. Update `canonical-version/book-structure.json`

## 📊 Statistics

- **Total Chapters**: 48
- **Total Pages**: 221
- **Total Words**: ~197,000
- **Average Pages per Chapter**: 4.6
- **Words per Page**: ~1,000
- **Reading Time**: ~13-16 hours at average reading speed

## 🎨 Design Features

### Visual Design
- Dark theme optimized for long reading sessions
- Purple gradient scheme matching Blood Craft aesthetic
- Comfortable serif font for extended reading
- Clean, distraction-free interface

### User Experience
- Responsive design for all screen sizes
- Smooth transitions and animations
- Auto-save bookmark feature
- Accessible navigation

## 📖 Reading Tips

1. **First Time Reading**: Start from Chapter 1, Page 1 and enjoy the journey
2. **Returning Reader**: The reader remembers where you left off
3. **Quick Reference**: Use the page selector to jump to specific moments
4. **Chapter Browsing**: Use the sidebar to get an overview of all chapters
5. **Mobile Reading**: The reader works great on phones and tablets

## 🔍 Finding Specific Content

### Using Chapter IDs
If you know the chapter number, use the sidebar to navigate directly. Chapter IDs follow this format:
- Regular chapters: `ch1`, `ch2`, `ch15`, `ch37`
- Half chapters (.5): `ch2_5`, `ch7_5`, `ch15_5`, etc.

### Using Page IDs
Each page has a unique ID combining chapter ID and page number:
- Format: `{chapter_id}_p{page_number}`
- Examples: `ch1_p1`, `ch2_p3`, `ch15_5_p2`

The metadata file (`book-structure.json`) can be queried programmatically to find specific page IDs.

### Programmatic Access
Use the `book_structure_examples.py` script to work with the book structure programmatically:

```bash
python3 book_structure_examples.py
```

This script demonstrates:
- Finding chapters by ID
- Finding pages by ID
- Listing all Raechelle POV chapters
- Getting chapter ranges
- Accessing all chapter and page metadata

See the script for code examples you can adapt for your own use cases.

### Using the Original Markdown
For searching specific text, you can still use the original `Blood-Craft-Canonical.md` file with your text editor's search function.

## 🛠️ Technical Details

### File Structure
```
canonical-version/
├── Blood-Craft-Canonical.md       # Original narrative (source)
├── Blood-Craft-Reader.html        # Interactive reader (generated)
└── book-structure.json            # Book metadata (generated)
```

### Generator Script
`book_reader_generator.py` - Python script that:
- Parses the markdown narrative
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

## 📝 Notes

- The reader is a static HTML file with no external dependencies
- All book content is embedded in the HTML file
- Your reading position is saved in browser localStorage
- Works offline once the HTML file is loaded

## 🤝 Contributing

When adding or modifying chapters in `Blood-Craft-Canonical.md`:

1. Ensure chapter headers follow the format: `# **Chapter [number]**`
2. Run `python3 book_reader_generator.py` to regenerate the reader
3. Test the reader in a browser to ensure proper navigation
4. Commit both the source markdown and generated files

## 📞 Support

For issues or questions about the book reader:
- Check that your browser is up to date
- Try clearing your browser cache
- Regenerate the reader with the generator script
- Ensure the source markdown file hasn't been corrupted

---

**Enjoy reading Blood Craft!** 📚✨
