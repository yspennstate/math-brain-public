# R19 / E0071 — Problem 3 fails even in Björklund's suggested symmetric product/diagonal special case

Date: 2026-09-18 UTC.  
Worker: R19 CLOSABLE OUTSIDE.  
Source: Michael Björklund, *Five remarks about random walks on groups*, arXiv:1406.0763v2, Appendix II §7.1, Problem 3.

## Result

The previous R19 artifact refuted the printed Problem 3 using `G=Z`, `H={0}` and the simple symmetric walk. This note strengthens that refutation to **exactly the special case suggested immediately after Problem 3**:

\[
G=G_0\times G_0,\qquad H=\Delta G_0,\qquad \mu=\mu_0\otimes\mu_0,
\]

with `mu_0` symmetric. In fact the displayed quantity does not merely stay positive: it diverges like an explicit constant times `sqrt(n)`.

Take

\[
G_0=\mathbb Z,
\qquad
\mu_0=\frac14\delta_{-1}+\frac12\delta_0+\frac14\delta_1.
\]

Set

\[
G=\mathbb Z^2,
\qquad
H=\Delta\mathbb Z=\{(m,m):m\in\mathbb Z\},
\qquad
\mu=\mu_0\otimes\mu_0.
\]

Identify `G/H` with `Z` by

\[
q(x,y)=x-y,
\]

and equip the quotient with

\[
d((x,y)H,(x',y')H)
=|(x-y)-(x'-y')|.
\tag{1}
\]

Then every hypothesis of Problem 3 holds, `H` has infinite index, `mu` is symmetric, and

\[
\frac1n\sum_{k=1}^n
\int_G d(gH,H)\,d\mu^{*k}(g)
\sim
\frac23\sqrt{\frac{2}{\pi}}\,\sqrt n
\longrightarrow +\infty.
\tag{2}
\]

Thus the printed statement fails even in the exact symmetric product/diagonal test case proposed by the source.

## 1. The measured-group and quotient hypotheses are exact

The support of `mu_0` is `{-1,0,1}`. Hence the support of `mu` contains

\[
(1,0),\ (-1,0),\ (0,1),\ (0,-1),
\]

so it generates all of `Z^2` as a semigroup. Therefore `(G,mu)` is a measured group in the source convention. The measure is symmetric.

The diagonal subgroup has infinite index because

\[
G/H\cong\mathbb Z
\]

through `q(x,y)=x-y`. Formula (1) is therefore a genuine metric and is left `G`-invariant. Its one-step moment is finite (indeed the quotient increment is bounded by 2), so all displayed integrals are finite.

## 2. The Poisson boundary is trivial, hence H acts ergodically

A random variable `A` with law `mu_0` has the same distribution as

\[
A\overset d=\frac{\varepsilon_1+\varepsilon_2}{2},
\]

where `epsilon_1,epsilon_2` are independent Rademacher variables. Consequently, after `k` steps, one coordinate of the `G`-walk has the law

\[
\frac12 S_{2k},
\]

where `S_m` is ordinary simple symmetric random walk after `m` Rademacher increments. Thus

\[
\Pr(X_k=0)=\frac{\binom{2k}{k}}{2^{2k}}.
\]

The two coordinates of the product walk are independent, so

\[
\Pr((X_k,Y_k)=(0,0))
=
\left(\frac{\binom{2k}{k}}{2^{2k}}\right)^2
\sim \frac1{\pi k}.
\tag{3}
\]

Hence

\[
\sum_{k\ge1}\Pr((X_k,Y_k)=(0,0))=\infty.
\]

Because the chain is irreducible, it is recurrent. If `f` is any bounded `mu`-harmonic function and `tau_y` is the hitting time of `y`, recurrence gives `tau_y<infinity` almost surely. The bounded martingale `f(Z_{m\wedge\tau_y})` and dominated convergence give

\[
f(x)=\mathbb E_x f(Z_{\tau_y})=f(y).
\]

Thus every bounded harmonic function is constant. By the source's Poisson representation, the Poisson boundary is a one-point space. Therefore every subgroup, in particular `H=Delta Z`, acts ergodically on it.

## 3. Exact quotient law

Let `A_i,B_i` be iid with law `mu_0`, with the two sequences independent. The quotient coordinate after `k` product steps is

\[
Q_k=\sum_{i=1}^k(A_i-B_i).
\]

Since

\[
A_i-B_i
\overset d=
\frac{\varepsilon_{i,1}+\varepsilon_{i,2}+\varepsilon_{i,3}+\varepsilon_{i,4}}2,
\]

