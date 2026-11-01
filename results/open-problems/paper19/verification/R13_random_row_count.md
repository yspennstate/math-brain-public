# R13 verification - random row counts and Poissonization

## Scope

Round R13 adds:

- Gaussian random row-count transfer by monotonicity;
- bounded-density/density-rate lower-side transfer for random row counts;
- almost-sure lower-envelope transfer under almost-sure count convergence;
- Poisson, binomial, and independent Bernoulli-thinning examples;
- a phase-retrieval warning for noncritical measurement counts.

## Five-agent audit

Exactly five read-only agents were launched and then closed.

1. `019f0a2b-9055-7cb0-ba4f-16e7de44555d` checked the Gaussian monotone squeeze.
2. `019f0a2b-a457-7243-bdc0-8224861da49d` checked the bounded-density/density-rate lower side and a.s. envelope.
3. `019f0a2b-ba8d-7ca0-8058-2691e47c23d9` checked Poissonization and independent thinning.
4. `019f0a2b-d008-7353-93f8-bee93acb6193` checked phase-retrieval implications.
5. `019f0a2b-f8cd-7762-b3f5-96f3dc4c7d56` checked integration placement and notation.

## Audit conclusions

For deterministic row count \(n\), the extremal statistic
\[
  M_m(n)=\min_{T\subset[n],\, |T|=m}\sigma_{\min}(A_T)
\]
is nonincreasing in \(n\).  Therefore, on
\[
  \lfloor\gamma_-m\rfloor\le N_m\le \lceil\gamma_+m\rceil,
\]
one has
\[
  M_m(\lceil\gamma_+m\rceil)\le M_m(N_m)\le M_m(\lfloor\gamma_-m\rfloor).
\]
This is pathwise, so dependence of a random prefix count \(N_m\) on the row
array is harmless.  The convention on \(\{N_m<m\}\) is harmless because
\(N_m/m\to\gamma>1\) implies that event has probability tending to zero.

For bounded-density and density-rate lower sides, only the upper bracket is
needed:
\[
  N_m\le \lceil\gamma_+m\rceil \quad\Rightarrow\quad
  M_m(N_m)\ge M_m(\lceil\gamma_+m\rceil).
\]
Letting \(\gamma_+\downarrow\gamma\) gives the lower threshold
\((h(\gamma)+\rho)/d_\F\).  The almost-sure version uses eventual upper
brackets for rational \(\gamma_+>\gamma\) plus the deterministic Borel-Cantelli
lower envelope.

For thinning, independence of retention indicators from the row values is
essential.  Value-dependent retention can bias the retained row law and is not
covered.

For phase retrieval, no random-row-count Balan--Wang corollary is claimed.
Away from the exact real critical count \(N=2m-1\), the fixed-excess
tall-submatrix statistic
\[
  \min_{|T|=m+r}\sigma_{\min}(A_T),\qquad N=2m-1+r.
\]
is only the branch where the complementary side has at most \(m-1\) rows and
therefore fails to span.  For \(r>0\), partitions whose two sides both span can
also enter the Balan--Wang minimum, so the fixed-excess statistic is not an
exact reduction of the full supercritical Balan--Wang statistic.

## Build verification

After integration:

- `paper19/extremal_hard_edge.pdf`: 29 pages, 525055 bytes.
- `master/master.pdf`: 852 pages, 7752355 bytes.
- `master/master.pdf` was copied to `~/Downloads/master.pdf`.

Targeted log scans found no undefined references or citations, no rerun request,
and no LaTeX error/fatal/emergency stop.  Remaining diagnostics are the existing
`\theHfootnote` warning and legacy box/hyperref warnings.
