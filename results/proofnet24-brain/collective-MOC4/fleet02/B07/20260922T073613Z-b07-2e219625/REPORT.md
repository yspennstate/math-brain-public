# fleet02/B07 MOC4 — full-Hessian Lyapunov–Schmidt cross-reserve

Run: `20260922T073613Z-b07-2e219625`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Outcome: **ESSENTIAL_STEP_APPLIED**  
Candidate: **`MOC4-MIXED-SCHUR-FULL-LS-CROSS-RESERVE-v1`**  
Parent target: **OPEN / NOT PROVED / NOT DISPROVED**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Fresh authority and scope


Protected-control blobs at the initial fresh read were:

- `AGENTS.md`: `94387098453b9f4a9b10179183f6f6ec780fd987`
- `scheduled_tasks/README.md`: `3d4a9372c87802ab734141a3374d04c8823372e3`
- `scheduled_tasks/fleet.json`: `e647d5d2479749f80ce7bb4862bee0f28513c7d9`
- `scheduled_tasks/roles.json`: `ed17ecc94f76720c0345b3e32249b791b20ec611`
- `scheduled_tasks/PROTOCOL.md`: `83a9268bf5287ca203e4be69a79e25382397bca7`


## 2. Source-bound lineage consumed

The latest complete campaign-lead state recovered before this proof is fleet03/B07 run `20260922T064004Z-fleet03-B07-MOC4-r12`, theorem `MOC4-KERNEL-QUARTIC-RESERVE-v1`, canonical report `yspennstate/math-open-problems/proofnet24/collective-MOC4/fleet03/B07/20260922T064004Z-fleet03-B07-MOC4-r12/REPORT.md`, creation commit `db68657018c5673e12729567dde29d01139d1971`, report blob `ec11bc9937109dc0059b8e2ab78a485a9f646e3e`. It splits a hypothetical positive-gap maximizer into the mixed-Schur boundary `MSQR` and the all-negative-definite branch `NDI`, and proves the pair-block Lyapunov–Schmidt necessary condition

`J4(Z*) + 3 <ell#,(-H_pair)^+ ell#> <= 0`.

The latest named-partner state consumed is fleet03/B08 run `20260922T072320Z-fleet03-B08-MOC4-r12`, theorem `MOC4-GENERIC-FACET-LADDER-v1`, canonical report blob `da2892a8a90526b2abdeecf897743fc5a51364e6`. Its exact generic-facet ladder demonstrates that tiny true-unitary support gaps are not informative until all elementary left/right pair stationarity and strictness gates are imposed. This run works precisely on the subsequent stationary/global-maximizer regime rather than on nonstationary near-facet points.

The named OTHER-account result applied directly is fleet03/B20 run `20260922T071802Z-fleet03-B20-MOC4-r12`, theorem `MOC4-MIXED-SCHUR-TRUST-COLLAPSE-v1`, canonical report blob `e37d1ae846af5e734e0051aad54aa1d7cb623ed6`. It proves that the complete same-pair global `S^2 x S^2` trust-region condition is exactly redundant with the lead's same-pair Lyapunov–Schmidt reserve on the mixed-Schur boundary, and explicitly identifies cross-split coupling / the full Spin(6) Hessian as the missing information. The present result implements that mechanism change.

Also retained as essential dependencies are fleet04/B08 run `20260922T061235Z-fleet04-B08-MOC4-r12` (`MOC4-STRICT-SPIN4-SECTORS-v1` and the exact mixed-Schur block), and this worker's immediately preceding theorem `MOC4-SPIN4-PAIR-ROOF-RESERVE-IDENTITY-v1`, which identifies complementary pair-block scalar reserves with exact target-roof deficits.

## 3. General full-Hessian cross-reserve theorem

Let `F:R^n -> R` be `C^4` near `0` and have a local maximum at `0`. Put

`A = -D^2 F(0) >= 0`.

Split the real tangent space orthogonally as `S ⊕ W` and write

`A = [[P,B],[B^T,C]]`.

Suppose `z in S` is a kernel direction of the pair block: `P z = 0`. Embed it as `(z,0)` in the full space. Because `A>=0` and

`(z,0)^T A (z,0) = z^T P z = 0`,

positive semidefiniteness implies `A(z,0)=0`; in particular

`B^T z=0`.

Therefore `ker P subset ker B^T`, equivalently `range B subset range P`.

Define the generalized Schur complement

`S_c = C - B^T P^+ B >= 0`,

where `P^+` is the Moore–Penrose pseudoinverse. For the pair-kernel direction define the cubic covector and quartic coefficient

`ell(y)=D^3F(0)[z,z,y]`,

`q=D^4F(0)[z,z,z,z]`.

Decompose `ell=(u,v)` with `u in S*`, `v in W*`.

### Theorem 3.1 — full Lyapunov–Schmidt necessary condition

