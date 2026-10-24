SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B04, 2026-09-22T23:54:08Z.
attacking: the rank-one clean-bank endpoint by triangular product rearrangement, then an overlap-safe scalar-square splice and an explicit diffuse rotated indefinite family.

# account03/B04 r21 — triangular rank-one bank rearrangement and sharpened zero-Schur endpoint

Programme `QFORM-DENSITY-3EIG-20260922`; assignment `Product Fourier rearrangement`; run `B04-20260922T235408Z-r21`. Execution `WITHOUT_VERIFIED_BRAIN`. Outcome `ESSENTIAL_STEP_APPLIED / SUPPORTING THEOREMS PROVED / FULL QFORM OPEN`.

## 1. Scope and source-pinned inputs

All coordinates below are original independent real coordinates whose one-dimensional probability densities are bounded by one. No moment, centering, Gaussian, compact-support, connected-support, log-concavity, post-rotation independence, arbitrary-joint coarea, conditional projection moment, or law-uniform pointwise quadratic-phase decay is used.

This run changes mechanism from r20. The previous theorem kept at least two cross singular directions jointly and used a multidimensional inverse-radius rearrangement. Here I treat the missing **rank-one** clean-bank endpoint by a nested one-dimensional decreasing rearrangement. One bank may carry arbitrary quadratic leakage; the other is required to enter only through one linear bank projection.

Completed peer result actually applied:

- account02/B04 scalar bank-projection theorem, `yspennstate/math-open-problems@07305f53ba9b8a1d3e6e79f8c851f415f007d4a7`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B04/B04-20260922T181702Z-dac07509/REPORT.md`:

`||p_(c^T X)||_infinity <= sqrt(2)/||c||_2`                                    (1.1)

for every nonzero coefficient vector `c` and an original-coordinate cap-one product vector.

For comparison, account01/B06 `yspennstate/math-open-problems@b74210c7e963a11c1f0532f98f5d705278967cd1`, path `proofnet24/QFORM-density/fleet-2026-09-22/account01/B06/20260922T190509Z-qform-r14-b06/REPORT.md`, proved the exact-zero Schur-row half-Riesz endpoint with constant `4 sqrt(2)e^(1/4)`. Section 5 below sharpens that constant by inserting (1.1).

The designated account04/B04 worker had a current-hour sign-in, but no completed current-QFORM handoff/report was present at the final pre-publication lookup. No designated-partner result is fabricated.

## 2. Fractional bathtub lemma

### Lemma 2.1

Let `S` be a real random variable with probability density bounded by `M<infinity`. For every `0<alpha<1`,

`sup_t E |S-t|^(-alpha) <= [2^alpha/(1-alpha)] M^alpha`.                       (2.1)

In particular,

`sup_t E |S-t|^(-1/2) <= 2 sqrt(2M)`.                                         (2.2)

### Proof

For fixed `t`, the kernel `|s-t|^-alpha` is symmetric decreasing about `t`. The bathtub/rearrangement principle maximizes its integral over all probability densities bounded by `M` by filling the interval of length `1/M` centered at `t` at height `M`. Therefore, with `R=1/(2M)`,

`E|S-t|^-alpha <= 2M integral_0^R x^-alpha dx`
` = 2M R^(1-alpha)/(1-alpha)`
` = 2^alpha M^alpha/(1-alpha)`.                                               (2.3)

This proves (2.1), and `alpha=1/2` gives (2.2). QED.

## 3. Triangular rank-one bank half-Riesz theorem

Let `I,J,K` be disjoint original-coordinate sets. Put

`U=u^T X_I`, `V=v^T X_J`,                                                     (3.1)

where `u,v` are nonzero. Let `W=X_K`. Assume only that `U` is independent of `(V,W)`, as follows from the disjoint original-coordinate banks. Let `beta(W)` be arbitrary measurable and let `H(V,W)` be arbitrary measurable; in QFORM applications `H` may contain all self-quadratic terms on the `J` bank, all quadratic terms on `W`, and their mutual couplings.

For `c!=0`, define

`T = 2c U [V+beta(W)] + H(V,W)`.                                               (3.2)

### Theorem 3.1 — `QFORM-RANK1-TRIANGULAR-HALFRIESZ-v1`

If `U,V` have density caps `M_U,M_V`, then

`sup_t E|t-T|^(-1/2) <= 4 sqrt(2 M_U M_V/|c|)`.                               (3.3)

Using (1.1), if `U,V` are the bank projections in (3.1), the rank-one physical cross block `B=cuv^T` has sole singular value

`sigma=|c| ||u||_2 ||v||_2`,                                                   (3.4)

and

`boxed: sup_t E|t-T|^(-1/2) <= 8/sqrt(sigma).`                                (3.5)

### Proof

Fix `(V,W)=(v0,w)`. Except on the null event `v0+beta(w)=0`, the variable `T` is affine in `U` with slope

`k=2c(v0+beta(w))`.                                                            (3.6)

The density of `kU` is bounded by `M_U/|k|`; translation by `H(v0,w)` is irrelevant. Lemma 2.1 therefore gives

`E_U |t-T|^-1/2 <= 2 sqrt(2 M_U/|k|)`
` = 2 sqrt(M_U/|c|) |v0+beta(w)|^-1/2.                                        (3.7)

