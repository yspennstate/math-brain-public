# Holistic referee report (independent, session 11)

Read the full assembled manuscript (~52pp) + all parts + STATE. Spot-checked prop:bd-tail,
rect:tall-tail, kth:laguerre-tail, random-count squeeze — all correct. Confirmed NO result
labeled PROVEN secretly depends on prob:pc (honest labeling is real).

## 1. Overall
Publishable as a **framework + lower-bound + conditional-universality** paper (not the full
universality/LDP paper the title advertises). Proven core is genuine and correct: the abstract
entropy/small-ball principle; a distribution-free LOWER side over a wide ensemble zoo; one new
UNCONDITIONAL EXACT law (quaternion base h(gamma)/4); deterministic finite-alphabet/sign
phase-retrieval obstructions; pathwise transfer corollaries; a well-posed open-problem suite.
Venues: EJP, ALEA, Random Matrices: Theory Appl., J. Theoret. Probab., or an ACHA frames venue.
A top general journal would require prob:pc (the upper side) proven.

## 2. HIGH priority
- **lem:two-proj has only a "Proof sketch"** deferred to Petrov1975 / external note. It is the
  per-pair analytic input to the universality reduction. Give a complete proof (appendix) or demote
  to an explicitly heuristic statement. (Mitigated: nothing PROVEN rests on it.)
- **Title/abstract overclaim vs ledger.** "Universality" and "large deviations" are largely
  CONDITIONAL/conjectural (thm:conditional-univ, cor:pr-cond, rect:exact, two:exact, kth:extremal all
  hinge on prob:pc; LDP is the IV.A sandwich + two open conjectures). State the conditionality
  unmistakably; consider retitling toward "lower bounds and conditional universality."
- **Quaternion exact theorem (thm:quaternion-gaussian-base) is buried** under "division algebras."
  It is the strongest result beyond ShmaloExtremal2026 — make it a headline. Double-check uniformity
  of the (1+O(t^2)) two-ball bound and the D=2 handling.
- **Dangling "pruning manuscript" artifacts**: intro.tex:8, universality.tex:386, geometric.tex:948
  ("pruning notation", "W=R+S signal-plus-noise"). Meaningless in a standalone paper — remove/define.

## 3. MEDIUM
- **Abstract** is a ~30-line run-on enumerating every corollary. Lead with the proven core:
  principle -> universal distribution-free lower side -> quaternion exact law -> deterministic
  alphabet/sign obstruction -> conditional universality reduced to ONE overlap moment.
- **Bloat**: ~10-12 near-identical finite-budget corollaries (finite-entropy-square, rowwise/entrywise
  heterogeneous, directional-row, rect:* and two:* finite-entropy variants) are the same union bound
  re-bookkept. Consolidate into one master finite-budget theorem + a remark listing specializations.
  Paper is stronger at ~35pp.
- **Notation**: unify rho (quaternion overlap) with varrho (real/complex overlap); k overloaded
  (submatrix size in two-sided vs index in k-th singular value); L overloaded (entropy L_m vs
  anti-concentration L_{m,i}); ldp.tex d/h shorthand drifts from d_F/h(gamma).
- **Numerics**: convincing for small-ball exponents and overlap moments (4-digit, real independent
  check) and Gumbel shape (KS p~0.96); the extremal BASE is only m<=8 (still ~6% from -log4). State
  plainly that simulation confirms the INPUTS and the Gumbel SHAPE, not the base (which is proven).
- **Open problems**: genuine and well-framed; prob:pc correctly the keystone. Keep.

## 4. Single most important
Reframe honestly + consolidate: foreground the proven core and the quaternion exact law in
title/abstract/intro; make proven-vs-conditional explicit at every theorem; complete or demote
lem:two-proj; compress the repetitive corollaries. That converts a sprawling ledger-style draft into
a clean, definitely-publishable framework paper. Proving prob:pc would lift it to a top venue but is
not required for acceptance.

## Lead disposition
- Saving this report for the user. Acting now on the one unambiguous mechanical item: locate and
  remove/define the dangling "pruning manuscript" artifacts (HIGH #4).
- The reframing (title/abstract/headline quaternion/consolidation) is the user's editorial call;
  this report gives the exact roadmap. lem:two-proj full proof exists in notes/IIB_lemma_2D.md
  (could be promoted to an appendix).
