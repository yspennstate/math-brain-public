# P20: radial inverse-source criterion from the 100-agent review

This is an append-only cross-reference to the complete new proof in [agent 105](https://github.com/yspennstate/math-open-problems/blob/master/proofnet24/portfolio-completion/runs/2026-09-14/2026-09-14_20-23-26/agents/105.md), Git blob `cf9813d491f65884742f303aeccd0b34d6e254cf`. The full derivation, source snapshot, exact arithmetic checks and limitations are retained there.

For the actual independent radial coordinates
\[
b_i=\sqrt{(d+2)/2}\,(1-d/S_i),\qquad S_i\sim\chi_d^2,\quad d\ge16,
\]
let \(L\ne0\) be deterministic, let \(T\) be the Frobenius isometry onto traceless symmetric matrices, and put
\[
B_i=T(Le_i),\quad C=\sum_i B_i^2,\quad
M_0=\mathbb E\,T(Lb),\quad
\mathcal E=\mathbb E\|Lb\|^2.
\]
The complete proof establishes
\[
K_L=\frac{d\{\operatorname{tr}(C^2)+\operatorname{tr}(M_0^4)\}}{\mathcal E^2}=O(1)
\quad\Longrightarrow\quad
\operatorname{tr}\!\left[T\!\left(\frac{Lb}{\|Lb\|}\right)^4\right]=O_P(d^{-1}),
\]
with no effective-rank lower bound. More precisely the probability at level \(R/d\) is at most \(\min\{1,C_*(K_L/R)^{1/7}\}\). The argument proves exact radial Fisher information \(1+6/d\), a uniform small-ball estimate, and a fourth-cumulant contraction bound. It also applies conditionally to a random \(L\) independent of \(b\), with \(K_L=O_P(1)\).

A separate explicit deterministic invertible family shows that centered contraction alone does not suffice for the uncentered source: its mean direction can force a normalized fourth trace tending to \(1/2\). This family does not satisfy the actual harmonic design's row constraints and is not a counterexample to P20.

**Remaining task:** prove the displayed weighted contraction and mean-direction condition for the actual harmonic inverse or the required selected-bottom map. The report does not prove expectation-level \(O(1/d)\), the remaining spectral/secular and graph-factor steps, or the full fixed-\(t\) hard-edge law.

The [complete report](https://github.com/yspennstate/math-open-problems/blob/master/proofnet24/portfolio-completion/runs/2026-09-14/2026-09-14_20-23-26/agents/105.md) compares the P20 and later P22 source reports at immutable baseline `4c708781adf206a4d28b7e3027365ba2b735c12d`. Its [exact check source](https://github.com/yspennstate/math-open-problems/blob/master/proofnet24/portfolio-completion/runs/2026-09-14/2026-09-14_20-23-26/computations/105_inverse_source_exact.js) and [recorded output](https://github.com/yspennstate/math-open-problems/blob/master/proofnet24/portfolio-completion/runs/2026-09-14/2026-09-14_20-23-26/computations/105_inverse_source_exact_output.json) contain 134 exact arithmetic checks. The probability theorem is established analytically, not by those finite checks. Historical priority and formal verification are not claimed.