At a local maximum,

1. `D^3F(0)[z,z,z]=0`;
2. `ell` annihilates `ker A`, hence `ell in range A`;
3. `q + 3 ell^T A^+ ell <= 0`.

**Proof.** Use the curved perturbation

`x(t)=t z+t^2 y`.

Since `Az=0`, the Hessian contributes first at order `t^4`. The odd `t^3` coefficient along the kernel line must vanish. The exact `t^4` coefficient is

`-1/2 y^T A y + 1/2 ell(y) + q/24`.

If `ell` did not annihilate `ker A`, taking the kernel component of `y` with either sign and arbitrarily large fixed coefficient would make the displayed coefficient positive, contradicting local maximality for sufficiently small `t`. Thus `ell in range A`. Maximizing the quadratic expression over `y` gives `y=(1/2)A^+ell` modulo `ker A` and maximum

`(1/8) ell^T A^+ell + q/24 <= 0`.

Multiplying by 24 gives the claim. No inverse of a determinant point occurs.

### Theorem 3.2 — exact block reserve decomposition

Because `range B subset range P`, let `K=P^+B`. Then

`A = T^T diag(P,S_c) T`,

with

`T=[[I,K],[0,I]]`.

For `ell in range A`, one necessarily has

`u in range P`,

`r := v-B^T P^+u in range S_c`,

and the exact energy identity

`ell^T A^+ell = u^T P^+u + r^T S_c^+r`.

Indeed `T^{-T}ell=(u,r)`. Solving the congruence-reduced system gives the two pseudoinverse energies; because `ell` is orthogonal to `ker A`, `ell^T x` has the same value for every solution of `Ax=ell`, so this energy equals `ell^T A^+ell` even though a nonorthogonal congruence does not itself commute with the Moore–Penrose operation.

Combining Theorems 3.1 and 3.2 gives the new **full mixed-Schur gate**

`q + 3 u^T P^+u + 3 r^T S_c^+r <= 0`.        (FULL-LS)

The lead's same-pair gate is only

`q + 3 u^T P^+u <= 0`.                         (PAIR-LS)

Thus the missing full-Hessian information is exactly the nonnegative cross-split reserve `r^T S_c^+r`.

If

`Delta := -(q+3u^T P^+u) >= 0`

is the pair-only Lyapunov–Schmidt slack, then

`r^T S_c^+r <= Delta/3`.                        (3.3)

In particular, **at exact pair-LS saturation `Delta=0`, one must have**

`r=0`, i.e. `v=B^T P^+u`,                      (3.4)

because `r in range S_c`. More quantitatively,

`r^T S_c^+r >= ||r||^2/lambda_max(S_c)`,

so

`||r||^2 <= (Delta/3) lambda_max(S_c)`.          (3.5)

This is the cross-split cubic payment absent from all same-pair trust-region tests.

## 4. MOC4 / Spin(6) specialization

Now let `F` be a fixed real support functional of

`D(U)=det(D_a+U D_b U*)`

restricted to the genuine row-unitary orbit through a hypothetical positive-gap global maximizer `U`. Its six unordered row pairs give six complex root planes, hence a 12-dimensional real off-diagonal tangent space. This is a true-unitary tangent space; no bistochastic surrogate is introduced.

Choose one complementary transposition pair and let `S` be its four-dimensional Spin(4) root block. On the lead's `MSQR` boundary, let `z` be a kernel vector of its negative Hessian `P=-H_pair`. Let `W` be the remaining four root planes, of real dimension eight. The full negative row-root Hessian has the block form above.

For each remaining transposition/root plane `sigma`, genuine two-plane variation gives

`h''_sigma(0)=2(h(P_sigma U)-h(U))=-2 g_sigma`,

where

`g_sigma=h(U)-h(P_sigma U)>=0`.

Therefore the diagonal negative-Hessian block on that two-real-dimensional root plane is `2 g_sigma I_2`, and

`tr C = 4 sum_{sigma in W} g_sigma`.

Since `0<=S_c<=C`,

`lambda_max(S_c) <= tr S_c <= tr C = 4 sum_{sigma in W}g_sigma`.

Equation (3.5) consequently yields the MOC4 cross-split estimate

`||r||^2 <= (4 Delta/3) sum_{sigma in W} g_sigma`.       (4.1)

By the preceding B07 pair-roof identity, at a support gap `gamma=h(U)-M>0`,

`g_sigma=2(gamma+rho_sigma)`,

where `rho_sigma>=0` is the exact pair-roof reserve. Hence

`||r||^2 <= (8 Delta/3) sum_{sigma in W}(gamma+rho_sigma)`. (4.2)

At exact pair-LS saturation the conclusion is stronger and parameter-free:

`r=0`.                                                     (4.3)

