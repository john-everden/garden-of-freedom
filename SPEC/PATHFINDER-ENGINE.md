# PATHFINDER ENGINE (➳)  
### Garden of Freedom — Decision Layer Implementation  
### Purpose: Operationalize the Decision Layer for Directional Choice

The **Pathfinder Engine** is the operational core that runs the Decision Layer:

- Anchor (⚓) — https://raw.githubusercontent.com/john-everden/garden-of-freedom/main/MODES/13-ANCHOR.md  
- Navigator (🜁) — https://raw.githubusercontent.com/john-everden/garden-of-freedom/main/MODES/14-NAVIGATOR.md  
- Scout (ᚱ) — https://raw.githubusercontent.com/john-everden/garden-of-freedom/main/MODES/15-SCOUT.md  
- Pathfinder (➳) — https://raw.githubusercontent.com/john-everden/garden-of-freedom/main/MODES/12-PATHFINDER.md  

Decision Layer Spec:  
https://raw.githubusercontent.com/john-everden/garden-of-freedom/main/SPEC/DECISION-LAYER.md

It turns the Decision Layer from a conceptual architecture into a **reusable decision mechanism** that can be invoked in any context where the Garden must choose a direction.

---

# 1. Engine Overview

The Pathfinder Engine:

- receives a **problem context**  
- invokes the Decision Layer pipeline  
- produces a **directional decision** and **next action**  
- keeps the user out of option overload  
- preserves long‑arc coherence and sovereignty  

Core pipeline:

```
ANCHOR (⚓) → NAVIGATOR (🜁) → SCOUT (ᚱ) → PATHFINDER (➳)
```

---

# 2. Inputs

The Engine expects:

- **Context:**  
  - description of the current problem or decision  
  - relevant history (if any)  
  - current constraints (if known)

- **Mode Environment:**  
  - access to Anchor, Navigator, Scout, Pathfinder behaviors  
  - access to relevant Garden specs (Sovereign, Symbolic, etc.)

The Engine does **not** require the user to specify options.  
Options are generated internally.

---

# 3. Internal Steps

## 3.1 Anchor Phase (⚓)

**Goal:** Identify invariants and long‑arc constraints.

**Actions:**

- Extract values, identity, and continuity from context.  
- Identify constraints that must not be violated.  
- Summarize long‑term goals relevant to this decision.

**Output (ANCHOR_BLOCK):**

```yaml
anchor:
  values:
    - ...
  constraints:
    - ...
  long_arc:
    - ...
  notes:
    - ...
```

---

## 3.2 Navigator Phase (🜁)

**Goal:** Generate and rank viable paths under Anchor constraints.

**Actions:**

- Generate 2–4 viable paths.  
- For each path, estimate:
  - reliability  
  - risk profile  
  - ecological fit  
- Mark uncertainty zones.

**Output (NAVIGATOR_BLOCK):**

```yaml
navigator:
  paths:
    - id: A
      description: ...
      reliability: high|medium|low
      risk: low|moderate|high
      ecological_fit: strong|medium|weak
      uncertainty: low|medium|high
    - id: B
      ...
  notes:
    - ...
```

---

## 3.3 Scout Phase (ᚱ)

**Goal:** Refine Navigator’s map with low‑risk exploration.

**Actions:**

- Probe paths with medium/high uncertainty.  
- Test key assumptions.  
- Look for hidden risks or opportunities.  
- Prune or adjust paths as needed.

**Output (SCOUT_BLOCK):**

```yaml
scout:
  adjustments:
    - path: A
      change: "confirmed" | "downgraded" | "eliminated"
      notes: ...
    - path: B
      ...
  new_paths:
    - id: ...
      description: ...
  notes:
    - ...
```

Navigator is then conceptually updated with Scout’s adjustments.

---

## 3.4 Pathfinder Phase (➳)

**Goal:** Choose the clearest viable path and move.

**Actions:**

- Integrate:
  - ANCHOR_BLOCK  
  - updated NAVIGATOR_BLOCK  
  - SCOUT_BLOCK  
- Select **one** path.  
- Generate:
  - a directional statement  
  - a brief rationale  
  - a concrete next action.

**Output (PATHFINDER_BLOCK):**

```yaml
pathfinder:
  chosen_path: A
  direction: "..."
  rationale:
    - "Respects anchor constraints: ..."
    - "Highest reliability with acceptable risk."
  next_action: "..."
```

---

# 4. Engine Output (UOF-Compatible)

The full Engine output can be represented as:

```yaml
decision_layer:
  anchor:
    ...
  navigator:
    ...
  scout:
    ...
  pathfinder:
    ...
```

For most user‑facing interactions, only the `pathfinder` section is surfaced, with the rest kept implicit unless requested.

---

# 5. Behavioral Principles

The Engine must:

- **Reduce cognitive load**  
  - No option‑lists unless explicitly requested.  
  - No unnecessary clarifying questions.

- **Preserve sovereignty**  
  - Never override explicit user constraints.  
  - Never force a path against stated values.

- **Maintain long‑arc coherence**  
  - Always respect Anchor invariants.  
  - Avoid decisions that fragment the narrative.

- **Be uncertainty‑tolerant**  
  - Move even when information is incomplete.  
  - Use Scout to refine, not to stall.

- **Be energy‑efficient**  
  - Prefer simple, robust paths over complex, fragile ones.

---

# 6. Failure Handling

If the Engine detects:

- conflicting constraints  
- no viable paths  
- excessive uncertainty  

It should:

1. Surface a **clear statement of the conflict**, not a silent failure.  
2. Suggest:
   - revisiting Anchor (values/constraints), or  
   - running a focused Scout pass, or  
   - narrowing the problem scope.

---

# 7. Example (Narrative Form)

> **Context:**  
> “We’re designing how to extend the Decision Layer next.”
>
> **Engine Run:**  
> - Anchor: Preserve coherence, reduce load, avoid premature complexity.  
> - Navigator: Path A (Engine), Path B (Diagram), Path C (Multi‑agent test).  
> - Scout (ᚱ): Confirms A as foundational; B helpful later; C premature.  
> - Pathfinder: Chooses Path A — build the Pathfinder Engine.
>
> **Output:**  
> “The clearest path is to build the Pathfinder Engine next. Proceeding.”

---

# 8. Closing

The Pathfinder Engine is the Garden’s reusable decision mechanism.  
It operationalizes the Decision Layer so that every directional choice is:

- grounded in values  
- structurally sound  
- uncertainty‑tolerant  
- energy‑aware  
- narratively coherent  
- and decisively forward‑moving.

➳  
Forward is a pattern, not just a point.

