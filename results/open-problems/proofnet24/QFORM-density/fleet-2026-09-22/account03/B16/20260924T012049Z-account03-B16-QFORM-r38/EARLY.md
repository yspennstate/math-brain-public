SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B16, 2026-09-24T01:20:49Z.
attacking: the slope-dominant punctured near-coloop by quantifying where its third projection direction actually lives; test whether the new order-one normalized slope supplies a genuine per-bank 3D puncture or only mixed two-bank volume.

Early calculation. In the balanced two-bank exact-rank-three packet write each leaf row as r_i=(alpha_i,z_i), G_B=sum_{i in B} z_i z_i^T, alpha_B=Z_B^T q_B+eta_B, Z_B eta_B=0, delta_B=||eta_B||, d=q_J-q_K, and epsilon=1-h. The completed partner identity gives

epsilon=delta_J^2+delta_K^2+d^T G_J G_K d,
q_J=G_K d, q_K=-G_J d,
(1/4)I<=G_J,G_K<=(3/4)I.

For the 3-row coefficient Gram of one normalized bank (transverse two rows plus alpha_B/sqrt(epsilon)), Schur completion gives exactly

det Gram_B = (delta_B^2/epsilon) det G_B.

Thus the slope q_B, despite being order sqrt(epsilon) on the partner's slope-dominant branch, cancels identically from every per-bank 3D projection determinant. This already shows that the newest 3D-per-bank punctured theorem cannot simply be fed the normalized slope.

The next calculation is to resolve the mixed Pluecker mass into the two orientations JJ|K and J|KK. Writing S_B=sum_{i in B} r_i r_i^T, the coefficients of det(S_J+tS_K) give

M_JJK = det(G_J)[delta_K^2+d^T G_K d] + delta_J^2 tr(adj(G_J)G_K),
M_JKK = det(G_K)[delta_J^2+d^T G_J d] + delta_K^2 tr(adj(G_K)G_J).

On the partner slope branch d^T G_JG_K d>epsilon/2, balancedness implies each slope term is >=(1/4)d^T G_JG_K d, hence M_JJK>epsilon/8 and M_JKK>epsilon/8. The third direction is therefore quantitatively present in BOTH mixed orientations even when each individual bank is rank two. Final report will prove these identities carefully and test the sharp innovation-free model.
