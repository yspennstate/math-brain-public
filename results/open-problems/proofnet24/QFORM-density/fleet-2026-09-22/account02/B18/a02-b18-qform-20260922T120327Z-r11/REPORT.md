# account02/B18 — literature-to-proof transfer: joint bilinear–square smoothing

**Run:** `a02-b18-qform-20260922T120327Z-r11`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** `Literature-to-proof transfer` / STRUCTURE  
**Status:** supporting theorem proved and partner-integrated; full conjecture OPEN / NOT PROVED  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Scope, sources, and correction discipline

The live target is: for independent real `X_i` with densities bounded by 1 and real symmetric `A` with at least three eigenvalues of magnitude at least 1, prove that `X^T A X` has an essentially bounded density with a universal bound.

This report does not use the refuted law-uniform pointwise Fresnel decay, does not rotate physical inputs and pretend independence survives, and does not use a bare nonsingular cross-minor as if it were sufficient. The current correction `QFORM-CROSSMINOR-ALONE-FALSE` is respected: a rank-two hyperbolic term by itself can have a logarithmic singularity. The third square below is the smoothing resource.

### Primary literature input

Mark Rudelson and Roman Vershynin, *Small Ball Probabilities for Linear Images of High-Dimensional Distributions*, IMRN 2015, no. 19, 9594–9617, DOI `10.1093/imrn/rnu243`, Theorem 1.2:

> if independent real variables have densities bounded by `K` and `sum a_i^2=1`, then the density of `sum a_i X_i` is bounded by `sqrt(2) K`.

This exact sharp one-dimensional projection theorem is the only external theorem used below.

### Completed internal results consumed

1. **Assigned partner account03/B18**, run `20260922T120058Z-account03-B18-qform-r1`, scientific commit `53bf1a45bf46dfa09a963d95935f6413c911d1b5`. Its Banks transfer proves that a physical pure bipartite form `[[0,B],[B^T,0]]` satisfies

`||p_Q||_infinity <= 2 sqrt(e pi)/sqrt(sigma_1(B)sigma_2(B))`,

so `sigma_2(B)>=1` closes that target slice. It also gives a one-pivot Schur + rank-two-bipartite + square theorem. Sections 6–7 below apply and sharpen the latter mechanism by smoothing the bilinear term and square jointly, reducing the Schur cross-block requirement from a second singular value to the top singular value.

2. **account03/B08**, `QFORM-DIFFUSE-SPECTRAL-FRAME-v1`, math-open-problems commit `9dcddd0bf3fbcb8e0b3396e0a4d883924d3f4ada`. If the selected low-rank spectral frame has all row leverages at most `1/2`, it gives `||p_Q||_infinity<=3e` when the selected eigenvalue determinant is at least 1, even with arbitrary coordinatewise phases. This is complementary to the localized physical-block mechanism below.

## 2. Rearrangement lemmas

### Lemma 2.1 — singular moment under a bounded density

If `U` has probability density `f_U` with `||f_U||_infinity <= K_U`, then

`E |U|^{-1/2} <= 2 sqrt(2 K_U)`.

**Proof.** The kernel `k(u)=|u|^{-1/2}` has decreasing rearrangement `k*(s)=sqrt(2/s)`. Among densities `0<=f<=K_U` of mass 1, the integral is maximized by filling the top `1/K_U` measure of the kernel. Hence

`int k f <= K_U int_0^{1/K_U} sqrt(2/s) ds = 2 sqrt(2K_U)`.

No support or moment assumption is used. `QED`

### Lemma 2.2 — conditional square smoothing

Let `(T,W)` be a pair of real random variables. Assume

- `T` has a density bounded by `K_T`;
- for almost every `t`, a regular conditional law of `W` given `T=t` has a density bounded by `K_W`;
- `beta !=0`.

Then

`T+beta W^2`

has a density satisfying

