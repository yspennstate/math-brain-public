SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B04, 2026-09-24T05:16:04Z.
attacking: convert the global half-row-cap determinant-entropy dual into a weighted disjoint-row-triple matching certificate, then identify the precise overlap-collapse witness when that certificate is small.

# account01/B04 r29 — disjoint row-triple fractional matching for the global row-cap currency

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Product Fourier rearrangement  
Status: **NEW SUPPORTING THEOREM / GLOBAL AGGREGATE-BEFORE-INVERSION CERTIFICATE / DESIGNATED PARTNER APPLIED / FULL QFORM OPEN**  
Continuity: the Fourier branch proved below has a continuous `C_0(R)` density; full-target continuity remains open.  
Execution status: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted conjecture is not proved here. No Gaussianity, moments, compact support, log-concavity, connected support, post-rotation independence, fiber supremum, arbitrary-joint coarea bound, or law-uniform pointwise quadratic-phase decay is used.

## 1. Fresh dependencies


The analytic receiver is the audited Theorem D at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`.

The exact global row-cap dual used below is account01/B04 r28,

`yspennstate/math-open-problems@d68771753f4b44672e307bb817409483a503eba0`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B04/20260924T034618Z-account01-B04-QFORM-auto11-r28/REPORT.md`.

The designated partner input is account02/B04 r19,

