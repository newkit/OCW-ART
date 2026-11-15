#!/usr/bin/env python3
"""OCW Build Diary: the command line of the art project's tool
(docs/ART-PROJECT.md). The code is the package ocwart/; `diary.py --help`
lists the commands."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from ocwart.cli import main  # noqa: E402

if __name__ == "__main__":
    main()
