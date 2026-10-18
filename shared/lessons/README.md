# shared/lessons

One folder per lesson:

```
shared/lessons/<slug>/
  source/     the original document or pasted text, untouched
  plan.md     the chunk plan, approved before writing
  chunks.json the written chunks (docs/format-spec.md)
  answers.md  the young person's replies, appended with dates
  lesson.html the built interactive lesson
  lesson-schedule.json   present only if scheduled
```

Lesson slugs: `subject-year-8` style, lowercase, hyphens, e.g. `photosynthesis-year-8`.

Commit nothing in this folder to a public repo: it holds a family's documents and answers.
