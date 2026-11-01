# fleet01/B01 — random-slope Plancherel replacement and a cross-minor density theorem

**Run:** `20260922T124907Z-b01-qform-auto11`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner control revision `2026-09-22.5`  
**Assignment:** `Oscillatory replacement`  
**Classification:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_TARGET-LEVEL_THEOREM / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and source state

The exact owner target is unchanged: for every `n`, independent real variables `X_i` with densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues satisfying `|lambda_j(A)|>=1`, prove that `Q=X^T A X` has a density with one universal `L^infinity` bound, or produce a target-valid counterexample. No moment, centering, compact-support, log-concavity, sign, diagonal-basis independence, or connected-support hypothesis is available. The requested continuous-density conclusion is tracked separately from essential boundedness.

Fresh controls were read from `yspennstate/math-research-brain` main, first at commit `68bb005560fedbe04bce4a19dde09ea0fb52c800` and refreshed before this write at commit `23a6dfbb212fb16db5743cae733ae25295710dfb`. The owner revision remained `2026-09-22.5`.

Corrections consumed and preserved:

- law-uniform pointwise Fresnel decay for `int exp(it x^2)f(x)dx` is false for arbitrary `f<=1` because phase-aligned fragmented supports exist;
- a projection-density theorem alone does not control an indefinite quadratic pushforward;
- diagonalizing `A` does not preserve independence;
- naive fiber-supremum integration can lose dimension;
- fleet02/B09's correction `QFORM-CROSSMINOR-ALONE-FALSE` only refutes the **two-pivot curved** claim: an invertible `2x2` cross block without a zero pivot-side principal block does not imply bounded density. The theorem below starts at cross dimension three and is compatible with that counterexample.

The scalar phase-alignment counterexample remains valid and is not weakened here. The replacement below obtains decay from **averaging the random linear coefficient created by a genuine cross block**, not from scalar quadratic curvature.

## 2. Named partner result actually applied

The assigned partner `fleet02/B01`, run `20260922T120355Z-fleet02-B01-qform-r19`, canonical report

`yspennstate/math-open-problems@fedbec07e3e8b2f9fcd2b1a65b0bb2a0137c212f:proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B01/20260922T120355Z-fleet02-B01-qform-r19/REPORT.md`

proved that for every nonzero original-coordinate diagonal entry `a=A_ll`, the full coupled characteristic function obeys

`||phi_Q||_3^3 <= 16*pi/|a|`,

with arbitrary outside couplings retained. Section 6 below combines this global `L^3` budget with the new random-slope tail to obtain a strictly different explicit `L^1` inequality. Thus the partner result is used in an actual inequality, not merely cited.

I also checked the completed fleet02/B09 report at

`yspennstate/math-open-problems@fa592b592c61bd1597aa8cf3270c3c9f58f410bf:proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B09/20260922T115241Z-fleet02-B09-QFORM-r1/REPORT.md`.

Its direct small-ball theorem assumes `A[I,I]=0` and already closes invertible cross packets of size `m>=2`. The present theorem removes `A[I,I]=0` for cross dimension `k>=3`; the price is the sharp Fourier threshold `k>2`.

## 3. The exact random-slope Plancherel identity

Let `I` be a set of `k` physical coordinates and write, after conditioning all coordinates outside `I`,

`F_t(beta) = int_{R^k} exp(i t [x^T B x + beta^T x]) prod_{i in I} f_i(x_i) dx`,

where `B=A[I,I]` is completely arbitrary. For each fixed nonzero `t`, regard `F_t` as a function of the **linear coefficient** `beta in R^k`.

Define

`h_t(x)=exp(i t x^T B x) prod_{i in I} f_i(x_i)`.

With Fourier convention `hat h(xi)=int exp(i xi^T x) h(x) dx`, one has

`F_t(beta)=hat h_t(t beta)`

up to an irrelevant sign convention. Therefore Plancherel and the change of variables `xi=t beta` give the exact identity

`int_{R^k} |F_t(beta)|^2 d beta`
`= (2*pi)^k |t|^{-k} int_{R^k} prod_{i in I} f_i(x_i)^2 dx`
`= (2*pi)^k |t|^{-k} prod_{i in I} ||f_i||_2^2`
`<= (2*pi)^k |t|^{-k}`.

The final inequality uses only `0<=f_i<=1` and `int f_i=1`, hence `int f_i^2<=1`.

This is the core replacement for the false scalar pointwise van-der-Corput step. A fixed scalar linear coefficient may still be phase-aligned. What cannot be phase-aligned is a `k`-dimensional family of linear coefficients of bounded density: Plancherel forces an averaged frequency-slope budget.

## 4. Main theorem: invertible disjoint cross packet, arbitrary pivot curvature

### Theorem 4.1 — `QFORM-RANDOM-SLOPE-CROSSMINOR-v1`

Let `X_1,...,X_n` be independent real variables with probability densities `0<=f_i<=1`, and let `A` be any real symmetric matrix. Suppose there are disjoint index sets `I,J` such that

- `|I|=|J|=k`,
- `C:=A[I,J]` is invertible.

