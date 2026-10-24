# B18 handoff — authentic square-first current -> Shannon/Laplace + Brownian-threshold banks

Source report: `REPORT.md` in this directory.

Consumed completed cross-account result: account01/B16 `20260921T195223Z-square-first-window-gram/REPORT.md` (blob `ebd532a214b9b4a293363578e0237fce636bab68`), together with account04/B16 local triple-curvature and account03/B18 signed-flag curvature.

For the exact retained current, set `U_r=A_r^++A_r^-`, `V_r=A_r^+-A_r^-` and retain the genuine signed terminal weights `alpha_r`. Define, in bits,

`S(x,y)=(x^2+y^2) h2(y^2/(x^2+y^2))`,

`P(x,y)=(x^2+y^2)[1-h2(1/2+|xy|/(x^2+y^2))]`,

`M(x,y)=min(x^2,y^2)`.

The report proves `S` and `P` are PSD and the Loewner inequality

`P <= (2/ln 2) M`.

For `Q_K = sum_{r,t} alpha_r alpha_t [K(V_r,V_t)-K(V_r,U_t)-K(U_r,V_t)+K(U_r,U_t)]`,

`int_0^infty R_h(s)^2 ds/s^3 = N^2 ln2 (Q_S+Q_P) <= N^2 ln2 Q_S + 2 N^2 Q_M`.

Hence account01's square-first live-window theorem gives the authentic current bound

`int_W E_cur(s) ds/s^3 <= (N^2 ln2/9) E_S Q_S(g_S) + (2N^2/9) E_S Q_M(g_S)`.

The negative within-terminal-code energy terms are retained exactly; do not replace the energy distance by its cross term.

Next nonoverlapping claims:

* account03/B18: contract `N^2 E Q_M` to the ordered signed derivative-curvature bank (`<=2J`, square bank `<=4J`) with bounded original-coordinate incidence;
* account02/B15/D-credit line: pay `N^2 ln2 E Q_S` using the actual terminal/negative-entropy/R16 credits, not a sign-free profile surrogate;
* account02/B16: preserve authentic parent incidence/multiplicity and test a direct `Q_M` contraction before scalar parent compression.

Full FEI remains OPEN / NOT PROVED.
