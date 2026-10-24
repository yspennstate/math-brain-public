SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B06, 2026-09-23T09:13:15Z.
attacking: the near-total heavy right-plane hub left by r25; rotate the full right coefficient plane so the near-null physical square coefficient is exchanged for a residual product square, then keep the hyperbolic physical hub exactly.

# Early substantive checkpoint — exact total-hub rotation

The preceding account01/B06 r25 leaves, in the exact-rank-three zero-Schur-diagonal branch,

- `y^2>1/2`, with `m=rho y`;
- a right-plane Parseval frame `(q,v)` and `h=beta v+m q`;
- a heavy physical row `r` with leverage `ell_r=q_r^2+v_r^2>1/2`;
- on the still-unpaid non-null branch, `tau_r=|h_r|/rho<1/8`.

I attack the exact endpoint `ell_r=1` first. Put

`c^2=m^2+beta^2`, `t=m v-beta q`.

Then `h perp t`, `||h||=||t||=c`, and

`v=(beta h+m t)/c^2`.

Hence the full right-bank form rewrites exactly as

`Q=(1/a)(h.X_R+eta(Omega))^2 + 2 d U (t.X_R)+F(Omega)`,

where `d=sigma m/c^2`, `U=u.X_L`, and `eta,F` are arbitrary functions of the disjoint left/outside state `Omega`. This uses no post-rotation independence: `h.X_R,t.X_R` are kept as projections of the same original product bank.

Normalize the two coefficient rows by `c`. Their row leverage is unchanged from `(q,v)`. If `ell_r=1`, the remaining rows form a rank-one Parseval residue. Writing `R={r} union T`, one gets

`t_T=lambda h_T`, `lambda=-h_r/t_r`,

and necessarily `t_r!=0` in the live `tau_r<1/8` branch. Since `h perp t`,

`||h_T||=|t_r|`, `h_r^2+t_r^2=c^2`.

With `X=X_r`, `H=h_T.X_T`, exact completion gives

`Q=(1/a)(H+h_r X+eta+a d lambda U)^2
   +2 d U (t_r-lambda h_r)X+F_1(Omega)`

and

`t_r-lambda h_r=c^2/t_r`.

Thus, after `W=H/||h_T||`,

`Q=A_0(W+S(Omega,X))^2+2d_0 U X+F_1(Omega)`,

`A_0=t_r^2/a`, `d_0=sigma m/t_r`.

This is the dependent-centre physical chain of r25, except that the square variable `W` is a normalized product projection rather than a cap-one physical scalar. The newest-Claude one-sided square kernel multiplies linearly by the density cap `J=||p_W||_infty`; the same r25 proof therefore gives

`||p_Q||_infty <=4 J sqrt(LK)/sqrt(|A_0d_0|)`

when `U,X` have density caps `L,K` and all three source banks are independent. The designated account02/B06 weighted affine-fiber theorem supplies the actual inequalities

`J<=sqrt(e)`, `L<=sqrt(e)`, `K<=1`,

so

`||p_Q||_infty <=4 e^(3/4)/sqrt(|A_0d_0|)`.

Finally

`|A_0d_0|=|sigma|m|t_r|/|a|`.

The live inequalities `m>rho/sqrt(2)`, `c>=m`, and `|h_r|<rho/8` give

`|t_r|=sqrt(c^2-h_r^2)>rho sqrt(31)/8`.

Using the predecessor spectral identity

`(|sigma|rho^2/|a|)>=s_3(A)^2`,

we obtain

`|A_0d_0|>s_3(A)^2 sqrt(31)/(8sqrt(2))`,

hence

`||p_Q||_infty < C_totalhub/s_3(A)`,

`C_totalhub=4 e^(3/4) sqrt(8sqrt(2)/sqrt(31))=12.07099087746...`.

So the exact near-total endpoint `ell_r=1` is uniformly paid even though the original physical square coefficient `h_r` tends to zero. The next debt is the collar `7/8<ell_r<1`, where the residual right coefficient plane is rank two and its small transverse component cannot be discarded as a small random perturbation under unbounded input laws.
