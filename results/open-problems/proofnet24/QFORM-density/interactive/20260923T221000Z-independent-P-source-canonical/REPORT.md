# Canonical rank three when the third light projection is independently sourced

**Status:** Proved all-level theorem for an original-product physical support split. The third light projection may have arbitrary fragmented law and infinite variance. Its source must be disjoint from the joint source of the linear and square projections; a mere pure-P subsource does not meet this hypothesis.

Let \(H,X_1,\ldots,X_n\) be mutually independent real variables with density caps one. Let \(\ell,v,p\) be orthonormal and let \(L=\ell\cdot X\), \(V=v\cdot X\), \(P=p\cdot X\). Suppose \(\operatorname{supp}p\) is disjoint from \(\operatorname{supp}\ell\cup\operatorname{supp}v\). Then for arbitrary \(\beta,\varepsilon\in\mathbb R\), the canonical quadratic
\[
 Q=2HL+\beta L^2+V^2+2\varepsilon LP
\]
has \(\|p_Q\|_\infty\le\tfrac12+8\sqrt2\).

Indeed \(H'=H+\varepsilon P\) is independent of the planar projection \((L,V)\), and its density is at most one by convolution with the independent \(H\). The pair \((L,V)\) is an orthonormal two-dimensional projection of original independent cap-one sources, hence has joint density at most two. Apply the proved square-root-kernel lemma for \(2H'L+r(L)+V^2\), which gives \(\tfrac12+4\sqrt2K\) for any measurable \(r\) and planar cap \(K\); choose \(r(L)=\beta L^2\) and \(K=2\). This is uniform even though \(H'\) may have unbounded support and \(P\) has no moments.

The square-root-kernel lemma and its proof are in `proofnet24/QFORM-density/interactive/20260923T212000Z-exact-rank3-physical-coloop-zero-diagonal/REPORT.md`, at commit c8542016844451bfa5585e5e15a89ed84f1602cb. In the unresolved fully overlapping canonical case, \(P\) depends on the same physical originals as \((L,V)\), so \(H+\varepsilon P\) is not independent of their planar projection.
