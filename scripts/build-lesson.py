#!/usr/bin/env python3
"""Build lesson.html from chunks.json using templates/lesson-shell.html.

Usage: python build-lesson.py path/to/chunks.json [--out path/to/lesson.html]
Standard library only. Never edits the input.
"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
TEMPLATE = HERE.parent / "templates" / "lesson-shell.html"
PLACEHOLDER = "__LESSON_DATA__"


def main(argv):
    if len(argv) < 2:
        print("usage: build-lesson.py <chunks.json> [--out lesson.html]")
        return 2
    src = pathlib.Path(argv[1]).resolve()
    out = src.parent / "lesson.html"
    if "--out" in argv:
        out = pathlib.Path(argv[argv.index("--out") + 1]).resolve()

    data = json.loads(src.read_text(encoding="utf-8"))
    chunks = data.get("chunks") or []
    if not chunks:
        print("ERROR: chunks.json has no chunks")
        return 1
    if len(chunks) < 5:
        print("WARNING: fewer than 5 chunks (spec says 5 to 12)")

    shell = TEMPLATE.read_text(encoding="utf-8")
    if PLACEHOLDER not in shell:
        print("ERROR: template placeholder missing")
        return 1
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    html = shell.replace(PLACEHOLDER, payload, 1)
    out.write_text(html, encoding="utf-8")
    print("built %s (%d chunks, %.0f KB)" % (out, len(chunks), out.stat().st_size / 1024))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
