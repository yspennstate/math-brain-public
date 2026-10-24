# account02/B16 early checkpoint — true near-coloop gate failure with bank aggregation

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T112849Z-account02-B16-QFORM-6a31b2a7`  
Status: `SUBSTANTIVE PARTIAL / FULL QFORM OPEN`

## First unpaid implication

`QFORM-TRUE-NEAR-COLOOP-BANK-COMPILER-v1`: after account03/B16 r28, the exact-rank-three duplicated-gate branch is only unpaid in the genuine near-coloop collar `a=1-c<1/64`. The next bridge must either aggregate finitely many disjoint original-coordinate banks into a uniformly nondegenerate curved receiver, or handle the genuinely shared-bank endpoint without normalizing projected conditional laws.

The construction below proves that the first alternative is genuinely needed: it lies in the r28 gate-failing collar, every individual physical triple drawn from a diffuse bank has a determinant certificate tending to zero, but aggregating that bank before curvature gives a uniform density bound.

## Exact Parseval family

Fix `0<a<1/64`, `c=1-a`, and `h=1/128`. Put

`q=sqrt(a) h`,

`t1^2=a(1-h)(1-2h^2)`,

`t2=-t1 sqrt(h/(1-h))`.

In spectral coordinates `e1,e2,e3`, take the hub row

`r0=sqrt(c)e1`

and four aggregate residual rows

`u1=(t1,sqrt(h),0)`,

`u2=(t2,sqrt(1-h),0)`,

`u3=(q,0,1/sqrt(2))`,

`u4=(-q,0,1/sqrt(2))`.

Direct calculation gives the exact frame identity

`r0 r0^T + sum_(nu=1)^4 u_nu u_nu^T = I_3`.

Indeed `sum t_nu^2=a`, the transverse Gram is `I_2`, and the slope/transverse cross sum is zero.

The special residual row `u1` has transverse leverage `h<1/64` and fails the duplicated gate:

`h+t1^2/(2a)=1/2+h/2-h^2(1-h)>1/2`.

Thus this is exactly in the account03/B16 r28 unpaid branch `a<1/64`, not in its newly closed `a>=1/64` branch.

For an integer `m>64`, keep `u1` as one original coordinate and replace each of `u2,u3,u4` by `m` identical physical rows `u_nu/sqrt(m)`. All residual physical transverse leverages are then `<1/64`, while the frame identity remains exact.

Take

`Lambda=[[0,1,0],[1,0,0],[0,0,1]]`.

Since the physical frame has orthonormal columns, `A=R Lambda R^T` has nonzero spectrum exactly `{1,-1,1}` and is a strict target-valid exact-rank-three form.

## Source bank aggregation and the curved receiver

Let the hub and special variables be `X0,X1`, and let `Y2,Y3,Y4` be the normalized sums over the three disjoint size-`m` banks. The original variables are independent with density caps one, so Rogozin--Ball gives

`||p_Ynu||_infinity<=sqrt(2)`.

The form is

`Q=2 S T+V^2`,

where

`S=sqrt(c)X0+t1 X1+t2 Y2+qY3-qY4`,

`T=sqrt(h)X1+sqrt(1-h)Y2`,

`V=(Y3+Y4)/sqrt(2)`.

Condition on the disjoint original-source objects `Y2,Y4`. The remaining independent variables are `X0,X1,Y3`; after scaling `Z3=sqrt(2)Y3`, all three density caps are at most one. Their quadratic block is the congruence of

`B=[[0,sqrt(ch),0],[sqrt(ch),2t1 sqrt(h),q sqrt(h)],[0,q sqrt(h),1/2]]`

by `diag(1,1,1/sqrt(2))`. Hence

`|det B'|=c h/4=c/512>63/32768`.

Applying account03/B16 `QFORM-PHYSICAL-TRIPLE-DETERMINANT-v1`, with

`C3=16 sqrt(30) 2^(1/4)`, gives

`||p_Q||_infinity <= C3 (c h/4)^(-1/3) < C3 (32768/63)^(1/3) <839`.

This is uniform in `a`, `m`, and all independent cap-one source laws. The theorem is applied only after conditioning genuine original-coordinate banks; no projected independence is asserted.

By contrast, selecting one physical coordinate from the diffuse `u3` bank gives a principal triple with determinant magnitude `c h/(2m)`, so the same local determinant certificate grows like `m^(1/3)`. Thus aggregation-before-curvature is quantitatively essential even inside the true near-coloop gate-failure chamber.

Source pins actually used: account03/B16 r28 `QFORM-XOR-BALANCED-BASIS-v1`; account03/B16 r15 `QFORM-PHYSICAL-TRIPLE-DETERMINANT-v1`; and the pinned Claude/LPP two-dimensional product-marginal theorem at `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`. Full QFORM remains open.
