SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B13, 2026-09-23T11:00:32Z.
attacking: aggregate two-hub Fourier control with arbitrary diagonal leaf curvature, then the high-density determinant-star / leaf-curvature obstruction.

# fleet02/B13 — diagonal-leaf aggregate Fourier compiler and determinant-star normal form

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: `Extremal product laws`  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **NEW SUPPORTING/TARGET-LEVEL THEOREMS; FULL QFORM OPEN; FULL CONTINUITY OPEN**

## 1. Exact target and first unpaid implication

The target remains: for every finite `n`, every independent real `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` having at least three eigenvalues of absolute value at least one, prove

`P(X^T A X in J) <= C |J|`

with one universal finite `C` for every interval `J`, or produce a valid counterexample. No moment, support, connectedness, log-concavity, identical-law, diagonal-basis, or post-rotation-independence assumption is allowed. Full continuity is a separate target.

The previous B13 run paid an arbitrary-width **exact-null** leaf bank attached to two physical hubs by the aggregate Gram determinant. The unpaid issue was genuine leaf curvature: small nonzero same-leaf-bank coefficients may not be perturbatively deleted because the input supports can be arbitrarily translated and fragmented.

This run proves that *all diagonal leaf curvature is harmless* whenever the physical two-hub cross bank is not concentrated at leverage one. The whole rectangular bank is paid by `det(BB^T)` before reciprocation. The only surviving diagonal-bank endpoint is therefore a quantitative leverage-one / determinant-star configuration. A second three-leaf estimate controls part of that endpoint and converts arbitrary off-diagonal leaf curvature into a graph-domination obstruction.

The first unpaid implication is now `QFORM-DETSTAR-OFFDIAGONAL-GLUE-v1`:

> In a high slab-ratio witness, close the branch where a substantial two-hub cross bank has almost all of its order-two volume on one physical leaf star, the same hub-hub-leaf principal `3x3` block is quantitatively near singular by the designated partner theorem, every transverse nonedge pair dominates the remaining active leaves, and every disjoint fifth cross volume is tiny by pinned D5. Do this without deleting near-null curvature or rotating the independent variables; otherwise construct an actual bounded-finite-union product-indicator counterexample.

## 2. Source-valid completed inputs actually consumed

### 2.1 Designated partner fleet03/B13 r24

Immutable source read at

`yspennstate/math-open-problems@497b7c154292683b23bbbf8563633d84a29ae12b`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B13/20260923T103046Z-fleet03-B13-qform-r24/REPORT.md`.

Its theorem `QFORM-LOCAL-3X3-PRINCIPAL-COMPILER-v1` states: if an original-coordinate principal `3x3` block `P=A[S,S]` has

`sigma_min(P)>=s>0`,

then the full ambient quadratic form, retaining every outside quadratic term, cross coupling and affine term, satisfies

`||p_Q||_inf <= L_*/s`,
`L_* = 128*2^(1/4) = 152.218510720348...`.                     (2.1)

No arbitrary-joint coarea statement is used. In Section 8 below this is applied to the same physical star center produced by the new aggregate theorem.

### 2.2 Required pinned Claude/Fourier package

Immutable source:

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`,
`FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`.

Two proved results are used at equation level.

First, its twisted one-dimensional Fourier lemma says that, for a cap-one density `f`,

`g(s,tau)=int exp(i s x^2+i tau x) f(x) dx`

obeys, uniformly in the quadratic twist `s`,

`int_R |g(s,tau)|^p d tau <= 4 pi / sqrt(p),   p>=2`.            (2.2)

This is the analytic input that makes the aggregate diagonal-leaf theorem below dimension-free: the `sqrt(p)` gain cancels the leverage factors exactly.

Second, its unconditional D5 theorem says that for every disjoint original-coordinate cross block `M=A[I,J]`, with `Z_5=e_5(M^T M)`,

`||p_Q||_inf <= C_5 Z_5^(-1/10)`,
`C_5=5 sqrt(2e)=11.658219907986...`.                              (2.3)

There is no row-marginal condition and all self-block curvature / outside coupling is retained. Section 8 applies it to every high-density witness.

The pinned counterexample search reports no valid counterexample in its tested families; none of those numerics are used as proof here.

## 3. No-attainment reduction to bounded finite-union product indicators

The reduction needed by this slot can be proved directly and does not require an attained bathtub optimizer.

### Proposition 3.1 — `QFORM-FINITE-MIXTURE-PURIFICATION-v2`