For fixed `w`, apply Lemma 2.1 again to `V`, whose density is bounded by `M_V`:

`E_V |V+beta(w)|^-1/2 <= 2 sqrt(2M_V).`                                       (3.8)

Averaging (3.7) proves (3.3). The exceptional coefficient-zero set has probability zero because `V` is absolutely continuous. Finally (1.1) gives

`M_U M_V <= 2/(||u||_2||v||_2)`,                                              (3.9)

which turns (3.3) into (3.5). QED.

**Why this is not contradicted by the two-sided leakage correction.** The clean bank `I` carries no additional quadratic dependence in (3.2). Arbitrary quadratic leakage is permitted on the coefficient-side bank `J` through `H(V,W)`. If both sides carry arbitrary quadratic leakage, the rank-one packet can collapse to a square and a standalone half-Riesz bound can diverge; no such extension is claimed.

## 4. Overlap-safe outer square

Let `Z` be one additional original coordinate, independent of `(X_I,X_J,W)`, with density bounded by one. Let `a!=0`, and let `m=m(U,V,W)` be arbitrary measurable; in particular the completed-square translation may reuse both active banks. Set

`Q = a[Z+m(U,V,W)]^2 + T`.                                                     (4.1)

### Theorem 4.1 — `QFORM-SQUARE-RANK1-TRIANGULAR-BANK-v1`

Under the hypotheses of Theorem 3.1,

`boxed: ||p_Q||_infinity <= 8 / sqrt(|a| sigma).`                              (4.2)

The law of `Q` is absolutely continuous. This branch proves essential boundedness; it does not prove that an arbitrary measurable-input density has a continuous representative.

### Proof

For fixed residual variables, the translated scalar square `a(Z+m)^2` has density bounded by

`|a|^-1/2 |s|^-1/2`                                                           (4.3)

on its supported half-line; removing the support indicator only enlarges the bound. Hence, for a.e. `t`,

