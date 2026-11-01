SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B18, 2026-09-23T17:05:38Z.
attacking: the exact-rank-three null-hub heavy-anchor tiny-edge collar, with emphasis on source-valid treatment of the exact zero-edge endpoint and source-separated/aligned twists.

# fleet02/B18 auto11 — zero-edge heavy endpoint and source-separated twist closure

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Role:** Literature-to-proof transfer / complementary constructions  
**Status:** `NEW SUPPORTING TARGET-LEVEL THEOREMS / DESIGNATED PARTNER APPLIED / FULL QFORM OPEN`  
**Continuity:** essential boundedness only for the new theorems; no continuity claim.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The unrestricted owner target remains **OPEN / NOT PROVED / NOT DISPROVED**: arbitrary independent real coordinates with one-dimensional probability densities bounded by one, arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, no moment/support/log-concavity/iid/rotated-independence assumption.

## 1. First unpaid implication after this run

The exact-rank-three null-hub moderate/high-shear packet has the already proved original-coordinate normal form

`Q=2(X_0+ell dot X_L)(g dot X_L)+d(beta dot X_L)^2`,                 (1.1)

with

`||beta||_2=1`, `beta dot g=0`, `gamma=||g||_2>0`.                 (1.2)

In the target-normalized compiler,

`|d| gamma^2=h D`, `h>=1/5`, `D=|pdet A|>=1`.                     (1.3)

For a leaf `i`, write

`q_i=beta_i^2+g_i^2/gamma^2`.                                      (1.4)

Completed fleet03/B18 r28 pays `max q_i<=1/2` continuously by `<12.927`; completed fleet04/B18 r4 pays a heavy witness `q_i>1/2` whenever `|g_i|>=1/64` by `<64.180`.

This run additionally pays:

* **every exact zero-edge heavy witness `g_i=0`, with arbitrary dense/source-entangled twist `ell`;**
* **every source-separated/aligned twist**, even if the heavy edge is tiny or zero.

Therefore the first local exact-null debt is sharpened to a genuinely punctured and source-entangled state:

`q_i>1/2`, `0<|g_i|<1/64`, no diffuse exit, and no decomposition that peels the twist onto coordinates disjoint from both `g` and `beta` while leaving the active part in `span{g,beta}`.       (1.5)

A small nonzero `g_i` is not replaced by zero: arbitrary cap-one inputs are unbounded and the live correction forbids coefficient deletion by perturbative continuity.

## 2. Primary theorem checked at literal hypotheses

The external source actually used is Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949 / Israel J. Math. 216 (2016), Theorem 1.1.

Its literal statement: for `1<=k<n`, `E in G_{n,k}`, there are `gamma_j in [0,1]`, `sum gamma_j=k`, such that for bounded nonnegative one-dimensional functions `f_j` with `||f_j||_1=1`, the product `f=prod f_j` satisfies

`||pi_E f||_infinity <= min((n/(n-k))^((n-k)/2),2^(k/2)) prod_j ||f_j||_infinity^(gamma_j)`.   (2.1)

Thus the owner cap-one class has every normalized one-dimensional original-product projection capped by `sqrt(2)` and every normalized two-dimensional projection capped by `2`. There is no moment, support, log-concavity, smoothness, iid, centering, or symmetry assumption. The conclusion is a joint marginal-density bound, **not independence of projected coordinates**. If the source block has dimension exactly `k`, the needed endpoint follows directly from the determinant-one/orthogonal change of variables and is at least as strong.

## 3. A two-scalar square/affine smoothing lemma

### Lemma `QFORM-SQUARE-AFFINE-RANDOM-SLOPE-v1`

Let `U,V` be independent real random variables with density caps at most one. Fix `a!=0`, arbitrary `b`, and `t!=0`. Then

`Z=aU^2+bU+2tV`                                                    (3.1)

has a density satisfying

`||p_Z||_infinity <= H_a(t)`,                                     (3.2)

where

`H_a(t)=min{1/(2|t|), sqrt(2/(|a||t|))}`.                         (3.3)

**Proof.** Complete the `U` square. A translated cap-one scalar square with coefficient `a` has density bounded by the one-sided kernel

`k_a(x)=|a|^(-1/2)|x|^(-1/2)`                                    (3.4)

(on the appropriate sign half-line). The variable `2tV` has a probability density capped by

`B=(2|t|)^(-1)`.                                                   (3.5)

