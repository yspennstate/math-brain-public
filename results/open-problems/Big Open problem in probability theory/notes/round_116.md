# Round 116 log

## Goal

Extract a concrete annular scale from the escaping-tail obstruction.

## Result

Added `prop:single-remote-annulus-obstruction` and
`cor:single-annulus-root-incidence`.

Failure of far-leg tightness implies that for every \(\alpha,\gamma>0\), every
tail start \(J\), and every fixed window length \(H\), sufficiently near
\(p_c\) there are \(p\), macroscopic \(K\), and \(j>J+H\) such that
\[
  \mathcal R_p^{(2^j,2^{j+1}]}(K)/\bar\chi_p
  \ge
  \frac{\epsilon}{2}(1-2^{-\alpha})(1-2^{-\gamma})
  2^{-(\alpha+\gamma)(j-J)}.
\]

The same annulus has root and deterministic incidence layers of comparable
relative size.

## Interpretation

The obstruction no longer has to be tracked as an infinite weighted tail.  It
can be localized to one dyadic annulus, although that annulus must escape past
every fixed window near criticality.
