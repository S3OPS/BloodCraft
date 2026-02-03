# Auto-Regeneration Quick Start

## 🚀 How It Works

```
┌─────────────────────────────────────────────────────────────────┐
│  Developer/Author makes changes to:                             │
│  📝 canonical-version/Blood-Craft-Canonical.md                  │
└────────────────────┬────────────────────────────────────────────┘
                     │
                     │ Commits & Pushes to main/master
                     ▼
┌─────────────────────────────────────────────────────────────────┐
│  🤖 GitHub Actions Workflow Triggers                            │
│  (.github/workflows/regenerate-html.yml)                        │
└────────────────────┬────────────────────────────────────────────┘
                     │
                     │ Automatically runs:
                     ▼
┌─────────────────────────────────────────────────────────────────┐
│  1. python3 book_reader_generator.py                            │
│  2. Generates new HTML and JSON                                 │
│  3. Commits the changes back                                    │
│  4. Pushes to repository                                        │
└────────────────────┬────────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────────┐
│  ✅ Updated Files:                                              │
│  📄 canonical-version/Blood-Craft-Reader.html (always in sync!) │
│  📄 canonical-version/book-structure.json (always in sync!)     │
└─────────────────────────────────────────────────────────────────┘
```

## 📋 What Gets Updated Automatically?

| File | Description | Auto-Updated? |
|------|-------------|---------------|
| `Blood-Craft-Canonical.md` | Source markdown (you edit this) | ❌ Manual |
| `Blood-Craft-Reader.html` | Interactive reader | ✅ **Automatic** |
| `book-structure.json` | Chapter/page metadata | ✅ **Automatic** |

## 🎯 Benefits

### For Authors/Editors
- ✅ **Just edit the markdown** - HTML updates automatically
- ✅ **No manual steps** - No need to run scripts
- ✅ **Never out of sync** - HTML always matches source
- ✅ **Version controlled** - All changes tracked in git

### For Readers
- ✅ **Always up-to-date** - HTML reader has latest content
- ✅ **Reliable** - No stale or outdated reader
- ✅ **Consistent** - Same content across all formats

### For Developers
- ✅ **Automated workflow** - Set it and forget it
- ✅ **PR verification** - Checks HTML sync on pull requests
- ✅ **Clear errors** - Helpful messages if something's wrong

## 🔍 How to Verify It's Working

### Check Recent Workflow Runs
1. Go to the repository on GitHub
2. Click the "Actions" tab
3. Look for "Regenerate HTML Reader" workflow
4. Recent runs show success/failure status

### After Making Changes
1. Edit `canonical-version/Blood-Craft-Canonical.md`
2. Commit and push to main/master branch
3. Wait ~1-2 minutes for workflow to complete
4. Check that `Blood-Craft-Reader.html` was updated

### Manual Trigger (If Needed)
1. Go to "Actions" tab on GitHub
2. Select "Regenerate HTML Reader" workflow
3. Click "Run workflow" button
4. Select branch and click "Run workflow"

## ⚠️ Important Notes

### The `[skip ci]` Tag
When the workflow commits HTML updates, it includes `[skip ci]` in the commit message. This prevents:
- ❌ Infinite loops (workflow triggering itself)
- ❌ Unnecessary builds
- ✅ Clean, predictable workflow runs

### Only Triggers On
- ✅ Changes to `canonical-version/Blood-Craft-Canonical.md`
- ✅ On `main` or `master` branch
- ✅ Or manual trigger via Actions tab
- ❌ Does NOT trigger on other files
- ❌ Does NOT trigger on other branches (unless manually run)

### Pull Requests
A separate workflow (`verify-html-sync.yml`) runs on PRs to:
- Check if HTML needs regeneration
- Provide helpful comments if out of sync
- Does NOT auto-commit (that happens after merge)

## 🛠️ Manual Regeneration (Optional)

If you want to regenerate locally before committing:

```bash
# Run the generator
python3 book_reader_generator.py

# Commit the changes
git add canonical-version/Blood-Craft-Reader.html
git add canonical-version/book-structure.json
git commit -m "Regenerate HTML reader"
git push
```

This is **optional** - the workflow will do it automatically anyway!

## 📚 More Information

- **Detailed docs**: [AUTO_HTML_GENERATION.md](AUTO_HTML_GENERATION.md)
- **Reader guide**: [BOOK_READER_GUIDE.md](BOOK_READER_GUIDE.md)
- **Generator script**: [book_reader_generator.py](book_reader_generator.py)
- **Workflow files**: `.github/workflows/regenerate-html.yml` and `verify-html-sync.yml`

## ❓ Troubleshooting

### HTML not updating?
- Check Actions tab for workflow failures
- Ensure changes were pushed to main/master
- Verify file path is correct
- Try manual trigger from Actions tab

### Workflow failing?
- Check workflow logs in Actions tab
- Verify Python script has no errors
- Ensure repository has write permissions
- Check for syntax errors in YAML files

### Need help?
- Review [AUTO_HTML_GENERATION.md](AUTO_HTML_GENERATION.md) for detailed troubleshooting
- Check recent commits for "Auto-regenerate HTML reader" messages
- Look at workflow logs for specific error messages
