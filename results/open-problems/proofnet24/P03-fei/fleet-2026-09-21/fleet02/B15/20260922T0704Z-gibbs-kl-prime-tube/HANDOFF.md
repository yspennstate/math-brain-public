# B15 handoff — all-gate Gibbs KL and explicit five-input prime tube

**Status:** `ESSENTIAL_STEP_APPLIED / EXPLICIT_PRIME_BIAS_TUBE`; full FEI remains **OPEN / NOT PROVED**.

**Candidate:** `LIMIT-PRIME-GATE-LIFT-v1`, `C^dagger=6.521851214`, `Gamma^dagger=Gamma_0+0.268204856 p(1-p)`.

**Consumed peer results:** fleet03/B18 `20260922T065506Z-prime-central-orbits` supplies the strict central prime reserve `delta5=0.004906502214`; fleet03/B15 `20260922T052547Z-arity5-bias-tube` supplies the committed-potential derivative bound `|Gamma^dagger'|<85` on the relevant output interval and the source-valid biased-Fourier transform Lipschitz estimate.

**Exact information bridge.** For the actual biased spectral law `w`, put `a_i=(Gamma(p_i)+h(V_i))/V_i`, `x_i=2^{-a_i}`, `Z=prod_i(1+x_i)`, and let `nu_p(S)=Z^{-1}prod_{i in S}x_i`.  If `v=V_{p_out}` and `x_out=2^{-[Gamma(p_out)+h(v)]/v}`, then for every nonconstant gate

`D_Gamma(G;p) = v [ KL_2(w^+ || nu_p^+) - log_2((Z-1)/x_out) ]`.

Moreover the entire conditional KL is exactly recovered by the statistic

`T(S)=( |hat G_p(S)| , prod_{i in S} x_i )`.

Thus the common gate residual is literally a packet plus original-coordinate-price relative-entropy payment; no physical projection integrality is assumed.

**New explicit tube.** For every essential composition-prime five-input gate `P` and every product-bias vector with

`max_i |p_i-1/2| <= 4.4e-6`,

`D_{Gamma^dagger}(P;p) >= 3.99745472e-5 + (1-zeta) KL_2(r || w0) > 0`,

where `w0` is the central spectral law, `zeta` is the perturbed mass on central-zero Fourier atoms, and `r` is the perturbed law conditioned on the old support.  The proof uses the exact five-bit granularity `w0(S)>=1/256` on old nonzero atoms and preserves the negative KL credit in the entropy perturbation formula.

**Replacement obligation:** any five-input composition-prime falsifier must now lie outside the `4.4e-6` central sup-norm tube.  The global information target outside it is

`KL_2(w^+ || nu_p^+) >= log_2((Z-1)/x_out)`.

Lower-bound this packet/price Gibbs-KL excess, or construct a genuine prime gate/bias source violating it.  Higher-arity primes remain open.
