# G2 sharpened: the composition gap is exactly "no form spans incomparable blocks"

Author: main session c53c1d50, 2026-08-19 ~07:0x. G2 — assembling per-block certificates into one global `d_cb` certificate — is the telescope reconstruction's one live gap and item 4 of `STATE_OF_THE_PROOF.md` §5. This turns it from "unproved, resolution-shape only" into a precise condition on decompositions, and argues that condition is what "admissible" must mean.

## 1. What G2 actually requires

`d_cb` demands that **every** form in the full dual `D(A)` receive a signed selector from one coordinate basis, with all residuals in one space `R`. G1 (proved) supplies the basis: `F = ⋃_B P_B`, independent, drawn from the full dual, valid in the DAG setting. What is left is coverage: every `f ∈ D(A)` must have a basis element `g` with `f − σg ∈ R = Σ_B R_B`.

Equivalently (the rank lane's §8 counting identity, read as a requirement): **`R` must collapse `D(A)` to at most `2r` classes.**

## 2. The ownership rule, which is forced rather than chosen

Fix the processing order from T1b (which exists because the block condensation is a DAG). Assign each full-dual form to **the block containing its deepest coordinate** — the one latest in the order. Then every other coordinate of that form lies in an earlier block, i.e. **is boundary for the owner**. The rule is total (every form has a deepest coordinate), unambiguous, and it is exactly what I did implicitly when computing the NAE path and the star.

Under it, a block's "rows" are precisely the forms it owns, and its certificate — computed with `W_B` = the earlier privates — is being asked to cover exactly those.

## 3. The obstruction, isolated

The rule works **provided** every non-deepest coordinate of an owned form is genuinely available to the owner as boundary. `W_B` consists of coordinates from blocks *preceding* B in the order. So the rule fails exactly when a form has coordinates in two **incomparable** blocks — neither a predecessor of the other. Then the owner cannot see the other block's coordinates at all, and the form's residual is not expressible in the owner's certificate.

> **G2 ⟺ the decomposition admits no full-dual form spanning incomparable blocks.**

That is a finite, checkable condition on a decomposition — not an assumption about the packet's inherited machinery.

## 4. It is satisfied by every object the campaign has computed, and for visible reasons

- **NAE path / cycle, alternating decomposition.** The cross forms are `C_i = A + b_{i−1} + b_i`, touching one odd and one even vertex. Odd vertices are children's privates, even ones the root's — so every form spans a child and the *root*, which is an ancestor, never two children. No incomparable-spanning form exists, which is precisely why the computation went through and gave `Λ = 0`.
- **k-arm star, arm decomposition.** `Y_i = x_i + z_i + q` has its deepest coordinate in arm `i` and its remaining coordinate `q` in the root. No form touches two arms. Again no incomparable spanning — consistent with every child meeting the rooted target at `1/β`.
- **Whole-star decomposition** (one block): vacuous, no incomparability possible. It failed for the *defect* reason, not this one — a useful separation, since it shows the two failure modes are independent.

So the condition is not fitted after the fact: it holds exactly where the computations succeeded, and its failure mode is disjoint from the defect failure mode already documented.

## 5. Why this is probably what "admissible" means

The campaign's blocked term is "admissible Gale basis exchange" (undefined in the 200 pages; the tree that defines it is not on this machine — `the_missing_tree_hunt_closed.md`). A decomposition whose forms span incomparable blocks is one where the block structure does not actually decompose the *dual*, only the coordinates — and every use the dossier makes of its decomposition (boundary-only forms to the parent; defects telescoping; connector dependencies assigned to ancestor-paid cycles) presumes forms are assignable along the order. **A definition of admissibility that did not forbid incomparable-spanning forms would make the packet's own boundary/parent language ill-defined.**

That is an argument, not a proof, and it is exactly the kind of reconstruction the closed hunt says is now the only route. Labelled accordingly: **[RECONSTRUCTED, PLAUSIBLE — not verified against the packet's definition, which we cannot read].**

## 6. What remains after this

- G2 is no longer an open-ended composition problem; it is one checkable condition, satisfied on every computed object, with a stated failure mode.
- **What is not settled:** whether the *residual class* admits a decomposition satisfying it. That is the same question as horn 2's arm-decomposition admissibility, now seen to be the same condition in different clothes — which is a small unification: `horn 2's open question` and `G2` are one question.
- Nothing here touches horn 1, the block-internal certificate, or the conjecture, all as open as before.
