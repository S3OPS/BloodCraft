#!/usr/bin/env python3
"""Final 1200-word insert for Chapter 1 to reach ~12,000 words."""

INSERTS = {
    "I had, in my second year at college, taken a psychology course that covered predictive processing theory—the idea that the brain is fundamentally a prediction machine, constantly generating models of reality and updating them based on incoming data, with perception itself being less a recording of what's out there than a comparison between prediction and surprise. I'd thought of Mom immediately and understood something about her that I hadn't had language for: she was simply better at the predictions than most people. Her models were more accurate, her updates faster. She knew what was coming because she was better at reading what was.": """

I had, over the previous year, extended this framework to myself and found it both clarifying and incomplete. Clarifying: the way I processed information did seem to involve a level of predictive modeling that exceeded what my peers described in their own experience. I would know, sometimes, before a professor finished articulating a problem, what the solution architecture looked like—not through exceptional intelligence so much as through a sense of pattern recognition that seemed to reach ahead of explicit reasoning. I would know, in social situations, what the subtext of a conversation was before the participants themselves seemed aware of it. I would know, sometimes, what was in a space before I fully entered it: the emotional temperature, the relational dynamics, the hidden fault lines.

Incomplete: because these weren't quite predictions in the conventional sense. Predictions are derived from stored patterns, extrapolated into the future using past data. What I experienced felt more like direct perception of a signal that was already there—not inference but reception. As though the world were broadcasting at a frequency that most people couldn't tune to, and I could, and had been able to since childhood, without understanding that this was unusual until I was old enough to compare notes.

I wondered what Mom's model of tonight predicted. I wondered whether she and Dad had been running their own predictions for twenty-three years, calibrating for this specific night, this specific convergence. And I wondered, not for the first time, whether the thing I was heading toward was something entirely new or something I had, in some sense, already lived.

The cabin came into view around the last curve of the road. Yellow light in the windows. A porch with wooden chairs. Beyond it, visible between the trees, the dark mirror of Mountain Fork Lake holding the red moon on its surface with a steadiness that felt deliberate—the water choosing to reflect exactly this, at exactly this moment, for exactly this arriving creature who was twenty-three years old and ready and not-ready and entirely present for whatever came next.

I breathed in through the cracked window. Pine resin and lake water and the particular mineral coolness of Ouachita October. And underneath it, just barely: something that was not any of these things. Something older. Something that knew my name before I did.

*There you are*, I thought again.

And the lake exhaled."""
}

# Read current file
with open('/home/runner/work/BloodCraft/BloodCraft/canonical-version/book1-expanded/ch01_expanded.md', 'r') as f:
    content = f.read()

# Apply insertions
for anchor, new_content in INSERTS.items():
    if anchor not in content:
        print(f"WARNING: Anchor not found: {repr(anchor[:80])}")
    else:
        content = content.replace(anchor, anchor + new_content, 1)
        print(f"Inserted after: {anchor[:70]}...")

# Write updated file
with open('/home/runner/work/BloodCraft/BloodCraft/canonical-version/book1-expanded/ch01_expanded.md', 'w') as f:
    f.write(content)

word_count = len(content.split())
print(f"\nFinal word count: {word_count}")
