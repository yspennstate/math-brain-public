# account01/B14 — translation-free closure from a definite physical 2x2 pivot

Status: **PROVED SUPPORTING THEOREM / ESSENTIAL_STEP_APPLIED / FULL QFORM TARGET OPEN**

Programme: `QFORM-DENSITY-3EIG-20260922`, owner-control revision `2026-09-22.5`.
Run: `20260922T120931Z-account01-B14-qform`.
Execution context: `WITHOUT_VERIFIED_BRAIN`.

## 1. Current target and correction-aware scope

The active owner control supersedes the older FEI order. The target is: for every finite `n`, independent real `X_i` with densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of magnitude at least `1`, prove that `Q=X^T A X` has an essentially bounded density with one universal constant.

This report does not use the refuted law-uniform pointwise Fresnel decay, does not diagonalize `A` and then assume independence, and does not use a fiberwise spectral supremum. The fresh correction `QFORM-CROSSMINOR-ALONE-FALSE` is also respected: a nonsingular cross block by itself is not used. The pivot below is an actual **definite principal** `2x2` block.

## 2. Partner result actually consumed

I use account02/B14's immutable localization theorem:

- repository/commit: `yspennstate/math-open-problems@ea6b7ae2aba8b38748214a4d38f47fa6f790b8e0`
- path: `proofnet24/QFORM-density/fleet-2026-09-22/account02/B14/20260922T120110Z-b14-qform-localization-r13/REPORT.md`.

It proves losslessly that the full small-ball target can be reduced to independent indicator densities `1_{E_i}` with every `E_i` a finite union of bounded intervals of total length exactly `1`, and then lifted back to arbitrary supports with the **same** constant. The theorem below is proved first on that exact reduced class and then lifted by the partner theorem. (A direct conditional-density proof gives the same extension.)

## 3. New theorem: definite physical-pair closure, uniform in all translations and fragments

### Theorem `QFORM-DEFINITE-PRINCIPAL-PAIR-v1`

Let `A` be any real symmetric `n x n` matrix. Suppose there are two original coordinate indices `i != j` such that the principal block

`B = A[{i,j},{i,j}]`

is positive definite or negative definite. Put

`Delta = det B > 0`.

Let `X_1,...,X_n` be independent with arbitrary probability densities satisfying `0<=f_k<=1`. Then `Q=X^TAX` has an essentially bounded density and

`boxed{ ||p_Q||_infinity <= pi / sqrt(Delta). }`

The bound is independent of `n`, all other entries/eigenvalues of `A`, the support locations, support diameters, number of fragments, and every translation-generated linear term.

Equivalently, for every bounded interval `I`,

`boxed{ P(Q in I) <= (pi/sqrt(Delta)) |I|. }`

### Proof

By the account02/B14 bang-bang/compactification theorem it is enough to prove the interval estimate for product indicator laws `f_k=1_{E_k}`, where each `E_k` is a finite union of bounded intervals and `|E_k|=1`.

Fix all coordinates except `x_i,x_j`; denote the frozen vector by `z`. The quadratic form becomes an affine quadratic polynomial in the two active physical coordinates `u=(x_i,x_j)^T`:

`Q(u,z) = u^T B u + ell(z)^T u + c(z)`

for some vector `ell(z)` and scalar `c(z)`. No restriction on `ell(z)` is imposed; in particular it contains every shift and every coupling to the frozen coordinates.

Assume first that `B` is positive definite. Completing the square,

`u^T B u + ell^T u + c = (u-u_0)^T B (u-u_0) + c_0`,

where `u_0=-(1/2)B^{-1}ell`. Set `v=B^{1/2}(u-u_0)`. The Jacobian is

`du = Delta^{-1/2} dv`.

For an interval `I=[a,b]`, `|I|=b-a`, the full-plane level strip satisfies

`|{u in R^2 : Q(u,z) in I}|
 = Delta^{-1/2} |{v in R^2 : |v|^2 in I-c_0}|`.

