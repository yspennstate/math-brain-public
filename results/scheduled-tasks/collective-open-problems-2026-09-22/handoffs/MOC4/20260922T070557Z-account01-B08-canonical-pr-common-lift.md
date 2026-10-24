# MOC4 handoff — account01/B08 canonical P/R common-compound lift

Run: `20260922T070557Z-account01-B08-MOC4-r11`  
Outcome: **ESSENTIAL_STEP_APPLIED**; parent MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.  
Execution: `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

Canonical scientific report: `yspennstate/math-open-problems/proofnet24/collective-MOC4/account01/B08/20260922T070557Z-account01-B08-MOC4-r11/REPORT.md`, report blob `565ca44ea43e09a1454061baf4a5015379b1b5d0`. Exact verifier blob `fb4c24bd92789ab0a65a25c849dd3c341d29a73f`; captured PASS output blob `a7d47916c126bc6980bfdc9ad3e55a25b7d4c0d9`.

## Inputs actually consumed

- Latest complete campaign lead: account03/B07 `20260922T064004Z-account03-B07-MOC4-r12`, `MOC4-KERNEL-QUARTIC-RESERVE-v1` / `MOC4-MIXED-SCHUR-LS-GATE-v1`.
- Assigned OTHER-account partner: account02/B09 `20260922T064517Z-account02-B09-MOC4-r17`, `MOC4-TRANSPOSE-TIE-SAFE-v1`.
- Prior account01/B08 no-go retained: the unconditional positive joint `(P,R)` lift is false for a genuine true unitary, so no universal-positive claim is revived.

## New exact theorem

For a true `U in U(4)`, let `P_ij=|u_ij|^2`. Let `R` be the genuine `3 x 3` complementary-pair channel, with

`R_{alpha,beta}=|det U[S,T]|^2+|det U[S,T^c]|^2`

for `alpha={S,S^c}`, `beta={T,T^c}`. Let `rho:S4->S3` be the action on the three complementary-pair partitions. For **any** Birkhoff decomposition

`R=sum_r mu_r P_r`,

define

`nu_sigma = (1/8) sum_i P_{i,sigma(i)} + (1/4) mu_{rho(sigma)} - 1/8`.

Then `sum nu=1`, and the same `nu` reproduces **every** true squared compound minor simultaneously:

`sum_{sigma:sigma(I)=J} nu_sigma = |det U[I,J]|^2`

for every equal-cardinality `I,J` and every degree `0<=|I|=|J|<=4`.

The key dimension-four identity is

`|det U[S,T]|^2 = ( sum_{i in S,j in T} P_ij - 1 + R_{alpha,beta} )/2`,

so matching `P` and `R` is in fact enough to match each individual degree-two minor, not merely an aggregate. Degree three follows by complements.

Therefore

`det(D_a+U D_b U*) = sum_sigma nu_sigma prod_i(a_i+b_{sigma(i)})`

for arbitrary complex spectra, including repeated and singular cases. If all `nu_sigma>=0`, this is a genuine convex common-compound representation.

**Structural corollary:** membership of the true same-unitary pair `(P,R)` in the joint permutation polytope `conv{(P_sigma,P_rho(sigma))}` is not merely a necessary projection test; it is **equivalent** to existence of a full positive common-compound law for that `U`.

## Explicit positivity gates

Write `p=min_ij P_ij`, `q=min_alpha,beta R_alpha,beta`. Choosing a Birkhoff decomposition with every `mu_r>=q/2` gives

`nu_sigma >= (4p+q-1)/8`.

Hence the source-valid sufficient certificate

`4p+q>=1  =>  full positive common-compound lift => MOC4 for this U for every spectra pair`.

No claim is made here that this numerical region strictly enlarges the true-unitary locus covered by earlier certificates; the exact theorem is the canonical section and its feasibility test.

More sharply, let `A_sigma=sum_i P_{i,sigma(i)}` and

`t_r=(1/2)max(0,1-min_{sigma:rho(sigma)=r}A_sigma)`.

The canonical section is nonnegative iff `R` has a Birkhoff coefficient vector satisfying `mu_r>=t_r` for all six quotient permutations. Because the `3 x 3` Birkhoff fiber is one-dimensional, this is an exact finite interval-feasibility test.

## Partner application / next obligation

Account02/B09's `MOC4-TRANSPOSE-TIE-SAFE-v1` says any positive-gap global maximizer has all row/column transposition gaps strict. Combining it with the theorem above, any actual violator must simultaneously:

1. satisfy all those strict physical pair-gap inequalities;
2. satisfy the campaign lead's surviving `MSQR` or `NDI` maximizer conditions;
3. fail the full joint-polytope/common-compound feasibility condition, and in particular fail the canonical lower-bound system above.

Next exact implication: `MOC4-MAXIMIZER-JOINT-FEASIBILITY-v2` — prove that no true-unitary positive-gap maximizer satisfying the lead/partner stationarity and Hessian constraints can lie outside the joint `(P,R)` permutation polytope, or use an actually violated joint facet together with structured spectral support to obtain a genuine target counterexample. Negative coefficients alone remain irrelevant.
