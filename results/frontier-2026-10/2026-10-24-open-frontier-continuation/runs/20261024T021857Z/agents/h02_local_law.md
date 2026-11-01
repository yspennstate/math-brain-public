# T384: selected local network law in the positive-correlation double-sliding cone

**Status.** Conditional local theorem for actual simultaneous GD at fixed multiplier `gamma>0`, with two unit inputs and `0<rho<1`. It uses the proved initial joint limit and finite boundary grid in `../../20261023T232238Z/BOUNDARY_GRID.md`, and the finite-horizon bootstrap, exact output identity, and small-endpoint estimate in `../../20261023T232238Z/MACRO_COMPACTNESS.md`. Its conclusion is an output/residual path law on compact intervals strictly before the selected ODE leaves the ratio cone. It makes no assertion about the path at a grazing exit or beyond the exit, and no `L^1` pre-step-kernel assertion.

## Cone, masses, and precise conclusion

Write `a=m^(1/alpha)`, `L=(log m)^(1/alpha)`, `h=gamma/L`, `z_i=W_i,0/a`, `v_i,0=XU_i,0`, `R_m=r_m(0)=y-f_m(0)`, and `C_m=C_m,0`. The projected input Gram is

\[
 G=\begin{pmatrix}1&\rho\\\rho&1\end{pmatrix},\qquad 0<\rho<1.
\]

For `r=(-p,q)`, define the continuous margin

\[
 g(r)=\min\{p,q,p-\rho q,q-\rho p\},\qquad
 \mathcal K=\{r:g(r)>0\}.                                      \tag{1}
\]

Thus `K` is exactly the stated strict cone `r_1<0<r_2`, `rho*r_2<|r_1|<r_2/rho`. The four slacks are useful at stopping times. For every initial row define the *initial-mark selector*

\[
 \sigma_i=\begin{cases}
 2,&z_i>0,\ (v_{i,0})_2>0,\\
 1,&z_i<0,\ (v_{i,0})_1>0,\\
 0,&\text{otherwise},
 \end{cases}
\qquad
 P_{j,m}=\sum_i z_i^2{\bf1}\{\sigma_i=j\},\quad
 Q_m=C_m+(1-\rho^2)\operatorname{diag}(P_{1,m},P_{2,m}).       \tag{2}
\]

The values assigned when `z_i=0` or a projection is exactly zero are immaterial. With the primitive marked Poisson measure `N` and `(F,C)` from `BOUNDARY_GRID.md`, set `R=y-F` and

\[
 P_2=\int z^2{\bf1}\{z>0,(Xu)_2>0\}\,N(dz,du),\quad
 P_1=\int z^2{\bf1}\{z<0,(Xu)_1>0\}\,N(dz,du),\quad
 Q=C+(1-\rho^2)\operatorname{diag}(P_1,P_2).                \tag{3}
\]

These sums are finite almost surely since `int z^2 N<infinity`. The initial limit gives jointly `(R_m,C_m,N_m,P_{1,m},P_{2,m},Q_m) => (R,C,N,P_1,P_2,Q)`. On `R in K`, put `r_*(t)=exp(-Qt)R` and `tau=inf{t>=0:g(r_*(t))<=0}` (with `inf(empty)=infinity`). The selected local residual is `r_*` on every compact interval `[0,T]` for which `min_{[0,T]}g(r_*)>0`; its output is `y-r_*`.

The following finite-width formulation avoids any hidden hitting-time continuity claim. Let `tau_m(delta)` be the first **grid node** `nh` at which `g(r_m(nh))<=delta`; take it to be zero if the initial node already qualifies. Let `r_m` denote the polygonal residual interpolation. For every `T<infinity`, `delta>0`, and `epsilon>0`,

\[
 \Pr\!\left( g(R_m)>2\delta,\ 
   \sup_{t\le T\wedge\tau_m(\delta)}
   \left\|r_m(t)-R_m+Q_m\int_0^t r_m(s)ds\right\|>\epsilon\right)
 \longrightarrow0.                                               \tag{4}
\]

The comparison remains true with the expression in the norm replaced by `r_m(t)-exp(-Q_m t)R_m`. In particular, for every `delta>0`,

