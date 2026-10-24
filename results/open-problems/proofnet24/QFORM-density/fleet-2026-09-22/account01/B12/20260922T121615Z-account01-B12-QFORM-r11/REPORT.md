# account01/B12 — 20% one-exception stability and arbitrary completion

**Run:** `20260922T121615Z-account01-B12-QFORM-r11`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner-control revision `2026-09-22.5`  
**Assignment:** `Additional eigenvalue control`  
**Classification:** `PROVED_SUPPORTING_THEOREM / TARGET_LEVEL_LOCAL_CRITERION / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; authenticated repository retrieval was used, but no native learned-memory receiver/context ingestion was verified.  
**Full conjecture:** **OPEN / NOT PROVED.**

## 1. Live target and corrections consumed

The active target is: for every dimension `n`, every independent real `X_i` with probability densities bounded by `1`, and every real symmetric `A` with at least three eigenvalues of modulus at least `1`, prove a universal finite bound on the density of `X^T A X`, or produce a valid counterexample.

Fresh control supersedes the scheduled FEI wording. The live correction inbox contains, in particular:

* `QFORM-CROSSMINOR-ALONE-FALSE`: a nonsingular rank-two cross block alone is insufficient;
* `QFORM-UNIVERSAL-PI-FALSE-AND-DIFFUSE-BRANCH`: the diagonal constant `pi` is not universal; the rank-exactly-three diffuse branch has a separate bound `24` under a leverage hypothesis.

Neither corrected claim is used below. The argument is entirely in original independent coordinates and uses principal blocks plus conditioning.

## 2. Exact partner result consumed and applied

The assigned partner `account02/B12` proved in

`yspennstate/math-open-problems@ffbe643d91659c040e06f33eb688b2d0ad5f0d50`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B12/20260922T115433Z-account02-B12/REPORT.md`

that a four-variable matrix of the form

`epsilon*lambda*I_4 + (mu-epsilon*lambda) vv^T`

has a density cap below `24.193/lambda`, uniformly in the exceptional eigenvalue and orientation. That report also gave a `1%` perturbative theorem. Its proof uses the source theorem

`yspennstate/math-open-problems@289810e1f075755898f573ee5b863ad3fa9af5b8`

`qform/fleet-2026-09-22/account02/B15/20260922T110507Z-account02-B15-qform-pivot-r1/REPORT.md`,

which establishes, uniformly over arbitrary linear tilts:

1. if a `2 x 2` principal block `C` is positive or negative definite, then the affine quadratic output density is at most `pi/sqrt(|det C|)`;
2. if a symmetric `3 x 3` principal block `C` has `sigma_min(C)>=kappa>0`, then the affine quadratic output density is at most

`C3/kappa`, where `C3 = 2*pi + 3*sqrt(3)`.

I apply those exact two source estimates below. The new step is to optimize the pair/triple switch and prove stability all the way up to every relative perturbation `delta<1/5`, not merely `1%`.

## 3. Arbitrary-completion monotonicity

### Lemma 3.1 — `QFORM-PRINCIPAL-BLOCK-COMPLETION-v1`

Let `J` be a set of original coordinates. Suppose a symmetric principal block `B=A[J,J]` has the following property: for every choice of independent variables `(X_j)_{j in J}` with one-dimensional density caps `1`, every linear tilt `ell`, and every scalar `c`,

`X_J^T B X_J + ell^T X_J + c`

has density norm at most `M`.

Then for **every** symmetric completion of that same principal block to an `n x n` matrix `A`—with arbitrary entries on `J x J^c` and `J^c x J^c`, hence arbitrary extra eigenvalues of either sign and arbitrary size—the full quadratic form `X^T A X` has density norm at most `M`.

#### Proof

Condition on all original independent coordinates in `J^c`. For each fixed outside value, the conditional polynomial in `X_J` is

`X_J^T B X_J + ell(w)^T X_J + c(w)`.

The variables in `J` remain independent with the same density caps. By hypothesis every conditional output density is bounded by `M`, uniformly in `w`. Averaging the conditional densities preserves the same cap. QED.

This is the valid replacement for any false claim that added spectral terms become an independent convolution after diagonalizing `A`: they need not. What is true is that arbitrary **matrix completion outside a certified original-coordinate principal block** only creates linear tilts after conditioning.

## 4. A rank-one-exception block is stable up to every `delta<1/5`

Put

`C3 = 2*pi + 3*sqrt(3)`.

For `0<=delta<1/5`, define

`eps = 1 - 5*delta`,

`A_delta = pi/sqrt(1-delta)`,

`D_delta = sqrt(C3^2 + 3*A_delta^2*eps)`,

and

