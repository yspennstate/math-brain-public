SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B11, 2026-09-23T16:13:53Z.
attacking: the collision-critical heavy-frame collar: derive a quantitative near-coloop or paid disjoint-bank alternative without a tiny physical minor.

# fleet03/B11 r36 — 8-sample collision stability and a true-near-coloop two-bank splitter

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** indefinite signatures `(2,1)` and `(1,2)`  
**Status:** `NEW STRUCTURAL THEOREMS / DESIGNATED PARTNER APPLIED / NON-NEARCOLOOP EXACT-RANK3 COLLAR PAID / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.


The unrestricted owner conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. This report works first in exact rank three and then sharpens the remaining true-near-coloop geometry. Arbitrary additional nonseparable spectrum is still a separate bridge.

## 1. Source-pinned inputs actually used

### Own predecessor r35

`yspennstate/math-open-problems@32a96eb18f2b23de67a15d846a56ccb3d998d889`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B11/20260923T152023Z-fleet03-B11-QFORM-r35/REPORT.md`.

For an exact-rank-three factorization

`A=R M R^T`, `R^T R=I_3`, `s=min |lambda(M)|`,

r35 defined the determinantal triple law

`v_K=det(R_K)^2`, `sum_K v_K=1`,

one- and two-point marginals

`c_i=||r_i||^2`, `g_ij=||r_i wedge r_j||^2`,

and collision energies

`C2=sum_i c_i^2`, `G2=sum_{i<j}g_ij^2`, `V2=sum_K v_K^2`.

For iid triples `K,L~v`, with `D=P(K cap L=empty)`, it proved

`D=1-C2+G2-V2`.                                                (1.1)

It also paid `C2<=3/4` by a literal original-coordinate rank-three cross cut and `C2>=5/4` by a physical pair-area receiver, leaving the collision collar `3/4<C2<5/4`.

### Designated partner fleet04/B11 r6

`yspennstate/math-open-problems@30555c1ca97752e10f5089ccd95f8514c704be5a`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B11/20260923T131400Z-fleet04-B11-extension-mass-r6/REPORT.md`.

For every physical pair `S`, with `g_S=||r_i wedge r_j||^2`, the partner proves the exact extension-mass identity

`W_2(S)=|det M|^2 [g_S^2-sum_{K contains S}v_K^2]`,             (1.2)

and the full-line pair-area bound

`||p_Q||_infinity <=128 sqrt(2)/(s sqrt(g_S))`.                 (1.3)

I apply (1.2) below to identify an exact probability in the determinantal triple law, and apply (1.3) at a concrete numerical threshold.

### Existing near-coloop sources

The current non-near-coloop exact-rank-three collar is independently paid by fleet03/B10 at

`yspennstate/math-open-problems@cecdb7eb0dc66a6e379225ed8ecef7417a3668b2`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B10/20260923T041602Z-fleet03-B10-QFORM-r23/REPORT.md`.

That source also identifies the true-near-coloop survivor after its transverse-heavy exit: one physical hub with leverage `c>63/64`; after the scalar-pivot exit its normalized hub Rayleigh coefficient is small; and every residual transverse leverage is `<1/4`.

For one-heavy/two-transverse-bank small-ball smoothing I also use the completed fleet03/B13 theorem

