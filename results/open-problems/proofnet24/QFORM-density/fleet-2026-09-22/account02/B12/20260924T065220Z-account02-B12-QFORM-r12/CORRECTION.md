# Correction to Section 4 of REPORT.md

The contrapositive normal form in Section 4 needs the fifth-skew-mode clause only when the near-antipodal spectral subspace has dimension at least five.

Precisely, if `s_5(I+K)<eta`, then

`dim U_+ <=4`, `dim U_- <=4`, and hence `dim U_0 >= m-8`.

In addition, **if `dim U_0>=5`**, then

`s_5(P_0 Skew(K) P_0|_(U_0)) < 2 eta`.

For `m>=13`, the dimension count automatically gives `dim U_0>=5`, so all four displayed conclusions in the original `(4.3)` hold. For `5<=m<=12`, the low-dimensional case `dim U_0<5` should be kept as a separate bounded-dimensional alternative rather than assigning an undefined fifth singular value to that compression.

The proof of Theorem 4.1 itself, the antipodal-skew rescue theorem, dense-tail compiler, stress family, pinned D5 application, and all numerical constants are unchanged.