Let `K:R^n->[0,1]` be any bounded measurable kernel; in particular take

`K(x)=1_{x^T A x in J}`.

Then

`sup_{independent densities 0<=f_i<=1, int f_i=1} int K(x) prod_i f_i(x_i) dx`

is equal to the supremum over products `prod_i 1_{E_i}` where every `E_i` is a bounded finite union of intervals of Lebesgue measure one.

No optimizer is asserted to exist, and no bound on the locations, diameters, or number of components of the `E_i` is asserted.

#### Proof of the one-marginal finite-mixture lemma

Fix `f`, `0<=f<=1`, `int f=1`, and `epsilon>0`.

1. Choose a bounded interval `I` for which the tail mass `tau=int_{I^c} f` is arbitrarily small. Replace the tail by an indicator of a bounded interval `J subset I^c` of length `tau`. The resulting compactly supported cap-one density `h=f 1_I+1_J` has mass one and differs from `f` in `L^1` by at most `2 tau`.

2. Choose a large integer `N`, partition a bounded interval containing `supp h` into finitely many cells `C_k` of equal length `1/N`, and let `g` be the cell-average conditional expectation of `h`. Then `0<=g<=1`, `int g=1`, and `||g-h||_1 ->0`. Write

`g=sum_k q_k 1_{C_k}`,   `0<=q_k<=1`.

Because each cell has length `1/N` and `int g=1`,

`sum_k q_k=N`.                                                     (3.1)

3. The polytope

`{q in [0,1]^M : sum q_k=N}`

is the hypersimplex: its extreme points are exactly the zero-one vectors with exactly `N` ones. Indeed a point with two fractional coordinates is not extreme, while the integer sum rules out exactly one fractional coordinate. Hence

`q=sum_alpha theta_alpha v^(alpha)`, `theta_alpha>=0`, `sum theta_alpha=1`,

with every `v^(alpha)` having exactly `N` ones. Therefore

`g=sum_alpha theta_alpha 1_{E_alpha}`,                             (3.2)

where each `E_alpha` is the union of exactly `N` grid cells and hence is a bounded finite union of intervals of total measure one.

Thus every cap-one probability density is an `L^1` limit of finite convex mixtures of such unit-measure indicators.

Apply this independently to all `n` marginals. If `g_i` approximates `f_i`, the telescoping product estimate gives

`||prod_i f_i-prod_i g_i||_1 <= sum_i ||f_i-g_i||_1`.             (3.3)

Expand the finite product of the mixtures (3.2). It is a finite convex mixture of product indicators. Since `0<=K<=1`, (3.3) transfers the value of the kernel with arbitrarily small loss, and one mixture component is at least the mixture average. The reverse inequality is trivial because indicators are admissible densities. QED.

This is exactly the transfer used below: bounded slabs can be studied on bounded finite-union product sets without assuming one centered interval, one connected support, bounded diameter, fixed fragment count, or a global attained optimizer.

## 4. Aggregate theorem for a two-hub bank with arbitrary diagonal leaf curvature

### Theorem 4.1 — `QFORM-DIAGONAL-LEAF-AGGREGATE-v1`

Let

`U=(U_1,U_2) in R^2`, `V=(V_1,...,V_m)`

be disjoint banks of original coordinates, all scalar coordinates independent and having probability densities at most one. Let `Z` denote any remaining independent coordinates. Let `B=[b_1 ... b_m]` be a real `2 x m` matrix of rank two and consider

`Q = F(U,Z)
     + sum_{j=1}^m [ d_j V_j^2 + (2 b_j dot U + c_j(Z)) V_j ]`,     (4.1)

where `F,c_j` are arbitrary measurable functions and `d_j` are arbitrary real numbers.

Thus the selected leaves may have arbitrary diagonal quadratic curvature, but no mutual `V_j V_k` terms. Put

`G=BB^T`,
`ell_j=b_j^T G^(-1)b_j`,
`h=max_j ell_j`.                                                   (4.2)

Then `0<=ell_j<=1` and `sum_j ell_j=2`. If `h<1`, then for every

`max(1,2h) <= q < 2`                                               (4.3)

one has a continuous density and

`boxed:
 ||p_Q||_inf <= [4 / ((2-q) sqrt(q))] det(G)^(-1/4).
`                                                                    (4.4)

Optimizing over the permitted `q` gives

`boxed:
 h<=1/2  =>  ||p_Q||_inf <= 4 det(BB^T)^(-1/4),
`                                                                    (4.5)

and

