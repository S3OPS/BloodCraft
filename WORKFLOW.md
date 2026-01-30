# Dual-Version Development Workflow

This guide explains how to effectively work on both the Canonical and Paradox versions of Blood Craft in parallel.

---

## 🎯 Overview

Blood Craft maintains two complete storylines with different creative approaches:
- **Canonical Version**: Traditional hero's journey
- **Paradox Version**: Psychological thriller with major twist

This document outlines best practices for developing both versions simultaneously.

---

## 🔄 Development Workflows

### Workflow 1: World-Building Updates

**Use When**: Updating supernatural rules, locations, or lore that affects both versions

**Steps**:
1. Identify the world-building element to update
2. Plan how it affects both storylines
3. Update canonical version files
4. Update paradox version files (maintaining version-specific tone)
5. Verify consistency across both versions
6. Update both Chapter-Summary-and-Timeline.md files

**Example**: Updating blood magic regeneration mechanics
```bash
# Edit both versions
- canonical-version/Chapter-Summary-and-Timeline.md
- paradox-version/Chapter-Summary-and-Timeline.md
- Update relevant chapters in both Blood-Craft-{Version}.md files

# Commit with clear message
git commit -m "[Both] Update blood magic regeneration mechanics

Clarified energy costs and healing limits
- Affects Chapters 8, 15, 23 in both versions
- Maintains consistency across storylines"
```

### Workflow 2: Character Trait Updates

**Use When**: Updating core personality traits or backstory

**Steps**:
1. Identify which character traits are shared vs. version-specific
2. Update shared traits in both versions
3. Adjust version-specific character development accordingly
4. Verify character voice consistency
5. Update character references in documentation

**Example**: Updating Raechelle's backstory
```bash
# Shared trait update
- Both versions: Update core backstory elements
- Canonical: Emphasize straightforward motivation
- Paradox: Layer in hidden knowledge/complexity

# Commit appropriately
git commit -m "[Both] Expand Raechelle's backstory

Added details about her training years
- Canonical: Focus on growth and dedication
- Paradox: Layer in foreshadowing of deeper knowledge"
```

### Workflow 3: Version-Specific Development

**Use When**: Adding chapters or content to only one version

**Steps**:
1. Determine which version needs the update
2. Review version-specific DEVELOPMENT.md guidelines
3. Ensure changes align with version's creative direction
4. Update relevant documentation for that version only
5. Check if any world-building changes need syncing

**Example**: Adding Paradox-specific foreshadowing
```bash
# Edit paradox version only
- paradox-version/Blood-Craft-Paradox.md (specific chapter)
- paradox-version/Chapter-Summary-and-Timeline.md

# Commit with version tag
git commit -m "[Paradox] Enhance foreshadowing in Chapter 12

Added subtle hint about Riven's ancient memories
- Integrated through dream sequence
- Maintains ambiguity for first-time readers"
```

### Workflow 4: Parallel Chapter Development

**Use When**: Writing new chapters for both versions simultaneously

**Steps**:
1. Plan chapter outline for both versions
2. Identify shared elements (events, world-building)
3. Identify divergent elements (tone, complexity, foreshadowing)
4. Write canonical version chapter
5. Write paradox version chapter
6. Cross-check for consistency in shared elements
7. Update documentation for both versions
8. Commit both together or separately based on scope

**Example**: Adding Chapter 31 to both versions
```bash
# If very similar, commit together
git commit -m "[Both] Add Chapter 31 - New Threats

Introduces antagonist faction in both versions
- Canonical: Clear threat, heroic response planned
- Paradox: Layered complexity, identity questions raised
- Shared: Faction structure, world-building elements
- ~4,500 words canonical, ~5,200 words paradox"

# If significantly different, commit separately
git commit -m "[Canonical] Add Chapter 31 - New Threats"
git commit -m "[Paradox] Add Chapter 31 - Identity Crisis"
```

---

## 📋 Development Checklists

### Starting a New Development Session

- [ ] Pull latest changes
- [ ] Review recent commits to both versions
- [ ] Check current status in both Chapter-Summary-and-Timeline.md
- [ ] Identify what needs to be synced vs. what's version-specific
- [ ] Review any TODOs or development notes

### Before Committing Changes

**For World-Building Changes**:
- [ ] Updated in both versions (if applicable)
- [ ] Consistency verified across versions
- [ ] Both Chapter-Summary-and-Timeline.md files updated
- [ ] No contradictions introduced

**For Character Development**:
- [ ] Core traits consistent across versions (if shared)
- [ ] Version-specific arcs maintained appropriately
- [ ] Character voice consistent within each version
- [ ] Documentation updated

