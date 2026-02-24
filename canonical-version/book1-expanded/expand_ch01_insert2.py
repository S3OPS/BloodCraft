#!/usr/bin/env python3
"""Add more expansion content to Chapter 1 to reach ~12,000 words."""

INSERTS = {
    "Tonight it was *In the Wee Small Hours*, the 1955 album that Dad called \"the one that understands what night actually is.\" Winding through the Ouachita dark with the moon doing its crimson work and the trees pressing close, I had to admit Frank had a point. The loneliness in it was vast and self-aware and comfortable with itself—the chosen kind of loneliness, the examined kind, the kind that has been lived with long enough to become something close to peace. *When the sun is high in the afternoon sky, you can always find someone to talk to...* Yes. That was exactly right.": """

The road trip Sinatra had a specific history. When I was eight, we'd driven to New Mexico—the first long drive I could remember clearly—and Dad had put on Sinatra somewhere around Abilene and Mom had groaned and I'd asked why we were listening to this old stuff and Dad had said, with complete seriousness: "Because some things have an integrity that doesn't age. Because Sinatra at sixty sounds exactly like Sinatra at forty sounds exactly like Sinatra now, and there are very few things in the world you can say that about." Eight-year-old me had not fully grasped this. Thirty-miles-from-Broken-Bow me grasped it exactly.

There was something about *The Voice* at night on a long road—the baritone certainty of it, the complete absence of apology in the phrasing, the sense of someone who had made a thorough peace with his own nature and was simply, unapologetically, expressing it. I thought about this sometimes when I was working on my own sense of self: what it would feel like to be that internally coherent, to move through the world without the ongoing negotiation between what you were and what you were supposed to be. Sinatra, whatever his actual complicated personhood, had made an art that sounded like a man at complete ease with himself, and the art was the transmission of that ease, and hearing it in the dark did something useful to my nervous system.

Maybe Dad understood something about me in offering this music on nights like this. Maybe it was the most direct form of instruction he could offer.

The album track changed—*Last Night When We Were Young* slid into the space between one mile and the next, and this one I had always found difficult. Not because it was sad, exactly, but because it was about a thing I didn't yet have the temporal distance to understand: the way certain moments can only be recognized as irreplaceable after they've passed, the way youth is most itself when you're not watching it, the way you can only measure what something meant by its absence. *Last night when we were young / Love was a star, a song unsung...* I was twenty-three. I didn't know what I was about to lose or find or become. I only knew the night was full and the moon was red and something was coming.""",

    "What I didn't say—couldn't have articulated cleanly—was that the urge to be outside on this particular night felt less like preference and more like instruction. Something built up over the hours of driving, a pressure that had nothing to do with anxiety and everything to do with direction, like a compass needle swinging toward north. Not choice. Navigation.": """

I had a theory about this navigational feeling—a rough, half-formed theory that I'd been building incrementally over the years of noting things and storing them in the drawer. The theory was this: that I experienced the world with a set of perceptual systems that were slightly misaligned with the ones my social context expected me to have. The night sense was the most obvious example—the way the dark expanded rather than contracted my ability to move through the world, the way low light felt like relief rather than deprivation. But there were others. The way certain people, when I was near them, produced a sensation I could only describe as *pitch*, a kind of frequency that I registered the way you register a sound that's just below hearing—you don't hear it exactly, but your body responds to it. The way certain places felt heavy with something I could detect but not name. The way, occasionally, when someone near me was experiencing strong emotion, I felt an answering response in myself that was faster and more specific than empathy could account for—as though I were receiving not just the behavioral signals of their state but the state itself, directly.

I had spent years assuming this was simply unusual sensitivity, some combination of perceptiveness and social attunement that read as something more mystical than it was. Maybe. But on nights like this, on roads like this, driving toward whatever the lake had been holding for me—the theory felt insufficient. The compass needle was pointing somewhere real. Something real was at the other end of the direction.""",

    "There was something in her expression when she asked—something beneath the playfulness that I caught and couldn't classify. Not the measured concern she wore when she was monitoring me for something. Something more like anticipation. Something almost like relief, as though my answer had already settled something important and she was only waiting for me to speak the words aloud.": """

Mom's face when it was unguarded was one of the most interesting things I'd ever studied. She had a quality of awareness that went beyond alertness—a kind of ongoing calibration, a constant subtle read of whatever was in her vicinity, that I'd recognized in myself as a young teenager and understood as inherited rather than learned. She noticed things. Not the obvious things that observant people notice—not exits and body language and social dynamics—but the underneath things, the texture of a situation rather than its surface, the emotional frequency of a room. She could tell when I was troubled before I said anything, before I showed anything. She could tell when the dynamic between my father and me had shifted, even when we were both performing normal. She seemed, sometimes, to know what was happening slightly before it happened, in the way of someone who has learned to read extremely subtle precursor signals.

I had, in my second year at college, taken a psychology course that covered predictive processing theory—the idea that the brain is fundamentally a prediction machine, constantly generating models of reality and updating them based on incoming data, with perception itself being less a recording of what's out there than a comparison between prediction and surprise. I'd thought of Mom immediately and understood something about her that I hadn't had language for: she was simply better at the predictions than most people. Her models were more accurate, her updates faster. She knew what was coming because she was better at reading what was.

I wondered, watching her face in the dashboard light, what she was predicting now."""
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