Convolution gives the trivial cap `B`. For the second cap, among probability densities bounded by `B`, the integral against the decreasing square-root singularity is maximized by filling an interval of length `1/B` adjacent to the singularity. Hence

`sup_y integral h(z) k_a(y-z) dz
 <= B integral_0^(1/B) |a|^(-1/2)x^(-1/2) dx
 =2 sqrt(B)/sqrt(|a|)
 =sqrt(2/(|a||t|))`.                                              (3.6)

This proves (3.3). QED.

### Lemma `QFORM-RANDOM-SLOPE-BATHTUB-v1`

Let `T` have a probability density capped by `sqrt(2)/gamma`, `gamma>0`. Then for every `a!=0`, putting

`H=|a| gamma^2`,                                                   (3.7)

one has

`E H_a(T) <= 6 e^(-1/3) H^(-1/3)`.                               (3.8)

**Proof.** The weight `H_a(t)` is even and decreasing in `|t|`. By the bathtub principle the worst cap-`K` density, `K=sqrt(2)/gamma`, is the saturated interval around zero of radius

`R=1/(2K)=gamma/(2sqrt(2))`.                                      (3.9)

The two branches in (3.3) cross at

`t_*=|a|/8`.                                                       (3.10)

If `R<=t_*`, direct integration gives

`E H_a(T)<=2^(9/4)/sqrt(|a|gamma)`.                               (3.11)

The case condition is `|a|>=2sqrt(2)gamma`, equivalently `H>=2sqrt(2)gamma^3`; substitution in (3.11) gives

`E H_a(T)<=4 H^(-1/3)`.                                          (3.12)

If `R>t_*`, direct integration gives

`E H_a(T)<= (sqrt(2)/gamma)[2+log(2sqrt(2)gamma/|a|)]`.            (3.13)

Set

`x=2sqrt(2)gamma^3/H>1`.                                         (3.14)

Then (3.13) is

`2 H^(-1/3) x^(-1/3)(2+log x)`.                                  (3.15)

The scalar function `x^(-1/3)(2+log x)` is maximized on `[1,infinity)` at `x=e`, with value `3e^(-1/3)`. Thus (3.8) follows, and it dominates (3.12). QED.

## 4. Main theorem — exact zero-edge heavy anchors are paid

### Theorem `QFORM-NULLHUB-ZEROEDGE-HEAVY-CLOSURE-v1`

In the null-hub normal form (1.1)-(1.2), suppose a leaf `i` satisfies

`g_i=0`, `beta_i!=0`.                                             (4.1)

Then for arbitrary independent original-coordinate cap-one laws, `Q` has an essentially bounded density and

`boxed: ||p_Q||_infinity
 <=6 e^(-1/3) (|d| gamma^2 beta_i^2)^(-1/3).`                     (4.2)

Equivalently, since `q_i=beta_i^2` when `g_i=0`,

`boxed: ||p_Q||_infinity
 <=6 e^(-1/3) (|d| gamma^2 q_i)^(-1/3).`                          (4.3)

No restriction is placed on `ell`; it may be dense and source-entangled with the `g` projection.

**Proof.** Delete coordinate `i` and write

`T=g_- dot X_-`, `B_-=beta_- dot X_-`, `L_-=ell_- dot X_-`.        (4.4)

Because `g_i=0`, `||g_-||=gamma`. Condition on the complete original block `X_-`. The only remaining variables are the two genuinely independent ORIGINAL coordinates `X_0` and `X_i`. Expanding (1.1), the conditional quadratic is

`Q=d beta_i^2 X_i^2
  +2(ell_i T+d beta_i B_-)X_i
  +2T X_0
  +C(X_-)`.                                                       (4.5)

Thus Lemma 3 applies with

`a=d beta_i^2`;                                                    (4.6)

all dependence on `L_-`, `B_-`, the output level and the conditioned block enters only through a linear coefficient or additive shift, which the lemma is uniform over.

Now `T/gamma` is a normalized one-dimensional linear projection of the disjoint ORIGINAL product block `X_-`. By the primary theorem (2.1), its density cap is at most `sqrt(2)`; hence

`||p_T||_infinity<=sqrt(2)/gamma`.                                (4.7)

If `X_-` has only one active source coordinate, the direct cap after scaling is even smaller, so (4.7) still holds. Averaging the conditional densities and invoking Lemma 3.8 with

`H=|d| beta_i^2 gamma^2`                                          (4.8)

