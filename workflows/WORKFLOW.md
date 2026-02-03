# Development Workflow

This guide explains the workflow for developing the Canonical Version of Blood Craft.

---

## 🎯 Overview

This repository contains the **Canonical Version** of Blood Craft - a traditional hero's journey following Riven Sixxx's supernatural awakening.

**Note**: The Paradox Version (psychological thriller) is maintained in a separate repository: [github.com/S3OPS/BloodCraftParadox](https://github.com/S3OPS/BloodCraftParadox)

---

## 🔄 Development Workflows

### Workflow 1: Adding New Chapters

**Steps**:
1. Review Chapter-Summary-and-Timeline.md for story context
2. Plan the chapter's role in the overall narrative
3. Write the chapter in Blood-Craft-Canonical.md
4. Update Chapter-Summary-and-Timeline.md with chapter summary
5. Update word/chapter counts in README.md
6. Commit with clear message

**Example**:
```bash
# Edit the novel
vim canonical-version/Blood-Craft-Canonical.md

# Update summary
vim canonical-version/Chapter-Summary-and-Timeline.md

# Update counts
vim canonical-version/README.md

# Commit
git commit -m "Add Chapter 39 - New Beginnings

Added epilogue chapter showing Riven's life 40 years later
- Introduces daughter Elena
- Shows lasting peace achieved
- Wraps up character arcs"
```

### Workflow 2: World-Building Updates

**Use When**: Updating supernatural rules, locations, or fundamental lore

**Steps**:
1. Identify the world-building element to update
2. Plan how it affects the storyline
3. Update relevant chapters in Blood-Craft-Canonical.md
4. Update Chapter-Summary-and-Timeline.md
5. Verify consistency across all references
6. Consider if changes should be synchronized with Paradox version (in separate repo)

**Example**: Updating blood magic mechanics
```bash
# Edit canonical version
vim canonical-version/Blood-Craft-Canonical.md

# Update summary
vim canonical-version/Chapter-Summary-and-Timeline.md

# Verify consistency
grep -r "blood magic" canonical-version/

# Commit
git commit -m "Update blood magic regeneration mechanics

Clarified energy costs and healing limits
- Updated Chapters 8, 15, 23
- Maintains internal consistency"
```
### Workflow 3: Character Development Updates

**Use When**: Updating character traits, backstories, or arcs

**Steps**:
1. Identify what needs to be updated
2. Update relevant chapters in Blood-Craft-Canonical.md
3. Verify character voice consistency throughout
4. Update character references in documentation
5. Check Chapter-Summary-and-Timeline.md

**Example**: Expanding character backstory
```bash
# Edit chapters
vim canonical-version/Blood-Craft-Canonical.md

# Update documentation
vim canonical-version/Chapter-Summary-and-Timeline.md

# Commit
git commit -m "Expand Raechelle's backstory

Added details about her training years
- Enhances character depth
- Maintains consistency throughout"
```

### Workflow 4: Enhancing Existing Chapters

**Use When**: Improving pacing, adding detail, or deepening emotional resonance

**Steps**:
1. Identify chapter(s) to enhance
2. Review current content and tone
3. Make targeted improvements
4. Update chapter summary if significantly changed
5. Test read for flow and pacing

**Example**: Enhancing romantic scenes
```bash
# Edit chapter
vim canonical-version/Blood-Craft-Canonical.md

# Commit
git commit -m "Enhance romantic scene in Chapter 18

- Added sensory details
- Deepened emotional connection
- Advanced Dom/sub dynamic naturally"
```

---

## 📋 Development Checklists

### Starting a New Development Session

- [ ] Pull latest changes
- [ ] Review recent commits
- [ ] Check current status in Chapter-Summary-and-Timeline.md
- [ ] Review any TODOs or development notes
- [ ] Verify working on correct branch

### Before Committing Changes

- [ ] Proofread for typos and grammar
- [ ] Verify character voice consistency
- [ ] Check timeline consistency
- [ ] Ensure world-building rules maintained
- [ ] Update documentation as needed
- [ ] Test read for flow
- [ ] Character voice consistent within each version
- [ ] Documentation updated

**For New Chapters**:
- [ ] Follows canonical version guidelines (check DEVELOPMENT.md)
- [ ] Chapter-Summary-and-Timeline.md updated
- [ ] Word count updated in README.md
- [ ] Quality standards met (grammar, flow, pacing)

### After Completing Changes

- [ ] Read through changes for flow
- [ ] Update word count in README.md
- [ ] Push to repository
- [ ] Note any follow-up work needed

---

## 🎨 Creative Direction Management

### Maintaining Version Identity

**Canonical Version**:
- ✅ Clear heroes and villains
- ✅ Straightforward moral framework
- ✅ Heroic progression and growth
- ✅ Satisfying power fantasy
- ✅ Romantic and uplifting tone
- ❌ Avoid excessive moral ambiguity
- ❌ Avoid psychological complexity that confuses
- ❌ Don't undermine heroic journey

### Quality Standards

Every chapter should have:
- Clear plot progression
- Character development moment  
- Balanced pacing (action, romance, introspection)
- Consistent world-building
- Proper grammar and spelling

---

## 🔍 Troubleshooting Common Issues

### Issue: Lost track of timeline
**Solution**: Review Chapter-Summary-and-Timeline.md, look for date markers in recent chapters

### Issue: Character voice feels off
**Solution**: Re-read previous chapters with that character, check DEVELOPMENT.md for character guidelines

### Issue: World-building contradiction
**Solution**: Search for previous mentions (`grep -r "term" canonical-version/`), resolve inconsistency

### Issue: Pacing feels slow
**Solution**: Review chapter for necessary content, consider combining scenes or trimming exposition

### Issue: Unsure about creative direction
**Solution**: Check canonical-version/DEVELOPMENT.md, review version identity guidelines

---

## 📚 Additional Resources

- **[QUICK_REFERENCE.md](QUICK_REFERENCE.md)** - Common tasks and quick tips
- **[CONTRIBUTING.md](CONTRIBUTING.md)** - Full contribution guidelines
- **[canonical-version/DEVELOPMENT.md](canonical-version/DEVELOPMENT.md)** - Version-specific guidelines
- **[CHAPTER_TEMPLATE.md](CHAPTER_TEMPLATE.md)** - Template for new chapters

---

**Last Updated**: January 2026

---

## 🔍 Quality Assurance

### Consistency Checks

**Between Versions**:
- [ ] Blood magic rules are identical
- [ ] Geography and locations match
- [ ] Supporting character core personalities align
- [ ] Timeline events occur at comparable points
- [ ] Supernatural faction structures consistent

**Within Each Version**:
- [ ] Character voices remain consistent
- [ ] Plot points follow logically
- [ ] World-building rules don't contradict
- [ ] Tone remains appropriate for version
- [ ] Pacing feels right for story type

### Testing Your Changes

**After Editing**:
1. Read the edited section aloud
2. Check for flow and naturalness
3. Verify character voice consistency
4. Ensure world-building consistency
5. Test if changes achieve intended effect

**For New Chapters**:
1. Read the full chapter straight through
2. Check pacing and engagement
3. Verify it fits with surrounding chapters
4. Confirm it advances plot and character
5. Review against version guidelines

---

## 🚀 Efficient Parallel Development

### Time-Saving Strategies

**Plan Together, Write Separately**:
- Outline both versions' chapters at once
- Identify shared vs. divergent elements
- Write each version's unique voice separately
- Cross-check after writing for consistency

**Batch Similar Tasks**:
- Update all world-building in one session
- Do character consistency passes together
- Review documentation for both versions at once
- Handle synchronization in dedicated sessions

**Use Templates**:
- Chapter outline template (adapt per version)
- Character development checklist
- Consistency verification checklist
- Commit message templates

### Common Patterns

**Pattern 1: Shared Event, Different Interpretation**
- Same event occurs in both versions
- Canonical: Clear heroic response
- Paradox: Complex psychological implications

**Pattern 2: Same Scene, Different Undertones**
- Dialogue and action similar
- Canonical: Straightforward meaning
- Paradox: Layered subtext and foreshadowing

**Pattern 3: Parallel Development**
- Same chapter number, different content
- Each serves its version's narrative arc
- Cross-reference for timeline consistency

---

## 📊 Progress Tracking

### Version Status Overview

**Current Status**:
- Canonical Version: ✅ 38 chapters complete (~157,000 words)
- Paradox Version: ✅ 30 chapters complete (~97,000 words) - **In [separate repository](https://github.com/S3OPS/BloodCraftParadox)**

### Future Development Tracking

**Book 2/Sequel Planning**:
- [ ] Outline canonical Book 2/sequel direction
- [ ] Plan character arc continuations
- [ ] Establish new world-building elements

**Maintenance**:
- [ ] Regular consistency checks
- [ ] Documentation updates
- [ ] Reader feedback incorporation
- [ ] Refinement passes

---

## 🎓 Learning Resources

### Key Documents
1. **CONTRIBUTING.md** - General contribution guidelines
2. **canonical-version/DEVELOPMENT.md** - Canonical-specific guidelines
3. **Chapter-Summary-and-Timeline.md** - Current state and chapter outlines
4. **docs/Comparison-Guide.md** - Understanding differences between versions
5. **QUICK_REFERENCE.md** - Quick reference for common tasks

### Reference Order

**Before Starting**:
1. Read CONTRIBUTING.md for general guidelines
2. Review canonical-version/DEVELOPMENT.md
3. Check Chapter-Summary-and-Timeline.md for context

**During Development**:
1. Refer to canonical-version/DEVELOPMENT.md
2. Check existing chapters for voice/tone
3. Maintain consistency with established lore

**After Completing**:
1. Review against canonical version guidelines
2. Verify consistency with documentation
3. Update all relevant files

---

## 💡 Tips & Best Practices

### Do's ✅

- **Do** commit frequently with clear messages
- **Do** maintain documentation with code changes
- **Do** cross-reference for consistency regularly
- **Do** keep the canonical version's identity distinct
- **Do** plan ahead for development
- **Do** use the DEVELOPMENT.md file as a guide

### Don'ts ❌

- **Don't** introduce contradictions in world-building
- **Don't** forget to update documentation
- **Don't** commit without testing changes
- **Don't** lose sight of the target audience

---

## 🤝 Collaboration

### Working with Others

**Communication**:
- Clearly indicate what you're working on
- Note any changes that affect world-building
- Document major creative decisions
- Share drafts for review

**Coordination**:
- Check for ongoing work before starting
- Avoid simultaneous edits to same sections
- Sync regularly on world-building changes
- Review each other's work for consistency

**Conflict Resolution**:
- Refer to DEVELOPMENT.md guidelines
- Prioritize canonical version's creative identity
- Consider target audience expectations
- Discuss ambiguous cases before committing

---

## ❓ Troubleshooting

### Common Issues

**Issue**: Inconsistency in world-building
**Solution**: Review Chapter-Summary-and-Timeline.md, identify discrepancy, update to match established rules

**Issue**: Character feels out of voice
**Solution**: Review previous chapters with that character, check DEVELOPMENT.md character guidelines, adjust for consistency

**Issue**: Unsure about creative direction
**Solution**: Check canonical-version/DEVELOPMENT.md for guidelines on tone, themes, and character arcs

---

## 📞 Questions?

Refer to:
- **General questions**: CONTRIBUTING.md
- **Canonical-specific**: canonical-version/DEVELOPMENT.md
- **Comparison info**: docs/Comparison-Guide.md
- **Current state**: canonical-version/Chapter-Summary-and-Timeline.md
- **Quick tasks**: QUICK_REFERENCE.md

---

**Last Updated**: January 2026

Happy writing! 🩸✨
