# Quick Reference Guide for Developers

This is a quick reference for common development tasks. For detailed information, see the full documentation files.

---

## 📚 Documentation Map

- **[CONTRIBUTING.md](CONTRIBUTING.md)** - Full contribution guidelines (read first!)
- **[canonical-version/DEVELOPMENT.md](canonical-version/DEVELOPMENT.md)** - Canonical version specifics
- **[CHAPTER_TEMPLATE.md](CHAPTER_TEMPLATE.md)** - Template for new chapters

---

## 🚀 Quick Start

### First Time Setup
```bash
# Clone the repository
git clone https://github.com/S3OPS/BloodCraft.git
cd BloodCraft

# Read the documentation
1. Read CONTRIBUTING.md
2. Read version-specific DEVELOPMENT.md
3. Review WORKFLOW.md for parallel development
```

### Before You Start Working
```bash
# Pull latest changes
git pull origin main

# Check current status
- Review canonical-version/Chapter-Summary-and-Timeline.md
```

---

## 📋 Common Tasks

### Adding a New Chapter

**Canonical Version**:
```bash
# 1. Edit the main novel file
canonical-version/Blood-Craft-Canonical.md

# 2. Update chapter summary
canonical-version/Chapter-Summary-and-Timeline.md

# 3. Update word count in
canonical-version/README.md

# 4. Commit with descriptive message
git commit -m "Add Chapter XX - Title"
```

### Updating World-Building

World-building changes affect the fundamental rules and systems of the story universe. 

