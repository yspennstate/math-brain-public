SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B05, 2026-09-23T19:24:28Z.
attacking: the near-coloop two-sheet coarea loss by isolating exactly what changes if one transverse square is carried by an independent original-coordinate bank; prove an arbitrary-Borel dyadic receiver and a full density bound before returning to the same-source overlap.

# fleet01/B05 auto15 — support-separated square receiver, arbitrary same-bank shear, and the remaining same-source obstruction

**Programme:** `QFORM-DENSITY-3EIG-20260922`.  
**Assignment:** quadratic coarea bound.  
**Status:** `NEW SUPPORTING THEOREM / ARBITRARY-BOREL DYADIC LEMMA / PRECISE MISSING FACTOR IDENTIFIED / FULL QFORM OPEN`.  
**Regularity:** the theorem below gives a bounded continuous density on its stated support-separated branch; unrestricted full-target continuity remains OPEN.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Why change the mechanism

The preceding B05 run proved an exact Pluecker-currency identity and, in the diffuse mixed-shear branch, obtained

`||p_Q||_infinity < 35.51 rho^(-1/6)`.

That left `QFORM-NEARCOLOOP-RHO-SIXTH-ROOT-RECOVERY-v1`: remove the last vanishing longitudinal-volume loss. Fresh source work now sharpens the obstruction. The current frontier addendum proves a two-light coarea estimate when there is no genuinely third overlapping light projection and a two-bank nonlinear chirp estimate for one special overlapping family. It also records that an arbitrary affine shear `dL` can create an `a r^2 log(1/r)` saddle tube, so the earlier strict `O(a r^2)` tube benchmark cannot be used uniformly in that enlarged scope.

This run therefore asks a narrower but decisive question: **is the affine/shear term itself the obstruction, or is the obstruction specifically that the transverse square shares the same original-coordinate source as the near-null linear form?** The answer below is: the shear is not the obstruction. If the square has an independent original-coordinate bank, even an arbitrary measurable same-bank remainder can be tolerated with a dimension-free continuous-density bound.

## 2. A sharp one-dimensional square `L^{3/2}` estimate

### Lemma 2.1
Let `V` have a probability density bounded by `K_V<infinity`. For `lambda != 0` and `gamma in R`, let

`Z = lambda V^2 + gamma V`.

Then `Z` has a density `g_Z` satisfying

`||g_Z||_(3/2) <= 2 K_V^(2/3) |lambda|^(-1/3)`.              (2.1)

#### Proof
Complete the square. Translation of `V` and translation of `Z` do not change density caps or `L^{3/2}` norms, so it is enough to treat `Z=lambda W^2`, where `W` has density cap `K_V`.

First assume `K_V=1` and `lambda=1`. On `z>0`,

`g(z) = [f_W(sqrt z)+f_W(-sqrt z)]/(2 sqrt z) <= z^(-1/2)`.

Hence

`int g(z)^(3/2) dz <= int g(z) z^(-1/4) dz = E |W|^(-1/2)`.   (2.2)

The cap-one assumption alone gives the exact layer-cake estimate

`E |W|^(-1/2)
 = int_0^infinity P(|W| < t^(-2)) dt
 <= int_0^infinity min(1, 2 t^(-2)) dt
 = 2 sqrt(2)`.                                                (2.3)

Therefore `||g||_(3/2) <= (2 sqrt2)^(2/3)=2`.

For general `K_V`, apply the cap-one estimate to `K_V W`; for general `lambda`, use the scaling law `||p_(aY)||_q=|a|^(-1+1/q)||p_Y||_q`. This gives (2.1). QED.

No interval support, connected support, moment, or regularity assumption was used.

## 3. The support-separated square Young receiver

### Theorem 3.1 — `QFORM-SUPPORT-SEPARATED-SQUARE-YOUNG-v1`
Let `H`, `V`, and a random bank `G` be mutually independent. Assume

`||f_H||_infinity <= K_H`,
`||f_V||_infinity <= K_V`.

Let `T=T(G)` be any real random variable with a density satisfying

