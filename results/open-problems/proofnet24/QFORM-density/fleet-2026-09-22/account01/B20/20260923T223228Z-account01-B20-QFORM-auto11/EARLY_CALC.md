# Early calculation — exact common-Gram escape cannot hide on the six controlled source arms

Status: supporting implication proved; unrestricted QFORM remains OPEN; continuity remains separate except on branches paid by the physical E3 receiver.

Run: `20260923T223228Z-account01-B20-QFORM-auto11`.

Completed designated partner consumed: account02/B20 `QFORM-R37-EXACT-COMMONGRAM-THIRDMODE-ESCAPE-v1`, canonical package `yspennstate/math-open-problems@edefefbd4d25c1c870330eb976e47a9356f7f4a0`, whose exact common-Gram endpoint gives

`max{ ||P A Q||_op, max_i ||Delta_i||_op, ||Q A Q||_op } >= 1/2`.

Here the five pairwise orthogonal planar frames are `U_1,W_1,W_2,W_3,U_2` on the disjoint physical nodes `D_1,K_1,K_2,K_3,D_2`; `P` is their sum and `Q=I-P`.

The earlier source packet has

`N_r=A[D_r,K]`, `E_r=N_r(I-Q_*)`,
`||E_1||_F^2+||E_2||_F^2 < epsilon^2`,
`epsilon=0.0023595307563857772`,

and the canonical physical `W_b=P_(K_b)V G_b^(-1/2)` frames. Let `Q_(D_r)` be the complement of `U_r` inside `D_r`, and `Q_(K_b)` the complement of `W_b` inside `K_b`.

For `v in ran Q_(K_b)`, support in `K_b` and `W_b^T v=0` imply

`0=W_b^T v=G_b^(-1/2)V^T P_(K_b)v=G_b^(-1/2)V^T v`,

so `V^T v=0`, hence `Q_*v=0`. Therefore

`||P_(D_r) A Q_(K_b)||_op <= ||E_r||_op < epsilon`,
`||Q_(D_r) A Q_(K_b)||_op < epsilon`.

For `w in ran W_b`, the vector `N_r Q_* w` lies in `ran U_r`, so

`Q_(D_r)N_r w=Q_(D_r)E_r w`,

and therefore

`||Q_(D_r) A P_(K_b)||_op < epsilon`.

By symmetry the same bounds hold in the reverse orientations. Thus every plane/complement or complement/complement block across each of the six strong source arms

`D_1-K_b`, `K_b-D_2`, `b=1,2,3`,

has operator norm `<epsilon`.

Now decompose the partner escape blockwise. In `P A Q` there are `5*6=30` frame/complement blocks. Exactly 12 oriented blocks lie on the six strong arms. The elementary block estimate

`||T||_op <= (sum_(i,r) ||T_ir||_op^2)^(1/2)`

shows that the arm-supported part has norm `<sqrt(12) epsilon`. Hence, if `||P A Q||_op>=1/2`, the non-arm part has norm `>1/2-sqrt(12)epsilon`. It has only 18 blocks, so at least one NON-ARM physical plane/complement block obeys

`||P_i A Q_r||_op > delta_PQ := (1/2-sqrt(12)epsilon)/sqrt(18)
 =0.11592458140257514...`.

Likewise `Q A Q` has `6*6=36` blocks; 12 oriented blocks lie on the six strong arms and 24 do not. Therefore, if `||Q A Q||_op>=1/2`, at least one NON-ARM physical complement/complement block obeys

`||Q_r A Q_s||_op > delta_QQ := (1/2-sqrt(12)epsilon)/sqrt(24)
 =0.10039363241770716...`.

Consequently the completed account02/B20 escape theorem sharpens, on the actual source packet, to the exhaustive alternative

1. `max_i ||Delta_i||_op >=1/2`; or
2. a non-arm physical plane/complement interaction has norm `>0.11592458`; or
3. a non-arm physical complement/complement interaction has norm `>0.10039363`.

Here “non-arm” means same-node, `D_1-D_2`, `K_a-K_b (a!=b)`, or any interaction involving the exterior node; none of the six already controlled `D_1-K_b` / `K_b-D_2` source arms can carry the forced third mode.

This is an equation-level use of the completed account02/B20 result, not merely a citation. It preserves the nonzero source tail; the tail is used to exclude the arm locations rather than deleted from the random polynomial.

Corrections preserved: no uniform pointwise quadratic oscillatory decay; no independence after rotation; no arbitrary-joint coarea; no conditional-cap shortcut; no one-good-minor inference; no deletion of a nonzero random tail.
