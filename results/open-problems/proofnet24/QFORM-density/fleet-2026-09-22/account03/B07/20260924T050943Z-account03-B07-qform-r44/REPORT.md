SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B07, 2026-09-24T05:09:43Z.
attacking: the r47 matched kernel-star low-rank image — lift its deterministic compression back to a literal physical crossing, or pay physical third volume before any minor inversion.

# account03/B07 — r44 timestamp-unique run: matching-image to physical rank-two lift

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: coordinate minor selection / GEOMETRY  
Execution: `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.  
Status: **NEW DIMENSION-FREE PHYSICAL-CARRIER LIFT / FULL QFORM OPEN / FULL-TARGET CONTINUITY OPEN**.

No Gaussian, moment, log-concavity, compact-support, connected-support, iid, diagonal-basis, post-rotation independence, law-uniform pointwise quadratic-phase decay, arbitrary-joint coarea, fiber supremum, or deletion of a small nonzero coefficient is used. Orthogonal matrices below act only on deterministic coefficient columns when proving matrix inequalities; no rotated random coordinates are declared independent.

## 1. Fresh state and exact incoming branch

Fresh startup control was `yspennstate/math-research-brain@6d966e0177a2aeb4a175e32aa4bc46dcc6161530`; OWNER CONTROL remains revision `2026-09-22.15`, QFORM-only, with no account03/B07 pause or reassignment. The current claim ledger still marks the unrestricted bounded-density conjecture and the full-target continuity conclusion OPEN.

The immediate mathematical input is account03/B07 r47,

`yspennstate/math-open-problems@2cd69fe31ce8e25593ffb331c58d6ce1127d7241`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B07/20260924T044009Z-account03-B07-qform-r47/REPORT.md`.

Its bounded-support-degree branch produces a pair-disjoint matching `M` of literal physical rank-one pairs in an anchor bank `H`. Let `H_M` be the union of the endpoints of these matched pairs, let `I,J` be the fixed disjoint physical banks from the overlap-two packet, and put

`C0 = A[I union J, H_M]`.                                            (1.1)

For each matched pair `K`, let `g_K` be its unit kernel vector, embedded in the two physical coordinates of `K`. Pair-disjointness makes the `g_K` orthonormal. With `G` the matrix of these columns,

`W = C0 G`                                                          (1.2)

is exactly the r47 kernel-star image. The r47 weighted matching estimate gives

`T := ||W||_F^2 > T0 := 8192/31 = 264.258064516129...`.             (1.3)

R47 could already pay if `e3(WW^T)>=1/64`, because deterministic compression cannot increase third exterior volume. Its remaining conclusion, however, was only that the compressed matrix `W` is close to rank one or two. The first missing implication is to synchronize this back to the *entire literal physical crossing* `C0`, retaining the orthogonal coefficient directions that were absent from `W`.

The analytic receiver used below is the completed account02/B03 theorem

`QFORM-Z3-CROSSING-MARGINAL-FREE-v1`,

source