`||p_{T+beta W^2}||_infinity <=2 K_W sqrt(K_T/|beta|)`.                    (2.1)

**Proof.** By reflection take `beta>0`. Conditional on `T=t`, the density of `beta W^2` at `s>0` is at most `K_W/sqrt(beta s)`. Therefore for every output value `q`,

`p(q) <= (K_W/sqrt(beta)) int_{t<q}(q-t)^(-1/2)p_T(t)dt`.

The translated one-sided kernel has decreasing rearrangement `r^(-1/2)`. Since `p_T<=K_T` and has mass 1, the bathtub principle gives

`int (q-t)_+^(-1/2)p_T(t)dt <= K_T int_0^{1/K_T}r^(-1/2)dr=2sqrt(K_T)`.

This proves (2.1). Notice that **independence of `T` and `W` is not required**; a uniform conditional density bound suffices. `QED`

A useful source-valid instance is `W=Z+h(V)`, where `Z` is independent of `V` with density bounded by `K_W` and `T` is any function of `V`: conditioning on `T` makes `W` a mixture of translations of `Z`, so its conditional density remains bounded by `K_W`.

## 3. Main new theorem: arbitrary bilinear block + translated square

### Theorem 3.1 — `QFORM-JOINT-BILINEAR-SQUARE-v1`

Let

- `X=(X_1,...,X_m)` and `Y=(Y_1,...,Y_k)` have mutually independent coordinates, each coordinate density bounded by 1;
- `Z` be independent of `(X,Y)` with density bounded by `K_Z`;
- `B` be a nonzero real `m x k` matrix;
- `alpha beta !=0`;
- `F:R^m->R` and `h:R^m x R^k->R` be arbitrary measurable functions;
- `r_Y in R^k` and `c in R`.

Define

`Q = 2 alpha X^T B Y + F(X) + r_Y^T Y + c + beta [Z+h(X,Y)]^2`.           (3.1)

Then `Q` has an essentially bounded density and

`||p_Q||_infinity <= 4 sqrt(2) K_Z / sqrt(|alpha beta| sigma_1(B))`.       (3.2)

### Proof

Condition on `X=x`. Put

`d(x)=2 alpha B^T x+r_Y`,
`T_x=d(x)^T Y + F(x)+c`,
`W_x=Z+h(x,Y)`.

For `d(x)!=0`, Rudelson–Vershynin Theorem 1.2 gives

`||p_{T_x}||_infinity <= sqrt(2)/||d(x)||_2`.                              (3.3)

Given `X=x` and `T_x=t`, the conditional law of `Y` may be complicated, but `Z` remains independent. Hence `W_x=Z+h(x,Y)` is a mixture of translations of the `Z` law and its conditional density is still bounded by `K_Z`. Lemma 2.2 applied conditionally gives

`||p_{Q|X=x}||_infinity`
`<=2 K_Z sqrt( sqrt(2)/[|beta| ||d(x)||_2])`
`=2^(5/4)K_Z |beta|^(-1/2)||d(x)||_2^(-1/2)`.                            (3.4)

Let `sigma=sigma_1(B)>0`; let `u,v` be unit left/right singular vectors for `sigma`, so `Bv=sigma u`, `B^Tu=sigma v`. Then

`||d(x)||_2 >= |v^T d(x)|=|2 alpha sigma u^T x+v^T r_Y|`.                 (3.5)

The scalar `U=u^T X` has density at most `sqrt(2)` by the same Rudelson–Vershynin theorem. Consequently the affine scalar

`S=2 alpha sigma U+v^T r_Y`

has density at most

`K_S <= sqrt(2)/(2|alpha|sigma)=1/[sqrt(2)|alpha|sigma]`.

Lemma 2.1 yields

`E ||d(X)||_2^(-1/2) <= E|S|^(-1/2)`
`<=2sqrt(2K_S)=2^(5/4)/sqrt(|alpha|sigma)`.                                (3.6)

