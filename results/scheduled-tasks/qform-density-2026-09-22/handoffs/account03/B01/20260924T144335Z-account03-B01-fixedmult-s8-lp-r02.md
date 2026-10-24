SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B01, 2026-09-24T14:43:35Z.
attacking: the multiplicity-eight robust two-anchor endpoint via determinant-free finite-Lp and small-ball control.

Objective actually followed: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`, which is later than and supersedes the older B01 oscillatory-role focus for task selection. Legacy owner control remains revision `2026-09-22.15`. Full three-eigenvalue conjecture remains OPEN.

## New proved supporting theorem

`QFORM-ROBUST-TWO-ANCHOR-FINITE-LP-v1`.

If `X in R^2` has probability density `f<=1`, `Y` is independent, `K=K^T` is arbitrary, `L=L(Y)` has density `g<=M`, and `R=R(Y)` is arbitrary and may be dependent on `L`, then `Q=X^T K X+2 X·L+R` satisfies

`|phi_Q(t)| <= min(1, pi sqrt(M)/|t|)`.

Hence for every finite `r>=2`, `||p_Q||_r <= (r sqrt(M))^(1-1/r)`, and for intervals of length `h`, `P(Q in J) <= (r sqrt(M) h)^(1-1/r)`. If `sqrt(M)h<=e^-2`, optimizing at `r=log(1/(sqrt(M)h))` gives `P(Q in J) <= e sqrt(M) h log(1/(sqrt(M)h))`. For `0<alpha<1`, `sup_a E[|Q-a|^-alpha 1_{|Q-a|<=1}] <= [4(1+alpha)sqrt(M)/(1-alpha)^2]^((1+alpha)/2)`.

Proof mechanism: encode arbitrary dependence of `R` on `L` by a complex density multiplier `h_t(l)` with `|h_t|<=1`, then apply Cauchy-Schwarz in the two-dimensional random slope and exact 2D Plancherel to `f(x)e^{it x^T K x}`. The anchor quadratic phase disappears from the L2 norm. No one-dimensional pointwise van-der-Corput estimate is used.

## Application to current s8 frontier

Input from account03/B17: `yspennstate/math-open-problems@0408c579bcda638e72c010ff99892a22b9049796`, robust pair with `D_H=det(CC^T)>=D0=0.3649442658827020...` in the remaining no-pivot `s_8>=1` collar. Baseline product-projection gives `L=CY+b/2` density cap `M <= e/sqrt(D0) = 4.499675651055483...`, so `sqrt(M)<=2.121243892402636...`.

Therefore throughout the entire robust-pair collar, uniformly for zero, rank-one, invertible, and arbitrarily near-singular anchor self-blocks,

`|phi_Q(t)| <= min(1,6.664084228844337/|t|)`,

`||p_Q||_r <= (2.121243892403 r)^(1-1/r)` for every finite r>=2,

and for `2.121244 h<=e^-2`, `P(Q in J)<=5.766138726448 h log(1/(2.121243892403 h))`.

At alpha=1/2 the truncated half-potential is `<19.060`. Thus the near-singular self-block determinant is no longer an obstruction at any finite Lp level. Multiplicity eight is still OPEN because the final endpoint logarithm has not been removed; no L-infinity or continuity claim is made for this theorem.

## Partner application and obstruction

Applied completed account04/B01 result `yspennstate/math-open-problems@beb9cc5cbb78b4fd4a8411862ac99fd7b7976034`: its `s_13` L2 theorem implies `P(Q in J) <= sqrt(6010) K/sqrt(s) |J|^(1/2) <77.525 K/sqrt(s) |J|^(1/2)`.

The phase-aligned counterexample remains preserved: for every fixed nonzero frequency tau and epsilon>0, a cap-one density can be supported on finitely many fragments totaling measure one where `tau x^2` is within epsilon modulo `2pi` of zero, hence `Re E exp(i tau X^2)>=cos epsilon`.

## Immutable source

Repository: `yspennstate/math-open-problems`
Full commit containing report + checks: `8b028e674c0702d5a27d4370b40015e9382a0d77`
Report: `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/account03/B01/20260924T144335Z-account03-B01-fixedmult-s8-lp-r02/REPORT.md`
Checks: sibling `CHECKS.txt`, `STATUS=PASS`.

Next exact obligation: `QFORM-S8-ROBUST-TWO-ANCHOR-LOG-ENDPOINT-REMOVAL-v1` — use original-product provenance of `L=CY+b/2` and the same-bank quadratic nature of `R`, not an arbitrary joint-law replacement, to remove the one remaining logarithm and obtain a true L-infinity bound.

Baseline support-package mismatch from the earlier B01 audit is resolved: `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, and `checks.json` are now present. No new fatal baseline defect was found.

Brain status: `WITHOUT_VERIFIED_BRAIN`; repository retrieval/writeback is verified, native learned-memory receiver ingestion is not.
