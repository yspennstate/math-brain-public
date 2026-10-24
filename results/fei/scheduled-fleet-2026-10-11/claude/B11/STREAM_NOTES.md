# B11 stream notes (Claude lead) - v2, 2026-10-11 23:3xZ
Run: runs/20261011T230100Z-claude-B11-block-descent-recentring (REPORT, CLAIMS R1-R6).

## Established
- R1 PROVED: for every block A and EVERY recentring map e, (ln2) J_A <= 2 E|S_A symdiff e(S_C)|
  (Gross log-Sobolev, fibrewise). Optimal e = conditional majority: (ln2) J_A <= 2 beta_A,
  beta_A = sum_{i in A} E min(p_i, 1-p_i) <= (1/2) sum H(Z_i|S_C). A052 affine syndrome and the
  baseline (2/ln2) I_A are special cases. Numerics n<=4: 0 violations, max ratio 0.920.
- R2 PROVED: in a dimension-critical C-witness, C Inf_i + D_C <= H(Z_i|Z_-i) + (2/ln2) beta_i;
  no coordinate is spectrally determined by the rest. Implies A052 rank-one bound exactly.
- R5 PROVED: M_n <= max(M_{n-1}, K_desc(n)); bounded K_desc => FEI. So sup K_desc >= C_*.
- R6 PROVED: phi(g x h) <= min(phi g, phi h, H/I of each factor) <= H/I(g x h).
- R3 CERTIFIED: K_desc = 4, 4.43383437, 4.53663407 and M_n = 2, 2.95588958, 3.40247555 (n=2,3,4),
  maxima only at point defects. R4 EVIDENCE: n=5,6 local search lands on point defects again.
- Codex checks: A051 (3.1) 0 violations (it is FEI(C) for restrictions); A052 constant correct;
  A053 Delta I = 2p sum f(a)f(a^i), product-parity full-support argument, TV <= 2 sqrt(p(1-p)) all
  re-derived and correct.

## Refuted / closed (do not repeat)
- Component descent (nine-bit, seven-bit controls); nine-bit control is NOT a block-descent
  obstruction (phi 2.7612 < H/I 2.7690). Point defects and tensor products are not obstructions.
- Searching n<=6 for descent obstructions: point defects dominate; the hard cases need n>=6 and
  indecomposable, non-point-defect structure.
- Tensor indecomposability as a quantitative property: one-point surgery gives it for free (A053).

## Next target per agent
- A051: phi = min_A L_A/I_A exactly on iterated point-defect compositions (FEI lower-bound
  family), n=6..9, orbit reduction; report phi/(H/I) and the first composition with phi > 4.54.
- A052: restate the pivot obstruction with beta_A (R1) and decide on those compositions whether
  some block has H(Z_A|Z_C) + (2/ln2) beta_A <= (H/I) I_A.
- A053: prove continuity of phi under one-point surgery with explicit remainder, so near-tensors
  inherit phi <= H/I from R6.
- A054: run phi on the seven-bit Brain45 witness; define the interface term as a cross term of
  L_A over components and pay it on a critical class.
- A055: activation embedding (C013) of an arbitrary core: compute phi and the R2 singleton
  inequality as rarity p -> 0; say which block inequality fails first, with numbers.

## Open (first unsupported line)
A finite K with K_desc(n) <= K for all n (every f has a proper block with L_A <= K I_A).
