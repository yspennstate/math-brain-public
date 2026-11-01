# A nonorthogonal finite-width ReLU flow can stop at an attracting boundary

**Scope.** This is a finite-width well-posedness obstruction and a local nonsmooth continuation calculation for the exact shallow two-input equations. It is not a nonorthogonal infinite-width limit, a statement about the probability of failure uniformly in width, or a resolution of T384. The prior orthonormal-input theorem explicitly imposed absorbing projected gates; that rule is not the Euclidean parameter gradient when the input Gram matrix is nonorthogonal.

## Proposition: an open, positive-probability set has no Carathéodory continuation

Fix any `0<alpha<2` and integer `m>=2`. Use the established scales

`a=m^(1/alpha)`, `L=(log m)^(1/alpha)`, `b=a L`, `beta=L/a>0`.

Take `d=2`, `x_1=(1,0)`, `x_2=(1/2,sqrt(3)/2)`, hence `G=[[1,rho],[rho,1]]` with `rho=1/2`, and fix labels `y=(-1,1)` for every `m`. Let `V_ij=U_i dot x_j`, `f_j=b^(-1) sum_i W_i (V_ij)_+`, and `r=y-f`. The pointwise ReLU convention is `D(v)=1{v>0}`, including `D(0)=0`. The projected classical equations are

`V_ij'=beta W_i sum_l G_jl r_l D(V_il)`,  `W_i'=beta sum_l r_l (V_il)_+`.       (1)

There is a nonempty open set `O_m` of initial parameter states with positive probability under independent standard symmetric `alpha`-stable original coordinates and output weights such that the unique smooth solution of (1) before its first hit reaches `V_11=0` in finite time, all other relevant gates remain strictly inside their sectors, and **no absolutely continuous Carathéodory solution of (1) extends beyond that hit**.

**Construction and exact evolution.** Require row 1 to have `W=W_1>0`, `q=V_11<0`, and `v=V_12>0`; require every other row to have `V_i1<0,V_i2<0` (their `W_i` are unrestricted). The latter rows are stationary and have zero output as long as the solution exists. While `q<0`, row 1 is active only on input 2, so

`r_1=-1`, `r_2=1-Wv/b`,

`W'=beta r_2 v`, `v'=beta W r_2`, `q'=rho beta W r_2=rho v'`.             (2)

Choose any `w_0,v_0>0` with `w_0 v_0<b`, and a small open rectangle `I_w x I_v` around `(w_0,v_0)` whose closure lies in `W>0,v>0,Wv<b`. The smooth *inactive-sector extension* of (2) exists globally. Indeed

`r_2'=-(beta/b)(W^2+v^2)r_2`,                                  (3)

so `r_2(t)>0`; `W,v` increase while `Wv<b`, which gives the upper bounds `W(t)<b/v(0)` and `v(t)<b/W(0)`. Thus `v(T)-v(0)>0` for every `T>0`. Fix, for instance, `T=1`. Continuous dependence and compactness of the rectangle's closure give

`kappa := inf_{(W(0),v(0)) in closure(I_w x I_v)} [v(T)-v(0)] >0`.

Choose `0<epsilon<rho kappa` and impose `q(0) in (-epsilon,0)`. Along the inactive-sector extension,

`q(t)=q(0)+rho [v(t)-v(0)]`,                                    (4)

which is strictly increasing, starts negative, and is positive by `T`. It therefore has a unique hit `tau in (0,T)`. Equations (2) are the actual smooth equations up to `tau`, so this is the actual first hit of row 1. At `tau`, `W>0`, `v>0`, and `0<r_2<1`; all other rows remain strictly inactive.

The stated inequalities, with `W(0) in I_w`, `v(0) in I_v`, `q(0) in (-epsilon,0)`, define `O_m`. The linear map `(U_i1,U_i2)->(V_i1,V_i2)` has determinant `sqrt(3)/2`, so `O_m` is a nonempty open subset of original parameter space. Each scalar symmetric `alpha`-stable has positive probability on every nonempty interval (equivalently, a full-support density); independence then gives `P(O_m)>0`. This is true for every fixed `m>=2`, with the same labels and Gram matrix. The present construction gives no width-uniform lower bound: requiring `m-1` fully inactive rows incurs a factor `P(V_1<0,V_2<0)^(m-1)`.

**Nonexistence after the hit.** At `q=0`, the convention `D(0)=0` assigns the left normal velocity

`F_0=F^- = beta W rho r_2>0`.                                  (5)

For `q>0` sufficiently close to the hit, `W,v,r_2` remain positive by continuity and

