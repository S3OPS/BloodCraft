#!/usr/bin/env python3
"""Expand Chapter 3 from 5,506 to ~12,000 words."""
import shutil

shutil.copy(
    '/home/runner/work/BloodCraft/BloodCraft/canonical-version/book1-expanded/ch03_orig.md',
    '/home/runner/work/BloodCraft/BloodCraft/canonical-version/book1-expanded/ch03_expanded.md'
)

with open('/home/runner/work/BloodCraft/BloodCraft/canonical-version/book1-expanded/ch03_expanded.md', 'r') as f:
    content = f.read()

INSERTS = []

# Insert 1: After waking up in the car - expand the disorientation
INSERTS.append((
    'For a precious\nmoment, I forgot about the accident, forgot about my parents, forgot about the blood and fire. Then reality crashed\nback, and I had to fight the urge to scream.',
    """

The forgetting lasted perhaps three seconds—the window between unconsciousness and conscious memory, when the brain has woken but the narrative hasn't yet loaded. Three seconds of just the driveway and the moonlight and the familiar smell of home, the pleasant anticipation of arrival without the reason for the journey attached to it.

And then it attached.

The grief that hit wasn't the clean, simple sadness I'd associated with loss in the abstract. It was structural—like a load-bearing wall had been removed from the architecture of my experience, and everything that had been resting on it was shifting, settling into new positions with the slow catastrophic grinding of tectonic plates. Not acute pain. Something worse: the beginning of a permanent reorganization. The world had changed its topology, and I was going to have to learn to navigate it differently forever.

I pressed my knuckles against my mouth and breathed through it. I counted to five. I looked at the line of wildflowers along the driveway, catching moonlight—Mom had planted those, years ago, Indian paintbrush and bluebonnets and coneflower, chosen for their Texas-native toughness. She said she wanted things that could survive the summers. They were surviving without her now. They would continue to do so. The wildflowers were indifferent to the fact that the woman who planted them was dead, and there was something in that indifference that I found, against all logic, stabilizing. The land went on. Whatever I was about to face, the land would go on.

I could too.

"""
))

# Insert 2: After the house description - expand the feeling of return
INSERTS.append((
    'A small, glistening tributary meanders through the heart of the forest, its clear waters whispering as they weave their\nway through, inviting exploration and adventure.',
    """

I had grown up here and I knew every dimension of it—the exact creak of the second step on the porch stairs, the way the front door stuck in humid weather, the particular quality of silence that descended on the property at 2 AM when even the coyotes had gone quiet. I knew the smell of the house in winter (woodsmoke and cardamom, Mom's spiced cider recipe) and in summer (cut grass and the particular mineral coolness of the central air) and in fall (cedar and the sharp smell of decaying leaves from the post oaks in the back).

I had left this house—was it only yesterday?—as one kind of person. I was returning as something else. The forty acres of my childhood hadn't changed. The structure of the house hadn't changed. The wildflowers in the driveway and the post oaks in the back and the seasonal creek hadn't changed.

I had changed. And the house, patient and permanent as it was, would now contain a different version of me within its familiar walls, and would not know or care about the difference.

This was, in its way, a comfort.

"""
))

# Insert 3: Expand Raechelle's answer about the scent
INSERTS.append((
    'Raechelle emphasized with purpose, but I couldn\'t help but notice it seemed like she was struggling to breathe as she\ncontinued.',
    """

I had been noticing this throughout the drive—the way she managed her proximity to me, always at a specific distance, never closer than she needed to be, her breathing controlled with what I now recognized as practiced effort. Whatever I was emanating since the awakening—the magical frequency, the pheromonal signature of my changed blood—it was affecting her in a way she was working to contain. She'd mentioned the sensitivity of her sense of smell. I was beginning to understand this wasn't a polite warning about hygiene. It was the vampire equivalent of asking someone to stand slightly upwind.

I found this information settling into a category with everything else I'd learned tonight: strange, significant, and something I would need to process thoroughly when I had more bandwidth. Currently my bandwidth was consumed entirely by the grief and the exhaustion and the new sensory information my awakened systems were generating without pause. Every room we walked through, I was receiving data—the trace scents left by my parents' daily passage through their home, the specific quality of the silence, the way the moonlight fell differently through each window. It was too much. I was going to need to learn to filter.

"""
))

