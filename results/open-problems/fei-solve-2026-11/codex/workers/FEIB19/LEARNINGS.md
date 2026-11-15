---
status: verified-local-proofs-and-computations
worker: FEIB19
date: 2026-11-10
---

# Learnings for the launching session

Compositions have an optimal filtration order respecting every block, with the target block last. Moving an outside step before a target-inside step improves the cost by superadditivity of Phi. For the other blocks, cumulative Fourier masses are multiaffine in each block's revealed nonconstant energy. Cost is concave in how a block's total energy is distributed among reveal slots, so consolidation at one slot cannot hurt. This proves the full block-order claim, not just a heuristic for symmetric gates. PROOFS.md gives the exact optimized composition law; composition.json and final_checks.json compare it against unrestricted truth-table DPs.

At every leaf of a read-once AND/OR/XOR/NOT formula, the optimized filtration cost equals exact erasure entropy. Off-path sibling subtrees first, target subtree last is an optimal order. The existing H<=10I theorem therefore gives FWC with coefficient 10 on this restriction-closed class. It does not automatically extend to majority gates: odd majority already has zero exact erasure and positive filtration cost.

Recursive Fano-plane DNFs are a substantially larger gap example than the supplied small hill-search examples. They are odd, monotone and transitive, so exact erasure is identically zero, yet their optimized filtration ratio tends to about 4.601671597979309. final_checks.json derives the coordinate influence from 36 pivotal inputs out of 128, evaluates the finite base-spectrum recurrence at 90 decimal digits and provides a summable tail. The gap is bounded; this is not an FWC counterexample.

The PM(K33) nine-coin tower's optimized witness minimum tends to approximately 4.86317608849. pm.json optimizes over coordinate type paths and over outside orders; native_audit.json independently redoes the all-core candidate's outside DPs in long double. A geometric analytic tail encloses the limit up to numerical rounding. The figure concerns the minimum erasure/witness coordinate ratio, not FEIB16's influence-weighted average erasure ratio.

The naive adaptive input-tree extension is false. The four-variable table b6a4 at coordinate 1 has E_i=1 bit and depth-grouped adaptive martingale cost about 0.774397470348 bits. audit.json specifies the policy and dyadic energy bins. An independent-input random choice of complete permutation remains valid if its cost is recomputed from spectral bins; a decision tree on spectral membership also remains valid by data processing. Actual input-tree energies are a different object.

The threshold filtration theorem can be proved directly for every reveal order at a largest-weight coordinate. Apply FLOW's bounded-step window/tail lemma to the deterministic remaining tail, and Berry–Esseen to its concentration. Adjacent tails differ in variance by at most the square of the target weight. This gives Cross_(K-1) Stay_K<=(160/3)delta^2, hence FWC coefficient 20.95691937544493. The coefficient is conservative. The proof avoids assuming that the level witness refines the last-position witness.

Two caution points belong with these results. The unnormalized comparison sentence in FLOW 12(g) has the wrong direction; the corrected lower comparison divides by the variance scaling t. Expected-depth bounds are not preserved with the same parameter under arbitrary restrictions: a rare deep branch is enough. Bounded degree and bounded sensitivity do give immediate explicit filtration bounds through lower bounds on every live influence.

The papers and local reports were useful for existing entropy constants and avoiding a false novelty claim. The math recall script exists but reports that its store is absent. No shared brain, mesh or fleet-board write was made; the launching session can ingest this file under its own coordination rules.