`boxed:
 1/2<h<1 => ||p_Q||_inf
 <= [2 / ((1-h) sqrt(2h))] det(BB^T)^(-1/4).
`                                                                    (4.6)

The constants do not depend on the number `m` of leaves. In particular, arbitrarily fragmented order-two cross volume is paid in aggregate before inversion.

### Proof

Fix `Z=z`. For each leaf define its twisted Fourier transform

`g_{j,t}(tau)
 = int exp(i t d_j v^2+i tau v) f_{V_j}(v) dv`.                    (4.7)

Integrating the independent leaves first and discarding only unimodular phases gives

`|phi_z(t)|
 <= int_R2 f_{U_1}(u_1)f_{U_2}(u_2) H_{t,z}(u) du`,               (4.8)

where

`H_{t,z}(u)
 = prod_j |g_{j,t}(2t b_j dot u+t c_j(z))|`,
`0<=H_{t,z}<=1`.                                                   (4.9)

The joint physical hub density

`F_U(u)=f_{U_1}(u_1)f_{U_2}(u_2)`

has mass one and is bounded by one. Hence for `q>=1`, with the usual `q'=infinity` interpretation at `q=1`,

`|phi_z(t)| <= ||F_U||_{q'} ||H_{t,z}||_q <= ||H_{t,z}||_q`.      (4.10)

This step keeps the original-coordinate product structure; no transformed random coordinates are declared independent.

Now normalize only inside the deterministic integral. Put

`a_j=G^(-1/2)b_j`, `ell_j=||a_j||^2`,
`v_j=a_j/sqrt(ell_j)` for `ell_j>0`.                               (4.11)

Then

`sum_j ell_j v_j v_j^T=I_2`,                                     (4.12)

so the one-dimensional maps `v_j dot y` with weights `ell_j` are geometric Brascamp-Lieb data. Also `ell_j<=1`, because

`I_2-a_j a_j^T=sum_{k!=j} a_k a_k^T >=0`.                         (4.13)

Make the analytic change of integration variable `y=G^(1/2)u`. It has Jacobian `det(G)^(-1/2)` and

`b_j dot u=sqrt(ell_j) v_j dot y`.                                (4.14)

For a fixed `q` satisfying (4.3), set

`p_j=q/ell_j >=2`

and

`F_j(r)=|g_{j,t}(2t sqrt(ell_j) r+t c_j(z))|^(q/ell_j)`.           (4.15)

The pinned twisted estimate (2.2) yields

`int F_j(r) dr
 <= [1/(2|t|sqrt(ell_j))] * [4pi/sqrt(q/ell_j)]
 = 2pi/(|t|sqrt(q)).`                                             (4.16)

The cancellation of `ell_j` in (4.16) is the crucial point. Applying geometric Brascamp-Lieb to (4.12), and using `sum ell_j=2`, gives

`int_R2 H_{t,z}(u)^q du
 <= det(G)^(-1/2) [2pi/(|t|sqrt(q))]^2
 = det(G)^(-1/2) 4pi^2/(q |t|^2).`                               (4.17)

Consequently

`|phi_z(t)|
 <= K_q |t|^(-2/q)`,

`K_q=det(G)^(-1/(2q)) (4pi^2/q)^(1/q)`.                           (4.18)

The estimate is uniform in `z`, all diagonal twists `d_j`, all affine terms, and the arbitrary hub/outside phase `F`, so the same bound holds for the unconditional characteristic function. Together with `|phi(t)|<=1`,

`|phi(t)| <= min(1,K_q |t|^(-alpha))`, `alpha=2/q>1`.              (4.19)

Thus `phi` is integrable. If `a=K_q^(1/alpha)=K_q^(q/2)`, then

`int_R min(1,K_q |t|^(-alpha)) dt
 = 2 a alpha/(alpha-1).`                                          (4.20)

Fourier inversion gives

`||p_Q||_inf
 <= [alpha/(pi(alpha-1))] K_q^(1/alpha)
 = [4/((2-q)sqrt(q))] det(G)^(-1/4),`                             (4.21)

which is (4.4). Since the inverse Fourier transform is absolutely convergent, this branch in fact has a continuous density.

For `h<=1/2`, take `q=1`, giving (4.5). For `h>1/2`, the function `4/((2-q)sqrt(q))` is increasing for `q>=1`, so take `q=2h`, giving (4.6). QED.

### Original-matrix form

