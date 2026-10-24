# account03/B01 — determinant-free finite-Lp control at the multiplicity-eight robust two-anchor endpoint

Run: `20260924T144335Z-account03-B01-fixedmult-s8-lp-r02`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Baseline manuscript: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, `manuscript.tex` blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.  
Fresh structural input: account03/B17, `yspennstate/math-open-problems@0408c579bcda638e72c010ff99892a22b9049796`, `improvements/account03/B17/20260924T141823Z-account03-B17-fixedmult-auto11/ROBUST_TWO_ANCHOR.md`.  
Designated partner input: account04/B01, `yspennstate/math-open-problems@beb9cc5cbb78b4fd4a8411862ac99fd7b7976034`, `improvements/account04/B01/20260924T130927Z-account04-B01-fixedmult-s13-L2-r1/THIRTEEN_EIGENVALUE_L2.md`.

Status: **PROVED SUPPORTING ENDPOINT THEOREM; multiplicity eight remains open.**

The later owner objective supersedes the older B01-only oscillatory brief for task selection, but this result is also an oscillatory replacement in exactly the old sense: it replaces false pointwise one-dimensional quadratic decay by a two-dimensional random-slope Plancherel estimate that is uniform in the anchor self-curvature and in an arbitrarily dependent complement phase.

## 1. Current mathematical frontier used in this run

The pinned seventeen-direction manuscript remains a valid baseline in this worker's audit. The support package named in its README is now present. Newer fleet work has lowered the bounded-density threshold to nine; the next unresolved structural frontier is multiplicity eight.

The account03/B17 robust-anchor theorem reduces the remaining no-pivot `s_8(A)>=1` collar to a literal original-coordinate pair `H={h_1,h_2}` with

\[
C=A[H,H^c],\qquad D_H:=\det(CC^T)\ge D_0,
\]

where

\[
D_0=0.3649442658827020\ldots.
\]

The pair self-block `K=A[H,H]` can be zero, rank one, or invertible and arbitrarily near singular. The exact-zero case is already bounded continuously; for invertible `K`, B17 pays the moving logarithmic Schur singularity but leaves a nonlogarithmic `6|det K|^{-1/2}` term. The issue is therefore to obtain estimates that do not deteriorate at all as `det K -> 0`.

## 2. New theorem: robust two-anchor finite-Lp compiler

### Theorem `QFORM-ROBUST-TWO-ANCHOR-FINITE-LP-v1`

Let `X=(X_1,X_2)` be a random vector on `R^2` with probability density `f` satisfying

\[
0\le f\le1.
\]

(For the QFORM application, `X_1,X_2` are independent original coordinates with individual density caps one, so this joint cap is automatic.) Let `Y` be independent of `X`. Let

\[
K=K^T\in\mathbb R^{2\times2},\qquad
L=L(Y)\in\mathbb R^2,\qquad R=R(Y)\in\mathbb R,
\]

where `R` is arbitrary measurable and may be arbitrarily dependent on `L`. Assume only that `L` has a probability density `g` satisfying

\[
\|g\|_\infty\le M<\infty.
\]

Define

\[
Q=X^TKX+2X\cdot L+R.
\tag{2.1}
\]

Then, for every `t != 0`,

\[
\boxed{
|\phi_Q(t)|\le
\min\left\{1,{\pi\sqrt M\over |t|}\right\}.
}
\tag{2.2}
\]

Consequently, for every finite `r>=2`, the law of `Q` has a density `p_Q in L^r(R)` and

\[
\boxed{
\|p_Q\|_r\le (r\sqrt M)^{1-1/r}.
}
\tag{2.3}
\]

Equivalently, if `J` is any interval of length `h`,

\[
\boxed{
\Pr\{Q\in J\}\le (r\sqrt M\,h)^{1-1/r}.
}
\tag{2.4}
\]

If `x:=sqrt(M)h<=e^{-2}`, choosing `r=log(1/x)` gives the near-Lipschitz small-ball estimate

\[
\boxed{
\Pr\{Q\in J\}
\le e\sqrt M\,h\log{1\over\sqrt M h}.
}
\tag{2.5}
\]

Finally, for every `0<alpha<1`,

\[
\boxed{
\sup_a \mathbb E\!\left[
 |Q-a|^{-\alpha}\mathbf 1_{\{|Q-a|\le1\}}
\right]
\le
\left[
 {4(1+\alpha)\sqrt M\over(1-\alpha)^2}
\right]^{(1+\alpha)/2}.
}
\tag{2.6}
\]

No bound in this theorem depends on `K`, its determinant, its rank, its signature, or its operator norm. No regularity of `R`, no density for the pair `(L,R)`, and no independence between `L` and `R` is assumed.

### Proof

For each `t`, define the complex measure on `R^2`

