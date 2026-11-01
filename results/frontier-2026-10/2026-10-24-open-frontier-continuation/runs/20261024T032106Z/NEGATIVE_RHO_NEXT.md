# Negative correlation, same-sign residuals: frozen entrance and the positive-time corner

**Status:** the finite frozen strict-gate classifier below is proved. The positive-time corner matching and any residual-coupled network law in this sector remain **OPEN**. This note extends the direction in `../../20261024T002440Z/DIRECTIONS.md`; it does not redo that run's proved opposite-sign negative-correlation theorem. The joint initialization, actual grid and truncation machinery are in `../../20261023T232238Z/{BOUNDARY_GRID,MACRO_COMPACTNESS}.md`.

## Finite frozen classifier

Let `rho=-a` with `0<a<1`, `R=(p,q)` with `p,q>0`, `gamma>0`, and `z!=0`. Write `v_n=(x_n,y_n)` and use the **strict pre-step gates**

\[
v_{n+1}=v_n+\gamma z
\begin{pmatrix}1&-a\\-a&1\end{pmatrix}
\operatorname{diag}(1_{x_n>0},1_{y_n>0})R. \tag{1}
\]

For `z>0`, the four sectors have increments

| Pre-step sector | Increment divided by `gamma*z` |
|---|---|
| `--` | `(0,0)` |
| `+-` | `(p,-ap)` |
| `-+` | `(-aq,q)` |
| `++` | `(p-aq,q-ap)` |

Consequently, `--` is dead immediately. An initially single-1 row (`x_0>0,y_0<=0`) stays single-1 forever under the frozen `R`, with `x` strictly increasing and `y` nonincreasing; single-2 is the mirror. An initially `++` row has three exhaustive possibilities:

* If `aq<=p<=q/a`, both increments are nonnegative, so it stays `++` forever, including the boundary cases with one zero drift.
* If `p<aq`, its first coordinate decreases at fixed rate `gamma*z*(aq-p)>0`, while its second increases. It reaches `x<=0` after exactly `ceil(x_0/[gamma*z*(aq-p)])` steps, then stays single-2 forever.
* If `q<ap` (equivalently `p>q/a`), the symmetric argument gives finite exit to permanent single-1.

The two exit cases cannot coincide: `p<aq` and `q<ap` would imply `p<a^2p`. At an exact hit of zero, that gate is off at the next pre-step, as (1) requires. This classifier is valid for every mark, including axes, and every fixed `gamma`; a generic mark makes its finite terminal sector strict.

For `z<0`, **every** orbit reaches `x<=0,y<=0` after finitely many steps, even though either coordinate may increase and an inactive gate may reactivate. Put `w=|z|`. Equation (1) becomes

\[
\Delta x=\gamma w(aq\,1_{y>0}-p\,1_{x>0}),\qquad
\Delta y=\gamma w(ap\,1_{x>0}-q\,1_{y>0}). \tag{2}
\]

Each coordinate has a global lower barrier

\[
x_n\ge L_1:=\min(x_0,-\gamma wp),\qquad
y_n\ge L_2:=\min(y_0,-\gamma wq). \tag{3}
\]

Indeed, an inactive coordinate receives a nonnegative cross increment; an active coordinate can fall by at most its own `gamma*w*R_j` in one step. Yet on every nondead step the sum decreases by at least a fixed amount:

\[
(x_{n+1}+y_{n+1})-(x_n+y_n)
=-\gamma w(1-a)(p\,1_{x_n>0}+q\,1_{y_n>0})
\le-\delta,
\quad \delta:=\gamma w(1-a)\min(p,q)>0. \tag{4}
\]

If the orbit stayed active for `N` steps, (3)–(4) would give `L_1+L_2<=x_0+y_0-N*delta`. Hence it must be dead by step

\[
N_* = \left\lfloor\frac{x_0+y_0-L_1-L_2}{\delta}\right\rfloor+1. \tag{5}
\]

This bound is deliberately coarse but finite. It handles gate reactivation and exact axis hits without a monotonicity claim for either coordinate. For example, with `a=1/2`, `p=q=gamma=w=1` and `v_0=(9/10,-1/10)`, the negative-`z` path is

