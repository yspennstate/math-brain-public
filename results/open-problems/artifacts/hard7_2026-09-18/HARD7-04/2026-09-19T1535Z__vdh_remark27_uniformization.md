# HARD7-04 addendum — uniform weighted form of van der Hofstad–Janson–Luczak Remark 2.7

**Status:** corollary/prior-art reconciliation for the quantitative histogram theorem; PARTIAL only.

A fresh read of the 2019 primary paper found an important piece of prior art that must be stated explicitly rather than hidden behind the phrase “classical extinction tilt.”  Van der Hofstad–Janson–Luczak, *Component structure of the configuration model: Barely supercritical case*, Random Structures & Algorithms 55 (2019), Remark 2.7, already states a **fixed-degree** asymptotic for the number `v_k(C_1)` of degree-`k` vertices in the giant.  In the finite-third-moment regime this has the first-order form

\[
v_k(C_1)=k\rho_n n_k(1+o_p(1))
\]

for every fixed `k` (equivalently their displayed size-biased formulation).  Therefore the extinction-tilt profile itself is absolutely not a new discovery of HARD7-04.

The theorem in `2026-09-19T1530Z__vdh_quantitative_histogram_duality.md` adds a different quantitative statement: one weighted `ell^1` estimate simultaneously over **all** degree classes in the triangular array, at the shrinking natural scale `n epsilon_n`, and the resulting `o_p(epsilon_n)` total-variation law outside the giant.

The relationship can be made exact.

Let

\[
\rho_n:=1-\xi_n.
\]

The already proved branching-process expansion gives `rho_n=O(epsilon_n)`.  For every integer `d>=0` and `0<=rho<=1`, concavity/Taylor's theorem gives

\[
0\le d\rho-\bigl(1-(1-\rho)^d\bigr)
\le \frac{d(d-1)}2\rho^2.
\tag{A.1}
\]

Indeed `f(rho)=1-(1-rho)^d` has `f(0)=0`, `f'(0)=d`, and `|f''(rho)|<=d(d-1)`.

Multiply (A.1) by `(1+d)n_d` and sum.  Since

\[
(1+d)d(d-1)=d^3-d\le d^3,
\]

the source third-moment assumption yields

\[
\sum_d(1+d)n_d
\left|1-\xi_n^d-d\rho_n\right|
\le \frac{\rho_n^2}{2}\sum_dd^3n_d
=O(n\varepsilon_n^2)
=o(n\varepsilon_n).
\tag{A.2}
\]

The histogram theorem gives

\[
\sum_d(1+d)
\left|N_{n,d}^{G}-n_d(1-\xi_n^d)\right|
=o_p(n\varepsilon_n).
\tag{A.3}
\]

Combining (A.2) and (A.3) therefore gives the simultaneous weighted upgrade

\[
\boxed{
\sum_{d\ge0}(1+d)
\left|N_{n,d}^{G}-d\rho_n n_d\right|
=o_p(n\varepsilon_n).
}
\tag{A.4}
\]

This is the clean bridge to 2019 Remark 2.7: for each fixed `d` it is consistent with their formula, while (A.4) controls the whole degree vector at once and makes the tail uniform.

Two normalization consequences are immediate.  Since

\[
\rho_n\sum_ddn_d=\Theta(n\varepsilon_n),
\]

(A.4) implies the empirical **vertex-degree law inside the giant** converges in total variation to the original size-biased degree law

\[
q_{n,d}:=\frac{dn_d}{\sum_jjn_j}.
\tag{A.5}
\]

Similarly, using the `d`-weighted part of (A.4), the empirical degree law seen from a uniformly chosen half-edge of the giant converges in total variation to the twice-size-biased law proportional to `d^2n_d` (under the present finite-third-moment assumptions).

These are not presented as novel source solutions: the fixed-`d` composition mechanism is explicit prior art in 2019.  Their value here is to show that the new outside-giant histogram theorem is a genuine **uniformization** of a known fixed-degree result rather than an accidental contradiction or rediscovery.

No finite exhaustive claim is made, so no checker is required.