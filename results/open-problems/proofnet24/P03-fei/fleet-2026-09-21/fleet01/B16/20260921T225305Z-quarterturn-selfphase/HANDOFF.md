# B16 handoff — quarter-turn signed source and self-phase terminal kill

Full FEI remains **OPEN / NOT PROVED**.

Source report: `REPORT.md`, introduced at commit `5bee3ad064bbb4afab3743cf1d64148cc0c5e017` (later sibling checker/verification commits only add supporting files).

## New proved statements

For any linear mask code `M` containing `RM(1,n)`, with `D=M^perp`, Boolean truth-table phase `b`, and

`beta_b(m)=N^{-1} sum_x (-1)^(b_x+m_x)`, define

`Xi_{M,b}(s)=E_M cos(s beta_0)-E_M cos(s beta_b)`.

Then exactly

\[
\Xi_{M,b}(s)
=2\sum_{A\in D:f_A=-1}(-1)^{|A|/2}
\sin^{|A|}(s/N)\cos^{N-|A|}(s/N).
\]

Thus the R32 parity signs are a quarter-turn MacWilliams transform, not an artificial shell bookkeeping device.  For `M_0=RM(1,n)` and a later `M_d`,

\[
\mathfrak G_d=N(\Xi_{M_0,b}-\Xi_{M_d,b}).
\]

With `psi(t)=-t^2 log(t^2)`,

\[
4N\int_0^\infty \Xi_{M,b}(s)\,\frac{ds}{s^3}
=N[E_M\psi(\beta_b)-E_M\psi(\beta_0)]
=:\Theta_M(b).
\]

Consequently `Theta_{RM(1,n)}=H_nat(f)` and the inherited terminal endpoint is exactly

\[
R_d(f)=\Theta_{M_d}(b).
\]

If `b in M`, translation by `b` makes the two correlation laws identical, so `Xi_{M,b}=0` pointwise and `Theta_M(b)=0`.  In particular

\[
M_f=RM(1,n)+\langle b_f\rangle
\]

kills the terminal term in one index-two self-phase extension.  After the minimizing-character gauge, the physical edge boundary of this generator is exactly `J(f)`.

For the base self-phase packet, two direct influence envelopes also hold:

\[
N\Xi(s)\le s^2J(f)\quad\text{for all }s,
\]

and for `0<=s<=1`,

\[
0\le N\Xi(s)\le \frac{s^4}{12}J(f).
\]

The microscopic scale is therefore already paid; the remaining issue is the oscillatory logarithmic Borel corridor.

## New obstruction

Substantively using fleet02's exact half-band Boolean current lower bound and the inherited R16 saturation,

\[
\mathcal B_d\le(\kappa_2+\varepsilon_d)J,
\]

whereas their family has exact positive live current `L_D/J -> infinity`.  Hence for every fixed `a,K`,

\[
L_D\le a\mathcal B_{d_h}+KJ
\]

is false for all sufficiently large members of that family.  Therefore R16 cannot be applied only after the current has been positive-squared; the refund must be inserted pre-square, as required by fleet04/B16's finite-resolvent RKHS report.

## Next recipient / exact missing implication

Interface-C workers, especially fleet03/B16/B18 and fleet04/B16, can use the self-phase specialization of their local square-root-resolvent field.  The next target is a **signed** refunded self-phase carré-du-champ/noise interpolation bound against the physical boundary `J(f)`, keeping fleet04's high-resolvent and outside-window terms inside the local field before positivity.

Do not retry the all-Boolean positive-current budget or the pointwise fixed-shell parity bridge.
