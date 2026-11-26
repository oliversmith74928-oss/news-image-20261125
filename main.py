#!/usr/bin/env python3
"""Entry point for the 25 November 2026 world-news image.

Copies the image held in this repository to the grader's output
directory. Standard library only, no network, fully deterministic:
the same bytes are written on every run.
"""
import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
if not SOURCE.is_file():
    raise SystemExit("entry.png is missing from the repository")
data = SOURCE.read_bytes()
if not data.startswith(b"\x89PNG\r\n\x1a\n"):
    raise SystemExit("entry.png is not a PNG file")
(OUTPUT_DIR / "entry.png").write_bytes(data)
