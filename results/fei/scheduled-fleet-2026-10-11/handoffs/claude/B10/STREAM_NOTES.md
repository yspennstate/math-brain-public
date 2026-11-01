# B10 stream notes (Claude lead) - v2 2026-10-11 23:31Z

## Frozen live potential
P_A = M_A + Delta_A (B09-BIASED-BLOCK-UNCERTAINTY v1, adb671ff); one bit Delta(p) = p log2((1-p)/p), p<=1/2.

## Established
- Tax-free J_A <= M_A REFUTED (B09 repair a1ff9357; AND p=1/8 q=1/4: J-M = 0.119545).
- A046: AND rare-p coefficient 4q(1-2q); lead re-derived it. Any one-bit tax needs coefficient >= 1/2.
- A047: fixed-child coefficient 2Z+2c-2 <= 1/2; lead re-derived Z-D from the angle form. Holds.
- A048 sections 1-2 (aligned tensor additivity of M,J,Delta; unrevealed factor leaves the ledger fixed while
  terminal entropy grows; dummy-coordinate tax, repaired by contracting to essential coordinates): hold.
- LEAD, CERTIFIED (review pending), run claude/B10/runs/20261011T230400Z-claude-B10-onebit-half-tax:
  J_i - M_i = h2(p) - sum_T q_T F(t_T), F(t) = h2(sin^2 t)+h2(sin^2(t-b)), sin^2 b = p,
  (sqrt(1-p)G_T, sqrt(p)H_T) = sqrt(q_T)(cos t_T, sin t_T). Hence J_i - M_i <= tau*(p) = h2(p) - min F <= Delta(p)/2
  for every f, every dimension, every bias. Strict except at p=1/2; tau* = (p/2)log2(1/p) - 0.2787p + o(p), so the
  1/2 is sharp. Proof: analytic for p<=0.08 and for p>=0.49 near the eigenstate, interval boxes in between.
- CONDITIONAL: product-biased blocks, J_A - M_A <= sum tau*(p_i) <= Delta_A/2, if the optimal Shannon uncertainty
  bound is additive for local measurement pairs (Schwonnek, Quantum 2, 59 (2018); cited, not re-read).
  Two-bit multistart found nothing below U(p1)+U(p2).

## Refuted / retired (do not retest under unchanged quantifiers)
tax-free J<=M; any O(p) one-bit tax; one-bit coefficient 1 as necessary; raw-L (O-RAW-CONV); fixed Renyi
alpha<1 (O-RENYI); weighted-control and rare-logarithm variants in the A046 ledger.

## Next target per agent
- A046: independent review of the lead run: re-derive the reduction from a_T,b_T; check lemma A's case split
  and lemma B's semi-concavity bound phi'' >= -4/ln2; re-run code/certify_half_tax.py.
- A047: exact finite-p sup over real children = h2(p) - (lower convex envelope of t -> (sin^2 t, F(t)) at
  abscissa p). Compare with the Boolean sup on n<=3 (exhaustive, exact intervals) at p in {1/8,1/4,3/8}.
- A048: payment. On point-defect tensors (A036: K >= T/4 - 8I) and on activations, is sum over essential
  revealed bits of tau*(p_i) <= K*I? Exact ledgers, no new potential.
- A049: frozen exhaustive check of the block claim: |A|=2, Boolean children on <=2 residual bits, biases in
  {1/8,1/4,3/8,1/2}^2, exact intervals. Target J_A-M_A > tau*(p1)+tau*(p2) (would refute additivity as used).
  Report the max of (J_A-M_A)/(Delta_A/2). Minimal witness only inside the searched domain; hand to A074.
- A050: scoped repair: restate B09 with tax sum tau*(p_i) on essential coordinates (lead lemma + A048
  contraction). List which C019/C018 uses survive and where (1/2)p log2(1/p) per rare revealed bit must come
  from influence or from C024 path entropy.

## Do not repeat
Re-refuting tax-free J<=M; O(p) taxes; raw-L; fixed Renyi; float sign claims without intervals; covers whose
seams were not recomputed (the lead's first PASS missed p in (0.08,0.0816)); automatic n increases.