\[
\nu_t(E)=\mathbb E\left[e^{itR}\mathbf 1_{\{L\in E\}}\right].
\]

Its total variation is dominated by the law of `L`. Hence, writing the latter as `g(l)dl`, there is a measurable `h_t` with `|h_t|<=1` such that

\[
d\nu_t(l)=h_t(l)g(l)\,dl.
\tag{2.7}
\]

Set

\[
a_t(x)=f(x)e^{itx^TKx},
\qquad
F_t(l)=\int_{\mathbb R^2} a_t(x)e^{2it l\cdot x}\,dx.
\]

Then

\[
\phi_Q(t)=\int_{\mathbb R^2}h_t(l)g(l)F_t(l)\,dl.
\tag{2.8}
\]

By Cauchy--Schwarz,

\[
|\phi_Q(t)|\le\|g\|_2\|F_t\|_2.
\tag{2.9}
\]

Since `g` is a probability density bounded by `M`,

\[
\|g\|_2\le\sqrt M.
\tag{2.10}
\]

With the Fourier convention `\hat a(\xi)=\int e^{i\xi\cdot x}a(x)dx`, we have

\[
F_t(l)=\widehat a_t(2tl).
\]

Two-dimensional Plancherel and the change `xi=2tl` give

\[
\begin{aligned}
\|F_t\|_2^2
&={1\over4t^2}\int_{\mathbb R^2}|\widehat a_t(\xi)|^2\,d\xi\\
&={1\over4t^2}(2\pi)^2\int_{\mathbb R^2}f(x)^2\,dx\\
&\le {\pi^2\over t^2},
\end{aligned}
\tag{2.11}
\]

because `f<=1` and `\int f=1`. Equations (2.9)--(2.11), together with the trivial characteristic-function bound, prove (2.2). Notice that the quadratic anchor phase has completely disappeared from the norm calculation; this is why no pointwise one-dimensional van der Corput estimate is being smuggled in.

Now fix finite `r>=2` and put

\[
q={r\over r-1}\in(1,2],\qquad a=\pi\sqrt M.
\]

From (2.2),

\[
\|\phi_Q\|_q^q
\le 2a+2a^q\int_a^\infty t^{-q}dt
=2a\,{q\over q-1}
=2\pi r\sqrt M.
\tag{2.12}
\]

The inverse Hausdorff--Young inequality in the present Fourier normalization is

\[
\|\mathcal F^{-1}\phi\|_r
\le(2\pi)^{-1/q}\|\phi\|_q.
\tag{2.13}
\]

For completeness, existence of the density follows without any informal inversion step: multiply `phi_Q` by `e^{-epsilon t^2}`. The corresponding Gaussian-smoothed laws have densities; (2.13) shows that these densities are Cauchy in `L^r` as `epsilon downarrow0`, because the multipliers converge to one in `L^q(|phi_Q|^qdt)`. Their `L^r` limit represents the original law by weak convergence against compactly supported continuous test functions. Combining (2.12) and (2.13) gives exactly (2.3).

Equation (2.4) is Holder on an interval. If `x=sqrt(M)h<=e^{-2}` and `r=log(1/x)`, then `r>=2` and

\[
(rx)^{1-1/r}
=rx\exp\left({r-\log r\over r}\right)
\le e\,rx,
\]

which gives (2.5).

For (2.6), take

\[
r={2\over1-\alpha},\qquad q={2\over1+\alpha}.
\]

Holder gives

\[
\int_{|x|\le1}|x|^{-\alpha}p_Q(a+x)dx
\le\|p_Q\|_r
\left({2\over1-\alpha q}\right)^{1/q}.
\]

Substituting (2.3), `1-alpha q=(1-alpha)/(1+alpha)`, and the displayed `r,q` yields (2.6).

## 3. Application to the fresh multiplicity-eight robust collar

For the B17 pair `H`, put `Y=X_{H^c}` and

\[
L(Y)=CY+b_H/2,
\qquad
R(Y)=Y^TA_{H^c,H^c}Y+b_{H^c}^TY+c.
\]

Then the full quadratic polynomial is exactly of the form (2.1), with `K=A[H,H]` and `X=X_H`. The outside cross map has

\[
D_H=\det(CC^T)\ge D_0.
\]

Let `G=CC^T` and `U=G^{-1/2}C`. Since `UU^T=I_2`, the baseline product-projection theorem gives `UY` a density bounded by `e`. Therefore `L` has a two-dimensional density bounded by

\[
M\le {e\over\sqrt{D_H}}
\le {e\over\sqrt{D_0}}
=4.499675651055483\ldots,
\tag{3.1}
\]

so

\[
\sqrt M\le2.121243892402636\ldots .
\tag{3.2}
\]

The new theorem now holds throughout the **entire** remaining robust-pair collar, uniformly through `det K=0`:

