# B16 FEI handoff — exact low-Hardy frequency localization

Full FEI remains **OPEN / NOT PROVED**.

New theorem: for a physical cut with `a_i(U)=hat eta_i(U)^2`, odd source
\[
A_i^\kappa(t)=-4\sum_{|U|\ {\rm odd}}a_i(U)\kappa_Ut^{|U|}
\]
and Hardy resolvent
\[
(\mathcal RA)(t)=t^{-1}\int_0^t sA(s)\,ds,
\]
the exact low-band energy is
\[
\int_0^{1/2}(\mathcal RA_i^\kappa)^2dt
=
16\sum_{U,V}a_i(U)a_i(V)\kappa_U\kappa_V
\frac{2^{-(r+s+3)}}{(r+2)(s+2)(r+s+3)}.
\]

Two useful consequences:

1. If `|kappa_U|<=M`, the energy is at most `M^2 E_i^2/90`, sharp at a one-bit affine cut. After the minimizing-character fold, the aggregate is at most `2 M^2 J/1215`.

2. Much more importantly, define
\[
M_H=\sup_{U\ {\rm odd}}
\frac{|\kappa_U|}{(|U|+2)2^{|U|-1}}.
\]
Then the energy is at most `M_H^2 E_i^2/10`, hence aggregate at most `2 M_H^2 J/135`. Thus the low Hardy channel tolerates multiplier growth of order `(r+2)2^{r-1}`.

For the inherited raw ordered-min entropy multiplier,
\[
|A^{raw}_{n,r}|
\le \frac{4(n+1)}{(r+1)(r+2)}+\frac{12}{n}.
\]
Therefore for odd `r>=R`,
\[
\frac{|A^{raw}_{n,r}|}{(r+2)2^{r-1}}
\le
\frac{4(n+1)}{(R+1)(R+2)^2 2^{R-1}}
+\frac{12}{n(R+2)2^{R-1}}.
\]
Taking the smallest odd `R` with `2^{R-1}>=n` makes this `O(R^{-3})+O(n^{-2}R^{-1})`.

Interpretation: the inherited raw dimension blow-up is genuinely a **low odd-mode** problem. The exact central Hardy geometry already pays the high-frequency tail. The next B16 target should compute the fully refunded Shapley+terminal+R16 multiplier only on the low odd band `r=1,3,...,R_n` with `2^{R_n-1}~n`; singleton cancellation remains mandatory. Do not demand uniform all-frequency `O(1)` control.

Structured check: the newest monomial-defect Shapley-refunded entropy multiplier has magnitude `H_k/k<=1` on the genuine odd cut spectrum, so its low-Hardy component is uniformly paid by `E_i^2/90`.

Report: `REPORT.md`; exact checker: `check_central_hardy_localization.py`; checker output: `verification.txt`.
