---
name: chunk-plan
description: "Use after ingest, to plan the chunks before writing."
version: 1.0.0
---

# Chunk plan

Decide the shape before writing a word of the lesson.

## Method

1. Read `source/lesson-text.txt` fully.
2. Find the load-bearing ideas: what must the young person understand for the test or the submission, and in what dependency order? Aim for 5 to 12 chunks.
3. Draft the plan as a table:
   - `#` order
   - chunk title (5 words max, literal)
   - one line saying what the chunk teaches
   - estimated minutes (2 to 6)
   - new terms introduced
4. Apply the structure rules from `docs/format-spec.md`: context first, one concept per chunk, example then practice, recap last.
5. List school-task alignment: which chunks cover what the teacher's task or test actually asks.
6. List open questions: anything the source leaves unclear goes here for the teacher.

## Output

Write `plan.md` in the lesson folder, then show the family a compact version: the titles with one line each, count, total minutes. Ask for a yes or a correction before any writing. If they say go, proceed straight into `chunk-write`.

## Boundary

The plan is pedagogy, not prose. No chunk bodies here. If the source is too short for 5 chunks, say so and offer to keep it as one-page notes instead.
