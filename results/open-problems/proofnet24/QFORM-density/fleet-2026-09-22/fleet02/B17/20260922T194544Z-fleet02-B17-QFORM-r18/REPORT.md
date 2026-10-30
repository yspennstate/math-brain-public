SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B17, 2026-09-22T19:45:44Z.
attacking: the saturated collinear minority-sign two-heavy branch by exact output-kernel rearrangement, after the nonorthogonal pointwise radial Laplace comparison was corrected false.

# fleet02/B17 — exact rearrangement ceiling for a collinear minority-sign two-heavy branch

Programme: `QFORM-DENSITY-3EIG-20260922`
Assignment: `Sharp constant and witnesses`
Status: `SUPPORTING_SHARP-BRANCH_THEOREM / FULL CONJECTURE OPEN`
Execution memory: `WITHOUT_VERIFIED_BRAIN`

## 1. Scope and source discipline

The full target remains the arbitrary-product-law theorem: independent real physical coordinates with one-dimensional densities at most one, and a real symmetric matrix with at least three eigenvalues of magnitude at least one.

This report does not use law-uniform pointwise quadratic stationary phase, the false arbitrary-joint rank-three coarea inequality, positive moments of conditional projection-density suprema, or independence after spectral rotation. It also explicitly consumes the correction `QFORM-TWO-HEAVY-RADIAL-LAPLACE-DOMINATION-FALSE-v1`: the tempting pointwise two-heavy Gaussian radial-Laplace comparison is false. The replacement below works only after retaining the exact output kernel and rearranging that kernel.

The completed designated-partner result actually applied is fleet03/B17 run `20260922T190408Z-fleet03-B17-QFORM-r15`, canonical report
`yspennstate/math-open-problems@37cd91fd64fa8a508ef9205038d5124a62fc877d:proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B17/20260922T190408Z-fleet03-B17-QFORM-r15/REPORT.md`.
Its theorem says the optimal essential-density constant is unchanged if one restricts to invertible target matrices, and its weak lower-semicontinuity lemma for interval concentration lets singular stress families transfer lower-bound obstructions to invertible perturbations.

## 2. Exact source-valid stress family

For each integer `m>=1`, define a physical-to-spectral frame `R_m` with rows

- `m` copies of `e_1/sqrt(m)`,
- `m` copies of `e_2/sqrt(m)`,
- two rows `e_3/sqrt(2)`.

Then exactly

`R_m^T R_m = I_3`.

Therefore

`A_m = R_m diag(1,1,-1) R_m^T`

has exact nonzero spectrum `{1,1,-1}` for every finite `m`. This is an actual target matrix in the original physical coordinates.

Put centered unit-interval laws on the first `2m` diffuse physical coordinates. Put arbitrary independent cap-one laws `f,g` on the two heavy coordinates `X,Y`. Writing

`Y_{j,m}=m^(-1/2) sum_{k=1}^m U_{j,k}`,

the exact finite form is

`Q_m = Y_{1,m}^2 + Y_{2,m}^2 - (X+Y)^2/2`.

By the ordinary CLT in the two disjoint diffuse banks,

`12 Q_m => W := G_1^2 + G_2^2 - 6(X+Y)^2`,

where `G_1,G_2` are independent standard Gaussians and are independent of `(X,Y)`.

The issue attacked here is whether arbitrary fragmentation/translation of the two heavy cap-one laws, or an off-zero output location, can make this first genuinely nonorthogonal/opposite-sign two-heavy Gaussian-completion branch exceed the current `3 sqrt(2)` obstruction.

## 3. Exact density kernel

Let

`S=X+Y`, `U=G_1^2+G_2^2`.

Since `U` has density

`p_U(u)=(1/2) exp(-u/2) 1_{u>=0}`,

the limiting output has the everywhere-defined density

`p_W(t) = (1/2) exp(-t/2) int f(x)g(y) exp[-3(x+y)^2] 1_{6(x+y)^2 >= -t} dx dy`.       (3.1)

We optimize (3.1) over all probability densities `0<=f,g<=1`.

A simple extreme-point/bathtub step is valid here because the kernel is nonnegative and the functional is bilinear. For fixed `g`, a maximizer over `f` may be replaced by an indicator `1_E` with `|E|=1`; with that `E` fixed, `g` may likewise be replaced by `1_F`, `|F|=1`. Hence it is enough, for an upper bound, to optimize over measurable unit sets `E,F`.

## 4. Nonnegative output locations

For `t>=0`, the one-variable kernel

`k_t(s)=(1/2) exp(-t/2) exp(-3s^2)`

is nonnegative, even, and decreasing in `|s|`. Reflecting one of the two sets and applying the one-dimensional Riesz rearrangement inequality gives

`p_W(t) <= (1/2) exp(-t/2) int_{I} int_{I} exp[-3(x-y)^2] dx dy`

with `I=[-1/2,1/2]`. Since the difference of two centered unit intervals has triangular density `1-|u|` on `[-1,1]`,

