# R44 verification - normalized Gaussian fixed-excess fixed-k lower sides

## Scope

Round R44 promoted the random diagonal fixed-\(k\) transfer into the normalized
Gaussian cases.  The new result is
`cor:normalized-gaussian-fixed-excess-fixed-k`: for iid real or complex Gaussian
matrices with \(N_m/m\to\gamma>1\), both row-normalized and
column-normalized matrices inherit the fixed-excess fixed-\(k\) singular-value
lower side
\[
  -\frac{h(\gamma)}{d_\F k(k+r)}
\]
and the normalized column-Gram lower side
\[
  -\frac{2h(\gamma)}{d_\F k(k+r)} .
\]
It also records the corresponding almost-sure lower envelopes on common
couplings.

This is lower-side bookkeeping only.  It does not add an upper side, an exact
law, a quaternion statement, a row-Gram theorem for \(r>0\), or a non-diagonal
covariance transfer.

## Agent audit

Exactly five read-only audit agents were launched for this round, and all five
completed:

- Avicenna: `019f0e3b-7c44-7ab3-884f-efcde804a352`
- Turing: `019f0e3b-9289-7f60-8baf-0754299a6ec9`
- Leibniz: `019f0e3b-a8e9-7c73-ba97-acf9b341630d`
- Planck: `019f0e3b-c61b-7ee0-a3e9-b0751d890c89`
- Carson: `019f0e3b-db2a-7501-9f6d-f8b15fb3920e`

Common findings:

- Safe claim: real/complex normalized Gaussian fixed-\((r,k)\) lower sides and
  lower envelopes.
- Unsafe claims rejected: exact law, upper side, quaternion extension,
  non-diagonal covariance, and row-Gram extension for \(r>0\).
- The proof must be phrased as a diagonal-weight transfer from \(G_m\), not as
  a new independent-Gaussian distributional identity after normalization.

## Mathematical checks

For row normalization, \(U_m=D_m^{\rm row}G_m\) with positive diagonal entries.
For column normalization, \(V_m=G_mE_m\) with positive diagonal entries.  Gaussian
\((m+r)\)-row submatrices have rank \(m\) almost surely, so the fixed-\(k\)
min--max comparisons in `rem:random-diagonal-fixed-k` apply off a null event.

The needed diagonal logarithmic extrema are \(o_P(m)\) from the existing
Gaussian norm estimates.  On common couplings they are \(o(m)\) almost surely:
upper row and column norm tails are summable, lower column norm tails are
summable, and the row lower-tail ball-volume bound remains summable after the
union over \(N_m=O(m)\) rows.

Applying `rem:random-diagonal-fixed-k` with \(A_m=G_m\), and using
`rect-kth:fixed-aspect-lower`, `rect-kth:gram-lower`, and
`cor:as-geometric-lower-envelopes`, gives the stated lower sides and a.s. lower
envelopes.

## Files changed

- `parts/ensembles.tex`: added
  `cor:normalized-gaussian-fixed-excess-fixed-k`.
- `STATE.md`: marked the normalized row/column Gaussian transfer rows as
  carrying the fixed-excess fixed-\(k\) lower sides.
- `PLAN.md`: recorded the row/column-normalized Gaussian consequence under
  V.B.
- `math-open-problems-fleet/master/chO_phase_retrieval_rmt.tex`: added the
  Lane O discoverability sentence in `laneO:cor:conditioning-variants`.
- `math-open-problems-fleet/MASTER_STATE.md`: recorded the master-side summary.

## Build verification

`pdflatex -interaction=nonstopmode -halt-on-error extremal_hard_edge.tex` passed
twice.  The final standalone PDF is 61 pages / 863,410 bytes.

`pdflatex -interaction=nonstopmode -halt-on-error master.tex` passed twice in
the fleet master.  The final master PDF is 856 pages / 7,776,655 bytes.

Targeted log scans for undefined references, undefined citations,
multiply-defined labels, and rerun requests return only the final `Output
written` lines.
