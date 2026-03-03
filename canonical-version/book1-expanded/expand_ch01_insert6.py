#!/usr/bin/env python3
"""Top-up insert for Chapter 1 to reach ~12,000 words."""

INSERTS = {
    "Computer science was the logical evolution of those years—the elegant mathematics of systems that behave predictably but feel alive, the strange intimacy of talking to machines in their own language. I was good at it in the way that some people are good at chess: quickly, and with a satisfaction that felt almost physical. My professors noted it. A few seemed almost unnerved by how fast I could see into the structure of a problem, how completely I could hold an entire architecture in my head before running a single test.": """

My senior thesis was on emergent behavior in distributed systems—the way complex patterns arise from simple rules, the way intelligence appears to spontaneously generate itself from the interaction of components that individually lack it. I had chosen the topic because it was academically interesting and because it felt, privately, like it was about something else. Like emergent behavior was a framework I was building not just for understanding artificial systems but for understanding myself: the question of whether a person could be more than the sum of their parts, whether something could arise from biology and history and environment that exceeded the explanation of those components and needed a different category entirely.

My thesis advisor, Dr. Patel, had called the work "unusually philosophical for a systems architecture paper" and given it an A. I had thanked her and not explained that the philosophy was the point."""
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
