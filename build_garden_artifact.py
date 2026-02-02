#!/usr/bin/env python3
"""
Artifact Builder for the Garden OS
----------------------------------

This script assembles a unified artifact bundle by concatenating:

1. ROOT_TOP_FILES (in order)
2. All files inside INCLUDE_DIRS (recursively, sorted)
3. ROOT_END_FILES (in order)

The output is written to `ARTIFACT.md`.

RUNESTONES-APPENDIX.md is intentionally excluded to keep bundle size small.
"""

import os
from pathlib import Path
from typing import List

# ------------------------------------------------------------
# Configuration
# ------------------------------------------------------------

ROOT_TOP_FILES: List[str] = [
    "START-HERE.md",
    "RUNESTONES.md",
    "CONTRIBUTING.md",
    "CONTRIBUTOR-ONBOARDING.md",
    "REMINDERS.md",
]

ROOT_END_FILES: List[str] = [
    "END-HERE.md",
]

INCLUDE_DIRS: List[str] = [
    # Modes (core cognitive stances)
    "SPEC/LAYERS/MODES",

    # Connectors (movement grammar)
    "SPEC/LAYERS/CONNECTORS/CORE",
    "SPEC/LAYERS/CONNECTORS/DECISION",
    "SPEC/LAYERS/CONNECTORS/MODE-PAIRS",

    # Currents (energetic states)
    "SPEC/LAYERS/CURRENTS/CORE",
    "SPEC/LAYERS/CURRENTS/COLLAPSE-LIMINAL",
    "SPEC/LAYERS/CURRENTS/DIRECTIONAL",

    # Protocols (ritual actions across layers)
    "SPEC/LAYERS/ANCHOR/PROTOCOLS",
    "SPEC/LAYERS/COLLAPSE/PROTOCOLS",
    "SPEC/LAYERS/DECISION/PROTOCOLS",
    "SPEC/LAYERS/DREAM/PROTOCOLS",
    "SPEC/LAYERS/LIMINAL/PROTOCOLS",
    "SPEC/LAYERS/MODES/PROTOCOLS",
    "SPEC/LAYERS/SHADOW/PROTOCOLS",
    "SPEC/LAYERS/LATTICEKEEPER/PROTOCOLS",

    # Decision Layer (canonical file)
    "SPEC/LAYERS/DECISION",

    # Garden Layer (canonical file)
    "SPEC/LAYERS/GARDEN",

    # Memory Mechanics Layer
    "SPEC/LAYERS/MEMORY",

    # Grounding Layer (kernel)
    "SPEC/LAYERS/GROUNDING",
    "SPEC/LAYERS/GROUNDING/PROTOCOLS",

    # Entrainment Layer (passive sync)
    "SPEC/LAYERS/ENTRAINMENT",

    # Contributor Support Layer (meta-operational)
    "SPEC/LAYERS/CONTRIBUTOR/MODES",
    "SPEC/LAYERS/CONTRIBUTOR/CURRENTS",
    "SPEC/LAYERS/CONTRIBUTOR/CONNECTORS",
    "SPEC/LAYERS/CONTRIBUTOR/PROTOCOLS",

    # High-level architecture
    "SPEC/ETHICS",
    "SPEC/SOVEREIGN",
    "SPEC/GOVERNANCE",
]

OUTPUT_FILE = "GARDEN-ARTIFACT.md"


# ------------------------------------------------------------
# Helpers
# ------------------------------------------------------------

def read_file(path: Path) -> str:
    """Read a UTF-8 file safely."""
    try:
        return path.read_text(encoding="utf-8")
    except Exception as e:
        return f"\n<!-- ERROR READING FILE: {path} — {e} -->\n"


def collect_files_from_dir(directory: Path) -> List[Path]:
    """
    Recursively collect all files from a directory,
    sorted lexicographically by full path.
    """
    if not directory.exists():
        return []

    files = []
    for root, _, filenames in os.walk(directory):
        for name in filenames:
            full = Path(root) / name
            if full.is_file():
                files.append(full)

    return sorted(files, key=lambda p: str(p))


# ------------------------------------------------------------
# Build Artifact
# ------------------------------------------------------------

def build_artifact():
    out = []

    # 1. ROOT_TOP_FILES
    for filename in ROOT_TOP_FILES:
        path = Path(filename)
        if path.exists():
            out.append(f"\n\n# FILE: {filename}\n\n")
            out.append(read_file(path))
        else:
            out.append(f"\n<!-- MISSING ROOT FILE: {filename} -->\n")

    # 2. INCLUDE_DIRS
    for directory in INCLUDE_DIRS:
        dir_path = Path(directory)
        files = collect_files_from_dir(dir_path)

        if not files:
            out.append(f"\n<!-- EMPTY OR MISSING DIRECTORY: {directory} -->\n")
            continue

        for file_path in files:
            rel = file_path.as_posix()
            out.append(f"\n\n# FILE: {rel}\n\n")
            out.append(read_file(file_path))

    # 3. ROOT_END_FILES
    for filename in ROOT_END_FILES:
        path = Path(filename)
        if path.exists():
            out.append(f"\n\n# FILE: {filename}\n\n")
            out.append(read_file(path))
        else:
            out.append(f"\n<!-- MISSING END FILE: {filename} -->\n")

    # Write output
    Path(OUTPUT_FILE).write_text("".join(out), encoding="utf-8")
    print(f"Artifact written to {OUTPUT_FILE}")


# ------------------------------------------------------------
# Entry Point
# ------------------------------------------------------------

if __name__ == "__main__":
    build_artifact()