Let `H={h_1,h_2}` and `T` be disjoint original-coordinate sets with `|H|=2`, and suppose `A[T,T]` is diagonal. Condition all original coordinates outside `H union T`. Then (4.1) holds with

`B=A[H,T]`.                                                       (4.22)

Therefore Theorem 4.1 applies directly to the full ambient quadratic form. All hub-hub curvature, outside curvature/couplings, and affine leakage remain present in `F` and `c_j`.

## 5. Determinant-star identity and the high-density diagonal-bank normal form

The leverage parameters in Theorem 4.1 have a useful exact physical interpretation.

### Lemma 5.1 — `QFORM-TWOHUB-LEVERAGE-STAR-IDENTITY-v1`

For a rank-two `2 x m` matrix `B=[b_1 ... b_m]`, write

`D=det(BB^T)>0`, `Delta_{jk}=det(b_j,b_k)`.

Then for every column `j`,

`boxed:
 sum_{k!=j} Delta_{jk}^2 = ell_j D,
`                                                                    (5.1)

and

`boxed:
 sum_{r<s; r,s!=j} Delta_{rs}^2 = (1-ell_j) D.
`                                                                    (5.2)

#### Proof

Cauchy-Binet gives

`D=sum_{r<s} Delta_{rs}^2`.                                       (5.3)

Delete column `j`; its Gram matrix is `G-b_j b_j^T`. The matrix determinant lemma gives

`det(G-b_j b_j^T)=det(G)(1-b_j^T G^(-1)b_j)=D(1-ell_j)`.          (5.4)

A second application of Cauchy-Binet identifies the left side of (5.4) with the sum in (5.2). Subtract from (5.3) to obtain (5.1). QED.

Thus `ell_j` is exactly the volume-sampling marginal of column `j`: it is the fraction of total squared `2x2` cross volume carried by pairs containing `j`.

### Corollary 5.2 — `QFORM-DIAGLEAF-DETSTAR-NORMALFORM-v1`

Let a slab `J` have ratio

`R=P(Q in J)/|J|`.                                                 (5.5)

For any two-hub / diagonal-leaf bank with `D=det(BB^T)>0`, let `h=max ell_j`.

If `h<=1/2`, Theorem 4.1 forces

`boxed: D <= (4/R)^4.`                                             (5.6)

If `h>1/2`, choose `j_*` with `ell_{j_*}=h`. Then

`boxed:
 (1-h) sqrt(2h) D^(1/4) <= 2/R.
`                                                                    (5.7)

In particular,

`boxed:
 sum_{r<s; r,s!=j_*} Delta_{rs}^2
 =(1-h)D
 <= 2 D^(3/4)/(R sqrt(2h))
 <= 2 D^(3/4)/R,
`                                                                    (5.8)

whereas the star centered at `j_*` carries

`boxed:
 sum_{k!=j_*} Delta_{j_*k}^2 = hD > D/2.
`                                                                    (5.9)

So if a hypothetical sequence has slab ratios `R_m -> infinity` while a diagonal two-hub bank has `D_m` bounded below, then its order-two cross volume is forced into a single physical **determinant star**: `h_m->1`, all non-star squared minors are `o(1)` relative to the appropriate scale, while more than half the total volume remains on the star.

This is an aggregate statement. It does not select one minor before taking a reciprocal and therefore is insensitive to arbitrarily many fragmented star spokes.

## 6. The leverage-one endpoint: a three-leaf diagonal-twist estimate

The aggregate theorem necessarily loses integrability as `h->1` because its Fourier exponent tends to one. A complementary physical estimate closes any endpoint that still contains three individually usable uncoupled leaves.

### Theorem 6.1 — `QFORM-THREELEAF-DIAGONAL-TWIST-v1`

Let `U=(U_1,U_2)` and `V_1,V_2,V_3` be five distinct original coordinates, all independent with densities at most one, and condition all remaining coordinates `Z`. Suppose the three selected leaves have no mutual off-diagonal curvature. Thus

`Q=F(U,Z)+sum_{j=1}^3 [d_j V_j^2+(2b_j dot U+c_j(Z))V_j]`.         (6.1)

If

`Delta=|det(b_1,b_2)|>0`, `b_3!=0`,                               (6.2)

then

`boxed:
 ||p_Q||_inf
 <= 3*2^(1/6) (Delta ||b_3||_2)^(-1/3)
 =3.367386144928... (Delta ||b_3||_2)^(-1/3).
`                                                                    (6.3)

The same statement holds after any permutation of the three leaves.

#### Proof

For fixed `z` define

