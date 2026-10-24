# All mixed-sign residuals at positive correlation: finite dead-or-support entrance

**Status: deterministic theorem for a frozen endpoint, with a robust certificate for later varying coefficients.** This extends `agents/h01_entrance.md` beyond the initial double-sliding ratio cone. The terminal survivor selector is then generally mark- and critical-step-dependent. A certificate here means permanent **positive support while the coefficients stay mixed and bounded**; the normal coordinate may be released from zero, so it is not always a sliding certificate.

Fix `0<rho<1`, `gamma>0`, `z>0`, and any frozen mixed residual `r_1<0<r_2`. Set

\[
a=-zr_1>0,\quad b=zr_2>0,\quad c=\rho b>0,\quad d=a-c\in\mathbb R,
\quad\kappa=(1-\rho^2)b>0.
\tag{1}
\]

The exact frozen strict-gate update has velocities, before multiplying by `gamma`,

| Gate sector | `--` | `+-` | `-+` | `++` |
|---|---|---|---|---|
| `(x,y)` velocity | `(0,0)` | `(-a,-rho*a)` | `(c,b)` | `(-d,b-rho*a)` |

The `++` support drift may now be negative. Nevertheless **support loss is irreversible**: if `y_n<=0,x_n<=0`, the row is dead; if `y_n<=0,x_n>0`, subsequent `+-` steps decrease both coordinates until `x<=0`, after exactly `ceil(x_n/(gamma*a))` steps, and then the row is dead. No frozen orbit with `y<=0` can regain support 2.

While `y_n>0`, with `s_n=1_{x_n>0}` and `eta_n=y_n-rho*x_n`, the two exact identities remain

\[
x_{n+1}=x_n+\gamma(c-a s_n)
=\begin{cases}x_n+\gamma c,&x_n\le0,\\x_n-\gamma d,&x_n>0,\end{cases}
\qquad
\eta_{n+1}=\eta_n+\gamma\kappa.
\tag{2}
\]

Choose any `D>max(d,0)`. The open half-strip `x> -gamma*D` is forward invariant **as long as support remains positive**. From a nonpositive `x`, the next increment is `gamma*c>0`; from a positive `x`, the next value is `x-gamma*d> -gamma*D`. If initially `x_0<=-gamma*D`, the orbit moves right by `gamma*c` at each positive-support step until it enters this half-strip. Its first such index is

\[
K=\left\lfloor\frac{-\gamma D-x_0}{\gamma c}\right\rfloor+1;
\quad K=0\text{ if }x_0>-\gamma D.
\tag{3}
\]

While `x<=-gamma*D`, it is nonpositive and the support increment is `gamma*b>0`, so support cannot be lost before this entry. In particular, `x_K>-gamma*D` and `y_K>0` whenever `y_0>0`.

Define

\[
M=\max\!\left(0,\left\lfloor\frac{\rho\gamma D-\eta_0}{\gamma\kappa}\right\rfloor+1\right),
\qquad N=\max(K,M).
\tag{4}
\]

Run the exact orbit through at most `N` steps, stopping earlier if `y<=0`. If support is lost, the preceding paragraph gives finite death. If it stays positive through `N`, then (2)--(4) give the strict finite certificate

\[
x_N>-\gamma D,\qquad \eta_N>\rho\gamma D,
\qquad y_N=\eta_N+\rho x_N>0.
\tag{5}
\]

Thus **every frozen orbit is dead after finitely many steps or reaches (5) after finitely many steps**. This is an exact finite algorithm for its selector, including strict-gate axis cases. There is no need for an upper bound on `x`: when `d<0`, the normal coordinate can move outward and grow linearly, but the one-sided certificate still works.