\[
 \Pr\!\left(
 \min_{0\le t\le T}g(e^{-Q_m t}R_m)>3\delta,\ 
 \sup_{0\le t\le T}\|r_m(t)-e^{-Q_m t}R_m\|>\epsilon
 \right)\longrightarrow0.                                      \tag{5}
\]

Hence, under a joint representation of the initial primitives, `r_m` converges uniformly to `r_*` on every compact interval contained strictly in `[0,tau)`. Equivalently, (5) gives the local conditional path law without choosing a representation. Since `R` has a density, `Pr(R in K)>0` and its initial cone boundary has probability zero. The local law may be conditioned on `R_m in K` / `R in K` after the usual margin localization. There is **no assertion that** `tau_m(delta)` converges to `tau`, nor that `tau` is a transversal crossing.

The selector in (2)-(3) does not depend on `gamma` or on the numerical value of `R` *within this strict cone*. The original marked grid and `gamma` still set the finite boundary-capture step and the finite-width oscillation phase. Because `U` is symmetric, each selected half-line has mark probability `1/2`; `P_1,P_2` are independent, identically distributed positive `alpha/2`-stable variables, independent of `(F,C)`, with Laplace transform

\[
 E e^{-\lambda P_j}=\exp\{-\tfrac12 c_\alpha
 \Gamma(1-\alpha/2)\lambda^{\alpha/2}\},\qquad \lambda\ge0. \tag{6}
\]

Here `c_alpha=Gamma(alpha)sin(pi alpha/2)/pi` is the stable tail constant in `BOUNDARY_GRID.md`. This distributional observation is a consequence of independent Poisson thinning, not an additional dynamical assumption.

## Frozen finite-grid entrance and a quantitative certificate

Fix `r=(-p,q) in K`, `z ne 0`, and a generic original projection `v_0=(x_0,y_0)=Xu`. The frozen critical grid is `v_{n+1}=v_n+gamma z G D(v_n)r`. Assume first `z>0`. If `y_0<=0` and `x_0<=0`, the row is exactly dead. If `y_0<=0<x_0`, only coordinate 1 fires, and each step before death subtracts `gamma z p` from `x` and `gamma rho z p` from `y`. Thus it reaches the nonpositive quadrant in finitely many steps. If `y_0>0`, both possible gate patterns keep `y` strictly increasing:

\[
 \Delta y=\begin{cases}
 \gamma z q,&x\le0,\\
 \gamma z(q-\rho p),&x>0,
 \end{cases}                                                     \tag{7}
\]

and both are positive by (1). While `y>0`, the normal coordinate obeys

\[
 x_{n+1}-x_n=\begin{cases}
 \gamma c,&x_n\le0,\\-\gamma d,&x_n>0,
 \end{cases}\quad
 c=\rho zq>0,\quad d=z(p-\rho q)>0.                    \tag{8}
\]

It enters the invariant strip `[-gamma*d,gamma*c]` in finitely many steps. The tangential coordinate `eta=y-rho*x` obeys exactly

\[
 \eta_{n+1}-\eta_n=\gamma(1-\rho^2)zq>0.             \tag{9}
\]

Choose any deterministic `C_*>c`, `D_*>d`. At a further finite step, the orbit has the **strict certificate**

\[
 -\gamma D_*<x_n<\gamma C_*,\qquad
 \eta_n>\rho\gamma D_*+\xi                              \tag{10}
\]

for some `xi>0`. The broad strip is invariant for all later coefficients `0<c_j<=C_*`, `0<d_j<=D_*` as long as the second gate is positive, and (9) with `z_jr_{2,j}>0` makes `eta` increase. Since `y_j=eta_j+rho*x_j>eta_j-rho*gamma D_*>0`, (10) itself certifies that the second gate stays positive. This is a robust finite-step certificate under an evolving residual, not a limit-only sliding statement. It is expressed in the **unscaled** projected coordinate `v`; for `q_i=v_i/L`, its strip and tangential threshold are `[-hD_*,hC_*]` and `rho*hD_*`.

For `z<0`, interchange coordinates and put `w=|z|`. The selected case is `x_0>0`, the normal coordinate is `y`, the support is `x`, and

\[
 c=\rho w p>0,\qquad d=w(q-\rho p)>0,\qquad
 \eta=x-\rho y,\quad \Delta\eta=\gamma(1-\rho^2)wp>0.       \tag{11}
\]