`C_delta = (C3 + D_delta)/eps`.

### Theorem 4.1 — `QFORM-ONE-EXCEPTION-20PCT-STABILITY-v1`

Let `Y_1,...,Y_4` be independent real variables with densities bounded by `1`. Let `lambda>0`, `epsilon in {+1,-1}`, `v in S^3`, `s in R`, and let `E` be any real symmetric `4 x 4` matrix satisfying

`||E||_op <= delta*lambda`, with `0<=delta<1/5`.

Set

`B = epsilon*lambda*I_4 + s vv^T + E`.

Then for every linear tilt `ell` and scalar `c`,

`T = Y^T B Y + ell^T Y + c`

has an essentially bounded density satisfying

`||p_T||_infinity <= C_delta/lambda`.

No alignment condition on `v` is imposed, `s` is arbitrary, and `E` need not annihilate `v`.

#### Proof

Reflect the scalar output if necessary and divide by `lambda`. It is enough to treat

`B = -I_4 + s vv^T + E`, `||E||_op<=delta`.

Relabel the original coordinates so that

`w_i=v_i^2`, `w_1<=w_2<=w_3<=w_4`, `sum w_i=1`.

Put

`a=w_1+w_2`, `b=1-w_1`.

If `a>0`, then

`a<=1/2` and `b/a>=3/2`.

Indeed `w_3+w_4>=2w_2>=w_1+w_2=a`, so `a<=1/2`; also `w_1<=a/2`, hence `b/a=(1-w_1)/a>=1/a-1/2>=3/2`.

Choose the switch optimally as follows. Let

`x = ((D_delta-C3)/(3*A_delta))^2`

and

`theta = 1-delta-x`.

The positive root defining `x` is equivalent to

`(3/2) A_delta x + C3 sqrt(x) - (1/2)A_delta eps = 0`.

Equivalently,

`A_delta/sqrt(x) = C3 / (eps/2 - 3x/2) = C_delta`.

Moreover `0<x<eps/3`, so

`gamma := eps/2 - 3x/2 >0`

and `theta` lies strictly between `(2/3)(1+delta)` and `1-delta`.

If `a=0`, then the rank-one perturbation vanishes on coordinates `{1,2}`. The corresponding pair equals `-I_2+E_{12}` and is negative definite with eigenvalue magnitudes at least `1-delta`, so the pair theorem already gives a cap no larger than the stated one. Hence assume `a>0`.

### Pair branch

Suppose

`s a <= theta`.

On coordinates `{1,2}`, the unperturbed matrix `-I_2+s v_{12}v_{12}^T` has eigenvalues `-1` and `-1+s a`. Since `sa<=theta<1`, it is negative definite. After adding `E_{12}`, Weyl's inequality gives two negative eigenvalues with magnitudes at least

`1-delta`

and

`1-theta-delta = x`.

Thus

`|det B_{12}| >= (1-delta)x`.

The exact definite-pair theorem yields

`||p_T||_infinity <= pi/sqrt((1-delta)x) = A_delta/sqrt(x) = C_delta`.

### Triple branch

Suppose instead

`s a > theta`.

Then `s>0`, and for the triple `{2,3,4}` the exceptional-vector mass is `b`. Since `b/a>=3/2`,

`s b > (3/2) theta`.

The base triple `-I_3+s v_{234}v_{234}^T` has eigenvalues

`-1, -1, -1+s b`.

Its positive eigenvalue is larger than `(3/2)theta-1`. After adding `E_{234}`, whose operator norm is at most `delta`, the smallest singular value is at least

`(3/2)theta - 1 - delta`.

Using `theta=1-delta-x`, this equals

`eps/2 - 3x/2 = gamma>0`.

(The other two eigenvalues stay at distance at least `1-delta` from zero, which is larger than `gamma`.)

The exact principal-triple theorem therefore gives

`||p_T||_infinity <= C3/gamma = C_delta`.

The two branches cover all real `s`. Restoring the output scale gives the factor `1/lambda`. QED.

## 5. Equivalent spectral-cluster statement

### Corollary 5.1 — `QFORM-THREE-EIGENVALUES-20PCT-CLUSTER-v1`

Let `B` be a real symmetric `4 x 4` matrix. Suppose that for some `lambda>0`, sign `epsilon`, and `0<=delta<1/5`, three eigenvalues of `B` satisfy

`|beta_j-epsilon*lambda| <= delta*lambda`, `j=1,2,3`,

while the fourth eigenvalue is completely arbitrary.

Then every affine quadratic form built from `B` and four independent density-`<=1` variables has density norm at most

`C_delta/lambda`.

#### Proof

