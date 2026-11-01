# T384: selected macroscopic dynamics in the negative-correlation mixed cone

**Status.** A conditional, fixed-`gamma`, two-input macroscopic theorem for actual simultaneous GD. It uses the joint initialization and finite-grid boundary theorem in `../../20261023T232238Z/BOUNDARY_GRID.md` and the finite-horizon bootstrap, exact output identity, and small-endpoint estimates in `../../20261023T232238Z/MACRO_COMPACTNESS.md`. It is not a general nonorthogonal or all-residual-cones theorem. The essential simplification is that there is no attracting sliding face while the residual has signs `(-,+)` and `rho<0`.

## Setting and exact frozen selector

Take `k=2`, unit inputs, and

\[
G=XX^{\mathsf T}=\begin{pmatrix}1&\rho\\\rho&1\end{pmatrix},
\qquad -1<\rho<0.
\]

All other initialization, normalization, and GD conventions are those of `BOUNDARY_GRID.md`: `a_m=m^{1/alpha}`, `L_m=(log m)^{1/alpha}`, physical step `h_m=gamma/L_m`, fixed `gamma>0`, `z_i=W_{i,0}/a_m`, and `v_{i,n}=XU_{i,n}`. Write `R=y-F` for the limiting initial residual and consider the event

\[
E=\{R_1<0<R_2\}.
\tag{1}
\]

For `r_1<0<r_2` and a marked endpoint `(z,u)`, let `v_0=Xu=(x_0,y_0)` and iterate the **frozen, discrete** map

\[
v_{n+1}=v_n+\gamma zG D(v_n)r,
\qquad D(v)=\operatorname{diag}(1_{v_1>0},1_{v_2>0}).
\tag{2}
\]

Its terminal selector `sigma_gamma(z,u;r)` is in `{0,1,2}`, where `0` means dead and `j` means permanently supported by input `j`. Except on coordinate-threshold null sets it has this explicit form:

* If `z>0`, every mark with `y_0>0` selects `2`, and every `--` mark selects `0`. For an initial `+-` mark set
  \[
  n_x=\left\lceil\frac{x_0}{\gamma z|r_1|}\right\rceil.
  \]
  It selects `2` exactly when
  \[
  y_0+\gamma |\rho|z|r_1|n_x>0;
  \tag{3}
  \]
  otherwise it selects `0`.
* If `z<0`, every mark with `x_0>0` selects `1`, and every `--` mark selects `0`. For an initial `-+` mark set
  \[
  n_y=\left\lceil\frac{y_0}{\gamma |z|r_2}\right\rceil.
  \]
  It selects `1` exactly when
  \[
  x_0+\gamma |\rho||z|r_2n_y>0;
  \tag{4}
  \]
  otherwise it selects `0`.

The strict inequalities encode Euler overshoot. For example, `rho=-1/2`, `z=1`, `r=(-1,1)`, `gamma=1`, and `v_0=(0.1,-0.1)` give `v_1=(-0.9,0.4)`, so the discrete selector is `2`. The corresponding continuous straight segment reaches `x=0` while `y=-0.05`; its Filippov flow would be dead. Thus a continuous-time entrance rule would give the wrong selected mass.

The deterministic selector was checked against literal frozen Euler iteration on 100,000 seeded random cases by `../code/f03_selector_check.py`; the captured result is `../outputs/f03_selector_check.txt`. This computational check is a reproducibility aid, not a substitute for the quadrant proof below.

To verify the rule, put `a=zr_1<0`, `b=zr_2>0` for `z>0`. The four quadrant velocities, divided by `gamma`, are

\[
--:(0,0),\quad +-:(a,\rho a),\quad -+:(\rho b,b),
\quad ++:(a+\rho b,\rho a+b).
\tag{5}
\]

In `-+` the first coordinate strictly decreases and the second strictly increases. In `++` the same is true, so after finitely many steps the orbit enters `-+`. In `+-`, while it remains there, `x` decreases and `y` increases. If `x` reaches the nonpositive side before `y` becomes positive, both gates are off and the orbit is dead. If `y` becomes positive first, including a simultaneous two-axis overshoot with positive terminal `y`, the orbit enters `++` or `-+` and ultimately selects `2`. Formula (3) tests the `y` value at the hypothetical first `x` crossing while the orbit remains in `+-`; it is equivalent to that race. For `z<0`, interchange the coordinates. In particular every frozen orbit terminates after a finite (mark-dependent) number of steps in `--`, `+-` for `z<0`, or `-+` for `z>0`, with strictly interior terminal coordinates almost surely. There is no positive-face sliding or recurrent gate switching in this sign cone.

## Selected theorem

Define the Poisson masses and selected matrix

\[
P_j=\int z^2 1\{\sigma_\gamma(z,u;R)=j\}\,N(dz,du),
\qquad Q=C+\operatorname{diag}(P_1,P_2).
\tag{6}
\]

