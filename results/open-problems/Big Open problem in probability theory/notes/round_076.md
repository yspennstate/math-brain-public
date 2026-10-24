# Round 076 log

## Goal

Close the remaining two-layer finite cyclic product \(T_3\square K_2\).

## Branching side

Use the oriented tree-fiber exploration, but retain the reached subset of the
two-point fiber.  The non-empty subset types are singleton and doubleton.  At
\[
  p=\frac{39}{100},
\]
the two-forward-child mean matrix is
\[
  M=
  \begin{pmatrix}
    2379/5000 & 1521/5000\\
    145119/250000 & 168831/250000
  \end{pmatrix}.
\]
With \(v=(1,7/4)^T\),
\[
  Mv=(20163/20000,\ 1762293/1000000)^T>v.
\]
Therefore \(p_c(T_3\square K_2)<39/100\).

## Operator side

Added `scripts/k2_saw_certificate.py`.  It quotient-enumerates length-15
self-avoiding walks on \(T_3\square K_2\) and verifies
\[
  \|C_{15}\|_{2\to2}
  \le
  639862+452048\sqrt2
  <(100/39)^{15}.
\]
The endpoint coefficients for tree radii \(0,\ldots,15\) are
\[
  192,448,592,984,1411,1750,1981,2008,
  1837,1498,1073,649,301,91,15,1.
\]
Thus \(\gamma_{\mathrm{SAW},2}(T_3\square K_2)<100/39\).

## Result

Combining the two inequalities gives
\[
  p_c(T_3\square K_2)<p_{2\to2}(T_3\square K_2).
\]
Together with Round 075, this proves
\[
  p_c(T_d\square K_2)<p_{2\to2}(T_d\square K_2)
  \qquad d\ge3.
\]