`r_1=-1-Wq/b`, `q'=F^+=beta W(r_1+rho r_2)<0`,                 (6)

because `rho=1/2` and `r_2<1` at the hit. For `q<0` nearby, `q'=F^->0`. Suppose an absolutely continuous full-state extension existed on `[tau,tau+delta]`. Shrink `delta` so these strict signs and the inactivity of the other rows persist. Almost everywhere, `q q'<=0`, including equality at `q=0`; therefore `(q^2)'=2q q'<=0` almost everywhere. Since `q(tau)^2=0`, necessarily `q=0` throughout this interval. But then `q'=0` almost everywhere, contradicting the pointwise right-hand side (5), which is strictly positive whenever `q=0` nearby. Thus no Carathéodory continuation exists. Assigning the right derivative `D(0)=1` instead also fails here, since it makes `F_0=F^+<0` while the two off-surface sides still point inward.

The argument is an actual coupled residual calculation, not a frozen-`r` cartoon: (3) proves that `r_2` evolves yet stays strictly positive through the hit. It also shows why a rule that permanently absorbs `q` at zero would be an additional constrained dynamics, not (1): the active second input keeps pushing `q` with normal speed `rho beta W r_2`.

## Filippov and Clarke continuation on the same event

The preceding failure concerns the **single-valued** field (1) with a pointwise derivative convention. Its Filippov regularization at `q=0`, away from all other gate boundaries, takes the convex hull of the two smooth limiting vectors. Equivalently, give gate 1 a fractional coefficient `theta in [0,1]` at the boundary. At `q=0`, where `r_1=-1` and `r_2=1-Wv/b`, the projected inclusion is

`q'=beta W(rho r_2+theta r_1)`,

`v'=beta W(r_2+rho theta r_1)`, `W'=beta r_2 v`.                (7)

The unique tangent coefficient is

`theta_*=-rho r_2/r_1=rho r_2 in (0,1)`.                      (8)

It gives the attracting sliding flow

`q=0`, `v'=beta W(1-rho^2)r_2`, `W'=beta r_2 v`,

`r_2'=-(beta/b)[v^2+(1-rho^2)W^2]r_2`.                       (9)

In the original hidden coordinates this is `U_1'=beta W r_2(x_2-rho x_1)`, tangent to `U_1 dot x_1=0`. The factor `1-rho^2` in (9) is the Schur complement of the active input Gram direction.

This solution remains on the boundary for every finite later time on the constructed event: `r_2` stays positive, `theta_*` remains interior, and `W,v` increase with `Wv<b`. Locally it is the unique absolutely continuous Filippov continuation. Any such solution starting at `q=0` obeys `q q'<=0` off the boundary, hence `q=0`; tangency then forces (8), after which the smooth two-dimensional ODE (9) is unique. The Filippov construction ignores the single-point choice `D(0)=0` and allows the state-dependent fractional value (8).

There is a matching Clarke interpretation for the *full Euclidean parameter loss* `ell=(1/2)||y-f||^2`. At this isolated boundary its joint Clarke subdifferential is precisely the convex hull of the two one-sided smooth gradients. With learning multiplier `eta=L^2` and `eta/b=beta`, the generalized-gradient inclusion `Theta' in -eta partial^C ell(Theta)` projects to (7). In fact (8) is also the **minimum-Euclidean-norm Clarke subgradient** selection: the `U_1` component to minimize is proportional to `theta r_1 x_1+r_2 x_2`, whose squared norm has derivative zero exactly at `theta=-rho r_2/r_1`; the `W_1` component is independent of `theta` at `q=0`. Thus the full Clarke inclusion and the Filippov inclusion agree locally here, and their viable continuation slides. A fixed choice `theta=0` or `theta=1` at zero does not produce a Carathéodory continuation; only the state-dependent tangent choice does.

## Boundaries of this result and routes ruled out

* `m=1` is unsuitable under these exact logarithmic scales because `L=(log 1)^(1/alpha)=0`; the construction starts at `m=2`.
* Freezing the residual misses the coupled evolution. Equations (2)–(3) pay for it and keep the attracting inequalities strict at the first hit.
* The open event proves positive probability for each fixed width. Its probability can shrink with `m`, so this note does **not** establish a macroscopic positive-probability failure event or the correct nonorthogonal stable endpoint law.
* Neither per-projection absorbing gates nor the orthonormal theorem's monotone alive-clock argument follows from Euclidean gradient flow for `rho!=0`. A nonorthogonal limit must first specify a well-posed nonsmooth selection, such as the Filippov/Clarke sliding flow, and then handle possible intersections of switching surfaces and singular endpoint initialization. No such limit is proved here.