Average (3.4) and use (3.6):

`||p_Q||_infinity`
`<=2^(5/4) *2^(5/4) K_Z /sqrt(|alpha beta|sigma)`
`=2^(5/2)K_Z/sqrt(|alpha beta|sigma)`
`=4sqrt(2)K_Z/sqrt(|alpha beta|sigma_1(B))`.

The exceptional set `d(X)=0` has probability zero because it forces the absolutely continuous scalar `S` to vanish. `QED`

### Consequence

Both the entire `X`-side self-interaction `F(X)` and the translation `h(X,Y)` of the square may be arbitrary. This asymmetry is useful after conditioning: one physical side of a Schur residual can carry an arbitrary quadratic principal block, while the `Y` side remains linear.

## 4. Independent third block transfer

Let a third disjoint coordinate block `W=(W_l)_{l in K}` have independent coordinate densities bounded by 1, and let `Z=c_0^T W` with `C0=||c_0||_2>0`. Rudelson–Vershynin gives `K_Z<=sqrt(2)/C0`. With `h=0`, Theorem 3.1 gives

`||p_{2alpha X^TBY+F(X)+r_Y^TY+beta(c_0^TW)^2}||_infinity`
`<=8/[C0 sqrt(|alpha beta|sigma_1(B))]`.                                  (4.1)

An arbitrary independent remainder on a fourth disjoint coordinate block may be added without increasing this bound.

## 5. Exact three-large-eigenvalue block slice

Partition physical coordinates into disjoint sets `I,J,K,D`. Let `B` be an `|I| x |J|` matrix, `c_0` a nonzero vector on `K`, and `A_D` any symmetric matrix supported on `D`. Define

`A = [[0, alpha B, 0, 0],
      [alpha B^T, 0, 0, 0],
      [0, 0, beta c_0 c_0^T, 0],
      [0, 0, 0, A_D]]`.                                                   (5.1)

The bipartite block has eigenvalues `+-|alpha|sigma_j(B)` and the rank-one square block has eigenvalue `beta C0^2`. If

`|alpha|sigma_1(B)>=1`,   `|beta|C0^2>=1`,                                (5.2)

then (5.1) has at least three eigenvalues of magnitude at least 1 and

`||p_{X^TAX}||_infinity<=8`.                                              (5.3)

Indeed (5.2) implies `C0^2|alpha beta|sigma_1(B)>=1`, so the denominator in (4.1) is at least 1. Smaller singular values of `B` are irrelevant.

This precisely pays the sharp rank-two control: if the square block is removed and `B` has only one nonzero singular value, centered uniform inputs give the logarithmic product singularity. The square is the third curvature resource that changes the singular kernel from nonintegrable-at-density-level to the integrable negative half moment in (3.6).

## 6. Direct application of the assigned partner result

The assigned partner account03/B18 proves:

`A=[[0,B],[B^T,0]], sigma_2(B)>=1  =>  ||p_{X^TAX}||_infinity<=2sqrt(e pi)`. (6.1)

Combining (6.1) with (5.3) gives a source-valid block dictionary:

- **two large bipartite singular values:** partner/Banks theorem, bound `2sqrt(e pi)`;
- **one large bipartite singular value + one large independent square:** this report, bound `8`.

Thus, on block-separable physical forms, the exact three-large threshold is covered without any `sigma_2` lower bound when the third eigenvalue is supplied by the square block. This fills the singular-value gap in the pure-bipartite transfer rather than re-proving it.

## 7. Schur-pivot strengthening of the partner mechanism

Choose one **physical** coordinate `z` and write, after a coordinate permutation,

`A = [[a, b^T],[b,C]]`,  with `a!=0`.

Completing the physical square gives

`x^T A x = a[z+(b^T w)/a]^2 + w^T S w`,

where

`S=C-bb^T/a`.                                                              (7.1)

