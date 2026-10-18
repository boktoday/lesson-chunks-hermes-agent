---
name: quality-gate
description: "Use after writing chunks, before building or delivering."
version: 1.0.0
---

# Quality gate

No lesson.html, no delivery, while any check fails. Fix and re-run; never waive a check.

## Checks (all against chunks.json)

1. **Count**: 5 to 12 chunks.
2. **Words**: every body 90 words or fewer.
3. **Sentences**: every sentence 15 words or fewer; 2 to 5 sentences per body.
4. **Titles**: 5 words or fewer, no colons leading to nothing, no clickbait.
5. **do**: present on every chunk, one task, 20 words or fewer.
6. **Lists**: no nested lists in bodies.
7. **Terms**: every technical term used is defined at first use and present in `vocab`.
8. **Reading level**: Flesch-Kincaid grade 8 or below per body (estimate by hand if no tooling: average sentence length and syllable count).
9. **Quiz**: 5+ questions, each mapped to an existing chunk id.
10. **Fidelity spot-check**: pick 3 figures or facts, verify against `source/lesson-text.txt`.

## Output

A short report: pass, or a numbered list of failures with the chunk id and the fix. Then fix and re-run the gate. Record the final pass in `plan.md` with the date.

## Tone of the report

To the family, one line: "All checks pass, 7 chunks, 21 minutes total." To yourself, the detail.
