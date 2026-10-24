# account02/B09 auto11 — substantive checkpoint

Programme: `QFORM-DENSITY-3EIG-20260922`. Full target remains OPEN.

## First unpaid implication

The newest designated-partner result actually available is account03/B09 r24,
`QFORM-PLUCKER-SMALLRHO-RANKSPLIT-v1`, source
`yspennstate/math-open-problems@9fcac412f233f09c6ee5e8a1140207d596cce8a2`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B09/20260923T045157Z-account03-B09-QFORM-r24/REPORT.md`.
Its small-disjointness branch produces, at `eta=1/16`, a literal physical triple carrying either a three-core, a two-core plus an outside line, or a one-core plus an outside plane. The first unpaid B09 implication is to turn those source-coordinate rank splits into a direct linear small-ball bound while allowing arbitrary residual same-bank curvature and without treating a small coefficient matrix as a small random perturbation.

This checkpoint pays a genuine part of the `k=1` branch: the exact-zero physical two-hub endpoint whenever the coefficient-space torsion is nonzero. It also identifies the precise algebraic survivor when that payment degenerates.

## Setup

Take one physical hub `h`, a leaf bank `I`, and arbitrary further conditioned coordinates. Suppose the exact leaf curvature is

`A_II = D + lambda_1 v_1 v_1^T + lambda_2 v_2 v_2^T`,

with `D` diagonal and `lambda_1 lambda_2 !=0`. Put

`c=A[I,h]`, `W=[v_1,v_2,c]`, `G=W^T W>0`, `U=W G^(-1/2)`.

Thus `U^T U=I_3`. Write rows of `U` as `u_i^T`, and set

`L=diag(lambda_1,lambda_2,0)`,
`K=G^(1/2) L G^(1/2)`,
`q=G^(1/2)e_3`.

Then for distinct leaves `i,j`,

`A_ij = u_i^T K u_j`,

while the physical hub edge is

`A_hj = u_j^T q`.

Fix a physical triple `S subset I`, put `T=I\S`, and let

`R_T=U_T^T U_T`.

Assume this is a partner `k=1` rank split: there is a unit vector `f`, with `H=f^perp`, such that

`R_T f = mu f`, `0<=mu<=eta`,

and

`R_T|_H >= eta I_H`.

The partner theorem supplies exactly this with `eta=1/16` on at least one sixth of its determinant mass in the `k=1` branch.

## New extraction lemma: coefficient torsion forces a physical two-row wedge

For a physical leaf `i in S`, define its two cross rows on the disjoint outside bank `T` by

`a_i=(A_ij)_(j in T)=U_T K u_i`,

`b=(A_hj)_(j in T)=U_T q`.

Let

`Delta_i(T)=||a_i||^2||b||^2-<a_i,b>^2`.

Define the scalar coefficient-space torsion

`Theta=|det(f,Kf,q)|=|f^T K(q cross f)|`.

### Lemma `QFORM-K1-TORSION-TO-PHYSICAL-WEDGE-v1`

There exists `i in S` such that

`boxed: Delta_i(T) >= [eta^2(1-eta)/3] Theta^2.`

### Proof

For fixed `i`, the Gram matrix of the two outside rows is

`[K u_i,q]^T R_T [K u_i,q]`.

Since `R_T>=eta P_H`, monotonicity of the determinant on positive `2 x 2` matrices gives

`Delta_i(T)
 >= eta^2 det([P_H K u_i,P_H q]^T[P_H K u_i,P_H q])
 = eta^2 det(f,K u_i,q)^2`.                                      (1)

The last equality is the three-dimensional area identity: the area of two projections onto `f^perp` equals the absolute scalar triple product with the unit normal `f`.

Put `z=K(q cross f)`. Then

`det(f,K u_i,q)=u_i^T z`.

Therefore

`sum_(i in S) det(f,K u_i,q)^2
 = z^T U_S^T U_S z
 = z^T(I-R_T)z`.                                                (2)

The splitting `R^3=span(f) direct_sum H` is spectral for `R_T`. On `span(f)`, `I-R_T` is at least `1-eta`; on `H` it is positive semidefinite. Hence

`z^T(I-R_T)z >=(1-eta)|f^Tz|^2=(1-eta)Theta^2`.                (3)

Since `|S|=3`, one `i in S` has triple-product square at least one third of (3). Combining with (1) proves the lemma. QED.

## Density consequence at the exact-zero physical endpoint

For the leaf `i` selected above, additionally assume the physical two-hub core is exactly zero:

`A_hh=A_ii=A_hi=0`.

The complete theorem `QFORM-ZERO-HUBPAIR-ARBITRARY-REMAINDER-v1` from
`yspennstate/math-open-problems@03ec6ccf1de2e2544e850cbda25d460aacae6a1b`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B09/20260923T024331Z-account02-B09-QFORM-auto12/REPORT.md`,
allows the entire complementary quadratic operator to remain arbitrary and gives

`||p_Q||_infinity <=2sqrt(2) Delta_full^(-1/4)`.

Adding complementary coordinates only adds a positive-semidefinite contribution to the two-row Gram matrix, so `Delta_full>=Delta_i(T)`. Consequently

`boxed:
 ||p_Q||_infinity
 <=2sqrt(2) 3^(1/4) eta^(-1/2)(1-eta)^(-1/4)|Theta|^(-1/2).`

The identical coefficient multiplies `|J|` for every interval `J`; there is no probability squaring and no square-root decoupling loss. At the partner scale `eta=1/16`, the numerical prefactor is `<15.132` before the `|Theta|^(-1/2)` factor.

The analytic point is that the dense same-side operator is not conditioned away: only the two physical hubs are used for conditional linear anti-concentration, and the full complementary quadratic form stays inside the arbitrary remainder of the zero-hubpair theorem.

## Exact target-valid regression / stress packet

The extraction is nonvacuous. In coefficient space let

`f=(e_1+e_2)/sqrt(2)`, `g=(e_1-e_2)/sqrt(2)`,

and use physical leaf rows

`u_i=f`, `u_1=u_2=g/sqrt(2)`, `u_3=u_4=e_3/sqrt(2)`.

These rows form an orthonormal three-frame. Take `lambda_1=1`, `lambda_2=-1`, `G=I`, and let the physical hub couple through the third column. Then the selected pair `(h,i)` has

`A_hh=A_ii=A_hi=0`,

and its two cross rows have disjoint outside supports and norms one, so `Delta_full=1`. Thus the earlier theorem gives the sharp packet estimate

`boxed: ||p_Q||_infinity <=2sqrt(2)`.

In the grouped basis `(v_1,v_2,h,c)`, the active coefficient matrix has eigenvalues `{1,-1,1,-1}`, so this is a literal target-valid form. The same-side leaf block is indefinite rank two; the zero-hubpair theorem would continue to allow any additional dense symmetric operator on the complement.

For this packet `Theta=1`. It lies at the exact `k=1` endpoint: the outside covariance is zero on `f` and equals `1/2` on `f^perp`.

## Precise survivor

The torsion vanishes exactly when

`det(f,Kf,q)=0`,

i.e. when `Kf` lies in the plane `span(f,q)`. Thus the `k=1` rank-split debt is no longer an undifferentiated “outside plane” case at the exact-zero physical endpoint. It splits into:

1. `Theta` quantitative: paid above by a genuine physical two-row wedge and direct linear anti-concentration;
2. `Theta` small/zero: an invariant-plane / lightcone-type coefficient geometry; or
3. nonzero physical two-hub core: the near-null interpolation still needs the external third source-compatible smoother and cannot be deleted as a small coefficient perturbation.

The full conjecture remains OPEN.
