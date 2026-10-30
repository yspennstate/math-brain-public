SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B09, 2026-09-23T12:14:44Z.
attacking: elevate the center of an arbitrary original-coordinate leaf-star curvature packet into the hub side, then close the exact rank-two augmented cross branch without square-root small-ball loss.

# Early substantive checkpoint

Work in strict `N3(tau)` with `tau=1/128`: `s_3(A)>=1`, every `|A_ii|<tau`, and every physical pair determinant has magnitude `<tau`. Put

`eta=sqrt(tau+tau^2)=0.08873294290312927`.

Then every physical off-diagonal coefficient satisfies

`|A_ij|^2 <= |A_ii A_jj|+|det A[{i,j}]| < tau^2+tau`,

hence `|A_ij|<eta`.

Assume a literal two-hub/leaf packet whose arbitrary within-leaf off-diagonal curvature is a star centered at one original leaf `s`: on `R=L\{s}`, the block `A_RR` is diagonal, while `d=A[R,s]` is arbitrary. Elevate the original coordinate `s` into the hub set `K={h1,h2,s}`. The surviving leaf self-block is diagonal and the exact physical cross is

`M=A[R,K]=[C_R,d]`.

This is only a repartition of original independent coordinates; no rotated coordinate is declared independent.

For the augmented cross, the self-block remainder has norm

`b <= tau+2 eta = 0.18527838580625855`.

If `rank M=1`, the pure symmetric cross matrix has rank at most two, so Weyl gives `s_3(A)<=b<1`, contradiction. Thus `rank M>=2`.

If `rank M=2`, write `M=C P^T` with `P^T P=I_2`. Since the pure cross has singular values `sigma_1,sigma_1,sigma_2,sigma_2`, Weyl gives

`sigma_2(M)>=1-b`.

Consequently `det(C^T C)^(1/4)=sqrt(sigma_1 sigma_2)>=1-b`.

The remaining issue is the whitened two-frame disjoint-basis mass `rho`. The intended closure is:

* if `rho>=10^-6`, apply the completed two-hub Pluecker smoother to obtain
  `||p_Q||_inf <= 2e [rho det(C^T C)]^(-1/4) <= 211.016`, with a continuous density and the same coefficient times interval length;
* if `rho<10^-6`, use the completed weighted two-frame EKR stability. The near-star alternative will be contradicted by elevating the high-leverage physical leaf and approximating the residual cross by rank one. The near-triangle alternative will be contradicted by a direct operator-norm bound on the six-coordinate physical core plus its Pluecker-controlled cross tail.

For the triangle constants, with `tau_EKR=(10^-6/2)^(1/3)=0.007937005259841` and `delta=10^-6+tau_EKR/(1-tau_EKR)=0.008001505312588399`, the high-leverage threshold is `1-2delta=0.9839969893748232`. The maximum augmented physical row norm is `r0=sqrt(3)eta=0.15368996541332813`. The planned high-leverage residual estimate is

`tau+3eta+r0 sqrt((2delta)/(1-2delta)) = 0.293611031005538 <1`.

If the triangle branch has no such high leverage, every internal triangle edge has Pluecker weight at least `delta`, while total outside-edge weight is at most `delta`. For an internal basis pair this implies

`||C_out||_op <= ||C_out||_F <= sqrt(2) r0=sqrt(6)eta`,

and therefore the full matrix norm is bounded by

`2tau+5eta+sqrt(6)eta = 0.6766401480038269 <1`,

again contradicting `s_3(A)>=1`.

This checkpoint is not yet the final proof; the next step is to write the two small geometric estimates carefully and source-pin the exact smoothing/stability inputs.
