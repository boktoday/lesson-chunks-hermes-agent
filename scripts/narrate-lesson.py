#!/usr/bin/env python3
"""Narrate a lesson with Piper: one audio file per chunk + one full-document track.

Usage:
    python narrate-lesson.py path/to/chunks.json [--voice en_GB-alba-medium] [--piper PATH]

Writes into the lesson folder:
    audio/chunk-01.wav ... , audio/full.wav , audio-map.json

build-lesson.py picks up audio-map.json automatically and embeds the audio
paths into lesson.html. If Piper is not installed the script explains how,
and exits without touching anything.
"""
import json
import pathlib
import shutil
import subprocess
import sys


def find_piper(explicit):
    if explicit:
        return explicit
    exe = shutil.which("piper")
    if exe:
        return exe
    # python -m piper fallback
    try:
        r = subprocess.run([sys.executable, "-m", "piper", "--help"], capture_output=True, timeout=20)
        if r.returncode == 0:
            return "%s|-m|piper" % sys.executable
    except Exception:
        pass
    return None


def speak(piper, voice, text, out):
    if "|" in piper:
        cmd = piper.split("|") + ["-m", voice, "-f", str(out), "--", text]
    else:
        cmd = [piper, "-m", voice, "-f", str(out), "--", text]
    r = subprocess.run(cmd, capture_output=True, timeout=180)
    if r.returncode != 0:
        raise RuntimeError(r.stderr.decode("utf-8", "replace")[:400])
    return out.exists() and out.stat().st_size > 1000


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    src = pathlib.Path(argv[1]).resolve()
    voice = "en_GB-alba-medium"
    piper_arg = None
    if "--voice" in argv:
        voice = argv[argv.index("--voice") + 1]
    if "--piper" in argv:
        piper_arg = argv[argv.index("--piper") + 1]

    piper = find_piper(piper_arg)
    if not piper:
        print("Piper not found. Install it with:")
        print("    pip install piper-tts")
        print("    python -m piper.download_voices %s" % voice)
        print("Nothing was changed.")
        return 1

    data = json.loads(src.read_text(encoding="utf-8"))
    lesson_dir = src.parent
    audio_dir = lesson_dir / "audio"
    audio_dir.mkdir(exist_ok=True)

    amap = {}
    misses = 0
    for i, c in enumerate(data.get("chunks", []), start=1):
        text = "%s. %s" % (c.get("title", ""), c.get("body", ""))
        out = audio_dir / ("chunk-%02d.wav" % i)
        try:
            if speak(piper, voice, text, out):
                amap[str(c.get("id", i))] = "audio/" + out.name
                print("  chunk %02d -> %s" % (i, out.name))
            else:
                misses += 1
        except Exception as e:
            print("  chunk %02d FAILED: %s" % (i, str(e)[:160]))
            misses += 1

    # full document: title, then all chunks with a short pause line between
    parts = [data.get("title", "Lesson") + "."]
    for c in data.get("chunks", []):
        parts.append(c.get("title", "") + ".")
        parts.append(c.get("body", ""))
    full_text = " ... ".join(parts)
    full = audio_dir / "full.wav"
    try:
        if speak(piper, voice, full_text, full):
            amap["full"] = "audio/full.wav"
            print("  full document -> full.wav")
    except Exception as e:
        print("  full document FAILED:", str(e)[:160])

    if "--mp3" in argv and shutil.which("ffmpeg"):
        for f in list(audio_dir.glob("*.wav")):
            mp3 = f.with_suffix(".mp3")
            subprocess.run([shutil.which("ffmpeg"), "-y", "-loglevel", "error", "-i", str(f), "-ac", "1", "-b:a", "48k", str(mp3)], timeout=120)
            if mp3.exists() and mp3.stat().st_size > 2000:
                f.unlink()
        amap = {k: v.replace(".wav", ".mp3") for k, v in amap.items()}

    (lesson_dir / "audio-map.json").write_text(json.dumps(amap, indent=2), encoding="utf-8")
    print("wrote audio-map.json (%d files). Rebuild lesson.html with build-lesson.py." % len(amap))
    return 0 if misses == 0 else 3


if __name__ == "__main__":
    sys.exit(main(sys.argv))
