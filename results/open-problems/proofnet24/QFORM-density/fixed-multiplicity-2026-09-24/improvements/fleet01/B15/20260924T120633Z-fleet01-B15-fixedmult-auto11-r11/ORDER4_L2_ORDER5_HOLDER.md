# B15 improvement: order-four endpoint L2 law and order-five pointwise Holder regularity

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Run: `20260924T120633Z-fleet01-B15-fixedmult-auto11-r11`  
Baseline source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Baseline manuscript blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`

Status: **proved supporting endpoint/regularity theorems; no multiplicity reduction of the L-infinity theorem is claimed.**

The baseline no-pivot mechanism gives, after a random original-coordinate cut, the Fourier envelope

\[
 |\phi_Q(t)|\le \min\left\{1,\left(\frac{u_k}{|t|}\right)^{k/4}\right\},
 \qquad
 u_k=\pi e\,Z_k(M)^{-1/(2k)}.
\tag{1}
\]

If there is no `eta=1/100` pivot and `s_{4k-3}(A)>=1`, the baseline spectral-to-volume proposition plus random cut gives

\[
 Z_k(M)\ge4^{-k}\kappa^k,
 \qquad \kappa=80^{-2},
\]

and consequently

\[
 u_k\le \pi e\,(4^{-k}\kappa^k)^{-1/(2k)}
 =160\pi e.
\tag{2}
\]

The two conclusions below identify what the adjacent orders `k=4` and `k=5` actually buy.

## Theorem A: thirteen directions give an L2 output law in the no-pivot chamber

Assume independent cap-one coordinate densities, arbitrary affine terms, `A=A^T`, no `eta`-pivot, and

\[
 s_{13}(A)\ge1.
\]

Then `Q=X^TAX+b^TX+c` has an `L^2(R)` density `p_Q`. More precisely, for the cut supplied by the order-four volume argument, if

\[
 u=\pi e Z_4(M)^{-1/8}\le160\pi e,
\]

then

\[
 \boxed{\|p_Q\|_2\le\sqrt{\frac{2u}{\pi}}\le\sqrt{320e}<29.50.}
\tag{3}
\]

It also obeys the translation estimate

\[
 \boxed{
 \|p_Q(\cdot+h)-p_Q\|_2
 \le\frac{2u}{\sqrt\pi}|h|^{1/2}
 \le320e\sqrt\pi\,|h|^{1/2}.
 }
\tag{4}
\]

### Proof

For `k=4`, (1) reads

\[
 |\phi_Q(t)|\le\min\{1,u/|t|\}.
\tag{5}
\]

Hence

\[
 \int_{\mathbb R}|\phi_Q(t)|^2dt
 \le2u+2u^2\int_u^\infty t^{-2}dt
 =4u.
\tag{6}
\]

This already implies absolute continuity with an `L^2` density without presupposing any density of `Q`. Let `\mu` be the law of `Q`, let `g_\epsilon` be the Gaussian heat kernel used in the manuscript, and write

\[
 p_\epsilon=\mu*g_\epsilon.
\]

Then

\[
 \widehat p_\epsilon(t)=e^{-\epsilon t^2}\phi_Q(t).
\]

Because `phi_Q in L^2`, dominated convergence shows these Fourier transforms form a Cauchy family in `L^2`. Plancherel therefore makes `p_epsilon` Cauchy in `L^2`; write its limit as `p`. For every `psi in C_c(R)`, `psi in L^2`, so

\[
 \int \psi p_\epsilon\to\int\psi p.
\]

On the other hand `\mu*g_\epsilon -> \mu` weakly. Thus `\mu=p(x)dx`. Plancherel and (6) give

\[
 \|p\|_2^2\le(2\pi)^{-1}4u=2u/\pi,
\]

which proves (3).

For (4), Plancherel gives

\[
 \|\tau_hp-p\|_2^2
 =\frac1{2\pi}\int_{\mathbb R}|e^{-ith}-1|^2|\phi_Q(t)|^2dt.
\tag{7}
\]

Put `delta=u|h|` and scale `t=ur`. Using

\[
 |e^{-ith}-1|^2\le\min(4,h^2t^2)
\]

and (5), the integral in (7), before the factor `1/(2pi)`, is at most

\[
 2u\int_0^\infty
 \min(4,\delta^2r^2)\min(1,r^{-2})dr.
\tag{8}
\]

If `delta<=2`, splitting at `r=1` and `r=2/delta` gives

\[
 \int_0^\infty
 \min(4,\delta^2r^2)\min(1,r^{-2})dr
 =4\delta-\frac23\delta^2\le4\delta.
\]

If `delta>=2`, the trivial bound `4 int_0^infinity min(1,r^-2)dr=8` is at most `4delta`. Hence (8) is at most `8u delta=8u^2|h|`. Dividing by `2pi` and taking a square root proves (4). QED.

### Why Theorem A does not lower the density theorem to thirteen

The endpoint (5) is not absolutely integrable. Moreover an `O(1/|t|)` characteristic-function bound alone cannot imply a bounded density. A self-contained witness is

\[
 p(x)=-\frac12\log|x|\,\mathbf1_{\{|x|\le1\}}.
\tag{9}
\]

It is a probability density and is unbounded at zero. Integration by parts gives its characteristic function

\[
 \phi(t)
 =-\int_0^1\log x\cos(tx)dx
 =\frac{\operatorname{Si}(t)}{t},
\tag{10}
\]

so `|phi(t)|=O(1/|t|)`. Thus the order-four endpoint needs an additional QFORM-specific cancellation/structure theorem before it can yield an `L^infinity` bound.

This is consistent with the baseline architecture: `k=4` corresponds algebraically to `4*4-3=13` spectral directions, but the present absolute-inversion receiver stops exactly at the nonintegrable endpoint.

## Theorem B: explicit C^{0,1/4} regularity in the seventeen-direction no-pivot chamber

Under the same arbitrary cap-one product-law and affine-term hypotheses, suppose instead that there is no `eta`-pivot and

\[
 s_{17}(A)\ge1.
\]

Then the baseline no-pivot density has a canonical representative in `C_0(R)` and, with

\[
 u=\pi e Z_5(M)^{-1/10}\le160\pi e,
\]

satisfies

\[
 \boxed{
 |p_Q(x+h)-p_Q(x)|
 \le
 \frac{32}{3\pi 2^{1/4}}u^{5/4}|h|^{1/4}.
 }
\tag{11}
\]

In particular the universal no-pivot chamber bound is

\[
 [p_Q]_{C^{0,1/4}}
 \le
 \frac{32}{3\pi 2^{1/4}}(160\pi e)^{5/4}
 <2.372\times10^4.
\tag{12}
\]

### Proof

For `k=5`, (1) gives

\[
 |\phi_Q(t)|\le\min\{1,(u/|t|)^{5/4}\}.
\tag{13}
\]

This is integrable, so manuscript Fourier inversion gives a bounded continuous density; Riemann-Lebesgue applied to the `L^1` inverse-transform integrand gives the canonical representative in `C_0(R)`.

For the modulus, Fourier inversion and `|e^{-ith}-1|<=min(2,|h||t|)` give

\[
 |p_Q(x+h)-p_Q(x)|
 \le\frac1\pi\int_0^\infty
 \min(2,|h|t)\min\{1,(u/t)^{5/4}\}dt.
\tag{14}
\]

Set `t=ur`, `delta=u|h|`. The right side is `(u/pi)I(delta)`, where

\[
 I(\delta)=\int_0^\infty
 \min(2,\delta r)\min(1,r^{-5/4})dr.
\]

For `0<delta<=2`, splitting at `1` and `2/delta` gives exactly

\[
 I(\delta)
 =\frac{32}{3\,2^{1/4}}\delta^{1/4}-\frac56\delta
 \le\frac{32}{3\,2^{1/4}}\delta^{1/4}.
\tag{15}
\]

For `delta>=2`, splitting at `2/delta` and `1` gives

\[
 I(\delta)=10-\frac2\delta\le10
 \le\frac{32}{3\,2^{1/4}}\delta^{1/4},
\tag{16}
\]

because at `delta=2` the last right side is `32/3>10` and increases thereafter. Substituting (15)-(16) into (14) proves (11), and (2) gives (12). QED.

## Exact threshold/regularity ledger after this improvement

For the **no-pivot** branch of the current baseline mechanism:

- order `k=3`, requiring `s_9(A)>=1`: Fourier tail `|t|^{-3/4}`; not a density inversion theorem, but after the Riesz weight `|t|^{-1/2}` it gives the full negative-half-potential estimate;
- order `k=4`, requiring `s_13(A)>=1`: Fourier tail `|t|^{-1}`; gives the new `L^2` density and `L^2` translation-1/2 modulus above, but not a bounded density;
- order `k=5`, requiring `s_17(A)>=1`: Fourier tail `|t|^{-5/4}`; gives `L^infinity`, `C_0`, and the explicit pointwise `C^{0,1/4}` modulus above.

The pivot branches of the manuscript are measure-domination arguments and do not inherit Theorem B automatically. Therefore this artifact deliberately does **not** strengthen the global theorem's regularity statement and does **not** claim a `17 -> 13` multiplicity reduction.

The precise remaining lower-threshold obligation is: upgrade the order-four no-pivot endpoint from `L^2`/`1/t` Fourier control to a dimension-free `L^infinity` density bound using additional QFORM structure, or replace the present receiver. The scalar/definite/indefinite pivot branches already close under thirteen large eigenvalues; the no-pivot endpoint is the obstruction.
