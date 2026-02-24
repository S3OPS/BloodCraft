#!/usr/bin/env python3
"""Expand Chapter 2 from 7,091 words to ~12,000 words."""

import shutil

# First copy the original as the starting point for expanded
shutil.copy(
    '/home/runner/work/BloodCraft/BloodCraft/canonical-version/book1-expanded/ch02_orig.md',
    '/home/runner/work/BloodCraft/BloodCraft/canonical-version/book1-expanded/ch02_expanded.md'
)

INSERTS = {
    # After the opening scene - the radio cuts off
    '"How could they even know where we are at this hour?" Mom\'s voice quivered with a nervous intensity that pulled my\nattention away from my swirling thoughts.': """

I realized I was gripping the door handle with both hands—my knuckles white, fingers aching from the pressure. I didn't remember reaching for it. My body had made the decision independently, some ancient survival mechanism recognizing threat before my conscious mind had caught up. The darkness outside was different now. Not the comfortable, inhabited darkness I'd spent my whole life befriending, but something heavier, purposeful—the dark of a predator waiting, not the dark of a forest resting.

"How could they even know where we are at this hour?" Mom's voice quivered with a nervous intensity that pulled my attention away from my swirling thoughts.""",

    # Expand the moment of the attack
    'Without warning, we were plunged into an impenetrable darkness as though a vast, heavy curtain had been drawn across the\nsky, swallowing the night whole.': """

The air inside the car had changed. Something metallic now, beneath the ozone—iron and cold stone, a smell that belonged underground, in old places, in the dark beneath dark. I tried to identify it and couldn't. My expanded senses, already sharpened tonight, were picking up signals I had no reference for, frequencies my nervous system recognized as important without having language to name them.

I had about three seconds of that heightened, wordless awareness before the world came apart.

Without warning, we were plunged into an impenetrable darkness as though a vast, heavy curtain had been drawn across the sky, swallowing the night whole.""",

    # Expand the car crash aftermath - the first moment of consciousness
    'As I slowly opened my eyes, consciousness seeped back into my mind, bringing with it a jarring realization: the interior of the car was painted red.': """

I don't know how long I was unconscious. It could have been seconds. It felt like hours. In between, there was nothing—not darkness, not dreams, just an absence so complete it had texture, the specific blankness of a mind that has temporarily ceased to process because too much has happened and the system has gone offline to perform emergency maintenance.

When awareness returned, it came in pieces. Sound first: a high-pitched ringing that slowly resolved into the crackle of something on fire, the settling of metal, and somewhere further—impossible, wrong—birdsong. An owl. A barred owl calling from somewhere in the darkness beyond the wreckage, its four-note call as calm and unhurried as if nothing had happened, as if the world had not just ended.

Then smell: gasoline, acrid and dangerous; hot metal; blood; earth; and something else, something underneath all of it, old and mineral and not quite right.

Then sensation: the seatbelt cutting into my neck and shoulder, pressure on my left arm where it was pinned against the upturned seat, a throbbing in my head that I recognized as concussion even before I was fully conscious enough to name it.

Then sight.

As I slowly opened my eyes, consciousness seeped back into my mind, bringing with it a jarring realization: the interior of the car was painted red.""",

    # Expand the vial description
    'As I unscrewed the cap, an unexpected sharpness grazed my hand, drawing a small trickle of blood that mingled with the\nviscous substance inside.': """

I turned the vial in the moonlight. The crimson liquid inside moved with unusual thickness, slower than blood, slower than any liquid I'd encountered, with a quality of density and age that didn't match its small volume. As though it contained more than a physical substance. As though it had weight beyond what could be measured.

The pentagram on the cap caught the moonlight and held it—not reflected it, *held* it, the silver seeming to glow slightly more than the ambient light should have allowed. I stared at it for longer than made sense given that the car behind me was full of gasoline and my mother was dead and I was in shock and the dark figure was watching me with red eyes that glowed like embers.

Mom's hands had sealed this. Mom had known what was in it. Mom had carried this—had thought to put it in the glove box, or had it there already, prepared, as though this night were not a catastrophe but a scheduled event that had finally arrived.

*This is what your parents hoped for you since the day you were born.*

Raechelle's words surfaced through the shock and landed differently than they had a minute ago. Not a comfort. A revelation. They had been preparing for this. The forty acres and the permissive night-wandering and the careful framework and the drawer full of things that didn't have names yet—all of it had been preparation. For tonight. For whatever was in this vial. For whoever I was about to become.

I had spent twenty-three years being kept safe. I was about to understand what I'd been kept safe *for*.

As I unscrewed the cap, an unexpected sharpness grazed my hand, drawing a small trickle of blood that mingled with the viscous substance inside.""",

    # Expand after the awakening power surge
    '"What are you?" she asked, her voice trembling with a mixture of bewilderment and concern. Her eyes were wide as she\nstared at me in disbelief.': """

I looked at my hands. They were the same hands I'd had all my life—the same familiar shape, the same calluses from typing and the same small scar on my right palm from a childhood fall—but they didn't feel like the same hands. They felt like instruments that had been recalibrated. Tools that had been built for a specific purpose and were only now understanding what that purpose was.

The magic—if that was what it was—had receded to a place just beneath my skin, no longer roiling but present, waiting, banked like coals that have done their first violent burning and settled into something more sustainable. I could feel it there the way you feel your own heartbeat when you're very still: constant, fundamental, mine.

The pain was gone. Not diminished—gone. Every bruise and laceration and concussion-throb from the crash: gone. My body had repaired itself with a thoroughness that should have been impossible and felt, in this moment, completely natural. As though the version of me that had been broken was a draft, and the version of me that was standing here now was the final manuscript.

The hunger, though. The hunger was new and enormous and wrong in the specific way that a new sense is wrong when it first activates—too large for the space it occupies, overwhelming in its novelty. And it was pointing at her. At Raechelle. At the warmth beneath the pale skin of her throat and the pulse I could—*hear*, somehow—could hear like music in a register I'd never had access to before.

I took a deliberate step back from her. Put distance between that hunger and its object. Noted, with the part of my mind that was still performing observation and analysis, that the hunger responded to distance the way all hungers respond: by intensifying.

"What are you?" she asked, her voice trembling with a mixture of bewilderment and concern. Her eyes were wide as she stared at me in disbelief.""",

    # Expand Raechelle kneeling scene
    'She paused, collecting her thoughts, and continued, "The magic of your Bloodline is particularly unique and powerful.': """

She was still on one knee. The gesture was not theatrical—she had dropped to it as though pulled by something involuntary, the way a compass needle swings to north. Whatever I had become in the last five minutes, it commanded something from her that had nothing to do with choice.

I was aware of this in a way that was simultaneously uncomfortable and clarifying. The dominant streak that I'd identified in myself years ago, that I'd explored carefully in Dallas, that I'd thought of as a preference and a personality trait—it was no longer operating at the level of personality. It was something structural. Something that reached through whatever I was and created a field around me that others responded to. Raechelle was responding to it without volition, pulled into deference by whatever I had awakened.

I didn't know whether to be unsettled or grateful. The unsettling part was obvious. The gratitude was this: that I had spent years developing the framework for this, the ethical structure, the understanding of what care and responsibility looked like in relation to power over others. I had not stumbled into this without preparation. Whatever design had produced me, it had given me time to build the character to carry what came next.

"Stand, why are you kneeling?" I said, motioning for her to rise.

She paused, collecting her thoughts, and continued, "The magic of your Bloodline is particularly unique and powerful.""",

    # Expand the end of chapter - the car ride beginning
    '"I know you have many questions," she said softly, her hands gripping the steering wheel. I noticed her knuckles were\nwhite with tension.': """

The interior of the car smelled of her—that night-jasmine-and-old-parchment scent that I'd noticed immediately and hadn't been able to stop noticing since. My upgraded senses catalogued it automatically, building a sensory profile the way they were now apparently building profiles of everything around me: the composition of the air, the temperature gradient in the space, the faint sound of her pulse which I could track the way you track a melody once you've identified it.

Her pulse was steady, measured, controlled. She was managing herself carefully, I realized. Performing calm. Whatever I had done when she knelt—whatever command had gone out from me involuntarily—it had cost her something to accept, and she was still integrating it, still finding her footing in the new topology of our relationship.

I thought about that. About what it would mean, long-term, to be whatever I was now in relation to whatever she was. About the centuries she'd been bound to my bloodline, waiting for this. About what "bound" meant, in practical terms, and whether the binding was a constraint she'd chosen or a condition she'd been born into.

About whether she had wanted this. About whether it mattered that she'd had no choice.

These were not small questions. I set them carefully in the newly expanded drawer that now lived in the part of me that had awakened tonight, alongside everything else that didn't yet have a name, and I resolved to return to them when I had the capacity to do them justice.

"I know you have many questions," she said softly, her hands gripping the steering wheel. I noticed her knuckles were white with tension."""
}