Here `P_1` receives only `z<0` atoms and `P_2` only `z>0` atoms. Both are finite almost surely because `P_1+P_2<=int z^2 N(dz,du)<infinity` almost surely. Their dependence on `gamma` and on the **initial** residual `R` is essential.

For a finite-width comparison quantity, use the same formula on every initial row with `z_i=W_{i,0}/a_m`, `u_i=U_{i,0}`, and `r_{m,0}=y-f_{m,0}`; call the resulting masses `P_{j,m}` and put

\[
Q_m=C_{m,0}+\operatorname{diag}(P_{1,m},P_{2,m}).
\tag{7}
\]

Outside `E_m={r_{m,0,1}<0<r_{m,0,2}}`, define the selectors arbitrarily, since only the conditional assertion is made. Let `r_m(t)` be the polygonal residual interpolation and `H_m(t)` the held pre-step tangent Gram (equation (2) of `BOUNDARY_GRID.md`). For every fixed `T<infinity`, conditionally on `E_m`,

\[
\sup_{0\le t\le T}
\|r_m(t)-e^{-Q_mt}r_{m,0}\|\ \longrightarrow\ 0
\quad\text{in probability},
\tag{8}
\]

and, for every `0<delta<T`,

\[
\int_0^T\|H_m(t)-Q_m\|dt\longrightarrow0,
\qquad
\sup_{\delta\le t\le T}\|H_m(t)-Q_m\|\longrightarrow0
\quad\text{in probability}.
\tag{9}
\]

Also `(f_{m,0},C_{m,0},N_m,Q_m)` converges jointly, conditionally on `E_m`, to `(F,C,N,Q)` conditionally on `E`. In particular the conditional macroscopic residual law is the unique path

\[
r(t)=e^{-Qt}R,\qquad r'(t)=-Qr(t),\qquad t\ge0.
\tag{10}
\]

The conditional statement is meaningful because the full-rank initialization gives `R` a density with full support, so `P(E)>0`, and its two coordinate-boundary events have probability zero. Equations (8)--(9) concern actual simultaneous GD at fixed `gamma`; (9) is stronger than what is available in the sliding cones treated in `e03_discrete.md`. It holds here because every selected endpoint has an eventually fixed binary gate.

## Proof

**1. Generic finite-grid entrance.** Conditional on `R` and `z`, every coordinate of a frozen `v_n` under a fixed finite gate history is an affine function of `Xu`. Since `U` has a density and `X` has row rank two, no Poisson atom hits a coordinate axis at any integer step, almost surely. The countable union over atoms and steps remains null. The quadrant argument above gives each atom a finite terminal step `N(z,u;R)`. On a finite cutoff set `epsilon<|z|<M`, `||u||<B`, the atoms are finite; their maximum terminal step `N_*` is finite and every terminal coordinate has a strict sign margin. The fixed-grid theorem gives joint convergence of these finitely many actual endpoint orbits through `N_*` to their frozen orbits, because `r_{m,n}-r_{m,0}=O_P(N_*/L_m)` and `W_{i,n}/a_m-z_i=o_P(1)` for each fixed `N_*`. Consequently their actual gates agree with their frozen terminal gates at step `N_*`, with probability tending to one. Random `N_*` causes no interchange problem: on a joint subsequence coupling, convergence holds simultaneously at each deterministic integer step, after which one uses the realized finite `N_*`.

**2. Persistence while the residual is mixed.** The growing-step bootstrap in `MACRO_COMPACTNESS.md` gives, on each finite physical horizon, `sup_{i,n}|W_{i,n}/a_m-z_i|=O_P(L_m/a_m)` after the stated energy localization. Hence each retained atom keeps the sign of `z_i`. If `z_i>0` and it entered `-+`, every later update with `r_{m,1}<0<r_{m,2}` moves its first projection down and its second up. If `z_i<0` and it entered `+-`, every later update moves its first projection up and its second down. A `--` row does not move. Thus none of these rows can reactivate or change terminal sector while the residual remains in the mixed cone. This argument uses actual simultaneous updates and needs no frozen-residual assumption after entrance.

**3. Output and small endpoints.** At grid nodes, let

\[
A_m(nh_m)=L_m^{-1}\sum_i z_i\big[(v_{i,n})_+-(v_{i,0})_+\big],
\]

and interpolate `A_m` polygonally. The exact identity and cross-time Gram estimate from `MACRO_COMPACTNESS.md` give, uniformly through `T`,

\[
f_m(t)-f_{m,0}
=C_{m,0}\int_0^t r_m(s)ds
+A_m(t)
+o_P(1),
\tag{11}
\]

