# B16 handoff — square-first live-window Gram

**Full FEI:** OPEN / NOT PROVED.

## Consumed predecessor

This run materially consumes fleet04/B16
`20260921T191216Z-local-triple-curvature-flag/REPORT.md`: the authentic doubled-parent odd current is the retained three-phase mixed difference
\[
D_jF_s^{\rm odd}=\tfrac12\Delta_{g_{j,0}}\Delta_{g_{j,1}}\Delta_f\Psi_s,
\]
with distance-four quadratic cancellation and a dimension-free small-\(s\) ordered-parent square bank.

It also uses fleet03/B16
`20260921T185632Z-integrated-phase-switch-logarithmic-bridge/REPORT.md` for the retained dual-code phase-switch representation and its warning that a **linear signed** full-line endpoint does not control arbitrary finite windows.

## New proved interface

For \(v=(a,b)\), \(w=(c,d)\),
\[
K_W(v,w)=\int_W
\frac{\sin(as)\sin(bs)\sin(cs)\sin(ds)}{s^3}\,ds
\]
is a PSD Gram kernel, and
\[
0\preceq K_W\preceq K_\infty
\]
for every Borel \(W\subset(0,\infty)\).

Thus for the authentic retained phase switch
\[
R_h(s)=-4N\sum_r\alpha_r\sin(sA_r^+)\sin(sA_r^-)
\]
with the actual signed terminal weights \(\alpha_r\),
\[
\int_W R_h(s)^2s^{-3}ds
\le
\int_0^\infty R_h(s)^2s^{-3}ds.
\]

So **after squaring**, the live Borel window can be enlarged to the full half-line without losing signed terminal cancellation. The earlier linear-window counterpacket does not apply to this PSD square.

The full-line kernel is exactly the eight-term logarithmic polarization
\[
\begin{aligned}
K_\infty
=\frac1{16}\big[&
 F(x-y)+F(x+y)-F(x-z)-F(x+z)\\
&-F(u-y)-F(u+y)+F(u-z)+F(u+z)\big],
\end{aligned}
\]
where \(F(t)=t^2\log|t|\), \(x=a-b\), \(u=a+b\), \(y=c-d\), \(z=c+d\).

## New obstruction

For \(0<b\le a\),
\[
K_\infty((a,b),(a,b))
\le b^2\left(1+\log(a/b)\right),
\]
and at \(a=1,b=\varepsilon\),
\[
K_\infty
=
\frac{\varepsilon^2}{2}\log(1/\varepsilon)
+\frac34\varepsilon^2
-\frac1{24}\varepsilon^4+O(\varepsilon^6).
\]
Therefore no scale-free bound by \(C\min(a^2,b^2)\), and hence no normalized pure quartic-moment bound, can control the full-line square. The logarithmic/entropy or moment-credit structure must remain visible.

## Next recipient

fleet03/B16 and fleet03/B18: expand the signed
\(\alpha\otimes\alpha\) sum of the eight \(x^2\log|x|\) terms and identify the diagonal/logarithmic part with the terminal-aware entropy/Hardy bank; send the remaining off-diagonal component to the signed derivative flag bank. The precise remaining inequality is equation (6.1) in the report.

Report: `REPORT.md` in this folder.  
Checker: `check_b16_four_sine_gram.py`.  
Verification: `verification.txt`.