No condition is imposed on `A[I,I]`, `A[J,J]`, the signs of eigenvalues, or any other entries of `A`.

Then for every `t!=0`,

`|phi_Q(t)| <= min(1, pi^(k/2) |det C|^(-1/2) |t|^(-k/2)).`          (4.1)

Consequently, if `k>=3`, `phi_Q in L^1(R)`, so `Q` has a bounded **continuous** density vanishing at infinity and

`||p_Q||_infinity <= [k/(k-2)] |det C|^(-1/k).`                       (4.2)

In particular for `k=3`,

`||p_Q||_infinity <= 3 |det A[I,J]|^(-1/3).`                         (4.3)

### Proof

Let `R=[n]\(I union J)` and condition on `X_R`. Write `x=X_I`, `y=X_J`. Under the conditioning,

`Q = x^T B x + 2 x^T C y + 2 u^T x + H(y)`,

where `B=A[I,I]` is arbitrary, `u=A[I,R]X_R`, and `H` contains all terms not involving `x`.

Define `F_t(beta)` as in Section 3. Then

`phi_Q(t) = E_{R,J}[ exp(i t H(X_J)) F_t(2 C X_J + 2u) ]`.

Cauchy-Schwarz discards only the unit-modulus outside phase:

`|phi_Q(t)|^2 <= E_{R,J} |F_t(2 C X_J+2u)|^2`.                       (4.4)

Conditional on `X_R`, the vector

`beta=2 C X_J+2u`

has a density bounded by

`M = 1/|det(2C)| = 2^(-k)|det C|^(-1)`,                              (4.5)

because the joint density of `X_J` is the product `prod_{j in J}f_j<=1`. Hence the exact Plancherel identity gives

`E_J |F_t(beta)|^2`
`<= M int |F_t(beta)|^2 d beta`
`<= 2^(-k)|det C|^(-1) (2*pi)^k |t|^(-k)`
`= pi^k |det C|^(-1) |t|^(-k).`                                      (4.6)

Averaging the unchanged right side over `X_R` and taking square roots proves (4.1).

For `k>2`, put

`K=pi^(k/2)|det C|^(-1/2)`.

Using both `|phi_Q|<=1` and (4.1), for any `T>0`,

`||phi_Q||_1`
`<= 2T + 2K int_T^infinity t^(-k/2) dt`
`= 2T + [4K/(k-2)] T^(1-k/2).`                                       (4.7)

The minimizing choice is

`T=K^(2/k)=pi |det C|^(-1/k)`.                                       (4.8)

Substitution gives

`||phi_Q||_1 <= 2*pi [k/(k-2)] |det C|^(-1/k).`                       (4.9)

Fourier inversion therefore gives a continuous density with

`||p_Q||_infinity <= (2*pi)^(-1)||phi_Q||_1`
`<= [k/(k-2)] |det C|^(-1/k)`,

which is (4.2). Integrability of `phi_Q` also yields a continuous representative vanishing at infinity. `QED`.

## 5. Threshold check and relation to the known two-eigenvalue obstruction

The theorem exposes the dimensional threshold exactly at the level of the random slope:

- `k=1`: (4.1) gives only `|t|^(-1/2)`;
- `k=2`: (4.1) gives the borderline `|t|^(-1)`;
- `k>=3`: the tail is integrable.

Thus the method itself distinguishes the same one/two/three half-power threshold that motivates the owner conjecture. For `k=2`, the fleet02/B09 counterexample

`Q=(X1+Y1)^2-(X2+Y2)^2`

has invertible `2x2` cross block but an unbounded logarithmic density. The present result predicts only a `C/|t|` Fourier bound there and makes no bounded-density claim. So the live correction is respected exactly rather than bypassed.

For the pure six-coordinate hyperbolic packet

`A = [[0,I_3],[I_3,0]]`,

one has `det C=1`, six eigenvalues in `{+1,-1}`, and (4.3) gives the explicit law-uniform bound

`||p_Q||_infinity <=3`

for all six independent marginal densities bounded by one. Unlike a scalar quadratic-phase argument, this conclusion is immune to phase-aligned fragmented supports because it is driven by slope averaging.

## 6. Actual application of fleet02/B01: hybrid low/high-frequency inequality

Assume the hypotheses of Theorem 4.1 with `k=3`, write

`D=|det A[I,J]|`,

and suppose additionally that some original-coordinate diagonal entry `a=A_ll` is nonzero. The partner theorem gives

`||phi_Q||_3 <= L := (16*pi/|a|)^(1/3)`.                              (6.1)

The new cross-packet theorem gives

`|phi_Q(t)| <= K |t|^(-3/2)`,
`K=pi^(3/2)D^(-1/2)`.                                                  (6.2)

For every `T>0`, Holder on the low-frequency interval and (6.2) on the tail yield

`||phi_Q||_1`
`<= (2T)^(2/3) L + 4K T^(-1/2)`.                                     (6.3)

If `A0=2^(2/3)L`, the minimizer satisfies

`T^(7/6)=3K/A0`,

and the minimized right side equals

`7*3^(-3/7) A0^(3/7) K^(4/7)`.                                       (6.4)