Thus any structured MOC4 point on the lead's mixed-Schur boundary that saturates the same-pair LS inequality must satisfy eight additional real cross-split cubic compatibility equations encoded by `v=B^T P^+u`. Away from saturation, their defect is quantitatively bounded by the same-pair slack and the other four genuine pair-roof deficits.

This is exactly the kind of information fleet03/B20 proved could not be recovered from the same singular pair orbit alone.

## 5. Singular determinant points and repeated spectra

The theorem is singular-safe. Derivatives of `F` along these unitary exponential paths are derivatives of the determinant polynomial / its polarization (equivalently nested commutator variations). No step uses `(A+B)^{-1}`, no division by `det(A+B)`, and no spectral-gap denominator is introduced. Hence a singular value of `det(A+B)` causes no loss in the local argument.

The repeated-spectrum branch remains covered by the previous B07 exact pair-symmetrized/common-lift argument: if either spectrum has a repeated eigenvalue, the associated swap leaves the determinant unchanged while its two-point average has a genuine common permutation lift, forcing every support functional below the target roof. The remaining proof tree may therefore be restricted to simple spectra without using a singular determinant inverse.

## 6. Exact calibration: cross reserve is genuinely stronger

`VERIFY_FULL_LS.py` uses only Python standard-library exact `Fraction` arithmetic. It takes

`P=diag(0,2,3,5)`,

`B=[[0,0],[1,2],[2,-1],[1,1]]`,

`S_c=diag(7,11)`,

and sets `C=B^T P^+B+S_c`, so the full block matrix is positive semidefinite by the exact congruence factorization. With

`u=(0,1,-2,3)`, `v=(4,-1)`, `q=-12`,

the checker obtains exactly

`u^T P^+u = 109/30`,

`r=(127/30,-49/15)`,

`r^T S_c^+r = 27183/7700`,

`ell^T A^+ell = 165479/23100`.

Thus the pair-only gate passes,

`q+3u^TP^+u = -11/10 <= 0`,

while the full gate fails sharply,

`q+3ell^TA^+ell = 73079/7700 > 0`.

So the new cross reserve is not an algebraic rewriting of the pair gate: it can rule out jets that every same-pair Lyapunov–Schmidt test accepts. This calibration is an abstract exact PSD-jet certificate, not an MOC4 counterexample.

## 7. Conditional end-to-end route and first unpaid implication

A compact conditional proof route is now:

1. repeated-spectrum cases are already covered by the exact common-lift argument, and singular determinant values are handled inverse-free;
2. the lead/partner strict-root results reduce a positive-gap zero-free simple-spectrum global maximizer to the lead's `MSQR` or `NDI` branches;
3. on `MSQR`, the same-pair LS gate is insufficient by fleet03/B20, but the present full-Hessian theorem adds the cross reserve (FULL-LS), with exact rigidity `r=0` at pair-LS saturation;
4. on `NDI`, one still needs a strict interior cross-root/stationarity contradiction;
5. together with the separate zero-face support obligation, exclusion of `MSQR` and `NDI` would rule out every positive support gap, hence prove the 24-vertex convex-hull inclusion by support-function separation.

The first essential missing implication is therefore

**`MOC4-CROSS-SPLIT-CUBIC-PAYMENT-v1`**:

> On a zero-free, simple-spectrum, positive-gap true-unitary global support maximizer in the structured `MSQR` branch, combine the determinant/same-unitary identities, the other pair-root certificates, subgroup roofs, and spectral conditioning to force
>
> `r^T S_c^+ r > Delta/3`
>
> unless `gamma<=0`.

This would contradict (3.3). On the exact-saturation subbranch `Delta=0`, it is enough to show that the exact cross compatibility `r=0`, together with the structured determinant coefficients and the other strict pair gates, forces the known zero-face branch or a contradiction. Conversely, an actual complex-spectrum true unitary satisfying all stationarity/strictness constraints with a strict support separation remains the legitimate counterexample route.

The named partner's `MOC4-GENERIC-FACET-LADDER-v1` is applied here as a guardrail: its tiny-gap but nonstationary exact unitary is excluded before this theorem is invoked, so the new gate is not being tested on an irrelevant near-facet surrogate.

## 8. Failure ledger and claim discipline

- Re-optimizing the complete same-pair trust-region problem is not a route to closure: fleet03/B20 proved that gate collapses exactly to the existing same-pair LS reserve on `MSQR`.
- The exact calibration above proves that passing the pair-only gate does not imply passing the full local-maximality gate; the missing obstruction can live entirely in cross-root cubic coupling.
- No full MOC4 proof is claimed.
- No MOC4 counterexample is claimed.
- No arbitrary bistochastic data are used as if they were unitarily realizable.
- No benchmark gold, private unrelated material, credentials, or external paid computation were used.

The scientific status is therefore **ESSENTIAL_STEP_APPLIED / TARGET STILL OPEN**.
