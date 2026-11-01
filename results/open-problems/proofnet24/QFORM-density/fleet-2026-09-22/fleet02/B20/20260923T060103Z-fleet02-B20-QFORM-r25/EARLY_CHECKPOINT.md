# fleet02/B20 r25 — early substantive checkpoint

Programme: `QFORM-DENSITY-3EIG-20260922`. Status: `ESSENTIAL_STEP_APPLIED / NEW AGGREGATE COMPILER / FULL TARGET OPEN`.

All matrices and random variables below remain in original physical coordinates. No post-rotation independence, uniform pointwise quadratic-phase decay, arbitrary-joint coarea, or worst-fiber supremum is used.

## Source inputs actually applied

The newest completed designated-partner report used is fleet03/B20 r26, `yspennstate/math-open-problems@766e706f955b5cf514e00be2a14fc856d65c2244`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B20/20260923T044630Z-fleet03-B20-QFORM-r26/REPORT.md`. In the surviving exact-rank-three collar it proves that a physical anchor `i` has an aggregate anchored compound packet

`max(P_i,M_i,D_i)>1/192`,

unless an earlier paid branch has already fired. Here, with rows ordered as `(i,j,K)`, `r_i=(a,b_j,b_K)`, `r_j=(b_j,H_jj,H[j,K])`,

`P_i=sum_j (a H_jj-b_j^2)^2`,

`M_i=sum_j ||a H[j,K]-b_j b_K||^2 + sum_j ||b_j H[j,K]-H_jj b_K||^2`,

and `D_i` is the sum of the fully disjoint `2x2` physical-minor squares.

The required pinned interactive source `e5f71d79eff325201dd0274053d20268ce65b837` supplies D'/three-volume and D5. In particular the q=4/3 three-volume form gives

`||p_Q||_inf <= (9 sqrt(3)e/2) Z_3^(-1/6)`

when an ORIGINAL-coordinate cross block has row third-volume marginals at most `2/3`.

## New theorem: anchored compound -> three low-rank aggregate packets

Write the exact-rank-three physical matrix around anchor `i` as

`A=[[a,b^T],[b,H]]`.

Split `M_i=M_i^(1)+M_i^(2)` according to its two displayed sums and define

`T:=aH-bb^T`,

`N:=diag(b)H-d b^T`, where `d=(H_jj)_j`.

Then exactly

`P_i+M_i^(1)=||T||_F^2`,                                      (1)

`M_i^(2)=||N||_F^2`.                                          (2)

Moreover `rank(T)<=2` and `rank(N)<=4`. For `T`: if `a!=0`, the physical Schur congruence sends `A` to `diag(a,H-bb^T/a)`, so exact rank three gives `rank(H-bb^T/a)=2` and hence `rank(T)=2`; if `a=0`, then `T=-bb^T` has rank at most one. For `N`, `diag(b)H` has rank at most three and `d b^T` rank at most one.

Consequently the partner packet with `mu:=1/192` implies at least one of the following:

(A) `||T||_op > sqrt(mu/4)=1/(16 sqrt(3))`;

(B) `||N||_op > sqrt(mu/8)=1/(16 sqrt(6))`;

(C) there is an actual original-coordinate physical cut `C=A[{i} union L,R]` with

`e_2(CC^T)>mu/8=1/1536`.

Indeed, if `P_i>mu` or `M_i^(1)>M_i/2`, (1) and rank(T)<=2 give (A); if `M_i^(2)>M_i/2`, (2) and rank(N)<=4 give (B). If `D_i>mu`, independently color every residual physical coordinate left/right. Each fully disjoint anchored minor is captured with probability `1/8`, so Cauchy-Binet gives a deterministic cut with (C).

This theorem is named `QFORM-ANCHORED-COMPOUND-LOWRANK-COMPILER-v1`.

### Exact signed two-volume identity for T

If `A=U Lambda U^T` with `U^T U=I_3`, and `c_i=||u_i||^2`, then

`e_2(T)=a det(Lambda)c_i`.                                      (3)

For `a!=0`, `det T[{j,k}]=a det A[{i,j,k}]`. Summing over `j<k`, using `det A_S=det(Lambda) det(U_S)^2` and the determinantal inclusion identity `sum_{j<k}det(U_{i,j,k})^2=c_i`, proves (3). Since rank(T)<=2, `|e_2(T)|` is the product of its two nonzero singular values whenever rank(T)=2.

## Paid subbranches of packet (C)

If the physical cut in (C) has rank three, `s_3(C)>=1/64`, and its row third-volume marginals are at most `2/3`, then

`e_2(CC^T)<=3 s_1(C)^2s_2(C)^2`,

so

`Z_3=s_1^2s_2^2s_3^2 > 1/(1536*3*4096)`.

The pinned q=4/3 D' receiver therefore gives a continuous density with

`||p_Q||_inf < 346`.                                             (4)

If instead `rank(C)=2` and the source-bank self-curvature transverse to the cross range is at least `1/64` in the exact scope of fleet03/B19 r26's `QFORM-RANK2-CROSS-TRANSVERSE-3D-CURVATURE-v1`, then `(s_1s_2)^2=e_2(CC^T)>1/1536`, and its exact estimate

`||p_Q||inf < 12.01 |lambda|^(-1/4)(s_1s_2)^(-3/8)`

gives

`||p_Q||inf < 135`.                                             (5)

Thus packet (C) is already paid in its rank-three diffuse-tail and rank-two transverse-curvature subbranches. The remaining (C) debt is low third singular value/high leverage, or rank-two near-range self curvature.

## Route counterexample: no single-minor extraction from anchored principal compound

Fix `0<c<1`, `mu>0`, and integer `m`. In R^3 put

`q=(1,1,0)/sqrt(2)`, `r=(1,-1,0)/sqrt(2)`, `e=(0,0,1)`, `J=diag(1,-1,1)`.

Build an `(1+3m)x3` matrix `U` with rows

- anchor `sqrt(c) q`;
- `m` q-rows `sqrt((1-c)/m) q`;
- `m` r-rows `m^(-1/2)r`;
- `m` e-rows `m^(-1/2)e`.

Then `U^TU=I_3`. Set

`t=(mu*m/c^2)^(1/4)`, `A_m=t U J U^T`.

The three nonzero eigenvalues are `t,-t,t`. The anchor and all q/r diagonals vanish, e-diagonals equal `t/m ->0`, and the largest physical entry is the anchor-r edge

`beta=t sqrt(c/m)=mu^(1/4)m^(-1/4)`.

The anchor principal currency is exactly

`P_0=m beta^4=mu`,                                               (6)

while every physical `2x2` minor is `O(beta^2)=O(m^(-1/2)) ->0`.

Hence a fixed aggregate anchored principal compound packet does NOT force a universally large physical local minor, even in exact rank three with all three nonzero eigenvalues eventually at least one. This refutes that closure shortcut, not QFORM.

For the concrete choice `c=1/2`, every spectral-frame leverage is at most `1/2`. The pinned Theorem F therefore applies to the same stress family and gives

`||p_(Q_m)||_inf <= 12/t <=12` for `t>=1`.                       (7)

Thus the family simultaneously demonstrates why local-minor extraction fails and why aggregate diffuse Fourier smoothing is the right currency.

## First unpaid implication

`QFORM-O3-COMPOUND-AGGREGATE-PACKET-PAYMENT-v1`: in the exact-rank-three collar, pay packet (A), packet (B), and the low-rank/high-leverage or near-range residual of packet (C), under arbitrary cap-one product inputs and arbitrary ambient couplings, without selecting a vanishing physical minor. The explicit family above shows the proof must aggregate before inversion.
