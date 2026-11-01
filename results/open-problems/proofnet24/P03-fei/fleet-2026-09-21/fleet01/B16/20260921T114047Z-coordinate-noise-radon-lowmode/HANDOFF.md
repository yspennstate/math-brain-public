# B16 handoff — coordinate-noise/Radon bridge

Full FEI remains **OPEN**.

Proved in `REPORT.md`:

- exact one-coordinate-noise identity `(T_t^{(i)} f)^2 = 1-(1-t^2) eta_i`, hence every nonconstant cut Fourier coefficient is exactly a normalized one-coordinate noisy-square correlation;
- exact q-flip frustration spectrum `p_hat_i(0)=2 E_i`, `p_hat_i(U)=-2 eta_hat_i(U)^2` for `U != 0`, giving a dimension-free centered `L2` kernel payment by `J(f)`;
- for the random-order raw dual-generator entropy displacement kernel, fixed low Walsh modes satisfy `A_{n,r}=4n/((r+1)(r+2))+O_r(1)`;
- the two-variable parity-switch function with `n-2` dummy coordinates realizes the bad singleton mode, so subtracting only the constant baseline still loses `~(2/3)n` relative to the distinguished-coordinate influence.

Therefore the next target is **not** another absolute or centered raw-baseline estimate. Compute the low displacement-Walsh multipliers of the *combined* Shapley plaquette + terminal + retained R16/moment refund kernel. Dummy-variable invariance forces cancellation of the raw `A_{n,1}` growth in any dimension-free closure. If that singleton cancellation holds, prove its fixed-`r` analogue and use the fractional noisy-square bank on the high-frequency remainder. If it fails for the complete residual, abandon the random-order q-flip basis route.

Companion exact checker: `check.py`; saved output: `CHECK_OUTPUT.txt`.