\[
\boxed{
|\phi_Q(t)|
\le
\min\{1,6.664084228844337/|t|\}.
}
\tag{3.3}
\]

For every finite `r>=2`,

\[
\boxed{
\|p_Q\|_r
\le
(2.121243892403\,r)^{1-1/r}.
}
\tag{3.4}
\]

For intervals with `2.121244 h<=e^{-2}`,

\[
\boxed{
\Pr\{Q\in J\}
\le
5.766138726448\,h
\log{1\over2.121243892403\,h}.
}
\tag{3.5}
\]

At `alpha=1/2`, the truncated half potential is uniformly bounded by

\[
\boxed{
\sup_a\mathbb E\!\left[|Q-a|^{-1/2}\mathbf1_{|Q-a|\le1}\right]
\le (24\sqrt M)^{3/4}
<19.060.
}
\tag{3.6}
\]

Thus the apparent determinant singularity in the near-singular anchor block is **not present at any finite Lp level**. The surviving obstruction to multiplicity eight is a genuine endpoint phenomenon: remove the one logarithm between (3.5) and a Lipschitz small-ball estimate, or obtain an equivalent `L^infinity` receiver from additional QFORM structure. This is more precise than describing the remaining issue as simply `det K ->0`.

## 4. Designated partner result applied to an actual inequality

The completed account04/B01 theorem at commit `beb9cc5cbb78b4fd4a8411862ac99fd7b7976034` proves, with the full arbitrary-law/affine/sign scope,

\[
s_{13}(A)\ge s
\quad\Longrightarrow\quad
\|p_Q\|_2\le\sqrt{6010}\,{K\over\sqrt s}.
\]

Applying Cauchy--Schwarz to an interval `J` gives the concrete distribution-function estimate

\[
\boxed{
\Pr\{Q\in J\}
\le
\sqrt{6010}\,{K\over\sqrt s}\,|J|^{1/2}
<77.525\,{K\over\sqrt s}\,|J|^{1/2}.
}
\tag{4.1}
\]

This confirms that the order-four crossing endpoint already has a dimension-free square-root small-ball law even though its absolute Fourier envelope is only `1/|t|`. The new two-anchor compiler above upgrades that endpoint style to every finite `L^r` in the sharper `s_8` robust collar.

## 5. Phase-aligned counterexample remains preserved

Nothing here repairs the false one-dimensional pointwise quadratic-phase claim. Fix any `tau != 0` and `epsilon>0`. The set of real `x` for which `tau x^2` lies within `epsilon` modulo `2pi` of `0` contains infinitely many disjoint intervals with unbounded total measure. Choose finitely many subintervals of total length one and let `f` be their indicator. Then `f` is a probability density with `0<=f<=1` and

\[
\Re\int e^{i\tau x^2}f(x)dx\ge\cos\epsilon.
\]

Thus no law-uniform positive-power pointwise decay in `|tau|` can hold. The new result works because it averages the **random two-dimensional slope** in `L^2` and uses Plancherel before any forbidden absolute pointwise quadratic estimate.

## 6. Baseline audit refresh and current status

The baseline source blob is unchanged from the prior complete B01 audit. The four support files that were absent during that earlier audit (`SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, `checks.json`) are now present; `checks.json` records a passing scoped suite. The earlier package mismatch is therefore resolved. The mathematical baseline remains PASS in this worker's prior end-to-end audit; this run found no new fatal defect in the rechecked theorem/scaling/dependency chain.

Fresh fleet evidence also shows a stronger already-reviewed bounded-density theorem at multiplicity nine; this run does not relabel that peer result as its own proof. The **full three-eigenvalue conjecture remains OPEN**, and multiplicity eight remains OPEN.

Continuity: Theorem (2.3) proves absolute continuity and finite `L^r` regularity for all finite `r`, but does **not** prove a continuous representative. The B17 exact-zero subcase remains continuous by its separate direct argument. Global continuity is open.

## 7. Next exact proof obligation

The next B01 endpoint is now:

`QFORM-S8-ROBUST-TWO-ANCHOR-LOG-ENDPOINT-REMOVAL-v1`.

Given the fixed robust cross determinant `D_H>=D_0`, upgrade the determinant-free family

\[
\|p_Q\|_r\lesssim (Cr)^{1-1/r}
\]

for all finite `r` to a uniform `L^infinity` bound, using structure not available to arbitrary functions with linear-in-r `L^r` growth. A successful mechanism must retain the original-product provenance of `L=CY+b/2` and the fact that `R` is a quadratic polynomial in the same outside bank, rather than replacing `(L,R)` by an arbitrary joint law.

No scheduler/task state, cadence, notification setting, permission, cross-account authentication, paid call, remote workflow, or public-release setting is changed by this result.
