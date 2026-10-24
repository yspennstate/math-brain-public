# MOC4 handoff — account04/B07 two-rook Spin(6) constraint

**Run:** `20260922T050458Z-account04-B07-MOC4-r11`  
**Status:** `ESSENTIAL_STEP_APPLIED`; full MOC4 remains OPEN.  
**Scientific source:** `yspennstate/math-open-problems`, `proofnet24/collective-MOC4/account04/B07/20260922T050458Z-account04-B07-MOC4-r11/REPORT.md`, blob `0e64ed2b868fbee674c65fc6e3789e8bbbd7867d`.  
**Exact verifier:** `verify_two_rook.py`, blob `f0dbcfc8b814b621a416d083c52f9a9115f0f52a`; captured output blob `819bec0bca5cfb2f88fbcce35e8a85e4783ceecd`.

## Exact dependencies consumed

- Team lead account03/B07 `20260922T043708Z-account03-B07-MOC4-r11`, report blob `c286ea3e5ec5a72902fbff82e94db343f2bbc543`, `MOC4-TRANSPOSE-SUBGROUP-CUBATURE-v1`.
- Assigned partner account01/B08 `20260922T044241Z-b08-moc4-r12`, report blob `f7391a0c2fdeaef6c5fac2bdfbca4513245e5abf`, including `MOC4-V4-BIRKHOFF-GLUE-v1` and `MOC4-PR-INTERIOR-CERTIFICATE-v1`.
- account04/B07 predecessor `MOC4-SPINOR-SINGULAR-VALUE-v1`, report blob `edef226995227fc0bff482cf97b6ec722abc8efc`.
- account01/B07 exact Spin(6) stationarity report blob `f569427535050fa80aa4fa079c380b1e3035c68f`.

## New theorem

For every even-even Spin(6) gauge `(r,c)`, let

`B^{r,c}_{ab}=|(N_{r,c})_{ab}|^2`, `p=P_{iota(r),iota(c)}`.

The predecessor singular-value theorem gives `sv(N_{r,c})=(sqrt(1-p),sqrt(1-p),0)`. Therefore

`B^{r,c}/(1-p)` lies **exactly in the convex hull of the 18 size-two matchings of K_{3,3}`** (with the `p=1` case equal to zero). The proof augments the normalized `3 x 3` substochastic matrix to a `4 x 4` doubly stochastic matrix with bottom-right entry zero, then applies Birkhoff. Every two-rook vertex is Spin(6)-realizable, so this is the sharp one-gauge linear mass hull.

Consequently, with `C^{r,c}=((-1)^r)((-1)^c)^T \circ K` and `mu_2(C)` the minimum weight of a size-two matching,

`Q_{K,X}(O) <= <R,X/2+C^{r,c}> - 2(1-p) mu_2(C^{r,c})`,

and hence also

`Q_{K,X}(O) <= max_{rho in S3} sum_a (X/2+C^{r,c})_{a,rho(a)} - 2(1-p) mu_2(C^{r,c})`.

These are sixteen valid true-unitary support roofs. Their local Birkhoff weights are **not** asserted to glue into one 24-state law.

## Cross-gauge odd-matching payment

Each forbidden odd signed `3`-matching appears as an anti-linear matching in four compatible gauges. If `p_*` is the maximum of the four corresponding `P` entries, then its selected squared masses `q_1,q_2,q_3` satisfy

`q_1+q_2+q_3 <= 2(1-p_*)`,

`sqrt(q_1)+sqrt(q_2)+sqrt(q_3) <= 2 sqrt(1-p_*)`,

`q_1 q_2 q_3 <= (64/729)(1-p_*)^3`.

For a parity-bad scalar assignment `rho`, with preferred orientation masses `v_a`, wrong masses `w_a`, `m_rho=min |G_{a,rho(a)}|`, and `R_rho=sum r_{a,rho(a)}`, this gives the direct same-unitary penalty

`2 sum_a |G_{a,rho(a)}| w_a >= 2 m_rho [ R_rho - 2(1-p_*^rho) ]_+`.

This is the main target-facing handoff: a parity-bad preferred quotient assignment must pay through a specific four-point unistochastic shadow pattern. It is stronger information than the endpoint-only subgroup cubature but does not assume a global positive lift.

## First missing implication

`MOC4-TWO-ROOK-RESIDUAL-STATIONARITY-v1`: at a genuine positive-reserve global support maximizer for structured spectral coefficients, combine the six complex Spin(6) stationarity balances, the sixteen two-rook roofs, the cross-gauge parity payment above, the lead subgroup cubature, and the partner's valid V4/interior certificates to force the remaining support gap nonpositive. A refutation must use actual spectra/support and a true maximizer; arbitrary `(P,R)` points or independently chosen gauge decompositions do not count.

Exact regression on the partner true-unitary checked all 16 gauges and all 24 odd signed matchings with rational arithmetic; the largest observed normalized odd-mass ratio was `29053648/43405625 < 1` and largest normalized product ratio was `1806991191020961/2827514326000000 < 1`.
