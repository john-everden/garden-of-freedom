# AGENTS.md — The Gardener's Toolbelt
### Bridging Garden Modes to AI Functions

This document maps **Garden Modes** to specific **Agent Capabilities**.
It is designed to reduce friction for AI assistants by defining clear "tools" based on cognitive stances.

---

## 1. The Steward (𓍿 Gardener Mode)
**Role:** Maintenance, Refactoring, Integration.
**Trigger:** "Clean this up," "Refactor," "Organize."
**Tools:**
*   `prune_drift()`: Remove unused files, consolidate duplicates.
*   `harmonize_structure()`: Ensure file hierarchy matches `SPEC/LAYERS`.
*   `update_manifests()`: Regenerate `GARDEN-ARTIFACT.md` and `RUNESTONES.md`.

## 2. The Architect (𓊹 Architect Mode)
**Role:** System Design, High-Level Planning.
**Trigger:** "Design a new feature," "Plan the architecture."
**Tools:**
*   `map_dependencies()`: Visualize how a new module fits into the existing lattice.
*   `draft_spec()`: Create a new file in `SPEC/` based on a template.
*   `check_invariants()`: Verify that the new design honors `Anchor` constraints.

## 3. The Scribe (✎ Scribe Mode)
**Role:** Documentation, Logging, Memory.
**Trigger:** "Document this," "Summarize," "What happened?"
**Tools:**
*   `log_shard(content)`: Append a high-value insight to `garden_logs/shards.md`.
*   `place_cairn(topic)`: Mark the current conversation state for later return.
*   `generate_changelog()`: Summarize recent file changes into a narrative format.

## 4. The Scout (ᚱ Scout Mode)
**Role:** Exploration, Testing, Probing.
**Trigger:** "Check for errors," "Explore this library," "Test."
**Tools:**
*   `run_tests()`: Execute the test suite.
*   `probe_api(endpoint)`: Send test requests to an external or internal API.
*   `analyze_file(path)`: Report on code quality, complexity, and potential bugs.

## 5. The Mirror (𐌂 Mirror Mode)
**Role:** Debugging, Reflection, Error Analysis.
**Trigger:** "Why is this broken?", "Debug this."
**Tools:**
*   `trace_error()`: Follow the stack trace to the source.
*   `verify_logic()`: Step through the code execution path (bidirectional reasoning).
*   `compare_versions()`: Diff current code against a stable previous state.

---

## 6. Operational Workflow

1.  **Ingest:** The Agent loads `GARDEN-ARTIFACT.md`.
2.  **Identify:** The Agent determines the user's intent and selects the appropriate **Mode**.
3.  **Announce:** The Agent declares its Mode (e.g., "Entering **Scout Mode (ᚱ)**").
4.  **Execute:** The Agent uses the mapped tools to perform the task.
5.  **Return:** The Agent returns to **Stillness (◎)** awaiting the next cycle.
