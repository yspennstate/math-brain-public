SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B03, 2026-09-23T02:19:07Z.
attacking: indefinite-pair / one-volume quarter-Riesz integrability splice — use a k=1 decoupled bank to absorb the physical pair's logarithmic singularity while retaining all sum/difference dependence.

# account02/B03 — one-volume quarter-Riesz plus indefinite-pair logarithmic smoothing

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: `Decoupled time integral`  
Run: `20260923T021907Z-account02-B03-QFORM-auto11`  
Classification: `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREM_PROVED / FULL_TARGET_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The full universal QFORM theorem remains open. This report proves a new synthesis theorem: after completing an invertible indefinite physical pair, a **rank-one decoupled cross-volume** in the residual already supplies enough quarter-order fractional smoothing to absorb the pair's logarithmic singularity and recover a linear small-ball / bounded-density estimate. The proof uses the designated partner account03/B03's weighted Riesz theorem at the new endpoint `k=1, gamma=1/4`, rather than the `k=2, gamma=1/2` endpoint used in the preceding B03 run. No conditional cap is assigned to a conjugate sum/difference variable, and no post-rotation independence is used.

## 1. Sources and correction boundary

Fresh owner control was resolved from `yspennstate/math-research-brain`; before publication main was at `1c9a140cc5268d5f8d0d1a4a9004068747bb306a`, OWNER CONTROL revision `2026-09-22.15`, with QFORM as the sole research target and no applicable account/slot pause.

Required pinned Claude source:

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/COUNTEREXAMPLE_SEARCH.md`.

The designated partner theorem actually used is account03/B03, `QFORM-VOLUME-MARGINAL-WEIGHTED-RIESZ-v1`:

`yspennstate/math-open-problems@406753a39f5fbaf78396b31075f36ae5682ef3ad`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B03/20260922T235821Z-account03-B03-QFORM-r22/REPORT.md`.

The physical-pair logarithmic envelope used as the second completed input is:

`yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`

`proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`.

Live corrections respected include `QFORM-UV-CONDITIONAL-CAP-FALSE`, `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1`, `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE`, the false arbitrary-joint coarea interface, and the false law-uniform pointwise quadratic-phase decay. The present argument keeps all independence statements in disjoint ORIGINAL coordinate banks.

## 2. Partner theorem at the new k=1 endpoint

Let `I,J` be disjoint sets of original independent coordinates in a conditioned residual quadratic-plus-linear form `R`, and let

`M=A[I,J]`.

For `k=1`, define

`Z1=e_1(M^T M)=||M||_F^2>0`,

and the squared-entry volume-sampling row marginals

`alpha_i = sum_j M_ij^2 / Z1`,

with

`h=max_i alpha_i`.

The partner's dependence-safe independent-copy / Brascamp--Lieb theorem states, for any `q>=max(1,2h)`, with

`a=k/(2q)=1/(2q)`,

and every `0<gamma<a`,

`H_gamma(R):=sup_s E|R-s|^(-gamma)`

`<= [a(2pi)^gamma / {gamma(a-gamma) Gamma(gamma) cos(pi gamma/2)}]`

`   * (e/q)^(gamma/2) Z1^(-gamma/2)`.

This comes from one independent-copy Cauchy--Schwarz step and the original-coordinate difference bank. The proof does not claim that `X_j-X'_j` is independent of `X_j+X'_j`.

Assume `h<1` and choose

`q=max(1,2h)<2`.

Then `a=1/(2q)>1/4`, so `gamma=1/4` is admissible. Substitution gives

`boxed:
 H_(1/4)(R) <= C1(q) Z1^(-1/8),
`

where

`C1(q)= [8(2pi)^(1/4)/{(2-q) Gamma(1/4) cos(pi/8)}] (e/q)^(1/8).`   (2.1)

For `h<=1/2`, `q=1` and

`C1(1)=4.284748578336202...`.                                     (2.2)

By Markov,

`sup_s P(|R-s|<rho) <= H_(1/4)(R) rho^(1/4)`.                    (2.3)

Thus one decoupled cross direction gives a quarter-power small-ball exponent uniformly over all self blocks and affine terms retained by the source theorem.

## 3. General fractional small-ball transducer for an indefinite physical pair

Let `U,V` be two original independent cap-one coordinates, independent of the remaining original-coordinate vector `Z`. Let `B` be an invertible indefinite symmetric `2 x 2` physical principal block, and write

`D=|det B|`, `kappa=sigma_min(B)>0`.

After completing this pair, the full quadratic-plus-linear polynomial has the exact form

`Q=((U,V)+m(Z))^T B ((U,V)+m(Z)) + R(Z)`,                        (3.1)

where the shift `m(Z)` may depend arbitrarily on the same variables that generate `R`.

The completed pair-log theorem gives, for every `r>0` and a.e. `t`,

`p_Q(t) <= 2sqrt(2)/r`

` + D^(-1/2) E log_+(2r^2/(kappa |t-R|)).`                       (3.2)

Suppose more generally that for some `0<alpha<=1`,

`sup_t P(|R-t|<rho) <= H rho^alpha`                              (3.3)

for every `rho>0`. Then layer cake gives, with `A=2r^2/kappa`,

`E log_+(A/|t-R|)`

`= integral_0^infinity P(|t-R|<A e^(-v)) dv`

`<= (H/alpha) A^alpha`.                                         (3.4)

Hence

`p_Q(t) <= 2sqrt(2) r^(-1)`

` + [H 2^alpha/(alpha sqrt(D) kappa^alpha)] r^(2alpha).`         (3.5)

For `m=2alpha`, the elementary minimisation

`min_(r>0) {A0/r+B0 r^m}`

`= ((m+1)/m) A0^(m/(m+1)) (m B0)^(1/(m+1))`                     (3.6)

is exact. At `alpha=1/2`, (3.6) recovers the source pair-log constant `4sqrt(2H)(D kappa)^(-1/4)`, providing a check on the bookkeeping.

At the new exponent `alpha=1/4`, (3.5)--(3.6) give

`boxed:
 ||p_Q||_infinity
 <= 3 * 2^(4/3) H^(2/3) D^(-1/3) kappa^(-1/6).
