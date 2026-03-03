#!/usr/bin/env python3
"""Tiny top-up for Chapter 1 - need ~400 more words."""

INSERTS = {
    "West, Texas is the kind of small town that is famous, locally, for its kolaches—Czech pastries sold at a gas station and bakery combination that draws drivers off I-35 by scent and reputation. The town is also famous, less locally, for the 2013 fertilizer plant explosion that killed fifteen people and left a crater large enough to swallow a house, and which my parents refused to discuss in any detail except to say that we had been away that weekend—visiting relatives in San Antonio—and that they thanked God for it every day in a tone that stopped conversation.": """

West was a town of about 2,800 people, the majority of Czech descent, with a downtown of brick buildings and feed stores and the Czech Stop that became, in the years after the explosion, almost a pilgrimage site for people who wanted to support the community's recovery. We were not Czech—we were anomalous, the family on forty acres who had arrived from elsewhere and integrated quietly, accepted rather than absorbed, always slightly outside the town's central social logic. Mom knew everyone at the farmer's market. Dad fixed the neighbor's computer when it crashed and refused payment. I had mowed lawns and baled hay for pocket money, performed all the social contracts of small-town boyhood. But we remained, at some level, the family at the edge of things—the people who were there but not quite *from* there, rooted in the place but rooted lightly, as though one end of our root system reached somewhere else entirely.

I understood this as the car moved through the Ouachita night. We had been *placed* in West, Texas. Not randomly. Placed, the way you place something carefully: with intention and forethought and a reason that may only become legible later."""
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