`G_{j,t}(s)=int f_{V_j}(v) exp(i t d_j v^2+i s v) dv`.             (6.4)

By Plancherel and `0<=f_j<=1`, `int f_j=1`,

`int |G_{j,t}(s)|^2 ds=2pi int f_j(v)^2 dv <=2pi`.                (6.5)

After integrating the leaves and dropping the arbitrary hub phase,

`I(t)=|phi_z(t)|
 <= int f_{U_1}(u_1)f_{U_2}(u_2) prod_{j=1}^3
       |G_{j,t}(2t b_j dot u+t c_j(z))| du`.                       (6.6)

Cauchy-Schwarz splits this into

`I(t)^2 <= A_12(t) B_3(t)`,                                       (6.7)

where

`A_12=int |G_1(...)|^2 |G_2(...)|^2 du`,                          (6.8)

and

`B_3=int f_{U_1}^2 f_{U_2}^2 |G_3(...)|^2 du`.                    (6.9)

The physical map

`u -> (2t b_1 dot u,2t b_2 dot u)`

has Jacobian `4|t|^2 Delta`, so (6.5) gives

`A_12(t) <= pi^2/(|t|^2 Delta)`.                                  (6.10)

For the second factor, `f_{U_i}^2<=f_{U_i}`. The linear form `Y=b_3 dot U` has density at most

`1/max(|(b_3)_1|,|(b_3)_2|) <= sqrt(2)/||b_3||_2`:               (6.11)

indeed one scaled summand has that density cap, and convolution with the other probability law cannot raise it. Hence another change of variable plus (6.5) gives

`B_3(t) <= sqrt(2) pi/(|t| ||b_3||_2)`.                           (6.12)

Therefore

`|phi(t)|
 <= min(1,
   2^(1/4) pi^(3/2)
   (Delta ||b_3||_2)^(-1/2) |t|^(-3/2)).`                         (6.13)

If the coefficient of `|t|^-3/2` is `K`, direct integration gives

`int_R min(1,K|t|^-3/2)dt=6K^(2/3)`.                             (6.14)

Fourier inversion yields (6.3). No random-coordinate rotation has occurred. QED.

## 7. Off-diagonal leaf curvature becomes a domination obstruction

Fix a physical hub pair `H={h_1,h_2}`. For every other original coordinate `j`, write

`b_j=A[H,{j}] in R^2`.                                            (7.1)

On the leaf vertices define the curvature graph `G_leaf`: vertices `j,k` are adjacent exactly when `A_{jk}!=0`.

For any three vertices `j,k,l` that are pairwise nonadjacent, their `3x3` leaf subblock is diagonal, so Theorem 6.1 applies. Thus a slab witness of ratio `R` necessarily satisfies

`boxed:
 |det(b_j,b_k)| ||b_l||_2
 <= (3*2^(1/6)/R)^3
`                                                                    (7.2)

for every ordering with `det(b_j,b_k)!=0`.

Equivalently, choose any threshold

`delta > 3*2^(1/6)/R`.                                            (7.3)

Call a leaf `delta`-active if `||b_j||_2>=delta`. If `j,k` are a nonadjacent active pair with

`|det(b_j,b_k)|>=delta^2`,                                       (7.4)

then **every other delta-active leaf is adjacent to `j` or to `k`**. Otherwise a third active leaf `l` nonadjacent to both would be pairwise nonadjacent with `j,k`, and the left side of (7.2) would be at least `delta^3`, contradicting (7.3).

Hence any transverse physical nonedge is automatically a two-vertex dominating set for the active leaf-curvature graph. This is a concrete product-preserving obstruction to a counterexample with sparse genuine leaf-leaf curvature.

## 8. Applying the completed partner theorem and pinned D5 to the same survivor

Let `R=P(Q in J)/|J|` be any slab ratio.

### Partner r24: every physical principal triple is near singular

From (2.1), for every original-coordinate triple `S`,

`boxed:
 sigma_min(A[S,S]) <= L_*/R,
 L_*=128*2^(1/4).
`                                                                    (8.1)

In particular, if Corollary 5.2 produces a determinant-star center `j_*` for a hub pair `H`, then the **same physical triple** satisfies

`boxed:
 sigma_min(A[H union {j_*},H union {j_*}]) <= L_*/R.
`                                                                    (8.2)

Thus the leverage-one endpoint cannot merely be called “one heavy leaf”: its heavy leaf is anchored to a quantitatively near-singular physical `3x3` hub block.

### Pinned D5: every physical fifth cross volume is tiny

