# Marginal-law review: nested critical grids give distinct macroscopic path laws

**Reviewed conclusion.** Assume the initial joint law and macro compactness theorems of the preceding run and the conditional mixed-cone selection theorem in `../agents/f03_cone.md`. For `G=[[1,-1/2],[-1/2,1]]`, every fixed label vector, and physical steps `1/L_m` and `1/(10L_m)`, the sets of possible unconditioned subsequential macroscopic **output path laws** are disjoint. In particular, if full unconditioned limits exist, they are different. This conclusion does not assert that either unconditioned full limit exists or that their behavior outside the mixed residual cone is known.

## Exact nested-grid selector inequality

On `r_1<0<r_2`, take any `z>0` and an initial `+-` projected mark `(x,y)`, `x>0>y`. Write `k=-rho>0` and `a=-zr_1>0`. The exact frozen-grid selector in `../agents/f01_entrance.md` or `../agents/f03_cone.md` says that this atom eventually supports coordinate 2 precisely when

\[
 y+k a c_\gamma(t_x)>0,\qquad
 t_x=x/a,\qquad c_\gamma(t)=\gamma\lceil t/\gamma\rceil .
\tag{1}
\]

All other initial sectors have a gamma-independent terminal choice: `y>0` eventually supports coordinate 2, and `x<=0,y<=0` is dead, outside null axis marks. For `gamma_c=1` and `gamma_f=1/10`, every coarse grid point is also a fine grid point. The least coarse grid point at or after `t` is therefore no earlier than the least fine grid point:

\[
 c_{\gamma_c}(t)\ge c_{\gamma_f}(t)\quad\text{for every }t>0.
\tag{2}
\]

Equations (1)--(2), including the strict inequality at a threshold, show that **every positive-`z` atom supporting coordinate 2 at the fine grid also supports it at the coarse grid**. The negative-`z` selector gives the analogous inclusion for coordinate 1, but is unnecessary for this proof. Let

\[
 P_{2,\gamma}=\int z^2\mathbf1\{\sigma_\gamma(z,u;R)=2\}\,N(dz,du).
\tag{3}
\]

The Poisson square sum is finite almost surely, so (2) implies `P_{2,c}>=P_{2,f}` almost surely under the common primitive `(F,C,N)` whenever `R_1<0<R_2`.

The inequality is strict with positive probability. Fix `rho=-1/2`, `z` in `(.995,1.005)`, projected mark `Xu` in `(.13,.15) x (-.13,-.11)`, and residual `R` in

\[
 B=(-1.005,-.995)\times(.995,1.005).
\tag{4}
\]

The interval arithmetic in `f01_entrance.md` proves that **every** such atom escapes to `-+` at `gamma_c=1` and dies at `gamma_f=.1`. The projected stable mark has a positive density because `X` has rank 2, so the atom set has positive finite Poisson intensity. `R=y-F` has full support and is independent of `N`, so `P(R in B and at least one target atom)>0` for any fixed labels. On that event,

\[
 P_{2,c}-P_{2,f}\ge (.995)^2>0.
\tag{5}
\]

No exclusion of other atoms is needed: (2) makes every other atom's contribution to the difference nonnegative. The unbounded large-atom square expectation is irrelevant; both random masses are finite almost surely.

## A bounded statistic of the output path

Let `f_gamma` denote the selected macroscopic output on the mixed cone. The theorem in `f03_cone.md` gives, for every `T<infinity`,

\[
 r_\gamma(t)=e^{-Q_\gamma t}R,
 \qquad Q_\gamma=C+\operatorname{diag}(P_{1,\gamma},P_{2,\gamma}),
 \qquad f_\gamma(t)=y-r_\gamma(t).
\tag{6}
\]

Its right derivative at zero exists and obeys

\[
 f'_{\gamma,2}(0+)=(CR)_2+R_2P_{2,\gamma}.
\tag{7}
\]

Both `R=y-f(0)` and this derivative are measurable from the **output path alone**. For a path `g in C([0,T];R^2)`, set `R(g)=y-g(0)`. Define `D_2(g)` to be the limit of `(g_2(T/n)-g_2(0))/(T/n)` as `n->infinity` when the limit exists, and zero otherwise. The existence set and limit are Borel measurable as limits of continuous evaluation maps. Choose the bounded strictly increasing function `psi(s)=1/2+arctan(s)/pi`, and define the bounded Borel path statistic

\[
 H(g)=\mathbf1\{R(g)\in B\}\,\psi(D_2(g)).
\tag{8}
\]

Under the common-primitive coupling of the two selected conditional laws, (2), (5), and `R_2>0` on `B` imply

\[
 H(f_c)\ge H(f_f)\quad\text{almost surely},
 \qquad P\{H(f_c)>H(f_f)\}>0.
\tag{9}
\]

Since `0<=H<=1`, its expectations are finite and `E H(f_c)>E H(f_f)`. Thus the **marginal** selected path laws differ; this inference uses a measurable path statistic, not merely positive-probability separation in one coupling.

## What this implies for unconditioned subsequences

The earlier `MACRO_COMPACTNESS.md` makes the unconditioned polygonal output laws tight in `C([0,T];R^2)`. The `f03_cone.md` theorem identifies their restrictions to the observable initial event `R(g)_1<0<R(g)_2`, for each gamma, with the selected law (6). The boundary of `B` has zero probability because `R` has a density. Hence **every** unconditioned subsequential path law for gamma `1` has the same expectation of (8), namely the coarse expectation in (9), and **every** such law for gamma `.1` has the distinct fine expectation. This proves the disjointness asserted at the top, without selecting any branch outside the mixed cone. The result also applies to held paths because the earlier macro theorem makes their distance from polygonal paths vanish on fixed horizons.

For reproducibility, `../code/f04_nested_selector_check.py` implements both the analytic selector and direct sector iteration with seed `20261024`; its captured execution is `../outputs/f04_nested_selector_check.txt`. It checked 100,000 random cone instances with no analytic/direct mismatch, 3,881 coarse-only escapes, and zero fine-only escapes. These checks support but do not replace the exact inequality (2). Nonnested multipliers have no such ordering: the central mark escapes at `.13` and dies at `.2`.