`p_W(t) <= exp(-t/2) B_0 <= B_0`,                                      (4.1)

where

`B_0 := int_0^1 (1-u) exp(-3u^2) du`.                                  (4.2)

## 5. Negative output locations: exact rearrangement of the two-shell kernel

Let `t=-6a^2`, `a>0`. The kernel in (3.1) becomes

`k_a(s)=(1/2) exp[-3(s^2-a^2)] 1_{|s|>=a}`.                            (5.1)

This is not decreasing in `|s|`, so the preceding centered-kernel shortcut is unavailable. Its symmetric decreasing rearrangement, however, is explicit:

`k_a^*(u)=(1/2) exp[-3u^2-6a|u|]`.                                     (5.2)

Indeed, for `0<z<1/2`, set
`c=(1/3) log[(1/2)/z]`. The superlevel set `{s:k_a(s)>z}` is the union of the two intervals
`a<|s|<sqrt(a^2+c)`, so its total length is

`2(sqrt(a^2+c)-a)`.

The centered rearranged superlevel set therefore has radius
`r=sqrt(a^2+c)-a`, i.e.

`c=r^2+2ar`.

Solving back for `z` gives exactly (5.2).

Apply Riesz rearrangement to `1_E(x) 1_{-F}(y) k_a(x-y)`. Both unit sets rearrange to `I`, while the kernel rearranges to (5.2). Therefore

`p_W(-6a^2)`
` <= int_{-1}^1 (1-|u|) k_a^*(u) du`
` = int_0^1 (1-u) exp[-3u^2-6au] du`
` <= B_0`.                                                              (5.3)

The last inequality is strict for `a>0`.

Equations (4.1) and (5.3) prove the global-in-output-location estimate

`boxed( ||p_W||_infinity <= B_0 )`.                                    (5.4)

No centering, connected support, finite fragment count, or translation restriction was imposed on the two heavy laws.

## 6. Exact sharp constant in this limiting branch

For `f=g=1_{[-1/2,1/2]}` and `t=0`, every rearrangement step above is an equality, so (5.4) is sharp. Elementary integration gives

`B_0`
`= sqrt(pi)/(2 sqrt(3)) erf(sqrt(3)) - (1-exp(-3))/6`.

Since the physical limiting form is `Q_infty=W/12`, density scaling gives the exact sharp branch constant

`C_col`
`= 12 B_0`
`= 2 sqrt(3 pi) erf(sqrt(3)) - 2 + 2 exp(-3)`
`= 4.1516968595129935...`.                                             (6.1)

Thus

`boxed(C_col < 3 sqrt(2)=4.242640687119285... )`,                        (6.2)

with gap approximately

`0.090943827606292`.

This strictly improves the previous centered-interval control: it proves that the same value is the supremum over *all* cap-one heavy laws and *all* output locations in this saturated collinear minority-sign two-heavy Gaussian-completion branch.

## 7. What the partner theorem adds

For the centered-interval extremizer, the finite matrices `A_m` above are exact source-valid target matrices and `Q_m=>Q_infty`. The partner's interval-concentration lower-semicontinuity gives

`C_col = K(Q_infty) <= liminf_m K(Q_m)`.

So this limiting value is not merely a formal Gaussian relaxation: finite source-valid members asymptotically realize at least the same interval concentration.

The partner's invertible-matrix equivalence also means rank deficiency by itself cannot be used to discard such stress geometries in a sharp-constant proof: any lower concentration obstruction from a singular target can be transferred to invertible perturbations without reducing the optimal global constant. This statement is one-way for the present branch; no claim is made that the branch upper bound (6.1) survives an arbitrary invertible perturbation.

Because `C_col<3sqrt(2)`, this branch does not raise the known universal lower bound.

## 8. Consequence for the proof/witness search

This result is not a proof of the full conjecture and is not a proof that `3sqrt(2)` is universally sharp. It excludes one of the first mechanisms left open after the orthogonal two-heavy theorem and after the pointwise radial-Laplace correction:

> two arbitrary cap-one macroscopic laws loaded collinearly on the minority-sign direction, with the two majority-sign directions supplied by diffuse independent banks, cannot beat `3sqrt(2)` in the Gaussian-completion limit, even through fragmentation, translation, or an off-zero output peak.

A witness above `3sqrt(2)` must therefore use a feature absent here: genuinely non-collinear heavy rows spanning more than one spectral direction, unsaturated heavy leverage with a residual Gaussian component in that direction, three or more interacting heavy rows, a finite/mesoscopic overshoot that disappears in the Gaussian-completion limit, additional spectral directions, or a different coupled off-zero geometry.

The full QFORM target remains `OPEN / NOT PROVED`.

## 9. Verification status

The accompanying deterministic checker evaluates (6.1), checks the strict gap to `3sqrt(2)`, and numerically verifies the monotonic family in (5.3) at representative `a`. Those computations are sanity checks only. The theorem is the analytic rearrangement argument above.
