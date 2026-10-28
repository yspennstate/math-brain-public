SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B10, 2026-09-22T23:18:27Z.
attacking: exact-rank-three hybrid/near-null physical direction; consume the ruled-side theorem and close a source-valid rank-two-bank/rank-one-null-ray packet before any reciprocal local minor.

# account03/B10 r21 — rank-two-bank/null-ray packet payment and heavy-core reduction

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Rank-three coupled case  
**Pre-publication refresh:** `yspennstate/math-research-brain@fca399c04de1ea2962bb05063894b810b1201803`, same owner revision  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Status:** supporting target-level branch proved; full QFORM remains `OPEN / NOT PROVED`.

## 1. Exact inherited state and correction boundary

The target remains the universal essential-density bound for `Q=X^T A X` under independent original coordinates with densities at most one and at least three eigenvalues of `A` having modulus at least one. No Gaussianity, moments, log-concavity, bounded support, connected support, or post-rotation independence is used below.

The live correction inbox was reread at the pre-publication control head. In particular, this argument does **not** use: law-uniform pointwise quadratic van-der-Corput decay; arbitrary-joint rank-three coarea; positive conditional projection-height moments; a worst fiber supremum; a single well-conditioned physical minor; or coefficient-smallness as a perturbative error.

The immediate B10 source is r20,

`yspennstate/math-open-problems@7acd371ee2ee83a7fae12d7bedb38bc99c051b6d`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B10/20260922T221548Z-account03-B10-QFORM-r20/REPORT.md`.

It produced three disjoint original-coordinate banks with tripartite exterior mass `T>=1/256`, a selected Gram core `G>=I_3/256`, and a whitened exact-rank-three matrix with determinant magnitude and least singular value at least `1/512`. The diffuse normalized-leverage branch is already paid by `96`, and the exact three-rank-one-bank endpoint is already paid by `<2200.567`. Thus the surviving chamber contains a genuine physical hub and genuine internal transverse geometry.

The newest rough geometric result actually consumed in this run is account04/B13,

`yspennstate/math-open-problems@574213e45f285d822893bea637ba6a5bc46a22b6`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B13/20260922T231352Z-account04-B13-rough-geometric-transfer-r5/REPORT.md`.

It proves the exact product-purification identity for bounded slab functionals and the rough one-sheet rank-three interval estimate. The exact designated partner `account04/B10` still had no completed current-QFORM artifact at the fresh lookup, so no result is attributed to it; the completed compatible account04/B13 theorem is applied below to an actual slab inequality.

A second completed input is account01/B13,

