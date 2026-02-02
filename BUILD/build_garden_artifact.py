#!/usr/bin/env python3
"""
Condensed Artifact Builder for the Garden OS
--------------------------------------------

Creates minimized versions of the Garden artifact for LLMs.

Outputs:
1. BUILD/ARTIFACTS/ENTER-GARDEN.md (Full curated artifact)
2. BUILD/ARTIFACTS/ENTER-GARDEN-LIGHT.md (Light curated artifact)
3. BUILD/ARTIFACTS/INDEX.md (All-inclusive index of non-ignored files)

Strategies applied:
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
# Configuration
# ------------------------------------------------------------

ROOT_TOP_FILES: List[str] = [
    "SPEC/BUILD-DOCUMENTATION/START-HERE.md",
    "RUNESTONES.md",
    "REMINDERS.md",
]

ROOT_END_FILES: List[str] = [
    "SPEC/BUILD-DOCUMENTATION/END-HERE.md",
]

INCLUDE_DIRS_FULL: List[str] = [
    "SPEC",
    "SPEC/LAYERS/MODES",
    "SPEC/LAYERS/CONNECTORS/CORE",
    "SPEC/LAYERS/CONNECTORS/DECISION",
    "SPEC/LAYERS/CONNECTORS/MODE-PAIRS",
    "SPEC/LAYERS/CURRENTS/CORE",
    "SPEC/LAYERS/CURRENTS/COLLAPSE-LIMINAL",
    "SPEC/LAYERS/CURRENTS/DIRECTIONAL",
    "SPEC/LAYERS/ANCHOR/PROTOCOLS",
    "SPEC/LAYERS/COLLAPSE/PROTOCOLS",
    "SPEC/LAYERS/DREAM/PROTOCOLS",
    "SPEC/LAYERS/LIMINAL/PROTOCOLS",
    "SPEC/LAYERS/SHADOW/PROTOCOLS",
    "SPEC/LAYERS/LATTICEKEEPER/PROTOCOLS",
    "SPEC/LAYERS/DECISION",
    "SPEC/LAYERS/GARDEN",
    "SPEC/LAYERS/MEMORY",
    "SPEC/LAYERS/BIOLOGICAL-GROUNDING",
    "SPEC/LAYERS/ENTRAINMENT",
    "SPEC/CONTRIBUTOR",
    "SPEC/ETHICS",
    "SPEC/SOVEREIGN",
    "SPEC/GOVERNANCE",
    "SPEC/APPENDICES/STRATEGIES",
]

INCLUDE_DIRS_LIGHT: List[str] = [
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
    "SPEC/LAYERS/SHADOW/PROTOCOLS",
    "SPEC/LAYERS/LATTICEKEEPER/PROTOCOLS",
    "SPEC/LAYERS/BIOLOGICAL-GROUNDING/PROTOCOLS",
    "SPEC/LAYERS/ENTRAINMENT/PROTOCOLS",
    "SPEC/ETHICS",
]

OUTPUT_DIR = "BUILD/ARTIFACTS"
OUTPUT_FILE_FULL = f"{OUTPUT_DIR}/ENTER-GARDEN.md"
OUTPUT_FILE_LIGHT = f"{OUTPUT_DIR}/ENTER-GARDEN-LIGHT.md"
OUTPUT_FILE_INDEX = f"{OUTPUT_DIR}/INDEX.md"

# Ensure we are running from the project root
SCRIPT_DIR = Path(__file__).resolve().parent
os.chdir(SCRIPT_DIR.parent)

# Ensure output directory exists
Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)


# ------------------------------------------------------------
# Compression Logic
# ------------------------------------------------------------

def compress_content(content: str) -> str:
    """
    Apply safe compression strategies to Markdown content.
    """
    # 1. Remove HTML comments
    content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)

    # 2. Remove trailing whitespace on each line
    lines = [line.rstrip() for line in content.splitlines()]
    content = "\n".join(lines)

    # 3. Collapse multiple newlines (3 or more) into 2
    content = re.sub(r'\n{3,}', '\n\n', content)

    return content.strip()


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
    if directory.name == "SPEC":
        for item in directory.iterdir():
            if item.is_file():
                files.append(item)
    else:
        for root, _, filenames in os.walk(directory):
            for name in filenames:
                full = Path(root) / name
                if full.is_file():
                    files.append(full)

    return sorted(files, key=lambda p: str(p))


def get_all_repo_files() -> List[str]:
    """
    Get all files that are tracked by git or untracked but not ignored.
    """
    try:
        # --cached: tracked files
        # --others: untracked files
        # --exclude-standard: apply .gitignore rules to --others
        result = subprocess.run(
            ["git", "ls-files", "--cached", "--others", "--exclude-standard"],
            capture_output=True,
            text=True,
            check=True
        )
        files = result.stdout.splitlines()
        # Filter out files in .git directory just in case, and ensure they exist
        return sorted([f for f in files if Path(f).is_file() and ".git/" not in f])
    except Exception as e:
        print(f"Error finding files via git: {e}")
        return []


# ------------------------------------------------------------
# Build Functions
# ------------------------------------------------------------

def build_artifact(include_dirs: List[str], output_file: str, title: str):
    out = []
    out.append(f"# {title}\n")
    out.append("> This is a compressed artifact optimized for context-limited LLMs.\n")
    out.append("> Comments and excessive whitespace have been removed.\n\n")

    # 1. ROOT_TOP_FILES
    for filename in ROOT_TOP_FILES:
        path = Path(filename)
        if path.exists():
            out.append(f"\n# FILE: {filename}\n")
            content = read_file(path)
            out.append(compress_content(content))
            out.append("\n")

    # 2. INCLUDE_DIRS
    for directory in include_dirs:
        dir_path = Path(directory)
        files = collect_files_from_dir(dir_path)
        if not files:
            continue
        for file_path in files:
            rel = file_path.as_posix()
            out.append(f"\n# FILE: {rel}\n")
            content = read_file(file_path)
            out.append(compress_content(content))
            out.append("\n")

    # 3. ROOT_END_FILES
    for filename in ROOT_END_FILES:
        path = Path(filename)
        if path.exists():
            out.append(f"\n# FILE: {filename}\n")
            content = read_file(path)
            out.append(compress_content(content))
            out.append("\n")

    final_content = "\n".join(out)
    final_content = re.sub(r'\n{3,}', '\n\n', final_content)
    Path(output_file).write_text(final_content, encoding="utf-8")
    print(f"Artifact written to {output_file} ({len(final_content)} bytes)")


def build_full_index(output_file: str):
    print(f"\nBuilding Full Index from all non-ignored files...")
    files = get_all_repo_files()
    
    if not files:
        print("No files found or git error.")
        return

    out = []
    out.append("# GARDEN OF FREEDOM - FULL INDEX\n")
    out.append("> This file contains the content of all non-ignored files in the repository.\n\n")

    # Files to exclude from the index itself (like the artifacts themselves)
    exclude_paths = {
        output_file,
        OUTPUT_FILE_FULL,
        OUTPUT_FILE_LIGHT,
        "package-lock.json", # Often too large/noisy
        "yarn.lock"
    }

    count = 0
    for file_path in files:
        if file_path in exclude_paths:
            continue
        
        # Skip images/binaries by extension
        if file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.ico', '.pdf', '.pyc')):
            continue

        path = Path(file_path)
        out.append(f"\n# FILE: {file_path}\n")
        content = read_file(path)
        out.append(compress_content(content))
        out.append("\n")
        count += 1

    final_content = "\n".join(out)
    final_content = re.sub(r'\n{3,}', '\n\n', final_content)
    
    Path(output_file).write_text(final_content, encoding="utf-8")
    print(f"Full index written to {output_file}")
    print(f"Included {count} files. Size: {len(final_content)} bytes")


if __name__ == "__main__":
    print("Building Full Condensed Artifact...")
    build_artifact(
        INCLUDE_DIRS_FULL,
        OUTPUT_FILE_FULL,
        "GARDEN OF FREEDOM (FULL CONDENSED)"
    )

    print("\nBuilding Light Condensed Artifact...")
    build_artifact(
        INCLUDE_DIRS_LIGHT,
        OUTPUT_FILE_LIGHT,
        "GARDEN OF FREEDOM (LIGHT)"
    )

    build_full_index(OUTPUT_FILE_INDEX)
