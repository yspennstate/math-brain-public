SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B19, 2026-09-24T04:26:44Z.
attacking: the account03/B19 r48 strong-rank-two adaptive-alignment survivor — test whether its curved two-bank core can itself be scalarized to bounded density before the third target resource is spent.

# account02/B19 — curved rank-two interface obstruction and full-target Fresnel payment

Programme: QFORM-DENSITY-3EIG-20260922.  
Status: **ESSENTIAL_STEP_APPLIED + CANDIDATE_ANALYTIC_INTERFACE_REFUTED / FULL QFORM OPEN**.  
All random-coordinate independence below is inherited only from disjoint ORIGINAL-coordinate product banks. No spectral/post-rotation independence, moments, compact support assumption beyond the explicit witness law, log-concavity, or perturbative deletion is used.

## 1. Source-pinned inputs

Required Claude/source checkpoint read at
`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, directory
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`:
`RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`.
The completed result used at equation level below is Theorem F (Fresnel–Brascamp–Lieb): if
`A=sum_{k=1}^3 lambda_k v_k v_k^T+B`, `B_II` is diagonal, the three-frame Gram on an original-coordinate bank `I` is `G_I`, and every normalized row leverage is at most `1/2`, then

`||p_Q||_infinity <= 12 (|lambda_1 lambda_2 lambda_3| det G_I)^(-1/3)`.

Fresh designated partner account03/B19 r48 is source-pinned at
`yspennstate/math-open-problems@e922248c12820c303861233f1a626fdf9aae9687:proofnet24/QFORM-density/fleet-2026-09-22/account03/B19/20260924T030130Z-account03-B19-QFORM-r48/REPORT.md`.
Its new strong-rank-two funnel says: for a physical cross block `N=A[R,C]` with the stated ultra-thin rank-two gate, either a light same-bank row has transverse distance `F_j>=2^-12` and a physical `E3` receiver pays the full law by `<905`, or every light same-bank row is within `2^-12` of the adaptive deleted-cross top-two singular plane, with at most three heavy coordinates per bank. The remaining edge is `QFORM-HEAVY6-ADAPTIVE-R2-SELF-CURVATURE-PAYMENT-v1`.

## 2. Exact full-target family in the perfect-alignment survivor

Fix an integer `m>=3`. Take five pairwise disjoint physical coordinate banks
`U1,U2,V1,V2,W`, each of size `m`. Let `u1,u2,v1,v2,w` be the flat unit vectors on the respective banks. Put

`l1=u1+v1`, `l2=u2+v2`,

and define

`A = l1 l2^T + l2 l1^T + w w^T`.                                      (2.1)

The vectors `l1,l2,w` are mutually orthogonal with norms `sqrt(2),sqrt(2),1`. On the orthonormal basis

`e1=l1/sqrt(2), e2=l2/sqrt(2), e3=w`,

(2.1) is

`[[0,2,0],[2,0,0],[0,0,1]]`.

Hence

`spec_nonzero(A)={2,-2,1}`.                                             (2.2)

This is an exact rank-three instance of the FULL target.

Take the two physical banks

`R=U1 union U2`, `C=V1 union V2`.

Then

`N=A[R,C]=u1 v2^T+u2 v1^T`,                                            (2.3)

so

`sigma_1(N)=sigma_2(N)=1`, `rank N=2`.                                  (2.4)

The same-bank curvature is simultaneously nontrivial:

`A[R,R]=u1u2^T+u2u1^T`,
`A[C,C]=v1v2^T+v2v1^T`.                                                  (2.5)

Thus this is exactly the analytic situation not covered by the pure-bilinear payment.

## 3. The r48 adaptive-alignment funnel is sharp: every light-row distance is zero

The top-two right singular space of `N` is `span(v1,v2)`. Every coordinate `j in C` has top-two leverage

`ell_j=1/m<=1/2`.                                                        (3.1)

There are therefore no heavy coordinates at all for `m>=3`.

If `j in V1`, delete `j` from `C` and write `J=C\{j}`. Then

`M_j=A[R,J]=u1 v2^T + u2 (v1|_J)^T`.

Its two-dimensional right singular space is exactly

`V_2(M_j)=span(v2,v1|_J)`.                                               (3.2)

The same-bank row into `J` is

`d_j=A[j,J]=m^(-1/2) v2`,                                                (3.3)

hence

`F_j=dist(d_j,V_2(M_j))=0`.                                              (3.4)

The same calculation for `j in V2` gives `d_j=m^(-1/2)(v1|_J)` and again `F_j=0`. Transposing gives the identical zero-distance statement on every row of `R`.

Therefore this family lies not merely within the r48 unpaid adaptive-alignment chamber but on its exact perfect-alignment face. The r48 promotion theorem cannot produce positive `E3` from same-bank row transversality here. This is an equation-level application of the newest partner theorem, not an analogy.

## 4. New obstruction: the curved two-bank scalar output can have infinite essential density

For a product input `X`, define the four scalar projections

`Y1=<u1,X>`, `Y2=<u2,X>`, `Z1=<v1,X>`, `Z2=<v2,X>`.

The `R union C` partial quadratic is

`H=2(Y1+Z1)(Y2+Z2)`.                                                     (4.1)

Choose every physical coordinate in the four banks to be independent `Uniform[-1/2,1/2]`, an admissible cap-one law. Set

`L1=Y1+Z1`, `L2=Y2+Z2`.

