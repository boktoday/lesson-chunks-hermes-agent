---
name: setup-audio
description: "Use during onboarding, to install Piper and enable narration."
version: 1.0.0
---

# Setup audio (Piper)

Spoken versions of the chunks and the whole document, generated on this machine. Once, at onboarding, then never again unless the voice changes.

## Step 1: check

```bash
python -c "import piper" 2>/dev/null && echo installed || echo missing
python -m piper --help
```

If both fail, install it (step 2). If either works, skip to step 3.

## Step 2: install (one command, no GPU)

Let the adult choose the interpreter: the one Hermes runs with is simplest.

```bash
pip install piper-tts
```

A virtual environment is tidier and avoids clashes:

```bash
python -m venv ~/.lesson-chunks-tts
# Windows: %LOCALAPPDATA%\lesson-chunks-tts
~/.lesson-chunks-tts/bin/pip install piper-tts      # Windows: Scripts\pip.exe
```

~40MB of wheels (onnxruntime) and about 63MB per voice. Repeatable on Windows, macOS, Linux, and Raspberry Pi 4 or better.

## Step 3: choose a voice

Ask the adult, with samples if they want. British voices suit this house by default:

- `en_GB-alba-medium` (default; warm female, Scottish)
- `en_GB-jenny_dioco-medium` (friendly female)
- `en_GB-alan-medium` (male)
- `en_GB-cori-high` (higher quality, slightly slower)
- `en_US-lessac-medium` (neutral US fallback)

Download it:

```bash
python -m piper.download_voices en_GB-alba-medium
```

## Step 4: test before trusting

```bash
python -m piper -m en_GB-alba-medium -f tts-test.wav -- "Chunk one of seven. The three inputs of photosynthesis."
```

Play the file. If it sounds right, record the choice in `shared/profile.json` under `preferences.audio.voice`. If it sounds wrong or slow, try `low` tier voices; on weak hardware that halves the work.

## Step 5: wire it into lessons

`narrate-lesson.py` finds `piper` on PATH or via `python -m piper` automatically. Set the default voice once in the profile, and from then on every `build-lesson` offers to narrate:

```bash
python scripts/narrate-lesson.py shared/lessons/<slug>/chunks.json --voice en_GB-alba-medium
python scripts/build-lesson.py shared/lessons/<slug>/chunks.json
```

The player then shows real audio per chunk plus a "Listen to all" button for the full document.

## Fallback, always

If the install fails on this machine, say so plainly and use the browser voice ("Read aloud" in every lesson file). Nothing else changes. Never block a lesson on audio setup.

## Upgrades worth knowing (researched Oct 2026)

- **Kokoro-82M** (Apache-2.0): more natural than Piper, ~86MB int8 ONNX, but needs a stronger CPU and more dependencies. Offer it if the adult asks for "better sounding" and the machine is a modern laptop.
- **KittenTTS nano**: 24MB, English only, smallest credible option.
- **Supertonic 3**: 31 languages, pure ONNX.
Piper stays the default: roughly 33x real-time on CPU, one install command, runs anywhere including a Raspberry Pi. Licence note: Piper itself is GPL-3.0 now; the audio files it produces are yours to keep and share.
