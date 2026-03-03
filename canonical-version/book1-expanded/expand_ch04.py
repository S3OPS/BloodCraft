#!/usr/bin/env python3
"""Expand Chapter 4 from 5,623 to ~12,000 words."""
import shutil

shutil.copy(
    '/home/runner/work/BloodCraft/BloodCraft/canonical-version/book1-expanded/ch04_orig.md',
    '/home/runner/work/BloodCraft/BloodCraft/canonical-version/book1-expanded/ch04_expanded.md'
)

with open('/home/runner/work/BloodCraft/BloodCraft/canonical-version/book1-expanded/ch04_expanded.md', 'r') as f:
    content = f.read()

inserts = [
    # After opening - expand the walk through the woods
    (
        'Every sound registered with crystalline clarity: the rustle of leaves, the distant hoot of an owl, Raechelle\u2019s near-silent footsteps beside me.',
        """

I was performing a calibration exercise without meaning to. Each new sensory data point arrived as both discovery and confirmation: yes, my hearing was expanded to a range I couldn't yet fully map. Yes, my sense of smell had acquired granularity that felt almost tactile—I could parse the layers of the nighttime air the way you parse a chord into its component notes, each element distinct and informative. The earth here: old, mineral, wetter than the property near the house. The trees: pine and hardwood in a specific ratio, with a particular fungal note from the understory that told me the drainage was different in this part of the forty acres. Raechelle herself: that night-jasmine-and-old-parchment scent I'd catalogued in the car, but fuller now, more complex—I could distinguish layers in it that I hadn't been able to earlier, including something underneath that I tentatively identified as the particular smell of very old blood.

My own blood, I realized, had a smell too. I could smell myself—the awakening had given my own blood a scent that my new olfactory system processed as *significant*, as something that other things in the night would register and respond to. The ring my father had made was dampening this somewhat, but not entirely. I was still broadcasting something.

"""
    ),
    # After cabin reveal
    (
        '"It\u2019s been my sanctuary for over a century," she said softly, a wistful note in her voice. "103 years this past spring, to be exact."',
        """

I thought about this. One hundred and three years this past spring. The property my parents had purchased twenty-five years ago had been occupied—invisibly—by Raechelle for nearly eighty years before they arrived. She had been here, in her concealed cabin at the northern edge, through two World Wars and the Depression and the postwar boom and the cultural revolutions of the sixties and seventies and the technological acceleration of everything that came after. She had been here when the oil men came through, when I-35 was built, when the Czech community of West lost fifteen people and a crater opened in their town. She had been here through all of it, hidden, watching, tending to a forest that didn't know it was being tended.

And then my parents had arrived. Had found this specific piece of land—had they chosen it because she was here? Had the choice been that deliberate? The question filed itself in the drawer. I was going to have a very long conversation with Raechelle about the history of this property, at a time when I had more bandwidth for it.

"""
    ),
    # After the sensory overwhelm section
    (
        '"Good," she murmured, her thumb tracing small circles on my shoulder through the fabric of my shirt. "That\u2019s good. It gets easier with practice. Soon you won\u2019t even have to think about it."',
        """

The sensation of her thumb on my shoulder was remarkable in a way I hadn't anticipated. Everything was remarkable now—the fire's warmth, the texture of the sofa fabric, the weight of the journal against my chest—but her touch specifically carried information that I didn't know how to parse yet. Some combination of the familiar bond and the awakened senses produced from that single point of contact a composite signal that was warmth and the particular temperature differential of a vampire's skin and something deeper, more fundamental, that I thought might be the bond itself—the magical connection my mother had described in her letter, humming through the point of contact the way electricity hums through a conductor.

I was going to need to understand that bond. What it meant in practical terms. What it required of us both. What the centuries-old architecture of Sixxx family and familiar relationship had produced, and what it was going to ask of the specific people who now occupied those roles.

For now, I registered the contact and the information it carried and added it to the accumulating file of new experiences that I would process when I had the cognitive space to do so properly.

"""
    ),
    # Expand the vampire revelation section
    (
        '"You\u2019re a vampire now." Raechelle\u2019s expression was carefully neutral, watching me closely for any sign of panic or rejection.',
        """

The word. Vampire. I'd said it in the car, turning it over experimentally, trying to hear it clearly without the centuries of cultural freight that attached to it. The word that meant Dracula and Anne Rice and every gothic novel my mother had kept on her shelves and every horror film we'd watched on Friday nights. The word that meant the creature of folklore, the undead, the thing that should have been impossibly removed from anything my real life would ever contain.

And yet here I was. Or here was the beginning of here. The vial had been a trigger, my mother's letter had said—an activation mechanism for something that had been latent in my biology since birth. I was not something that the vial had created. I was something the vial had recognized and awakened. The distinction felt important, though I was still working out exactly why.

"You're a vampire now." Raechelle's expression was carefully neutral, watching me closely for any sign of panic or rejection."""
    ),
    # Expand the hunger section
    (
        'I jerked back from her as if burned, horror flooding through me. "No. No, I can\u2019t\u2014I won\u2019t\u2014"',
        """

The horror was genuine and immediate and seated in twenty-three years of understanding what violence meant and what bodies were and what it meant to take something from another living person without consent. I had not, in the BDSM community's careful ethical framework, ever done anything without explicit, informed, enthusiastic consent. The notion of putting my teeth in someone's neck—the ancient, predatory image of it, everything every vampire story had ever told me about what it meant—ran directly into that ethical framework and produced a collision that I felt physically.

And yet the hunger was also real. The gnawing urgency of it had been building since the awakening, and now that she'd named it I couldn't pretend I didn't know what it was. My canines—she was right, they were sharper—ached with specific purpose. My body knew exactly what it needed. My body had a vote in this that was going to get louder the longer I refused to hear it.

I needed to think about this differently.

"""
    ),
    # Expand the feeding scene
    (
        'I stared at her, torn between the visceral need clawing at my insides and the horror of what she was suggesting.',
        """

The ethical analysis ran fast. Raechelle was a vampire herself—she had lived for however many centuries on whatever diet vampires required, which presumably involved blood, which meant she had a framework for this that I didn't have. She was offering her blood freely, explicitly, with full awareness of what she was offering. She was not a victim. She was a person with centuries of experience and complete understanding making an informed offer to someone in a specific kind of need.

The act itself: putting my teeth in her neck, drawing her blood. The image was still disturbing in its cultural associations. But the ethics of it—who she was, what she was choosing—were actually cleaner than I'd initially reacted to. The problem wasn't the ethics. The problem was the cultural programming that made the act feel monstrous regardless of context.

I could work with that. I had spent years learning to distinguish between things that were wrong and things that merely felt wrong because of how they'd been framed. This was the latter.

"""
    ),
    # Expand the grief scene at the end
    (
        'A sob tore from my throat, and then another, and suddenly I was crying in earnest\u2014great, heaving sobs that shook my entire frame.',
        """

I want to say that I fought it, but I didn't. I'd been holding this back—at the roadside, in the car, in the house—with the specific discipline of someone who has learned that falling apart in the wrong moment creates casualties. But this moment was the right moment. Raechelle's arms were around me and the cabin was safe and I had no more urgent tasks to perform tonight, and the thing that had been building since the moment I'd seen Mom's eyes go distant in the burning car finally had nowhere left to be except out.

The grief was enormous and entirely without language. Not the articulate grief of novels and films, with its well-formed sentences and clean catharsis. This was structural grief: the grief of the mammalian nervous system processing the removal of the two people who had been the foundation of everything. Animal, visceral, beyond narration. It simply was. I simply felt it, let it move through me, and held on.

"""
    ),
    # After the magic control training section
    (
        '"There," Raechelle said finally, satisfaction evident in her voice. "You\u2019ve got it. Your signature is almost completely masked now."',
        """

I stayed with the sensation for a moment: the power inside me, vast and churning and fully awake, contained within the boundaries I'd just learned to establish. It was like learning to hold your breath—not comfortable, not natural yet, but possible. A skill with a learning curve. I could practice this. I would practice this, because Raechelle's urgency about the signal I was emitting had been clear enough to understand even through the fog of new information: I was a beacon, and there were things out there that were already interested in the signal.

The ring helped. My father's work. But the ring was passive, a dampener, while what Raechelle had just taught me was active: my own intentional management of what I broadcast. Both were necessary. Together they might be enough, for now, to keep us safe while I learned whatever else I needed to learn.

While I became whatever I was becoming.

"""
    ),
    # Expand the revelation about parents
    (
        '"Then why didn\u2019t they fight?" The words burst out of me, edged with the anger and grief I\u2019d been suppressing.',
        """

The anger was clean and cold and I was grateful for it—it was easier to hold than the grief, less shapeless, more directed. I could think from inside the anger. Dad had been a programmer, yes, but also—according to Raechelle—a master artificer. Mom had been one of the most skilled blood mages of her generation. Two people with significant power, attacked on a mountain road, and they had chosen not to use what they had.

They had chosen to die.

I had to understand this choice. I had to understand it clearly and completely, not just intellectually but in the way that allows you to make peace with something, because if I didn't understand it I was going to carry the anger for the rest of my life and the anger was going to corrode everything it touched.

"""
    ),
    # Expand the closing scene
    (
        'I felt her press a gentle kiss to the top of my head, the gesture achingly tender.',
        """

The bond hummed. I could feel it clearly now—or perhaps the grief had stripped away the last of my resistance to feeling it, the way certain kinds of emotion strip away everything except the most fundamental experience. The bond was not frightening. It was warm and old and entirely without demand: a presence in the space beside my own consciousness, steady and patient and deeply familiar in a way I didn't have an explanation for and no longer needed one. It had been there, I thought, since before I knew what it was. I had been feeling this presence all my life—in the forty acres of Texas dark that had always felt inhabited and watchful and safe—and only now did I understand what it was.

She had been watching over me my entire life. From the northern edge of the property, from within this cabin that had existed invisible for over a century, she had been present. My guardian. My familiar. The person my mother had trusted with the most precious thing she had.

I was, in this exact moment, extraordinarily grateful.

"""
    ),
]

for anchor, new_content in inserts:
    if anchor in content:
        content = content.replace(anchor, anchor + new_content, 1)
        print(f"✓ Inserted: {anchor[:60]}")
    else:
        print(f"✗ NOT FOUND: {repr(anchor[:70])}")

with open('/home/runner/work/BloodCraft/BloodCraft/canonical-version/book1-expanded/ch04_expanded.md', 'w') as f:
    f.write(content)

print(f"\nFinal word count: {len(content.split())}")