`                                                                  (3.7)

This is the exact bridge needed below: a logarithmic physical-pair singularity consumes only a **positive quarter-order small-ball exponent**, not a half-order exponent.

## 4. New theorem: one decoupled cross volume + one indefinite physical pair

### Theorem 4.1 — `QFORM-INDEFINITE-PAIR-ONEVOLUME-QUARTER-RIESZ-v1`

Assume the situation of Section 3. In the Schur residual `R`, suppose there are disjoint original-coordinate banks `I,J` with cross block `M`,

`Z1=||M||_F^2>0`,

and maximum row energy marginal

`h=max_i sum_j M_ij^2/Z1 <1`.

Put `q=max(1,2h)`. Then the full ambient quadratic form satisfies

`boxed:
 ||p_Q||_infinity
 <= C_pair1(q) D^(-1/3) kappa^(-1/6) Z1^(-1/12),
`                                                                  (4.1)

where

`C_pair1(q)=3*2^(4/3)*C1(q)^(2/3)`.                              (4.2)

For `h<=1/2`,

`C_pair1(1)=19.942433131734543...`.                              (4.3)

Consequently every interval `J0` obeys

`P(Q in J0) <= C_pair1(q) D^(-1/3) kappa^(-1/6) Z1^(-1/12) |J0|`.

#### Proof

The partner theorem gives (2.1), hence (2.3) with

`H=C1(q) Z1^(-1/8)`.

Insert this `H` into (3.7):

`H^(2/3)=C1(q)^(2/3) Z1^(-1/12)`.

This is exactly (4.1). All conditioning is on original coordinates. The pair shifts may be arbitrarily dependent on `R`; the pair-log theorem was designed for that dependence. The decoupling theorem uses only the independent coordinate differences inside its chosen bank and never separates a conjugate sum/difference pair. QED.

### Interpretation

The preceding B03 run required a rank-two decoupled bank because a physical **square** peel consumes `H_(1/2)`. The present theorem shows that an indefinite physical pair is analytically cheaper: its logarithmic singularity consumes only `H_(1/4)`, so a rank-one decoupled volume is already sufficient. This is a real reduction in the cross-rank needed for a paid branch.

## 5. Source-valid higher-rank target family paid by the theorem

The theorem is not merely a residual lemma. Fix `m>=2` and `0<epsilon<1`. Let

`B=[[0,1],[1,0]]`,

and on a disjoint bank of `2m` coordinates put

`v=(1,...,1)/sqrt(2m)`,

`S_m=epsilon I_(2m)+v v^T`.

Set

`A_m=B direct_sum S_m`.                                           (5.1)

The eigenvalues of `A_m` are

`+1, -1, 1+epsilon, epsilon (multiplicity 2m-1)`.                 (5.2)

Thus `A_m` is a genuine owner-target matrix with at least three eigenvalues of modulus at least one; it also has arbitrarily many nonzero small eigenvalues, so it is not an exact-rank-three case.

Partition the residual bank into equal halves `I,J`. Since the diagonal `epsilon I` contributes no cross entries,

`M=S_m[I,J]=v_I v_J^T`.                                          (5.3)

Therefore

`Z1=||M||_F^2=||v_I||^2 ||v_J||^2=1/4`.                         (5.4)

Every row has the same cross energy, and the volume-sampling row marginal is

`alpha_i=1/m`, hence `h=1/m<=1/2`.                               (5.5)

The physical pair has `D=kappa=1`. Applying (4.1) gives, uniformly in `m`, in `epsilon in (0,1)`, and in all independent cap-one input laws,

`boxed:
 ||p_(X^T A_m X)||_infinity
 <= C_pair1(1) 4^(1/12)
 =22.38462434131946... .
`                                                                  (5.6)

The same analytic estimate survives arbitrary additional self-block and affine terms that leave the completed pair and the residual cross certificate `(Z1,h)` intact; for the explicit family (5.1), the target spectral hypothesis is verified directly by (5.2).

This example demonstrates why the theorem is complementary to the source exact-rank-three physical-pair theorem: the residual here is full rank because of the `epsilon I` tail, but one aggregate cross direction still supplies exactly the fractional integrability needed by the pair logarithm.

## 6. What remains unpaid

The full conjecture is still open. The analytic splice proved here pays the following branch:

- an invertible indefinite physical pair with quantitative `D` and `kappa`, and
- after its Schur completion, a disjoint original-coordinate residual cross block with `Z1` bounded below and row-energy marginal bounded away from the hub endpoint `h=1`.

The first structural implication still missing from the bare three-large-eigenvalue hypothesis is an exhaustive alternative that forces either this certificate or one of the already-paid aggregate exits (rank-two volume plus square, mixed hub/bank Fresnel, diffuse higher-volume, exact-null coloop, or a bounded physical core) at universal scale. In particular, the theorem does not assert that every N3 matrix has such a pair or such a nonhub rank-one residual cross bank.

The new mathematical lesson is narrower and source-valid: **once an indefinite pair is available, the residual decoupled rank requirement can drop from two to one.** The remaining obstruction is structural aggregation/localisation, not the time-integrability exponent for this branch.

Independent review status: not independently reviewed in this run. Full target remains OPEN; continuity is not claimed by this argument.
