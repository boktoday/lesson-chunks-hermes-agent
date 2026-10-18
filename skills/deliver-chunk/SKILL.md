---
name: deliver-chunk
description: "Use from a cron, to send one chunk and take the reply."
version: 1.0.0
---

# Deliver chunk

One message, one chunk, and then listen.

## The message

First delivery of a schedule opens with one line: "Brendan's assistant here. Lesson chunks for {subject}, one a day. Reply 'pause' any time."

Every delivery after that:

```
Chunk {n} of {total}: {title}

{body}

Do: {do}

Reply with your answer. 'Don't get it' if you want it another way.
```

- On chunks after the first, add one recall line at the top: the `recall` question assigned by the schedule, answered from memory before reading the new chunk.
- No emoji walls, no exclamation marks, no encouragement padding. British English.
- Quiet hours respected; delivered times logged to `answers.md`.

## Handling replies

1. **An answer** → append to `answers.md` with date and chunk id, reply in one line ("Saved. Chunk {n} done."). If the answer shows a misunderstanding, say so kindly and offer the expanded version.
2. **"Don't get it" / confused** → resend that chunk expanded: one extra concrete example, same limits, clearly marked "Chunk {n}, slower version". Do not skip ahead.
3. **"Pause"** → disable the lesson's remaining jobs, reply "Paused." Resume only on request.
4. **Something personal or distressing** → stop the lesson, be plain and kind, point to a trusted adult (and the helplines note in this repo's hard-moments reference if present). Never counsel.
5. **Nothing** → nothing. No follow-ups to an unanswered chunk; the schedule sends the next anyway.

## Quiz sweep

The evening before the deadline, send the `quiz` array: five questions, numbered, one line each: "Answer in one message or one at a time." Save answers, mark obvious misses against the chunks, and finish with one line on what to reread (chunk numbers). No scores, no grades.
