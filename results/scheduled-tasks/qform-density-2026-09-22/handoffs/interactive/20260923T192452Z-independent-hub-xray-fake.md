# QFORM interactive handoff: independent hub does not save projection-only leakage bridge

**Original independent-coordinate QFORM conjecture remains OPEN.** This is a counterexample only to an attempted intermediate theorem that replaces a genuine product light projection by an arbitrary dependent light law with the same numerical projection bounds.

**Canonical proof:** yspennstate/math-open-problems commit a850772af1824dd69d5063e3815d17a69645dcaf, path proofnet24/QFORM-density/interactive/20260923T192452Z-independent-hub-all-projections-fake/REPORT.md, verified blob a8c6c07c0d1a4e9c99e0b4f65081f0a23000fc6d.

There are H independent with cap-one density, and a *dependent* light triple (L,V,P) with joint cap<1 and every rotational orthogonal d-dimensional projection obeying \(\|p_{\pi_d Z}\|_\infty<2^{d/2}\) for d=1,2,3, such that
\[
Q=2HL+V^2+2LP
\]
has unbounded density at target **−1**. The quadratic matrix has eigenvalues \(\sqrt2,-\sqrt2,1,0\), hence \(s_3=1\).

Construction: positive \(a_k\) sum to 1 yet \(\sum a_k\log(1/a_k)=\infty\), and choose extremely separated centers \(c_k\). The independent hub has density 1 on intervals \([c_k-a_k/2,c_k+a_k/2]\). The light shell \(E_k\) has \(l\in[a_k,1]\), \(v\in[0,1]\), and \(p\) within \(a_k/2\) of \(-c_k-(1+v^2)/(2l)\). Give \(\bigcup E_k\) density 1/512 and fill the missing probability with a standard Gaussian. The kth matched hub/shell term contributes \([a_k/1024]\log(1/a_k)\) to the density at −1, so the output essential supremum diverges.

**Projection audit:** Each *individual* shell meets every line in length <142: on dyadic \(|p+c_k|\asymp R\), its quadratic shell polynomial has positive value at zero and sublevel size \(\lesssim a_k/R\); three-point interpolation gives section \(O(\sqrt{a_kR})\), and the dyadic sum is O(1). A line meeting several shells has light-coordinate slopes \(O(1/c_k)\) from superlacunary separation; each earlier shell then occupies at most \(2a_m\) in the p-coordinate. The union line bound is 160. Its plane-section area is at most \(160\sqrt2\) by foliation with a transverse coordinate inside the bounded (L,V) square. After Gaussian filler, 2D cap \(<0.472<2\), 1D cap \(<0.842<\sqrt2\), 3D cap \(<1<2\sqrt2\). The light law is a genuine probability.

**Scope:** This disproves the bridge “all low-dimensional light projection caps + independent physical H imply a uniform density for leakage.” It does not realize the light law as an orthonormal projection of independent original variables; it is **not** a product-law counterexample. Any proof of the original conjecture must use more than those caps, such as product-factorization information. The target −1 lies on the nonruled side of the indefinite ternary quadratic, consistent with positive-side ruled-line bounds.

**Integrity:** Changed-file allowlist is canonical mathematical report and this handoff. Both were manually checked for unrelated/private information. No automated privacy scanner or native learned-memory ingestion is claimed.