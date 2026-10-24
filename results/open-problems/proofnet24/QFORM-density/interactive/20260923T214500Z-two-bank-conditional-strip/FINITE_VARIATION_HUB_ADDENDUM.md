# Finite-variation hub corollary

Under the two-bank assumptions in the [conditional strip report](./REPORT.md), let the independent hub \(H\) have a cap-one probability density \(f_H\) of finite total variation \(\operatorname{TV}(f_H)\). Then, for
\[
Q=2HL+\beta L^2+V^2+2\varepsilon LP,
\]
the [finite-component layer-cake bound](./QUASICONCAVE_HUB_ADDENDUM.md) yields
\[
\|p_Q\|_\infty
\le C\sqrt{M_AM_B}\,\sqrt{\operatorname{TV}(f_H)/2}+\frac12. \tag{1}
\]
The estimate is uniform in \(\beta,\varepsilon\) and requires no support, moment, or independence-within-bank assumptions on the overlapping \(P\) coordinate.

For completeness, write \(E_t=\{h:f_H(h)>t\}\), \(t\in(0,1)\), and let \(N_t\) be its number of interval components for almost every \(t\). One-dimensional BV coarea and integrability of \(f_H\) give
\[
\int_0^1 2N_t\,dt=\operatorname{TV}(f_H).
\]
Layer cake gives \(\int_0^1|E_t|dt=\int f_H=1\). For the interval components \(I_{t,j}\),
\[
K(f_H)=\int_0^1\sum_{j=1}^{N_t}\sqrt{|I_{t,j}|}\,dt
\le\int_0^1\sqrt{N_t|E_t|}\,dt
\le\sqrt{\Big(\int_0^1N_tdt\Big)
\Big(\int_0^1|E_t|dt\Big)}
=\sqrt{\operatorname{TV}(f_H)/2}.
\]
Substitution in the linked density bound proves (1). Cap-one densities of infinite variation remain outside this corollary.
