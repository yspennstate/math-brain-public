# account02/B08 r30 early calculation — one diagonal twist upgrades diffuse rank two

The live unpaid endpoint from B08 r29 and account03/B08 r44 is the exact aligned same-bank block

`A_bank = D + M^T C M`,

with `D` physical diagonal, `M` a two-row original-coordinate arm, and arbitrary affine terms after conditioning all other ORIGINAL coordinates.  Write the nonzero spectral factorisation of the rank-two part as

`M^T C M = R diag(lambda1,lambda2) R^T`, `R^T R=I_2`,

and let `c_i=||R_{i,:}||^2`.  The inherited diffuse arm gate gives `c_i<=1/2` (the column space is exactly `row(M)`).

For one coordinate `j` with `0<c_j<1/2` and `d_j=D_jj !=0`, the fixed-source Fresnel formula gives, for

`G_i(s,tau)=int exp(i(s x^2+tau x)) f_i(x) dx`,

`|phi(t)| <= [4 pi |t| sqrt(|lambda1 lambda2|)]^(-1)
              int_R2 prod_i |G_i(t d_i, t b_i + <R_i,u>)| du`.

Geometric Brascamp--Lieb with exponents `c_i` yields the refined inequality

`|phi(t)| <= 4 pi P^(-1/2)|t|^(-1) h_j(t)`, `P=|lambda1 lambda2|`,

where

`h_j(t)= ||G_j(t d_j,.)||_(p_j) / (4 pi sqrt(c_j))^(c_j)`,
`p_j=1/c_j`,

and the fixed-source twisted Fourier lemma gives `0<=h_j<=1`.

Now use the one-dimensional homogeneous Strichartz estimate for the parabola extension operator:

`|| ||G_j(s,.)||_p ||_(L^q_s) <= C_Str ||f_j||_2 <= C_Str`,
`2/q+1/p=1/2`.

Thus with `q=4/(1-2c_j)`,

`||h_j||_(L^q_t)
 <= |d_j|^(-1/q) C_Str /(4 pi sqrt(c_j))^(c_j)`.

For any `T>0`, Holder on `|t|>T` gives

`int |phi(t)|dt
 <= 2T + 4 pi P^(-1/2) B_j [2(q-1)]^((q-1)/q) T^(-1/q)`,

where `B_j` is the preceding `L^q` norm.  Optimising in `T` produces a finite density bound with the exact scale

`||p_Q||_infty
 <= C_FS(c_j) P^(-2/(5-2c_j)) |d_j|^(-(1-2c_j)/(5-2c_j))`.

The powers add to `-1` under coefficient scaling.  This is the missing analytic mechanism at the aligned diagonal-twist endpoint: rank two supplies the critical `|t|^-1`, while one nonzero ORIGINAL diagonal twist on a genuinely diffuse carrier row supplies an integrated-in-time Strichartz gain.  No post-rotation independence is asserted; the spectral frame is used only in deterministic Fresnel linearisation, while every stochastic factor remains an original one-dimensional density.

Immediate structural router for the exact B08 endpoint, taking a concrete diffuse threshold `h=1/4`: if `|det C| S_M^2 >= p0 L^2` and some physical diagonal twist satisfies `|d_j|>=d0 L` on a row of arm leverage `<=1/4`, this compiler gives `O_{p0,d0}(L^-1)`.  Otherwise either the aligned carrier is near rank one, every target-scale diagonal twist is supported on the fewer than eight arm-heavy physical coordinates `ell_i>1/4`, or the physical diagonal is subthreshold.  These are strictly narrower survivors than arbitrary carrier-plus-diagonal curvature.

The full conjecture remains open; this early record is not a completion claim.
