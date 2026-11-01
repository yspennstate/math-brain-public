# Round 118 log

## Goal

Extract an explicit radius-scale consequence from the Round 117 annular volume
obstruction.

## Result

Added `cor:logarithmic-radius-obstruction`.

If far-leg tightness fails and \(G\) has maximum degree at most
\(\Delta\ge2\), then the escaping annulus from the penalized volume obstruction
can be chosen so that
\[
  2^j\ge \frac14\log_\Delta\bar\chi_p.
\]
It still satisfies
\[
  V((2^j,2^{j+1}])
  \gtrsim_{\epsilon,\eta}
  2^{-2\eta(j-J)}\bar\chi_p.
\]

## Interpretation

The obstruction has to live beyond the logarithmic susceptibility scale.  This
does not contradict exponential volume growth, but it gives the next
correlation-length target: rule out two-replica backscattering from finite
sets to annuli at distances at least \(c\log\bar\chi_p\).
