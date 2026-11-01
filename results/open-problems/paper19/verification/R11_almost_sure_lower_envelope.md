# R11 verification: almost-sure lower envelopes

Date: 2026-06-27.

Round discipline: exactly 5 read-only audit agents were launched.

## Agent reports

1. Feynman audited the abstract Borel--Cantelli upgrade. Verdict: valid when
   the small-ball `o(1)` is uniform after taking the supremum over the index
   family. The union bound gives an exponentially summable bad-event
   probability at every fixed epsilon slack. No independence across dimensions
   is required.

2. Noether audited density-rate and smoothing applications. Verdict: valid.
   The limsup density-rate constant causes no threshold loss because the
   epsilon slack absorbs the eventual limsup slack. For smoothing, the safest
   proof is the scaling identity
   `F + sigma G = sigma (sigma^{-1}F + G)`, which avoids any issue when
   `sigma` is exponentially large.

3. Harvey audited geometric applications. Verdict: valid for proved lower-side
   results. Fixed-excess and two-sided failures are exponentially summable;
   proportional-excess failures are superexponentially summable on the
   exponential `m` scale. The `k`-th singular-value version remains conditional
   because its uniform one-matrix tail is not proved in the manuscript.

4. Erdos audited phase-retrieval implications. Verdict: safe strengthening is
   only an almost-sure lower envelope. Do not claim an exact a.s. Balan--Wang
   base or `omega=4^{-m+o_as(m)}`. The bounded-density critical real lower side
   and row-normalized Gaussian critical lower envelope are valid on any common
   coupling.

5. Newton audited manuscript placement. Verdict: add the core result after the
   polynomial small-ball corollary, then add application corollaries in the
   universality, geometric, and phase-retrieval sections. Mirror Lane O as a
   short unnumbered paragraph to avoid unnecessary master theorem-number churn.

## Integrated result

The manuscript now contains:

- `cor:as-lower-envelope`: a summable lower-envelope criterion using first
  Borel--Cantelli.
- `cor:as-square-lower-envelope`: almost-sure lower envelopes for
  bounded-density, density-rate, and smoothed square row-submatrix lower sides.
- `cor:as-geometric-lower-envelopes`: almost-sure lower envelopes for
  fixed-excess, proportional-excess, and two-sided lower sides.
- `cor:pr-as-lower-envelope`: critical real Balan--Wang lower envelopes,
  including row-normalized Gaussian critical frames.
- `laneO:par:as-lower-envelope`: compact master-chapter mirror.

No matching almost-sure exact base is claimed.