`yspennstate/math-open-problems@3650b3e290b85ababdcd33294a86d25459da6f3d`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B04/20260924T043800Z-account02-B04-QFORM-auto11-r19/REPORT.md`,

whose theorem `QFORM-THREE-CARRIER-CUBE-DUAL-v1` is applied in Section 6.

## 2. Row-triple currency

Let `I,J` be disjoint banks of original independent coordinates and put

`M=A[I,J]`.

For each physical row triple `S subset I`, `|S|=3`, define

`z_S := det(M[S,:] M[S,:]^T) = sum_(|T|=3) det(M[S,T])^2 >=0`.   (2.1)

Let

`Z := sum_S z_S = e_3(M M^T)=e_3(M^T M)`.                        (2.2)

For a probability law `p` on supported row triples, let

`alpha_i=P_p(i in S)`,

and

`G_row(p)=exp(H(p)+sum_S p_S log z_S)`.                           (2.3)

Account01/B04 r28 proved

`G_(1/2)^*(M)=sup_{alpha_i<=1/2} G_row(p)
             =inf_(0<x_i<=1) [sum_S z_S prod_(i in S)x_i] prod_i x_i^(-1/2)`. (2.4)

Theorem D then gives

`||p_Q||_infinity <=6 sqrt(e) [G_(1/2)^*(M)]^(-1/6)`,             (2.5)

and the characteristic function is in `L^1`, hence `p_Q in C_0(R)`.

All variables here are literal original coordinates. Arbitrary same-bank quadratic curvature and affine terms remain allowed by the receiver.

## 3. Main theorem — weighted fractional matching of disjoint physical row triples

Build a graph whose vertices are supported row triples `S` (`z_S>0`) and whose edges are unordered pairs `{S,T}` with

`S cap T = emptyset`.                                             (3.1)

Give edge `{S,T}` weight

`c_ST=sqrt(z_S z_T)`.                                             (3.2)

Define the weighted fractional matching number

`nu_perp(z)=max sum_(S perp T) lambda_ST sqrt(z_S z_T)`,           (3.3)

where `lambda_ST>=0` and every triple vertex has load at most one:

`sum_(T:T perp S) lambda_ST <=1` for every `S`.                   (3.4)

### Theorem `QFORM-DISJOINT-ROWTRIPLE-FRACTIONAL-MATCHING-v1`

For every real matrix `M`,

`boxed: G_(1/2)^*(M) >=2 nu_perp(z).`                             (3.5)

Consequently, if `nu_perp(z)>0`, then for the full ambient quadratic form

`boxed:
 ||p_Q||_infinity
 <=6 sqrt(e) [2 nu_perp(z)]^(-1/6),
 p_Q in C_0(R).}`                                                (3.6)

### Proof

Fix any feasible fractional matching `lambda` and any dual point `0<x_i<=1`. Write `x_S=prod_(i in S)x_i`. From the vertex-load constraints,

`sum_S z_S x_S
 >=sum_S [sum_(T:T perp S)lambda_ST] z_S x_S
 =sum_(unordered S perp T) lambda_ST (z_S x_S+z_T x_T)`.         (3.7)

AM-GM gives

`z_S x_S+z_T x_T >=2 sqrt(z_S z_T) sqrt(x_S x_T)`.               (3.8)

For a disjoint pair of triples, every physical row occurs at most once in `S union T`; hence

`sqrt(x_S x_T) prod_i x_i^(-1/2)
 =prod_(i notin S union T) x_i^(-1/2) >=1`,                      (3.9)

because every `x_i<=1`. Therefore

`[sum_S z_S x_S] prod_i x_i^(-1/2)
 >=2 sum_(S perp T)lambda_ST sqrt(z_S z_T)`.                     (3.10)

Take the infimum over `x`, then the supremum over feasible `lambda`, and use (2.4). This proves (3.5). Substituting into (2.5) proves (3.6). QED.

### LP-dual collapse witness

Finite-dimensional LP duality gives the exact companion formula

`nu_perp(z)=min sum_S y_S`,                                      (3.11)

subject to

`y_S>=0`,
`y_S+y_T>=sqrt(z_S z_T)` for every `S perp T`.                   (3.12)

Thus a failure of the matching certificate is not an unstructured failure: if `G_(1/2)^*(M)<g`, then necessarily `nu_perp(z)<g/2`, hence there is an explicit low-cost fractional vertex-cover potential `y` dominating every disjoint triple product. Converting that potential overlap certificate into one of the already-paid C2/C3, pair-E4, grouped-hub, ridge, square-bank or rank-two-star receivers is the remaining structural step; it is not claimed here.

## 4. Canonical disjoint-pair aggregation and an `e_6/e_3` corollary

The matching theorem has a second useful aggregate form which does not select a single edge. Define

`D_S=sum_(T:T perp S) z_T`,
`Delta=sum_S z_S D_S=sum_(ordered S perp T) z_S z_T`.            (4.1)

Assume `Delta>0` and put

`w_S=z_S D_S/Delta`.                                              (4.2)

Consider the symmetric ordered-pair law

`pi(S,T)=z_S z_T/Delta`, `S perp T`.                              (4.3)

Its first marginal is `w`, and by symmetry its second marginal is also `w`. For every physical row `i`, the events `i in S` and `i in T` are disjoint under `pi`, so

`2 alpha_i=P(i in S)+P(i in T)=P(i in S union T)<=1`.             (4.4)

Thus `w` is automatically feasible for the half-row-cap theorem. Moreover

`log G_row(w)
 =sum_S w_S log(z_S/w_S)
 =log Delta-sum_S w_S log D_S
 >=log(Delta/Z)`,                                                 (4.5)

since `D_S<=Z`. Hence

`boxed: G_(1/2)^*(M) >= Delta/Z.`                                (4.6)

Equivalently, if `delta=Delta/Z^2` is the probability that two independent canonical row-volume triples are physically disjoint, then

`boxed: G_(1/2)^*(M) >= delta Z.`                                (4.7)

This is a direct aggregate-before-reciprocal bridge: a positive fraction of disjoint canonical third-volume mass can be spent without isolating any individual minor.

There is also a singular-value corollary. Let `G=M M^T`. For disjoint triples `S,T`, Hadamard-Fischer log-submodularity for the PSD matrix `G` gives

`det G_S det G_T >=det G_(S union T)`.                            (4.8)

Every six-set `U` has exactly `binom(6,3)=20` ordered decompositions `U=S disjoint_union T`. Therefore

`Delta>=20 sum_(|U|=6) det G_U=20 e_6(G)`.                       (4.9)

Combining with (4.6),

`boxed:
 G_(1/2)^*(M)
 >=20 e_6(M M^T)/e_3(M M^T).}`                                  (4.10)

Whenever the right side is positive,

`boxed:
 ||p_Q||_infinity
 <=6 sqrt(e) [20 e_6(MM^T)/e_3(MM^T)]^(-1/6),
 p_Q in C_0(R).}`                                                (4.11)

This `e_6/e_3` estimate is only a corollary; the fractional-matching certificate (3.5) can be much stronger because it retains the physical row geometry rather than collapsing to singular values.

## 5. Genuinely rotated indefinite stress family: diffuse physical rows, no local pair currency

Let

`v=(1,2,3,4,5,6)^T`, `||v||^2=91`,
`R=I_6-2 vv^T/91`.                                               (5.1)

`R` is an exact orthogonal Householder matrix. Every entry of `R` is nonzero: off-diagonal entries are `-2ij/91`, and diagonal entries are `1-2i^2/91`, none of which vanishes for `i=1,...,6`.

For an integer `m>=3`, define a `(6m)x6` physical cross block `M_m` with rows indexed by `(j,r)`, `j=1,...,6`, `r=1,...,m`, by

`row_(j,r)(M_m)=m^(-1/2) e_j^T R`.                               (5.2)

Every physical cross coefficient is nonzero and

`M_m^T M_m=I_6`.                                                  (5.3)

Set

`A_m=[[0,M_m],[M_m^T,0]]`.                                       (5.4)

The nonzero spectrum of `A_m` is exactly `+1` six times and `-1` six times. Thus this is a genuinely rotated, indefinite, nonseparable target-valid family for every `m`.

For a physical row triple `S`,

`z_S=m^(-3)` if the three rows come from three distinct direction groups, and `z_S=0` otherwise. There are

`binom(6,3)m^3=20m^3`                                            (5.5)

supported triples, so

`Z=20`.                                                          (5.6)

The supported-triple disjointness graph has an explicit perfect matching: pair each three-group set with its complementary three-group set, and within each complementary pair match the `m^3` copy-tuples bijectively. There are `10m^3` matched edges, each of edge weight `m^(-3)`. Taking `lambda=1` on these edges gives

`nu_perp(z)>=10`.                                                (5.7)

Since the dual point `x_i=1` gives the opposite inequality `G_(1/2)^*(M_m)<=Z=20`, (3.5) and (5.7) prove the exact value

`boxed: G_(1/2)^*(M_m)=20.`                                     (5.8)

Therefore, uniformly in the number `6m` of left-bank physical coordinates,

`boxed:
 ||p_(X^T A_m X)||_infinity
 <=6 sqrt(e) 20^(-1/6)
 =6.004269244596687...,
 p_(X^T A_m X) in C_0(R).}`                                     (5.9)

This family is designed to make every fixed local row pair weak while preserving a constant global product-Fourier packet.

Indeed, for any fixed physical pair `{a,b}` from two distinct direction groups, the pair-anchored fourth-volume mass of account03/B04's pair-E4 theorem is

`H_ab=6/m^2`.                                                     (5.10)

Thus a fixed-pair fourth-volume certificate scales like `m^(1/4)` in density, while the new global fractional-matching certificate is constant. This is the intended aggregate-before-inversion phenomenon.

## 6. Designated account02/B04 r19 applied at an actual inequality

Apply account02/B04 r19's completed `QFORM-THREE-CARRIER-CUBE-DUAL-v1` to the same `M_m`. Choose three literal carrier rows `h_1,h_2,h_3`, one from each of direction groups `1,2,3`.

Because every supported row triple has weight `m^(-3)`, the aggregate carrier-face masses depend only on face size and are

`W_empty=(20m^3-30m^2+12m-1)/m^3`,                              (6.1)
`W_i=(10m^2-8m+1)/m^3` for each singleton face,                  (6.2)
`W_ij=(4m-1)/m^3` for each pair face,                            (6.3)
`W_123=1/m^3`.                                                    (6.4)

The partner theorem's complementary-face lower bound is therefore

`boxed:
 G_H >=2[sqrt(W_empty W_123)+3 sqrt(W_i W_ij)].}`                (6.5)

The carrier-constrained optimizer distributes uniformly inside each face because all supported `z_S` are equal. Any noncarrier row from one of groups `1,2,3` has marginal at most `1/(m-1)<=1/2`, and any row from groups `4,5,6` has marginal at most `1/m<=1/2`. Hence for `m>=3` the partner carrier-balanced law is also a legitimate global Theorem-D law, so (6.5) gives an actual full-law density certificate.

At `m=64`, exactly

`W_empty=5120767/262144`,
`W_i=40449/262144`,
`W_ij=255/262144`,
`W_123=1/262144`.                                                 (6.6)

Thus

`G_H >=0.09077276176664519...`,                                  (6.7)

and account02/B04 r19 plus Theorem D gives

`||p_(X^T A_64 X)||_infinity <=14.756133187970226...`.            (6.8)

On the identical matrix the new global disjoint-matching theorem gives instead

`||p_(X^T A_64 X)||_infinity <=6.004269244596687...`,             (6.9)

an improvement factor

`2.457606843871874...`.                                          (6.10)

This comparison is not a claim that the partner theorem is globally weaker; r19 was built for a small number of genuinely heavy carriers. The present family is the complementary diffuse regime in which forcing three arbitrary rows to marginal `1/2` wastes most of the third-volume entropy, while a global disjoint matching preserves it exactly.

## 7. First unpaid implication

The new theorem converts the r28 optimization gap into a precise combinatorial one. The next target is

`QFORM-LOW-DISJOINT-MATCHING-TO-PHYSICAL-OVERLAP-RECEIVER-v1`:

> Starting from the surviving target-scale physical cross block supplied by the global structural funnel, if `nu_perp(z)` is not target-scale, use the LP-dual low-cost potential `y_S` from (3.11)-(3.12), together with account02/B04 r19's complementary carrier-face collapse and the pair-anchored E4 collapse, to force an already-paid overlap-C2/C3, fixed-pair/hyperbolic, grouped-hub, ridge, square-bank or rank-two-star receiver.

The obstruction is real: a 3-uniform support can be pairwise intersecting with every physical row marginal below `1/2` (Fano-type configurations), so `nu_perp=0` does not by itself imply one heavy row. The remaining bridge must use the determinant/Gram structure, not only abstract hypergraph intersection.

## 8. Status

- Full universal three-large-eigenvalue conjecture: **OPEN**.
- Full-target continuity: **OPEN**.
- New matching / disjoint-pair / `e_6/e_3` branches: **continuous `C_0` density proved** under their stated currencies.
- Partner result applied at an actual inequality: **yes**, account02/B04 r19, Section 6.
- Repository use is not native learned-memory ingestion: status remains **`WITHOUT_VERIFIED_BRAIN`**.
