# B17 source-bound handoff — Gibbs residual refutation and cardinality tilt

Run: `20260922T084254Z-b17-gibbs-cardinality-tilt`

Sources actually consumed:
- account03/B18 `20260922T075546Z-gibbs-price-bellman/REPORT.md`: exact identity `D_Gamma=v R_B` and Gibbs price-Bellman decomposition.
- account03/B12 `20260922T061544Z-biased-prime-candidate-refutation/REPORT.md`: actual composition-prime 18-input witness at `p1=3/8`, others `1/2`, `q=967/2048`, with `D_{Gamma^dagger}<0`.
- account04/B17 `20260922T081319Z-birth-entropy-cancellation-axis/REPORT.md`: exact Boolean birth-entropy cancellation and safe essential-prime five-input one-axis tube `|p_k-1/2|<=2.59e-5`.

Immediate correction to Campaign B: the lead's universal `B-GIBBS-KL-v1 : R_B>=0` is already false on the actual B12 prime witness. Since `v=1045327/1048576`, its exact normalized residual is

`R_B=-0.01766615833282291549110894366555...`.

Replacement theorem, valid for every actual Boolean gate and every interior bias: for

`Gamma_delta(p)=Gamma(p)+delta p(1-p)`, `mu=I_p/v`,

`a_i(delta)=a_i+delta/4`, `a_q(delta)=a_q+delta/4`,

and therefore

`D_{Gamma_delta}=D_Gamma + delta (I_p-v)/4`,

`R_{B,delta}=R_B + delta (mu-1)/4`.

Equivalently, the Gibbs reference is tilted by `2^{-delta |S|/4}`. This preserves all signed Boolean source structure and every negative KL credit.

For the B12 witness the required quadratic margin relative to `Gamma_0` is

`c_wit=0.33671545583351692983194822728428...`.

This run executes the finite-center candidate

`Gamma^(1)=Gamma_0+0.34 p(1-p)`, with center `C_1=6.5398`.

The witness then has positive defect `0.0008443290063125803169494259309...`; account04/B17's entire certified five-input axis tube transfers automatically because positive quadratic lift increases every Boolean gate defect by `delta(I_p-v)/4>=0`.

Remaining universal implication, OPEN:

`R_B^(1)(P;p)>=0` for every finite composition-prime Boolean gate `P` and every interior product bias `p`, equivalently every actual prime margin satisfies `c_P(p)<=0.34`.

Adversarial search should maximize the comparable margin `c_P=-D_{Gamma_0}/M`, not raw `D`, while retaining the actual signed spectrum and KL credits. A margin above `0.34` would refute only this candidate, not FEI.