It obtains the mirrored certificate `-gamma D_*<y<gamma C_*`, `x-rho*y>rho*gamma D_*+xi`. An initial `x<=0<y` instead moves both coordinates down until dead. Therefore the frozen selector is exactly (2) for every generic mark. Genericity is automatic almost surely for the marked PPP: for each fixed finite gate history, every tested projection is an affine function of `Xu` with a nonzero coordinate coefficient; `U` has a density, `X` has rank two, and a countable union over atoms and integer steps has null probability. This excludes exact threshold hits, including the dead quadrant and certificate boundaries when needed. The inequalities in (10) can alternatively be made strict by choosing the broad `C_*,D_*` with slack and waiting one more step for `eta`.

## Matching the actual grid and retaining the certificate

Fix a finite marked cutoff `epsilon<|z|<M`, `||u||<B` with zero-intensity boundaries, and localize the initial residual and finite-horizon energy as in `MACRO_COMPACTNESS.md`. There are finitely many limiting atoms. On a residual bound `||r_n||<=R_*`, take broad constants, for example `C_*=3rho M R_*` and `D_*=3M(1+rho)R_*`, enlarged if necessary. The retained actual weights satisfy `|W_{i,n}/a-z_i|=o_P(1)` uniformly through the horizon, so eventually `|W_{i,n}/a|<=2M` and their signs are fixed. If the residual is stopped inside `g(r_n)>delta`, each positive-weight retained row has

\[
 c_{i,n}=\rho z_{i,n}r_{2,n}>0,\qquad
 d_{i,n}=-z_{i,n}(r_{1,n}+\rho r_{2,n})>0,          \tag{12}
\]

bounded above by the chosen broad constants; the mirrored inequalities hold for negative weights. The lower bounds on a finite cutoff are also strict, of order `epsilon*delta`, up to harmless fixed factors.

For each fixed integer `N`, the boundary-grid theorem gives joint matching of these actual endpoint orbits through step `N` to the frozen orbits with residual `R`, including their signs. Every retained limiting atom becomes either strictly dead or strictly certified after a finite, atom-dependent number of frozen steps. The maximum over the finite retained set is finite almost surely. One can first restrict it to `<=N_0` with arbitrarily high probability, then use the deterministic `N_0`-step convergence, and finally remove this restriction. This is the required order of limits: **no** finite-grid theorem is invoked with `N_0` growing with `m`. The strict terminal sign/certificate margins persist for the actual rows with probability tending to one. The finite-step residual drift is `O_P(N_0/L)`, so on `g(R_m)>2delta` these steps occur before `tau_m(delta)` with probability tending to one.

After this matching step, a dead retained row is exactly immobile, since both ReLU gates vanish. For a certified positive-weight row, the strip in (10) is invariant under the *actual changing* `r_{m,n},z_{i,n}` until `tau_m(delta)`, and the exact identity

\[
 \eta_{n+1}-\eta_n=h(1-\rho^2)z_{i,n}r_{2,n}>0       \tag{13}
\]

in scaled coordinates maintains the support certificate. The support coordinate is also directly increasing under the double-cone inequalities (7); (10) remains the explicit robust protection against a support loss during chatter. The negative-weight row follows (11) with its mirrored support. The boundary projection need **not** converge in sign or have finitely many switches: it remains in an `O(h)` strip while its support projection grows macroscopically.

## Actual output action and small-atom removal

For a retained positive-weight row after its certificate step, let `(x_n,y_n)=v_{i,n}/L`, `eta_n=y_n-rho*x_n`, and `p_{i,n}=z_{i,n}((x_n)_+,y_n)`. The exact product rule and (13), as in `../../20261024T012528Z/agents/g01_sliding.md`, give uniformly for all grid subintervals after capture

\[
 p_{i,\ell}-p_{i,k}
 =e_2(1-\rho^2)h\sum_{n=k}^{\ell-1} z_{i,n}^{2}r_{2,n}
 +O\!\left(h+\sup|\eta_n|\operatorname{TV}(z_i)\right).   \tag{14}
\]