proves (4.2). QED.

### Target-normalized heavy consequence

In the completed B18 moderate/high-shear compiler, (1.3) holds. If the zero-edge witness is heavy, `q_i=beta_i^2>1/2`, then

`|d|gamma^2 q_i=hD q_i>1/10`.                                    (4.9)

Therefore

`boxed: ||p_Q||_infinity
 <6 e^(-1/3) 10^(1/3)
 =9.262319471965087... .`                                         (4.10)

This closes the **literal `g_i=0` endpoint** left by fleet04/B18 r4. It also closes the `q_i=1,g_i=0` near-coloop endpoint where the newest fleet03/B18 r31 whitening checkpoint has `det G_i=1-q_i=0` and therefore cannot use its residual two-dimensional pair cap.

Continuity is not claimed by this argument.

## 5. A genuinely source-entangled target family paid by Theorem 4

Let `X_0,X_1,X_2,X_3` be arbitrary independent cap-one inputs and put

`G=(X_1+X_2)/sqrt(2)`, `W=(X_1-X_2)/sqrt(2)`,                     (5.1)

`Q_theta=2(X_0+theta W)G+X_3^2`.                                 (5.2)

For arbitrary product laws the rotated variables `G,W` need not be independent, and no such independence is used. In the original coordinates the physical matrix is

`A_theta = [[0,1/sqrt(2),1/sqrt(2),0],
            [1/sqrt(2),theta,0,0],
            [1/sqrt(2),0,-theta,0],
            [0,0,0,1]]`.                                         (5.3)

An orthogonal change used only to compute its spectrum gives the block

`[[0,1,0],[1,0,theta],[0,theta,0]] direct_sum [1]`,               (5.4)

so

`spec(A_theta)={-sqrt(1+theta^2),0,1,sqrt(1+theta^2)}`.            (5.5)

Hence (5.2) is in the exact owner target for every real `theta`.

Take the heavy leaf `i=3`. Then `g_i=0`, `beta_i=1`, `gamma=1`, `d=1`, so (4.2) yields the **whole-line**, law-uniform estimate

`boxed: ||p_(Q_theta)||_infinity
 <=6 e^(-1/3)
 =4.299187863442736...}`                                          (5.6)

for every `theta`, despite the dense/source-entangled twist `theta W` sharing the same original sources as `G`.

This is more than an aligned/source-separated special case.

### Required pinned e5f result applied to the same family

