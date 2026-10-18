# Format spec: lesson chunks

Binding for every skill in this repo. If a skill and this document disagree, this document wins.

## What a chunk is

One idea, made finishable. A chunk is the smallest unit a young person can read, do something with, and tick off in roughly two to six minutes.

## Lesson object (`chunks.json`)

```json
{
  "slug": "photosynthesis-year-8",
  "title": "Photosynthesis",
  "subject": "Science, Year 8",
  "for": "young person, 13-23",
  "created": "2026-10-18",
  "source_note": "from source/lesson-text.txt, word count 812",
  "vocab": [
    {"term": "chlorophyll", "definition": "the green pigment that catches light"}
  ],
  "chunks": [
    {
      "id": 1,
      "title": "Why plants eat light",
      "body": "Plants cannot eat. So they build their own food from light, water and air. This process is called photosynthesis. It happens in the leaves, where a green pigment called chlorophyll catches the light.",
      "do": "In one sentence: what does photosynthesis turn light into?",
      "recall": null,
      "meta": {"words": 42, "minutes": 2}
    }
  ],
  "quiz": [
    {"q": "Name the three inputs a plant needs for photosynthesis.", "source_chunk": 2}
  ]
}
```

## Hard limits (the quality gate enforces all of these)

| Rule | Limit |
|---|---|
| Chunks per lesson | 5 to 12 |
| Body length | 90 words maximum, 60 typical |
| Sentence length | 15 words maximum |
| Sentences per chunk | 2 to 5 |
| Chunk title | 5 words maximum, literal |
| `do` task | exactly one, under 20 words, writable answer in 2 minutes |
| Reading level | Flesch-Kincaid grade 8 or below (year 8) |
| New terms | defined on first use, also listed in `vocab` |
| Nested lists | never inside a chunk body |
| Quiz | 5 questions minimum, each mapped to a chunk |

## Structure rules

1. **Build order.** Context or a hook first, then one concept per chunk, worked example, practice, recap last. Every lesson ends on a chunk that revisits the first idea.
2. **Predictable template.** Every chunk renders the same way: title, body, one task. Surprise is a tax on attention.
3. **One new idea per chunk.** If a chunk teaches two things, split it.
4. **Concrete before abstract.** Name the thing, then the mechanism.
5. **No filler.** No "as we all know", no encouragement padding inside the body; encouragement belongs in delivery, not in the text.
6. **Active voice, present tense** where the source allows.
7. **Numbers and dates as digits.** "1945", not "nineteen forty-five".

## Recall and quiz

- `recall` on a chunk is a one-line question from a chunk at least one step back. The scheduler fills these in as it assigns delivery order.
- The `quiz` array is the pre-test sweep: five questions across the whole lesson, each traceable to a chunk.

## Voice for delivery (chat messages)

- Address the young person directly: "Chunk 3 of 7: Why leaves are green."
- One message per slot. Body, then the task, then (later chunks) one recall line.
- British English, no em dashes, no guilt, no streak pressure. "Done" and "paused" are complete answers.
- Never the local word for teen; this repo is for young people.

## Fidelity

- Every fact in a chunk traces to the source. Quotes keep their original wording where wording matters.
- If the source is wrong on a plain factual matter, write the chunk correctly and add a note to `plan.md`, never silently.
- Missing information becomes a question to the teacher, listed in `plan.md`, not an invented chunk.