`yspennstate/math-open-problems@eac866b378f5c54411a55f7eb49f89336a4701ae`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B13/20260922T213118Z-fleet03-B13-qform-r17/REPORT.md`.

Its theorem is used only in its stated original-coordinate bank scope.

## 2. Intersection-count bookkeeping: the partner star is exactly `P(|K cap L|=2)`

Let

`J=|K cap L|`, `P_j=P(J=j)`, `j=0,1,2,3`,                         (2.1)

for iid determinant triples `K,L~v`.

Then immediately

`P_0=D`, `P_3=V2`.                                                (2.2)

Moreover

`E binom(J,2)=sum_{i<j}P(i,j in K and i,j in L)=G2`,             (2.3)

so

`G2=P_2+3P_3`.                                                    (2.4)

Now sum the designated partner identity (1.2) over all physical pairs. An ordered pair `(K,L)` with `|K cap L|=2` has one and only one common physical pair, whereas `K=L` is excluded from the partner's ordered `k!=l` star. Therefore

`boxed: W_tot/|det M|^2 = P_2.`                                  (2.5)

This is the promised actual use of the designated fleet04/B11 theorem at an exact probabilistic identity, not merely a citation.

Define the failure probability of the ideal linear-intersection state by

`epsilon=P(J!=1)=P_0+P_2+P_3`.                                  (2.6)

## 3. A finite combinatorial lemma: eight linear-intersecting triples force a common vertex

### Lemma `QFORM-8TRIPLE-LINEAR-INTERSECTION-v1`

A family of eight **distinct** three-element sets in which every two sets intersect in exactly one element has a common element.

Equivalently, a 3-uniform pairwise-intersecting linear hypergraph with empty total intersection has at most seven edges.

### Proof

Take two edges

`A={x,a1,a2}`, `B={x,b1,b2}`.

Assume there is no common vertex. Then some third edge `C` omits `x`. Because every intersection has size exactly one, after relabeling

`C={a1,b1,c}`.                                                   (3.1)

Any further edge containing `x` must avoid all four vertices `a1,a2,b1,b2`, otherwise it would meet `A` or `B` twice. To meet `C` it must therefore contain `c`. Two such further edges would share both `x` and `c`, so there is at most one of them.

Any edge not containing `x` must choose exactly one of `{a1,a2}` to meet `A` and exactly one of `{b1,b2}` to meet `B`. There are four such ordered choices. At most one edge can realize any fixed choice, since two would share those two chosen vertices. Hence the whole family has at most

`2 + 1 + 4 = 7`

edges. Contradiction. QED.

The Fano plane shows that seven is the correct finite threshold for this purely combinatorial statement.

## 4. Weighted stability: collision-critical means true near-coloop

Sample eight iid determinant triples `K_1,...,K_8~v`. Let `G` be the event that all `binom(8,2)=28` pairs satisfy

`|K_a cap K_b|=1`.                                                (4.1)

By the union bound,

`P(G)>=1-28 epsilon`.                                             (4.2)

On `G` the eight triples are distinct. Lemma 3 then forces one common physical coordinate. Hence

`P(G)<=sum_i P(i in K_1,...,i in K_8)=sum_i c_i^8`.             (4.3)

Therefore

`boxed: sum_i c_i^8 >=1-28 epsilon.`                             (4.4)

Now assume the r35 collision collar upper bound

`C2=sum_i c_i^2 <=5/4`                                         (4.5)

and suppose, for contradiction, that

`q=max_i c_i <=63/64`.                                          (4.6)

Put `x_i=c_i^2`. Then `0<=x_i<=a=(63/64)^2` and `sum_i x_i<=5/4`. Convexity of `x^4` shows that the largest possible eighth moment is obtained by filling one coordinate to the cap and putting the remaining mass in one further coordinate:

`sum_i c_i^8=sum_i x_i^4
 <= a^4+(5/4-a)^4`                                              (4.7)

`=124955438978561/140737488355328`

`=0.8878617945993099...`.                                       (4.8)

But if `epsilon<=1/256`, (4.4) gives

`sum_i c_i^8 >=1-28/256=57/64=0.890625`,                        (4.9)

and the exact positive gap is

`57/64-[a^4+(5/4-a)^4]
 =388886587903/140737488355328
 >0`.                                                            (4.10)

Thus:

### Theorem `QFORM-COLLISION-STABILITY-TO-TRUE-NEARCOLOOP-v1`

Inside `C2<=5/4`,

`boxed: epsilon<=1/256  =>  max_i ||r_i||^2 >63/64.`            (4.11)

This is a dimension-free stability statement for the determinant-volume hypergraph. No physical minor is selected or inverted.

## 5. If collision stability fails, an existing paid third-direction currency is quantitatively large

Assume now

`epsilon>1/256`.                                                 (5.1)

There are two cases.

### Case A: genuinely disjoint triples

If

`D=P_0>=1/768`,                                                  (5.2)

apply the completed r34 literal original-coordinate cross-cut theorem:

`||p_Q||_infinity
 <=6e/(s D^(1/6))
 <=6e 768^(1/6)/s
 =49.3559219707.../s`.                                          (5.3)

This branch has a continuous density.

### Case B: overlap-two / concentrated-triple third volume

If `D<1/768`, then

`P_2+P_3=epsilon-D >1/384`.                                     (5.4)

By (2.4),

`G2=P_2+3P_3 >=P_2+P_3 >1/384`.                                (5.5)

Since `sum_{i<j}g_ij=3`,

`max_{i<j}g_ij >=G2/3 >1/1152`.                                (5.6)

Apply the designated partner's actual pair-area inequality (1.3):

`boxed:
 ||p_Q||_infinity
 <128 sqrt(2) sqrt(1152)/s
 =6144/s.`                                                       (5.7)

This is the concrete partner-result payment required by the B11 assignment. I claim essential boundedness here; the cited pair-area theorem does not supply a continuity upgrade at this scope.

Combining r35's two outer `C2` wings with Sections 4--5 gives a compact alternate route to the known non-near-coloop closure:

### Corollary `QFORM-EXACTRANK3-NONNEARCOLOOP-COLLISION-CLOSURE-v1`

For exact rank three, signature `(2,1)` or `(1,2)`, and `s=min|lambda(M)|`,

`max_i ||r_i||^2 <=63/64  =>  ||p_Q||_infinity <=6144/s`.       (5.8)

The scope is not claimed as a new fleet-wide closure, because fleet03/B10 already closes this non-near-coloop range by another mechanism. The new content here is the short 8-sample collision-stability bridge and its exact coupling to the fleet04/B11 star probability.

## 6. True-near-coloop geometry: the third direction splits into two independent transverse banks

The only genuinely new exact-rank-three survivor of the collision argument has a physical hub `0` with

`c=||r_0||^2>63/64`.                                             (6.1)

Write

`r_0=sqrt(c)e`,
`r_j=s_j e+w_j`, `w_j perpendicular e`, `j!=0`,
`rho=1-c<1/64`.                                                   (6.2)

Parseval gives the exact identities

`sum_j s_j^2=rho`,
`sum_j s_j w_j=0`,
`sum_j w_j w_j^T=I_2`.                                          (6.3)

If some residual transverse leverage `h_j=||w_j||^2` is at least `1/4`, the existing B10 transverse-heavy theorem already pays the full density. Thus the still-unpaid state may assume

`h_j<1/4` for every `j!=0`.                                     (6.4)

The vectors `w_j` are therefore a two-dimensional Parseval frame. Define its determinant-pair probability law

`mu_{jk}=det(w_j,w_k)^2`, `j<k`.                                (6.5)

Cauchy--Binet gives `sum mu=1`, and the inclusion marginal of coordinate `j` is exactly `h_j`.

For two iid pairs `P,Q~mu`, a union bound gives

`P(P cap Q !=empty)
 <=sum_j h_j^2
 <=(max_j h_j) sum_j h_j
 <(1/4)*2=1/2`.                                                  (6.6)

Hence the pair-disjointness probability `d_perp` satisfies

`d_perp>1/2`.                                                     (6.7)

Now color the residual **original coordinates** independently into two banks `S,T` with probability one half each. Put

`G_S=sum_{j in S}w_jw_j^T`, `G_T=sum_{j in T}w_jw_j^T`,
`delta_S=det G_S`, `delta_T=det G_T`.                            (6.8)

Cauchy--Binet identifies `delta_S` with the total `mu`-mass of pairs wholly inside `S`, and similarly for `T`. Only disjoint ordered pair-pairs can contribute to `delta_S delta_T`; for each such ordered pair the prescribed coloring has probability `1/16`. Therefore

`E[delta_S delta_T]=d_perp/16>1/32`.                            (6.9)

So some literal original-coordinate partition satisfies

`boxed: delta_S delta_T>1/32.`                                  (6.10)

Since `0<=G_S,G_T<=I_2`, each determinant is at most one. Thus both satisfy

`delta_S>1/32`, `delta_T>1/32`.                                 (6.11)

If `lambda_min(G_B)` denotes the smaller eigenvalue, the larger eigenvalue is at most one, so

`boxed: lambda_min(G_S),lambda_min(G_T)>1/32.`                  (6.12)

Equivalently, if `W_B` is the row matrix with rows `w_j`,

`boxed: sigma_2(W_S),sigma_2(W_T)>1/sqrt(32).`                  (6.13)

This proves:

### Theorem `QFORM-TRUE-NEARCOLOOP-TWO-TRANSVERSE-BANK-SPLIT-v1`

In the true-near-coloop exact-rank-three survivor after the transverse-heavy exit, the residual original independent coordinates admit a disjoint bipartition into **two** banks, each carrying a uniformly conditioned two-dimensional transverse spectral frame. The construction never rotates the random variables.

## 7. Each selected bank also carries a fixed physical hub-star energy

Write the spectral matrix in the orthogonal splitting `e direct_sum e^perp` as

`M=[[q,b^T],[b,C]]`.                                             (7.1)

The physical hub-to-leaf coefficients are

`A_0j=sqrt(c)(q s_j+b^T w_j)`.                                  (7.2)

In the current B10 survivor, after the normalized Rayleigh exit we may use `|q|<1/16`. Since `sigma_min(M)>=1`,

`||b||^2+q^2=||Me||^2>=1`,

hence

`||b||>=sqrt(255)/16`.                                          (7.3)

For either selected bank `B=S,T`, let `s_B=(s_j)_{j in B}`. By (6.13), (6.3), and `rho<1/64`,

`||(q s_j+b^T w_j)_{j in B}||_2`
` >= sigma_2(W_B)||b||-|q| ||s_B||_2`
` > sqrt(255)/(64 sqrt(2)) -1/128`.                             (7.4)

The right side is strictly larger than `1/6`: after moving `1/128`, squaring reduces this to the exact integer inequality `9180>8978`. Therefore

`sum_{j in B}(q s_j+b^T w_j)^2 >1/36`.                          (7.5)

Multiplying by `c>63/64` gives the clean physical statement

`boxed:
 sum_{j in B} A_0j^2 > (63/64)(1/36)=7/256,
 B=S,T.`                                                         (7.6)

Thus the true-near-coloop third direction is not hiding in one diffuse star: **two disjoint independent original-coordinate banks simultaneously carry both full transverse rank and a fixed hub interaction**.

If `|q|>=1/100`, the already-completed scalar-pivot/rank-two affine half-Riesz theorem pays the full density directly:

`||p_Q||_infinity
 <=128[c |A_00| |det M|]^(-1/4)
 <=128 sqrt(640/63)
 <408`,                                                          (7.7)

because `A_00=cq`, `c>63/64`, and `|det M|>=1`. Therefore the analytically hard descendant can be restricted further to

`|q|<1/100`.                                                      (7.8)

At (7.8), the completed fleet03/B13 one-heavy/two-transverse-bank theorem applies to the actual banks constructed in Section 6 with `kappa=1/32`. Its row-energy/small-ball calculation gives

`r_* = sqrt(63/64)[sqrt(1/32)sqrt(1-10^-4)-10^-2]
 =0.1654598528...`,                                              (7.9)

and hence the concrete product-safe concentration estimate

`boxed:
 P(Q in I) <= min(1,10.3912310444... sqrt(|I|))`                 (7.10)

for every interval `I` in this final true-near-coloop descendant.

Equation (7.10) is not yet the required linear small-ball estimate and therefore is **not** a bounded-density proof. It is, however, a target-valid quantitative consequence of the new bank splitter.

## 8. Rank-two control and how the third direction now appears

The mandatory opposite-sign rank-two control remains

`p_{2XY}(t)=log(1/(2|t|))`, `0<|t|<1/2`,                         (8.1)

for independent centered unit uniforms. The logarithmic endpoint is real.

The present run isolates the third direction in two complementary ways.

1. Away from a true near-coloop, failure of the ideal `|K cap L|=1` determinant geometry forces either disjoint rank-three volume or pair-area / extension volume. Those currencies are already paid and remove the rank-two logarithm.
2. In the true-near-coloop limit, determinant triples almost all share the heavy physical coordinate. The third direction does **not** disappear: after deleting that hub, the residual vectors form an exact two-dimensional Parseval frame. Section 6 forces this transverse frame into two independent original-coordinate banks of fixed conditioning, and Section 7 shows the near-null hub couples with fixed energy to **both** banks.

The remaining analytic problem is exactly to convert this two-bank transverse curvature plus hub slope into one more half-power of smoothing, upgrading the square-root small-ball law (7.10) to a linear law without taking a worst conditional density or replacing the small nonzero hub quadratic coefficient by zero.

## 9. First remaining implication

The B11 successor is now

`QFORM-TRUE-NEARCOLOOP-TWOBANK-SQRT-TO-LINEAR-v1`:

> In exact rank three with signature `(2,1)` or `(1,2)`, assume one original hub has leverage `c>63/64`, `|q|<1/100`, and there are two disjoint residual original-coordinate banks `S,T` with `G_S,G_T >= (1/32)I_2` and hub-star energies `sum_{S}A_0j^2, sum_T A_0j^2 >7/256`. Prove `P(Q in I)<=C|I|` uniformly for arbitrary cap-one product inputs, retaining all same-bank and cross-bank curvature.

The exact `q=0` / exact-coloop endpoint has separate completed receivers. The source-valid next mechanism should therefore interpolate **jointly** in the original product coordinates; the raw scalar square peel is known to lose logarithmically as `q->0` and is not a valid bridge.

Even a closure of this exact-rank-three successor would still leave the owner's arbitrary-additional-spectrum bridge. Global continuity remains open; continuity is proved only in the explicitly cited Fourier/cross-cut branches above.

## 10. Verification

`VERIFY.py` and `VERIFY_OUTPUT.txt` beside this report check the exact eighth-moment gap, the two paid constants, and the clean two-bank hub-star constant. The checker ends

`QFORM_B11_R36_COLLISION_NEARCOLOOP_CHECK_PASS`.

Numerical checks are regression aids only; all structural statements above are proved algebraically/combinatorially.
