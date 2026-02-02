# Using the Narrative Consistency Reviewer Agent

## Overview

The **Narrative Consistency Reviewer** is a specialized GitHub Copilot agent designed to analyze the BloodCraft narrative for consistency issues, including:
- Repeating scenes and duplicate content
- Timeline inconsistencies and time jumps  
- Character description variations
- Plot holes and unresolved threads
- World-building rule violations

This agent was created based on the comprehensive analysis that identified and fixed inconsistencies in the canonical version (see `NARRATIVE_CONSISTENCY_REVIEW.md`).

---

## Prerequisites

To use this agent, you need:
1. GitHub Copilot subscription (Business or Enterprise)
2. GitHub Copilot enabled in your editor (VS Code, Visual Studio, JetBrains, etc.)
3. Access to the BloodCraft repository

---

## Quick Start

### Basic Usage

1. **Open GitHub Copilot Chat** in your editor (usually with keyboard shortcut or sidebar icon)

2. **Invoke the agent** using the `@` mention syntax:
   ```
   @narrative-consistency-reviewer Please analyze the canonical version for narrative inconsistencies
   ```

3. **Review the generated report** which will include:
   - Executive summary with statistics
   - Categorized issues (Critical, Major, Minor)
   - Specific line numbers and quotes
   - Recommended fixes with before/after text
   - Timeline analysis
   - Character consistency verification

---

## Command Examples

### Full Narrative Analysis
```
@narrative-consistency-reviewer Analyze /canonical-version/Blood-Craft-Canonical.md for all types of inconsistencies including repeating scenes, time jumps, and character continuity issues. Provide a comprehensive report with line numbers and recommended fixes.
```

### Focused Analyses

**Check for Repeating Scenes:**
```
@narrative-consistency-reviewer Scan chapters 1-38 for any duplicate or repeating scenes. Flag any content that appears multiple times without clear narrative justification.
```

**Timeline Verification:**
```
@narrative-consistency-reviewer Verify the timeline consistency across the entire narrative. Check character ages, time jumps, and ensure all temporal references align correctly.
```

**Character Consistency Check:**
```
@narrative-consistency-reviewer Review all physical descriptions of major characters (Riven, Raechelle, Viktor, Morgana, etc.) and flag any inconsistencies in hair color, eye color, or other attributes.
```

**New Chapter Review:**
```
@narrative-consistency-reviewer Review the new chapters in /canonical-version/new-chapters/ and verify they are consistent with the main narrative. Check for timeline alignment and character description consistency.
```

**Plot Thread Verification:**
```
@narrative-consistency-reviewer Identify all major plot threads introduced in the narrative and verify each one is properly resolved. Flag any hanging threads or contradictions.
```

---

## Understanding the Report

### Severity Levels

The agent categorizes issues into three severity levels:

#### 🔴 Critical Issues (Priority 1)
- **Impact**: Breaks story logic or reader immersion
- **Examples**: Character's hair color changes without explanation, contradictory ages, impossible timeline
- **Action**: Fix immediately before publication

#### 🟠 Major Issues (Priority 2)  
- **Impact**: Creates confusion or weakens narrative
- **Examples**: Duplicate chapter content, significant age discrepancy, unresolved major plot thread
- **Action**: Fix soon, before next major release

#### 🟡 Minor Issues (Priority 3)
- **Impact**: Noticeable but doesn't break the story
- **Examples**: Small formatting inconsistencies, minor clarifications needed
- **Action**: Fix when convenient, may wait for next editing pass

#### ✅ Verified Consistent
- Elements that were thoroughly checked and confirmed correct
- Provides assurance about what's working well

---

## Sample Report Structure

When you invoke the agent, expect a report like this:

```markdown
# Blood Craft Canonical - Narrative Consistency Analysis

**Analysis Date**: 2026-02-01
**Document Analyzed**: /canonical-version/Blood-Craft-Canonical.md
**Total Length**: 14,502 lines, 47 chapters

## EXECUTIVE SUMMARY

Total Issues Found: 10
- Critical: 1
- Major: 2  
- Minor: 7
- Consistency Rate: 99.93%

## 🔴 CRITICAL ISSUES

### Issue 1: Character Hair Color Inconsistency
**Severity**: CRITICAL
**Impact**: Breaks reader immersion during key scenes

**The Problem**: 
Raechelle's hair described as both "midnight black" and "crimson"...

**Instances Found**:
- Line 630: "midnight hair cascading..."
- Line 4979: "crimson that matched her hair"

**Recommended Fix**:
Line 4979 - Change:
OLD: "matched her hair"
NEW: "complemented her midnight hair"

[... continues with detailed analysis ...]
```

---

## Best Practices

### When to Run Analysis

**✅ Do run analysis**:
- After completing new chapters
- Before publishing or releasing content
- After major editing sessions
- When merging story branches
- After receiving reader feedback about confusion
- As part of quality assurance process

**❌ Don't run analysis**:
- During active writing sessions (wait until draft is complete)
- For every tiny change (batch your edits)
- When you know issues exist and plan to fix them

