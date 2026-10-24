# account01/B17 FEI handoff — signed convolution packet

**Classification:** `ESSENTIAL_STEP_APPLIED`. **Full FEI remains OPEN.** Execution: `WITHOUT_VERIFIED_BRAIN`.

Bound source versions: live candidate `LIMIT-PRIME-GATE-LIFT-v1`; account03/B18 exact Gibbs/Bellman decomposition `20260922T075546Z-gibbs-price-bellman/REPORT.md`; account04/B16 signed single-\(T\) residual theorem `20260922T081206Z-signed-gibbs-phase-residual/REPORT.md`, blob `2ff82a8e044d035beb32d8fa48a7bc6303abbc14`.

New theorem: for balanced uniform Boolean \(f\), radial Gibbs law \(\rho_y(S)=y^{|S|}/((1+y)^k-1)\), and sign-aligned Gibbs amplitudes, the whole family of \(\binom{k}{2}\) two-coordinate Boolean convolution equations accumulates orthogonally. If \(d^2=\sum(\sqrt w-\sqrt\rho)^2\), then for every \(q>4\), \(\alpha=(q-4)/(q-2)\),

\[
2\sqrt{\binom{k}{2}}\frac{y}{(1+y)^k-1}[3-2(1+y)^{k-2}]_+
\le 2d+Q_{k,q}(y)^{2-\alpha}d^\alpha,
\]

with

\[
Q_{k,q}(y)=1+\sqrt{\frac{(1+(q-1)y)^k-1}{(1+y)^k-1}}.
\]

Therefore the live Gibbs residual has an explicit positive KL floor whenever the packet term is positive. At the mesoscopic scale \(y=\eta/k\), every fixed \(0<\eta<\ln(3/2)\) yields a **dimension-independent** positive KL separation from the radial Gibbs law. Full formulas/proof/checker are in private scientific artifact `proofnet24/P03-fei/fleet-2026-09-21/account01/B17/20260922T084426Z-signed-convolution-packet/`.

Remaining essential gap: make the packet scale compatible with the Bellman-optimal low-price tilt uniformly in arity and arbitrary product bias (or falsify the live candidate with a genuine Boolean gate+bias). The mesoscopic \(y=\eta/k\) tilt eventually has negative \(\lambda\), so the new KL floor alone is not a full-candidate proof.