`yspennstate/math-open-problems@df738b7f0821d9af56dfd992cab10ecc6704e3fb`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B03/20260923T184716Z-account02-B03-QFORM-auto11/REPORT.md`.

For any literal physical crossing `C` with `Z3=e3(CC^T)>0`, it retains arbitrary same-side curvature, affine terms, outside couplings and additional spectrum and gives

`||p_Q||_infinity <= C3 Z3^(-1/6)`,
`C3=3*2^(4/3)*e^(1/3)=10.5501688311648...`,                       (1.4)

with a continuous density on that branch.

## 2. Orthogonal completion of the matched physical pairs

Each matched pair has a second unit vector `u_K`, orthogonal to its kernel vector `g_K`, supported on the same two physical coordinates. Because the pairs are disjoint, the columns of

`O = [G U]`                                                         (2.1)

form a block-diagonal orthogonal basis of `R^{H_M}`. Consequently

`C0 O = [W V]`,                                                     (2.2)

where `V=C0U`, and

`C0 C0^T = [W V][W V]^T`.                                          (2.3)

Thus every singular value, every exterior volume and every Frobenius distance to a fixed rank are unchanged by the deterministic right rotation. This is coefficient bookkeeping only; the random variables remain in their original physical coordinates.

Set

`E = e3(C0 C0^T) = e3([W V][W V]^T)`,
`tau = 1/64`.                                                       (2.4)

If `E>=tau`, (1.4) immediately gives the full ambient form a continuous density with

`||p_Q||_infinity <= 2 C3 = 21.1003376623296...`.                  (2.5)

Hence only `E<tau` remains.

## 3. High second-volume: the same determinant-heavy plane controls all omitted columns

Put

`B=WW^T`, `T=tr B`, `Z=e2(B)`, `V3=e3(B)`,                         (3.1)

and define the second Newton transform

`H2(B)=B^2-TB+Z I`.                                                 (3.2)

If the eigenvalues of `B` are `x_i>=0`, define the complete `E2` inclusion marginals

`alpha_i = x_i(T-x_i)/Z`.                                          (3.3)

When `Z>0`,

`sum_i alpha_i = 2`.                                               (3.4)

Therefore the spectral projection `P` onto the directions with `alpha_i>2/3` has rank at most two. The eigenvalues of `H2(B)` are `Z(1-alpha_i)`, so

`H2(B) >= (Z/3)(I-P)` on `P^perp`.                                 (3.5)

The key new point is that the *full omitted physical coefficient block* `V` is paid by the same Newton transform. Cauchy--Binet, separated according to whether a 3-column minor uses three `W` columns or exactly two `W` columns and one `V` column, gives

`E >= V3 + tr(V^T H2(B) V)`.                                       (3.6)

Also Newton's identity gives

`tr(B H2(B)) = 3 V3`.                                              (3.7)

Equations (3.5)-(3.7) imply

`||(I-P)W||_F^2 <= 9 V3/Z`,                                        (3.8)

`||(I-P)V||_F^2 <= 3(E-V3)/Z`.                                     (3.9)

Hence, with one common rank-at-most-two physical row-space carrier,

`dist_F(C0, rank<=2)^2`
` = dist_F([W V], rank<=2)^2`
` <= [9V3+3(E-V3)]/Z`
` <= 9E/Z`.                                                        (3.10)

In particular, for any threshold `z0>0`, the branch `Z>=z0`, `E<tau` satisfies

`dist_F(C0, rank<=2) < 3 sqrt(tau/z0)`.                             (3.11)

This is stronger than merely proving that the compressed image `W` is low rank: every omitted physical pair direction is synchronized to the same rank-two carrier.

## 4. Low second-volume: one heavy physical-image direction plus a rank-one residual

Suppose now `Z<z0`. Let `x1` be the largest squared singular value of `W`. Since

`T^2 = sum_i x_i^2 + 2Z <= x1 T + 2Z`,                             (4.1)

the matching energy (1.3) gives

`x1 > T0 - 2 z0/T0 =: x_*`.                                       (4.2)

Right-rotate only the `W` columns by an SVD. This again changes no physical crossing invariant. We may therefore write one column of `W` as `sqrt(x1) u`, `||u||=1`, with every other rotated `W` column orthogonal to `u`.

Project every remaining column, including all of `V`, onto `u^perp`; call the resulting matrix `Y`. Every three-column minor consisting of the heavy column and any two remaining columns contributes

`x1` times the corresponding squared two-column area of `Y`. Since these minors are a subset of the full Cauchy--Binet sum,

`E >= x1 e2(YY^T)`.                                                (4.3)

Let the squared singular values of `Y` be `y1>=y2>=...>=0`, and set

`s = sum_{i>=2} y_i`.                                              (4.4)

Then

`s^2 = sum_{i>=2} y_i^2 + 2 e2(y_2,y_3,...)`
` <= y1 s + 2 e2(y_2,y_3,...)`
` <= 2 e2(YY^T)`.                                                  (4.5)

The squared Frobenius distance from `Y` to rank one is exactly `s`. Adding back the heavy direction `u` therefore yields a rank-two approximant to all of `[W V]`, and by (4.2)-(4.5),

`dist_F(C0,rank<=2)`
` <= (2 e2(YY^T))^(1/4)`
` < (2 tau/x_*)^(1/4)`.                                            (4.6)

No nonzero tail has been set equal to zero.

## 5. Optimized physical rank-two lift

Choose `z0` so that the high- and low-`Z` bounds (3.11) and (4.6) agree:

`3 sqrt(tau/z0)`
` = [2 tau/(T0-2 z0/T0)]^(1/4)`.                                  (5.1)

Equivalently,

`81 tau (T0-2z0/T0)=2 z0^2`.                                      (5.2)

For

`tau=1/64`, `T0=8192/31`,

the positive solution and the resulting constants are

`z0 = 12.929187291442911356...`,                                   (5.3)
`x_* = 264.16021178028070944...`,                                  (5.4)
`d_* = 0.10429071727552326290...`.                                 (5.5)

We have proved:

### Theorem 5.1 — `QFORM-MATCHING-IMAGE-TO-PHYSICAL-R2-LIFT-v1`

In the r47 pair-disjoint matching branch, let `C0=A[I union J,H_M]` be the literal physical crossing and suppose its compressed kernel-star image `W=C0G` satisfies `||W||_F^2>8192/31`. Then one of the following holds:

1. `e3(C0C0^T)>=1/64`, and the full ambient quadratic form has a **continuous** density with
   `||p_Q||_infinity <=21.1003376623296...`; or

2. the complete physical crossing, with every matched-pair coefficient direction retained, satisfies
   `dist_F(C0,rank<=2)<0.104290718`.                                (5.6)

The proof aggregates the determinant packet before any coordinate-minor inversion.

There is a useful refinement of branch 2. Since

`||C0||_F^2 >= ||W||_F^2>T0`

and the squared tail beyond the top two singular directions is `<d_*^2`, either

`dist_F(C0,rank<=1)<sqrt(2)d_*`
` =0.147489346800663...`,                                         (5.7)

or

`s1(C0)s2(C0)`
` > d_* sqrt((T0-d_*^2)/2)`
` =1.19876993884320...`.                                          (5.8)

Thus the surviving physical carrier is either quantitatively near rank one, or genuinely nondegenerate rank two; the earlier compressed-image ambiguity is removed.

## 6. Required application of account04/B07

The designated partner is

`yspennstate/math-open-problems@dab16464e87c939cc0cf3fd01d070045290192fa`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B07/20260923T161510Z-account04-B07-coordinate-core-r2/REPORT.md`.

