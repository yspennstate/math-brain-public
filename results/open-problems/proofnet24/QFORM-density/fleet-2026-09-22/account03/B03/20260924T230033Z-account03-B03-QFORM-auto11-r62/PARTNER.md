# r62 partner application

Use account04/B03 `QFORM-B03-PAIR-IN-HUB-PLANCHEREL-v1`,
commit `da1d4e5510082c67ee7b34bbe70fde2060451518`.

At k=2:
[
 |phi_P(t)|^2 <= min(1, pi^3 alpha |t|^{-3}).
]
Splitting at (t_0=pi alpha^{1/3}) gives
[
 int |t|^{1/2}|phi_P(t)|^2dt
 <=(8/3)pi^{3/2}alpha^{1/2}.
]
For alpha=1 the bound is 14.848874658217888.

For a normalized no-pivot s3 output Q, r62 gives
[
 int |t|^{-1/2}|phi_Q(t)|^2dt
 <=41.48595888463038.
]
When P and Q are independent, complementary-weight Cauchy--Schwarz gives
[
 int |phi_Q(t)phi_P(t)|dt
 <=sqrt(41.48595888463038 * 14.848874658217888) alpha^{1/4}.
]
Fourier inversion therefore gives
[
 oxed{||p_{Q+P}||_infty
 <=3.95018530081809,alpha^{1/4}.}
]
For the partner's literal six-source packet alpha=1, so the density bound is <3.951.

This is the required equation-level application. Applying the two weights to the same output controls L2 rather than L1 and does not yield a bounded density.