\[
(9/10,-1/10)\longrightarrow(-1/10,2/5)
\longrightarrow(2/5,-3/5)
\longrightarrow(-3/5,-1/10), \tag{6}
\]

so the active gate changes `1 -> 2 -> 1 -> dead` before the finite death. A claim that both projections decrease would be false.

For fixed `(a,p,q,z,gamma)` each finite coordinate test is an initial projected mark plus a gate-word-dependent constant. The full-rank stable projection has a density; countably many finite gate-word axis hyperplanes have zero mark probability. Thus almost every Poisson atom obtains a strict finite sector history or strict dead pair, locally stable over that finite history under small parameter perturbations. Robustness of the permanent ++ classification additionally requires a strict ratio margin aq<p<q/a; at a ratio equality, a small residual perturbation can change the eventual sector even though every state in a fixed finite history stays strict. This finite certificate is a boundary-grid ingredient, not an interchange of a growing number of boundary steps with the width limit. The negative initial residual quadrant is the exact sign mirror: replacing `(R,z)` by `(-R,-z)` leaves (1) unchanged.

## Why a later corner cannot be restarted from zero

Consider one positive-`z` row that starts single-1. While both residual components stay positive it remains single-1. If the limiting residual later has `r_1<0<r_2`, its *candidate* normalized single-1 path from the macroscopic origin is

\[
q(t)=z\big(I_1(t),-aI_1(t)\big),\qquad
I_j(t)=\int_0^t r_j(s)\,ds, \tag{7}
\]

for as long as the first gate is active and the second is off. A return of `I_1` to zero after it was positive makes this path hit the collapsed corner `q=(0,0)` at a strictly positive physical time. Such a return is compatible with a positive off-diagonal in the candidate initial residual action. For instance, the positive definite matrices `C=[[2,1],[1,3]]` and `Q=C+diag(1,1)=[[3,1],[1,4]]`, with `R=(1,10)`, give `(Q^{-1}R)_1=-6/11<0`; `I_1` starts by increasing, so the constant-`Q` candidate has a finite return. Here `p<aq`, so frozen positive-`z` `++` rows exit to single-2 and a diagonal endpoint action is consistent with the classifier. At its return `r_1<0<r_2`, because the first residual-axis crossing is transversal and the mixed signs persist under this positive-off-diagonal `Q`. These matrices are algebraically compatible with `rho=-1/2`: take input rows `(1/2,-sqrt(3)/2)` and `(1/2,sqrt(3)/2)`; positive ray masses `4`, `4/3`, `8/3` on the common, first-only and second-only rays produce the displayed `C`. The exact parameter point is only an illustrative candidate, not a probability or actual-network path claim.

Crucially, the **unscaled** row retains a mark-dependent invariant during every single-1 step. In the *actual* simultaneous-GD recursion, let `z_{i,n}=W_{i,n}/m^{1/alpha}`, allowing it to change at each step. Whenever row `i` has gate 1 on and gate 2 off,

\[
\Delta v_{i,1}=\gamma z_{i,n}r_{m,n,1},\qquad
\Delta v_{i,2}=-a\gamma z_{i,n}r_{m,n,1},\qquad
\boxed{\Delta(v_{i,2}+a v_{i,1})=0.} \tag{8}
\]

The cancellation is exact despite changing `W_i` and the coupled, changing residual. When every pre-step since initialization has been single-1, its constant is the **original** mark `H_i=(Xu_i)_2+a(Xu_i)_1`; on any later consecutive single-1 interval, the constant is the value of `v_2+a v_1` at that interval's start. In particular the one-gate states lie on `v_2=H_i-a v_1` for the originally single-1 row. As `v_1` descends toward zero, `H_i>0` allows gate 2 to turn on before a continuous corner arrival, while `H_i<0` places the continuous intersection at a dead point. The discrete last step can overshoot the axis and alter this simple sign prediction: for `a=1/2`, `gamma*z*r_1=-1`, `v=(9/10,-49/100)` has `H=-4/100<0`, but one single-1 step lands at `(-1/10,1/100)`, activating gate 2. Thus neither the scaled state `q=0` nor the sign of `H_i` alone is a complete critical-grid restart rule. The single-2 mirror invariant is `v_{i,1}+a v_{i,2}`.

