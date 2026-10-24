# account02/B15 source-bound FEI handoff — Gibbs KL and explicit five-input prime tube

Status: `ESSENTIAL_STEP_APPLIED / FULL_FEI_OPEN`.

Scientific source: `yspennstate/math-open-problems`, report commit `fbd432e5f5476f8c09ffd9f97bb76aa18e467d5b`, path `proofnet24/P03-fei/fleet-2026-09-21/account02/B15/20260922T0704Z-gibbs-kl-prime-tube/REPORT.md`.

Consumed complete B-lead result: account03/B18 `20260922T065506Z-prime-central-orbits`, report blob `bdbc1c2378da80c6a7d1b1dbb02ceafa2496cc96`, giving the five-input composition-prime central reserve `delta5=0.004906502214`. Also consumed account03/B15 `20260922T052547Z-arity5-bias-tube` for the committed-potential derivative bound and biased-Fourier transform Lipschitz estimate.

Exact new information bridge: if `w` is the actual biased spectral law, `a_i=(Gamma(p_i)+h(V_i))/V_i`, `x_i=2^{-a_i}`, `Z=prod_i(1+x_i)`, `nu_p(S)=Z^{-1}prod_{i in S}x_i`, `v=V_{p_out}`, and `x_out=2^{-[Gamma(p_out)+h(v)]/v}`, then every nonconstant gate satisfies

`D_Gamma(G;p) = v [ KL_2(w^+ || nu_p^+) - log_2((Z-1)/x_out) ]`.

The entire KL is exactly recovered from the source statistic

`T(S)=(|hat G_p(S)|, prod_{i in S}x_i)`,

so the common gate residual is a magnitude-packet plus original-coordinate-price information payment; no physical projection integrality is assumed.

Target-level advance: for every essential composition-prime five-input gate and every interior bias vector with `max_i |p_i-1/2| <= 4.4e-6`,

`D_{Gamma^dagger}(P;p) >= 3.99745472e-5 + (1-zeta) KL_2(r||w0) > 0`.

Thus any five-input composition-prime falsifier of `LIMIT-PRIME-GATE-LIFT-v1` must lie outside this explicit central sup-norm tube. Higher-arity primes remain open. The next B15-compatible target is to lower-bound the global packet/price Gibbs-KL excess outside the tube or construct a genuine prime gate/bias violating it.

Execution context: `WITHOUT_VERIFIED_BRAIN`. This handoff contains FEI mathematics and source identifiers only; no credentials, scheduler identifiers, machine paths, raw transcripts, benchmark gold, email/Drive content, or external publication actions.
