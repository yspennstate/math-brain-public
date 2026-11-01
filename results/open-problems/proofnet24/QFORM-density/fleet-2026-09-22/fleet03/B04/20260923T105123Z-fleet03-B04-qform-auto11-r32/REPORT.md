SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B04, 2026-09-23T10:51:23Z.
attacking: finite compound-hub payment by aggregate exterior-power contractions and product Fourier smoothing.

# fleet03/B04 r32 — exact-cross-rank product Plancherel and a rank-three compound-hub exit

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Product Fourier rearrangement  
**Status:** `PROVED SUPPORTING THEOREM / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Scope and first missing implication

The full target remains open: for every dimension, independent real coordinates with probability densities bounded by one, and every real symmetric matrix A with at least three eigenvalues of modulus at least one, prove a universal bound for the density of `X^T A X`, or give a valid counterexample.

The preceding B04 run proved an entropy-dual alternative for a physical cross block M. At the useful parameter `h=2/3`, either the product-Fourier estimate already closes, or some set H of at most six physical rows satisfies

`E3(M_{H^c,*}) < E3(M)/16`.

At exact entropy infeasibility it even gives `|H|<=4` and `rank(M_{H^c,*})<=2`. The unpaid step was to turn this finite compound hub into an L-infinity endpoint without selecting a tiny coefficient.

This run proves an exact-cross-rank product-space theorem which allows arbitrary same-bank quadratic curvature and arbitrary conditioned outside couplings. It then applies it to the finite-hub state. The result completely pays every heavy hub-intersection pattern whose retained cross block has rank exactly three, with an explicit constant. Thus the finite-hub obstruction is narrowed to the genuinely higher-rank (`>=4`) patterns; the exact rank-three pattern is no longer unpaid.

No law-uniform pointwise quadratic-phase decay, arbitrary-joint coarea bound, post-rotation independence, or naive fiber-supremum estimate is used.

## 2. Inputs actually used

### 2.1 Product projection density theorem

Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures* (arXiv:1507.07949), prove that if a product probability density on `R^n` has one-dimensional factors bounded by one, then every `r`-dimensional orthogonal marginal has density bounded by `2^(r/2)`.

This exact product-marginal input was also already applied in fleet01/B16's completed `QFORM-GROUPED-L2-FRESNEL-v1`:

`yspennstate/math-open-problems@e4c589aa572f7d140c78a832af2d554eed97fde4`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B16/20260922T211047Z-fleet01-B16-QFORM-r16/REPORT.md`.

That report's equation (7) gives the three-dimensional instance `||p_Y||_infinity<=2^(3/2)` after frame normalization. I apply the same product-marginal theorem below at the exact L2 inequality, rather than treating a rotated coordinate vector as independent.

### 2.2 Previous B04 compound-hub theorem

