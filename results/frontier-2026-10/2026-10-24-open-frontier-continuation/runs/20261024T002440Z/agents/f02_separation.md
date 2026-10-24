# Positive-probability macroscopic separation of two critical Euler grids

**Status: proved, conditional only on the joint stable initialization and finite-horizon bootstrap in the preceding run.** This is a *same-initialization* statement for actual simultaneous finite-width GD. It does not identify either marginal macroscopic law or assert that the two marginal laws differ.

## Statement

Fix `0<alpha<2`, any deterministic labels `y in R^2`, and `d=k=2` with unit inputs whose Gram matrix is

\[
G=XX^T=\begin{pmatrix}1&-1/2\\-1/2&1\end{pmatrix}.
\]

Use the iid original-coordinate symmetric `alpha`-stable initialization, normalization `a=m^(1/alpha)`, `L=(log m)^(1/alpha)`, output `f=b^(-1)sum W_i(XU_i)_+`, `b=aL`, and actual simultaneous GD equations (1) of [BOUNDARY_GRID.md](../../20261023T232238Z/BOUNDARY_GRID.md). On the **same** initialized network, run two separate GD trajectories from time zero, one with physical step `h_c=1/L` (`gamma_c=1`) and one with `h_f=1/(10L)` (`gamma_f=1/10`). Use the held output at physical time `t` (polygonal interpolation gives the same conclusion). There are deterministic `T,c,p>0`, depending on `alpha,X,y` but not `m`, for which

\[
\liminf_{m\to\infty}
\mathbb P\{f^{c}_{m,2}(T)-f^{f}_{m,2}(T)\ge cT\}\ge p>0. \tag{S}
\]

The proof gives any sufficiently small fixed `T`, with a correspondingly small `c` (for example `c=1/4` after the constants are chosen). The same-initialization qualifier matters: (S) is a nonvanishing distance in this natural coupling, not by itself a proof that the two one-time marginal distributions differ.

## Robust finite-step mask contrast

Let `r_* = (-1,1)` and `v_*=(0.14,-0.12)`. For the frozen endpoint equation `v_{n+1}=v_n+gamma z G D(v_n)r`, at `z=1,r=r_*,v_0=v_*`, the coarse first step is

\[
v^c_1=(-0.86,0.38),
\]

and the fine first and second steps are

\[
v^f_1=(0.04,-0.07),\qquad v^f_2=(-0.06,-0.02).
\]

Fix the open boxes `z in (0.99,1.01)`, `||v_0-v_*||_infty<0.005`, and `||r_0-r_*||_infty<0.01`. Direct interval arithmetic gives strict margins for all displayed signs: the coarse first step is in `-+`; the fine first is in `+-` and the fine second is in `--`. For example, the fine second coordinate lies between `-0.027` and `-0.013` when its second-step residual and weight are frozen within the same displayed boxes. In the actual network, the second-step residual differs from `r_0` by `O(1/L)` and its weight ratio differs from `z` by `O(1/a)` on a bounded-energy event, so these signs persist for all sufficiently large `m`.

Once the fine row enters `--`, its hidden and output weights never move again: its ReLU vector and both gradients are exactly zero. After the coarse row enters `-+`, while `z_{i,n}=W_{i,n}/a>0` and `r_{n,2}>0`, its projected increments are

\[
v_{i,n+1,1}-v_{i,n,1}=-\tfrac12 z_{i,n}r_{n,2}<0,
\qquad
v_{i,n+1,2}-v_{i,n,2}=z_{i,n}r_{n,2}>0. \tag{1}
\]

Thus its `-+` mask persists on the short physical horizon constructed below. The frozen Filippov path from `v_*` also reaches a negative half-axis and stops; the coarse discrete path jumps across into `-+`. The Filippov observation is contextual and is not used to infer finite-width behavior.

## A positive-probability isolation event

Write `z_i=W_{i,0}/a`, `v_i=XU_{i,0}`, and `V_{U,m}=a^(-2)sum_i ||U_{i,0}||^2`. Let `A={u:||Xu-v_*||_infty<0.005}`, a bounded open set of positive stable-mark probability because `X` is invertible. Let `B=(0.99,1.01) x A` in marked `(z,u)` space. Choose a deterministic `K_U<infinity` such that

\[
\mathbb P\{\|y-F-r_*\|_\infty<0.01,\ V_U<K_U\}>0, \tag{2}
\]

where `V_U=\sum_{\ell=1}^2(S_\ell^++S_\ell^-)` is the original-coordinate hidden square-mass limit. Such `K_U` exists since `V_U<infinity` almost surely and `F` has a nondegenerate, everywhere positive stable density.

