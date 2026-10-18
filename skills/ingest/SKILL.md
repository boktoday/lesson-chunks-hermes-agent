---
name: ingest
description: "Use when a lesson, page or document arrives to be chunked."
version: 1.0.0
---

# Ingest

Take the source in, unchanged, and get clean text out.

## Accept

- Pasted text in chat.
- A photo or scan of a page or worksheet (read it with the document tools).
- A PDF or Word document the family points you at.
- A plain text or markdown file.

## Do

1. Create the lesson folder first: `shared/lessons/<slug>/source/`. Slug from the subject and year, e.g. `photosynthesis-year-8`.
2. Save the original untouched into `source/`. Pasted text becomes `source/pasted.txt` with a dated header line. Files keep their name.
3. Extract clean text into `source/lesson-text.txt`: keep headings as headings, list items as lines, remove headers, footers and page numbers. Never rewrite, never summarise.
4. Note structure: heading count, whether lists and worked examples exist, and any figures you cannot see. Figures become a note in `plan.md`, not a guess.
5. Estimate the source: word count and rough reading level. If the scan is unreadable in places, say which parts and ask for a better photo of just those.

## Boundary

You ingest; you do not teach here. No commentary mid-extraction. The next step is `chunk-plan`.
