# BloodCraft Custom Agents

This directory contains custom GitHub Copilot agents designed to assist with various tasks in the BloodCraft repository.

## Available Agents

### 1. Narrative Consistency Reviewer
**File**: `narrative-consistency-reviewer.agent.md`

**Purpose**: Specialized agent for comprehensive narrative analysis to detect:
- Repeating scenes and duplicate content
- Timeline inconsistencies and time jumps
- Character continuity issues (physical descriptions, ages, abilities)
- Plot inconsistencies and unresolved threads
- World-building rule violations

**When to Use**:
- After writing new chapters or making significant edits
- Before publishing or releasing new content
- When readers report confusing or contradictory elements
- As part of quality assurance for long-form fiction
- To verify consistency after merging multiple story branches

**How to Use**:
1. Open GitHub Copilot Chat in your editor
2. Type: `@narrative-consistency-reviewer Please analyze the canonical version for any narrative inconsistencies, repeating scenes, or timeline issues`
3. The agent will analyze the entire narrative and provide a comprehensive report

**Example Commands**:
```
@narrative-consistency-reviewer Analyze Blood-Craft-Canonical.md for repeating scenes and time jumps

@narrative-consistency-reviewer Check if character descriptions are consistent throughout the story

@narrative-consistency-reviewer Review the timeline progression in chapters 1-38

@narrative-consistency-reviewer Verify that all plot threads introduced are resolved

@narrative-consistency-reviewer Check for duplicate content between main chapters and POV chapters
```

**What You'll Get**:
- Comprehensive report with severity-rated issues
- Exact line numbers for each inconsistency
- Specific before/after text for fixes
- Timeline analysis showing character age progression
- Character profile consistency verification
- Prioritized action plan for fixes
- Verification of consistent elements

**Report Categories**:
- 🔴 **Critical Issues**: Break story logic or immersion - fix immediately
- 🟠 **Major Issues**: Create confusion - fix soon
- 🟡 **Minor Issues**: Noticeable but not story-breaking - fix when convenient
- ✅ **Verified Consistent**: Confirmed correct elements

**Previous Analysis Results**:
The agent was used to conduct the comprehensive review documented in:
- `NARRATIVE_CONSISTENCY_REVIEW.md`
- `INCONSISTENCY_ANALYSIS_REPORT.md`
- `FIXES_COMPLETED_SUMMARY.md`

This review found 10 inconsistencies (99.93% consistency rate), all of which have been fixed.

---

### 2. Stephen King (Example Agent)
**File**: `my-agent.agent.md`

**Purpose**: Example agent that emulates Stephen King's writing style

**Note**: This is a demonstration agent showing the basic format. Replace or modify as needed.

---

## Agent Configuration Format

GitHub Copilot agents use a specific markdown format:

```markdown
---
name: Agent Name
description: Brief description of what the agent does
---

# Full Agent Title

[Detailed instructions for the agent behavior, responsibilities, and guidelines]
```

### Key Elements:
1. **YAML Front Matter**: Must include `name` and `description`
2. **Markdown Body**: Contains the full prompt and instructions for the agent
3. **File Extension**: Must be `.agent.md`
4. **Location**: Must be in `.github/agents/` directory
5. **Branch**: Must be merged to default branch to be available

## Creating New Agents

To create a new custom agent for BloodCraft:

1. **Create a new file** in `.github/agents/` with `.agent.md` extension
2. **Add YAML front matter** with `name` and `description`
3. **Write detailed instructions** covering:
   - Agent's role and expertise
   - Specific tasks it should perform
   - Analysis standards and criteria
   - Output format and structure
   - Limitations and boundaries
4. **Test locally** using GitHub Copilot CLI: `gh copilot suggest -a <agent-name>`
5. **Commit and merge** to the default branch
6. **Agent becomes available** in Copilot Chat with `@agent-name`

## Best Practices for Agent Design

### Do:
- ✅ Be specific about the agent's expertise and role
- ✅ Provide clear, actionable instructions
- ✅ Include example outputs or formats
- ✅ Define boundaries (what the agent should/shouldn't do)
- ✅ Make instructions comprehensive but focused
- ✅ Include context about the repository/project
- ✅ Specify output format and structure

### Don't:
- ❌ Make agents too general-purpose
- ❌ Overlap significantly with other agents
- ❌ Leave instructions vague or ambiguous
- ❌ Forget to test before committing
- ❌ Create agents for one-time tasks

## Agent Ideas for BloodCraft

Potential agents to consider creating:

1. **Character Consistency Tracker**: Focus specifically on character descriptions, personalities, and development arcs
2. **Timeline Validator**: Specialized in verifying mathematical accuracy of dates, ages, and time progression
3. **POV Differentiation Checker**: Ensure POV chapters are distinct and not just duplicates
4. **World-Building Analyzer**: Verify magic system rules, setting descriptions, and lore consistency
5. **Dialogue Naturalness Reviewer**: Check for authentic character voices and realistic conversation flow
6. **Chapter Structure Analyzer**: Review pacing, scene transitions, and structural elements
7. **Publishing Readiness Checker**: Comprehensive pre-publication review checklist

## Resources

- **GitHub Copilot Custom Agents Documentation**: https://gh.io/customagents/config
- **Copilot CLI for Testing**: https://gh.io/customagents/cli
- **BloodCraft Contributing Guide**: `/CONTRIBUTING.md`
- **BloodCraft Development Guide**: `/canonical-version/DEVELOPMENT.md`

---

## Support and Feedback

If you have questions about using these agents or suggestions for new agents:
1. Check the agent's instructions for usage examples
2. Review the comprehensive documentation in each agent file
3. Create an issue with the `agent-feedback` label (if applicable)
4. Refer to the consistency review reports for examples of agent output

---

**Last Updated**: February 2026
