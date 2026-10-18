# Lesson Chunks Agent

A free Hermes agent profile that turns any lesson, document or reading into **lesson chunks**: small, sequential, plain-language steps a young person can actually finish, delivered either as one interactive HTML file or drip-fed in chat before a test.

The idea comes from the Lesson Chunks AI app (lessonchunks.distinctoapps.com): complex lessons broken into digestible steps for neurodivergent learners. This is the agent edition: it runs on the family's or teacher's own machine, keeps every source and answer on disk, and can schedule the chunks over days so the knowledge is embedded before it is needed.

## What it does

1. **Ingest** any source: pasted text, a photo of a page, a PDF or a Word document.
2. **Plan** the chunks: 5 to 12 steps, one idea each, in an order that builds.
3. **Write** each chunk to a strict format spec: short sentences, under 90 words, one task per chunk, new terms defined as they appear.
4. **Gate** the result through automated quality checks: word caps, sentence length, reading level, jargon, chunk completeness.
5. **Build** a single self-contained `lesson.html` with chunk navigation, a per-chunk timer, text-to-speech, answer boxes that autosave, and clean printing.
6. **Schedule** the whole set for spaced delivery in Telegram (or WhatsApp where connected): one chunk per message, a recall question from earlier chunks, and a five-question sweep before the test date.

## Why an agent and not just the app

- The source document, the chunk plan, every answer and the final HTML live in **your folder**, readable forever.
- The app waits to be opened. The agent **knocks**: spaced delivery, retrieval practice and a pre-test sweep are built in.
- Runs **local-first**; every AI step works with frontier models online when you want them.

## Quick start

```bash
git clone https://github.com/boktoday/lesson-chunks-hermes-agent.git
cd lesson-chunks-hermes-agent
# follow INSTALL.md: copy profile.yaml and config.yaml into a new Hermes profile
hermes --profile lesson-chunks
```

Then: "Here's a lesson, chunk it for me", or paste a document. The agent creates a lesson folder under `shared/lessons/`, walks you through the plan, and hands back `lesson.html`.

## Project structure

```
skills/          eight skills: ingest, chunk-plan, chunk-write, quality-gate,
                 build-lesson, schedule-lesson, deliver-chunk, qa-tutor
templates/       lesson-shell.html (interactive single-file lesson)
                 chunker.html (browser-only splitter, no AI needed)
scripts/         build-lesson.py (chunks.json -> lesson.html)
schedules/       lesson-delivery.md (cron pattern for spaced delivery)
shared/lessons/  one folder per lesson: source/, chunks.json, answers.md, lesson.html
docs/            format-spec.md, design.md, local-models.md
```

## The format spec

The heart of the repo is `docs/format-spec.md`: one idea per chunk, 90 words max, sentences 15 words max, one task per chunk, reading level at year 8, predictable structure every time. Any model, local or frontier, that follows the spec produces the same shape.

## Licence

PolyForm Noncommercial 1.0.0: free for families, schools, churches and personal use, with credit. Commercial use by arrangement.

Built on Hermes Agent. Learn. Build. Give.