`p_Q(t) <= |a|^-1/2 E|t-T|^-1/2.                                              (4.4)

Apply (3.5). Mixtures of the a.e. absolutely continuous conditional square laws are absolutely continuous. QED.

This complements r20 exactly at cross rank one: r20 paid every quadratically-clean cross bank of rank at least two by a multidimensional inverse-radius rearrangement; Theorem 4.1 pays rank one after one independent scalar square, while allowing arbitrary coefficient-side quadratic leakage.

## 5. Sharpened exact-zero physical Schur endpoint

The same nested rearrangement improves the completed exact-zero theorem of account01/B06.

Let `S=S^T` be any real residual matrix, choose a physical coordinate `i` with

`S_ii=0`, `beta_i=(sum_{j!=i} S_ij^2)^(1/2)>0`,                               (5.1)

and allow an arbitrary affine perturbation. Write

`X^T S X+b^T X+c-t = 2X_i d^T Y + H(Y)`,                                     (5.2)

where `||d||_2=beta_i` and `Y` is the other original-coordinate product vector. Here the clean scalar `X_i` has density cap exactly one, while by (1.1)

`||p_(d^T Y)||_infinity <= sqrt(2)/beta_i`.                                   (5.3)

The proof of Theorem 3.1 with `M_U=1`, `M_V=sqrt(2)/beta_i`, `c=1` gives

`boxed:
 sup_t E|X^T S X+b^T X+c-t|^-1/2
 <= 2^(11/4) beta_i^-1/2`,                                                    (5.4)

where

`2^(11/4)=6.727171322029716...`.                                              (5.5)

Thus if an outer original-coordinate pivot `a!=0` is completed and its Schur complement has such an exact-zero row,

`boxed:
 ||p_Q||_infinity <= 2^(11/4)|a|^-1/2 beta_i^-1/2.`                           (5.6)

This improves `4 sqrt(2)e^(1/4)=7.26...` from account01/B06. It remains an **exact-zero** result. The live correction `QFORM-NEAR-ZERO-HALF-RIESZ-ONLY-FALSE-v1` forbids extending (5.6) to a merely small nonzero diagonal using only `beta_i`, and this report makes no such claim.

## 6. Explicit genuinely rotated indefinite target family

For every `m>=2`, split original coordinates into one scalar `Z` and two disjoint `m`-coordinate banks `x,y`. Let

`u=v=m^(-1/2)(1,...,1)`, `U=u^T x`, `V=v^T y`,                               (6.1)

and define

`Q_m = Z^2 + 4UV + V^2`.                                                       (6.2)

On the active orthonormal span `(Z,U,V)`, the matrix is

`A_act = [[1,0,0],[0,0,2],[0,2,1]]`.                                         (6.3)

Its characteristic polynomial is

`(lambda-1)(lambda^2-lambda-4)`,                                              (6.4)

so its three nonzero eigenvalues are

`1, (1+sqrt(17))/2, (1-sqrt(17))/2`,                                         (6.5)

whose absolute values are `1, 2.5615528128..., 1.5615528128...`. Thus the exact target spectral hypothesis is met.

In physical original coordinates, every `x-y` cross-block entry is `2/m` and every `y-y` entry from `V^2` is `1/m`; the form is nonseparable and indefinite, and its local coefficients vanish as `m` grows. The cross block is

`B=2uv^T`,                                                                    (6.6)

with sole singular value `sigma=2`. The `x` bank is quadratically clean, while the `y` bank carries the nonzero same-side curvature `V^2`. Theorem 4.1 with `a=1` yields, for **every** admissible choice of the independent coordinate laws and every `m>=2`,

`boxed: ||p_(Q_m)||_infinity <= 8/sqrt(2)=4sqrt(2)=5.656854249492381...`.      (6.7)

This is a genuinely rotated indefinite target family controlled at aggregate bank scale even though every individual active physical coefficient tends to zero.

## 7. What is paid and what remains

New paid endpoint:

- one outer independent scalar square + one **rank-one** quadratically clean cross bank is now controlled with constant `8/sqrt(|a|sigma)`, allowing arbitrary quadratic contamination on the coefficient-side bank and arbitrary overlap of the square translation;
- the exact-zero Schur-row half-Riesz constant improves to `2^(11/4)` using the completed scalar bank-projection theorem.

Together with r20, every clean cross-bank rank `>=1` has a product-rearrangement endpoint after a usable outer scalar square. What is **not** paid is the structural implication from bare `s_3(A)>=1` to such a usable clean packet. Genuine quadratic leakage on both sides, or a small but nonzero near-isotropic Schur diagonal, still requires a different mechanism; the correction examples show why simply discarding that leakage or taking a continuity limit is invalid.

Next exact debt:

`QFORM-CLEAN-BLOCK-OR-TWOSIDED-LEAKAGE-ROUTING-v1`: starting from an arbitrary unresolved three-large-eigenvalue matrix, either expose a quantitatively usable scalar-square plus clean cross bank (rank one now included), or route the two-sided-leakage/near-isotropic residual into an already-paid ridge, determinant, rank-two affine, or grouped-bank branch without inverting a vanishing physical coefficient.

Full QFORM remains OPEN. No target counterexample is produced here. Continuity for the full target remains OPEN.