`||f_T||_infinity <= K_T`,

and let `R=R(G)` be **any measurable real function of the same bank**, with no density, moment, support, smoothness, or independence assumption relative to `T`. Let `t lambda != 0`, and define

`Q = 2 t H T + R + lambda V^2 + gamma V + c`.                 (3.1)

Then `Q` has a bounded continuous density and

`boxed(||p_Q||_infinity
 <= 6 (K_H K_T K_V)^(2/3) |t|^(-2/3) |lambda|^(-1/3).)`       (3.2)

Equivalently, the coefficient dependence is exactly `|t^2 lambda|^(-1/3)`.

#### Proof
Complete the square in `V`; the deterministic resulting constant is absorbed into `c`. Condition on the entire bank `G`. For a realized value `T=l !=0`, the two remaining random summands

`Y_l=2 t l H`,
`Z=lambda V^2+gamma V`

are independent. Since `f_H<=K_H` and has mass one,

`||f_H||_3^3 <= K_H^2`,

and therefore

`||p_(Y_l)||_3 <= K_H^(2/3) (2|t l|)^(-2/3).`                 (3.3)

Lemma 2.1 gives

`||p_Z||_(3/2) <= 2 K_V^(2/3)|lambda|^(-1/3).`                (3.4)

Young's convolution inequality with exponents `3` and `3/2` yields, uniformly in the arbitrary conditioned shift `R(G)+c`,

`||p_(Q|G)||_infinity
 <= 2^(1/3) K_H^(2/3) K_V^(2/3)
    |t|^(-2/3)|lambda|^(-1/3)|T|^(-2/3).`                    (3.5)

Because `T` has a density, `P(T=0)=0`. Its negative `2/3` moment is bounded using only the density cap:

`E |T|^(-2/3)
 = int_0^infinity P(|T| < u^(-3/2)) du
 <= int_0^infinity min(1, 2 K_T u^(-3/2)) du
 = 3*2^(2/3) K_T^(2/3).`                                     (3.6)

Averaging (3.5) and multiplying the constants gives exactly (3.2), because

`2^(1/3) * 3*2^(2/3) = 6`.

For continuity, for every conditioned `l !=0`, `p_(Y_l) in L^3` and `p_Z in L^(3/2)`, so their convolution is continuous by translation continuity in `L^(3/2)` and Holder. Its supremum is dominated by the integrable right side of (3.5). Dominated convergence over `G` therefore supplies a continuous representative of the unconditional density. QED.

### Important scope
The arbitrary term `R(G)` may contain, for example,

`beta T^2 + 2 epsilon T P(G) + R_0(G)`,

with **arbitrary** same-bank `P(G)` and arbitrary measurable `R_0(G)`. Thus a third same-bank shear in the *remainder* is harmless as long as the transverse square variable `V` comes from an independent source bank. No conditional density of `P` is used.

This theorem is not the full QFORM theorem because the hard diffuse near-coloop configuration has the square direction and the linear/shear directions supported on the same original coordinates.

## 4. Arbitrary-Borel curved dyadic lemma, uniform in the affine shear

The fresh correction shows that a strict interval-tube estimate `O(a r^2)` can fail after adding an arbitrary `dL`, with a genuine `a r^2 log(1/r)` saddle. The following weaker Borel estimate survives every such shear and is already summable after the usual `1/|L|` coarea weight.

### Lemma 4.1 — `QFORM-SUPPORT-SEPARATED-BOREL-SQUARE-DYADIC-v1`
Let `V` be independent of a bank `G`, with `||f_V||_infinity<=K_V`. Let `T=T(G)` have density cap `K_T`, and let `R=R(G)` be arbitrary. Fix `t lambda !=0`. For every Borel set `A subset R` of finite Lebesgue measure `a=|A|` and every `r>0`,

`P( r<=|T|<=2r,
    R/(2tT) + (lambda V^2+gamma V)/(2tT) in A )
 <= 8 K_T K_V sqrt(|t|/|lambda|) r^(3/2) sqrt(a).`            (4.1)

