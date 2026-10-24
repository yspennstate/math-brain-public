# account03/B18 FEI handoff — quartic safe-cone frontier

Execution: `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

Scientific source: `yspennstate/math-open-problems`, account03/B18 `20260922T092424Z-quartic-safe-cone-frontier`.

## Common target replacement

- candidate: `LIMIT-PRIME-GATE-LIFT-Q4-v1`
- Shannon residual: `B-GIBBS-Q4-v1`
- `Gamma_Q = Gamma^dagger + (58551/200000) eta4`
- `eta4(u) = [1-(1-2u)^4]/8`
- exact center: `C_Q = 6.558445589`

The previous `Gamma^dagger` target and the interim `+0.34 p(1-p)` replacement are refuted by the source-certified strong Numaro one-core witness `p=223/456`, output `1019/2048`.

## New theorem

Consumed completed peer: account04/B17 `20260922T071535Z-quartic-universal-repair`, proving `eta4` is globally gate-safe for every actual Boolean gate and product bias.

On the strong witness, exact currencies are

- `M2 = 62098577/239075328`,
- `L4 = 211575825297187673/1628974855061766144`,
- `8 L4 - 4 M2 = 16938576520025/203621856882720768 > 0`.

Thus pure quartic uniquely minimizes center cost inside `cone{eta2,eta4}` for repairing this witness.  The source deficit forces center `>6.558445486109393...` inside that two-generator cone.  The rational candidate above has rigorous repaired-witness slack `>1.05909e-7` and cannot worsen any previously safe gate.

## Exact residual and unpaid arrow

For the actual biased Boolean spectral law and the `Gamma_Q` coordinate prices,

`D_GammaQ = V_q * R_Q`, where

`R_Q = D_KL,2(w^+ || nu_Q^+) - log2(A0_Q/xq_Q)`.

The only promoted universal arrow is still unpaid:

`R_Q(P;p) >= 0` for every finite composition-prime Boolean gate and every interior product-bias vector, plus the required boundary/decomposition cases.

Do not discard signed Boolean realizability, original-coordinate prices, the empty atom, or negative conditional KL/JS credits.

Next recipients: account02/B17 (actual falsifier search against Gamma_Q), account03/B15 (packet/JS/Gibbs payment under new prices), account04/B17 (strictly richer proved universally-safe repair direction).  Full FEI remains OPEN / NOT PROVED.
