# Erratum to 2026-09-19T17-48-00Z report

This is a mathematical notation correction to the immutable report; the theorem and conclusion are unchanged.

In Section 4.2, after equation (4.9), the report says

`log(1+chi2(P_N S_t||Q_N)) <= M_N log 2 - 2 t delta N + o(1) -> -infinity`.

That displayed line is impossible as written because `log(1+chi2)>=0`. The intended and correct consequence of equation (4.5) is

`chi2(P_N S_t||Q_N) <= (2^{M_N}-1) exp(-2 t delta N) <= exp(M_N log 2 - 2 t delta N)`,

or equivalently, whenever `chi2>0`,

`log chi2(P_N S_t||Q_N) <= M_N log 2 - 2 t delta N`.

Since `M_N=ceil((log N)^{1+eta})=o(N)`, the right-hand side tends to `-infinity` for every fixed `t>0`, so

`chi2(P_N S_t||Q_N) -> 0`

and therefore

`TV(P_N S_t,Q_N) <= (1/2) sqrt(chi2(P_N S_t||Q_N)) -> 0`.

No other statement, metric, status, audit count, or conclusion of the run is changed. The original report remains immutable; this artifact is the controlling correction for that one line.