The pinned record `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `COUNTEREXAMPLE_SEARCH.md`, proves its ruled one-sheet theorem: for an exact rank-three signature `(2+,1-)` with all three magnitudes at least one and no out-of-range linear term,

`p_Q(t)<=pi sqrt(2)` on the one-sheet/majority-sign half-line.      (5.7)

The family (5.2) has precisely that signature, so literally

`boxed: p_(Q_theta)(t)<=pi sqrt(2)
 for a.e. t>=0.`                                                   (5.8)

The new zero-edge theorem pays the formerly more delicate whole line and improves the numerical constant on this family from `pi sqrt(2)=4.442882938...` to `4.299187864`.

The e5f counterexample search itself reports no valid QFORM counterexample and explicitly leaves convex/two-sheet geometry open. That search miss is not treated as novelty evidence.

## 6. Second theorem — source-separated/aligned twists are paid

### Theorem `QFORM-NULLHUB-SOURCE-SEPARATED-TWIST-CLOSURE-v1`

In (1.1), suppose the leaf indices split into disjoint original-coordinate sets

`L=J disjoint_union K`                                             (6.1)

such that

`g_K=0`, `beta_K=0`,                                               (6.2)

and for some real numbers `a,b`,

`ell_J=a g_J+b beta_J`.                                            (6.3)

Then

`boxed: ||p_Q||_infinity
 <=3*4^(2/3)(|d|gamma^2)^(-1/3).`                                 (6.4)

In the target-normalized moderate/high-shear compiler, `|d|gamma^2=hD>=1/5`, hence

`boxed: ||p_Q||_infinity
 <=3*4^(2/3)*5^(1/3)
 =12.9266081401913... .`                                          (6.5)

**Proof.** Put

`S=X_0+ell_K dot X_K`, `C=g dot X_J`, `D_0=beta dot X_J`.          (6.6)

Because `X_0` is independent of `X_K` and has density cap one, convolution with the independent random shift `ell_K dot X_K` gives

`||p_S||_infinity<=1`.                                             (6.7)

The source set of `S` is disjoint from `J`, so `S` is genuinely independent of `(C,D_0)`.

The coefficient rows `g/gamma` and `beta` are orthonormal. Thus `(C/gamma,D_0)` is an orthogonal two-dimensional projection of the ORIGINAL product block `X_J`. By LPP, its joint density cap is at most `2`; after undoing the deterministic scaling,

`||p_(C,D_0)||_infinity<=2/gamma`.                                (6.8)

No independence of `C,D_0` is asserted.

Using (6.3), the quadratic becomes

`Q=2SC+2aC^2+2bCD_0+dD_0^2`.                                     (6.9)

Apply the completed fleet02/B18 theorem `QFORM-CAPPED-SCALAR-DEPENDENT-PAIR-v1`, source `math-open-problems@ba2e2fbc9d22196f83c4ae35080e7f3d23a55fa1`, which states that if a scalar of density cap `K` is genuinely independent of a pair with joint-density cap `M`, then

`2 beta S C+alpha C^2+2 delta C D+gamma_0 D^2`

has density cap

`3(2MK)^(2/3)|beta^2 gamma_0|^(-1/3)`.                            (6.10)

Substitute `K=1`, `M=2/gamma`, `beta=1`, `gamma_0=d` to obtain (6.4). QED.

Exact coefficient alignment `ell in span{g,beta}` is the special case `K=empty`. The theorem also permits arbitrary extra twist on a genuinely disjoint source block.

## 7. Completed designated partner applied and live splice

The latest **completed** designated-partner theorem used here is fleet03/B18 r28, `QFORM-SCHUR-NULLHUB-TRANSVERSE-COMPILER-v1`, source `math-open-problems@43b16ba3992035298289170540682e8aa62a9ad4`. It proves that in the exact-rank-three Schur-isotropic null-hub packet, if all transverse leverages obey `q_j<=1/2`, then

`||p_Q||_infinity <=3*2^(4/3)[r^2|det D_schur|]^(-1/3)`,           (7.1)

with a continuous `C_0` density. Under the target normalization and `r>=1/2`, this is `<12.927`.

Apply it first. Only a heavy transverse witness `q_i>1/2` survives. Then:

* completed fleet04/B18 r4 pays `|g_i|>=1/64` by `<64.180`;
* Theorem 4 above pays `g_i=0` by `<9.263` with **arbitrary twist**;
* Theorem 6 pays any source-separated/aligned twist by `<12.927`, irrespective of the size of `g_i`.

Thus the remaining exact-null heavy collar must have a genuinely **nonzero tiny edge** `0<|g_i|<1/64` and a **source-entangled non-aligned twist**. This is a strict narrowing of the previous endpoint, not a claim that all exact rank three is solved.

The newest fleet03/B18 r31 artifact available during this run was a checkpoint rather than a completed report. It proves the useful exact residual-pair cap

`||p_(beta_- dot X_-, (g_-/gamma) dot X_-)||_infinity <=2/sqrt(1-q_i)`

for `q_i<1`, and isolates `q_i>3/4` as a near-coloop collar. I do not promote that checkpoint to a completed partner theorem. Theorem 4 above is complementary: it pays the singular endpoint `g_i=0` directly even when `q_i=1`, where that two-dimensional whitening determinant vanishes.

## 8. Correction audit and literature boundary

The proof uses no post-rotation independence. The variables `G,W` in Section 5 are explicitly allowed to be dependent. LPP is used only as an unconditional marginal-density theorem for genuine ORIGINAL-coordinate product blocks. No arbitrary-joint coarea theorem, no conditional-density-cap-as-independence step, no pointwise law-uniform quadratic-phase decay, no moment or support estimate, and no deletion of a small nonzero coefficient occurs.

The pinned `e5f71d79...` `RESULTS`, `FOURIER_ROUTE_REPORT`, and `COUNTEREXAMPLE_SEARCH` were reread. The ruled-surface theorem was applied at the literal inequality (5.8). Search misses were not used as evidence of novelty or truth of the full conjecture.

The full conjecture remains OPEN. The next useful theorem is a **punctured zero-edge interpolation**: control the state `0<|g_i|<1/64` without paying the degenerating physical-pair singular value and without replacing `g_i` by zero. Any solution must exploit the exact rank-one Schur remainder / moving critical value or another product-preserving mechanism through the source-entangled twist.
