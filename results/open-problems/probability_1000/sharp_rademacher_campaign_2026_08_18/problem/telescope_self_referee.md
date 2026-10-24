# Self-referee of the telescope draft — one hidden assumption found, and it discharges

Author: main session c53c1d50, 2026-08-19 ~06:2x. **This is a SELF-referee and therefore not independent** — the campaign's standing rule is that a document's author is the worst person to adjudicate it, and the hostile referee assigned to this draft died on a usage limit twice. It is run now because the missing-tree hunt closed with "reconstruction is the only route" (`the_missing_tree_hunt_closed.md`), which makes this draft load-bearing for three separate results: W1-rooted, the horn-2 reduction, and the clause-tension analysis. A fresh adversarial pass is still owed and should be the first thing run when limits reset.

Attack targets are the ones I wrote for the (dead) referee, applied to my own work.

## Target 1 — T1a (rank telescopes with no absorption clause): SURVIVES

Claim: with `V_i = R_{B_1}+…+R_{B_i}` and `R_<^i := V_{i−1} ∩ span W_{B_i}`,
  `dim(Σ_B R_B) = Σ_i dim((R_{B_i}+V_{i−1})/V_{i−1}) ≤ Σ_i dim((R_{B_i}+R_<^i)/R_<^i)`.

- The equality is the dimension filtration of a sum — correct without conditions.
- The inequality needs `R_<^i ⊆ V_{i−1}`, which holds **by construction** (it is defined as an intersection with `V_{i−1}`). Given that, `r + R_<^i ↦ r + V_{i−1}` is well defined and surjective onto `(R_{B_i}+V_{i−1})/V_{i−1}`, so the dimension can only drop.

I tried to build a counterexample at 3–4 blocks in dimension ≤ 6 and could not: any attempt to make the arising quotient *exceed* the `R_<`-quotient requires `R_<^i ⊄ V_{i−1}`, which the definition forbids. **T1a is correct as stated.**

## Target 2 — T1b (`Σ_B L_B ≤ ℓ`): a HIDDEN ASSUMPTION, now identified and discharged

The proof orders blocks ancestors-first and uses `H(Q_B|W_B) ≥ H(Q_B | all earlier privates)`, which requires **`W_B` to be measurable with respect to the privates of blocks processed EARLIER**. I asserted that as "boundaries are functions of ancestor privates". That is an assumption about the decomposition, and I did not flag it.

**Where it could fail:** if a block's boundary drew on *sibling* privates, no ancestors-first order would make it measurable; worse, if two blocks each appeared in the other's boundary, **no order at all** would work and the chain-rule step would be unavailable. So T1b silently requires the *block-level* "boundary-depends-on" relation to be **acyclic**.

**Why it discharges — and the reason is structural, not lucky.** The dossier's blocks are **strongly connected components** ("a singleton-layer cyclic strongly connected component", S6 §6, and throughout). The condensation of any directed graph by its SCCs is a **DAG** — that is the standard theorem — so the block-level dependency relation is acyclic by construction, a topological order exists, and every block's boundary is measurable with respect to the privates of blocks preceding it in that order.

So: **T1b holds, and the SCC structure of the blocks is exactly what makes its ordering possible.** That is worth stating positively — the packet's choice to decompose into SCCs is not just a way of isolating the hard case; it is what licenses the entropy chain rule at the tree level. The draft should have said so, and now does.

## Target 3 — G1 (assembly into one full-dual coordinate basis): SURVIVES, and generalises

The induction picks a block `B*` carrying a nonzero coefficient with no nonzero-coefficient descendant, then projects onto `Q_{B*}`. The step to check is that ancestors and incomparable blocks contribute nothing there:
- an ancestor's forms are supported in its own privates plus *its* ancestors' privates, and `Q_{B*}` belongs to a strict descendant — disjoint;
- an incomparable block's forms are supported in its privates plus its predecessors', and `B*` is not among its predecessors (else they would be comparable) — disjoint.

Both arguments use only "predecessor in the order", never "parent in a tree", so **G1 holds verbatim in the DAG setting** that Target 2 established, not merely in a strict tree. That is a small generalisation of what I originally proved.

## What this changes in the draft

1. T1b now carries its hypothesis explicitly (acyclic block-level dependency) together with its discharge (SCC condensation is a DAG).
2. G1 is stated for DAGs rather than trees.
3. T1a is unchanged.

## What it does not change

This is self-refereeing. The three targets I chose are the three I already believed hardest, which is precisely the bias an independent referee exists to defeat — the cluster referee found four dead items and two vacuous ones in a document I had checked myself, and the rank memo's author listed seven ways his own memo could be wrong. **Nothing here should be treated as adjudication.** The draft remains UNREFEREED in the campaign's ledger sense, and the conjecture remains OPEN.
