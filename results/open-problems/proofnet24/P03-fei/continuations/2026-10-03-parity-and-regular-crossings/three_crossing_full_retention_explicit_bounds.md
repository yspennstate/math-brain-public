# Explicit dyadic bounds for the full-retained-crossing obstruction

Date: 2026-10-02. This is a separate quantitative addendum to the stable
[full proof](three_crossing_full_retention_obstruction.md), which is left
unchanged. For every odd `N>=15`, its perturbed largest-coordinate
entropy ratio obeys the explicit bound

\[
 \boxed{\frac{\Delta_zH(f_N)}{I_z(f_N)}
 \ge\frac{L_N-2^{-N}}{1+2^{-N}},\qquad
 L_N=\frac{N+3}{2}-\log_2\frac{N(N+1)}2.}
\]

Thus no asymptotic-only or unquantified positivity assertion is required.
The script checks the dyadic inequalities using integers.

Retain `epsilon=2^-N`, `M=N+2N^6+1`, and let

\[
 B=\lfloor N^4/72\rfloor,\qquad D=\lfloor N^4/36\rfloor.
\]

Since `e>2`, the probability bound in the full proof gives

\[
 d_N\le2^{1-D},\qquad
 2\sqrt{d_N}\le2^{3/2-D/2}\le\bar t:=2^{2-B}.
\]

The final comparison uses `D>=2B`. For `N>=15`, `N^2>=216`, hence
`B>=3N^2` and `D>=6N^2`. In particular `bar t<1/2`, so entropy
continuity is monotone on the interval `0<=t<=bar t`.

The generic binary-entropy estimate and `log_2 e<2` give

\[
 h_2(\bar t)\le\bar t[\log_2(1/\bar t)+\log_2e]
 \le\bar t B.
\]

We may therefore replace each entropy continuity error by
`omega_bar=bar t(M+B)`. For `N>=2`, `N+1<=N^6/2` and
`B<=N^4/72<=N^6/72`, so `M+B<=3N^6`. Also `log_2 N<=N` gives
`3N^6<=2^(2+6N)`. Thus

\[
 \frac{2\bar\omega}{\epsilon}
 \le2^{N+3-B}(M+B)
 \le2^{7N+5-3N^2}\le2^{-N}=\epsilon.
\]

The last inequality is `3N^2>=8N+5`, valid here. Likewise,

\[
 \frac{2d_N}{\epsilon}\le2^{N+2-D}
 \le2^{N+2-6N^2}\le2^{-N}=\epsilon.
\]

Consequently

\[
 \Delta_zH(f_N)\ge\epsilon L_N-\epsilon^2,
 \qquad I_z(f_N)\le\epsilon+\epsilon^2.
\]

The symmetric pivotal comparison also gives
`I_z(f_N)>=epsilon-2d_N>=epsilon(1-epsilon)>0`.
For `N=15`, `L_15=9-log_2(120)>2`. When odd `N` increases by two,
`L_N` increases: the ratio `(N+2)(N+3)/(N(N+1))` is less than two
for `N>=5`. Thus the numerator above is strictly positive throughout
the claimed range, and division proves the displayed bound.

These estimates are analytic consequences of the already proved
Chernoff and entropy-continuity inequalities. No large-dimensional
truth-table enumeration or numerical tail inference is used.