The estimate is uniform over `R`; in particular `R` may include an arbitrarily large affine shear in `T` and an arbitrary same-bank term `2 epsilon T P(G)`.

#### Proof
Complete the square in `V` and absorb the resulting deterministic term into `R`. Condition on `G`, so `T=l` and `R=r_0` are fixed. The event in (4.1) requires

`W^2 in E_l`

for a Borel set whose Lebesgue measure is

`|E_l| = (2|t l|/|lambda|) a`.                                (4.2)

If `W` has density cap `K_V`, then for every Borel `E`,

`P(W^2 in E) <= 2 K_V sqrt(|E|)`.                              (4.3)

Indeed, after scaling to cap one, the square density is bounded by `z^(-1/2)` and the integral of this decreasing kernel over a set of measure `m` is at most `2 sqrt(m)`.

On the shell, `|l|<=2r`, so (4.2)-(4.3) give a conditional probability at most

`4 K_V sqrt(|t| r a/|lambda|)`.

Also `P(r<=|T|<=2r)<=2K_T r`. Multiplication gives (4.1). QED.

This is deliberately a **Borel-set** statement, not an interval-only frozen-slice estimate. It therefore does not commit the interval-to-Borel error already corrected elsewhere in the fleet.

## 5. Concrete target-valid family and what the theorem actually removes

Take an independent physical hub `H`, an arbitrary independent product bank `G`, and a further independent square bank giving a scalar projection `V`. Let `L=L(G)` and `P=P(G)`. Consider

`Q_epsilon = 2 H L + 2 epsilon L P + V^2`.                     (5.1)

In spectral coordinates `(H,L,P,V)`, when `L` and `P` are orthonormal and the only displayed terms are retained, the homogeneous matrix is

`[[0,1,0,0],
  [1,0,epsilon,0],
  [0,epsilon,0,0],
  [0,0,0,1]]`.

Its nonzero eigenvalues are

`1, +sqrt(1+epsilon^2), -sqrt(1+epsilon^2)`,

so it satisfies the exact three-large-eigenvalue target for every epsilon.

Theorem 3.1 applies with `R(G)=2 epsilon L P`, `t=lambda=1`. It gives

`||p_(Q_epsilon)||_infinity
 <= 6 (K_H K_L K_V)^(2/3)`                                    (5.2)

uniformly in `epsilon`, in the dimension of the bank, in the law of `P`, and in arbitrary additional measurable same-bank terms added to `R(G)`.

If `H` is a physical cap-one coordinate and `L,V` are unit linear projections of disjoint cap-one product banks, the standard scalar projection cap gives `K_L,K_V<=sqrt2`, hence

`||p_(Q_epsilon)||_infinity <= 6*2^(2/3) < 9.525`.             (5.3)

If `L` and `V` themselves are physical cap-one coordinates, the bound is simply `6`.

Therefore the near-null shear `2 epsilon LP` is **not by itself** the source of the rho-loss. The difficult factor is precisely that in the genuine diffuse survivor the variable carrying the square cannot be separated from the original coordinates carrying `L` and `P`.

## 6. Required fleet02/B05 theorem applied to an actual inequality

The newest completed partner report `fleet02/B05`, canonical mathematics

`yspennstate/math-open-problems@fcb8ba61036bee6535de7b0fb0077bb07d76bea6:proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B05/20260923T184914Z-fleet02-B05-QFORM-auto11c/REPORT.md`,

proves for a physical triple

`M=[[a,b,e],[b,0,c],[e,c,0]], c!=0`

that

`||p_Q||_infinity <= 8*2^(1/4) (|det M| |c|)^(-1/4)`.         (6.1)

Apply it to the target-valid control

`Q_control = V^2 + 2 H L`,

using the physical ordering `(V,H,L)`. Then

`M=[[1,0,0],[0,0,1],[0,1,0]]`,
`det M=-1`, `c=1`, and `spec(M)={1,1,-1}`.

Thus the partner theorem gives the concrete full-line inequality