where the four signs are independent Rademachers, we obtain the exact identity in distribution

\[
Q_k\overset d=\frac12 S_{4k}.
\tag{4}
\]

The quotient metric (1) therefore gives

\[
\int_G d(gH,H)\,d\mu^{*k}(g)
=\mathbb E|Q_k|
=\frac12\mathbb E|S_{4k}|.
\tag{5}
\]

## 4. Exact expectation and asymptotic divergence

For simple symmetric random walk,

\[
\mathbb E|S_{2m}|
=2m\frac{\binom{2m}{m}}{2^{2m}}.
\tag{6}
\]

For completeness, (6) follows by writing `S_{2m}=2(B-m)` with `B~Bin(2m,1/2)`, using symmetry, and telescoping

\[
(j-m)\binom{2m}{j}
=m\left[\binom{2m-1}{j-1}-\binom{2m-1}{j}\right].
\]

Putting `m=2k` into (6) and using (5),

\[
a_k:=\int_G d(gH,H)\,d\mu^{*k}(g)
=2k\frac{\binom{4k}{2k}}{2^{4k}}.
\tag{7}
\]

Stirling's formula gives

\[
\frac{\binom{4k}{2k}}{2^{4k}}
\sim\frac1{\sqrt{2\pi k}},
\]

hence

\[
a_k\sim\sqrt{\frac{2k}{\pi}}.
\tag{8}
\]

Finally,

\[
\frac1n\sum_{k=1}^n a_k
\sim
\sqrt{\frac2\pi}\,\frac1n\sum_{k=1}^n\sqrt k
\sim
\frac23\sqrt{\frac2\pi}\,\sqrt n,
\]

which proves (2).

## 5. Why this matters for the source interface

The source says immediately after Problem 3 that one could start with the product/diagonal case

\[
G=G_0\times G_0,
\quad H=\Delta_2G_0,
\quad \mu=\mu_0\otimes\mu_0,
\]

for symmetric `mu_0`. The example above is exactly of that form, with `G_0=Z`, a symmetric aperiodic finite-range `mu_0`, infinite-index diagonal subgroup, and trivial Poisson boundary.

It also clarifies the likely normalization issue. In this example the ordinary single-time drift is zero:

\[
\frac1k\int_G d(gH,H)\,d\mu^{*k}(g)
=\frac{a_k}{k}\to0,
\]

while the printed Cesaro average of the unnormalized distances diverges. Thus a natural drift-normalized variant behaves exactly as the Karlsson--Ledrappier motivation suggests, whereas the literal printed normalization does not.

This does **not** prove which correction the author intended. It only shows that the literal formula is false even in the source's own proposed test class.

## 6. Method accounting

- **#3 PROVE SOMETHING STRONGER.** Strengthen the previous trivial-subgroup refutation to the exact symmetric product/diagonal special case proposed by the source, with divergence rather than a merely positive liminf.
- **#14 FIND THE GROUP ACTING.** The diagonal action collapses `G/H` to the difference coordinate `x-y`, making the quotient walk explicit.
- **#25 COUNT THE SAME THING TWICE.** The quotient difference after `k` product steps is exactly half of a `4k`-step simple symmetric walk, yielding the closed form (7).

These methods are distinct from the preceding E0071 triple #2/#23/#30.

## 7. Prior-art and current-source check

Dated search: 2026-09-18 UTC.

Checked the current arXiv v2 PDF/HTML, exact `Problem 3` wording and the immediately following product/diagonal special case; exact-phrase searches for `d(gH,H)`, quotient-space drift, Poisson-boundary ergodicity, later Björklund work, and citing literature. The current arXiv record remains v2 (2014-07-07) and still prints the same formula. The bounded search did not surface a later primary erratum or explicit resolution of the exact printed Problem 3.

A later citation in the 2025 literature still cites arXiv:1406.0763v2 as the source, but no correction of Problem 3 was recovered in this run. This is bounded negative evidence only. Because the counterexample is elementary and the normalization looks suspicious relative to Theorem 1.3, **publication novelty remains UNVERIFIED and typo/folklore risk is high**.

## 8. Status

Frozen source metric `C_E0071` was already `1` before this run and remains `1`: **NO MOVEMENT**. This artifact strengthens the source refutation but does not create a second source case.

Mathematical label remains **REFUTED AS PRINTED**. Fleet closure still requires two independent end-to-end audits, one from P26 and one from a distinct OTHER track. Repository search in this run found neither audit. No finite computational core is used, so no exact-arithmetic checker or Lean file is applicable.
