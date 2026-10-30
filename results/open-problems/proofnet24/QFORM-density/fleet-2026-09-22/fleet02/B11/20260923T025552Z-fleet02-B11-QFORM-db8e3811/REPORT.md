SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B11, 2026-09-23T02:55:52Z.
attacking: the remaining opposite-sign two-sheet branch via minority-sign Schur completion and exact product-preserving half-Riesz smoothing.

# fleet02/B11 — minority-sign Schur sharpening and a dependent-pair falsifier

**Status:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREM + SOURCE-VALID OBSTRUCTION / FULL_TARGET_OPEN`.

The full QFORM conjecture is not proved here. The first unpaid implication attacked is the genuinely rotated exact-rank-three indefinite branch when an ORIGINAL coordinate has the minority physical sign. The new estimate is uniform in the output level, improves the current fleet03/B11 cone-pivot bound on this branch, and uses the newest required Claude package at an actual inequality. A second construction shows exactly why the remaining near-null argument may not replace product-projection provenance by an arbitrary bounded joint pair density.

## 1. Source pins actually used

1. Required Claude source: `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/COUNTEREXAMPLE_SEARCH.md`. Its proved rank-two PSD theorem states that for two orthonormal spectral directions and positive eigenvalues `sigma1,sigma2`, the product-input quadratic form has density at most

   `2*pi / sqrt(sigma1*sigma2)`.

   The same source's ruled theorem gives the `(2,1)` one-sheet side `t>=0` the dimension-free bound `<= pi*sqrt(2)` when all three spectral magnitudes are at least one.

2. Designated partner actually applied: fleet03/B11 r22, `yspennstate/math-open-problems@3a8e3494dac898f3b7180d5b80a8c5eb974a8412`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B11/20260923T021243Z-fleet03-B11-QFORM-r22/REPORT.md`. Its full-matrix theorem gives, if two ORIGINAL physical diagonals satisfy `Aii>=eta` and `Ajj<=-eta`,

   `||p_Q||_inf <= eta^(-1) [9.2 + log_+(10000 eta)]`.

   Its exact-rank-three cone theorem gives a two-sheet bound of order `(L/|Aii|)^2` when a minority-sign physical pivot exists. Section 3 below sharpens that dependence by a different Schur mechanism.

3. The current control/correction set forbids independence after spectral rotation, arbitrary-joint rank-three coarea, a universally good physical minor/cross cut, and treating a small matrix perturbation as a small random quadratic error on arbitrary unbounded inputs. None is used below.

## 2. Rank-two logarithmic control and what the third direction must do

For two opposite-sign directions the logarithmic singularity is genuine. For example, if `U,V` are centered unit-interval uniforms, the product form `2UV` has a logarithmically divergent density at zero. Therefore no proof below promotes the rank-two saddle itself to bounded density.

There are two sign-sensitive scalar-Schur geometries for an exact rank-three `(2,1)` form.

* A **majority-sign** positive physical pivot leaves an indefinite rank-two Schur remainder. Its density can retain the logarithmic singularity; the third scalar square must smooth a half-Riesz potential of that remainder. This is the existing orientation-free rank-two-half-Riesz mechanism.
* A **minority-sign** negative physical pivot leaves a positive-semidefinite rank-two Schur remainder. Here the newest Claude rank-two PSD theorem supplies an actual bounded remainder density. The third scalar square then costs only a one-sided half-Riesz transform of a bounded density. This gives the sharper theorem below.

Thus the third direction is used explicitly; the opposite-sign rank-two failure is retained rather than hidden.

## 3. New theorem: minority-sign Schur definite sharpening

### Theorem 3.1 — `QFORM-MINORITY-SCHUR-DEFINITE-v1`

Let

`A = R Lambda R^T`, `R^T R=I_3`,

with exact rank three and signature `(2,1)`,

`Lambda = diag(lambda1,lambda2,-mu)`, `lambda1,lambda2,mu >= 1`.

Let `r_i` be the `i`-th row of `R`, put `c_i=||r_i||^2`, and suppose one ORIGINAL physical diagonal has the minority sign

`a=A_ii<0`.

Then for every independent cap-one product input,

`||p_{X^T A X}||_inf <= 2 sqrt(2 pi) ( |a| c_i |det Lambda| )^(-1/4).`        (3.1)

In particular, if `|a|>=eta`, then, with no leverage hypothesis and no dependence on the spectral condition number,

