# Quick Reference Guide for Developers

This is a quick reference for common development tasks. For detailed information, see the full documentation files.

---

## 📚 Documentation Map

- **[CONTRIBUTING.md](CONTRIBUTING.md)** - Full contribution guidelines (read first!)
- **[WORKFLOW.md](WORKFLOW.md)** - How to work on both versions in parallel
- **[canonical-version/DEVELOPMENT.md](canonical-version/DEVELOPMENT.md)** - Canonical version specifics
- **[paradox-version/DEVELOPMENT.md](paradox-version/DEVELOPMENT.md)** - Paradox version specifics

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

# Check status of both versions
- Review canonical-version/Chapter-Summary-and-Timeline.md
- Review paradox-version/Chapter-Summary-and-Timeline.md
```

---

## 📋 Common Tasks

### Adding a New Chapter to One Version

**Canonical Version**:
```bash
# 1. Edit the main novel file
canonical-version/Blood-Craft-Canonical.md

# 2. Update chapter summary
canonical-version/Chapter-Summary-and-Timeline.md

# 3. Update word count in
canonical-version/README.md

# 4. Commit with version tag
git commit -m "[Canonical] Add Chapter XX - Title"
```

**Paradox Version**:
```bash
# 1. Edit the main novel file
paradox-version/Blood-Craft-Paradox.md

# 2. Update chapter summary
paradox-version/Chapter-Summary-and-Timeline.md

# 3. Update word count in
paradox-version/README.md

# 4. Commit with version tag
git commit -m "[Paradox] Add Chapter XX - Title"
```

### Updating World-Building (Both Versions)

World-building changes affect the fundamental rules and systems of the story universe. These MUST be consistent across both versions.

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
# 1. Update both versions consistently
canonical-version/Blood-Craft-Canonical.md (affected chapters)
paradox-version/Blood-Craft-Paradox.md (affected chapters)

# 2. Update both summaries
canonical-version/Chapter-Summary-and-Timeline.md
paradox-version/Chapter-Summary-and-Timeline.md

# 3. Verify consistency across all references
# Search for other mentions of the updated element
grep -r "element_name" canonical-version/
grep -r "element_name" paradox-version/

# 4. Commit with [Both] tag
git commit -m "[Both] Update blood magic mechanics

- Clarified regeneration rules
- Updated energy cost system
- Affects Chapters X, Y, Z in both versions"
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

### Enhance Romance (Both Versions)

Romance is central to both versions but expressed differently. Updates must respect each version's identity while maintaining core relationship elements.

**Core Romance Elements (Must Sync)**:
- Riven and Raechelle's fundamental connection
- Key relationship milestones (first kiss, first intimacy, commitment)
- Core emotional beats (trust, vulnerability, devotion)
- Dom/sub dynamic foundation (consent, care, boundaries)
- Character growth through the relationship

**Version-Specific Romance Approaches**:

**Canonical Version**:
- Straightforward romantic progression
- Clear emotional communication
- Uplifting and affirming intimate scenes
- Power fantasy elements (protective, strong bond)
- Satisfying, uncomplicated love story
- Focus on joy and connection

**Paradox Version**:
- Psychological depth and complexity
- Hidden emotional tensions (Raechelle's secret)
- Intimate scenes carry weight of past/identity
- Question of whether love is redemption
- Emotional vulnerability as central theme
- Focus on healing and transformation

**Enhancement Process**:
```bash
# 1. Identify romance scene or element to enhance
# - Deepening emotional connection
# - Adding intimate moments
# - Developing Dom/sub dynamics
# - Character vulnerability

# 2. Update in both versions (version-appropriate style)
canonical-version/Blood-Craft-Canonical.md (specific chapters)
paradox-version/Blood-Craft-Paradox.md (specific chapters)

# 3. Ensure romance serves character development
# Not just added for its own sake

# 4. Commit with appropriate tag
git commit -m "[Both] Enhance intimate scene in Chapter X

- Deepened emotional vulnerability
- Advanced Dom/sub dynamic naturally
- Canonical: Focus on joy and connection
- Paradox: Added psychological complexity"
```

**Romance Enhancement Checklist**:
- [ ] Scene serves character development
- [ ] Maintains consent and boundaries
- [ ] Advances relationship believably
- [ ] Appropriate to chapter pacing
- [ ] Respects version's romantic identity
- [ ] Balances intimacy with plot progression
- [ ] Dom/sub dynamic feels earned and natural
- [ ] Emotional beats land authentically

**Examples of Romance Enhancements**:
- **Emotional Depth**: Add vulnerable conversation after battle
- **Physical Intimacy**: Expand existing scene with more sensory detail
- **Dom/Sub Dynamic**: Show trust-building through power exchange
- **Character Growth**: Use intimate moment to reveal character change
- **Tension**: Add romantic tension in political/action scenes

**Common Enhancement Scenarios**:
```bash
# Adding a new romantic scene
- Canonical: Focus on connection and satisfaction
- Paradox: Layer in psychological complexity

# Deepening existing intimate scene
- Add sensory details and emotional reactions
- Ensure Dom/sub dynamic is clear and consensual
- Balance physical and emotional intimacy

