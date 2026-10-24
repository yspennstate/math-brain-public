# R9 verification: two-sided and proportional-excess density-rate lower sides

Date: 2026-06-27.

This round used exactly five read-only audit subagents.

## Two-sided density-rate lower side

Verifier: Sartre.

Verdict: PROVEN lower-side extension.  For one selected \(k\times k\) minor with
entry density bound \(K_k\),
\[
  \Pr\{\sigma_{\min}\le t\}
  \le C_{\mathbb F}K_k k^{d_{\mathbb F}+1}t^{d_{\mathbb F}}.
\]
Union over \(\binom{N_k}{k}\binom{n_k}{k}\) minors gives threshold
\((h(\gamma_R)+h(\gamma_C)+\rho)/d_{\mathbb F}\), where
\(\rho=\limsup k^{-1}\log K_k\).  The density contribution is a single \(+\rho\),
not one contribution per side.

## Two-sided smoothed deterministic lower side

Verifier: McClintock.

Verdict: PROVEN lower-side corollary.  For \(A_k=F_k+\sigma_kG_k\), arbitrary
deterministic \(F_k\), shifted Gaussian entries have density bounded by
\(C_{\mathbb F}\sigma_k^{-d_{\mathbb F}}\).  With
\(\eta=\limsup k^{-1}\log\sigma_k^{-1}\), the two-sided threshold is
\[
  \frac{h(\gamma_R)+h(\gamma_C)}{d_{\mathbb F}}+\eta .
\]
No boundedness or conditioning assumption on \(F_k\) is needed for this lower
side.

## Proportional-excess density-rate lower side

Verifier: Heisenberg.

Verdict: PROVEN lower-side extension.  For \(\ell_m/m\to\beta\in(1,\gamma)\),
the coordinate-minor projection proof remains valid with
\(p_m=\ell_m-m+1\asymp m\), provided the high-dimensional ball-volume factor is
kept explicit.  At \(t=e^{-sm}\),
\[
  \Pr\{\sigma_{\min}\le t\}
  \le \exp\{((\beta-1)\rho-d_{\mathbb F}(\beta-1)s+o(1))m^2\}.
\]
The row-set union is only \(\exp(O(m))\), so \(s>\rho/d_{\mathbb F}\) wins.
For \(\rho=0\), this gives \(\liminf m^{-1}\log M_{m,\ell}\ge0\) in probability.
It is not an upper bound or a \(\sqrt m\)-edge theorem.

## Integration

Verifier: Faraday.

Verdict: put all three additions in `parts/geometric.tex`; keep `universality.tex`
as the square-template section.  In Lane O, use compact corollaries after the
proportional-excess paragraph and after the two-sided Gaussian theorem.  Add
guard wording that exact two-sided bases remain conditional on pair correlation.

## Ledger

Verifier: Planck.

Verdict: add rows for proportional-excess density-rate, two-sided density-rate,
and smoothed geometric lower sides.  Remove the unsupported implication that a
3-agent panel is an active round; future active rounds must use exactly five
subagents.
