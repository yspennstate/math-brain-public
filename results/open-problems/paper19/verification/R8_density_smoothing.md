# R8 verification: density-rate and smoothing extensions

Date: 2026-06-27.

This round used exactly five read-only audit subagents.

## Square density-rate lower side

Verifier: Mendel.

Verdict: PROVEN lower-side extension.  The proof of the bounded-density
one-matrix tail gives the explicit bound
\[
  \Pr\{\sigma_{\min}(G_m)\le t\}
  \le C_{\mathbb F}K_m m^{d_{\mathbb F}+1}t^{d_{\mathbb F}},
  \qquad 0<t\le1,
\]
when all scalar entry densities are bounded by a deterministic \(K_m\).  Union
over \(\binom{N_m}{m}=\exp((h(\gamma)+o(1))m)\) row sets gives the lower
threshold \((h(\gamma)+\rho)/d_{\mathbb F}\), where
\(\rho=\limsup m^{-1}\log K_m\).  The complex case requires a bounded
two-real-dimensional density on \(\mathbb C\).

## Fixed-excess bounded-density lower side

Verifier: Russell.

Verdict: PROVEN lower-side extension.  For fixed excess \(r\), set
\(p=r+1\).  Conditioning on all but one column and then on all but a good
\(p\)-coordinate minor of an orthonormal projection gives
\[
  \Pr\{\sigma_{\min}(G)\le t\}
  \le C_{\mathbb F,r}K_m^p m^{1+d_{\mathbb F}p}t^{d_{\mathbb F}p}.
\]
The proof must not use the full column density \(K_m^{m+r}\), which would be
exponentially too expensive.  Union over row sets gives the lower threshold
\[
  \frac{h(\gamma)}{d_{\mathbb F}(r+1)}+\frac{\rho}{d_{\mathbb F}}.
\]

## Smoothed deterministic frames

Verifier: Zeno.

Verdict: PROVEN lower-side corollary, not an exact recovery theorem.  For
\(A_m=F_m+\sigma_mG_m\), arbitrary deterministic \(F_m\), and
\(\eta=\limsup m^{-1}\log\sigma_m^{-1}\), shifted Gaussian entries have density
bounded by \(C_{\mathbb F}\sigma_m^{-d_{\mathbb F}}\).  The density-rate theorem
therefore gives
\[
  \liminf \frac1m\log\min_{|T|=m}\sigma_{\min}((A_m)_T)
  \ge -\frac{h(\gamma)}{d_{\mathbb F}}-\eta
\]
in probability.  Subexponential smoothing preserves the Gaussian lower-side
base.  No upper side follows without pair-correlation input.

## Master integration

Verifier: Boole.

Verdict: insert after Lane O's bounded-density lower-side proposition, before
the sign-frame obstruction, because these are lower-side union-bound results.
Add a guard sentence that exact limits still require pair correlation.

## Ledger cleanup

Verifier: Mill.

Verdict: remove stale `NEEDCITE` claims from the R7 ledger entry, correct the
PLAN statement for IV.A from an exact rate to the proved sandwich plus
conjectural exact rate, and add theorem rows for density-rate and smoothed
deterministic lower sides.