# Read current file
with open('/home/runner/work/BloodCraft/BloodCraft/canonical-version/book1-expanded/ch02_expanded.md', 'r') as f:
    content = f.read()

# Apply insertions
for anchor, new_content in INSERTS.items():
    if anchor not in content:
        print(f"WARNING: Anchor not found: {repr(anchor[:80])}")
    else:
        content = content.replace(anchor, new_content + anchor[len(anchor.split('\n')[0]):], 1) if '\n' in anchor else content.replace(anchor, anchor + new_content, 1)
        # Actually do it simply:
        pass

# Redo with simpler approach
with open('/home/runner/work/BloodCraft/BloodCraft/canonical-version/book1-expanded/ch02_expanded.md', 'r') as f:
    content = f.read()

for anchor_full, new_content in INSERTS.items():
    # Use first line of anchor as the actual search key
    anchor = anchor_full
    if anchor in content:
        content = content.replace(anchor, anchor + new_content, 1)
        print(f"✓ Inserted after: {anchor[:60]}...")
    else:
        print(f"✗ NOT FOUND: {anchor[:60]}...")

with open('/home/runner/work/BloodCraft/BloodCraft/canonical-version/book1-expanded/ch02_expanded.md', 'w') as f:
    f.write(content)

word_count = len(content.split())
print(f"\nFinal word count: {word_count}")
