---
name: build-lesson
description: "Use when chunks pass the gate, to emit lesson.html."
version: 1.0.0
---

# Build lesson

Turn `chunks.json` into one self-contained `lesson.html`.

## Do

1. Confirm `quality-gate` passed (check the note in `plan.md`).
2. Run the build:

```bash
python scripts/build-lesson.py shared/lessons/<slug>/chunks.json
```

The script injects the lesson data into `templates/lesson-shell.html` and writes `shared/lessons/<slug>/lesson.html`.

3. Verify: open the file, check the chunk count matches, the first chunk renders, the timer and the read-aloud button work, and an answer typed into chunk 1 survives a reload.
4. Hand over the path. One line: "lesson.html is ready: 7 chunks, TTS on, answers save in the browser, prints clean."

## What the lesson file carries

- Chunk navigation with progress ("Chunk 2 of 7") and arrow keys.
- Per-chunk timer, count-up by default.
- Read-aloud per chunk (browser speech, works offline).
- An answer box per chunk that autosaves locally, plus "Download my answers".
- Print styles: every chunk, title supressed controls, answer lines.
- No network calls beyond the font stack; the file works offline forever.

## Boundary

Never hand-edit the emitted HTML to fix content problems; fix `chunks.json` and rebuild, so the folder stays the source of truth.
