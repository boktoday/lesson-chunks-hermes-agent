# Design notes

## Why this exists

The Lesson Chunks AI app does one thing well: it breaks lessons into digestible steps for neurodiverse learners. Its limits: it lives in a browser tab, it waits to be opened, and the source and the work are only as durable as the browser's storage. The agent edition keeps the pedagogy and removes the limits.

## The two-layer architecture

1. **The agent does the judgement.** Ingest, plan, write, gate. Language rewriting is the value, and it needs a model. Any model that follows `docs/format-spec.md` produces the same shape.
2. **The lesson file is the product.** `build-lesson` emits a single self-contained `lesson.html`: no server, no build step, no network. It carries the app's best features: chunk navigation, per-chunk timer, text-to-speech via the browser voice (offline), answer boxes that autosave, printing. Send it by email, put it on the school LMS, open it in ten years.

3. **Optional browser-only splitter.** `templates/chunker.html` splits pasted text into chunks and generates the same interactive shell with heuristic structure only (no rewriting). Honest label: without AI it structures, it does not simplify. Include it for people with no key and no agent.

## Scheduling model (spaced delivery)

`lesson-schedule.json` per lesson:

```json
{
  "slug": "photosynthesis-year-8",
  "channel": "telegram",
  "recipient": "@youngperson",
  "deadline": "2026-10-30",
  "sweep_time": "18:30",
  "quiet_hours": "20:00-07:00",
  "chunks": [
    {"id": 1, "send": "2026-10-23T07:30"},
    {"id": 2, "send": "2026-10-24T07:30"},
    {"id": 3, "send": "2026-10-25T07:30"},
    {"id": 4, "send": "2026-10-26T07:30"},
    {"id": 5, "send": "2026-10-27T07:30"},
    {"id": 6, "send": "2026-10-28T07:30"},
    {"id": 7, "send": "2026-10-29T07:30"},
    {"id": "quiz", "send": "2026-10-29T18:30"}
  ]
}
```

Rules: front-load roughly 60 percent of chunks, one per day maximum per lesson, a quiz sweep the evening before the deadline, everything inside quiet hours. No deadline: two or three a week. A responsible adult approves the table before any cron is installed.

## What is deliberately not built

- No accounts, no cloud sync, no analytics.
- No assessment generation. qa-tutor explains; it does not write the essay.
- No gamification: encourage with a line ("Chunk 3 of 7 done"), never with points, streaks or badges. (The IEP family agent carries that pattern for families who want it; here it would add load.)