Substituting (6.1)-(6.2) and dividing by `2*pi` gives the explicit density bound

`||p_Q||_infinity`
`<= 7*2^(-1/7)*3^(-3/7) |a|^(-1/7) D^(-2/7)`
`< 3.960 |a|^(-1/7) D^(-2/7).`                                       (6.5)

This is an actual combined inequality using the completed fleet02/B01 result. It improves the exponent paid on a small cross determinant from `D^(-1/3)` in (4.3) to `D^(-2/7)` when a useful diagonal gate is also present. The safe bound is the minimum of (4.3) and (6.5).

## 7. Aggregating all cross minors of one physical triple

The fixed-minor theorem still pays one reciprocal determinant and therefore does **not** by itself close the spectral-to-coordinate aggregation problem. There is, however, a clean averaged strengthening using a published bounded-density projection theorem.

Rudelson--Vershynin, *Small Ball Probabilities for Linear Images of High-Dimensional Distributions*, IMRN 2015(19), 9594--9617, DOI `10.1093/imrn/rnu243`, Theorem 1.1, states that if independent coordinates have densities bounded by `K`, the density of every `d`-dimensional orthogonal projection is bounded by `(C_RV K)^d` for an absolute constant `C_RV`.

Fix only a physical triple `I`, `|I|=3`, and put

`C=A[I,I^c]`.

If `rank C=3`, set

`s_I := sqrt(det(C C^T))`.

Writing `C=S U`, with `S=(CC^T)^(1/2)` and `U U^T=I_3`, the projection theorem gives

`||p_{C X_{I^c}}||_infinity <= C_RV^3/s_I`.

Therefore the random slope `beta=2CX_{I^c}` has density cap

`M <= C_RV^3/(8s_I)`.                                                 (7.1)

Using the same Plancherel identity as above,

`|phi_Q(t)| <= pi^(3/2) C_RV^(3/2) s_I^(-1/2)|t|^(-3/2)`,             (7.2)

and hence

`||p_Q||_infinity <= 3 C_RV s_I^(-1/3)`.                             (7.3)

By Cauchy--Binet,

`s_I^2 = det(CC^T) = sum_{J subset I^c, |J|=3} det(A[I,J])^2`.        (7.4)

Thus (7.3) aggregates **all** disjoint `3x3` cross minors attached to the same physical triple before paying the reciprocal cost. This is exactly the kind of operation that the Walsh/Pluecker stress tests require. It also clarifies why a projection-density theorem *alone* was insufficient: the missing step is (3.1), the Plancherel average over the random linear coefficient. The projection theorem supplies only the density cap for that coefficient.

No explicit numerical value of `C_RV` is asserted here; only its published universality is used. The fixed-minor theorem (4.2) is completely self-contained and explicit.

## 8. First essential missing implication toward the full conjecture

The compact conditional route is now:

1. find a physical triple `I` for which the cross-volume
   `s_I=sqrt(det(A[I,I^c]A[I,I^c]^T))`
   is bounded below by a universal constant; then (7.3) proves a universal continuous-density bound immediately;
2. if no such triple exists, exploit that every three coordinate rows have small exterior volume outside themselves, and prove that the matrix must enter one of the already controlled localized/separable branches.

The first unpaid implication is therefore the **spectral-to-cross-volume/local-structure dichotomy**:

`at least three |eigenvalues|>=1`
`=> [some s_I >= c] OR [a quantitatively controlled localized/separable configuration]`,

with a universal `c>0` and a second branch that is genuinely covered by existing local/coarea or separable-phase theorems.

This is not automatic. Rank-three diffuse frames can spread every fixed coordinate minor, while diagonal matrices have `s_I=0` for every `I` but are separately easy. Moreover, algebraic factor-analysis examples show that vanishing disjoint `3x3` off-diagonal minors is not by itself equivalent to `diagonal + rank<=2`; five-index pentad-type constraints can remain. Therefore I do not rename this residual as solved.

A useful exact identity for the next step is

`A[I,I^c]A[I,I^c]^T = (A^2)[I,I] - A[I,I]^2`.                         (8.1)

It expresses the new Fourier smoothing currency `s_I` purely through the full spectral square and the local principal block. A quantitative dichotomy based on (8.1), exterior powers and the already source-valid local triple results is the natural continuation.

## 9. Status, scope, and regularity

**New proved scope.** Every quadratic form having an invertible disjoint `k x k` physical cross block with `k>=3` has a bounded continuous density under arbitrary independent marginal densities `<=1`, with explicit constant (4.2), regardless of all principal-block curvature and all outside couplings. A full-rank three-row cross map admits the aggregated version (7.3) through Rudelson--Vershynin.

**What is not proved.** The owner target remains open because the three-large-eigenvalue hypothesis has not yet been shown to force a universal lower bound on the cross-volume or an already solved alternative branch. No novelty claim is inferred from search or repository absence.

**Continuity.** In the new cross-packet scope continuity is proved, not merely essential boundedness, because `phi_Q in L^1`.

**Classification:** `ESSENTIAL_STEP_APPLIED`; **full conjecture:** `OPEN`.