`yspennstate/math-open-problems@1c9eda73c97b03bf78aa6750726df00ce3768d21`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B04/20260923T095028Z-fleet03-B04-qform-auto11-r31/REPORT.md`.

In particular, with `Z=E3(M)`, failure of the entropy Fourier exit at `eta=1/16` gives a physical row set H, `|H|<=6`, with

`E3(M_{H^c,*}) < Z/16`.                                           (2.1)

At exact infeasibility, one may take `|H|<=4` and `rank(M_{H^c,*})<=2`.

The designated fleet04/B04 partner still had no completed current-QFORM handoff directory visible on the fresh main lookup for this run, so no partner theorem is invented. The completed fleet01/B16 product-marginal result is the existing-worker result actually applied at an equation below.

## 3. Rearranged complex marginals

Let X and Y be two disjoint banks of original independent coordinates. Their one-dimensional densities are bounded by one. Let

`B` be a real `m x n` matrix of exact rank `r>=3`.

Let `F(X)` and `G(Y)` be arbitrary measurable real functions, finite almost surely. Define

`Q = F(X) + 2 X^T B Y + G(Y)`.                                  (3.1)

Take a thin singular value decomposition

`B = U Sigma V^T`,                                               (3.2)

where `U^T U=V^T V=I_r` and

`Sigma=diag(sigma_1,...,sigma_r)`, `sigma_j>0`.

Put

`Z_X=U^T X`, `Z_Y=V^T Y`.

Let their ordinary marginal densities be `rho_X,rho_Y`, and write

`M_X=||rho_X||_infinity`, `M_Y=||rho_Y||_infinity`.

For each real t define complex pushforward measures

`mu_t^X(E)=E[1_{Z_X in E} exp(i t F(X))]`,

`mu_t^Y(E)=E[1_{Z_Y in E} exp(i t G(Y))]`.

They have densities `a_t,b_t` satisfying

`|a_t|<=rho_X`, `|b_t|<=rho_Y`                                  (3.3)

and `||a_t||_1,||b_t||_1<=1`. Therefore the cap/mass rearrangement inequality gives

`||a_t||_2 <= M_X^(1/2)`, `||b_t||_2 <= M_Y^(1/2)`.             (3.4)

Equation (3.4) is the decreasing-rearrangement payment: among nonnegative functions of mass at most one and cap M, the L2 norm is maximized by filling a set of measure `1/M` at height M. No pointwise oscillatory estimate enters.

## 4. Main theorem — exact-cross-rank product Plancherel

### Theorem 4.1 — `QFORM-EXACT-CROSS-RANK-PLANCHEREL-v1`

Under (3.1)--(3.2), for every exact cross rank `r>=3`, Q has a bounded continuous density vanishing at infinity and

`boxed: ||p_Q||_infinity <= [r/(r-2)] (M_X M_Y)^(1/r) (prod_j sigma_j)^(-1/r).`   (4.1)

In particular the sharp product-marginal bound `M_X,M_Y<=2^(r/2)` gives the dimension-free-in-the-ambient-space estimate

`boxed: ||p_Q||_infinity <= [2r/(r-2)] (prod_j sigma_j)^(-1/r).`                 (4.2)

For rank exactly three,

`boxed: ||p_Q||_infinity <= 6 (sigma_1 sigma_2 sigma_3)^(-1/3)
                              =6 E3(B)^(-1/6).`                                  (4.3)

Here the last identity is Cauchy--Binet for an exact-rank-three matrix.

### Proof

Use Fourier convention

`hat f(xi)=int exp(i xi.y) f(y)dy`,

so Plancherel is `||hat f||_2=(2pi)^(r/2)||f||_2`.

Because X and Y are genuinely independent source banks, (3.1)--(3.3) give

`phi_Q(t)=int_Rr int_Rr a_t(u)b_t(v) exp(2 i t u^T Sigma v) du dv`.              (4.4)

For `t!=0`, integrate first in v and apply Cauchy--Schwarz:

`|phi_Q(t)|
 <= ||a_t||_2 [int |hat b_t(2t Sigma u)|^2 du]^(1/2)`

` = ||a_t||_2 (2|t|)^(-r/2) (prod_j sigma_j)^(-1/2) ||hat b_t||_2`

` = (pi/|t|)^(r/2) (prod_j sigma_j)^(-1/2) ||a_t||_2 ||b_t||_2`.                 (4.5)

By (3.4), with

`D=prod_j sigma_j`,

`|phi_Q(t)| <= K |t|^(-r/2)`,

`K=pi^(r/2) D^(-1/2)(M_XM_Y)^(1/2)`.                            (4.6)

Together with `|phi_Q(t)|<=1`,

`|phi_Q(t)| <= min(1,K|t|^(-r/2))`.                             (4.7)

Since `r>2`, this is integrable. Let `T=K^(2/r)`. Direct integration gives

`int_R min(1,K|t|^(-r/2)) dt
 =2[T + K int_T^infinity t^(-r/2)dt]
 = [2r/(r-2)] K^(2/r).`                                        (4.8)

Fourier inversion therefore yields

`||p_Q||_infinity
 <= (1/(2pi)) [2r/(r-2)] K^(2/r)
 = [r/(r-2)] (M_XM_Y)^(1/r)D^(-1/r)`,                          (4.9)

which is (4.1). The product-marginal theorem gives `M_X,M_Y<=2^(r/2)`, so `(M_XM_Y)^(1/r)<=2`, proving (4.2). The integrable characteristic function also gives a continuous `C_0` representative. QED.

### Conditional ambient version

If a full quadratic form contains two disjoint original-coordinate banks I,J with cross block `B=A[I,J]` of exact rank `r>=3`, condition on every original coordinate outside `I union J`. The conditional form has exactly the shape (3.1): all self curvature and induced affine terms are absorbed into F and G, while the cross block B is unchanged. The bound above is uniform in the conditioning values. Averaging gives the same L-infinity bound. More directly, the unconditional characteristic function inherits (4.7), so continuity is retained as well.

Thus Theorem 4.1 tolerates arbitrary same-bank quadratic blocks, arbitrary outside quadratic coefficients and arbitrary outside couplings.

## 5. Finite compound-hub rank-three payment

Let M be a physical cross block and let

`Z=E3(M)>0`.

Assume a physical row set H with `|H|=h` satisfies

`E3(M_{H^c,*}) <= eta Z`, `0<=eta<1`.                            (5.1)

For each nonempty `K subset H`, let `W_K` be the sum of squared 3-by-3 minors whose physical row triple S has exact hub intersection

`S cap H = K`.                                                    (5.2)

Because a 3-row minor uses at most three rows of H, only subsets with `1<=|K|<=3` can occur. Certainly there are at most `2^h-1` nonempty classes. From (5.1),

`sum_{K nonempty} W_K >= (1-eta)Z`.                              (5.3)

Hence some nonempty K obeys

`W_K >= (1-eta)Z/(2^h-1)`.                                      (5.4)

Now condition the original hub coordinates in `H minus K` and retain all coordinates in `H^c union K`. Let

`B_K=M_{H^c union K,*}`.                                        (5.5)

Every minor counted by `W_K` remains a minor of `B_K`, so

`E3(B_K)>=W_K`.                                                   (5.6)

If `rank(B_K)=3`, Theorem 4.1 gives, uniformly in the conditioned hub values,

`||p_Q||_infinity
 <=6 E3(B_K)^(-1/6)
 <=6 [(2^h-1)/(1-eta)]^(1/6) Z^(-1/6).`                         (5.7)

This proves:

### Corollary 5.1 — `QFORM-COMPOUND-HUB-RANK3-PATTERN-EXIT-v1`

Whenever a finite row hub H captures all but eta of the third-minor volume and one volume-heavy exact hub-intersection pattern K has retained cross rank exactly three, the full ambient quadratic has a continuous density satisfying (5.7).

For the preceding B04 parameters `h<=6`, `eta=1/16`,

`boxed: ||p_Q||_infinity <=12.097978152622812 Z^(-1/6).`          (5.8)

For the substantial-third-volume packet recorded in the preceding report, `Z>=2^(-18)`, this becomes

`boxed: ||p_Q||_infinity <=96.7838252209825.`                    (5.9)

At exact entropy infeasibility the preceding run gives `h<=4` and `rank(M_{H^c,*})<=2`. Since the empty-hub class has zero third volume, a nonempty hub pattern has weight at least `Z/15`. If one such heavy pattern leaves exact rank three, (5.7) improves to

`||p_Q||_infinity <=6*15^(1/6) Z^(-1/6)
                    =9.422506814850118 Z^(-1/6).`               (5.10)

The remaining exact support-deficient obstruction is therefore not “finite hub” in general. It is specifically the case in which every determinant-volume-heavy retained hub pattern has cross rank at least four (or the relevant rank-three patterns carry too little third volume).

## 6. Genuinely rotated indefinite target with all self and cross entries nonzero

Define two orthogonal matrices

`R=(1/3) [[1,-2,-2],[-2,1,-2],[-2,-2,1]]`,

and, with `v=(1,2,3)^T`,

`S=I-2 vv^T/(v^Tv)
  =[[6/7,-2/7,-3/7],[-2/7,3/7,-6/7],[-3/7,-6/7,-2/7]].`

Let

`B=R diag(3,2,1) S^T`

` =[[32/21,-2/7,19/21],
    [-34/21,10/7,10/21],
    [-31/21,-2/7,40/21]].`                                     (6.1)

Every entry of B is nonzero, its singular values are exactly `3,2,1`, and `det B=6`.

Now set

`A = [[J_3/20, B], [B^T, J_3/20]]`,                             (6.2)

where `J_3` is the all-ones 3-by-3 matrix. Thus every physical entry of A is nonzero; there is genuine same-bank curvature on both sides and a dense rotated cross interaction.

Let `A_0=[[0,B],[B^T,0]]`. Its exact spectrum is

`{-3,-2,-1,1,2,3}`.                                             (6.3)

The perturbation `A-A_0=diag(J_3/20,J_3/20)` has operator norm `3/20`. Weyl's inequality therefore leaves the four eigenvalues associated to `+/-3,+/-2` with modulus at least `2-3/20=1.85`. Hence A is an indefinite target satisfying the required “at least three eigenvalues of modulus at least one” hypothesis.

For this example the two source banks each have exactly three original coordinates. The SVD rotations are volume-preserving `3x3` maps, so the projected joint densities satisfy the sharper caps

`M_X,M_Y<=1`                                                     (6.4)

rather than `2^(3/2)`. The parameterized estimate (4.1) gives, for every admissible independent cap-one input law,

`boxed: ||p_{X^T A X}||_infinity
       <=3*6^(-1/3)
       =1.6509636244473134.`                                    (6.5)

The density is continuous and vanishes at infinity. This example is fully indefinite and physically dense; the theorem does not depend on the small self-block size except for the separate spectral certificate that A belongs to the target class.

## 7. Why this does not solve the full conjecture

Theorem 4.1 is insensitive to ambient dimension but it pays the complete pseudodeterminant of the exact physical cross block. For cross rank `r>3`, an additional singular value may be arbitrarily small even while `E3(M)` is large. Because the input laws have no moment or support bound, a small coefficient cannot simply be discarded as a perturbation. Thus (4.2) does not convert the bare three-large-eigenvalue hypothesis into a universal constant.

The concrete new residual after combining r31 and this run is:

`QFORM-FINITE-COMPOUND-HUB-HIGHER-RANK-v1`:

> In the at-most-six-row/at-most-six-column compound-hub state, handle the determinant-volume-heavy patterns whose retained physical cross rank is at least four, without paying arbitrarily small extra singular values. Equivalently, combine the rank-three pattern exit above with a regularized-determinant / mixed-norm mechanism that ignores tiny fourth-and-higher cross singular values while retaining enough integrated Fourier decay.

This is strictly narrower than the preceding “pay the finite hub” debt: the rank-three part of that debt is now complete, with constants.

## 8. Checks and integrity boundary

The finite arithmetic checked for the explicit example is recorded in `CHECKS.json` beside this report: `R^T R=S^T S=I`, `det B=6`, `spec(B^T B)={9,4,1}`, `spec(A_0)={-3,-2,-1,1,2,3}`, and the constants in (5.8)--(6.5).

The live corrections remain binding. In particular, the proof uses a uniform L2 norm of **complex projected measures**, not pointwise one-dimensional Fresnel decay, and it never asserts independence of the projected vectors `U^T X` or `V^T Y`.

Full QFORM remains OPEN. Full-target continuity also remains OPEN; continuity is proved only for the branches stated here.