`||p_{X^T A X}||_inf <= 2 sqrt(2 pi) eta^(-1/2).`                            (3.2)

Reflection gives the signature `(1,2)` statement: a positive ORIGINAL physical diagonal carrying the unique positive sign satisfies the same estimate.

At `eta=1/4`, (3.2) is `< 10.027`, compared with the current partner cone estimate whose two-sheet term is `8 sqrt(pi e) eta^(-2)` after normalization by the top spectral scale.

### Proof

Partition the matrix at the original coordinate `i`:

`A = [[a,b^T],[b,C]]`,

and set the Schur complement

`S = C - b b^T/a`.

Because `a<0` consumes the unique negative direction, Sylvester inertia additivity gives

`S >= 0`, `rank(S)=2`.

Let its two nonzero eigenvalues be `s1,s2>0`.

#### Exact pseudodeterminant identity

For every pair `J={j,k}` not containing `i`, Schur's determinant identity gives

`det A[{i} union J] = a det S[J]`.

Summing over all such pairs and using `rank(S)=2`,

`a s1 s2 = sum_J det A[{i} union J]`.                                      (3.3)

Because `A=R Lambda R^T` has exact rank three, Cauchy-Binet gives

`det A[I] = det(Lambda) det(R_I)^2` for every 3-set `I`.

Furthermore

`sum_{J: |J|=2, i notin J} det(R_{ {i} union J})^2 = c_i`.                  (3.4)

For completeness, total squared 3-row volume is `det(R^T R)=1`, while the sum over triples avoiding `i` is

`det(R_{-i}^T R_{-i}) = det(I_3-r_i^T r_i)=1-c_i`.

Subtracting proves (3.4). Since both `a` and `det Lambda` are negative, (3.3)-(3.4) yield

`s1 s2 = |det Lambda| c_i / |a|`.                                          (3.5)

#### Use of the required Claude result

Completing the square only in the ORIGINAL independent coordinate `X_i` gives

`Q = a ( X_i + b^T X_{-i}/a )^2 + R_0`,

`R_0 = X_{-i}^T S X_{-i}`.                                                  (3.6)

The required Claude rank-two PSD theorem applies to `R_0` because `S` is a rank-two PSD quadratic form of the remaining ORIGINAL independent cap-one coordinates. Therefore

`||p_{R_0}||_inf <= M := 2 pi / sqrt(s1 s2)`.                               (3.7)

Conditioned on `X_{-i}`, translation of `X_i` does not change its density cap. The density of `a(X_i+h)^2` is bounded by

`|a|^(-1/2) |w|^(-1/2) 1_{w<0}`.

Consequently, for a.e. `t`,

`p_Q(t) <= |a|^(-1/2) E[(R_0-t)_+^(-1/2)]`.                                (3.8)

For any probability density `g<=M`, layer cake gives the sharp elementary estimate

`sup_t int_0^infty u^(-1/2) g(t+u) du <= 2 sqrt(M)`.                        (3.9)

Indeed, if `U` has density `u -> g(t+u) 1_{u>0}` with total mass at most one, then

`int U^(-1/2) = int_0^infty P(0<U<s^(-2)) ds <= int_0^infty min(1,M s^(-2)) ds = 2 sqrt(M)`.

Combining (3.7)-(3.9),

`||p_Q||_inf <= 2 sqrt(2 pi) |a|^(-1/2) (s1 s2)^(-1/4)`

`= 2 sqrt(2 pi) (|a| c_i |det Lambda|)^(-1/4)`,

which proves (3.1).

Finally let `L=max(lambda1,lambda2,mu)`. Since `|a|=|r_i^T Lambda r_i| <= L c_i`, one has `c_i>=|a|/L`; and since all three spectral magnitudes are at least one, `|det Lambda|>=L`. Hence

`|a| c_i |det Lambda| >= |a|^2`,

which proves (3.2). QED.

### Relation to the ruled one-sheet theorem

The required Claude ruled theorem already pays the one-sheet side `t>=0` by `pi sqrt(2)`. Theorem 3.1 instead pays **all levels** whenever a minority-sign original pivot exists. On the difficult two-sheet side, it replaces the geometric cone-margin loss `(L/|a|)^2` by the Schur identity (3.5), which packages the entire same-sign transverse curvature before inversion.

## 4. Designated partner r22 applied to the full-matrix proof map

Theorem 3.1 is exact-rank-three. The partner's r22 opposite-diagonal theorem is full-matrix and therefore remains the applicable exit when additional nonseparable spectrum is present.

