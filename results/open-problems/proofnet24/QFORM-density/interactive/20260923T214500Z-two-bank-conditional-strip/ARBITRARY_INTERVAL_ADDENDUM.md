# Arbitrary single-interval length and convex-mixture hub corollary

This addendum extends the unit-interval hub corollary in [the two-bank conditional strip lemma](../20260923T214500Z-two-bank-conditional-strip/REPORT.md). All light assumptions and the planar bank density constants \(M_A,M_B\) are the same. In particular \(P_A,P_B\) may have arbitrary heavy tails and may overlap with \(L_A,V_A,L_B,V_B\) within their physical banks.

Suppose the independent hub \(H\) is uniform on **any** interval \(I\) of length \(D\ge1\). Its density is \(D^{-1}\mathbf1_I\), so it obeys the cap-one hypothesis. Let
\[
Q=2HL+\beta L^2+V^2+2\varepsilon LP.
\]
For fixed \(L=l\ne0\) and target \(s\), the conditional density formula is
\[
p_Q(s)=\mathbb E\left[\frac1{2D|L|}
\mathbf1_{\{(s-\beta L^2-V^2-2\varepsilon LP)/(2L)\in I\}}\right].
\]
The indicator restricts \(W=\beta l^2+V^2+2\varepsilon lP\) to an interval of length \(2D|l|\). The pointwise conditional slice estimate in the linked proof gives joint \(dl\)-mass at most \(C\sqrt{M_A M_B}\sqrt{D|l|}\,dl\). Hence the part \(0<|l|<1\) contributes at most
\[
\frac{C\sqrt{M_A M_B}}{\sqrt D}
 \int_{0<|l|<1}|l|^{-1/2}\,dl
\le C'\sqrt{M_A M_B}D^{-1/2}.
\]
The pointwise slice estimate remains valid when \(D|l|>1\); its upper bound may then exceed the actual slice mass, which is harmless. On \(|L|\ge1\) the hub density formula is at most \(1/(2D)\). Thus
\[
\|p_Q\|_\infty\le C'\sqrt{M_A M_B}D^{-1/2}+\frac1{2D}
\le C'\sqrt{M_A M_B}+\frac12,
\]
uniformly in \(D\ge1\), interval location, \(\beta,\varepsilon\), and all light laws.

Any cap-one hub law that is a convex mixture of uniform distributions on intervals of lengths at least one inherits the same uniform bound by conditioning on the mixture label, since the label is independent of the light originals. This includes mixtures with unbounded interval locations and lengths. It does **not** include every cap-one density: a disconnected cap-one density can place mass in components shorter than one and need not admit this representation.
