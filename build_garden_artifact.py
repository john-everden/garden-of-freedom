#!/usr/bin/env python3
import os
from pathlib import Path
from typing import List, Tuple

# ---------------------------------------------------------------------------
# CONFIGURATION
# ---------------------------------------------------------------------------

# Repo root (assumes script is run from repo root)
REPO_ROOT = Path(__file__).resolve().parent

# Root-level files to include in the artifact
INCLUDE_ROOT_FILES: List[str] = [
    "README.md",
    "START-HERE.md",
    "START-HERE-ADVANCED.md",
    "SPEC.md",
    "RUNESTONES.md",
    "LICENSE.md",
    "CONTRIBUTING.md",
]

# Canonical Garden-critical directories
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

    # High-level architecture
    "SPEC/ETHICS",
    "SPEC/SOVEREIGN",
    "SPEC/GARDEN",
    "SPEC/GOVERNANCE",

    # Top-level SPEC files (modal ecology, tri-layer, pathfinder engine)
    "SPEC",
]

# Output artifact file
OUTPUT_FILE = REPO_ROOT / "GARDEN-ARTIFACT.md"


# ---------------------------------------------------------------------------
# HELPERS
# ---------------------------------------------------------------------------

def rel_path(path: Path) -> str:
    """Return path relative to repo root, POSIX-style."""
    return str(path.relative_to(REPO_ROOT).as_posix())


def collect_files_in_dir(dir_rel: str) -> List[Path]:
    """Collect all markdown files in a directory (recursive)."""
    base = REPO_ROOT / dir_rel
    if not base.exists():
        return []
    return sorted(p for p in base.rglob("*.md") if p.is_file())


def collect_root_files() -> List[Path]:
    files = []
    for name in INCLUDE_ROOT_FILES:
        p = REPO_ROOT / name
        if p.exists():
            files.append(p)
    return files


def build_toc(
    root_files: List[Path],
    dir_files: List[Tuple[str, List[Path]]],
) -> str:
    lines = []
    lines.append("## TABLE OF CONTENTS\n")

    if root_files:
        lines.append("- / (root)")
        for f in root_files:
            lines.append(f"  - {rel_path(f)}")
        lines.append("")

    for dir_rel, files in dir_files:
        if not files:
            continue
        lines.append(f"- /{dir_rel}")
        for f in files:
            lines.append(f"  - {rel_path(f)}")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def read_file(path: Path) -> str:
    return path.read_text(encoding="utf-8")


# ---------------------------------------------------------------------------
# MAIN BUILD LOGIC
# ---------------------------------------------------------------------------

def build_artifact() -> None:
    root_files = collect_root_files()

    dir_files: List[Tuple[str, List[Path]]] = []
    for d in INCLUDE_DIRS:
        files = collect_files_in_dir(d)
        dir_files.append((d, files))

    lines: List[str] = []

    # Header / Manifest
    lines.append("# GARDEN ARTIFACT BUNDLE")
    lines.append("### Unified Cognitive Architecture — Complete Specification\n")
    lines.append(
        "This file contains the full content of Garden-critical files:\n"
        "- Modes\n- Connectors\n- Currents\n- Protocols\n- Decision Layer\n"
        "- Ethics\n- Sovereign Layer\n- Garden Layer\n- Core Specs\n"
    )
    lines.append(
        "Use this file if you cannot download multiple files or traverse directories.\n"
    )

    # TOC
    lines.append(build_toc(root_files, dir_files))

    # Root files section
    if root_files:
        lines.append("# / (root)\n")
        for f in root_files:
            lines.append(f"## {rel_path(f)}\n")
            lines.append("```markdown")
            lines.append(read_file(f).rstrip())
            lines.append("```\n")

    # Directory sections
    for dir_rel, files in dir_files:
        if not files:
            continue
        lines.append(f"# /{dir_rel}\n")
        for f in files:
            lines.append(f"## {rel_path(f)}\n")
            lines.append("```markdown")
            lines.append(read_file(f).rstrip())
            lines.append("```\n")

    # Closing invocation
    lines.append("# END OF ARTIFACT")
    lines.append("Enter Silence (𓇳).")
    lines.append("Integrate what you have read.")
    lines.append("Return to the Garden with clarity.\n")

    OUTPUT_FILE.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    build_artifact()
    print(f"Wrote artifact to {OUTPUT_FILE}")