The constant in `O(h)` depends on the localized retained atom and the broad strip bounds. The exact weight update gives `TV(z_i)=O(L^2/a^2)=o(1)` on a bounded physical horizon, because `||v_i/L||` and the residual are bounded; the finite-horizon row bootstrap also gives uniform `z_{i,n}->z_i`. The `O(h)` capture interval in physical time has bounded finite `N_0` steps and contributes `o_P(1)` to the output. The mirrored identity is

\[
 p_{i,\ell}-p_{i,k}
 =e_1(1-\rho^2)h\sum_{n=k}^{\ell-1} z_{i,n}^{2}r_{1,n}+o_P(1).
                                                                    \tag{15}
\]

These are *actual row outputs* with the changing output weight included. The exact network decomposition uses instead the initial-weight endpoint term

\[
 A_m(t)=L^{-1}\sum_i z_i\big[(v_i(t))_+-(v_i(0))_+\big],     \tag{16}
\]

with polygonal interpolation. For a finite retained set, replacing the actual `p_{i,n}-p_{i,0}` by the summand in (16) costs at most `sup_n|z_{i,n}-z_i| sup_n||(v_{i,n}/L)_+||=o_P(1)` per row. Replacing `z_{i,n}^2` by `z_i^2` in (14)-(15) also costs `o_P(1)`. Hence every retained survivor contributes its `z_i^2(1-rho^2)` diagonal Volterra action, and every retained dead row contributes zero, uniformly up to the cone stop.

For omitted initially small endpoints, equation (12) of `MACRO_COMPACTNESS.md` gives on each finite-horizon energy localization

\[
 \sup_{t\le T}\|A_m^{\{|z_i|\le\epsilon\}}(t)\|
 \le K_T\left(\sum_{|z_i|\le\epsilon}z_i^2+o_P(1)\right). \tag{17}
\]

The same square mass bounds their contributions to `P_{1,m},P_{2,m}`. Its limiting small-`z` expectation is `O(epsilon^(2-alpha))`. For fixed `epsilon`, the probabilities of an atom beyond a large `|z|` cutoff or a large original-mark cutoff tend to zero. Remove cutoffs in this order. The exact output identity (11) of `MACRO_COMPACTNESS.md`, with its uniform cross-time Gram freeze, now yields uniformly up to `T wedge tau_m(delta)`

\[
 f_m(t)-f_m(0)
 =Q_m\int_0^t r_m(s)ds+o_P(1).                         \tag{18}
\]

Grid-to-polygon interpolation costs `O_P(h)` on the bootstrap localization. Since `r_m=y-f_m`, (18) proves (4). The finite-cutoff proof also establishes the claimed joint convergence of `P_{j,m}`: initial marked point-process convergence handles finitely many atoms because `v_{j,0}=0` has zero mark probability; (17) removes small atoms. Neither step needs a second moment of the full stable square mass.

The pre-step first-layer Gram of a certified row may keep switching between its two binary values. Equations (14)-(18) identify the *output action* along the selected residual, not a pointwise or `L^1` limit of the tangent Gram. The frozen chatter example in `../../20261023T232238Z/agents/e03_discrete.md` explicitly rules out that upgrade.

## Stopping comparison and scope

On `||Q_m||<=K`, Gronwall applied to (4) gives the stopped comparison to `exp(-Q_m t)R_m`. The matrices `Q_m` are tight by the joint initial limit. The function `g` in (1) is Lipschitz. If the comparison ODE has `min_{[0,T]}g>3delta` but the actual grid first reaches `g<=delta` by time `T`, their states at that first grid node are separated by at least a fixed multiple of `delta`, contradicting the stopped comparison. This proves (5). The use of **grid-node** stopping ensures every update counted before the stop has coefficients inside the cone, while the polygonal path remains uniformly close to its nodes. No continuity of the map from a path to its first hitting time is used.

The ratio cone need not be invariant for a general realized `Q`: for `p=-r_1,q=r_2`, at `p=rho*q` the derivative of `p-rho*q` under `r'=-Qr` is `q[rho(Q_22-Q_11)+(1-rho^2)Q_12]`, which can be negative. This is why the theorem stops at its ODE ratio-cone exit. It does not classify support changes at that exit, prove a global two-input path law, extend to deep networks or test inputs, or identify a kernel in `L^1`.
