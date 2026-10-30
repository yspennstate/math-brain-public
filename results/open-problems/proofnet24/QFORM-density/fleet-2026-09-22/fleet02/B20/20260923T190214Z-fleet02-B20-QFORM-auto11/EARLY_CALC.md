# Early substantive calculation — mixed-fan Schur minor

Programme `QFORM-DENSITY-3EIG-20260922`; fleet02/B20 run `20260923T190214Z-fleet02-B20-QFORM-auto11`.

Newest completed designated input: fleet03/B20 r37 at `598dae792b4a447492bc318bfa830fece803bb6d`.  On its diffuse branch there are disjoint ORIGINAL-coordinate banks `D_1,D_2,K_1,K_2,K_3`, two-dimensional physical left frames `U_1,U_2`, and for every `r=1,2`, `b=1,2,3`,

` s_2(U_r^T A[D_r,K_b]) > a_D := 0.002408434254376076.`

For each bank choose orthonormal two-frames `R_b` and `L_b` so that

`A_b := U_1^T A[D_1,K_b]R_b`,
`B_b := L_b^T A[K_b,D_2]U_2`

are invertible `2 x 2` matrices with `s_2(A_b),s_2(B_b)>a_D`.  Put

`C_0=U_1^T A[D_1,D_2]U_2`,
`D_ab=L_a^T A[K_a,K_b]R_b`.

For `a != b`, the ACTUAL physical cross cut

`M_ab=A[D_1 union K_a, K_b union D_2]`

has the orthogonal compression

`T_ab=[[A_b,C_0],[D_ab,B_a]]`.

Define the Schur defect

`S_ab := B_a-D_ab A_b^{-1}C_0`.

For every bottom-row index `q` and every right-block column `j`, the `3 x 3` minor of `T_ab` using the two top rows, bottom row `q`, the two left-block columns, and right-block column `j` is exactly

`det(A_b) (S_ab)_{qj}`.

Therefore, using `e_3(MM^T)=||wedge^3 M||_HS^2` and contraction under orthogonal compression,

`e_3(M_ab M_ab^T) >= e_3(T_ab T_ab^T)
                      >= det(A_b)^2 ||S_ab||_F^2
                      > a_D^4 ||S_ab||_F^2.`

This is an actual ORIGINAL-coordinate third-cross-volume certificate; no random variable is rotated and no independence after rotation is used.

Taking the fixed threshold

`delta_0=a_D^2=5.800555557652045e-6`,

if any ordered pair has `||S_ab||_F>=delta_0`, the marginal-free physical `Z_3` receiver (`QFORM-Z3-CROSSING-MARGINAL-FREE-v1`, fleet02/B03) gives

`||p_Q||_infinity
 <= 10.5501688311648 (a_D^4 delta_0^2)^(-1/6)
 = 10.5501688311648 a_D^(-4/3)
 < 32679.823.`

Thus every diffuse r37 survivor not already paid by this exit satisfies, simultaneously for all six ordered pairs `a!=b`,

`||B_a-D_ab A_b^{-1}C_0||_F<a_D^2`.

Since `s_2(B_a)>a_D`, multiplying on the left by `B_a^{-1}` gives the dimensionless coherent collar

`||I_2-B_a^{-1}D_ab A_b^{-1}C_0||_op<a_D<0.002409.`

In particular `C_0` and every `D_ab` are invertible: otherwise `D_ab A_b^{-1}C_0` has rank at most one and cannot lie within operator distance `<a_D` of `B_a`, whose second singular value is `>a_D`.

This converts the diffuse 3-fan debt into either a fixed full-law payment or a simultaneous six-relation planar-twist/Schur-cancellation collar.  Full QFORM remains open; the heavy-common-anchor branch of r37 remains separate.
