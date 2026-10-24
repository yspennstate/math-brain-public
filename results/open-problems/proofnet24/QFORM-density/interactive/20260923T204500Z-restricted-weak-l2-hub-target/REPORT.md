# A restricted weak-\(L^2\) target for the central one-hub branch

**Scope.** This is a sufficient estimate and a proved special case, not a proof of the full quadratic-form density conjecture. The general overlapping-leakage estimate below remains open for original-product light variables.

Let \(H\) have an arbitrary Lebesgue density \(f_H\leq1\), let \(Y=(L,V,P)\) be independent of \(H\), and consider
\[
Q=2HL+\beta L^2+V^2+2\varepsilon LP.
\]
For a target \(s\), \(0<r\leq1/2\), and a measurable \(E\subset\mathbb R\), define
\[
T_s(l,v,p)=\frac{s-v^2-\beta l^2}{2l}-\varepsilon p,\qquad
\mu_{r,s}(E)
 =\mathbb E\!\left[
 \frac{\mathbf1_{\{r\leq |L|\leq2r\}}}{2|L|}
 \mathbf1_E(T_s(L,V,P))\right].
\]
The formula obtained by integrating out \(H\) is
\[
p_Q(s)=\mathbb E\!\left[
 \frac{f_H(T_s(L,V,P))}{2|L|}\right]
\]
for almost every \(s\), interpreted by monotone limits across the dyadic \(L\)-shells. The contribution from \(|L|>1\) is at most \(1/2\).

## Sufficient restricted weak-\(L^2\) estimate

If, uniformly in \(s,\beta,\varepsilon,r\) and in every measurable \(E\) of finite length,
\[
\tag{RW2}
\mu_{r,s}(E)\leq C\sqrt{r\,|E|},
\]
then the dyadic \(|L|\leq1\) contribution to \(p_Q(s)\) is at most
\[
C\sum_{j\geq1}2^{-j/2}<2.415C.
\]
Indeed, layer cake and Cauchy--Schwarz give
\[
\int f_H\,d\mu_{r,s}
 =\int_0^1\mu_{r,s}(\{f_H>t\})\,dt
 \leq C\sqrt r\int_0^1|\{f_H>t\}|^{1/2}dt
 \leq C\sqrt r,
\]
because \(\int_0^1|\{f_H>t\}|dt=\int f_H=1\). Thus (RW2) would prove a uniform density bound without any support or regularity assumption on \(H\). This avoids the known failure of the absolute Fourier norm \(\int|\widehat f_H(t)|/\sqrt{|t|}\,dt\).

Equivalently, before the \(1/(2|L|)\) weight, the target is
\[
\Pr(r\leq|L|\leq2r,\ T_s(L,V,P)\in E)
 \leq 4C\,r^{3/2}\sqrt{|E|}.
\]

## Proved case: independent transverse leakage

Assume the pair \((L,V)\) has joint density at most \(M\), and
\[
P=\alpha L+\eta V+N
\]
where \(N\) is independent of \((L,V)\). No density, support, or moment assumption on \(N\) is needed. Then (RW2) holds with \(C=4M\) (a loose elementary constant), uniformly in \(s,\beta,\varepsilon,\alpha,\eta\).

To prove it, first condition on \(N=n\). Completing the square gives
\[
v^2+2\varepsilon\eta lv
 =(v+\varepsilon\eta l)^2-\varepsilon^2\eta^2l^2.
\]
For fixed \(l\ne0\), the condition \(T_s(l,v,\alpha l+\eta v+n)\in E\) restricts \((v+\varepsilon\eta l)^2\) to a measurable set of length at most \(2|l||E|\). The elementary square-root rearrangement bound
\[
|\{v:v^2\in B\}|\leq2\sqrt{|B|}
\]
therefore bounds the permitted \(v\)-length by \(2\sqrt{2|l||E|}\), independently of every translation. Using \(g_{L,V}\leq M\), and integrating over both signs of \(l\in[r,2r]\),
\[
\mu_{r,s}(E)
 \leq M\sqrt{2|E|}\int_{r\leq|l|\leq2r}|l|^{-1/2}dl
 =4M\sqrt2(\sqrt2-1)\sqrt{r|E|}
 < 2.35M\sqrt{r|E|}.
\]
Averaging in \(N\) proves the claim. This contains \(\varepsilon=0\) with no assumption on \(P\). It also covers disjoint original-coordinate supports for \(P\) and \((L,V)\), after a deterministic linear regression of \(P\) on \(L,V\).

## Open original-product case and projection-cap obstruction

The unresolved case has \(L,V,P\) as overlapping linear images of independent original coordinates with densities at most one. Product provenance implies powerful projection caps and sometimes a split \(Y=Y_1+Y_2\) into independent banks with planar \((L,V)\) caps, but no proof of (RW2) for this overlap is known. The central negative targets \(s\in(-1,0)\), a rough \(H\), and \(\varepsilon\ne0\) are the acute regime. The current two-bank Fourier argument bounds outer \(|s|\geq1\); the ruled-line argument bounds \(s\geq0\) under all-plane caps.

The stronger-looking assumption that **every one- and two-dimensional orthogonal projection of \(Y\)** has a universal density cap is insufficient for (RW2). The dependent-light construction with independent cap-one \(H\) and those projection caps has unbounded output density at negative targets. If (RW2) held under projection caps alone, the preceding dyadic sum would bound that output, a contradiction. Thus an eventual proof must use the convolution/independent-coordinate provenance, or a stronger property derived from it.

Related source-pinned reports:
- Outer two-bank density: https://github.com/yspennstate/math-open-problems/blob/f0d3e4df297cf45c4f8a0298051cef186faf1de4/proofnet24/QFORM-density/interactive/20260923T203000Z-two-bank-outer-density/REPORT.md
- Negative-target dependent-light fake: https://github.com/yspennstate/math-open-problems/blob/ed1915681c630e9b26339c245f49056e908ee333/proofnet24/QFORM-density/interactive/20260923T203400Z-negative-target-projection-fake/REPORT.md