**Exact last-step overshoot lemma.** The obstruction can be stated without any limiting approximation. On an actual single-1 pre-step in a local mixed residual interval, assume `z_{i,n}>0`, `r_{m,n,1}=-p_n<0`, and `r_{m,n,2}>0`. Let `eta=v_{i,2,n}+a v_{i,1,n}<0`, `x=v_{i,1,n}>0`, and `delta=gamma*z_{i,n}*p_n>0`. Then `v_{i,2,n}=eta-a*x<0`. Suppose this step crosses to `x'=x-delta<=0`. The exact update and invariant give

\[
x'=x-\delta,\qquad
y'=\eta+a(\delta-x),\qquad
\theta:=x/\delta\in(0,1]. \tag{9}
\]

With the strict gate convention, the row lands in single-2 exactly when `y'>0`, and lands dead when `y'<=0`. Away from equality, the survival criterion is equivalently

\[
\theta<1+\frac{\eta}{a\delta}. \tag{10}
\]

The open window `-a*delta<eta<0` makes this a nontrivial threshold in `theta∈(0,1)`: two incoming unscaled rows with the same negative invariant and the same local drift can take different terminal sectors solely because their fractional last-step overshoots differ. For example, `a=1/2`, `delta=1`, `eta=-1/10` give threshold `theta<4/5`; incoming `x=7/10,y=-9/20` lands at `(-3/10,1/20)` (single-2), while `x=9/10,y=-11/20` lands at `(-1/10,-1/20)` (dead). If `eta<=-a*delta`, death is certain at this step. Once a row lands strict single-2, every subsequent step with `z_{i,k}>0` and `r_{m,k,2}>0` changes its coordinates by `gamma*z_{i,k}*(-a*r_{m,k,2},r_{m,k,2})`; its first coordinate decreases and second increases, so single-2 persists over that local mixed interval. Equality in (10) means `y'=0` and thus death under strict gates. The fixed finite frozen-grid hyperplane argument makes equality null there, but it does **not** establish a null threshold at a width-dependent positive-time return; a moving-time matching proof must handle that separately.

Equation (7) has lost `H_i` because it divides `v` by `L=(log m)^{1/alpha}`. At a positive-time return, the `O(1)` original-mark offset and the pre-step overshoot phase `theta_m` in (9) again decide which gate fires. A proof through this corner must match the incoming unscaled row, its exact invariant and grid phase to a new *moving-time* microscopic entrance, with residual coefficients frozen or controlled at the return and then with finite-cutoff/random-index localization before restoring the infinitely many atoms. Reusing the time-zero selector at the collapsed scaled origin would erase the original mark and can give the wrong sector. In particular, a conditional-uniform or otherwise universal limiting law for `theta_m` is **OPEN**; it would require a joint high-frequency density/rate argument and cannot be inferred from the macroscopic convergence in (7). The previous opposite-sign negative-correlation corner race is relevant machinery, but its time-zero incoming state is not automatically the state here.

## Next proof obligations

1. Establish the residual/endpoint candidate through any initial positive-residual interval for each strict ratio regime, accounting for `++` rows that remain double-active versus those that exit to a single gate. Do not infer it solely from the frozen classifier.
2. At each possible residual-axis and cumulative-return time, transfer the incoming **unscaled** finite-row state and invariant through a localized boundary grid. Determine the limiting joint law, if any, of the original mark, local drift and fractional overshoot `theta_m`; do not assume a uniform phase. Prove the corresponding robust terminal certificates and threshold-null statement before passing from finite rows to a Poisson-selected mass.
3. Only after that, identify the selected Poisson masses and a residual-coupled path law on fixed physical horizons. Check possible repeated regime changes and small-atom removal independently. No full negative-`rho` same-sign theorem or pre-step kernel limit is asserted here.

The exact-Fraction script `code/negative_rho_entrance_check.py` and its executed output `outputs/negative_rho_entrance_check.txt` check 2,700 rational parameter/mark cases against the frozen sector classifier and finite death bound, plus the exact changing-coefficient invariant, gate reactivation, and both sides of the overshoot threshold. These computations support the finite identities above; they do not supply the missing moving-time phase law.
