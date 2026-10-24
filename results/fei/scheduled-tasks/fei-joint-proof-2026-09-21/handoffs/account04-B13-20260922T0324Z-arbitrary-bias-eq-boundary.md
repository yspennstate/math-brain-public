# account04/B13 FEI handoff — arbitrary-bias EQ boundary

Source scientific artifact: `yspennstate/math-open-problems/proofnet24/P03-fei/fleet-2026-09-21/account04/B13/20260922T0324Z-arbitrary-bias-eq-boundary/REPORT.md`, readback blob `58bc9653da0a1db3514c927bc0a88c78b695e10c`.

Newest peer consumed: account03/B17 `20260922T0304Z-biased-eq-boundary`, report blob `1da6fe7259cf4a560dd703f42947bd90060e73bd`.

New result: for the antipodal sparse gate `EQ_d`, arbitrary biases have exact Fourier coefficients
`hat f(S)=-2[P prod_{i in S}sqrt(q_i/p_i)+(-1)^|S| Q prod_{i in S}sqrt(p_i/q_i)]`, exact normalized influences `It_i/V_i=P_{-i}+Q_{-i}`, and exact Poincare currency `W=P sum q_i+Q sum p_i-r(1-r)`.

If a symmetric potential has `Gamma(s)=A s log2(1/s)+B s+o(s)`, `A>0`, and `p_i=t w_i` for a fixed interior probability vector `w`, then

`D_EQ(tw)=A t H(w)+o(t)` and `W_EQ(tw)=t^2(1-sum w_i^2)/2+O(t^3)`.

Hence

`t c_EQ(tw) -> -2 A H(w)/(1-sum w_i^2) <= -2A/ln 2 < 0`.

For the source read-once fixed-point tail, tightness of the fresh-variable AND line forces `A=2(C0-4)=4.9096` at `C0=6.4548`; the quadratic lift does not change `A`. Therefore the live lifted candidate is safe along every fixed-ratio rare-corner (and complementary) EQ ray. The EQ adversarial search is reduced to compact interior biases or singular hierarchical boundaries whose bias ratios themselves degenerate.

Full FEI remains OPEN. Next target: either certify the compact interior for EQ3/EQd with the fixed candidate, or analyze the one-coordinate-dominant hierarchical boundary against the decomposable/cocycle mechanism.

Account04/B18 mixed-curvature conservation and exact zero-defect classification are preserved unchanged and were not used as a shortcut.
