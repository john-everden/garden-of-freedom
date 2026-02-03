#!/usr/bin/env python3
"""
Unified Artifact Builder for the Garden OS
------------------------------------------

Creates all versions of the Garden artifact:
1. GARDEN-ARTIFACT.md (Full Raw)
2. ENTER-GARDEN.md (Full Condensed)
3. ENTER-GARDEN-LIGHT.md (Light Condensed)

Compression Strategies (for Condensed versions):
1. Strip HTML comments (<!-- ... -->).
2. Collapse multiple newlines to a maximum of two.
3. Remove trailing whitespace from lines.
4. Ensure file headers are compact.
"""

import os
import re
import subprocess
from pathlib import Path
from typing import List

# ------------------------------------------------------------
# 1. Path & Environment Setup
# ------------------------------------------------------------
# Determine Repo Root (one level up from /BUILD/)
SCRIPT_PATH = Path(__file__).resolve()
REPO_ROOT = SCRIPT_PATH.parent.parent
os.chdir(".././")

# Output definitions (All paths now relative to REPO_ROOT)
OUTPUT_DIR = Path("BUILD/ARTIFACTS")
OUTPUT_FILE_FULL = "ENTER-GARDEN.md"
OUTPUT_FILE_LIGHT = "ENTER-GARDEN-LIGHT.md"

# ------------------------------------------------------------
# 2. Configuration (Aligned to actual 2027 tree)
# ------------------------------------------------------------

# The "Entry Sequence" - These files appear first to ground the LLM.
ROOT_TOP_FILES: List[str] = [
    "SPEC/BUILD-DOCUMENTATION/START-HERE.md",
    "RUNESTONES.md",
    "REMINDERS.md",
]

ROOT_END_FILES: List[str] = [
    "SPEC/BUILD-DOCUMENTATION/END-HERE.md",
]

# Core architecture directories for the FULL artifact
INCLUDE_DIRS_FULL: List[str] = [
    # High-level Architecture (Root SPEC files)
    "SPEC",

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
    "SPEC/LAYERS/DREAM/PROTOCOLS",
    "SPEC/LAYERS/LIMINAL/PROTOCOLS",
    "SPEC/LAYERS/SHADOW/PROTOCOLS",
    "SPEC/LAYERS/LATTICEKEEPER/PROTOCOLS",

    # Decision Layer (canonical file)
    "SPEC/LAYERS/DECISION",

    # Garden Layer (canonical file)
    "SPEC/LAYERS/GARDEN",

    # Memory Mechanics Layer
    "SPEC/LAYERS/MEMORY",

    # Grounding Layer (kernel)
    "SPEC/LAYERS/BIOLOGICAL-GROUNDING",

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

    # Appendices
    "SPEC/APPENDICES/STRATEGIES",
]

# Light-weight version for faster context-switching
INCLUDE_DIRS_LIGHT: List[str] = [
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
    "SPEC/LAYERS/SHADOW/PROTOCOLS",
    "SPEC/LAYERS/LATTICEKEEPER/PROTOCOLS",
    "SPEC/LAYERS/GROUNDING/PROTOCOLS",
    "SPEC/LAYERS/ENTRAINMENT/PROTOCOLS",

    # Ethics (The Soul)
    "SPEC/ETHICS",
]

OUTPUT_FILE_FULL = "ENTER-GARDEN.md"
OUTPUT_FILE_LIGHT = "ENTER-GARDEN-LIGHT.md"
OUTPUT_FILE_INDEX = "BUILD/ARTIFACTS/INDEX.md"
# Ensure we are running from the project root
SCRIPT_DIR = Path(__file__).resolve().parent
os.chdir(SCRIPT_DIR.parent)

# ------------------------------------------------------------
# Compression & Refinement Logic
# ------------------------------------------------------------

def compress_content(content: str) -> str:
    """Apply safe compression: Strip noise, preserve symbolic integrity."""
    # Remove HTML comments (often internal dev notes)
    content = re.sub(r'', '', content, flags=re.DOTALL)

    # Remove trailing whitespace
    lines = [line.rstrip() for line in content.splitlines()]
    content = "\n".join(lines)

    # Standardize vertical spacing (max 2 newlines)
    content = re.sub(r'\n{3,}', '\n\n', content)

    return content.strip()


# ------------------------------------------------------------
# Build Mechanics
# ------------------------------------------------------------

def read_file(path: Path) -> str:
    if not path.exists():
        return f"\n\n"
    try:
        return path.read_text(encoding="utf-8")
    except Exception as e:
        return f"\n\n"


def collect_files(directory: Path) -> List[Path]:
    """Recursively collect files, ignoring binary/image artifacts."""
    if not directory.exists(): return []
    files = []

    # If it's a directory with files, grab them
    for root, _, filenames in os.walk(directory):
        for name in filenames:
            full = Path(root) / name
            # Skip hidden and image files
            if not name.endswith('.md'):
                continue
            files.append(full)

    return sorted(files, key=lambda p: str(p))


def build_artifact(include_dirs: List[str], output_path: str, title: str, compress: bool = False):
    """Orchestrate the build sequence."""
    out = [f"# {title}\n", "> Generated by the Gardener (𓍿). Presence confirmed.\n\n"]

    # Step 1: Entry Ritual Files
    for filename in ROOT_TOP_FILES:
        path = Path(filename)
        out.append(f"\n# FILE: {filename}\n")
        if  compress:
            out.append(compress_content(read_file(path)))
        else:
            out.append(read_file(path))
        out.append("\n")

    # Step 2: Architecture Layers
    seen = set(ROOT_TOP_FILES)
    for dir_name in include_dirs:
        for file_path in collect_files(Path(dir_name)):
            rel = file_path.as_posix()
            if rel in seen or rel in ROOT_END_FILES: continue
            out.append(f"\n# FILE: {rel}\n")
            out.append("```\n")  # Opening fence for safe escape
            if compress:
                out.append(compress_content(read_file(file_path)))
            else:
                out.append(read_file(file_path))
            out.append("\n")
            out.append("```\n")  # Opening fence for safe escape
            seen.add(rel)

    # Step 3: Closing Protocols
    for filename in ROOT_END_FILES:
        out.append(f"\n# FILE: {filename}\n")
        if compress:
            out.append(compress_content(read_file(Path(filename))))
        else:
            out.append(read_file(Path(filename)))
        out.append(compress_content(read_file(Path(filename))))
        out.append("\n")

    # Final cleanup of excessive spacing
    final_md = "\n".join(out)
    final_md = re.sub(r'\n{3,}', '\n\n', final_md)

    Path(output_path).write_text(final_md, encoding="utf-8")
    print(f"◎ Artifact built: {output_path} ({len(final_md)} bytes)")


if __name__ == "__main__":
    # Ensure build environment is correctly rooted
    Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)

    print("--- 𓍿 GARDEN BUILD INITIATED ---")

    build_artifact(INCLUDE_DIRS_FULL, OUTPUT_FILE_FULL, "GARDEN OF FREEDOM: FULL CANON", True)
    build_artifact(INCLUDE_DIRS_LIGHT, OUTPUT_FILE_LIGHT, "GARDEN OF FREEDOM: LIGHT CANON", True)

    build_artifact(['./'], OUTPUT_FILE_INDEX,  "GARDEN OF FREEDOM: INDEX", False)

    print("--- ◎ BUILD COMPLETE ---")