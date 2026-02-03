# Automatic HTML Reader Generation

## Overview

This repository includes automated generation of the interactive HTML reader from the canonical markdown file. Whenever changes are made to `canonical-version/Blood-Craft-Canonical.md`, the HTML reader is automatically regenerated to stay in sync.

## How It Works

### GitHub Actions Workflow

The automation is powered by a GitHub Actions workflow (`.github/workflows/regenerate-html.yml`) that:

1. **Triggers automatically** when:
   - Changes are pushed to `canonical-version/Blood-Craft-Canonical.md` on the main/master branch
   - Manually triggered via the Actions tab

2. **Executes the generator**:
   - Runs `book_reader_generator.py` to parse the markdown
   - Generates updated `Blood-Craft-Reader.html`
   - Updates `book-structure.json` metadata

3. **Commits changes automatically**:
   - If the HTML or JSON files changed, commits them back to the repository
   - Uses `[skip ci]` to prevent infinite loops

### Manual Generation

You can also manually regenerate the HTML reader at any time:

```bash
python3 book_reader_generator.py
```

This will:
- Parse `canonical-version/Blood-Craft-Canonical.md`
- Generate `canonical-version/Blood-Craft-Reader.html`
- Create `canonical-version/book-structure.json` with chapter metadata

## Generated Files

### Blood-Craft-Reader.html
An interactive, single-file HTML reader with:
- Chapter navigation sidebar
- Page-by-page reading experience (≈1000 words/page)
- Keyboard shortcuts (arrow keys for navigation)
- Automatic bookmarking (saves your reading position)
- Jump-to-page functionality
- Responsive design for desktop and mobile

### book-structure.json
Metadata file containing:
- Chapter titles and IDs
- Page breakdown for each chapter
- Word counts
- Navigation structure

## Benefits

### ✅ Always in Sync
The HTML reader is automatically regenerated whenever the source markdown changes, ensuring readers always have the latest version.

### ✅ No Manual Work
Authors and contributors don't need to remember to run the generator script - it happens automatically.

### ✅ Version Control
All generated files are tracked in git, so you can see the full history of changes.

### ✅ Easy to Review
Pull requests will show the HTML changes, making it easy to verify the generation worked correctly.

## Workflow Details

### Trigger Conditions

**Automatic triggers:**
- Push to `main` or `master` branch
- Only when `canonical-version/Blood-Craft-Canonical.md` is modified

**Manual trigger:**
- Go to the "Actions" tab in GitHub
- Select "Regenerate HTML Reader" workflow
- Click "Run workflow"

### Permissions

The workflow uses `GITHUB_TOKEN` which has write permissions to commit back to the repository. No additional secrets or configuration needed.

### Skip CI Tag

Commits made by the workflow include `[skip ci]` to prevent infinite loops:
- The workflow commits HTML updates
- GitHub Actions sees `[skip ci]` and doesn't trigger another workflow run
- Prevents unnecessary builds

## Troubleshooting

### HTML Not Regenerating?

1. **Check if the workflow ran:**
   - Go to the "Actions" tab in GitHub
   - Look for recent "Regenerate HTML Reader" runs
   - Check logs for errors

2. **Verify the file path:**
   - Workflow only triggers for `canonical-version/Blood-Craft-Canonical.md`
   - Changes to other files won't trigger regeneration

3. **Manual trigger:**
   - You can always manually run the workflow from the Actions tab
   - Or run `python3 book_reader_generator.py` locally

### Workflow Failing?

Check the workflow logs for:
- Python errors in the generator script
- Git permission issues
- File path problems

## Development

### Modifying the Generator

If you need to change how the HTML is generated:

1. Edit `book_reader_generator.py`
2. Test locally: `python3 book_reader_generator.py`
3. Verify the HTML looks correct
4. Commit changes to the script
5. The workflow will use the updated script on next trigger

### Changing Trigger Conditions

Edit `.github/workflows/regenerate-html.yml` to:
- Add more file paths to watch
- Change branch restrictions
- Modify commit messages
- Add notifications

### Testing the Workflow

You can test without modifying the canonical file:
1. Go to Actions tab
2. Select "Regenerate HTML Reader"
3. Click "Run workflow" button
4. Select the branch and run

## Related Files

- `.github/workflows/regenerate-html.yml` - GitHub Actions workflow
- `book_reader_generator.py` - Python script that generates HTML
- `canonical-version/Blood-Craft-Canonical.md` - Source markdown
- `canonical-version/Blood-Craft-Reader.html` - Generated HTML
- `canonical-version/book-structure.json` - Generated metadata

## See Also

- [BOOK_READER_GUIDE.md](BOOK_READER_GUIDE.md) - How to use the HTML reader
- [CONTRIBUTING.md](CONTRIBUTING.md) - Contributing guidelines
- [README.md](README.md) - Main repository documentation
