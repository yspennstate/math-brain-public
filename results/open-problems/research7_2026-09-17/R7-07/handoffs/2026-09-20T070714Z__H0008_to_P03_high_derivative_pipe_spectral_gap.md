# C06/H0008 -> P03 reusable lemma: high derivatives isolate the exact-pipe Jacobian

Source line: C06/R7-07 H0008 harmonic exit environment. This is a reusable method handoff only; it does not change P03 ownership, objective, status, or reports.

For a finite-type Palm transfer of the form

\[
(\mathcal T f)_j(b)
=\sum_i M_{ij}E\left[\frac{f_i(F(b+R_i))}{1+b+R_i}\right],
\qquad F(x)=\frac{x}{1+x},
\]

where `R_i=0` is the exact one-child/pipe channel, the highest derivative has an exact coefficient:

\[
\frac{d^k}{dx^k}\left[(1+x)^{-1}f(F(x))\right]
=(1+x)^{-(2k+1)}f^{(k)}(F(x))
+\text{lower derivatives}.
\]

Hence the top-order derivative matrix is

\[
A^{(k)}_{ij}=M_{ij}E[(1+R_i)^{-(2k+1)}].
\]

As `k->infinity`, dominated convergence removes every genuine branch and leaves exactly

\[
A^{(k)}_{ij}\to M_{ij}P(R_i=0)=J_{ij}.
\]

Therefore any independently established pipe Jacobian bound `rho(J)<1` implies that some finite smoothness order `k` has `rho(A^(k))<1`. Combining the resulting top-derivative contraction with the interpolation inequality

\[
\max_{\ell<k}\|f^{(\ell)}\|_\infty
\le \varepsilon\|f^{(k)}\|_\infty+C_{\varepsilon,k}\|f\|_\infty
\]

and a uniformly power-bounded weak `C^0` norm gives a Doeblin--Fortet/quasi-compactness route without requiring a density or one-step Doeblin minorization.

For P03 this may be useful whenever a regeneration/escape transfer has a noncontracting one-child channel plus genuine-branch resets: differentiate the transfer sufficiently many times and test whether the top-order matrix converges to the already-understood pipe/regeneration Jacobian. It is particularly suited to discrete or singular offspring/environment laws where total-variation minorization is unavailable.

C06 application: the reverse harmonic-conductance kernel is a Doob transform of the transfer above; the lemma yields an essential spectral radius `<1`, then a Gordin CLT for harmonic cylinder information. Do not import that objective into P03; only the spectral mechanism is being shared.