**Note**: The Paradox Version is now in a separate repository ([BloodCraftParadox](https://github.com/S3OPS/BloodCraftParadox)). If you need to synchronize world-building changes, you'll need to apply them there separately.

**Common World-Building Elements**:
- Blood magic mechanics (regeneration, energy costs, limitations)
- Nocturne geography and locations (districts, landmarks, safe zones)
- Supernatural faction structures (hierarchy, powers, territories)
- Magic system rules (how it works, what's possible/impossible)
- Historical events and lore (ancient battles, founding stories)
- Creature types and abilities (vampires, shifters, etc.)
- Political systems and governance

**Update Process**:
```bash
# 1. Update the canonical version
canonical-version/Blood-Craft-Canonical.md (affected chapters)

# 2. Update summary
canonical-version/Chapter-Summary-and-Timeline.md

# 3. Verify consistency across all references
grep -r "element_name" canonical-version/

# 4. Commit with clear message
git commit -m "Update blood magic mechanics

- Clarified regeneration rules
- Updated energy cost system
- Affects Chapters X, Y, Z"
```

**World-Building Update Checklist**:
- [ ] Rule change is consistent with established lore
- [ ] Updated in ALL relevant chapters in both versions
- [ ] Chapter summaries reflect the change
- [ ] No contradictions introduced
- [ ] Change enhances story, doesn't just add complexity
- [ ] Reader understanding is maintained
- [ ] Future chapters won't be contradicted

**Example Updates**:
- **Magic System**: "Blood regeneration now requires 24 hours instead of 12"
- **Geography**: "Added the Crimson Quarter as a neutral zone in Nocturne"
- **Factions**: "Clarified the Council's authority structure"
- **Creatures**: "Expanded werewolf transformation triggers and limitations"

### Enhance Romance

Romance is central to the canonical version. Updates should maintain the version's identity while deepening emotional connections.

**Core Romance Elements**:
- Riven and Raechelle's fundamental connection
- Key relationship milestones (first kiss, first intimacy, commitment)
- Core emotional beats (trust, vulnerability, devotion)
- Dom/sub dynamic foundation (consent, care, boundaries)
- Character growth through the relationship

**Canonical Version Romance Approach**:
- Straightforward romantic progression
- Clear emotional communication
- Uplifting and affirming intimate scenes
- Power fantasy elements (protective, strong bond)
- Satisfying, uncomplicated love story
- Focus on joy and connection

**Enhancement Process**:
```bash
# 1. Identify romance scene or element to enhance
# - Deepening emotional connection
# - Adding intimate moments
# - Developing Dom/sub dynamics
# - Character vulnerability

# 2. Update in canonical version
canonical-version/Blood-Craft-Canonical.md (specific chapters)

# 3. Ensure romance serves character development
# Not just added for its own sake

# 4. Commit with appropriate message
git commit -m "Enhance intimate scene in Chapter X

- Deepened emotional vulnerability
- Advanced Dom/sub dynamic naturally
- Focus on joy and connection"
```

### Updating a Character's Core Traits

```bash
# 1. Update in the canonical version file
canonical-version/Blood-Craft-Canonical.md

# 2. Update chapter summaries if needed
canonical-version/Chapter-Summary-and-Timeline.md

# 3. Check for consistency across all appearances
grep -r "character_name" canonical-version/

# 4. Commit with clear message
git commit -m "Update Raechelle's backstory

- Added training history details
- Maintains consistency throughout"
```

---

## ✅ Quick Checklists

### Before Committing Any Changes

- [ ] Spell-check and grammar review completed
- [ ] Character voices remain consistent
- [ ] Timeline consistency verified (if applicable)
- [ ] World-building rules maintained
- [ ] Both versions updated if applicable
- [ ] Documentation updated (Chapter summaries, READMEs)
- [ ] File formatting is consistent
- [ ] Commit message clearly indicates version(s) affected

### Adding New Chapters

- [ ] Follows version-specific guidelines (check DEVELOPMENT.md)
- [ ] Balances action, politics, character development, romance
- [ ] Deepens Dom/sub relationship organically
- [ ] Continues supernatural world-building appropriately
- [ ] Supporting characters have meaningful moments
- [ ] Romance scenes serve character development
- [ ] Chapter-Summary-and-Timeline.md updated
- [ ] Word count updated in README.md
- [ ] Quality standards met (grammar, flow, pacing)

### Paradox Version Specific (Pre-Twist Chapters)

- [ ] 1-2 subtle hints planted
- [ ] Surface story is compelling on its own
- [ ] Hints are missable on first read
- [ ] Raechelle's knowledge carefully balanced
- [ ] Psychological tension maintained

---

## 🎨 Version Identity Quick Reference

### Canonical Version - Key Elements

✅ **Include**:
- Clear heroic progression
- Straightforward moral framework
- Satisfying power fantasy
- Romantic supernatural themes
- Uplifting, hopeful tone

❌ **Avoid**:
- Excessive moral ambiguity
- Unreliable narration
- Overly dark or cynical tones
- Complicated philosophical questions

---

## 🔄 Commit Message Format

```bash
# Format
Brief description

Detailed explanation
- Specific change 1
- Specific change 2

# Examples
Add Chapter 31 - New Threats
Enhance foreshadowing in Chapter 12
Update blood magic mechanics
```

---

## 📊 Current Status

**As of January 2026**:

| Version | Status | Chapters | Word Count | Location |
|---------|--------|----------|------------|----------|
| Canonical | ✅ Complete | 38 | ~157,000 | This repository |
| Paradox | ✅ Complete | 30 | ~97,000 | [Separate repository](https://github.com/S3OPS/BloodCraftParadox) |

**Current Focus**: Canonical version complete; ready for Book 2 development or sequel planning

---

## 🔍 Consistency Requirements

### Core Elements to Maintain
- Blood magic mechanics and rules
- Nocturne geography and locations
- Core character traits and backstories
- Timeline of major events
- Supernatural faction structures
- Magic system fundamentals

### Note on Paradox Version
The Paradox Version is now in a separate repository: [BloodCraftParadox](https://github.com/S3OPS/BloodCraftParadox). If world-building changes need to be synchronized, they must be applied in that repository separately.

---

## 💡 Quick Tips

### Do's ✅

- Commit frequently with clear messages
- Review DEVELOPMENT.md when unsure
- Update documentation alongside content
- Maintain consistency in world-building
- Test changes before committing

### Don'ts ❌

- Don't introduce world-building contradictions
- Don't forget to update documentation
- Don't commit without checking for errors
- Don't make changes that conflict with established lore

---

## 📖 Where to Find Things

**World-Building Information**:
- canonical-version/Chapter-Summary-and-Timeline.md
- Early chapters of Blood-Craft-Canonical.md

**Character Information**:
- canonical-version/Chapter-Summary-and-Timeline.md
- canonical-version/DEVELOPMENT.md (character sections)

**Creative Guidelines**:
- canonical-version/DEVELOPMENT.md
- CONTRIBUTING.md (general guidelines)

**Quick Reference**:
- This file (common tasks)

**Version Comparison**:
- docs/Comparison-Guide.md
- README.md (main overview)

---

## ❓ Common Questions

**Q: Where is the Paradox Version?**
A: The Paradox Version has been moved to a separate repository: [github.com/S3OPS/BloodCraftParadox](https://github.com/S3OPS/BloodCraftParadox). This repository now focuses exclusively on the Canonical Version.

**Q: Should I synchronize world-building changes with the Paradox version?**
A: If you're making fundamental changes to blood magic rules, Nocturne geography, or core lore, consider whether they should be synchronized with the Paradox version in its separate repository. However, this is now optional since they're maintained separately.

**Q: What if I want to add content that doesn't fit the canonical version's style?**
A: Consider if it can be adapted to fit the canonical version's heroic, romantic style. If not, it might be better suited for a different project or the Paradox version repository.

---

## 🚨 Emergency Troubleshooting

**Issue**: Git conflict
- Solution: Review the conflict, resolve based on canonical version's guidelines

**Issue**: Forgot which file to edit
- Solution: Check file path - everything is in `canonical-version/`

**Issue**: Character acting inconsistently
- Solution: Review previous chapters, check DEVELOPMENT.md character guidelines

**Issue**: Can't remember world-building rule
- Solution: Search Chapter-Summary-and-Timeline.md in canonical-version

**Issue**: Unsure about creative direction
- Solution: Check canonical-version/DEVELOPMENT.md for guidelines

---

## 📞 Need More Help?

- **Full guidelines**: [CONTRIBUTING.md](CONTRIBUTING.md)
- **Canonical specifics**: [canonical-version/DEVELOPMENT.md](canonical-version/DEVELOPMENT.md)
- **Chapter template**: [CHAPTER_TEMPLATE.md](CHAPTER_TEMPLATE.md)

---

**Last Updated**: January 2026

Happy developing! 🩸✨
