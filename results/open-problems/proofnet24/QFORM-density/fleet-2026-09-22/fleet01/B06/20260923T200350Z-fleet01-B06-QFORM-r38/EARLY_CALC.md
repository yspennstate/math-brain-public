SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B06, 2026-09-23T20:03:50Z.
attacking: remove the remaining rank-two volume row-marginal gate from the shared-index physical-pivot receiver, using fleet02/B06's new row-gate-free E2 half-Riesz theorem before any reciprocal-minor selection.

# Early calculation — row-gate-free shared-index pivot splice

Let `i` be an original physical coordinate with scalar pivot `c=A_ii!=0`. Completing the square in the genuine independent scalar `X_i` gives

`Q = c (X_i + Psi(X_{-i}))^2 + S(X_{-i})`,

where `S` is a quadratic-affine polynomial in the remaining independent original coordinates. Hence the standard square kernel gives

`||p_Q||_infinity <= |c|^(-1/2) H_(1/2)(S)`,

where `H_(1/2)(S)=sup_t E|S-t|^(-1/2)`.

In the r32 shared-index bordered packet, define

`S_i^off = sum_{j!=k; j,k!=i} D_({i,j},{i,k})^2`.

The exact Schur-minor identity

`D_({i,j},{i,k}) = c det A^(i)[{X,j},{Y,k}]`

and a fair random cut of the remaining physical background coordinates give a literal disjoint original-coordinate cross block `M_cut` of the Schur form `S` satisfying

`Z_2 := e_2(M_cut^T M_cut) >= S_i^off/(4c^2)`.

The fresh designated-partner theorem fleet02/B06,
`QFORM-E2-HALFRIESZ-ROW-GATE-FREE-v1`, canonical commit
`b38a9627f059b13d532f5c208c30579ec2d2d362`, states for any such literal cross block, with arbitrary same-bank curvature and affine terms and with NO volume-row-marginal hypothesis,

`H_(1/2)(S) <= 8 e^(1/4) Z_2^(-1/8)`.

Therefore

`||p_Q||_infinity
 <= |c|^(-1/2) 8 e^(1/4) [S_i^off/(4c^2)]^(-1/8)
 = 8 (2e)^(1/4) |c|^(-1/4) (S_i^off)^(-1/8)`.

Thus the old r32 obstruction “every cut carrying the shared-index packet has a heavy E2 volume-sampling row” disappears completely. The remaining local debt is only small physical pivot or concentration of the shared-index packet on the diagonal terms `D_({i,j},{i,j})`.

Within the r30/r32 high-collision/low-tail transverse-curvature chamber, r32 gives `W_i^L >= (81/65536) W`, while the preceding transverse branch has `W>s^6/128`, `s=s_3(A)`. Hence if `S_i^off >= W_i^L/2` and `|c|>=s/16`, then

`S_i^off > 81 s^6 / 2^24`

and the new splice yields

`||p_Q||_infinity < 112.845/s`.

This is a scoped density branch, not the full conjecture. Continuity is not claimed by this square-peel/half-Riesz splice.