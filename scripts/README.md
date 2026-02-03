# Scripts Directory

This directory contains utility scripts for the BloodCraft project.

## Available Scripts

### Book Reader Generation

**`book_reader_generator.py`**
- Generates the interactive HTML book reader from the markdown source
- Automatically creates page breaks, chapter navigation, and bookmarking features
- See [BOOK_READER_GUIDE.md](../BOOK_READER_GUIDE.md) for usage details

**`validate_book_reader.py`**
- Validates the generated book reader for correctness
- Checks chapter IDs, page structure, and navigation integrity

**`book_structure_examples.py`**
- Example code demonstrating how to work with chapter and page IDs
- Useful for developers working on book reader features

### Content Processing

**`reduce_blood_archon.py`**
- Utility script for reducing "Blood Archon" references in the text
- Used for content editing and consistency

**`comprehensive_reduce.py`**
- Comprehensive text reduction and processing script
- Multi-purpose content transformation utility

## Usage

Run scripts from the repository root directory:

```bash
# Generate the book reader
python scripts/book_reader_generator.py

# Validate the book reader
python scripts/validate_book_reader.py

# View examples
python scripts/book_structure_examples.py
```

## Requirements

These scripts require Python 3.6+ and use only standard library modules (no external dependencies required).

## Documentation

For more information about the book reader system:
- [BOOK_READER_GUIDE.md](../BOOK_READER_GUIDE.md) - User guide for the interactive reader
- [AUTO_HTML_GENERATION.md](../AUTO_HTML_GENERATION.md) - Automatic regeneration system
- [AUTO_REGENERATION_QUICKSTART.md](../AUTO_REGENERATION_QUICKSTART.md) - Quick start guide