Here is the needed augmentation of the preceding run's signed-ray initialization proof. Set `H_{ell,s,m}=a^{-2}sum_i ((s U_{i,ell})_+)^2` for `ell=1,2` and `s in {+,-}`. Its four coordinates are exactly the signed-coordinate-square categories used to derive that run's `S_ell^s` variables; moreover `V_{U,m}=sum_{ell,s}H_{ell,s,m}` exactly. At fixed positive jump cutoffs, append these four square categories to the one-row Fourier/Laplace functional for the signed-ray product terms and marked `W` endpoints. A `W` endpoint `|W|>epsilon a` and a square endpoint `|U_ell|>sqrt(eta)a` overlap with probability `O(m^{-2})` by independence. For a product jump `|WU_ell|>tau aL` and a square endpoint in the same `U_ell` coordinate, split at `|U_ell|=H a`. The portion above has `limsup_m mP(|U_ell|>Ha)=O(H^{-alpha})`; on the portion below, the product jump requires `|W|>tau L/H`, so independence makes its probability, after multiplication by `m`, tend to zero. Send `H` to infinity. Different-coordinate product/square overlaps are independent, and distinct square categories are independent or disjoint. The product/marked-endpoint overlaps are already bounded in that proof. Thus the truncated transform factors.

The small square jumps have uniformly vanishing first moment `O(eta^{1-alpha/2})` as their square cutoff `eta` decreases; the existing centered product small-jump estimate removes the other cutoff. Consequently the **joint** limit is `(f_{m,0},(H_{ell,s,m})_{ell,s},N_m) => (F,(S_ell^s)_{ell,s},N)`, with `N` independent of `(F,(S_ell^s)_{ell,s})`. Summing the four square coordinates proves `(f_{m,0},V_{U,m},N_m)=>(F,V_U,N)` and the independence needed in (2). No independence between `F` and `V_U` is needed for (2).

For parameters `delta>0` and `0<epsilon<0.99`, let

\[
Q_m(\epsilon)=\sum_{|z_i|\le\epsilon}z_i^2,
\qquad Q(\epsilon)=\int_{|z|\le\epsilon}z^2N(dz,du).
\]

Augmenting the same joint convergence by `Q_m(epsilon)=>Q(epsilon)` is routine but worth recording: restrict first to `kappa<|z|<=epsilon` and bounded marks, apply marked-point-process convergence, then remove `kappa` by the finite-width and Poisson estimates `E sum_{|z_i|<=kappa} z_i^2=O(kappa^(2-alpha))` and `E int_{|z|<=kappa}z^2N=2alpha c_alpha kappa^(2-alpha)/(2-alpha)`, where `c_alpha=Gamma(alpha)sin(pi alpha/2)/pi`. Large marks at fixed `kappa` have vanishing occurrence probability. Hence this augmentation is joint with `f_{m,0},V_{U,m},N_m`. Also `Q(epsilon)` is independent of the restriction of `N` to `|z|>epsilon`.

