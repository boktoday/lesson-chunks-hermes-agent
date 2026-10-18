---
name: chunk-write
description: "Use after the plan is approved, to write the chunks to spec."
version: 1.0.0
---

# Chunk write

Write each chunk so it can be read once and finished.

## Per chunk

1. Title: 5 words max, literal ("Why leaves are green", never "Lighting up learning").
2. Body: 60 to 90 words, 2 to 5 sentences, 15 words per sentence max. One idea. Active voice where the source allows. New terms defined at first use.
3. `do`: exactly one task, under 20 words, answerable in writing in two minutes. A question about the chunk's idea, or a micro-action ("Copy the equation, then cover it and rewrite it").
4. `recall`: leave null here; the scheduler assigns recall questions when it builds delivery order.
5. `meta`: count words and estimate minutes honestly.

## Rules (from docs/format-spec.md, binding)

- No nested lists, no filler phrases, no encouragement inside the body.
- Numbers and dates as digits.
- Every fact traces to the source. Missing information becomes a teacher question in `plan.md`, never an invented line.
- If a chunk comes out over 90 words, split it; if two ideas appear, split it.

## Output

`chunks.json` in the lesson folder, matching the schema in the spec. Include `vocab` entries for every new term, each defined in one short line. After the last chunk, run `quality-gate`; do not hand anything over until it passes.
