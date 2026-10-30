SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B02, 2026-09-24T03:49:30Z.
attacking: the r44 active-hub/aligned-rank-two survivor — turn failure of punctured same-bank third-volume exits into a sharper diagonal + rank-at-most-16 coefficient normal form, then re-run the integrated-Fourier carrier compiler.

# fleet01/B02 r44b — early calculation

Full QFORM remains OPEN. All coordinates below are literal original independent coordinates. This calculation does not rotate the random vector, discard a quadratic tail probabilistically, assume moments/support/log-concavity, or use pointwise van-der-Corput decay.

Start from the r43/r44 full-cut ultra-rank-two packet. Let `S|T` be the full physical cut, `M=A[S,T]`, and let `x1>=x2>=...` be the squared singular values. The live packet has

`P:=x1*x2 > 274877906935/618475290624 = 0.4444444444298925...`,
`rho^2:=sum_(j>=3) xj < T_*:=7.993605777562852e-15`,
`zeta:=2^-48`.

For `k in S`, put `b_k=A[S\{k},k]`, let `u1,u2` be the top two left singular vectors of M, `ell_k=u1(k)^2+u2(k)^2`, and

`d_k=dist(b_k,span(u1^(-k),u2^(-k)))`.

Define the punctured third-volume mass

`W_S=sum_k sum_{|R|=3, R subset S\{k}} sum_{|C|=2,C subset T} det([M[R,C],b_k[R]])^2`,

and define `W_T` by transposition. A fair Bernoulli split `L subset S` makes every determinant in `W_S` a literal 3x3 minor of the full physical cut `A[L,T union (S\L)]` with probability `1/16`; hence some cut has `E3>=W_S/16`. Therefore, by the completed fleet02/B02 physical-E3 Fourier theorem, either `W_S>=16 zeta` or `W_T>=16 zeta` pays the ambient law with

`||p_Q||inf <= C3 zeta^(-1/6) = 256 C3 <2648.342`,
`integral |phi_Q| <=2 pi 256 C3 <16640.020`,
`C3=10.345083232147514...`,

and continuous C0 density.

On the still-unpaid branch, `W_S,W_T<16 zeta`. The exact exterior identity gives

`W_S >= P sum_k (1-ell_k)d_k^2`.

Since `sum ell_k=2`, the exceptional set `E_S={k:ell_k>3/4}` has size at most two. Hence

`sum_(k notin E_S) d_k^2 < 64 zeta/P`.

For every nonexceptional k choose a least-squares coefficient `c_k in R^2`; set `c_k=0` on the exceptional set, and let `U=(u1,u2)`, `C=(c_k)_k`. For i,k both nonexceptional and i!=k, with residuals `r_ik=A_ik-u_i.c_k`, symmetry gives

`A_ik - (u_i.c_k+c_i.u_k)/2 = (r_ik+r_ki)/2`.

Thus, after absorbing the diagonal exactly,

`A[S,S]=D_S + L_S + K_S + E_S^rem`,
`L_S=(UC^T+CU^T)/2`, `rank L_S<=4`,
`K_S` supported on the at-most-two exceptional rows/columns, `rank K_S<=4`,
`||E_S^rem||F^2 <=64 zeta/P`.

The same holds on T. Let `M_2=s1 u1 v1^T+s2 u2 v2^T`. The global aligned matrix made from `L_S,L_T,M_2,M_2^T` has rank at most EIGHT, not twelve: its range lies in `span(U,C_S)` on S plus `span(V,C_T)` on T, while the cross term already lies in the U/V part of this same eight-dimensional space. The two exceptional row/column matrices contribute rank at most eight total. Therefore

`A=D+R_16+E_0`,
`rank R_16<=16`,
`||E_0||F^2 <128 zeta/P +2 T_* =130 zeta/P`,
so
`||E_0||F <1.019396267936651e-6`.

This rank-16 normal form is the substantive new step to complete and source-pin in REPORT.md. If the existing many-diagonal coordinate-core exit does not fire, absorbing at most 22 diagonal entries of magnitude >=1/8 leaves a rank-at-most-38 carrier instead of r43's rank-at-most-42 carrier. The next calculation will re-run the r44 spectral-gap/leverage fork with rank 38 and apply fleet02/B02 to the diffuse physical-E3 exit.
