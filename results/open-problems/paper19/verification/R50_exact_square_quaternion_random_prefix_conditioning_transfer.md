# R50 verification - exact square quaternion random-prefix conditioning transfer

## Scope

Round R50 added `cor:quat-random-prefix-conditioning-exact`.  For an infinite
iid standard quaternion Gaussian row array \((R_{im})_{i\ge1}\) in \(\HH^m\),
an integer prefix count \(N_m/m\to\gamma>1\) in probability, positive real row
weights over the realized prefix, and one global all-column invertible
quaternion right factor \(S_m\), define
\[
  B_{m,T}=\operatorname{diag}(d_{im}:i\in T)(R_{im})_{i\in T}S_m,
  \qquad T\subset[N_m],\ |T|=m .
\]
If
\[
  \max_{i\le N_m}|\log d_{im}|
  +|\log\smin(S_m)|+|\log\|S_m\||=o_P(m),
\]
then
\[
  m^{-1}\log\min_{T\subset[N_m], |T|=m}\smin(B_{m,T})
  \to -h(\gamma)/4
\]
in probability, with the same fixed positive convention on \(\{N_m<m\}\) as in
R49.  The normalized square Gram statistic has base \(-h(\gamma)/2\).  A.s.
count convergence plus a.s. `o(m)` conditioning extrema transfer only lower
envelopes.

This is a square random-prefix and global all-column right-factor statement.
It is not a condition-number-only covariance theorem, value-dependent row
selection theorem, selected-column covariance transfer, fixed-excess exact law,
Balan-Wang or supercritical phase-retrieval result, quaternion spherical-radial
universality theorem, or a.s. exact law.

## Agent audit

Exactly five read-only audit agents were launched, and all five completed:

- Euler the 2nd: `019f0e75-82f7-72b3-ad42-869f53ea7c84`
- Laplace the 2nd: `019f0e75-8356-7792-b1b4-cade72435de3`
- Ptolemy the 2nd: `019f0e75-83a0-7c11-bbcb-098bb4997038`
- Herschel the 2nd: `019f0e75-83e5-7bf1-8486-c22294921baf`
- Dalton the 2nd: `019f0e75-8425-7532-9e19-93eae6ad0d2d`

Consensus:

- PASS for the direct pathwise transfer from
  `thm:quat-random-row-count-gaussian`.
- The row-weight maximum must be over the realized prefix, \(\max_{i\le N_m}\).
- No independence is needed between the count, rows, weights, and right factor,
  because the comparison is pathwise.
- The right-factor hypothesis must control absolute scale:
  \(|\log\smin(S_m)|+|\log\|S_m\||=o_P(m)\).  Condition number alone is
  insufficient.
- Positive real column diagonals are included as a special case of the global
  right factor; selected-column non-diagonal covariance is not included.
- Row-normalized random-prefix matrices and full-prefix column normalization
  have the needed subexponential norm extrema by deterministic prefix brackets.
- Independent thinning is covered only after distributional reindexing of the
  retained iid rows and only under the same conditioning-extrema hypothesis.
- A.s. hypotheses transfer only lower envelopes, not a.s. exact laws.

## Pathwise check

On the event \(N_m\ge m\), for every \(T\subset[N_m]\), \(|T|=m\),
\[
  e^{-\Delta_m^{\rm rpref}}\smin((R_{im})_{i\in T})
  \le
  \smin(B_{m,T})
  \le
  e^{\Delta_m^{\rm rpref}}\smin((R_{im})_{i\in T}).
\]
The constants are uniform over all selected square row sets.  Taking minima,
logs, and dividing by \(m\) gives an `o_P(1)` difference from the R49 statistic
\(M_m^\HH(N_m)\).  R49 supplies the exact random-prefix base.  The Gram claim
is the pathwise identity
\[
  \lambda_{\min}(m^{-1}B_{m,T}^*B_{m,T})=m^{-1}\smin(B_{m,T})^2.
\]

For row normalization, the realized-prefix row-norm extrema are bounded on
\(\{N_m\le\lceil\gamma_+m\rceil\}\) by deterministic-prefix extrema.  For
column normalization, the full-prefix column norms are bracketed on
\(\{\lfloor\gamma_-m\rfloor\le N_m\le\lceil\gamma_+m\rceil\}\).  The same
quaternion \(\chi^2\) norm tails used in R47 give `o_P(m)` extrema and a.s.
`o(m)` extrema on common couplings with eventual deterministic brackets.

## Files changed

- `parts/ensembles.tex`: added
  `cor:quat-random-prefix-conditioning-exact`.
- `STATE.md`: added row `V.A-square-rc-cond` and the R50 round log.
- `PLAN.md`: recorded the random-prefix conditioning transfer in V.A.
- `math-open-problems-fleet/master/chO_phase_retrieval_rmt.tex`: added the Lane
  O compact random-prefix conditioning paragraph.
- `math-open-problems-fleet/MASTER_STATE.md`: recorded the master-side summary.

## Build verification

- Standalone: `pdflatex -interaction=nonstopmode -halt-on-error extremal_hard_edge.tex`
  completed cleanly after the reference-settling pass; output
  `extremal_hard_edge.pdf` has 67 pages and 904,372 bytes.
- Master: `pdflatex -interaction=nonstopmode -halt-on-error master.tex`
  completed cleanly after the reference-settling pass; output `master.pdf` has
  858 pages and 7,789,837 bytes.
- Targeted scans of `extremal_hard_edge.log` and `master.log` found no
  undefined citations/references, multiply-defined labels, or rerun requests.
- The refreshed `master.pdf` was copied to
  `~/Downloads/master.pdf` with matching size 7,789,837 bytes.