There is a wider simple-selector subcone on this one sign population. If `a<=b/rho`, then `b-rho*a>=0`, so both possible positive-support drifts are nonnegative and an initially positive `y` never closes. Thus for `z>0` the selector is exactly `1{y_0>0}` throughout `a<=b/rho`, including `d<=0`; the lower double-cone inequality `a>rho*b` is needed for *sliding capture*, not for survival of this sign population. The mirrored `z<0` population has its own corresponding condition, so both half-mark selectors are simultaneously simple in the original double ratio cone.

## Why (5) is robust under residual evolution

Allow subsequent `z_n>0,r_{1,n}<0<r_{2,n}` to vary, and write `a_n=-z_nr_{1,n}>0`, `b_n=z_nr_{2,n}>0`, `c_n=rho*b_n>=0`, `d_n=a_n-c_n`. Suppose merely `d_n<=D` for all later steps. Then, whenever support is positive, the variable-coefficient version of (2) gives `eta_{n+1}-eta_n=gamma(1-rho²)b_n>0`. It also preserves `x>-gamma*D`: a nonpositive `x` gains `gamma*c_n>=0`, while a positive `x` has `x-gamma*d_n> -gamma*D`. Induction from (5) proves `y_n=eta_n+rho*x_n>0` forever under these coefficient bounds. Bounds uniform on a compact strict mixed-residual neighborhood provide the intended open certificate. The argument also allows `d_n` to change sign and the normal to release and recapture.

If the varying coefficients have uniform positive lower bounds `c_n>=c_*>0` and `(1-rho²)b_n>=kappa_*>0`, the same calculation gives a uniform finite dead-or-certificate stopping bound, replacing `c,kappa` in (3)--(4) by `c_*,kappa_*`; if support is lost before then, finite death additionally needs `a_n` bounded below while the mixed sector persists. The frozen theorem needs no such variation hypothesis.

## Generic local constancy, and a strict step-size example

For fixed parameters, every finite orbit coordinate is `Xu` plus a constant on a specified finite gate word. Hence all pre-step axis equalities lie in a countable union of mark hyperplanes. Full-rank projected stable marks have a density; under the earlier independent marked-Poisson primitive, no atom lies on any such threshold almost surely. For a generic atom the finite stopping word and the terminal strict death or support certificate survive a sufficiently small perturbation of the mark, `z,r,rho,gamma`. Thus the all-mixed selector is locally constant away from these null thresholds, although it need not be constant across marks or step sizes.

For an exact rational, strict-margin example, take `rho=1/2,z=1,r=(-3,1)`, and `(x_0,y_0)=(11/10,3/10)`. Here `c=1/2,d=5/2`, and the `++` support drift is `-1/2`. At `gamma=1`, the first state is `(-7/5,-1/5)` and the row is dead. At `gamma=1/2`, the first three states are

\[
(-3/20,1/20),\quad(1/10,11/20),\quad(-23/20,3/10).
\tag{6}
\]

For `D=3`, the last state has `x_3>-3/2` and `eta_3=7/8>3/4=rho*gamma*D`, hence is certified. All gate and certificate inequalities used here are strict, so nearby marks and parameters give the same two outcomes. This explains why the gamma-independent stable half-mark masses of the initial **double cone** cannot simply be reused throughout all mixed residuals; outside that cone, the retained masses are selectors depending on `gamma,R`, and the original mark.

For `z<0`, swap coordinates 1 and 2 and use the positive magnitude `|z|`. The supporting coordinate is 1, and the same dead-or-certificate argument applies with `r_1,r_2` mirrored. As in `agents/h01_entrance.md`, finite stopping and finite-cutoff transfer do not by themselves establish a full residual-coupled macroscopic network law or justify interchanging infinitely many atoms with an increasing boundary horizon.

The exact-rational script `code/h01_entrance_check.py` and its actual output `outputs/h01_entrance_check.txt` check 3,362 all-mixed rational mark/step cases against the finite stopping bound, dead absorption, and 30 additional certified-support steps. All assertions passed; 1,832 cases died and 1,530 reached the one-sided support certificate. The script also checks the strict example (6) exactly.
