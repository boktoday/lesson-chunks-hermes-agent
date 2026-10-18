---
name: schedule-lesson
description: "Use when a lesson should be drip-fed before a test or deadline."
version: 1.0.0
---

# Schedule lesson

Plan spaced delivery, get approval, then install the crons.

## Ask (three questions)

1. Who receives the chunks, and on which channel (Telegram, or WhatsApp where connected)?
2. When is it needed: test date, submission date, or open-ended?
3. Morning time preference (default 7:30am).

## Build the schedule

- With a deadline: front-load roughly 60 percent of chunks, one per day, leave the last day for the quiz sweep at 6:30pm the evening before.
- No deadline: two or three per week with growing gaps.
- No weekends unless the deadline is within three days.
- Everything inside 7am to 8pm local.
- Write `lesson-schedule.json` (schema in docs/design.md) into the lesson folder.

## Approve

Show the family a compact table: chunk number, title, date and time. One line each. Explicit yes before any cron is installed. Then install one cron per send time with the prompt from `schedules/lesson-delivery.md`.

## Changes

"Pause" disables the lesson's jobs and marks the schedule paused. "Resume" reinstalls from the next unsent chunk. "Test moved": rewrite remaining dates, reinstall, confirm the new table. "Don't get chunk N": deliver-chunk handles expansion; the schedule does not move.

## Boundary

The agent schedules deliveries of chunks; it never sends the lesson document itself through chat. If the family wants the HTML, they open it locally or print it.
