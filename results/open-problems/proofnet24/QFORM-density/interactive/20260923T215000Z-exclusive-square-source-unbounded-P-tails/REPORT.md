# Canonical rank three with an independent square source

**Status:** Proved sufficient case for the exact canonical original-product problem. This estimate allows arbitrary fragmented and infinite-variance original-coordinate laws, including the hub and the entire third light projection. It is not the unrestricted mixed-sign rank-three theorem.

## Theorem

Let \(H\) and \((X_i)_{i\in J}\) be mutually independent real variables, each with a probability density bounded by one. Let \(\ell,v,p\in\mathbb R^J\) be orthonormal, \(L=\ell\cdot X\), \(V=v\cdot X\), and \(P=p\cdot X\). Let \(S\subset J\) satisfy
\[
 \ell_i=p_i=0\quad(i\in S),\qquad
 c=\bigl(\sum_{i\in S}v_i^2\bigr)^{1/2}>0.
\]
For arbitrary \(\varepsilon,\beta\in\mathbb R\) with \(|\beta|\le\varepsilon^2\), put
\[
 Q=2HL+\beta L^2+V^2+2\varepsilon LP.
\]
Then \(Q\) has a bounded density and
\[
 \|p_Q\|_\infty\le {\sqrt2\over c}(1+G_2),\qquad
 G_2=\max\{10^6,44\cdot10^{15/2}\}.
 \tag{1}
\]
The constant is independent of the number of coordinates, all individual support diameters and variances, \(\beta\), and \(\varepsilon\). The bound is uniform in the output level. In particular, if \(c\ge c_0>0\), this is a dimension- and law-uniform all-level result.

## Proof

Set \(T=J\setminus S\), \(V_S=\sum_{i\in S}v_iX_i\), \(V_T=\sum_{i\in T}v_iX_i\), and
\[
 Q_\star=2HL+\beta L^2+2\varepsilon LP.
\]
The random variable \(V_S\) is independent of \((H,X_T)\). By the one-dimensional projection-density bound for a product of independent density-one inputs, \(V_S\) has a density \(g\) bounded by \(\sqrt2/c\). Because \(\ell\) and \(p\) vanish on \(S\), the random variables \(L,P,Q_\star,V_T\) are measurable with respect to \((H,X_T)\).

Conditional on \((H,X_T)\), \(Q=Q_\star+(V_S+V_T)^2\). The elementary two-branch square change of variables therefore bounds its conditional density at \(s\) by
\[
 {\sqrt2\over c}(s-Q_\star)^{-1/2}\mathbf1_{\{s>Q_\star\}}.
 \tag{2}
\]
The shift \(V_T\) is completely unrestricted and may depend on \(Q_\star\).

The quadratic matrix of \(Q_\star\) acts on the three orthonormal coefficient directions \((H,L,P)\) as
\[
 B=\begin{pmatrix}0&1&0\\1&\beta&\varepsilon\\0&\varepsilon&0\end{pmatrix}.
\]
Its null direction is proportional to \((-\varepsilon,0,1)\). On its orthogonal complement, it is orthogonally equivalent to \(\begin{psmallmatrix}0&\sqrt{1+\varepsilon^2}\\\sqrt{1+\varepsilon^2}&\beta\end{psmallmatrix}\). Consequently its two nonzero eigenvalues have absolute values at least one exactly when
\[
 {\sqrt{\beta^2+4(1+\varepsilon^2)}-|\beta|\over2}\ge1
 \quad\Longleftrightarrow\quad |\beta|\le\varepsilon^2.
\]
The already-proved global two-eigenvalue truncated half-power theorem applies to \(Q_\star\), with arbitrary original-coordinate product laws and arbitrary affine shifts, and gives
\[
 \sup_s\mathbb E\bigl[|s-Q_\star|^{-1/2};\ |s-Q_\star|\le1\bigr]\le G_2.
 \tag{3}
\]
Indeed, the no-\(10^{-15}\)-pivot branch gives \(10^6\), while the pivot branch gives \(44\cdot10^{15/2}\). Since \((s-Q_\star)^{-1/2}\le1\) when \(s-Q_\star>1\), averaging (2) and applying (3) proves (1). The quadratic \(Q_\star\) has no atoms because it is a nonconstant polynomial of a vector with an absolutely continuous product law; thus the value at \(s=Q_\star\) is irrelevant. The same argument may be stated directly for interval probabilities to avoid choosing pointwise density versions.

## Independent tail-core variant

There is a second elementary way to remove arbitrary fragmented input tails. Partition the light source originals into a set \(T\) of unrestricted laws and a set \(R\) of laws with variances at most \(V_0\). Suppose \(R\) has a physical partition into independent banks \(A,B\) such that each restricted \(3\times3\) Gram matrix of \((\ell,v,p)\) is at least \(cI_3\), with \(c>0\). Condition on all variables in \(T\). They translate the total \((L,V,P)\), and may create arbitrarily large affine terms when the square is expanded, but the already-proved two-bank all-\(\beta\) R\'enyi-tail theorem is uniform in arbitrary bank means: simply assign the three translated constants to bank \(A\). Each bank projection has joint density \(\le Cc^{-3/2}\); its \(P\)-variance is \(\le V_0\). Hence that theorem yields
\[
 \|p_Q\|_\infty\le C'c^{-1}(1+V_0)^{1/3}.
 \tag{4}
\]
This conclusion needs neither a variance bound nor a finite support bound for any variable in \(T\). It is a genuinely scoped statement: an arbitrary set \(T\) can destroy the entire full-rank bounded-variance core, so (4) does not settle the general canonical problem.

## Scope and provenance

The independence of \(V_S\) from \(Q_\star\) in (1) uses exact coordinate zeros of both \(\ell\) and \(p\) on \(S\). An orthogonal spectral rotation of all inputs does not provide that independence. Likewise, (4) explicitly needs a full-rank finite-variance physical source core. No extension to the overlapping-source, unbounded-tail case is asserted.

The rank-two half-power theorem used in (3) is `lower_levels.tex`, Theorem `lower:two`, together with `structure.tex`, Lemma `lem:pivot-half`, in the manuscript at commit d6f59993e85da91da39942ae96d92481abbaf541. The all-\(\beta\) two-bank result used for (4) is the archived `20260923T205630Z-finite-p-support-fourier/ALL_BETA_ADDENDUM.md`; its bounded-variance consequence was checked in `CANONICAL_BOUNDED_VARIANCE_P_TAILS.md`.
