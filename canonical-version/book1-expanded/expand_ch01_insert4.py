#!/usr/bin/env python3
"""Final top-up inserts for Chapter 1 to reach ~12,000 words."""

INSERTS = {
    "I had been here before. Not this lake. Not this road. Not this body, perhaps.": """

The feeling was not deja vu. I knew what deja vu felt like—the false-recognition glitch of the brain's pattern-matching systems, the brief stammer of temporal processing that makes a new experience feel like a remembered one. This was different. This was not a malfunction. It was the opposite of a malfunction: a clarity, a sudden resolution, as though a long-running process had finally returned its output.

I had been here in the way that a river has been in the ocean before it reaches the ocean—not physically, not yet, but in its composition, in the minerals it carries and the direction it moves and the inevitable destination that was fixed at the moment of its source. I was arriving somewhere I had always been aimed toward. And the knowing of it was quiet and enormous and slightly terrifying and, underneath the terror, so deeply right that the terror couldn't dent it.

The water. The red moon on the water. The forest standing at the edge of the lake with its ancient patience. And something in the water—not visible, not surfacing—present the way a sleeping thing is present: not absent, but resting, and very nearly awake.""",

    "The gaming came first—MMORPGs at twelve, then a gradual drift toward games with richer narrative architecture, games where the choices you made and the character you shaped felt like they were reaching toward something that mattered. My teenage years were spent as a night elf in one game, a vampire lord in another, a dark mage in a third. I only recognized the pattern later: I was always something old. I was always something that belonged to the dark and moved through it as native, not visitor.": """

The usernames I chose in those years were telling, in retrospect. Not *Riven* or any variation of my own name—I was not that literal. But always something that gestured at antiquity: *Ancientblood*, *Duskwalker*, *Nightborn*. Always something that placed the character at the intersection of the human and the not-quite. Always something with an old wound at its center that was also, somehow, a source of power rather than a limitation. I was not, I don't think, consciously seeking these characters. I was recognizing them. I was finding, in the narrative architecture of games, something that matched an internal landscape I hadn't been able to name.

My guild in the primary MMORPG I played from fourteen to eighteen was one I'd built myself and named, with the elaborate seriousness of a teenage fantasy nerd, *The Crimson Court*. We ran night raids, specifically. My preferences regarding raid timing were somewhat unusual among players in the Central Time Zone, but I had a persuasive argument: the server latency was better at 2 AM, which was technically true, and the actual reason—that playing in the dark, when the house was quiet and the Texas night pressed against the windows, produced a quality of focus and absorption that daylight hours couldn't match—I kept to myself."""
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
