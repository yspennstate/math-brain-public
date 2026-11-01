# Round 117 log

## Goal

Translate the single-annulus incidence obstruction into a volume-growth
necessary condition.

## Result

Added `cor:escaping-annulus-volume` and
`cor:subexponential-volume-obstruction`.

If far-leg tightness fails, then for every fixed window and all sufficiently
near-critical \(p_0\), there are \(p\in[p_0,p_c)\) and an escaping dyadic
annulus \(I_j=(2^j,2^{j+1}]\) such that
\[
  V(I_j)
  \ge
  \frac{\epsilon^2}{16}
  (1-2^{-\alpha})^2(1-2^{-\gamma})^2
  2^{-2(\alpha+\gamma)(j-J)}\bar\chi_p.
\]

Equivalently, for every \(\eta>0\),
\[
  V((2^j,2^{j+1}])
  \gtrsim_{\epsilon,\eta}
  2^{-2\eta(j-J)}\bar\chi_p
\]
along some escaping annulus.

## Interpretation

The remaining obstruction must live at scales whose annular volume is large
enough to accommodate the near-critical susceptibility, up to an arbitrarily
small prescribed exponential penalty in the dyadic index.
