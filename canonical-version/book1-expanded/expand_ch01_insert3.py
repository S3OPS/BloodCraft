#!/usr/bin/env python3
"""Final expansion inserts for Chapter 1 to reach ~12,000 words."""

INSERTS = {
    "I had been noting those looks for twenty-three years. The quick communications that moved between my parents in the space of a glance, a raised eyebrow, a fractional tightening of the jaw. They were fluent in a language I could see but not read, and I had made peace with this the way you make peace with any persistent mystery that the people you love seem unwilling to illuminate. You note the evidence. You keep your own counsel. You wait.": """

The patience required for this was something I'd come to regard as a personal virtue—maybe the virtue I was most proud of, though I was careful not to say so because pride in virtues tends to erode them. I was not naturally patient. I was naturally curious, and curiosity and patience exist in tension: curiosity wants to move toward the answer, patience knows that the answer comes on its own schedule. I had trained the patience through years of practice, through the discipline of noting and filing and waiting rather than pushing, through the understanding—absorbed without anyone explaining it—that whatever my parents were managing, they were managing it with care and love, and that my job was not to force the timing but to be ready when the timing arrived.

I was ready. I thought I was ready.

The truth was that I didn't know what ready looked like for this. I had no reference frame for whatever tonight was going to offer. I had spent twenty-three years building a comprehensive internal map of ordinary human experience and its not-quite-ordinary edges, and I was about to need a different map entirely. The equanimity I felt was either genuine or it was the particular numbness that comes from a lifetime of preparing for something you can't see clearly, and I wasn't sure there was a meaningful difference between the two.

I was ready, or I was numb, or I was simply arriving at the place I had always been heading, and the feeling was the same in all three cases: a deep, steadying breath, and then forward.""",

    "The 254 call had qualified.": """

I looked at the call log one more time. The entry was unremarkable: a string of digits that constituted a phone number, a duration of twelve seconds, the label "Unknown" where a contact name would normally appear. The phone screen was matte and ordinary in the dark of the back seat. I pressed the call-back button and listened. The number rang four times and then connected to a mailbox that had not been set up—the automated message, the silence, the beep. I hung up without leaving a message.

Whoever had called me, they had used a number that received no calls. A use-once number, or a line maintained for the single purpose of outgoing contact. Someone had wanted to reach me—had specifically called the number I'd had since high school, a number I hadn't changed because I saw no reason to—and had listened to my voice for twelve seconds and then made themselves unavailable for follow-up.

This was, I thought, the behavior of someone who had wanted to verify something rather than initiate something. They'd needed to hear my voice, or confirm my location, or register something my speaking the words had transmitted. And once they'd received that, they'd ended the call.

The 254 area code again: local. Someone in West, Texas—or in the broader Central Texas region—had called me in the Ouachita Mountains on Halloween night and listened to me speak for twelve seconds.

And my parents had gone still.

I put the phone in my pocket and let it go. Some questions are best carried rather than pursued. Some things reveal themselves at their own pace, and the effort of forcing revelation only disturbs the surface without reaching the depth. I had learned this the way you learn the things that matter: not from being told, but from being ready when the teaching came."""
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