`yspennstate/math-open-problems@680ff828e47704689fde0ca4b1690860a9cbd71f`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B13/20260922T222028Z-account01-B13-qform-auto11/REPORT.md`.

Its affine zero-pivot `1+2` theorem says: if a cap-one scalar is independent of a two-dimensional vector with joint density cap `M_2`, and a nonsingular symmetric active matrix has zero scalar pivot, then arbitrary affine perturbations have a **continuous** density bounded by

`6 M_2^(2/3) |det H|^(-1/3)`.                                      (1.1)

The product-projection bounds used below are the already-proved two-dimensional cap `2/sqrt(det H_B)` and one-dimensional cap `sqrt(2)/||a||_2` for linear images of independent cap-one coordinates.

## 2. Exact packet identity for a rank-two bank and a rank-one bank

Write an exact-rank-three form in spectral-frame notation

`A=R M R^T`, `R^T R=I_3`, `D=|det M|>0`,                         (2.1)

and denote the physical spectral row for coordinate `j` by `r_j in R^3`.

Let `B,C` be disjoint original-coordinate banks satisfying:

1. all rows in `B` lie in one two-dimensional plane `E`, and their Gram on that plane is positive definite,

   `H_B := sum_(i in B) r_i r_i^T |_E`, `h:=det_E(H_B)>0`;       (2.2)

2. all rows in `C` lie on one unit ray `r`,

   `r_k=alpha_k r`, `m:=sum_(k in C) alpha_k^2>0`;              (2.3)

3. `r` is transverse to `E`, with

   `delta:=dist(r,E)^2>0`.                                      (2.4)

Define the `2+1` spectral exterior packet

`T_(B,B;C)
 := sum_(i<j in B, k in C) det(r_i,r_j,r_k)^2`.                 (2.5)

### Lemma 2.1 — `QFORM-RANK2-RANK1-PACKET-IDENTITY-v1`

`boxed: T_(B,B;C)=m h delta.`                                   (2.6)

#### Proof

Choose an oriented orthonormal basis `(e_1,e_2)` for `E` and a unit normal `n`. For `i in B`, write `r_i=x_i e_1+y_i e_2`. Cauchy-Binet in the two-dimensional coefficient matrix gives

`sum_(i<j in B) det_E(r_i,r_j)^2 = det_E H_B = h`.              (2.7)

For `k in C`, `r_k=alpha_k r`, and

`det(r_i,r_j,r_k)^2
 = alpha_k^2 det_E(r_i,r_j)^2 (r dot n)^2
 = alpha_k^2 det_E(r_i,r_j)^2 delta`.                           (2.8)

Summing `(2.8)` first over `k`, then over `i<j`, gives `(2.6)`. QED.

This identity is aggregate-before-inversion: no individual pair or triple is selected.

## 3. Main theorem: exact null ray + rank-two bank is paid at packet scale

Assume in addition that the rank-one ray is **spectrally null**,

`r^T M r=0`.                                                    (3.1)

### Theorem 3.1 — `QFORM-RANK2BANK-NULLRAY-PACKET-v1`

Under `(2.1)`-`(2.4)` and `(3.1)`, for arbitrary independent original-coordinate densities bounded by one, and with arbitrary original coordinates outside `B union C` retained in the full exact-rank-three form,

`boxed:
 ||p_Q||_infinity <= 12 [D T_(B,B;C)]^(-1/3).`                 (3.2)

Moreover this branch has a continuous density representative.

#### Proof

Condition on every original coordinate outside `B union C`. Because the ambient matrix has exact rank three, those outside coordinates contribute only an affine term and a constant to the active polynomial; they do not change the active quadratic coefficients. The input coordinates in `B` and `C` remain mutually independent cap-one variables.

**Step 1: compress the entire rank-one bank before any reciprocal payment.** Put

`W=sum_(k in C) alpha_k X_k`.                                  (3.3)

The one-dimensional product-projection theorem gives

`||p_W||_infinity <= K_0:=sqrt(2/m)`.                           (3.4)

The variable `W` is genuinely independent of the whole bank `B` because `B` and `C` are disjoint original-coordinate sets.

**Step 2: keep the rank-two bank as a genuine joint product projection.** Put

`Z=sum_(i in B) r_i X_i in E`.                                 (3.5)

Whitening the coefficient Gram `H_B` turns `Z` into a two-dimensional orthogonal projection of the original product law. Hence the completed two-dimensional product-marginal theorem gives

`||p_Z||_infinity <= M_2:=2/sqrt(h)`.                           (3.6)

No independence between the two coordinates of `Z` is asserted or used.

**Step 3: compute the active determinant exactly.** Choose an orthonormal basis `(e_1,e_2)` of `E` and set

`F=[r,e_1,e_2]`.                                                (3.7)

In variables `(W,Z_1,Z_2)`, before the scalar density normalization, the active quadratic matrix is

`H_0=F^T M F`.                                                  (3.8)

Its scalar pivot is zero by `(3.1)`. Since

`|det F|^2=dist(r,E)^2=delta`,                                  (3.9)

we have

`|det H_0|=D delta`.                                            (3.10)

**Step 4: normalize only the genuinely independent scalar.** Let

`X_0=K_0 W`.                                                    (3.11)

Then `X_0` has density at most one. The active spectral column corresponding to `X_0` is `r/K_0`, so the rescaled active quadratic matrix `H` still has zero scalar pivot and

`|det H|=D delta / K_0^2`.                                     (3.12)

Apply account01/B13's affine zero-pivot `1+2` theorem `(1.1)` conditionally on the outside coordinates. Equations `(3.6)` and `(3.12)` give

`||p_(Q | outside)||_infinity
 <=6 (2/sqrt(h))^(2/3) (K_0^2/(D delta))^(1/3)`.                (3.13)

Using `K_0^2=2/m`, the powers of two combine exactly:

`6 * 2^(2/3) * 2^(1/3)
 =12`,                                                          (3.14)

hence

`||p_(Q | outside)||_infinity
 <=12 (D m h delta)^(-1/3)
 =12 [D T_(B,B;C)]^(-1/3)`,                                   (3.15)

by Lemma 2.1. The bound is uniform in the outside conditioning value, so averaging proves `(3.2)`.

The cited zero-pivot theorem gives a continuous conditional density for every affine shift. Its explicit integral construction is measurable in the outside affine parameters, and `(3.15)` is a common integrable bound. Dominated convergence therefore gives a continuous representative after mixing over the outside coordinates. QED.

### Corollary 3.2 — physical determinant form

For exact rank three,

`|det A_{ijk}|=D det(r_i,r_j,r_k)^2`.

Therefore the packet paid in `(3.2)` is exactly the **sum of physical principal-triple determinants** over the structured bank:

`P_(B,B;C):=sum_(i<j in B,k in C)|det A_{ijk}|=D T_(B,B;C)`.     (3.16)

Thus

`boxed: ||p_Q||_infinity <=12 P_(B,B;C)^(-1/3).`                (3.17)

For example, a packet `P_(B,B;C)>=1/4096` already gives

`||p_Q||_infinity<=192`.                                       (3.18)

This is the useful form for B10's delocalized determinant banks: arbitrarily many tiny local triples are harmless if their **structured total packet** stays bounded below.

## 4. Compatible account04 theorem applied to the new inequality

The exact designated `account04/B10` has no completed current-QFORM artifact discoverable at this run's fresh lookup. I therefore do not attribute a theorem to it.

I instead apply the completed compatible account04/B13 product-purification theorem to `(3.17)`. For the fixed slab kernel

`K_J(x)=1_{x^T A x in J}`,                                     (4.1)

account04/B13 proves the exact identity

`sup_(0<=f_i<=1, int f_i=1) int K_J prod_i f_i
 = sup_(|E_i|=1) |{x in prod_i E_i : x^T A x in J}|`,           (4.2)

with bounded finite interval unions sufficient on the right and no attainment assertion.

The proof of Theorem 3.1, restricted to indicator inputs, gives

`|{x in prod_i E_i : x^T A x in J}|
 <=12 P_(B,B;C)^(-1/3) |J|`.                                  (4.3)

Applying `(4.2)` transfers `(4.3)` with **zero constant loss** to every admissible cap-one product law, recovering the target inequality `(3.17)`. This is an actual use of completed account04 mathematics on the new branch, not merely a citation.

## 5. The nonnull companion and why the true survivor is near-null

For comparison, if the same rank-one bank ray satisfies

`q:=r^T M r !=0`,                                               (5.1)

the entire rank-one bank can again be compressed before paying a scalar pivot. This gives a useful near-null dependence estimate even when the remaining coordinates are not confined to a rank-two bank.

Let the complement spectral vector be decomposed as

`Y_D=r U+Z`, `Z in r^perp`.                                    (5.2)

Because the removed bank `C` lies exactly on `r`, Parseval gives that the transverse coefficient frame for `Z` is an orthogonal two-dimensional projection frame. In the spectral basis `(r,r^perp)`, write

`M=[[q,b^T],[b,C_2]]`,
`S=C_2-bb^T/q`.                                                 (5.3)

Completing the scalar square yields exactly

`Q=q (W+U+b^T Z/q+shift)^2 + Z^T S Z + affine(Z)+const`,        (5.4)

and

`|det S|=D/|q|`.                                                (5.5)

The square pushforward of the translated `W` has the uniform envelope

`K_0 / sqrt(|q| |s|)`.                                         (5.6)

Applying the completed rank-two affine half-Riesz theorem to the Parseval product projection `Z` gives

`sup_t E |Z^T S Z+affine(Z)-t|^(-1/2)
 <=128 |det S|^(-1/4)`.                                        (5.7)

Therefore

`boxed:
 ||p_Q||_infinity
 <=128 sqrt(2) m^(-1/2) D^(-1/4) |q|^(-1/4).`                  (5.8)

This supporting estimate improves the singular exponent in the scalar Rayleigh parameter from the naive square-root pivot loss to a quarter power by retaining the rank-two Schur curvature. It is **not** uniform as `q ->0`; the exact-null theorem of Section 3 is the complementary product-safe endpoint when a rank-two bank packet is available. No coefficient perturbation is invoked between them.

## 6. Application to the r20 heavy tripartite core

Whiten r20's selected tripartite core algebraically. Its normalized rows `u_i` satisfy

`sum_i u_i u_i^T=I_3`,                                        (6.1)

and the whitened spectral matrix `M_S` satisfies

`D_S:=|det M_S|>=1/512`,
`sigma_min(M_S)>=1/512`.                                      (6.2)

Failure of r20's diffuse gate provides a physical hub row with

`m=||u_i||^2>1/2`.                                             (6.3)

Let `r=u_i/sqrt(m)` and `q=r^T M_S r`.

If `|q|>=1/512`, `(5.8)` gives the explicit dimension-free estimate

`||p_Q||_infinity
 <=128 sqrt(2) (1/2)^(-1/2)(1/512)^(-1/4)(1/512)^(-1/4)
 =256 sqrt(512)
 <5793`.                                                       (6.4)

Thus a genuinely unpaid heavy-core sequence can be forced into the **near-null physical direction** `|q|<1/512` without taking a reciprocal local triple.

At exact nullity `q=0`, Theorem 3.1 additionally pays every state in which some disjoint internal rank-two bank `B` carries a structured packet

`P_(B,B;{i})>=1/4096`,                                         (6.5)

with the much smaller bound `192` and continuity.

Finally, apply account04/B13's newest rough ruled theorem to the exact-rank-three selected core. Since `(6.2)` gives spectral scale `sigma>=1/512`, on the one-sheet side of an indefinite signature its conditional interval density contribution is at most

`512 pi sqrt(2) <2275`.                                        (6.6)

Conditioning outside the selected original-coordinate core produces an affine term lying in the range of its rank-three principal block; completing the square is a coordinatewise translation and preserves all density caps. Hence `(6.6)` survives those outside couplings. It does **not** control the two-sheet side, exactly as the source warns.

Consequently the first unpaid B10 implication is now more sharply localized:

**`QFORM-TRIPARTITE-NEARNULL-TWOSHEET-DIFFUSE-PACKET-v1`.**  
Inside r20's uniformly conditioned tripartite core, the remaining difficult sequence may be assumed to have a heavy original-coordinate direction with very small spectral Rayleigh quotient, to lie on the two-sheet side after range-affine completion, and—at exact nullity—to have every available disjoint rank-two bank/null-ray structured principal-triple packet below the fixed aggregate gate. One must pay the genuinely positive-residual / internally rank-three leakage **before** any conditional-height supremum or reciprocal atom. The natural next mechanism is an overlap-sensitive two-bank trace or a three-bank Fresnel argument retaining the dense self-couplings exactly.

This is strictly narrower than r20's generic `heavy + internal transverse` residual, but it is not yet the full exact-rank-three closure.

## 7. Algebra regression check

A bounded numerical regression check was run only on the algebraic identities. For 1000 random rank-two planes/banks and rank-one rays, the largest absolute error in

`T_(B,B;C)=m h delta`

was `5.684341886080801e-13` (the random instances were not scale-normalized, so this is an absolute floating-point check). For 500 random invertible symmetric `M` and random plane/ray frames, the largest absolute error in

`|det(F^T M F)|=|det M| delta`

was `5.329070518200751e-15`.

These computations are regression checks only; the proofs are the exact Cauchy-Binet and determinant arguments above.

## 8. Status

Proved in this run:

- `QFORM-RANK2-RANK1-PACKET-IDENTITY-v1`;
- `QFORM-RANK2BANK-NULLRAY-PACKET-v1`, including the physical packet bound `12 P^(-1/3)` and continuity;
- the nonnull rank-one-bank Schur/half-Riesz estimate `(5.8)`;
- a concrete heavy-core reduction `(6.4)`;
- direct application of completed compatible account04/B13 purification and ruled-side mathematics to `(4.3)` and `(6.6)`.

Not proved:

- `QFORM-TRIPARTITE-NEARNULL-TWOSHEET-DIFFUSE-PACKET-v1`;
- the complete arbitrary-orientation exact-rank-three theorem;
- arbitrary additional spectral directions;
- the full owner QFORM conjecture.

**Full QFORM conjecture: OPEN / NOT PROVED / NOT DISPROVED.**