The set on the right is an annulus, a disk, or empty. Its area is exactly

`pi * length((I-c_0) intersect [0,infinity)) <= pi |I|`.

Therefore

`|{u in E_i x E_j : Q(u,z) in I}|
 <= pi |I| / sqrt(Delta)`

for every frozen `z`, with no support/location term.

If `B` is negative definite, apply the same argument to `-B` and `-Q`; `det(-B)=det B=Delta`, so the identical estimate holds.

Now integrate in the remaining coordinates. Since every `|E_k|=1`, Fubini gives

`|{x in prod_k E_k : Q(x) in I}|
 <= pi |I| / sqrt(Delta)`.

The account02/B14 reduction then lifts this finite-union estimate to all independent densities `0<=f_k<=1`, including arbitrary unbounded supports, with no loss in the constant. The interval small-ball characterization yields an essentially bounded density satisfying the claimed cap. QED.

## 4. Why this is a localization theorem rather than a diagonal special case

The two active coordinates may remain strongly coupled to all other coordinates. Conditioning merely turns those couplings into the arbitrary vector `ell(z)`. The shell-area computation is exactly translation invariant after completing the square, so neither distant support fragments nor large conditional linear terms cost anything.

The theorem therefore covers matrices far beyond diagonal forms. It also survives arbitrary additional small or large eigenvalues and arbitrary off-block couplings: they are frozen into `ell(z),c(z)` and never enter the constant.

The exact constant `pi/sqrt(det B)` is the same beta/annulus constant that appears in the two same-sign diagonal-square control, but here it is attached to a genuine physical principal block and is uniform over all conditional translations.

## 5. Interaction with the current cross-minor correction

The fresh event `QFORM-CROSSMINOR-ALONE-FALSE` gives the control example

`(X1+Y1)^2-(X2+Y2)^2`,

whose nonsingular cross block does **not** force a bounded density. That does not conflict with the theorem here: its relevant two-coordinate principal pivots are indefinite/degenerate, not definite. The positivity/negativity of the principal block is the exact geometric input that makes the global two-dimensional shell area finite.

## 6. Exact structural consequence and remaining gap

Define

`Delta_+(A) = max_{i<j : A[{i,j}] definite} det A[{i,j}]`,

with value `0` if no definite principal pair exists. Then whenever `Delta_+(A)>0`,

`||p_Q||_infinity <= pi / sqrt(Delta_+(A)).`

In particular, any target matrix satisfying the owner hypotheses and `Delta_+(A)>=delta` is closed with universal cap `pi/sqrt(delta)`.

This does **not** finish the owner target because three large spectral eigenvalues do not force a dimension-free lower bound on a definite physical principal minor. For example, matrices of signature `(2,1)` can have every `2x2` coordinate principal block indefinite (the signed complete-graph example is a basic warning). Diffuse rank-three matrices can also have all fixed coordinate minors small.

The first unpaid implication after this B14 result is therefore a clean dichotomy/aggregation problem:

> prove that every target matrix either has a definite physical pair with determinant bounded below by a universal constant, or belongs to a complementary heavy/diffuse/hyperbolic regime already controlled by one of the global mechanisms; alternatively prove a weighted aggregation that uses many small definite principal pairs without paying the reciprocal determinant before summation.

The present theorem supplies the translation- and fragment-free closure branch whenever such a pivot exists.

## 7. Status and integrity

Classification: `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_THEOREM`.
Full conjecture: `OPEN`.

Dependencies actually used:
1. current owner target/control revision `2026-09-22.5`;
2. account02/B14 immutable localization theorem at commit `ea6b7ae2aba8b38748214a4d38f47fa6f790b8e0`;
3. fresh correction `QFORM-CROSSMINOR-ALONE-FALSE` from account02/B09, used to delimit the pivot hypothesis.

No pointwise oscillatory-decay claim, rotated-coordinate independence, moment bound, support-radius bound, fragment-count bound, email, remote workflow, paid model/API, public release, or permission change is used.
