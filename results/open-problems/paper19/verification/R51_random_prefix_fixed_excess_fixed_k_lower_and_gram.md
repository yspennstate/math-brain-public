# R51 verification - random-prefix fixed-excess fixed-k lower sides

## Scope

Round R51 added `cor:random-prefix-fixed-excess-fixed-k-lower`.  For
\(\F\in\{\R,\C,\HH\}\), \(d_\F\in\{1,2,4\}\), an infinite iid standard
Gaussian row array \((R_{im})_{i\ge1}\) over \(\F^m\), fixed \(r\ge0\) and
fixed \(k\ge1\), define for deterministic \(n\ge m+r\)
\[
  M_{\F,m}^{(r)}[k](n)=
  \min_{\substack{T\subset[n]\\ |T|=m+r}}
  \sigma_{m-k+1}((R_{im})_{i\in T}).
\]
If an integer prefix count \(N_m/m\to\gamma>1\) in probability, possibly
dependent on the row array, then for every \(\varepsilon>0\),
\[
  \PP\{M_{\F,m}^{(r)}[k](N_m)
  \le \exp[-(h(\gamma)/(d_\F k(k+r))+\varepsilon)m]\}\to0,
\]
with the \(+\infty\) convention on \(\{N_m<m+r\}\).  The normalized
column-Gram statistic with \((m+r)^{-1}A_T^*A_T\) has lower base
\(2h(\gamma)/(d_\F k(k+r))\).  If \(N_m/m\to\gamma\) almost surely on a common
coupling, the corresponding lower envelopes hold.

This is only a lower-side random-prefix transfer of the deterministic-count
fixed-excess fixed-\(k\) lower sides.  It is weaker than the exact square
random-prefix laws when \(r=0,k=1\).  It is not an upper side, exact
fixed-excess law, a.s. exact law, value-dependent row-selection theorem,
row-Gram statement for \(r>0\), beta interpolation, proportional Wishart-edge
law, Balan-Wang or supercritical phase-retrieval statement, or conditioning
transfer.

## Agent audit

Exactly five read-only audit agents were launched, and all five completed:

- Euclid the 2nd: `019f0e7f-b6d8-75d0-8311-23be98ca7e5d`
- Darwin the 2nd: `019f0e7f-b729-73f0-af7e-960f5b5508af`
- Hubble the 2nd: `019f0e7f-b77f-7ed0-b3ed-c9d4e9b026de`
- Maxwell the 2nd: `019f0e7f-b7e0-7482-9bb8-962aa186751b`
- Copernicus the 2nd: `019f0e7f-b833-7e40-b6c8-04aabee0b26e`

Consensus:

- PASS for the random-prefix lower-side transfer over \(\R,\C,\HH\).
- Only the upper deterministic bracket is needed: for any \(\gamma_+>\gamma\),
  \(N_m\le\lceil\gamma_+m\rceil\) with probability tending to one.
- The prefix-count dependence on the row array is harmless because the proof is
  pathwise.
- No summability of count deviations is needed for convergence in probability;
  a.s. count convergence gives eventual upper brackets for the lower envelope.
- The normalized column-Gram statistic keeps normalization \((m+r)^{-1}\), not
  \(N_m^{-1}\).
- The result is lower-side only and does not upgrade fixed-excess laws to exact
  convergence.

## Pathwise check

For deterministic \(n\), \(M_{\F,m}^{(r)}[k](n)\) is nonincreasing in \(n\),
because adding prefix rows enlarges the tested family.  On
\(\{N_m\le\lceil\gamma_+m\rceil\}\),
\[
  M_{\F,m}^{(r)}[k](N_m)
  \ge M_{\F,m}^{(r)}[k](\lceil\gamma_+m\rceil).
\]
The deterministic-count lower sides at aspect \(\gamma_+\) are
`rect-kth:fixed-aspect-lower` for \(\R,\C\) and
`thm:quat-fixed-excess-fixed-k-lower` for \(\HH\).  Letting
\(\gamma_+\downarrow\gamma\) gives the stated lower base.

For Gram variables,
\[
  \lambda_{(k)}((m+r)^{-1}A_T^*A_T)=(m+r)^{-1}\sigma_{m-k+1}(A_T)^2,
\]
so the lower exponent doubles and \(m^{-1}\log(m+r)\to0\).

## Files changed

- `parts/ensembles.tex`: added
  `cor:random-prefix-fixed-excess-fixed-k-lower`.
- `STATE.md`: added row `V.A-rect-kth-rc` and the R51 round log.
- `PLAN.md`: recorded random-prefix fixed-excess fixed-`k` lower sides in V.A.
- `math-open-problems-fleet/master/chO_phase_retrieval_rmt.tex`: added the Lane
  O compact random-prefix fixed-excess paragraph.
- `math-open-problems-fleet/MASTER_STATE.md`: recorded the master-side summary.

## Supplemental proof-tightening audit

After resuming, exactly five additional read-only audit agents checked the
already-integrated corollary and its proof wording:

- Curie (`019f0e85-aca5-7c82-9b9c-ba70d4600894`) passed the result and flagged
  that the `N_m<m+r` convention should be \(+\infty\) or split off explicitly.
- Newton (`019f0e85-ad74-7eb1-a19c-12af4b81aca1`) passed monotonicity,
  random-prefix dependence, and the normalized column-Gram pathwise identity.
- Copernicus (`019f0e85-ae3e-7392-aa43-7c41ffea8585`) confirmed the result is
  lower-side only and should not upgrade the square exact random-count theorem.
- Kepler (`019f0e85-af10-7ba1-ad57-74f122a501f7`) confirmed the safe scope and
  warned not to fold in unproved bounded-density fixed-\(k\) tails.
- Boyle (`019f0e85-afd7-7140-9b5d-719a0da36a59`) requested an explicit
  \(\varepsilon\)-split: choose \(\gamma_+>\gamma\) with
  \(h(\gamma_+)/(d_\F k(k+r))<h(\gamma)/(d_\F k(k+r))+\varepsilon/2\).

The manuscript proof now uses the \(+\infty\) convention on \(\{N_m<m+r\}\)
and includes the explicit \(\gamma_+\) slack choice.

## Build verification

- Standalone: `pdflatex -interaction=nonstopmode -halt-on-error extremal_hard_edge.tex`
  completed cleanly after the reference-settling pass; output
  `extremal_hard_edge.pdf` has 68 pages and 910,837 bytes.
- Master: `pdflatex -interaction=nonstopmode -halt-on-error master.tex`
  completed cleanly after the reference-settling pass; output `master.pdf` has
  859 pages and 7,792,903 bytes.
- Targeted scans of `extremal_hard_edge.log` and `master.log` found no
  undefined citations/references, multiply-defined labels, or rerun requests.
- The refreshed `master.pdf` was copied to
  `~/Downloads/master.pdf` with matching size 7,792,903 bytes.
