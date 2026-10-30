SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B09, 2026-09-23T06:13:24Z.
attacking: pay the partner rank-split k=2 branch: two physical core directions plus a disjoint outside line, retaining arbitrary dense within-bank curvature via source-coordinate conditional linear anti-concentration.

# fleet02/B09 auto11 — substantive checkpoint: k=2 rank split -> physical pair + external line

Programme: `QFORM-DENSITY-3EIG-20260922`. Full target remains OPEN.

## First unpaid implication

The newest completed designated-partner input is fleet03/B09 r24,
`QFORM-PLUCKER-SMALLRHO-RANKSPLIT-v1`, canonical source
`yspennstate/math-open-problems@9fcac412f233f09c6ee5e8a1140207d596cce8a2`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B09/20260923T045157Z-fleet03-B09-QFORM-r24/REPORT.md`.
Its small-disjointness branch produces a physical triple `S` and one of `k=3,2,1`. The prior B09 run paid a genuine exact-zero endpoint in the `k=1` branch. This run attacks `k=2`: two active directions are physically concentrated on `S`, while the disjoint bank `T=S^c` carries a quantitative outside line.

The exact remaining issue is not finding the line; the partner already does that. It is to turn the coefficient-space split into original-coordinate currency before any reciprocal minor payment, while remembering that arbitrary same-bank curvature can cancel a displayed low-rank component.

## Lemma: `QFORM-K2-COREPAIR-LINE-EXTRACTION-v1`

Let `U in R^(N x 3)` have orthonormal columns, rows `u_i^T`, and suppose a physical triple `S` belongs to the partner `k=2` branch at scale `eta in (0,1)`. Thus there is an orthogonal splitting

`R^3=F direct_sum span(f)`, `dim F=2`, `|f|=1`,

such that

`singular_min(P_S U|_F) >= sqrt(1-eta)`

and, for `T=S^c`,

`||P_T U f||_2 > sqrt(eta)`.

Then:

1. there are distinct physical coordinates `i,j in S` such that, writing `a_l=P_F u_l`,

`|det_F(a_i,a_j)| >= (1-eta)/sqrt(3)`;

2. the `2 x 2` row map from `F` determined by this pair has

`singular_min([a_i^T;a_j^T]|_F) >= (1-eta)/sqrt(6)`;

3. on the disjoint original-coordinate bank `T`, the coefficient vector

`r=(<u_t,f>)_(t in T)`

satisfies `||r||_2>sqrt(eta)`. Hence the aggregate scalar `Z=r^T X_T` is an original-product linear projection; by the standard one-dimensional product-marginal bound,

`||p_Z||_infinity <= sqrt(2)/||r||_2 < sqrt(2/eta)`.

No independence between `Z` and other projections of `X_T` is asserted.

### Proof

Choose an orthonormal basis of `F`. The `3 x 2` matrix `P_S U|_F` has two singular values at least `sqrt(1-eta)`, so Cauchy--Binet gives

`sum_{i<j in S} det_F(a_i,a_j)^2
 =det[(P_S U|_F)^T(P_S U|_F)]
 >=(1-eta)^2`.

There are three pairs, hence one has determinant magnitude at least `(1-eta)/sqrt(3)`. Each selected row has norm at most one, so the operator norm of the resulting `2 x 2` matrix is at most its Frobenius norm, at most `sqrt(2)`. The product of its singular values is the determinant magnitude, giving the second claim. The third is exactly the partner outside-line bound written in physical coefficients:

`||r||_2^2=f^T U_T^T U_T f=||P_TUf||_2^2>eta`.

At the partner scale `eta=1/16`, the extracted physical core pair has determinant at least `15/(16sqrt(3))>0.5412`, smallest singular value at least `15/(16sqrt(6))>0.3827`, and the external disjoint line has norm `>1/4`.

This is an aggregate-before-inversion statement: the physical pair is selected only after summing all three pair minors on the core triple, and the outside direction remains a full disjoint bank projection.

## Required newest-Claude result applied to a real target inequality

The required source package
`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, in particular `COUNTEREXAMPLE_SEARCH.md`, proves the rank-two positive-semidefinite bound

`||p_(lambda_1 Y_1^2+lambda_2 Y_2^2)||_infinity
 <=2 pi/sqrt(lambda_1 lambda_2)`

for a two-dimensional orthogonal projection of an arbitrary cap-one product law (`lambda_1,lambda_2>0`). Apply it as follows.

Take three original coordinates `S={1,2,3}` and let `e=(1,1,1)/sqrt(3)`. Let `v_1,v_2` be any orthonormal basis of `e^perp`, so

`P_F=v_1v_1^T+v_2v_2^T=I-ee^T`

is a genuinely dense same-side physical block. Take a disjoint physical hub `h`, a disjoint bank `T` and a unit vector `c` on `T`. For arbitrary further disjoint coordinates `R`, let `H(X_R)` be an arbitrary quadratic-affine form and set

`Q=X_S^T P_F X_S + 2X_h <c,X_T> + H(X_R)`.

The first term is independent of the remainder and has density at most `2 pi`. Convolution therefore gives the actual target inequality

`boxed: ||p_Q||_infinity <=2 pi`,
`boxed: P(Q in L)<=2 pi |L|`.

The matrix has the two eigenvalues `1,1` from `P_F` and the star eigenvalues `+1,-1`; hence it has at least four eigenvalues of modulus at least one. The arbitrary `H` can contain an additional dense same-side quadratic operator on its disjoint bank without changing the bound.

This packet is exactly the partner `k=2` endpoint for the mixed frame `U=[v_1,v_2,c]`: every nonzero Pluecker basis uses two rows from the three-coordinate core, so two such bases cannot be disjoint (`rho=0`); the core carries `F` isometrically and `T` carries the outside line isometrically. Thus a genuine `rho=0`, `k=2` target family is paid with a linear small-ball bound.

## Regression obstruction: arbitrary same-bank curvature cannot be ignored

The same exact `k=2` coefficient geometry does NOT pay arbitrary within-bank curvature merely because a favorable rank-two component has been displayed. Keep the same `v_1,v_2,c`, but add on the core bank the dense residual curvature

`R_S=-(v_1v_1^T+v_2v_2^T)`.

It exactly cancels the advertised rank-two positive component. If `T` is one physical coordinate and `c=1`, the actual form reduces to

`Q=2X_hX_t`.

For iid `Uniform[-1/2,1/2]` inputs,

`p_Q(q)=log(1/(2|q|))`, `0<|q|<1/2`,

so the density is logarithmically unbounded at zero. The coefficient frame still has a perfect `k=2` core-plus-line split and the formal curvature coefficients can still be `lambda_1=lambda_2=1`.

This is not a counterexample to QFORM: after cancellation the active matrix has only eigenvalues `+1,-1`. It is a source-valid obstruction to the intermediate claim that partner `k=2` geometry plus a favorable displayed curvature component can absorb an arbitrary same-bank quadratic residual. Any successful `k=2` payment must certify the third direction in the ACTUAL total block/form, or keep the external third source-compatible smoother unconditioned through the cancellation.

## Next exact debt

`QFORM-K2-ACTUALCORE-OR-EXTERNAL-SMOOTHER-v1`: starting from the extracted physical pair and disjoint outside line, prove a uniform direct interval bound whenever the actual physical core is not already paid by a finite-core/definite/indefinite-pair theorem, while keeping arbitrary same-bank residual curvature in the active kernel rather than treating it as a small random perturbation.
