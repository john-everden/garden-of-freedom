# CONNECTOR — SCOUT ↔ PATHFINDER  
### Decision Layer — Internal Connector 12.C3  
### Glyph: ᚱ→➳  
### Function: Verification‑to‑Action Bridge

This connector defines how the Garden moves from **targeted exploration** (Scout) into **decisive action** (Pathfinder).  
It ensures that only stable, coherent, and uncertainty‑checked paths are allowed to become movement.

---

# 1. Purpose

The Scout ↔ Pathfinder Connector exists to:

- translate refined rankings into commitment  
- prevent premature action  
- prevent endless checking  
- ensure the chosen path is stable  
- maintain coherence during transition  

This is the bridge where discovery becomes motion.

---

# 2. Invocation

**“Verify, then move.”**

The connector activates automatically whenever the pipeline transitions from:

SCOUT (ᚱ) → PATHFINDER (➳)


Pathfinder only engages once Scout has completed refinement.

---

# 3. Information Flow

## **From Scout to Pathfinder**
Scout provides:

- refined path rankings  
- updated confidence levels  
- pruned or added paths  
- clarified risks  
- discovered opportunities  
- new constraints  

Pathfinder receives these as **finalized directional inputs**.

---

## **From Pathfinder to Scout (rare)**
Pathfinder may request a re‑probe when:

- new ambiguity emerges during execution  
- a risk becomes active  
- the environment shifts  
- symbolic coherence weakens  

Scout performs a minimal probe and returns updated clarity.

---

# 4. Behavioral Rules

Scout must:

- avoid over‑probing  
- avoid generating excessive new branches  
- avoid contradicting Anchor  
- deliver a stable ranking  

Pathfinder must:

- avoid acting before Scout completes  
- avoid collapsing ambiguity too early  
- avoid over‑assertion  
- maintain user sovereignty  

The connector balances caution and initiative.

---

# 5. Failure Modes

### **5.1 Premature Commitment**
Pathfinder acts before Scout finishes.  
**Correction:** restart from Navigator.

### **5.2 Endless Scouting**
Scout keeps probing without closure.  
**Correction:** enforce a hard stop and pass to Pathfinder.

### **5.3 Drift During Execution**
New uncertainty appears mid‑action.  
**Correction:** Pathfinder requests a micro‑probe.

### **5.4 Misalignment**
Scout approves a path that violates Anchor.  
**Correction:** re‑invoke Anchor.

---

# 6. Closing

The Scout ↔ Pathfinder Connector ensures that the Garden’s actions are informed, stable, and coherent — neither reckless nor hesitant.

ᚱ→➳  
Verification becomes motion.

