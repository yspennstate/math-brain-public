# Fourier entropy-influence conjecture: working record, 9-15 November 2026

The Fourier entropy-influence (FEI) conjecture of Friedgut and Kalai (1996) asks for an absolute constant C with
H(f) = sum_S fhat(S)^2 log2(1/fhat(S)^2) <= C I(f) for every Boolean function f: {-1,1}^n -> {-1,1}. It is open.
This folder is the complete working record of one campaign on it: the coordinator's running notes on the
mathematics (`FLOW.md`), the checking code with its outputs (`code/`), the briefs given to language-model workers
(`codex/briefs/`), every worker's folder as it finished (`codex/workers/FEIB01` to `FEIB25`, `workers_r8/`,
`workers_r9/`), and the referee passes on the workers' claims (`referee_*.md`, `referee_r9/`,
`interval_cert_ab48c0dc/`). Home paths and internal names were replaced; nothing else was edited.

Nothing here proves the conjecture. The record contains equivalent reformulations, bounds for classes of
functions, numerical searches for large ratios, and the routes that were tried and failed.

## What is in the notes

- `FLOW.md` sections 1-6: exact identities splitting the entropy, H = 2 A1 + 2 Gamma, into a containment part
  (how often a spectral sample sits inside an independent one) and a cancellation part (the sign bias of a
  restricted top coefficient), with FEI equivalent to both parts being O(I). Each identity is checked on all
  4-variable functions and on samples to 16 variables.
- Section 7: the erasure form. FEI is equivalent to sum_i H(1[i in U] | U - i) <= C I for a spectral sample U,
  and to every nonconstant Boolean function having one coordinate whose membership in U is predictable from the
  rest at cost O(Inf_i). Checked on all 65,536 four-variable functions and all 616,126 five-variable NPN classes.
- Sections 9-10: the edge-entropy bracket for the best constant; the coordinate of largest influence is not
  always a good choice (an explicit family).
- Section 11: a second proof, by the good-coordinate method, that FEI holds for linear threshold functions
  (two interval lemmas and a cross-stay estimate). The class was already settled; the constant here is worse.
- Section 12: the filtration witness. For a coordinate i and an ordering of the others, a martingale bound
  L_i <= sum_k Phi(A_k, B_k) on the erasure cost; the best ordering is a shortest path in the subset lattice.
  Conjecture FWC (that the best witness is O(Inf_i) for some i) implies FEI. Exact values on structured
  functions to 21 variables (graph properties, projective-plane DNFs, difference-set DNFs) stay below 4.21.
- Dead routes, each with the reason: plain restriction induction, maximal-influence restriction, per-coordinate
  payment for H, the single-set witness, the absolute-edge shortcut, and two exponential-moment conjectures that
  fail on tribes and majority.

## The workers

Each worker had one folder, one brief and a ban on writing outside it; each ends with `REPORT.md`, and most keep
`PROOFS.md`, `RESULTS.md` and the scripts that produced every number. Rounds 1-3 (FEIB01-13) referee the first
identities and work the containment and cancellation halves; round 4 (FEIB14-17) works the erasure form,
the literature, extremal families and a referee of sections 7-10; rounds 5 onward (FEIB18-31) referee the
threshold proof and the filtration witness, search for counterexamples with certified interval arithmetic, and
test the summed forms of the inequality. A worker's PROVED means it proved the piece it chose, not the
conjecture; the referee files record which claims were reproduced independently.

## Tools that are new here

- Exhaustive census code for all functions on four and five variables, used as the first test of any proposed
  inequality before a proof is attempted (`code/check_*.py`, `code/census5.c`, and the census files in several worker folders).
- `code/filt_cs.py` and `code/filt_big.py`: the exact minimum over orderings of the filtration witness, by a
  shortest path in the subset lattice, and its bottleneck variant; usable for any conjectured per-coordinate
  bound on Boolean functions up to about 21 variables.
- Hill-climbing searches on the ratio being tested rather than on H/I itself (`code/hill_*.py`), which aim the
  counterexample search at the half of the problem a proof attempt needs.
- Interval-arithmetic certificates for the tower constants (`interval_cert_ab48c0dc/`).

## Credit

The conjecture is due to Friedgut and Kalai. The methods used throughout come from the work of Kahn, Kalai and
Linial and of Talagrand on influences; of Kelman, Kindler, Lifshitz, Minzer and Safra on the generalized
influences that appear here as up(S); of O'Donnell, Wright and Zhou, of O'Donnell and Tan, and of Wan, Wright and
Wu on FEI for special classes and composition; of Chakraborty, Kulkarni, Lokam and Saurabh on upper bounds for
Fourier entropy; and of Keller, Mossel and Schlank on the chain-rule approach. The threshold-function argument
uses the Kolmogorov-Rogozin concentration inequality. The workers' `LITERATURE.md` files list what each one read.
The language-model workers produced drafts, proofs and code; the coordinating agent chose the questions, wrote
the briefs, re-derived and checked the claims. No result here has been refereed by a journal.