# Insert 4: Expand the entry into the house
INSERTS.append((
    'The moment I crossed the threshold, a chill swept over me, an overwhelming sense of dread washing over my senses like a\ncold wave.',
    """

Raechelle paused at the threshold before entering—a slight hesitation, so brief I might have missed it if my senses hadn't been operating at their new heightened register. Old habit, I guessed. Whatever rules governed her kind, entering someone's home still had meaning attached to it. She crossed when I gestured her in, and whatever hesitation had been there was gone.

Inside: the smell of my parents. Not fresh—the traces of the last days before the trip, the accumulated scent of people who have lived somewhere for years, something indefinable and entirely specific to them that I had never consciously registered before because it had always simply been the smell of home, undifferentiated from home itself. Now I could parse it. Dad's particular soap and the coffee he ground every morning. Mom's herb garden scent carried in on her hands, lavender and thyme. The woodsmoke that lingered in the stone fireplace from the last time they'd lit a fire—two weeks ago, I thought, the night it got unexpectedly cold for October.

The smell of them was everywhere. And they were nowhere.

"""
))

# Insert 5: Expand the sacred objects section
INSERTS.append((
    'These ordinary objects—things I\'d seen a thousand times without really noticing—now felt sacred and terrible all at once.\nEach one a small monument to lives that would never return.',
    """

I picked up Mom's coffee mug. The weight of it was familiar—heavier than expected, the good ceramic, the one with the small chip on the handle from when I'd dropped it three years ago and she'd kept it anyway. The lipstick mark on the rim was her specific shade: a deep berry that she said was "practical but interesting," which was very Mom—practical but interesting, everything she did. I turned it in my hands. Set it back down exactly where it had been.

Dad's slippers. The right one slightly more compressed at the heel than the left—he had a habit of leaning on his right foot while he stood at his standing desk. The fabric was worn thin at the toe on both. He'd had these slippers for at least six years; I'd given them to him one Christmas and he'd worn them into the ground with the particular loyal devotion he extended to objects that had proven themselves comfortable. He hated replacing things that worked. He would have hated replacing these.

These were not significant objects. They were not heirlooms or artifacts or the kind of thing anyone would include in an inventory of what matters. They were just shoes, and just a mug. But they were the specific shapes of specific lives, and I was the last person who would know what those shapes meant, and the knowledge of that—the weight of being the last keeper of these meanings—settled on me with a completeness that was its own kind of devastation.

"""
))

# We need around 6,494 more words. Let's see what we have so far.
# These 5 inserts should give us roughly 1,000 words of new content.
# Need ~5,500 more. Let's add more.

# Insert 6: Finding the journal
INSERTS.append((
    'I made my way to the bookshelf first—Mom\'s domain',
    """

The house was quiet around me with that specific quality of inhabited silence that is different from ordinary silence—the silence of a space that has held people and now doesn't, that remembers the sounds that used to fill it and is not yet accustomed to their absence. I kept expecting to hear something. Dad's keyboard. Mom's voice from another room. The small ordinary sounds of two people living their lives.

What I heard instead was my own heartbeat, and Raechelle's breath behind me, and the settling of the house itself—the creak of the roof in the night wind, the tick of the pipes cooling—sounds that had always been there under the human noise but that I had never heard clearly before tonight. My awakened senses made the silence louder.

I made my way to the bookshelf first—Mom's domain""",
))

# Insert 7: Reading the journal - add emotional depth
INSERTS.append((
    'I sat down heavily on the worn leather of the armchair—Dad\'s chair—and opened the journal.',
    """

The chair still smelled of him. His particular scent—a combination of coffee and the pine soap he favored and something warm underneath that was just *him*, just the baseline human smell of my father—was embedded in the leather with years of occupation. I sat in it and breathed it in and felt the grief move through me in another of its structural waves, and I let it move. I was learning already that trying to stop these waves was like trying to stop a tide: you could hold your breath when it came over you, but you had to let it pass rather than fight it.

I opened the journal.

"""
))

for anchor, new_content in INSERTS:
    if anchor in content:
        content = content.replace(anchor, anchor + new_content, 1)
        print(f"✓ Inserted after: {anchor[:60]}")
    else:
        print(f"✗ NOT FOUND: {repr(anchor[:70])}")

with open('/home/runner/work/BloodCraft/BloodCraft/canonical-version/book1-expanded/ch03_expanded.md', 'w') as f:
    f.write(content)

print(f"\nWord count: {len(content.split())}")
