# R49 verification - exact square quaternion random row-count transfer

## Scope

Round R49 added `thm:quat-random-row-count-gaussian` and
`cor:quat-poisson-thinning`.  For an infinite iid standard quaternion Gaussian
row array \((R_{im})_{i\ge1}\) in \(\HH^m\), define
\[
  M_m^{\HH}(n)=\min_{\substack{T\subset[n]\\ |T|=m}}\smin((R_{im})_{i\in T}).
\]
If an integer prefix count \(N_m\), possibly dependent on the row array,
satisfies \(N_m/m\to\gamma>1\) in probability, then
\[
  m^{-1}\log M_m^{\HH}(N_m)\to -h(\gamma)/4
\]
in probability, with any fixed positive convention on \(\{N_m<m\}\).  The
normalized square Gram statistic has base \(-h(\gamma)/2\).  If \(N_m/m\to
\gamma\) almost surely on a common coupling, only the lower envelopes transfer
almost surely.

## Agent audit

Exactly five read-only audit agents were launched, and all five completed:

- Zeno the 2nd: `019f0e6c-5c64-7da0-a4c0-81976fe95642`
- Sartre the 2nd: `019f0e6c-5ca9-7ac0-aa2f-e19b59e6688f`
- Aquinas the 2nd: `019f0e6c-5d08-7573-8827-b287d0f60520`
- Raman the 2nd: `019f0e6c-5d58-7462-9cae-77eba8b33c5d`
- Lovelace the 2nd: `019f0e6c-5db4-7a13-8a14-0f9ae4cce6e7`

Consensus:

- PASS for prefix counts by the pathwise monotone squeeze.
- Dependence of \(N_m\) on the row array is harmless for prefix counts because
  the proof is pathwise.
- Use \(1<\gamma_-<\gamma<\gamma_+\), with floors and ceilings; do not write an
  informal \(\gamma-\varepsilon\) unless it stays above \(1\).
- \(N_m<m\) has probability tending to zero, so a fixed positive convention is
  harmless.
- Independent Poisson and binomial counts are safe.  Independent Bernoulli
  thinning is safe only as a distributional reindexing statement: conditional
  on the retained count, the retained rows are iid quaternion Gaussian and row
  order is irrelevant.
- Value-dependent thinning or row selection is not covered.
- No Balan--Wang, fixed-excess exact, supercritical phase-retrieval, quaternion
  spherical-radial universality, or a.s. exact law is implied.

## Pathwise check

For deterministic \(n\), \(M_m^{\HH}(n)\) is nonincreasing in \(n\).  On the
high-probability event
\[
  \lfloor\gamma_-m\rfloor\le N_m\le\lceil\gamma_+m\rceil
\]
one has
\[
  M_m^{\HH}(\lceil\gamma_+m\rceil)
  \le M_m^{\HH}(N_m)
  \le M_m^{\HH}(\lfloor\gamma_-m\rfloor).
\]
The source theorem `thm:quaternion-gaussian-base` gives deterministic-count
limits \(-h(\gamma_+)/4\) and \(-h(\gamma_-)/4\).  Continuity of \(h\) and
\(\gamma_\pm\to\gamma\) squeeze the random-count limit to \(-h(\gamma)/4\).

For the a.s. lower envelope, if \(N_m/m\to\gamma\) a.s. then for every
\(\gamma_+>\gamma\), eventually \(N_m\le\lceil\gamma_+m\rceil\).  The summable
lower-side estimate in the proof of `thm:quaternion-gaussian-base` gives the
deterministic-row-count lower envelope at \(\gamma_+\), then
\(\gamma_+\downarrow\gamma\).  The Gram statement follows from `cor:gram-transfer`.

## Files changed

- `parts/ensembles.tex`: added `thm:quat-random-row-count-gaussian` and
  `cor:quat-poisson-thinning`.
- `STATE.md`: added row `V.A-square-rc` and the R49 round log.
- `PLAN.md`: recorded quaternion square random prefix row counts in V.A.
- `math-open-problems-fleet/master/chO_phase_retrieval_rmt.tex`: added the Lane
  O compact quaternion random row-count paragraph.
- `math-open-problems-fleet/MASTER_STATE.md`: recorded the master-side summary.

## Build verification

- Standalone: `pdflatex -interaction=nonstopmode -halt-on-error extremal_hard_edge.tex`
  completed cleanly after the reference-settling pass; output
  `extremal_hard_edge.pdf` has 66 pages and 897,449 bytes.
- Master: `pdflatex -interaction=nonstopmode -halt-on-error master.tex`
  completed cleanly after the reference-settling pass; output `master.pdf` has
  858 pages and 7,788,977 bytes.
- Targeted scans of `extremal_hard_edge.log` and `master.log` found no
  undefined citations/references, multiply-defined labels, or rerun requests.
- The refreshed `master.pdf` was copied to
  `~/Downloads/master.pdf` with matching size 7,788,977 bytes.
