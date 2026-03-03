#!/usr/bin/env python3
"""Fix failed anchors in Chapter 2 expansion."""

INSERTS = {
    '"How could they even know where we are at this hour?" Mom\'s voice quivered with a nervous intensity that pulled my\nattention away from my swirling thoughts.': """

I realized I was gripping the door handle with both hands—my knuckles white, fingers aching from the pressure. I didn't remember reaching for it. My body had made the decision independently, some ancient survival mechanism recognizing threat before my conscious mind had caught up. The darkness outside was different now. Not the comfortable, inhabited darkness I'd spent my whole life befriending, but something heavier, purposeful—the dark of a predator waiting, not the dark of a forest resting.

The air in the car had changed too. Something metallic beneath the ozone, beneath the Sinatra that was no longer playing—iron and cold stone, a smell that belonged underground, in old places, in the dark beneath dark. I tried to identify it and couldn't. My senses, already sharpened by the evening's accumulating strangeness, were picking up signals I had no reference for, frequencies my nervous system recognized as important without having language to name them.

""",
    '"What are you?" she asked, her voice trembling with a mixture of bewilderment and concern. Her eyes were wide as she\nstared at me in disbelief.': """

I looked at my hands. They were the same hands I'd had all my life—the same familiar shape, the same calluses from typing, the same small scar on my right palm from a childhood fall—but they didn't feel like the same hands. They felt like instruments that had been recalibrated. Tools built for a specific purpose, only now understanding what that purpose was.

The power had receded to a place just beneath my skin—no longer roiling but present, waiting, banked like coals that have done their first violent burning and settled into something more sustainable. I could feel it the way you feel your own heartbeat when you're very still: constant, fundamental, mine.

The pain was gone. Not diminished—gone. Every bruise and laceration and concussion-throb from the crash: erased. My body had repaired itself with a thoroughness that should have been impossible and felt, in this moment, completely natural. As though the damaged version of me had been a draft, and the version standing here now was the final manuscript.

The hunger, though. The hunger was new and enormous and pointing at her—at Raechelle—at the warmth beneath the pale skin of her throat and the pulse I could somehow hear, the way you hear a melody once you've identified it. I took a deliberate step back from her. Put distance between that hunger and its object. Noted, with grim analytical precision, that the hunger intensified with the distance rather than diminishing.

""",
    'She paused, collecting her thoughts, and continued, "The magic of your Bloodline is particularly unique and powerful.\nIt\'s rooted in blood magic, a force that typically awakens only the red discipline magic within its chosen. But based on\nwhat I\'ve just witnessed during your awakening, I can\'t help but feel that your experience is more complex than that.\nThere\'s something unusual at play here, something that transcends the expected boundaries of your lineage."': """

She was still on one knee. The gesture was not theatrical—she had dropped to it as though pulled by something involuntary, the way a compass needle swings to north without choosing to. Whatever I had become in the last five minutes, it commanded something from her that had nothing to do with volition.

I was aware of this in a way that was simultaneously uncomfortable and clarifying. The dominant streak I'd identified in myself years ago, that I'd explored carefully in Dallas with an ethical framework I'd built deliberately—it was no longer operating at the level of personality. It was something structural now. Something that reached through whatever I was and created a field around me that others responded to. Raechelle was responding to it without choice, pulled into deference by the thing I had awakened. I didn't know whether to be unsettled or grateful. The unsettling part was obvious. The gratitude was this: that I had spent years developing the framework for this—the ethical structure, the understanding of care and responsibility in relation to power. Whatever design had produced me had given me time to build the character to carry what came next.

"""
}

# Read current file
with open('/home/runner/work/BloodCraft/BloodCraft/canonical-version/book1-expanded/ch02_expanded.md', 'r') as f:
    content = f.read()

for anchor, new_content in INSERTS.items():
    if anchor in content:
        content = content.replace(anchor, anchor + new_content, 1)
        print(f"✓ Inserted after: {anchor[:60]}...")
    else:
        print(f"✗ NOT FOUND: {repr(anchor[:80])}")

with open('/home/runner/work/BloodCraft/BloodCraft/canonical-version/book1-expanded/ch02_expanded.md', 'w') as f:
    f.write(content)

word_count = len(content.split())
print(f"\nFinal word count: {word_count}")