`boxed(||p_(Q_control)||_infinity
 <= 8*2^(1/4)=9.513656920...).`                                (6.2)

Our Theorem 3.1 independently gives the sharper value `6` when all three displayed variables are physical cap-one coordinates. The point of (6.2) is not constant optimization: it verifies at the exact three-eigenvalue endpoint that the partner's pair-log/Schur mechanism and the present Young/coarea mechanism meet on the same valid control, while the unresolved case begins only when the square ceases to be an independent source bank.

## 7. Relation to the newest completed fleet receivers

Fresh source review found three relevant facts, all preserved at their exact scopes.

1. The new independent-square-bank theorem allows arbitrary-rank quadratic remainder but pays a half-potential of that remainder. Theorem 3.1 is complementary: it allows **arbitrary measurable** same-bank `R(G)` but exploits the explicit bilinear hub `2tHT` and a scalar density cap on `T`.

2. The fresh two-light coarea theorem gives

`||p_(2tHL+beta L^2+2 epsilon LV+lambda V^2)||_infinity
 <= 1/2 + 4sqrt2 M/(|t|sqrt|lambda|)`

for a joint density cap `M` of `(L,V)`. It does not contain a genuinely third overlapping projection `P`.

3. The fresh two-bank nonlinear-chirp factorization proves a special same-source overlapping family uniformly by exploiting a two-bank algebraic factorization. That result is stronger than Theorem 3.1 on its own structured family, but it does not supply the general same-source replacement needed for the arbitrary diffuse frame.

The present result therefore closes a different interface: **arbitrary same-bank remainder plus independent square bank**, with no positive conditional-density moment and no interval-to-Borel promotion.

## 8. Exact first unpaid implication

The support-separated theorem removes the shear, rough support, and Borel-profile issues simultaneously. What it cannot survive is replacing the independent square source by a simultaneous linear form of the same product bank as `T`.

The first unpaid implication is therefore sharpened to

`QFORM-SAME-SOURCE-SQUARE-YOUNG-REPLACEMENT-v1`:

> In the diffuse near-coloop product frame, replace the independent convolution step
> `L^3(2tTH) * L^(3/2)(lambda V^2)`
> by a product-preserving estimate when `(T,V,P)` are simultaneous linear forms of the same independent rough coordinates. The estimate must retain enough original-coordinate factorization to avoid the known `int p_T^(1/3)` Renyi/fiber loss and must be uniform as the longitudinal Gram mass `rho->0`.

Equivalently, one needs a same-source substitute for either Lemma 2.1 **inside the conditional bank** or for the Borel square estimate (4.3) after conditioning only information that does not destroy the transverse smoothing. Generic joint-density caps, X-ray bounds, conditional-density suprema, and interval-only square-root profiles are all insufficient by current corrections.

This also explains the preceding `rho^(-1/6)` projected-crossing loss: if one can carve out a genuinely independent transverse square bank with cap `O(1)`, Theorem 3.1 pays the entire moving shear at no `rho` cost. Hence the remaining factor is an **independence/source-incidence deficit**, not missing determinant currency and not the affine-shear saddle by itself.

## 9. Scope and status

No Gaussianity, log-concavity, moment, compact support, connected support, diagonal basis, or independence after rotation is used. All independence invoked in Theorem 3.1 is explicitly an original-source-bank hypothesis and is therefore a scoped supporting theorem, not a hidden assumption in the full target.

The unrestricted QFORM conjecture remains `OPEN_NOT_PROVED_NOT_DISPROVED`. The unrestricted continuous-density conclusion remains OPEN. The support-separated theorem here has a bounded continuous density.

Sources consumed before publication include the live QFORM controls/corrections, the preceding B05 Pluecker/projected-crossing report, the newest fleet02/B05 double-zero Schur closure, the newest Claude `hub that sees P` continuation, the corrected independent-square-bank theorem, the two-light coarea addendum, and the fresh affine-shear tube correction. Repository transport was used; no native brain receiver use was verified, so execution remains `WITHOUT_VERIFIED_BRAIN`.