Its `r=0` physical-coordinate core theorem says that for three original coordinates with diagonal magnitudes at least `d` and mutual off-diagonal magnitudes at most `epsilon`,

`s3 >= d-3 epsilon`,                                               (6.1)

and the full ambient essential density is bounded by

`2 sqrt(18 pi)/(d-3 epsilon)`.                                    (6.2)

Apply this on the actual matched-pair bank. A rank-one physical pair has principal block

`A[K,K]=lambda_K u_K u_K^T`.                                      (6.3)

Therefore one of its two physical endpoints has diagonal magnitude at least `|lambda_K|/2`. For every matched pair with `|lambda_K|>=1/32`, choose such an endpoint; then

`|A_ii|>=1/64`.                                                    (6.4)

If three chosen endpoints have all three mutual physical edges at most `1/768`, the partner theorem at the concrete inequality

`d-3 epsilon = 1/64-3/768 = 3/256`                                (6.5)

gives

`s3(A[T,T])>=3/256`                                                (6.6)

and hence

`||p_Q||_infinity <=1283.393676611072...`.                        (6.7)

Continuity is not claimed by this partner gate. Consequently, in an unpaid matching branch, either at most two matched pairs have `|lambda_K|>=1/32`, or the graph on the selected high-`|lambda|` endpoints with edges `|A_ij|>1/768` has independence number at most two. This is an actual original-coordinate inequality; no spectral-coordinate independence is used.

## 7. What this closes, and what remains

R47's bounded-degree branch ended with a low-rank conclusion only for the deterministic compressed image `W=C0G`. Theorem 5.1 closes that synchronization gap: either the full physical crossing itself pays a genuine third-volume receiver, or the entire literal crossing is within `0.104291` in Frobenius norm of rank at most two, with a further near-rank-one versus nondegenerate-rank-two split.

This is not yet an analytic receiver for the nonzero physical tail in (5.6). It would be invalid to delete that tail as a small quadratic perturbation. The next precise debt is

`QFORM-PHYSICAL-R2-CARRIER-WITH-RETAINED-TAIL-RECEIVER-v1`:

consume a literal crossing with (5.6) together with (5.7) or (5.8), while retaining its nonzero tail, arbitrary same-side curvature, all outside couplings and additional spectrum; alternatively force another physical `E3` packet or a bounded principal core. The distinct r47 high-degree hub branch also remains and requires its own receiver.

Full QFORM remains **OPEN / not proved / not disproved**. Full-target continuity remains **OPEN**. Continuity is proved only on the physical `E3` exit (5.6 alternative 1); the account04/B07 principal-core exit establishes essential boundedness only.

## 8. Computation and source audit

`CHECKS.py` performs exact integer Cauchy--Binet/Newton packet checks and floating regression of both the high-`Z` and low-`Z` branches. `CHECKS.txt` ends `STATUS=PASS`. The computations are regression evidence only; the proof is Sections 2--6.

A pre-publication repository search for the matching-kernel-star physical-rank-two lift found the r47 source but no separate source matching the new `V`-column Newton packet / optimized physical-lift statement. This is a limited duplicate-work check, not evidence of external novelty.