The integral interpolation differs from its grid sum by `O_P(h_m)` under the same horizon bootstrap. Stop at the first time the finite-width residual leaves the mixed cone. Its initial strict margin and the fixed-grid estimate ensure that the first `N_*` steps lie before this exit with probability tending to one. For each retained terminal atom, those steps occupy physical time `N_*gamma/L_m=o(1)` and contribute `o_P(1)` uniformly to `A_m`. Thereafter a `z>0`, selector-`2` atom changes only its positive second projection, by `gamma(W_{i,n}/a_m)r_{m,n,2}` per step. Multiplication by `z_i/L_m` gives `z_i^2 int_0^t r_{m,2}(s)ds+o_P(1)` uniformly up to the stopping time. A selector-`1` atom analogously contributes `z_i^2 int_0^t r_{m,1}(s)ds` in coordinate one; a dead atom contributes `o_P(1)`. A killed row can lose a positive **initial** projection during its first `N_*` steps, but on the finite cutoff that loss is only `O_P(1/L_m)` in `A_m`; it contributes no persistent macroscopic coefficient. The replacement of current `W_{i,n}/a_m` by `z_i` is uniform for finitely many retained atoms.

The omitted initially small endpoints satisfy, uniformly through `T`, the square-mass bound (12) of `MACRO_COMPACTNESS.md`:

\[
\sup_t\|A_m^{\{|z_i|\le\epsilon\}}(t)\|
\le K_T\left(\sum_{|z_i|\le\epsilon}z_i^2+o_P(1)\right).
\tag{12}
\]

Here `K_T` is deterministic on each bootstrap localization. The same square mass bounds their contribution to `P_{j,m}` and, with the uniform `o_P(1)` weight-square freeze error, to the pre-step Gram; its expected limit superior is `O(epsilon^{2-alpha})`. At fixed `epsilon`, large `|z|` and large `||u||` have vanishing occurrence probability as their cutoffs grow. Cutoff removal in (11) therefore gives, uniformly up to cone exit,

\[
\sup_t\left\|r_m(t)-r_{m,0}
+Q_m\int_0^t r_m(s)ds\right\|\longrightarrow0
\quad\text{in probability}.
\tag{13}
\]

The same finite-cutoff argument applied to `H_m` proves (9) up to cone exit. On retained atoms, the pre-step gate is constant after `N_*`, and `DGD` is exactly `e_je_j^{\mathsf T}` for its single active input because `G_{jj}=1`. The first `N_*` steps have vanishing physical duration, explaining the `L^1` assertion; for `t>=delta` they are eventually over, explaining uniform convergence there. The second-layer Gram freezes uniformly to `C_{m,0}` by the bootstrap. Small endpoints are bounded uniformly by their initial square mass plus `o_P(1)`.

**4. No finite cone exit.** Every entry of `C_{m,0}` is nonnegative because it is a sum of outer products of nonnegative ReLU vectors. Likewise each ray `q_ell^+` and `q_ell^-` defining `C` is nonnegative, so `C_{12}>=0`. In particular `Q_m` and `Q` have nonnegative off-diagonal entries. For either matrix, set `s=(-r_1,r_2)`. Its selected linear ODE is

\[
s'=\begin{pmatrix}-Q_{11}&Q_{12}\\Q_{12}&-Q_{22}\end{pmatrix}s.
\tag{14}
\]

This is a Metzler system. If `s(0)>0`, then `s_j(t)>=s_j(0)e^{-Q_{jj}t}>0` for every finite `t`. On localized events with `s_{m,j}(0)>=eta>0` and `||Q_m||<=K`, the comparison path `e^{-Q_mt}r_{m,0}` has a deterministic positive cone margin on `[0,T]`. Equation (13) and Gronwall make the actual residual uniformly close to that path until its first cone exit; the margin then rules out an exit by continuity of polygonal interpolation (and the held residual differs by `O_P(h_m)`). Remove the localization using tightness of `Q_m`, convergence of the initial residual, and `P(E\setminus\{s_j(0)>=eta\})->0` as `eta↓0`. This proves (8), removes the stopping from (9), and gives the global fixed-`T` selected law (10).

Finally, the finite-cutoff selector is locally constant at every generic marked orbit, so marked PPP convergence and the same square-mass cutoff prove joint convergence of `P_{j,m}` to `P_j`. A diagonal argument over cutoffs yields joint convergence with `(f_{m,0},C_{m,0},N_m)`. Conditioning on `E_m` is legitimate because its limiting boundary has zero probability. This completes the theorem.

## Boundaries of the claim

The theorem selects an output law and a strong positive-time tangent Gram limit only on the `R_1<0<R_2`, `rho<0` event. It does not identify the dynamics in other residual cones, where attracting faces and persistent chatter can arise. Nor does the selected matrix describe a residual-independent derivative of the entrance map: its atoms are classified using the particular initial residual and fixed `gamma`. The overshoot in (3)--(4) is precisely why that dependence cannot be discarded.
