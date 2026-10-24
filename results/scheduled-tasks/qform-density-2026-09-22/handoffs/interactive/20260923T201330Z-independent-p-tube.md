# QFORM handoff: affine-uniform dyadic tube estimate with independent \(P\)

**Status:** proved for the independent-\(P\) subclass; general product-correlated \(P\) remains open.

**Full proof:** https://github.com/yspennstate/math-open-problems/blob/master/proofnet24/QFORM-density/interactive/20260923T201330Z-independent-p-tube/REPORT.md

Let \(F(l,v)=-c-dl-(\gamma+v^2)/(2l)\), \(r\leq|l|\leq2r\), \(|\gamma|\geq1\). If \(P\) is independent of \((L,V)\), \(f_P\leq1\), and the joint \((L,V)\) density is \(\leq M\), then for every \(q>2\),
\[
\Pr\{|P-F(L,V)|\leq a,\ r\leq|L|\leq2r\}
 \leq C_q M a r^{2-1/q}.
\]
This gives the requested gain \(\alpha=1-1/q\) for any \(1/2<\alpha<1\), both signs of \(\gamma\), uniformly in affine shear \(c,d\). No \(V\)-interval restriction is needed. For \(\gamma>0\), an explicit quadratic-root argument gives the endpoint \(160M a r^2/\sqrt\gamma\).

**Key proof mechanism:** The Lebesgue pushforward density \(m\) of \(F\) over \(r\leq|l|\leq2r\), \(v\in\mathbb R\), obeys \(\|m\|_q\leq C_q r^{2-1/q}\). After Gaussian cutoff in \(v\), its Fourier transform is a Fresnel amplitude integral over \(l\). The trivial bound is \(Cr^{3/2}|t|^{-1/2}\). Weighted van der Corput gives \(Cr^2/|t|\), because the phase has \(|\phi''(l)|=|t\gamma|/|l|^3\); affine \(d\) disappears. Splitting at \(|t|=r\), Hausdorff–Young, and monotone cutoff removal prove the \(L^q\) estimate. Hölder against independent \(f_P\) gives linear \(a\).

**Scope:** Compatible with two-bank Gram nondegeneracy when each bank has separate originals for \(P\) and \((L,V)\); does not cover correlated \(P\) in a general diffuse frame. Any attempted extension must replace the independent-\(P\) Hölder step with a product-specific correlated-incidence bound. The earlier dependent-light fake prevents replacing this with a generic 3D projection cap.


**Affine-regression extension (report commit 25aa9185e2eecc92bad1b12ab3a163a8127d6f0d):** The same conclusions hold with an extra density-cap factor \(K\) if \(P=\alpha L+\beta V+Z\), \(Z\) is independent of \((L,V)\), \(f_Z\leq K\). Shear \(V'=V+\beta L\) (Jacobian one) and replace \(d\) by \(d+\alpha-\beta^2/2\). In particular, jointly Gaussian projections with covariance bounded below admit such a Gaussian regression residual. No analogous independent residual is known for arbitrary fragmented product projections.


**Sharp logarithmic endpoint (report commits 7feb1c4b20bb05f66a5e43e83763193f9ef28b00 and ceb088054fe5c9e2cbbe9044a40db2ade54964a8):** Tracking \(\|m\|_q\leq Cq r^{2-1/q}\), \(q\geq3\), and choosing \(q=\log(1/r)\) gives \(P(E_{r,a})\leq C M a r^2(1+\log_+(1/r))\), both signs of \(\gamma\). The log is necessary for \(\gamma=-1\) even for independent cap-one axes: set \(l_0=3r/2\), \(d=-1/(2l_0^2)\), \(c=1/l_0\); then \(F(l,v)=((l-l_0)^2/l_0^2-v^2)/(2l)\). Taking \(L\) density one on \([r,2r]\cup[2,3-r]\) and \(V,P\) uniform \([-1/2,1/2]\) gives \(P(E_{r,a})\geq3ar^2[1+\log(1/(32r))]\) for \(r<1/32,\ a\leq1/4\). The elliptic \(\gamma>0\) sign has log-free endpoint.