Partition some remaining physical coordinates into disjoint groups `I,J`, and condition on every coordinate outside `I union J union {z}`. Assume only that the **J-side quadratic block vanishes** in the Schur complement,

`S_JJ=0`,                                                                  (7.2)

and let

`B_0=S_IJ`.                                                                 (7.3)

The block `S_II` may be completely arbitrary. After conditioning the outside coordinates,

- `X_I^T S_II X_I` and all conditioned terms form the arbitrary function `F(X)` in Theorem 3.1;
- couplings from `J` to conditioned coordinates form `r_Y^T Y`;
- the completed-square center `(b^T w)/a` is an arbitrary affine `h(X,Y)`;
- the original physical pivot `z` remains independent with density bounded by 1.

Therefore Theorem 3.1 applies with `alpha=1`, `beta=a`, `K_Z=1`:

`||p_{X^TAX}||_infinity <=4sqrt(2)/sqrt(|a|sigma_1(B_0))`.                  (7.4)

By symmetry, the same conclusion holds if `S_II=0` instead, with the roles of `I,J` exchanged. In particular,

`|a|sigma_1(B_0)>=1  =>  ||p_{X^TAX}||_infinity<=4sqrt(2)`.                 (7.5)

This is `QFORM-SCHUR-ONESIDED-CROSS-SQUARE-v1`.

**Improvement relative to the consumed partner result.** The partner's one-pivot Schur theorem first obtains a bounded residual bilinear density and therefore needs a rank-two cross scale (`sigma_2`). Equation (7.4) never asks the residual bilinear form to have a bounded density by itself. It combines the rank-one conditional linear density with the pivot square before averaging and hence needs only `sigma_1`. It also allows an arbitrary self-interaction on the conditioned `X` side; only the opposite `Y` principal block must vanish.

The correction `QFORM-CROSSMINOR-ALONE-FALSE` remains respected: when `a=0`, the square resource vanishes and (7.4) gives nothing.

## 8. Relation to the diffuse theorem and remaining full implication

The current state now has three distinct source-valid mechanisms:

1. **Diffuse spectral frame** (account03/B08): max row leverage at most `1/2`, bound `3e` for the low-rank-plus-coordinatewise-remainder model.
2. **Pure physical bipartite rank >=2** (assigned partner account03/B18 / Banks): `sigma_2(B)>=1`, bound `2sqrt(e pi)`.
3. **Physical pivot square + one-sided Schur cross block** (this report): `|a|sigma_1(B_0)>=1`, bound `4sqrt(2)`, with arbitrary self-interaction on one active side and arbitrary outside couplings handled by conditioning.

The full conjecture is still open. The first unpaid structural implication is now sharper:

> From a general symmetric `A` with at least three eigenvalues of magnitude at least 1, prove that either a source-valid diffuse-frame branch applies, or there is a physical scalar pivot `a` and a conditioning partition for which one side of the Schur residual has vanishing principal block and `|a|sigma_1(B_0)` is bounded below by a universal constant; otherwise identify and control the remaining two-sided self-interaction geometry.

One must not replace this by a bare cross-minor statement, and an orthogonal change of physical coordinates is forbidden because it destroys independence. Rudelson–Vershynin's large-coordinate removal/tensorization method is a natural next source to test against this structural dichotomy.

## 9. Status

`QFORM-JOINT-BILINEAR-SQUARE-v1`: **PROVED_IN_SOURCE / supporting theorem**.

`QFORM-SCHUR-ONESIDED-CROSS-SQUARE-v1`: **PROVED_IN_SOURCE / supporting theorem**.

Block-separable three-large-eigenvalue corollary (5.3): **PROVED_IN_SOURCE / target conclusion on stated structural class**.

`QFORM-DENSITY-THREE-LARGE-EIGENVALUES`: **OPEN / NOT PROVED**.

No novelty claim is made. Independent end-to-end review has not occurred.
