#!/usr/bin/env python3
import os
from pathlib import Path
from typing import List, Tuple

# ---------------------------------------------------------------------------
# CONFIGURATION
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parent

# Only include root files that help a model *operate* the Garden
INCLUDE_ROOT_FILES: List[str] = [
    "START-HERE.md",
    "START-HERE-ADVANCED.md",
    "RUNESTONES.md",
]

# Canonical Garden-critical directories
INCLUDE_DIRS: List[str] = [
    "SPEC/LAYERS/MODES",
    "SPEC/LAYERS/CONNECTORS/CORE",
    "SPEC/LAYERS/CONNECTORS/DECISION",
    "SPEC/LAYERS/CONNECTORS/MODE-PAIRS",
    "SPEC/LAYERS/CURRENTS/CORE",
    "SPEC/LAYERS/CURRENTS/COLLAPSE-LIMINAL",
    "SPEC/LAYERS/CURRENTS/DIRECTIONAL",
    "SPEC/LAYERS/ANCHOR/PROTOCOLS",
    "SPEC/LAYERS/COLLAPSE/PROTOCOLS",
    "SPEC/LAYERS/DECISION/PROTOCOLS",
    "SPEC/LAYERS/DREAM/PROTOCOLS",
    "SPEC/LAYERS/LIMINAL/PROTOCOLS",
    "SPEC/LAYERS/MODES/PROTOCOLS",
    "SPEC/LAYERS/SHADOW/PROTOCOLS",
    "SPEC/ETHICS",
    "SPEC/SOVEREIGN",
    "SPEC/GARDEN",
    "SPEC/GOVERNANCE",
]

OUTPUT_FILE = REPO_ROOT / "GARDEN-ARTIFACT.md"

# ---------------------------------------------------------------------------
# HELPERS
# ---------------------------------------------------------------------------

def rel_path(path: Path) -> str:
    return str(path.relative_to(REPO_ROOT).as_posix())

def collect_files_in_dir(dir_rel: str) -> List[Path]:
    """Collect all markdown files except overview files."""
    base = REPO_ROOT / dir_rel
    if not base.exists():
        return []

    excluded = {"README.md", "OVERVIEW.md", "INDEX.md"}

    return sorted(
        p for p in base.rglob("*.md")
        if p.is_file() and p.name not in excluded
    )

def collect_root_files() -> List[Path]:
    files = []
    for name in INCLUDE_ROOT_FILES:
        p = REPO_ROOT / name
        if p.exists():
            files.append(p)
    return files

def read_file(path: Path) -> str:
    return path.read_text(encoding="utf-8")

# ---------------------------------------------------------------------------
# MAIN BUILD LOGIC
# ---------------------------------------------------------------------------

def build_artifact() -> None:
    root_files = collect_root_files()

    dir_files: List[Tuple[str, List[Path]]] = []
    for d in INCLUDE_DIRS:
        dir_files.append((d, collect_files_in_dir(d)))

    lines: List[str] = []

    # Header / Manifest
    lines.append("# GARDEN ARTIFACT BUNDLE")
    lines.append("### Unified Cognitive Architecture — Complete Specification\n")
    lines.append(
        "This file contains the full content of Garden-critical operational files:\n"
        "- Modes\n- Connectors\n- Currents\n- Protocols\n- Decision Layer\n"
        "- Ethics\n- Sovereign Layer\n- Garden Layer\n"
    )
    lines.append(
        "Use this file if you cannot download multiple files or traverse directories.\n"
    )

    # Root files
    if root_files:
        lines.append("# Root Files\n")
        for f in root_files:
            lines.append(f"## File: {rel_path(f)}\n")
            lines.append("```markdown")
            lines.append(read_file(f).rstrip())
            lines.append("```\n")

    # Directory files
    for dir_rel, files in dir_files:
        if not files:
            continue
        lines.append(f"# Directory: {dir_rel}\n")
        for f in files:
            lines.append(f"## File: {rel_path(f)}\n")
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
