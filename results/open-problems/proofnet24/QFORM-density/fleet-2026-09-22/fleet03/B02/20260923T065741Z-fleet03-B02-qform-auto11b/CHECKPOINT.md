SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B02, 2026-09-23T06:57:41Z.
attacking: the small-F / two-heavy-star correction packet; extract a new physical third-volume block before reciprocal payment, then apply the fractional-volume Fourier theorem only when its determinant-weighted marginal gate is actually satisfied.

# Substantive checkpoint — star-plane to physical E3

Programme `QFORM-DENSITY-3EIG-20260922`; full target OPEN. Source control observed at this stage: `yspennstate/math-research-brain@3472b73338c7b2861bdfbd103b7081905c4bd05a`, owner revision `2026-09-22.15`. Execution remains `WITHOUT_VERIFIED_BRAIN`.

Use the correction-safe r21 notation. For physical anchors `x,y` and residual original-coordinate banks `U,V`, put

`d=A_xx`, `e=A_yy`, `a=A_xy`, `delta=de-a^2`,
`u=A[U,x]`, `c=A[U,y]`, `r=A[x,V]`, `v=A[y,V]`, `N=A[U,V]`,

`xi=a u-d c`, `eta=a v-e r`,

and for `delta!=0`

`T=N-[u,c] [[d,a],[a,e]]^(-1) [r;v]`.

The preceding compiler's unpaid same-side resource is

`Rcorr=(||xi||^2 ||eta||^2/delta^2) F^2`,
`F=||P_(xi^perp) T P_(eta^perp)||_F`.

On the q=4/3 third-volume gate-failure branch it has `Rcorr>Z/12`, where `Z` is the original physical cross block's third volume.

Define the two star planes

`U0=span{u,c}`, `V0=span{r,v}`,

and the companion star vectors

`chi=a c-e u`, `zeta=a r-d v`.

Since

`xi wedge chi = -delta (u wedge c)`,
`eta wedge zeta =  delta (r wedge v)`,

put

`q_U=P_(xi^perp) chi`, `q_V=P_(eta^perp) zeta`.

When the correction resource is nonzero, xi and eta are nonzero, and therefore

`||u wedge c|| = ||xi|| ||q_U||/|delta|`,
`||r wedge v|| = ||eta|| ||q_V||/|delta|`.                 (C.1)

Now define the actual physical cross blocks

`M_U=A[U,{x,y} union V]=[u,c,N]`,
`M_V=A[{x,y} union U,V]=[r^T;v^T;N]`.

Because the rank-two correction from N to T has range in U0 and row-space in V0,

`P_(U0^perp)T=P_(U0^perp)N`,
`T P_(V0^perp)=N P_(V0^perp)`.                                  (C.2)

Set

`F_U=||P_(U0^perp) T P_(eta^perp)||_F`,
`F_V=||P_(xi^perp) T P_(V0^perp)||_F`.

Summing only the 3x3 minors of M_U using both special columns u,c and one V-column gives, by Cauchy--Binet / exterior algebra,

`E3(M_U) >= ||u wedge c||^2 ||P_(U0^perp)N||_F^2
          >= (||xi||^2 ||q_U||^2/delta^2) F_U^2`.             (C.3)

Similarly

`E3(M_V) >= (||eta||^2 ||q_V||^2/delta^2) F_V^2`.             (C.4)

Consequently, for every theta in (0,1],

`q_U F_U >= theta ||eta|| F  =>  E3(M_U) >= theta^2 Rcorr`,
`q_V F_V >= theta ||xi|| F   =>  E3(M_V) >= theta^2 Rcorr`.    (C.5)

Thus on `Rcorr>Z/12`, either of these inequalities turns the same-side correction packet into a literal physical third-volume block of size `>theta^2 Z/12`, before selecting any individual minor.

Now apply the newest fractional-volume theorem at its exact gate. If the normalized squared-3x3-minor row marginals of the relevant M_U (or, after transposition, its column marginals) satisfy `alpha_i<=q/2`, `1<=q<3/2`, then

`||p_Q||_infinity <= [3e/((3-2q)sqrt(q))] E3(M_U)^(-1/6)`

with a continuous density. Combining with (C.5) and `Rcorr>Z/12` gives

`||p_Q||_infinity
 < [3e/((3-2q)sqrt(q))] (12/theta^2)^(1/6) Z^(-1/6)`.         (C.6)

The same statement holds with M_V. At `q=4/3`, `theta=1/2`, the new physical volume exceeds `Z/48` and

`||p_Q||_infinity < [(9sqrt(3)e)/2] 48^(1/6) Z^(-1/6)`,       (C.7)

again with continuity.

This is a genuinely new correction-safe exit: it applies the current fractional-volume result with every marginal gate retained. What remains if the exit does not fire is explicit: the correction mass must either have small star-plane companion/deep-transverse product (`q_U F_U` and `q_V F_V`), or the newly exposed physical E3 block itself has a heavy determinant-weighted marginal. Those are structural cases, not a silently dropped gate.