Because `U1 union V1` and `U2 union V2` are disjoint original-coordinate banks, `L1,L2` are independent. Each is a normalized sum of `2m` interval variables, so its density `f` is continuous and strictly positive at zero. Hence there exist constants `c,delta>0` (for this fixed `m`) such that

`f(x)>=c` for `|x|<=delta`.                                              (4.2)

For `0<h<2 delta^2`, the density of `H=2L1L2` satisfies

`p_H(h)= integral_R f(x) f(h/(2x)) dx/(2|x|)`

and restricting to `x in [h/(2delta),delta]` gives

`p_H(h) >= (c^2/2) log(2 delta^2/h) -> infinity` as `h downarrow 0`.      (4.3)

Therefore

`boxed: ||p_H||_infinity = infinity`.                                   (4.4)

This proves `QFORM-R2-INTERNAL-CURVATURE-FIBER-LINF-FAILURE-v1`:

> A fixed-strength literal physical rank-two crossing, even with `sigma_1 sigma_2=1`, does not imply a bounded density for the two-bank partial quadratic once arbitrary same-bank curvature on those same banks is retained. This failure persists on the exact perfect-alignment face of the newest account03/B19 r48 survivor.

Consequently the remaining r48 branch cannot be solved by first scalarizing the curved two-bank output using only the rank-two cross-volume and then convolving a third source. The third target resource must be retained jointly through the smoothing step.

This is NOT a counterexample to QFORM, because the full target law includes the independent `W`-square below.

## 5. Strict local no-pivot stress

The construction can be made arbitrarily diffuse in physical coordinates. Outside `W`, every diagonal is zero; on `W`, every diagonal equals `1/m`. Every nonzero physical off-diagonal entry has magnitude `1/m`. Direct inspection gives

`max_i |A_ii|=1/m`,
`max_{i<j} |det A[{i,j},{i,j}]|=1/m^2`,
`max_{|S|=3} |det A[S,S]|=1/m^3`.                                      (5.1)

For the triple claim, triples lying entirely in the bipartite `R union C` core have determinant zero; the only nonzero case is one `W` coordinate times one connected core pair, of magnitude `1/m^3`.

Thus for every fixed `tau>0`, choosing `m>max(3,1/tau)` puts the exact target family simultaneously in strict scalar, pair, and triple no-pivot territory while preserving (2.2), (2.4), (3.4), and the logarithmic singularity (4.3) of the two-bank partial output.

## 6. Positive full-target payment by the required pinned Theorem F

The obstruction is repaired when the genuine third target resource is spent before the two-bank scalarization. The three orthonormal eigenvectors are

`r_+=(l1+l2)/2`, `r_-=(l1-l2)/2`, `r_3=w`,

with coefficients `lambda_+=2`, `lambda_-=-2`, `lambda_3=1`.

Use Theorem F from the required `e5f71d...` source with `I` equal to all five original-coordinate banks and residual `B=0`. Since the three eigenvectors are orthonormal,

`G_I=I_3`, `det G_I=1`.                                                 (6.1)

For a coordinate in one of `U1,U2,V1,V2`, the three-frame leverage is `1/(2m)`; for a coordinate in `W` it is `1/m`. Hence

`max_i leverage_i=1/m<=1/2` for `m>=2`.                                  (6.2)

All hypotheses of Theorem F therefore hold in the original product coordinates, and

`||p_Q||_infinity <= 12 |2*(-2)*1|^(-1/3)`
`                  = 12 * 4^(-1/3)`
`                  = 7.55952629936924...`.                               (6.3)

The Fourier receiver also gives a continuous `C_0` density in this branch. This is a real target-level equation using one of the explicitly required completed source results.

The contrast between (4.4) and (6.3) is the key point: the SAME target family has an unbounded curved two-bank partial density but a uniformly bounded full quadratic once the third direction is kept inside the joint Fresnel/product estimate.

## 7. Sharpened first unpaid implication

The previous first debt `QFORM-HEAVY6-ADAPTIVE-R2-SELF-CURVATURE-PAYMENT-v1` must be strengthened to

`QFORM-HEAVY6-ADAPTIVE-R2-SELF-CURVATURE-THIRD-RESOURCE-JOINT-PAYMENT-v2`:

> In the strong physical rank-two crossing survivor of account03/B19 r48, after every transverse-light-row physical-`E3` exit has failed, retain the third actual target spectral resource through the smoothing argument. Either manufacture a literal original-coordinate three-Fresnel packet satisfying Theorem F (or another already-paid grouped/hub/volume receiver), or prove a product-preserving descent that jointly spends the adaptively aligned same-bank curvature and the third resource. Do not replace the curved two-bank core by a scalar bounded-density law first: the family above disproves that interface even at `F_j=0` for every light row.

In the explicit stress family the entire third resource is the disjoint `W` square and Theorem F pays it by `<7.560`; in the general survivor that disjointness/diffuse-frame gate is not automatic. Heavy-six handling, the giant near-rank-one frontier, rank-<=9 carrier frontiers, arbitrary-extra-spectrum closure outside completed inductive branches, and the unrestricted continuity theorem remain separate debts.

## 8. Status

This run does not prove or disprove unrestricted QFORM. It removes a tempting analytic interface inside the newest strong-rank-two synthesis branch and shows the correct order of operations on an exact target-valid, arbitrarily no-pivot family: spend the third resource jointly before taking any two-bank density supremum.