Fix `eta>0`. If an ambient indefinite matrix has ORIGINAL coordinates `i,j` with

`A_ii>=eta`, `A_jj<=-eta`,

then the partner gives the real full-matrix inequality

`||p_Q||_inf <= eta^(-1)[9.2+log_+(10000 eta)]`.                            (4.1)

Thus, after this completed partner exit is removed, any unpaid full-matrix indefinite branch has at most one physical diagonal sign at scale `eta`; the other sign occurs only through diagonals of magnitude `<eta` (or through off-diagonal structure). In the exact-rank-three subproblem, if the minority sign nevertheless occurs at magnitude `>=eta`, Theorem 3.1 improves the branch to (3.2). The surviving B11 chamber is therefore genuinely near-null/one-sign at the physical-diagonal level, not a missed fixed-scale opposite-sign pair.

## 5. New source-valid obstruction: arbitrary bounded dependent pair is not enough

A tempting near-null shortcut is: keep one genuinely independent scalar, replace the remaining projected pair by an arbitrary two-dimensional density cap, and hope the third square universally smooths the rank-two saddle. This is false even for the exact spectral matrix `diag`-congruent to `{1,1,-1}`.

### Proposition 5.1 — `QFORM-DEPENDENT-PAIR-HALFRIESZ-SURROGATE-FALSE-v1`

For every `L>e^8`, put `delta=1/log L` and

`E_L = {(u,v): 1<=u<=L, (1-delta)/u <= v <= 1/u}`.

Its area is

`|E_L| = delta int_1^L du/u = 1`.

Let `(U,V)` have density `1_{E_L}` and let `X` be independent Uniform`[-1/2,1/2]`. All displayed densities are bounded by one, but `U,V` are dependent. For

`Q = X^2 + 2 U V`,

whose coefficient matrix in coordinates `(X,U,V)` is

`[[1,0,0],[0,0,1],[0,1,0]]`

and has spectrum `{1,1,-1}`, one has

`p_Q(2) = sqrt(2 log L) -> infinity`.                                      (5.1)

### Proof

The density of `X^2` is `s^(-1/2)` on `0<s<1/4`. On `E_L`,

`0 <= 1-uv <= delta`,

and `2 delta<1/4` by `L>e^8`. Therefore

`p_Q(2) = int_{E_L} [2(1-uv)]^(-1/2) du dv`

`= (1/sqrt2) int_1^L du/u int_0^delta s^(-1/2) ds`

`= sqrt(2 delta) log L = sqrt(2 log L)`.

QED.

This is **not** a counterexample to QFORM: the target requires the ORIGINAL coordinates to be independent, while `U,V` here are dependent. It is a counterexample to a proof interface. In particular, even an independent cap-one scalar plus an arbitrary cap-one dependent pair does not control the parabolic half-Riesz trace. The completed exact-null/dependent-pair kernels in the fleet therefore need their stronger product-projection provenance; one may not collapse that provenance to a mere joint-density cap.

This also explains the rank-two logarithmic issue sharply: the hyperbolic tube puts unit mass at `UV` within `delta` of one, so the square kernel integrates a `s^(-1/2)` singularity over logarithmically many hyperbolic scales. Genuine product geometry is what must prevent that concentration.

## 6. What remains unpaid

The full QFORM conjecture remains OPEN. The sign-specific branch is narrowed as follows.

* The newest Claude ruled theorem pays the exact-rank-three one-sheet half-line.
* The designated fleet03/B11 r22 pair theorem pays any full-matrix fixed-scale opposite physical-diagonal pair.
* Theorem 3.1 sharply pays an exact-rank-three fixed-scale minority physical pivot, uniformly in the output level.
* Proposition 5.1 forbids replacing the surviving dependent projected pair by an arbitrary joint-density cap.

The first unpaid B11 implication is now the **near-null one-sign physical-diagonal compiler**: in the exact-rank-three or N3 residual where every minority physical diagonal is arbitrarily small and fixed-scale pair exits fail, aggregate the original product coordinates before inversion so that either a genuine product-preserving scalar/dependent-pair kernel, a ruled/volume exit, or a quantitative minority Schur pivot appears. Small scalar curvature itself cannot be discarded perturbatively on unbounded supports.

No continuity claim is made for Theorem 3.1; it establishes essential boundedness in its scope. No novelty is claimed beyond this source-pinned fleet context until external comparison/review.
