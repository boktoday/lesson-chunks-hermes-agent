# Schedule: lesson delivery

How scheduled chunks reach the young person. One cron job per scheduled lesson.

## The cron prompt (template)

> Deliver chunk {N} of {lesson title} to {recipient} on {channel}; full instructions in skills/deliver-chunk/SKILL.md; lesson folder shared/lessons/{slug}/. After sending, log the delivery time to answers.md.

Install with the Hermes scheduler at each time in `lesson-schedule.json`. One job per send time (schedules change; individual jobs are easier to move or pause than one clever job).

## Defaults

- Morning deliveries 7:30am, quiz sweep 6:30pm the evening before the deadline.
- Never outside 7am to 8pm local unless the family sets otherwise.
- Weekends: off unless the deadline is within 3 days.
- One message per lesson per day, maximum.

## Pause and resume

"Pause" disables every job for that lesson (the agent keeps the schedule file, marks `"paused": true`). "Resume" re-installs from the next unsent chunk. "Test moved to X" rewrites the remaining dates and reinstalls.