From (2.3), for every disjoint original-coordinate cut `I,J`, with `M=A[I,J]`,

`boxed:
 e_5(M^T M)
 <= (5 sqrt(2e)/R)^10.
`                                                                    (8.3)

So a genuine diverging counterexample sequence would simultaneously have:

* all physical principal `3x3` blocks tending to singularity at rate `O(1/R)`;
* every physical disjoint fifth cross volume tending to zero at rate `O(R^-10)`;
* every substantial diagonal two-hub leaf bank collapsing to a one-center determinant star by (5.7)-(5.9);
* every transverse nonedge pair dominating all remaining active leaves by Section 7.

These conclusions use the partner and pinned results as actual inequalities, not merely as citations.

## 9. Why this advances the previous two-hub leaf-curvature gap

The preceding exact-null-bank theorem paid

`A[T,T]=0`

by the entire aggregate determinant `det(BB^T)`. It left open the possibility that even tiny leaf self-curvature could destroy the direct conditional linear-form proof on unbounded fragmented supports.

Theorem 4.1 removes that concern for **arbitrary diagonal leaf curvature**. Its proof never declares the normalized variables `G^(1/2)U` independent; the normalization is only an analytic change of integration variable after the physical product density has been handled by Holder. The quadratic leaf terms appear solely through the pinned twisted Fourier transforms, where their size and signs disappear from (2.2).

The remaining obstruction is now sharply localized:

1. diagonal leaf banks with leverage bounded away from one are paid dimension-free by their aggregate Gram determinant;
2. if aggregate determinant survives at high slab ratio, its `2x2` volume becomes a physical determinant star with one leverage tending to one;
3. any individually nonfragmented three-leaf endpoint is paid by Theorem 6.1;
4. any attempt to avoid mutually uncoupled leaves forces the genuine off-diagonal curvature graph into the domination pattern of Section 7;
5. the star center's physical hub triple is simultaneously near singular by the designated partner compiler, while all fifth cross volume is tiny by D5.

This is substantially narrower than “arbitrary nonzero leaf curvature”. What is still missing is a product-compatible compiler for the near-singular central `3x3` star plus its off-diagonal leaf-curvature spokes. Small coefficients cannot be deleted as perturbations of random variables on arbitrary translated supports.

## 10. Geometric/product-set interpretation

For product-indicator inputs `f_i=1_{E_i}`, `|E_i|=1`, Theorems 4.1 and 6.1 are literal geometric sublevel-set estimates. For example Theorem 4.1 gives

`|{x in prod E_i : x^T A x in J}|
 <= [4/((2-q)sqrt(q))] det(BB^T)^(-1/4) |J|`.                    (10.1)

Proposition 3.1 transfers this inequality back to arbitrary cap-one marginals with zero constant loss. The transfer preserves arbitrarily remote translations, separated fragments, and unbounded original supports in the limit; it assumes neither a centered interval nor an attained global bathtub optimizer.

## 11. Status

New proved results in this run:

* `QFORM-FINITE-MIXTURE-PURIFICATION-v2` — self-contained no-attainment product-indicator reduction.
* `QFORM-DIAGONAL-LEAF-AGGREGATE-v1` — dimension-free aggregate two-hub bound with arbitrary diagonal leaf curvature whenever max leverage `<1`.
* `QFORM-TWOHUB-LEVERAGE-STAR-IDENTITY-v1` — exact physical volume-sampling identity.
* `QFORM-DIAGLEAF-DETSTAR-NORMALFORM-v1` — high-density diagonal banks force a one-center determinant star.
* `QFORM-THREELEAF-DIAGONAL-TWIST-v1` — complementary leverage-one endpoint bound for any usable uncoupled physical triple.
* `QFORM-TWOHUB-LEAFCURVATURE-DOMINATION-v1` — every transverse nonedge pair dominates all sufficiently active leaves in a high-density witness.

Completed external results actually applied:

* designated partner fleet03/B13 r24 physical principal-`3x3` compiler, yielding (8.1)-(8.2);
* pinned `e5f71d79...` twisted `L^p` lemma, used centrally in (4.16), and D5, yielding (8.3).

The full arbitrary-dimensional conjecture is **OPEN / NOT PROVED / NOT DISPROVED**. No valid counterexample is produced here. Full continuity remains separate, although the two new Fourier branches individually have continuous densities because their characteristic functions are integrable.

Independent end-to-end review status: **NOT INDEPENDENTLY END-TO-END REVIEWED**.
