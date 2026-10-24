SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B15, 2026-09-23T18:02:50Z.
attacking: expected-conditional-height regularity compiler and rough-input bridge; derive a source-valid obstruction to extending the completed Gaussian-mixture branch to arbitrary rough cap-one inputs.

# Early mathematical checkpoint — a BV obstruction to Gaussian-mixture rough closure

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T180250Z-account02-B15-qform-auto12`  
Status: `SUBSTANTIVE_PARTIAL / SOURCE-VALID APPROXIMATION OBSTRUCTION / FULL QFORM OPEN`.

## First unpaid implication

The unrestricted theorem is still the uniform small-ball/height estimate

\[
\sup_{n,A,f_i,y,\varepsilon>0}
\varepsilon^{-1}\Pr\{|X^TAX-y|\le \varepsilon\}<\infty,
\qquad s_3(A)\ge1,
\]

over arbitrary independent probability densities `0<=f_i<=1`.  Fixed-instance absolute continuity or `C_0` regularity does not pay this quantifier reversal.

A tempting completion route after the newly completed arbitrary-rank Gaussian-component-mixture theorem is: approximate every cap-one marginal weakly by Gaussian location-scale mixtures satisfying the same average component-peak budget, use the already-paid mixture height estimate, then invoke account03/B15's zero-loss weak interval trace.  The calculation below proves that this approximation premise is false, even for smooth compactly supported cap-one marginals.

## Gaussian-mixture BV bound

Let

\[
g(x)=\int \gamma_\sigma(x-m)\,\Pi(dm,d\sigma),\qquad \sigma>0,
\]

where `gamma_sigma` is the centered Gaussian density of standard deviation `sigma`.  Put

\[
K(\Pi):=\int \sigma^{-1}\,d\Pi.
\]

Then

\[
\|g\|_\infty\le \frac{K(\Pi)}{\sqrt{2\pi}}
\]

and, more importantly,

\[
\operatorname{Var}(g)=\|g'\|_{L^1}
\le \sqrt{\frac2\pi}\,K(\Pi). \tag{1}
\]

Indeed `||gamma_sigma'||_1=sqrt(2/pi)/sigma`, and differentiation under the mixture followed by Tonelli/Minkowski gives (1).

Consequently the mixture class with the manuscript's cap-compatible budget

\[
K(\Pi)\le \sqrt{2\pi}
\]

lies inside the rigid source class

\[
0\le g\le1,\qquad \operatorname{Var}(g)\le2. \tag{2}
\]

This is source regularity, not an output continuity assertion.

## Weak closure retains the BV cost

Suppose `g_m dx => mu` weakly and each `g_m` is such a Gaussian mixture with `K(Pi_m)<=K`.  The height bound gives `mu<=K/sqrt(2*pi) dx`, so `mu=g dx`.  For every `phi in C_c^1`,

\[
\left|\int g\,\phi'\right|
=\lim_m\left|\int g_m\,\phi'\right|
\le \sqrt{\frac2\pi}K\,\|\phi\|_\infty.
\]

Hence `g in BV` and

\[
\operatorname{Var}(g)\le \sqrt{\frac2\pi}K. \tag{3}
\]

More generally, if only `liminf K(Pi_m)<infty`, lower semicontinuity gives

\[
\liminf_m K(\Pi_m)
\ge \sqrt{\frac\pi2}\,\operatorname{Var}(g). \tag{4}
\]

Thus the average inverse-scale budget cannot stay uniformly bounded when the limiting cap-one source has large variation.

## Smooth compact cap-one witnesses with arbitrarily large required budget

Fix `N>=2`.  Choose `N` disjoint intervals `I_j` of length `1/N`, separated by gaps larger than `4 delta`, and a nonnegative `C_c^infinity` mollifier `eta_delta` of mass one supported in `[-delta,delta]`.  Put

\[
E_N=\bigcup_{j=1}^N I_j,\qquad f_N=1_{E_N}*\eta_\delta.
\]

Then

\[
0\le f_N\le1,\qquad \int f_N=1,
\]

so `f_N` is an admissible QFORM marginal.  Because the `2N` mollified jump profiles have disjoint supports,

\[
\operatorname{Var}(f_N)=2N. \tag{5}
\]

If Gaussian mixtures `g_m` converge weakly to `f_N dx`, (4) and (5) force

\[
\boxed{\liminf_m E\,\sigma_m^{-1}\ge N\sqrt{2\pi}.} \tag{6}
\]

In particular, for the budget `sqrt(2*pi)` used by the completed Gaussian-mixture QFORM theorem, already `N=2` is impossible; and no fixed constant relaxation of that budget is weakly dense in all smooth compact cap-one densities, because `N` is arbitrary.

This is an exact target-level obstruction: take three independent coordinates with marginal `f_N` and, for example, `A=I_3`.  The resulting instance satisfies every owner hypothesis.  It is not a counterexample to the QFORM theorem (indeed this diagonal instance is already bounded); it refutes only the proposed rough-input completion route through uniformly budgeted Gaussian-mixture approximation.

## Why the partner weak-trace theorem matters

The completed account03/B15 rough-trace theorem shows that if a sequence of certified inputs converges weakly to an admissible source and the output interval estimates have one common constant, then that constant passes to the limit with zero loss.  Therefore the only missing premise in the Gaussian-mixture approximation strategy would have been density of the certified source class.  Equations (3)-(6) prove that premise fails sharply: the certified source class has a hidden BV bound.

Next step in this run: independently re-check the ruled one-sheet rough bridge at the current corrected scope (in particular, the source audit's requirement that the linear term lie in the quadratic range), and apply that completed result to an explicit majority-side tent/heat inequality without using continuity.
