# FEI handoff supplement — sharp front-loading of random-restriction currency

Source: `proofnet24/P03-fei/fleet-2026-09-21/account02/B18/20260922T051105Z-random-depth-barycenter/FRONTLOADING.md`, creation commit `463eb9aab538d3f037d3476718db4d272f6a9d79`.

From the exact fixed-size random-restriction formula,

\[
\Delta_r=P_r-P_{r+1}=\frac1{4n}\sum_{k\ge2}kW_k\left[1-\frac{(r)_{k-1}}{(n-1)_{k-1}}\right]
\]

is nonincreasing in depth.  Since `Delta_0+...+Delta_{n-2}=P_0`, every first `m` depths consume at least the uniform fraction

\[
\boxed{Q_m=P_0-P_m\ge \frac{m}{n-1}P_0},
\qquad
\boxed{P_m\le\frac{n-1-m}{n-1}P_0}.
\]

This strictly strengthens B18's previous `m/n` contraction.  For `1<=m<=n-2`, equality at the level-profile relaxation requires all positive higher-order Fourier mass on the top level `k=n`; pure top level attains equality.

Use this only as a currency input to the signed two-generation/adaptive-depth compensation problem.  It is not a bound on the signed base deficit and does not prove FEI.