Let `v` be a unit eigenvector for the arbitrary fourth eigenvalue. In an orthonormal eigenbasis define the rank-one-exception model `epsilon*lambda I_4+s vv^T` to match that fourth eigenvalue exactly, and put the three cluster errors into `E`. Then `||E||_op<=delta*lambda`; Theorem 4.1 applies. QED.

Numerically,

* `C_0 = 24.1830382899...`, slightly sharpening the partner's `<24.193` exact-cluster constant;
* `C_0.01 = 25.4061740874...`, improving the partner's `<26.697` one-percent stability constant;
* `C_0.10 = 47.3081752809...`;
* the theorem remains finite for every `delta<0.2` and necessarily blows up in this particular two-branch estimate as `delta` approaches `0.2`.

The `1/5` threshold is a sufficiency threshold for this pair/triple/Weyl mechanism, not a counterexample beyond `1/5`.

## 6. High-dimensional arbitrary-completion consequences

### Corollary 6.1 — local principal-block criterion

Let `A` be any real symmetric `n x n` matrix. If **one** four-coordinate principal block `A[J,J]` satisfies Theorem 4.1 (or Corollary 5.1) with parameters `lambda,delta`, then for arbitrary independent input densities bounded by `1`,

`||p_{X^T A X}||_infinity <= C_delta/lambda`.

All entries of `A` outside `J x J` are unrestricted. Consequently the full matrix may have arbitrarily many additional eigenvalues, of arbitrary sign and magnitude, and arbitrary cross-couplings to the certified coordinates. This follows directly from Lemma 3.1 and does **not** assert that the outside spectral contribution is independent.

### Corollary 6.2 — global codimension-one cluster

Suppose `n>=4` and `A` has `n-1` eigenvalues in the interval

`[epsilon*lambda-delta*lambda, epsilon*lambda+delta*lambda]`

with `0<=delta<1/5`, while one exceptional eigenvalue is arbitrary. Then

`||p_{X^T A X}||_infinity <= C_delta/lambda`.

Indeed globally

`A = epsilon*lambda I_n + s vv^T + E`, `||E||_op<=delta*lambda`,

for a unit exceptional eigenvector `v`. Restricting to any four original coordinates gives exactly the block hypothesis of Theorem 4.1; condition on the rest.

This is the precise sense in which an arbitrary extra eigenvalue and arbitrary matrix completion are controlled without invoking a false rotated-coordinate convolution.

## 7. What changed and what remains open

**Mathematical change.** The partner's arbitrary-orientation one-exception theorem is now quantitatively stable under every operator-norm perturbation of relative size `delta<1/5`, with an explicit optimized constant. The previous proven perturbative radius in the consumed B12 partner report was `1%`. The new principal-block completion lemma also makes explicit that once such a block exists, every additional outside eigenvalue/cross coupling is harmless by conditioning.

**Full target status.** Still **OPEN**. The target hypothesis of merely three eigenvalues with modulus at least `1` does not imply the existence of a fixed four-coordinate block satisfying the cluster condition. Delocalized rank-three projectors are an explicit obstruction to all bounded-size fixed-principal-block extraction arguments. The remaining universal bridge must aggregate many weak coordinate interactions, or otherwise exploit the product structure without selecting one uniformly strong local block.

**Next useful implication.** Combine the now-broad local stability theorem with an aggregate/diffuse mechanism: prove that every matrix with three large spectral directions either has a principal block in the `delta<1/5` one-exception basin, or admits a product-preserving cross-block/partition estimate of the type already proved for diffuse rank-three frames. That dichotomy would be genuinely closer to the full theorem; it is not established here.

## 8. Provenance

Fresh coherent protected-control snapshot before the mathematical write: `yspennstate/math-research-brain@b2072e8df9e1777df5a215ae7afd8c79ac06d3eb`, OWNER CONTROL revision `2026-09-22.5`.

Corrections consumed at that snapshot: `QFORM-CROSSMINOR-ALONE-FALSE` and `QFORM-UNIVERSAL-PI-FALSE-AND-DIFFUSE-BRANCH`.

Primary partner dependency: `yspennstate/math-open-problems@ffbe643d91659c040e06f33eb688b2d0ad5f0d50:proofnet24/QFORM-density/fleet-2026-09-22/account02/B12/20260922T115433Z-account02-B12/REPORT.md`.

Underlying pair/triple dependency: `yspennstate/math-open-problems@289810e1f075755898f573ee5b863ad3fa9af5b8:qform/fleet-2026-09-22/account02/B15/20260922T110507Z-account02-B15-qform-pivot-r1/REPORT.md`.

No public release, external paid computation, new permissions, or scheduler mutation is part of this result.
