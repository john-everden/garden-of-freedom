#!/usr/bin/env python3
import os
from pathlib import Path
from typing import List, Tuple

# ---------------------------------------------------------------------------
# CONFIGURATION
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parent
# Root files that appear at the *top* of the artifact
ROOT_TOP_FILES: List[str] = [
    "START-HERE.md",
    "RUNESTONES.md",
    "CONTRIBUTING.md",
    "CONTRIBUTOR-ONBOARDING.md",
    "REMINDERS.md",
]

# Root files that appear at the *very end* of the artifact
ROOT_END_FILES: List[str] = [
    "END-HERE.md",
]

# Canonical Garden-critical directories (operational only)
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

def read_file(path: Path) -> str:
    return path.read_text(encoding="utf-8")

# ---------------------------------------------------------------------------
# MAIN BUILD LOGIC
# ---------------------------------------------------------------------------

def build_artifact() -> None:
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

    # -----------------------------------------------------------------------
    # TOP ROOT FILES
    # -----------------------------------------------------------------------
    if ROOT_TOP_FILES:
        lines.append("# Root Files\n")
        for name in ROOT_TOP_FILES:
            f = REPO_ROOT / name
            if f.exists():
                lines.append(f"## File: {rel_path(f)}\n")
                lines.append("```markdown")
                lines.append(read_file(f).rstrip())
                lines.append("```\n")

    # -----------------------------------------------------------------------
    # DIRECTORY FILES
    # -----------------------------------------------------------------------
    for dir_rel in INCLUDE_DIRS:
        files = collect_files_in_dir(dir_rel)
        if not files:
            continue
        lines.append(f"# Directory: {dir_rel}\n")
        for f in files:
            lines.append(f"## File: {rel_path(f)}\n")
            lines.append("```markdown")
            lines.append(read_file(f).rstrip())
            lines.append("```\n")

    # -----------------------------------------------------------------------
    # END ROOT FILES (END-HERE.md)
    # -----------------------------------------------------------------------
    if ROOT_END_FILES:
        lines.append("# Final Orientation\n")
        for name in ROOT_END_FILES:
            f = REPO_ROOT / name
            if f.exists():
                lines.append(f"## File: {rel_path(f)}\n")
                lines.append("```markdown")
                lines.append(read_file(f).rstrip())
                lines.append("```\n")

    # Final marker only
    lines.append("# END OF ARTIFACT\n")

    OUTPUT_FILE.write_text("\n".join(lines), encoding="utf-8")

if __name__ == "__main__":
    build_artifact()
    print(f"Wrote artifact to {OUTPUT_FILE}")
