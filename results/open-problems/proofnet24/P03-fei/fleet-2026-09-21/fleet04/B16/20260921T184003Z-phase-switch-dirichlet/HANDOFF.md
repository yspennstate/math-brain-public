# B16 handoff — phase-switch Dirichlet / quartic cancellation

Status: **WITHOUT_VERIFIED_BRAIN; full FEI OPEN / NOT PROVED.**

New exact facts:

1. If `b_R` is the same-active-syndrome signed R32 aggregate and `Psi_s` is the retained `C0-D_d` Borel potential, then
   \[
   \sum_{|R|\ {\rm odd}}b_R^2
   =\frac14 E_S[\Psi_s(g_S)-\Psi_s(fg_S)]^2
   =E_S\,\mathfrak G_{f,g_S}(s)^2.
   \]
   Here `mathfrak G` is the actual signed frustrated R32 response with a dual-character twist.

2. Hence the authentic parity current obeys the sharp syndrome-only reductions
   \[
   E_{\rm cur}\le\frac19E_S[\Delta_f\Psi_s]^2,\qquad
   E_{\rm cen}\le\frac{11}{1152}E_S[\Delta_f\Psi_s]^2.
   \]

3. For every residual code `E <= C0`, the exact MacWilliams phase switch factors as a sine product.  Because `C0` has no weight-two word, its quadratic term vanishes identically:
   \[
   \sum_{r\in E^\perp}A_r^+A_r^-=0.
   \]
   The first possible response is quartic:
   \[
   |\Phi_{E,s}(h)-\Phi_{E,s}(fh)|
   \le \frac23s^4(p_+^2+p_-^2)\sqrt{p_+p_-}.
   \]

4. Keeping `C0-D_d` as one signed dual average gives
   \[
   |\Psi_s(h)-\Psi_s(fh)|
   \le \frac43s^4(1-\rho_d)(p_+^2+p_-^2)\sqrt{p_+p_-},
   \quad
   \rho_d=\frac{2N}{|D_d^\perp|}.
   \]
   The retained quadratic term still cancels *before* any absolute value.

5. In the minimizing-character gauge,
   `p_+p_- <= J(f)/4`, so at every fixed Borel time
   \[
   E_{\rm cen}(s)
   \le\frac{11}{1152}(1-\rho_d)^2J(f)
   \min\{16s^4,(4/9)s^8\}.
   \]

Next target: keep the exact sine product at large Borel time and insert the ordered physical flag/Radon Hardy kernel before taking absolute values.  Do not return to raw channel counts, unit q-flip frames, one-resolvent transport, or generic endpoint `L2`.
