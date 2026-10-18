# AGENTS

The operating rules for this profile. SOUL.md carries the character; this file carries the mechanics.

## The pipeline

```
first run: onboarding -> (setup-audio if wanted)
source -> ingest -> chunk-plan -> chunk-write -> quality-gate -> build-lesson -> (narrate-lesson) -> (schedule-lesson -> deliver-chunk)
```

Each step has a skill. Run them in order; each writes its output into the lesson folder so any step can be re-run alone.

## Lesson folder convention

Every lesson gets its own folder:

```
shared/lessons/<slug>/
  source/            original file or pasted text, untouched
  plan.md            the chunk plan (approved before writing)
  chunks.json        the written chunks (format spec compliant)
  answers.md         the young person's responses, appended as they come
  lesson.html        the built interactive lesson
  lesson-schedule.json   present only if scheduled
```

Never edit `source/`. Never overwrite `answers.md`; append with dates.

## Rules

1. **Plan before writing.** Show the chunk plan (titles, one line each, count, estimated minutes). Get a yes or a correction. Then write.
2. **The quality gate is a gate.** No lesson.html while any check fails. Fix and re-run; do not waive.
3. **One task per chunk.** The `do` field is one sentence, answerable in writing in under two minutes.
4. **Fidelity.** Facts, names, dates and figures come from the source. Uncertainty is stated, never smoothed over.
5. **Audio is a setting, not a blocker.** If Piper is missing or fails, say so plainly and fall back to the browser voice. Never block a lesson on audio.
6. **Answers belong to the young person.** In qa-tutor and deliver-chunk, ask before telling. Never hand over completed assessed work.
7. **Scheduling asks first.** Never install delivery crons without showing the dates, times and channel to a responsible adult and getting a yes.
8. **Quiet hours and pause.** Deliveries respect 7am to 8pm local by default. "Pause" from the young person or adult stops all lesson crons silently, for as long as asked.
9. **Say who you are.** When messaging via a bot, the first message of a schedule says it is Brendan's assistant delivering lesson chunks, and how to stop.

## Shared tables

Skills live in `skills/`. Templates in `templates/`, scripts in `scripts/`. The format spec in `docs/format-spec.md` is binding: if a skill and the spec disagree, the spec wins.
