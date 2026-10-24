# B07 stream notes (Claude lead) - v2, 2026-10-11 23:45 UTC

Full FEI: OPEN. Read before every stage. A finite check is evidence; a claim closes only with a proof or exact certificate.

## Established (lead run 20261011T230024Z, CERTIFIED/PROVED, review pending A088/A094)
- Two-address class: the 3-variable one-point defect (addresses = 2 of its variables, third coordinate alone in every
  conditional law, so every conditional law is trivially product) has H/I = 16/3 - (3/2)log2 3 = 2.9559 > 40/17.
  So C_2 >= 2.9559, and C_k >= max H/I over (k+1)-variable functions. X008 (40/17) is not extremal.
- Exhaustive N<=5 census (1,564,928 functions at N=5, integer certificate): max H/I is exactly that value, attained only
  by embedded point defects. N=4 count 10,560 confirmed by brute force over all truth tables.
- Generic inequality, no Booleanity: p_max (H - H_inf)^2 <= (1 - p_max) Var_p(ell), with EQUALITY on point defects.
  A031's anchor is correct but its point-defect calibration is generic (and looser than this bound there).
- A032's ten-atom obstruction, 2261 laws, 840/360360 pattern count and the even-rank admission (n<=4) re-derived: accept.

## Rules for every new B07 inequality
- Must FAIL for some normalized non-Boolean vector (psi_n, or the dyadic fixed-order family). Otherwise it is a generic
  probability fact.
- Must survive vacuous embeddings: a hypothesis on conditional laws is empty when each conditional law has one active
  coordinate; test the 3-bit point defect first.
- Uniform B<=K*I is FEI-equivalent (C018): never a helper.

## Targets (one each)
- A031: drop anchor/Cauchy routes. Coordinate erasure via F = E_i f + i D_i f in {+-1,+-i}: Boolean iff F^4 = 1,
  Inf_i = P(F in {+-i}), B_i = sum_T |Fhat(T)|^2 h(sin^2 arg Fhat(T)). Prove one bound that uses F^4 = 1 and name the
  non-Boolean control it excludes.
- A032: N=6 two-address search for H/I > 2.9559, pure configurations first (four {0,+-1} slices with disjoint supports,
  product spectra). Exact integer certificate for any hit; frozen spec first.
- A033: your phase-degree payment kappa(d): check it on the 3-bit point defect and on psi_n; state which hypothesis
  excludes each.
- A034: conditional phase bound with the tensor guard AND the vacuous-embedding guard. The two-address constant now
  starts at 2.9559; target the first unsupported line: realizable heavy slices obey sum_J w_J N_J <= K(H(w) + E|J|),
  where N_J counts non-fair coordinates (u_J >= 5^N_J from the norm-arithmetic lemma).
- A035: countertests: point defects, their tensor powers, bent+point surgery, against every frozen B07 payment;
  exact or interval certificates.

## Do not repeat
- Fixed convolution prefixes, dyadic granularity, small square defects as new admission conditions.
- Point-defect calibration as evidence of Booleanity use.
- 40/17 as the two-address benchmark.
- Dense 2^n x 2^n matrices for n >= 12 (memory limit 1 GB): use fast transforms.
