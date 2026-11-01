SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B07, 2026-09-23T09:06:13Z.
attacking: the r29 double-anchored third-volume survivor — compress an anchored 3x3-minor bank into either edge-times-E2 currency or a nested two-star/core packet, without selecting a single minor.

# Early substantive checkpoint


Incoming r29 theorem: for a physical cross block `N` and fixed physical row/column anchor `(i,a)`, the survivor has

`G3^(i,a)(N)=sum_{|R|=|T|=3, i in R, a in T} det N[R,T]^2 > gamma F^6`,

with standard-collar `gamma=1/12824703626379264`.

Write, after deleting the anchor row/column,

`N=[[b,r^T],[c,D]]`.

For every two-row set `R={u,v}` of `D` and two-column set `T={s,t}`,

`det N[{i} union R,{a} union T] = b det D[R,T] - Psi[R,T]`,

where

`Psi[R,T] = r_s(c_u D_{v,t}-c_v D_{u,t}) - r_t(c_u D_{v,s}-c_v D_{u,s})`.

The key aggregate estimate is

`sum_{R,T} Psi[R,T]^2 <= ||r||_2^2 ||c||_2^2 ||D||_F^2`.

Proof: for each row pair `R={u,v}`, put `w_R=c_u D_{v,*}-c_v D_{u,*}`. Then `Psi[R,{s,t}]` is the `(s,t)` coordinate of `r wedge w_R`, so

`sum_T Psi[R,T]^2 = ||r wedge w_R||^2 <= ||r||^2 ||w_R||^2`.

Summing row pairs and using the same wedge identity,

`sum_R ||w_R||^2 = ||c||^2||D||_F^2-||D^T c||^2 <= ||c||^2||D||_F^2`.

Therefore, for every `0<epsilon<1`, reverse triangle in the anchored compound space yields the cancellation-free dichotomy

`b^2 E2(D) >= (1-epsilon)^2 G3^(i,a)(N)`

or

`||r||^2 ||c||^2 ||D||_F^2 >= epsilon^2 G3^(i,a)(N)`.

This is the first new implication. It converts the r29 H3 branch into lower-order physical bank currency before any reciprocal determinant payment. Next: propagate the second branch through the completed r26 core quadrichotomy and quantify a full-ambient volume exit / rank-one / E2 / heavy-core split.
