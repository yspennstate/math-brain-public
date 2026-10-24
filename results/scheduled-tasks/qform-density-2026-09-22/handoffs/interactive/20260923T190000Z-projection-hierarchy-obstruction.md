# Interactive QFORM handoff: all marginal density caps still lose the two-sheet trace

**Full target:** OPEN. This is an interactive mathematical result, not any account's scheduled sign-in or learned-memory ingestion.

**Canonical report:** yspennstate/math-open-problems commit 2bf287d4d9a51864ea73ea4a3caa8438350514f7, path proofnet24/QFORM-density/interactive/20260923T190500Z-full-marginal-cap-shell/REPORT.md, verified blob 8124a47fed89a66fe606a7a081f2bae114844986.

**Proved scoped theorem:** For \(q(u,v,w)=2uv+w^2\), \(s_3(A_q)=1\), construct a dependent probability density \(g_\delta\) satisfying simultaneously the exact numerical Livshyts--Paouris--Pivovarov caps \(\|p_{\pi_EY}\|_\infty\le 2^{k/2}\) for **all** orthonormal projections \(E\) of dimensions \(k=1,2,3\), and even \(\|g_\delta\|_\infty<1\), while
\[
 \mathbb P(|q(Y)+1|\le\delta)\ge\delta\log(1/\delta)/1024,
 \quad \|p_{q(Y)}\|_\infty\ge\log(1/\delta)/2048.
\]
The explicit shell is \(E_\delta=\{1\le u\le\delta^{-1/2},\,0\le w\le1,\,|q(u,v,w)+1|\le\delta\}\), volume \((\delta/2)\log(1/\delta)\); use \(g_\delta=(1/512)\mathbf1_{E_\delta}+(1-|E_\delta|/512)h\), \(h\) standard three-dimensional Gaussian.

**Proof certificate:** All affine line intersections with \(E_\delta\) have length at most 64. Along a line with \(|d_u|\ge1/2\), \(q+1\) becomes a degree-two polynomial \(P(u)\) with \(P(0)=1+\beta^2\ge1\); three-point Lagrange interpolation yields \(u\)-sublevel measure \(\le\sqrt{48}\delta^{-1/2}\sqrt\delta<7\). Other directions have bounded \(v\)- or \(w\)-range. Every affine plane section has area at most \(3\cdot64=192\), by foliating through a direction \(r=(0,r_v,r_w)\). Thus the shell contributions to 1D and 2D projection peaks are at most \(192/512=3/8\) and \(64/512=1/8\); Gaussian contributions are at most \((2\pi)^{-1/2}\) and \((2\pi)^{-1}\). Joint peak is below \(1/512+(2\pi)^{-3/2}<1\).

**Relation to prior correction:** account01/B06's recorded \`QFORM-TWOSHEET-XRAY-ONLY-FALSE\` refuted use of the two-dimensional X-ray cap alone. This improves the information-loss obstruction by retaining 3D joint and 1D caps too, but gives logarithmic rather than \(1/\delta\) output blowup. It does not challenge a theorem that uses the *actual product projection representation*.

**Crucial warning:** The \(g_\delta\) coordinates are dependent; no product source for this three-dimensional law is supplied. This is NOT an admissible counterexample to the owner's conjecture and does not prove that an actual product projection can realize the shell. Do not promote it to a refutation of the full problem.

**Next proof debt:** Retain convolution of the original source-line measures, distributed minors, or another genuinely product-preserving invariant when paying the two-sheet trace and subsequent spectral tails. Do not replace the actual spectral marginal by an arbitrary joint density merely because its entire marginal-cap hierarchy satisfies the LPP numerical bounds.