# Enhancing emotional vulnerability
- Show characters revealing fears or hopes
- Use intimate settings for character revelations
- Build trust through gradual disclosure
```

### Updating a Character's Core Traits

```bash
# 1. Update in both version files
canonical-version/Blood-Craft-Canonical.md
paradox-version/Blood-Craft-Paradox.md

# 2. Update chapter summaries if needed
# 3. Check for consistency across all appearances
# 4. Commit with [Both] tag
git commit -m "[Both] Update Raechelle's backstory

- Added training history details
- Maintains consistency across versions"
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

### Paradox Version - Key Elements

✅ **Include**:
- Psychological depth and complexity
- Moral ambiguity and grey characters
- Layered foreshadowing for twist
- Questions about identity and consciousness
- Earned redemption arcs

❌ **Avoid**:
- Making twist obvious
- Sacrificing character for shock value
- Ignoring emotional consequences
- Forgetting romance at the core

---

## 🔄 Commit Message Format

```bash
# Format
[Version] Brief description

Detailed explanation
- Specific change 1
- Specific change 2

# Examples
[Canonical] Add Chapter 31 - New Threats
[Paradox] Enhance foreshadowing in Chapter 12
[Both] Update blood magic mechanics
```

**Version Tags**:
- `[Canonical]` - Changes only to canonical version
- `[Paradox]` - Changes only to paradox version
- `[Both]` - Changes affecting both versions
- `[Docs]` - Documentation-only changes

---

## 📊 Current Status

**As of January 2026**:

| Version | Status | Chapters | Word Count |
|---------|--------|----------|------------|
| Canonical | ✅ Complete | 30 | ~88,000 |
| Paradox | ✅ Complete | 30 | ~97,000 |

**Current Focus**: Both versions complete; infrastructure ready for Book 2 development

---

## 🔍 Consistency Requirements

### Must Stay Synchronized Between Versions

- Blood magic mechanics and rules
- Nocturne geography and locations
- Core character traits and backstories
- Timeline of major events
- Supernatural faction structures
- Magic system fundamentals

### Can Differ Between Versions

- Character arc trajectories
- Relationship complexity levels
- Moral framework (clear vs. ambiguous)
- Narrative tone and style
- Plot resolutions
- Thematic depth and exploration

---

## 💡 Quick Tips

### Do's ✅

- Commit frequently with clear messages
- Use version tags in commit messages
- Cross-reference for consistency regularly
- Review DEVELOPMENT.md when unsure
- Update documentation alongside content

### Don'ts ❌

- Don't let one version lag in quality
- Don't introduce world-building contradictions
- Don't blur versions' creative identities
- Don't forget to update documentation
- Don't commit without testing

---

## 📖 Where to Find Things

**World-Building Information**:
- Chapter-Summary-and-Timeline.md (both versions)
- Early chapters of both versions

**Character Information**:
- Chapter-Summary-and-Timeline.md (both versions)
- DEVELOPMENT.md (both versions - character sections)

**Creative Guidelines**:
- DEVELOPMENT.md (version-specific)
- CONTRIBUTING.md (general guidelines)

**Workflow Help**:
- WORKFLOW.md (parallel development)
- This file (quick tasks)

**Version Comparison**:
- docs/Comparison-Guide.md
- README.md (main overview)

---

## ❓ Common Questions

**Q: Which version should I work on first?**
A: Work on whichever version your changes apply to. If it's world-building, do both together.

**Q: How do I know if a change affects both versions?**
A: If it's about supernatural rules, locations, or core character traits, it likely affects both. If it's about narrative tone or complexity, it's probably version-specific.

**Q: Can I change the twist in the Paradox version?**
A: The core twist (Riven as reincarnation) is fundamental to the version. You can refine how it's revealed or foreshadowed, but the twist itself should remain.

**Q: What if I want to add content that doesn't fit either version's style?**
A: Consider if it can be adapted to fit either version, or if it might be better as a separate companion piece or side story.

**Q: How often should I sync changes between versions?**
A: For world-building changes, sync immediately. For other changes, review weekly or after major updates.

---

## 🚨 Emergency Troubleshooting

**Issue**: Git conflict between versions
- Solution: Check which version the conflict is in, resolve based on that version's guidelines

**Issue**: Forgot which version a file belongs to
- Solution: Check file path: `canonical-version/` or `paradox-version/`

**Issue**: Character acting inconsistently
- Solution: Review previous chapters, check DEVELOPMENT.md character guidelines

**Issue**: Can't remember world-building rule
- Solution: Search Chapter-Summary-and-Timeline.md in both versions

**Issue**: Unsure about creative direction
- Solution: Check version-specific DEVELOPMENT.md for guidelines

---

## 📞 Need More Help?

- **Full guidelines**: [CONTRIBUTING.md](CONTRIBUTING.md)
- **Workflow details**: [WORKFLOW.md](WORKFLOW.md)
- **Canonical specifics**: [canonical-version/DEVELOPMENT.md](canonical-version/DEVELOPMENT.md)
- **Paradox specifics**: [paradox-version/DEVELOPMENT.md](paradox-version/DEVELOPMENT.md)

---

**Last Updated**: January 2026

Happy developing! 🩸✨
