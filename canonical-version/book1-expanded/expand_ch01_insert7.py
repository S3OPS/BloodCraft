#!/usr/bin/env python3
"""Micro top-up for Chapter 1 to reach ~12,000 words."""

INSERTS = {
    "I was twenty-three years old on Halloween. I was in a car with two people who loved me completely and had, I was increasingly certain, been keeping something from me completely. And all of it—the twelve-second call and the loaded looks and the crimson moon and the pressure in my chest that felt exactly like north—was converging toward a point I couldn't yet see but could feel approaching the way you feel a storm before the sky changes: a shift in pressure, a change in the quality of air, something that has already decided and is only waiting for you to catch up.": """

I had read somewhere—in one of the folklore books I'd found in Mom's shelves and borrowed without her noticing—that many traditions describe the moment of supernatural awakening not as a single dramatic event but as the culmination of many small events, the final click of a mechanism that has been building for years. The individual clicks are not remarkable. The accumulation is everything. And there is always, in the stories, a last ordinary moment that comes just before the click—a moment of warmth and normalcy and the particular sweetness of not yet knowing what is about to change. The car. The music. The laughter about Dean Winchester. My mother's hand reaching back to find mine in the dark.

The stories were right about this. The ordinary was very beautiful tonight. I held it carefully, the way you hold something you know you are about to set down.

I was twenty-three. I was on my birthday. I was exactly where I was supposed to be.

Something in the lake moved just beneath the surface of the water, leaving no ripple, only a presence—the certainty of motion without its evidence. My eyes found the water through the trees as we rounded the last curve.

I breathed.

I was ready."""
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