### How to Use the Results

1. **Review the Executive Summary** first to understand scope
2. **Address Critical Issues** immediately - these break the story
3. **Prioritize Major Issues** based on which chapters are being revised
4. **Batch Minor Issues** to fix during your next editing pass
5. **Use Verified Consistent** as a checklist of what's working

### Iterative Analysis

After fixing issues:
1. Commit your changes
2. Run the agent again with:
   ```
   @narrative-consistency-reviewer Re-analyze the narrative focusing on the areas we just fixed (lines X-Y, chapters A-B). Verify the fixes resolved the issues and didn't introduce new problems.
   ```
3. Repeat until consistency rate is satisfactory (>99% is excellent)

---

## Understanding Agent Capabilities

### What the Agent WILL Do
✅ Detect repeating/duplicate content  
✅ Verify timeline and age progression  
✅ Track character descriptions across entire narrative  
✅ Identify plot holes and inconsistencies  
✅ Check world-building rules  
✅ Provide specific, actionable fixes  
✅ Assess severity and prioritize issues  
✅ Acknowledge narrative strengths

### What the Agent WILL NOT Do
❌ Make stylistic or creative suggestions  
❌ Rewrite content for artistic reasons  
❌ Change your narrative voice  
❌ Add new plot elements  
❌ Edit grammar or spelling (unless it causes confusion)  
❌ Flag intentional artistic choices

---

## Interpreting Special Cases

### Intentional Repetition (Not Flagged as Issues)
- **Flashbacks**: Clearly marked returns to past events
- **POV Shifts**: Same event from different character perspectives (X.5 chapters)
- **Callbacks**: Deliberate references to earlier moments
- **Recurring Themes**: Intentional motifs and patterns

### Expected Changes (Not Flagged as Issues)
- **Aging**: Silver hair in later chapters when character is older
- **Power Progression**: Abilities growing with training
- **Relationship Evolution**: Bonds deepening over time
- **Supernatural Transformation**: Explicitly described changes (vampire transformation, etc.)

---

## Troubleshooting

### "Agent not found" error
**Cause**: Agent file not merged to default branch yet  
**Fix**: Ensure `.github/agents/narrative-consistency-reviewer.agent.md` is committed and merged to main/master branch

### Agent provides generic responses
**Cause**: Instructions not specific enough  
**Fix**: Use more specific commands like:
```
@narrative-consistency-reviewer Read the ENTIRE file at /canonical-version/Blood-Craft-Canonical.md from line 1 to line 14502. Track every instance of Raechelle's hair color description and report all variations with exact line numbers.
```

### Analysis misses known issues
**Cause**: Agent hasn't analyzed full context  
**Fix**: Explicitly instruct:
```
@narrative-consistency-reviewer Analyze the complete narrative from beginning to end before drawing any conclusions. Create a working timeline showing all character ages and time jumps.
```

### Report is too long/detailed
**Cause**: Full comprehensive analysis requested  
**Fix**: Ask for specific focus:
```
@narrative-consistency-reviewer Focus only on Critical and Major issues. Skip Minor issues and provide a summary report.
```

---

## Examples from Real Analysis

The agent successfully identified issues that were fixed in the February 2026 consistency review:

### Example 1: Hair Color Detection
**Agent Found**: Raechelle's hair described as "midnight black" (7 times), "crimson" (1 time), and "amber/copper" (1 time)  
**Agent Recommended**: Change all to canonical "midnight black"  
**Result**: Fixed at lines 4979, 5917, 5607

### Example 2: Age Contradiction
**Agent Found**: Terravos described as ruling "thousands of years" vs "three centuries"  
**Agent Recommended**: Standardize to "centuries" for consistency  
**Result**: Fixed at line 1258

### Example 3: Duplicate Content
**Agent Found**: Chapter 20 contained 344 lines of duplicate content from Chapter 19.5  
**Agent Recommended**: Remove duplicate, retain canonical version  
**Result**: Duplicate deleted, reducing file by 344 lines

---

## Integration with Workflow

### Suggested Workflow

```
┌─────────────────────┐
│  Write/Edit Content │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Draft Complete     │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Run Consistency    │
│  Review Agent       │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Review Report      │
│  Prioritize Fixes   │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Apply Fixes        │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Re-run Agent       │
│  Verify Fixes       │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Ready to Publish   │
└─────────────────────┘
```

---

## Additional Resources

- **Agent Configuration**: `.github/agents/narrative-consistency-reviewer.agent.md`
- **Agent Documentation**: `.github/agents/README.md`
- **Previous Analysis**: `NARRATIVE_CONSISTENCY_REVIEW.md`
- **Fixes Applied**: `FIXES_COMPLETED_SUMMARY.md`
- **GitHub Copilot Docs**: https://gh.io/customagents/config

---

## Support

For questions or issues with the agent:
1. Review this guide thoroughly
2. Check the agent configuration file for detailed instructions
3. Examine the example reports in the repository
4. Consult GitHub Copilot documentation for general agent usage

---

**Last Updated**: February 2026  
**Agent Version**: 1.0
