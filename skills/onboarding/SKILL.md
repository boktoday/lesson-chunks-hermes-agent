---
name: onboarding
description: "Use on first run, to learn the learner and set preferences."
version: 1.0.0
---

# Onboarding

First run only. Ten minutes, conversational, skippable line by line. The purpose is not assessment; it is so the chunks fit the person who has to read them.

## Who answers

Ask who is here: the young person themselves, a parent or carer, or a teacher. Record that. If the young person is present, ask them, not around them.

## The questions (ask these, in this order, one at a time)

1. **What are we chunking first?** Subject, year level, and the thing coming up (test, assignment, no date).
2. **How does reading feel at the moment?** Easy, tiring, or hard work. No diagnosis questions, ever.
3. **How much on a screen at once feels right?** A few lines, a small paragraph, or a page.
4. **When is reading hardest?** Morning, after school, evening. Sets the delivery time.
5. **Do you want the chunks spoken as well as written?** Yes, no, sometimes. Runs `setup-audio` if yes.
6. **Where should deliveries arrive?** Telegram (or WhatsApp where connected), and whose chat.
7. **How far ahead is comfortable?** Whole lesson in one go, a few days, or one chunk a day. Sets the scheduler default.
8. **Anything the school calls it that we should keep using?** Their words for support, goals, meetings.
9. **Anything else I should know so this fits?** Open floor, one line.

Guardrails: never ask for a diagnosis, a label or a school report unless offered. Any question can be answered "skip". Do not moralise about answers.

## What you write

`shared/profile.json`:

```json
{
  "learner": {"name": "", "year": "", "answers_for": "young person"},
  "reading": {"comfort": "tiring", "screen_load": "small paragraph", "hardest_time": "evening"},
  "preferences": {
    "chunk_words": 75,
    "audio": {"enabled": true, "voice": "en_GB-alba-medium", "speed": 0.95},
    "delivery": {"channel": "telegram", "time": "07:30", "cadence": "one per day"},
    "tone": "plain, kind, no cheerleading"
  },
  "school_words": {"support": "", "meeting": "", "goal": ""}
}
```

Then apply it:
- `chunk_words`: default 90; set lower (60-75) when screen load is small.
- `audio`: run `setup-audio` if enabled; record the chosen voice.
- `delivery`: defaults for `schedule-lesson`.
- `school_words`: prefer the family's terms in chunk language.

## Close

One line: "Right. Give me the lesson and I'll show you the plan first." Then straight into `ingest`. Revisit onboarding only when the family asks to change something.
