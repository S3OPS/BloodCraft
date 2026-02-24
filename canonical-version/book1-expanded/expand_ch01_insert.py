#!/usr/bin/env python3
"""Insert expansion blocks into Chapter 1 to reach ~12,000 words."""

import re

INSERTS = {
    # Anchor -> inserted immediately AFTER this anchor text
    "I was beginning to suspect it was something older than me.": """

I was born at 11:58 PM on October 31st. Two minutes shy of midnight. Two minutes shy of the next day, November 1st—All Saints' Day, the day of the righteous, the day the holy dead are honored. Instead I landed on the cusp, neither fully Halloween nor fully the day that follows. Born in the last guttering minutes of the night that belongs, in every tradition I would later study, to the restless and the strange and the not-quite-living-not-quite-dead.

Dad had told me this story with a particular look on his face that I could never quite decode. Not pride, exactly. Not sentimentality. Something more like *recognition*—the look of someone who has been waiting to see if a prediction comes true and has now received the answer. He described the moment of my birth with an unusual level of detail for a man who was generally vague about emotional events: the way the hospital room had gone very quiet as the clock approached midnight, the nurse who had stood holding her breath at the corner of the room, the quality of the light, the exact sound the monitors made. He described these things the way someone describes a scene they have returned to many times in memory, examining it from different angles.

"The moon was full that night too," he said once, when I was about sixteen and asking about my birth for reasons I couldn't have articulated. "But that night it was just—silver. Just the normal color." He paused. "I remember being relieved about that."

I had asked him why. He had smiled and said, "Just a superstition," and changed the subject with the practiced ease of a man who had changed many subjects on many occasions. But I had heard, in those four words and that pause, something that wasn't quite a lie and wasn't quite the truth: a careful navigation around something that couldn't be said directly.

Just a superstition. I had filed it in the drawer. The drawer was getting full.

Growing up with a Halloween birthday is a particular experience that creates a particular kind of person. The holiday becomes personal in a way other children's birthdays are not—you don't just observe it, you inhabit it, you are constitutionally entangled with it. For most of my childhood I loved this without reservation. The whole world decorated for my birthday. The whole world dressed in the aesthetics of darkness and magic and the uncanny as an annual celebration. The candy was incidental. What I loved was the atmosphere: the permission, on this one night, for the eerie to be acknowledged, for the ordinary world to admit what it spent the rest of the year pretending wasn't there.

Other kids treated Halloween as a costume party. I treated it as something more like a homecoming.

As I got older and read more widely, I came across the historical and anthropological layers beneath the candy and the costumes: Samhain, the Celtic feast of the dead; the thinning of the veil between worlds that various traditions described as happening specifically at this time of year; the medieval church's strategic layering of All Saints' and All Souls' Day over an older, more complicated holiday; the persistent cross-cultural belief that the last day of October was when whatever separated the visible from the invisible became briefly, dangerously permeable. I read these things with the particular recognition of someone who has been living adjacent to a concept without having its name. I had always felt the thinning. I had just never had a word for it.

On Halloween night, the world felt like it was breathing differently. Slower, deeper, as though it had briefly remembered something it spent the rest of the year forgetting. On Halloween night, the darkness had texture and weight and a quality of attention that I found not frightening but deeply, specifically comforting—the comfort of a sensory environment that matched something internal, the relief of the outside world finally resembling the inside one.

Twenty-three Halloweens. Twenty-three years of the world, for one night, making sense.""",

    "I was thinking about them now, watching the reddish moon track our car through the Ouachita dark, wondering if that drawer was finally ready to come unstuck.": """

The drawer metaphor was one I'd developed somewhere around age fourteen, when I realized that what I was doing with the things I noticed and couldn't explain was not forgetting them but storing them. Deliberately. Systematically. As though some part of me knew that a day would come when the drawer would open and the contents would be needed, and until that day the most useful thing was to keep careful inventory without disturbing the arrangement.

The contents were numerous. The back-door night when I was five or six. The overheard conversations about timing. The way my parents went alert at any unexpected contact—a stranger knocking, an unknown car on the road, a phone call from an unfamiliar number. The inexplicable physical responses I had to certain stimuli: the particular quality of attention I felt when I was near someone who was bleeding (not squeamishness, which would have been normal; something more like a sharpening of focus, a heightening of all sensory input that I found alarming and tried to suppress). The fact that I healed unusually quickly from minor injuries—a bruise that should have lasted a week gone in two days, a cut that closed before I'd finished cleaning it. The dreams, recurring since childhood, of vast dark spaces and a voice I recognized but couldn't place, speaking in a language I almost understood.

I had compartmentalized all of these things efficiently. I was good at compartmentalization. It was, I thought, one of my more useful skills—the ability to note something, file it, and proceed with the day without the unresolved thing bleeding into the rest of my functioning. Dad was similar in this way. Mom less so—she was more likely to sit with an unresolved thing, to turn it over, to live inside the uncertainty until it resolved itself. But she was also, I had come to understand, the one who understood it better. The drawer made sense to Dad. The contents of the drawer were something he was working with differently: not storing, but timing. Waiting for something. The right moment.

Maybe tonight was the right moment.

The moon shifted slightly as the road curved, slipping behind a stand of pines before reemerging larger and redder than before, and the feeling in my chest that I'd been managing all evening pulsed once, hard, like a second heartbeat. I put my hand flat against my sternum and held it there. Under my palm, my own heartbeat was steady and unremarkable. But beneath it, or alongside it, or woven through it—something else. Older. Slower. Patient in the way that very old things are patient, because they have learned that time is abundant and the right moment always comes.""",

    "I wish I had asked her what she was working out. I had twenty-three years of Friday nights and I let them pass without asking.": """

There was one film in particular—I came across it when I was about fifteen, late at night while my parents thought I was asleep—that I watched three times in a row and then deleted from the browser history with the careful efficiency of someone who senses they've touched something private. It was not a major film. A small European production, subtitled, about a family of ancient vampires living in a contemporary city, maintaining their secrecy not through violence but through care—through the cultivation of specific, chosen relationships with humans who knew what they were and chose them anyway. The humans in the film were not victims. They were partners. They were people who had been told a true and terrible and magnificent thing about the world, and had decided that knowing it was worth the cost.

I had watched that film three times in one night and then never spoken of it, because something about it had cracked something open in me that I wasn't ready to examine in daylight. The specific moment: a scene in which the youngest vampire, a young man who had been made against his will and was still adjusting, asked the oldest member of his family when it had stopped feeling like loss and started feeling like—and he'd paused, searching for the word—*home*. And the oldest, a woman who carried her centuries lightly, had looked at him with an expression that was at once ancient and entirely tender, and said: *When you stopped fighting the nature of what you are and let yourself be curious about it instead.*

I was not a vampire. That was not what I was drawing from the film. What I was drawing from it was something harder to name: the image of a family that had found a way to hold a complicated truth together, to carry it across generations with care and love and the specific patience of people who understood that the right moment would come, and that until it did, the most important thing was to keep the person safe and loved and as whole as possible.

I thought about my parents' movie nights differently after that. Mom's careful attention to the older stories. The books she pulled out and read in silence afterward. The way she and Dad exchanged certain looks during certain scenes—not looks of the narrative, not tracking the plot, but something more private, more internal, as though the film were reminding them of something they carried with them always.

I had been living, I was beginning to understand, in the center of a story. I just hadn't been told the genre yet.""",

    "I think they knew—in the way they seemed to know things they wouldn't explain—that keeping me from it would have been the more dangerous choice.": """

The night wandering had its own education—a curriculum that no homeschooling syllabus could have included but that was, I suspect, more important than anything that was. I learned the behavior of every animal that moved through those forty acres after dark. The coyotes—the family in the northwest corner, usually three or four of them, their calls a form of communication I began to find almost legible after years of listening. The white-tailed deer that moved along the creek bed after midnight, the does and fawns in summer, the bucks in fall who smelled of something feral and ancient that I could detect a hundred yards away. The great horned owl that hunted the eastern edge of the property and who I identified as the same individual for six years by the particular variation in its call—a slightly lengthened first note that I thought of as a speech pattern, a verbal fingerprint.

I learned the smell of weather before it arrived—the metallic anticipation of lightning, the heavy sweetness of approaching rain in summer, the particular dry cold that preceded the ice storms of Texas winter that shut down the town for a week and left the post oaks encased in crystal. I learned the way the land communicated through sound: the specific silences that meant a predator was nearby, different from the ordinary silences of a quiet night; the change in the creek's sound that indicated it had been raining to the north; the way the wind moved differently through the grass in different seasons as the stems changed from green to gold to brown.

This was, I think now, the real education of my childhood. Not the history and mathematics and literature that Mom guided me through during daylit hours—though I was grateful for those too, and absorbed them with genuine appetite—but the night curriculum, the embodied knowledge of how to move through the dark without fear, how to read an environment that does not announce itself but can be understood if you pay attention in the right way.

I thought about this as the Oklahoma trees moved past the car windows, denser and more various than my Texas forty acres, and recognized the same quality of attention rising in me: the opening out, the expansion of perception, the way my senses sharpened when the light was low and the world stopped presenting its daytime surface and showed something more fundamental underneath. I felt, in the Ouachita dark, exactly as I had felt as a child in Riven's forest: alert, oriented, at home.

My parents had given me this, whatever it was. Whether they'd intended to, or whether it was simply what I was made of—I didn't yet know. But it was the most valuable thing I owned.""",

    "I loved it immediately. Whatever had been pulling in my chest all evening pulled a little harder.": """

The Ouachita Mountains are old mountains—among the oldest in North America, formed in the Pennsylvanian and Permian periods, five hundred million years of compression and uplift and erosion producing what is now a series of folded ridges running east-west, unusual in a continent where most ranges run north-south. They are not dramatic mountains by the standards of the Rockies or the Appalachians. They do not startle with their height. Their power is different—a settled, patient power, the authority of something that has endured long enough to have absorbed everything that happened on and through it: the Caddo people who named them in a word that means something close to *country of the big shadow*, the Cherokee who were moved here in the removal and shaped their own relationship with these ridges, the homesteaders and the oil men and the dam builders and the foresters, all of them passing through what the mountains regarded with the long perspective of deep time.

I felt this age as the car wound through the switchbacks—felt it the way you feel certain presences, not through sight or sound but through some less-named sense, the sense that detects duration and weight and the particular stillness of things that have been in place long enough to have their own gravity. The Ouachita darkness was not the darkness of my Texas flatlands—it had dimension, verticality, the sense of something standing upright in the night with its own purposes.

And the trees. The trees here were remarkable in ways I was only beginning to register. The shortleaf pines that dominated the drier ridges were tall and straight, their bark plated and reddish in the headlights, their crowns invisible in the dark above. The hardwoods in the hollows were dense and various—white oak, red oak, hickory, sweetgum, tulip poplar—growing in the mixed forest ecology of the Ouachita that is different from both the eastern deciduous forests and the southern pine flatlands. They grew with the comfort of things that belong exactly where they are, rooted in the precise soil that produced them, in no hurry, going nowhere.

Between them: darkness. The specific darkness of old forest, which is not absence but presence, not the darkness of empty space but the darkness of a space that is fully, densely occupied by lives and processes that do not require light to continue. Mycorrhizal networks threading through the soil. Insects moving in patterns that daylight interrupts. Owls and bats conducting their economies. Salamanders breathing through their skin in the wet hollows along the creek. All of it happening, all of it continuous, the darkness not an interruption of life but life's preferred medium.

I pressed my face closer to the glass and tried to see as much of it as I could. The urgency was physical—a specific hunger, distinct from anything I'd felt before in its quality and clarity. I wanted to be *in* that forest. I wanted to stand in that darkness and let it close around me and feel, finally, what I had been feeling building all evening: whatever was on the other side of the wanting.""",

    "Though I was beginning to wonder what exactly our bloodline was.": """

The question of bloodline—of what, exactly, I had inherited and from whom—had occupied me in different forms for as long as I could remember asking it. In childhood it took the form of the ordinary questions children ask about family: where did grandparents come from, why didn't we have aunts and uncles at Thanksgiving, why did Dad never talk about his childhood the way other parents talked about theirs. The answers were always gentle, deflective, technically sufficient: a family dispersed by circumstances, a difficult past that my parents had chosen to move away from, the intentional construction of a small and chosen life. These answers satisfied the child-version of me because children accept the architecture of the world they're given. They satisfied the adolescent version of me less, and the twenty-three-year-old version of me not at all.

I knew the facts of my genealogy as my parents had presented them. Dad's family was from the Pacific Northwest, the details thin on the ground—grandparents who had died before I was born, parents of his own he spoke of with an odd telescoping quality, as though the events of his childhood had occurred at a very great distance from the person speaking. Mom's family was more present: her mother, my grandmother, had visited us several times in my early childhood and had a quality about her that I found impossible to categorize—she was clearly very old, in the way of her generation, but there was something else underneath the age, something that didn't match it, a sharpness and a patience that seemed to operate on a different timescale than the rest of her. She looked at me the way Dad had looked at me on Halloween—that *recognition*, that sense of receiving an expected confirmation.

She had said something to me, on the last visit I remembered clearly, that I had filed in the drawer and returned to often. I was perhaps eight years old. She had crouched to my level—she was very tall for a woman of her apparent age, and the crouching brought her face even with mine—and she had taken my face in both hands and looked at me for a long moment and then said, quietly: "You're going to be fine. You're going to be more than fine. Just remember—the strength runs toward the kind thing, always." And then she had released me and stood and said something ordinary to my mother and the moment passed.

I had never seen her again after that visit. Mom told me, when I asked, that she had "gone to the countryside." This was apparently the extent of the available information.

The strength runs toward the kind thing, always. I had held that sentence for fifteen years, turning it over occasionally, finding in it different things at different ages. What strength? What was kind, in the particular sense she meant it? And why had she said it the way you say something you need to make sure the other person has received—not as advice, but as transmission, a thing being passed from one person to another because it cannot be held by only one of them?

The drawer was very full tonight. And the moon was very red. And we were nearly at the lake where something waited that had learned, over a very long time, the particular virtue of patience.

I pulled out my phone and looked at the call log one more time. Twelve seconds. The 254 area code glowed in the screen light. I put the phone away and looked out the window at the mountains.

My name was Riven Sixxx. The last name was unusual—Dad had explained it, when I was old enough to ask, as a family name that had been anglicized from something older, something he couldn't quite reconstruct from the records he'd found. Six generations back, the name had been different. He'd shown me the genealogical document once: a hand-written notation in what appeared to be German or possibly Old Dutch, next to a name in a script he couldn't fully read. He'd translated the notation as best he could: *the one who is both*. I'd asked both what. He'd said he didn't know.

The one who is both. I pressed my palm against the cold glass and watched the moon.""",

    '"Happy birthday, baby," she said quietly.': """

Her hand in mine was the most familiar thing in the world—the specific warmth of it, the slight roughness at the palm from her gardening, the way she squeezed once and then held steady. I had grown up holding that hand. I had held it on the first day of college orientation, standing outside the building while other students moved around us, her saying *you're ready, you've always been ready* and me not quite believing it but believing that she believed it, which was enough. I had held it three years ago when our old dog had died, the black lab mix named Ranger who had slept at the foot of my bed for eleven years, and she had held on through the whole long last hour at the vet and afterward in the car, not saying anything, just present with the weight of it. I had held it on smaller occasions too—the ordinary contact of a family that touched each other without thinking about it, the incidental communication of love through proximity.

Now, in the dark, approaching whatever waited at the lake, I held her hand and thought about everything she had not told me and everything she had given me instead of telling me, and I could not find it in myself to feel anything but grateful. Whatever was coming—whatever tonight was the beginning of—I was coming to it loved and known and held. That was not nothing. That was, perhaps, everything.

"Happy birthday, Mom," I said.

She laughed, surprised. "It's not my birthday."

"I know. But you're the reason I'm here. Seems like you should get something too."

In the front seat, I heard Dad's quiet sound—not quite a laugh, not quite a sigh. The sound he made when something moved him that he didn't want to acknowledge was moving him. The sound I associated with end-of-movie moments, with certain songs, with the rare occasions when he let himself be seen feeling something large.

"Kid," he said, and stopped.

"Yeah?"

He was quiet for a moment. Outside, the pines pressed close on either side, and the road curved once more, and the cabin lights appeared—yellow and warm in the dark, a human brightness in all the inhuman night—and the lake beyond them glittered crimson and ancient under the blood moon.

"There are things we're going to need to tell you," Dad said. "Tonight. After we're settled. Things we've—" He stopped again. Cleared his throat. "Things that should have been said before, maybe. We made choices about the timing. We thought it was right. I hope it was right."

I looked at the lake. At the moon. At the cabin that waited.

"Whatever it is," I said, "I've been waiting for it my whole life."

Another quiet from the front seat. Then Mom's hand squeezed mine—once, twice, three times. Our old code. *I love you. I love you. I love you.*

I squeezed back. Same code. Same meaning."""
}

# Read current file
with open('/home/runner/work/BloodCraft/BloodCraft/canonical-version/book1-expanded/ch01_expanded.md', 'r') as f:
    content = f.read()

# Apply insertions
for anchor, new_content in INSERTS.items():
    if anchor not in content:
        print(f"WARNING: Anchor not found: {anchor[:60]}...")
    else:
        content = content.replace(anchor, anchor + new_content, 1)
        print(f"Inserted after: {anchor[:60]}...")

# Write updated file
with open('/home/runner/work/BloodCraft/BloodCraft/canonical-version/book1-expanded/ch01_expanded.md', 'w') as f:
    f.write(content)

word_count = len(content.split())
print(f"\nFinal word count: {word_count}")