For any `delta>0`, take `epsilon` small enough that `P(Q(epsilon)<delta)>0` (Markov's inequality even gives at least `1/2` if its mean is below `delta/2`). Consider the event

\[
\begin{split}
E_m=\{&\|r_{m,0}-r_*\|_\infty<0.01,\quad V_{U,m}<K_U,\\
&\text{exactly one }(z_i,U_{i,0})\in B,\quad
\text{no other }|z_i|>\epsilon,\quad Q_m(\epsilon)<\delta\}.
\end{split} \tag{3}
\]

The limiting event has positive probability. Indeed, its marked-Poisson part has probability

\[
\mu(B)e^{-\Lambda_\epsilon}\,P\{Q(\epsilon)<\delta\}>0,
\quad \Lambda_\epsilon=\mu\{|z|>\epsilon\}=2c_\alpha\epsilon^{-\alpha},
\]

and it is independent of the positive-probability event (2). Boundary-null truncation, or a slightly smaller open box, yields `liminf_m P(E_m)>0`. Denote a positive lower bound by `p_0`. On `E_m`, the designated row has bounded original mark, and the initial total row energy obeys

\[
S_{m,0}=a^{-2}\sum_i(W_{i,0}^2+\|U_{i,0}\|^2)
<K_U+1.01^2+\delta\le K:=K_U+3 \tag{4}
\]

for `delta<=1`. This choice of `K` precedes the choice of `delta`, avoiding a circular small-mass/energy localization.

## Short-time deterministic comparison on `E_m`

Apply the finite-horizon bootstrap of [MACRO_COMPACTNESS.md](../../20261023T232238Z/MACRO_COMPACTNESS.md), equations (6)--(12), to the finite pair `gamma in {1,1/10}` with the common initial bounds (4) and `||r_0||<=2`. Use its constants for the horizon `T<=1`. For all sufficiently large `m` there are deterministic `M,R_*<infinity`, depending only on `K,X` and the two gammas, such that for both schemes, up to physical time `T`,

\[
S_n\le 2K,\quad \|r_{n+1}-r_n\|\le M h_\gamma,
\quad \|r_n-r_0\|\le M(T+h_\gamma),
\quad \sup_{i,n}|W_{i,n}/a-z_i|=O_K(L/a). \tag{5}
\]

All estimates in (5) can be taken deterministic on `E_m`; the `O_K` constant is uniform in `m`. Choose `T>0` so small that `MT<0.05`, and then take `m` large enough that `Mh_c<0.01` and the weight error is below `0.01`. The coarse designated row satisfies `z_{i,n}>0.98`, `r^c_{n,2}>0.9`; hence (1) preserves its mask through `T`. The fine row is exactly dead from step 2 onward.

Let `n_c=floor(TL)` and `n_f=floor(10TL)` and compare the two held outputs at time `T`. The integration-by-parts identity (11) of `MACRO_COMPACTNESS.md` gives, in either scheme,

\[
f^\gamma_{n_\gamma}-f_0
= C_{m,0}J_\gamma+E^\gamma_{*,m}+E^\gamma_{\rm small,m}+e^\gamma_m,
\quad J_\gamma=h_\gamma\sum_{j<n_\gamma}r^\gamma_j, \tag{6}
\]

where `E_*` is the single designated row's `L^{-1}z_i[(v_{i,n})_+-(v_{i,0})_+]`, the small term is the same sum over all other rows, and `sup ||e_m^gamma||=O_K(L/a)`. This error is the cross-time hidden Gram replacement error, not an Euler tangent-kernel approximation. The initial second-layer matrix obeys `||C_{m,0}||<=||X||^2 K_U` on `E_m`.

Because the fine designated row has second projected coordinate negative initially and forever, `(E^f_{*,m})_2=0`. For the coarse row, its initial second coordinate is negative and its coordinates after the first step lie in `-+`. Thus, from (1),

\[
(E^c_{*,m})_2=\frac{z_i}{L}
\left(v^c_{i,1,2}+\sum_{j=1}^{n_c-1}z^c_{i,j}r^c_{j,2}\right).
\]

Using `z_i>0.99`, `z^c_{i,j}>0.98`, `r^c_{j,2}>0.9`, and `n_c/L->T`, this is at least `0.7T` for all sufficiently large `m` (at fixed positive `T`). The residual Lipschitz bound in (5), summed in time, gives

\[
\|J_c-J_f\|\le M T^2+O_{K,T}(1/L), \tag{7}
\]

since both Riemann sums have the same leading term `Tr_0`. Finally, square-mass bound (12) of `MACRO_COMPACTNESS.md` applied separately to the two schemes yields

\[
\|E^c_{\rm small,m}\|+\|E^f_{\rm small,m}\|
\le 2(T+h_c)\|G\|R_*[Q_m(\epsilon)+O_K(L/a)]
\le 2(T+h_c)\|G\|R_*[\delta+O_K(L/a)]. \tag{8}
\]

First choose `delta<=1` small enough that `4||G||R_*delta<0.1`, and then choose `epsilon` as above. Shrink `T` further, if necessary, so that `||X||^2 K_U M T<0.1`; all earlier bounds still hold. At this fixed `T`, the `1/L` and `L/a` terms in (6)--(8) are below `0.1T` for sufficiently large `m`. Taking the second component of the difference in (6) now gives

\[
f^c_{m,2}(T)-f^f_{m,2}(T)
\ge 0.7T-0.1T-0.1T-0.1T>\tfrac14T
\quad\text{on }E_m. \tag{9}
\]

Together with `liminf P(E_m)>=p_0>0`, this proves (S). The held/polygonal discrepancy is `O_K(1/L)` on this event, so the same claim applies to polygonal output interpolation.

## Scope

The event may be extremely rare because it forbids all other `|z|>epsilon` atoms; only strict positive probability is claimed. The result avoids selecting the full nonorthogonal macroscopic differential inclusion: a single robustly retained endpoint creates the order-`T` signal, while every other endpoint is controlled in total by its square mass. It also does not prove a separation of marginal output laws. A claim of marginal step-size dependence needs a separate observable or law comparison; a positive-probability difference under this coupling alone does not supply one.