**For New Chapters**:
- [ ] Follows version-specific guidelines (check DEVELOPMENT.md)
- [ ] Chapter-Summary-and-Timeline.md updated
- [ ] Word count updated in README.md
- [ ] Cross-version consistency maintained (world-building)
- [ ] Quality standards met (grammar, flow, pacing)

### Regular Maintenance

**Weekly**:
- [ ] Review consistency between versions
- [ ] Check for any sync issues in world-building
- [ ] Update any planning documents
- [ ] Review development notes

**After Major Updates**:
- [ ] Verify timeline consistency
- [ ] Check character arc alignment where needed
- [ ] Update comparison documentation if needed
- [ ] Test reading experience in both versions

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

**Paradox Version**:
- ✅ Psychological depth and complexity
- ✅ Moral ambiguity and grey areas
- ✅ Layered foreshadowing for twist
- ✅ Questions about identity and choice
- ✅ Earned redemption arc
- ❌ Avoid making twist obvious
- ❌ Don't sacrifice character for shock
- ❌ Don't forget romance at the core

### Decision Framework

When unsure about whether something fits a version:

**Ask yourself**:
1. Does this serve the version's core identity?
2. Does this align with reader expectations for this version?
3. Does this maintain the version's tone and themes?
4. Would this be better in the other version?

**If the answer is unclear**: Default to the version's DEVELOPMENT.md guidelines.

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
- Canonical Version: ✅ 30 chapters complete (~88,000 words)
- Paradox Version: ✅ 30 chapters complete (~97,000 words)

### Future Development Tracking

**Book 2 Planning**:
- [ ] Outline canonical Book 2 direction
- [ ] Outline paradox Book 2 direction
- [ ] Identify shared vs. divergent storylines
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
3. **paradox-version/DEVELOPMENT.md** - Paradox-specific guidelines
4. **Chapter-Summary-and-Timeline.md** (both versions) - Current state
5. **docs/Comparison-Guide.md** - Understanding differences

### Reference Order

**Before Starting**:
1. Read CONTRIBUTING.md for general guidelines
2. Review relevant version's DEVELOPMENT.md
3. Check Chapter-Summary-and-Timeline.md for context

**During Development**:
1. Refer to version-specific DEVELOPMENT.md
2. Cross-reference with other version for consistency
3. Check existing chapters for voice/tone

**After Completing**:
1. Review against version guidelines
2. Verify consistency with documentation
3. Update all relevant files

---

## 💡 Tips & Best Practices

### Do's ✅

- **Do** commit frequently with clear messages
- **Do** use version tags in commit messages [Canonical], [Paradox], [Both]
- **Do** maintain both versions' documentation equally
- **Do** cross-reference for consistency regularly
- **Do** keep versions' creative identities distinct
- **Do** plan ahead for parallel development
- **Do** use the DEVELOPMENT.md files as guides

### Don'ts ❌

- **Don't** let one version lag behind in quality
- **Don't** introduce contradictions in shared elements
- **Don't** blur the lines between versions' creative directions
- **Don't** forget to update documentation
- **Don't** commit without testing changes
- **Don't** mix version-specific changes in one commit
- **Don't** lose sight of each version's target audience

---

## 🤝 Collaboration

### Working with Others

**Communication**:
- Clearly indicate which version(s) you're working on
- Note any changes that affect both versions
- Document major creative decisions
- Share drafts for consistency review

**Coordination**:
- Check for ongoing work before starting
- Avoid simultaneous edits to same sections
- Sync regularly on world-building changes
- Review each other's work for consistency

**Conflict Resolution**:
- Refer to DEVELOPMENT.md guidelines
- Prioritize version's creative identity
- Consider target audience expectations
- Discuss ambiguous cases before committing

---

## ❓ Troubleshooting

### Common Issues

**Issue**: Inconsistency between versions in world-building
**Solution**: Review Chapter-Summary-and-Timeline.md in both versions, identify discrepancy, update to match established rules

**Issue**: Character feels out of voice
**Solution**: Review previous chapters with that character, check DEVELOPMENT.md character guidelines, adjust for consistency

**Issue**: Unsure if change should affect both versions
**Solution**: Check if it's a core world-building element (both) or version-specific narrative choice (one)

**Issue**: Commit includes changes to both versions
**Solution**: If tightly coupled (world-building), commit together with [Both] tag. If separate changes, use separate commits.

---

## 📞 Questions?

Refer to:
- **General questions**: CONTRIBUTING.md
- **Canonical-specific**: canonical-version/DEVELOPMENT.md
- **Paradox-specific**: paradox-version/DEVELOPMENT.md
- **Comparison info**: docs/Comparison-Guide.md
- **Current state**: Chapter-Summary-and-Timeline.md (in each version)

---

**Last Updated**: January 2026

Happy writing! May both versions flourish. 🩸✨
