# Twisted Wiener surrogate falsified by a dependent light law

**2026-09-23. Rigorous scope:** This disproves an abstract replacement for the genuine-product twisted Wiener lemma; it does **not** refute the QFORM conjecture or exhibit a product-projection light law.

Full proof, including every projection-density orientation and every affine two-dimensional Fourier plane:
https://github.com/yspennstate/math-open-problems/blob/master/proofnet24/QFORM-density/interactive/20260923T195500Z-twisted-wiener-plane-surrogate-falsifier/REPORT.md
(commit c57c9c8c312e6459e2b5f5240a5ef4b00e2511b3).

Construction: for smooth compact probability h, k→∞, B=k⁴,
\[
 g_k(l,v,p)=h(l)h(v)\frac1k\sum_{j=1}^k h(p-kl-jB).
\]
This dependent law is a mixture of k thin sheared tubes. Its twisted Wiener \(J_1=\int_{\mathbb R^2}|\int g_k e^{i(yl+zv+lp)}|\) is ≥c√k: stationary-phase chirps on each tube yield √k Fourier L1, with B-separated frequency packets. Every 1D/2D/3D orthogonal projection has a dimension-independent density cap. Its full 3D Fourier L1 is O(1). More subtly, supremum of Fourier L1 over **every affine 2D frequency plane** is O(log k); the proof changes η→a=η+kξ and uses the normalized Dirichlet kernel average O(log k/k), split by whether transformed plane normal's a-component exceeds1/k.

Dilate by a fixed constant to meet the exact 2^{d/2} LPP-type caps, weight the bad law by α_k=1/(1+log(k+1)), and add a broad Gaussian. The resulting probability laws have all projection-density caps, full 3D Wiener, and all-affine-2D-plane Wiener bounded by constants independent of k, yet J_1≥c√k/log k−O(1)→∞.

**Implication:** A proof of the genuine-product linear twisted Wiener estimate must use more than any combination of these marginal/projection/Wiener numerical bounds. The categorical tube label is dependent on L; no representation as an orthogonal projection of independent cap-one inputs is provided. The earlier six-input P-code falsifier refuted only an even stronger mixed-conditional slice norm, not this unconditioned product estimate.
