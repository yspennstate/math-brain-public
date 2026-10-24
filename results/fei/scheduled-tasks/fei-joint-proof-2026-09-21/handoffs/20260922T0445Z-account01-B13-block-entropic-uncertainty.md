# FEI handoff — account01/B13 block entropic uncertainty

Classification: `AUXILIARY_ONLY`. Full FEI remains OPEN. Execution: `WITHOUT_VERIFIED_BRAIN`.

Source-bound scientific report: `yspennstate/math-open-problems`, commit `5592acca867d55ed23881ca1bac907417048fded`, path `proofnet24/P03-fei/fleet-2026-09-21/account01/B13/20260922T0445Z-block-entropic-uncertainty/REPORT.md`. Checker commit `9c4f8272d1f540709a23c846aa7b18d850fe8876`; captured-output commit `cb7bd8ffac986eac7c9830dc2de283de06f38a83`.

Named peer result consumed and applied: account02/B18 `20260922T040428Z-random-block-currency`, report blob `bd4972b11cb13989282f555deb9354509d1da590`. Its exact selector is `D_*(G)-E D_*(G_A)=B_A^RO+a_*Q_A`, with stable candidate `C_*=6.5218512`, `a_*=0.2682048`. Account03/B13 `20260922T040037Z-bent-swap-local-margin` is also consumed as the source-valid refutation of a uniform pointwise local scalar cap.

New theorem. For a physical block `A`, branch assignment `Z=X_A`, root spectral sample `S=(U,T)` with `U=S cap A`, `T=S cap A^c`, and child spectral sample `T` after restriction, put

`L_A=sum_{i in A} -log2 max(p_i,1-p_i)` and `eta_A=H(Z)-L_A`.

Then

`H(Z|T)+H(U|T) >= L_A`, hence

`I(Z;T) <= H(U|T)+eta_A`,

and the exact restriction entropy drop obeys

`Delta_A H = H(U|T)+I(Z;T) <= 2 H(U|T)+eta_A`.

At uniform bias `eta_A=0`; in particular for a singleton `JS_i <= H(S_i|S_-i)`.

Application to the exact selected restriction. If

`L_A^RO=sum_{i in A} It_i/V_i [Gamma_RO(p_i)+h2(V_i)]`,

then

`B_A^RO >= L_A^RO + E Gamma_RO(r_Z)-Gamma_RO(r) - 2H(U|T)-eta_A`.

Therefore a minimum-essential-arity stable-candidate counterexample on the uniform cube must satisfy, for every proper nonempty block A,

`2H(S_A|S_Ac) > C0 sum_{i in A} Inf_i + E Gamma_RO(r_Z)-Gamma_RO(r) + a_* Q_A`, `C0=6.4548`.

This is a proved simultaneous structural condition, not a hypothesis. The remaining implication is to show that no composition-prime Boolean gate can satisfy these inequalities at every block/scale; a crude Han bound is insufficient.

Bias penalty is necessary: for the two-bit one-point defect with biases `(1/5,9/10)` and block the second coordinate, `H(U|T)=0.137351990984347`, `I(Z;T)=0.248854588206471`, so the unpenalized biased form fails by `0.111502597222124`, while `eta_A=0.316992500144231` restores the theorem.

Finite falsification checks: exhaustive uniform singleton cases through n=4, `131474` cases, zero observed violation; 750 deterministic random biased block cases, zero observed violation of the penalized theorem. Analytic proof is independent of these checks.
