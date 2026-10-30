# B17 source-bound handoff — signed convolution packet

**Classification:** `ESSENTIAL_STEP_APPLIED`; **full FEI remains OPEN**.

Bound live candidate: `LIMIT-PRIME-GATE-LIFT-v1`, \(C^\dagger=6.521851214\), with exact balanced-uniform Gibbs/Bellman identity from fleet03/B18 `20260922T075546Z-gibbs-price-bellman/REPORT.md`.

Substantively applied fleet04/B16 `20260922T081206Z-signed-gibbs-phase-residual/REPORT.md`, blob `2ff82a8e044d035beb32d8fa48a7bc6303abbc14`. B16 obtained a one-\(T\) lower bound from the Boolean convolution identities. New result: all \(inom{k}{2}\) two-coordinate equations accumulate orthogonally. If \(ho_y(S)=y^{|S|}/((1+y)^k-1)\), \(b_S=\operatorname{sgn}(\hat f(S))\sqrt{\rho_y(S)}\), and \(d^2=\sum(\sqrt w-\sqrt\rho)^2\), then for every \(q>4\), \(\alpha=(q-4)/(q-2)\),

\[
2\sqrt{\binom{k}{2}}\frac{y}{(1+y)^k-1}
[3-2(1+y)^{k-2}]_+
\le 2d+Q_{k,q}(y)^{2-\alpha}d^\alpha,
\]

\[
Q_{k,q}(y)=1+\sqrt{\frac{(1+(q-1)y)^k-1}{(1+y)^k-1}}.
\]

Hence \(D_{KL,2}(w\|\rho_y)\ge d_*^2/\ln2\), where \(d_*\) is the unique positive root of the displayed equality. For \(y=\eta/k\), any fixed \(0<\eta<\ln(3/2)\) gives a **dimension-independent positive KL floor**; the explicit formula is in `REPORT.md`.

The exact remaining gap is compatibility with the Bellman-optimal/low-price tilt (and arbitrary product biases): at \(y=\eta/k\) the corresponding \(\lambda\) eventually becomes negative, so this packet floor alone does not close the live candidate. Next useful move: derive a packet inequality whose scale follows the optimal tilted price distribution, or produce a genuine Boolean gate+bias violating the candidate.
