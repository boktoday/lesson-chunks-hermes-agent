# INSTALL

## 1. Prerequisites

- Hermes Agent 0.21 or later (any platform).
- Python 3.10+ (the build script uses only the standard library).
- Optional: a frontier model key, or a local model via Ollama (see `docs/local-models.md`).

## 2. Create the profile

```bash
cp profile.yaml ~/.hermes/profiles/lesson-chunks/profile.yaml
cp config.yaml ~/.hermes/profiles/lesson-chunks/config.yaml
cp -r skills ~/.hermes/profiles/lesson-chunks/
cp -r templates ~/.hermes/profiles/lesson-chunks/
cp -r scripts ~/.hermes/profiles/lesson-chunks/
cp -r schedules ~/.hermes/profiles/lesson-chunks/
mkdir -p ~/.hermes/profiles/lesson-chunks/shared/lessons
```

(On Windows the profile root is `%LOCALAPPDATA%\hermes\profiles\lesson-chunks`.)

## 3. Model

Edit `profile.yaml`: set `model.default` and `model.provider` to whatever you run (default: deepseek-v4-flash). For a fully local setup, point it at Ollama and see `docs/local-models.md`.

## 4. First run

```bash
hermes --profile lesson-chunks
```

First run starts with the onboarding questions (skills/onboarding). Answer or skip; it writes `shared/profile.json`.

If the family wants spoken chunks, run the `setup-audio` skill: one `pip install piper-tts`, one voice download (~63MB), one test sentence. Then `scripts/narrate-lesson.py` adds audio to every lesson and `build-lesson.py` embeds it.

Try: "Here is a lesson, chunk it for me:" then paste a few paragraphs. You should get a plan, then chunks, then a working `lesson.html` in `shared/lessons/<slug>/`.

## 5. Scheduling (optional)

Telegram (or WhatsApp where your Hermes gateway has it connected) must already be wired for the profile. Then the agent can install lesson crons via `schedule-lesson`. Test with one lesson before trusting it with a deadline.
