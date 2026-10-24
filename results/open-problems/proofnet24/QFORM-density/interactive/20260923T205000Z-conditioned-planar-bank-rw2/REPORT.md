# A conditioned planar-bank RW2 theorem for genuine product inputs

**Scope.** This proves all-target restricted weak-L² for the displayed canonical form, and a density bound for that form with arbitrary original-coordinate affine terms. It permits arbitrary hub densities bounded by one. It includes genuinely overlapping light coordinates after conditioning, and gives a concrete bound for three light original coordinates. The bound depends on a robust planar bank, so it does not resolve the diffuse high-dimensional branch.

Let \(H\) have a probability density at most one. Let \(X=(X_i)_{i\in B\cup C}\) have independent probability densities at most one, independent of \(H\), and let \(L,V,P\) be linear forms in \(X\). Write \(L=L_B+L_C\), \(V=V_B+V_C\), \(P=P_B+P_C\). Assume

1. the pair \((L_B,V_B)\) has a joint density bounded by \(M\);
2. \(P_B=\alpha L_B+\eta V_B\) identically for some real \(\alpha,\eta\).

The law of \((L_C,V_C,P_C)\) is unrestricted. For
\[
 T_s(l,v,p)=\frac{s-v^2-\beta l^2}{2l}-\varepsilon p,\qquad
 \mu_{\rho,s}(E)=\mathbb E\!\left[
 \frac{\mathbf 1_{\{\rho\leq|L|\leq2\rho\}}}{2|L|}
 \mathbf 1_E(T_s(L,V,P))\right],
\]
the following holds uniformly in **all real** \(s,\beta,\varepsilon,\alpha,\eta\), all \(0<\rho\leq1/2\), and all finite-length measurable \(E\):
\[
 \boxed{\mu_{\rho,s}(E)
 \leq 4\sqrt2(\sqrt2-1)M\,\sqrt{\rho|E|}.} \tag{1}
\]
Consequently the density of
\[
 Q=2HL+\beta L^2+V^2+2\varepsilon LP
\]
obeys
\[
 \boxed{\|p_Q\|_\infty\leq \tfrac12+4\sqrt2\,M.} \tag{2}
\]
The usual density representative and essential supremum are intended. The condition \(s\geq0\) is **not** needed here.

## Proof

Condition on the entire block \(X_C\). Denote its realized contributions by \(l_0,v_0,p_0\). Then
\[
 P=\alpha L+\eta V+n_0,\qquad
 n_0=p_0-\alpha l_0-\eta v_0,
\]
while the conditional pair \((L,V)=(L_B+l_0,V_B+v_0)\) has density at most \(M\). Although \(n_0\) need not be independent of the unconditional pair \((L,V)\), it is constant under the conditioning.

For each fixed \(l\ne0\), completing the square in \(v\) gives
\[
 v^2+2\varepsilon l(\alpha l+\eta v+n_0)
 =(v+\varepsilon\eta l)^2+
 (2\varepsilon\alpha-\varepsilon^2\eta^2)l^2+
 2\varepsilon n_0 l.
\]
The condition \(T_s(l,v,\alpha l+\eta v+n_0)\in E\) therefore restricts the square \((v+\varepsilon\eta l)^2\) to a measurable set of length \(2|l||E|\). The one-dimensional square-root rearrangement bound
\[
 |\{v:v^2\in D\}|\leq2\sqrt{|D|}
\]
bounds the permitted \(v\)-length by \(2\sqrt{2|l||E|}\). Integrating the conditional density over the shell and including the weight \(1/(2|l|)\) yields
\[
 \mu_{\rho,s}(E\mid X_C)
 \leq M\sqrt{2|E|}\int_{\rho\leq|l|\leq2\rho}|l|^{-1/2}\,dl
 =4\sqrt2(\sqrt2-1)M\sqrt{\rho|E|}.
\]
Average in \(X_C\) to prove (1). For (2), integrate out \(H\), apply layer cake to its cap-one density on each shell, and sum \(\rho=2^{-j}\), \(j\geq1\). Since \(\sum_{j\geq1}2^{-j/2}=1/(\sqrt2-1)\), the small-\(|L|\) contribution is at most \(4\sqrt2M\). The contribution from \(|L|>1\) is at most \(1/2\).

## A physical two-coordinate criterion

If \(B=\{i,j\}\) and
\[
 d_{ij}=l_i v_j-l_j v_i\ne0,
\]
then the invertible map \((X_i,X_j)\mapsto(L_B,V_B)\) has density at most \(1/|d_{ij}|\). Since the two rows \((l_i,l_j)\), \((v_i,v_j)\) form a basis of \(\mathbb R^2\), \(P_B=\alpha L_B+\eta V_B\) for unique \(\alpha,\eta\). Thus
\[
 \|p_Q\|_\infty\leq\tfrac12+\frac{4\sqrt2}{|d_{ij}|}. \tag{3}
\]

For an orthonormal three-frame \((l,v,p)\) in \(\mathbb R^n\), Cauchy–Binet gives
\[
 \sum_{i<j}(l_i v_j-l_j v_i)^2=1.
\]
If \(n=3\), some pair has \(|d_{ij}|\geq1/\sqrt3\); hence **every** such three-input near-hub form, for arbitrary cap-one product laws and the displayed quadratic form, satisfies
\[
 \|p_Q\|_\infty\leq\tfrac12+4\sqrt6<10.3. \tag{4}
\]
For general \(n\), the same argument yields \(\tfrac12+4\sqrt{n(n-1)}\). This finite-dimensional estimate does not furnish a dimension-free bound when every physical pair minor is small. A larger bank can still give a dimension-free result if it satisfies assumptions 1–2 with universal \(M\).

## Arbitrary original-coordinate affine terms in the density theorem

The **density bounds (2)–(4)** remain valid after adding an arbitrary deterministic linear form \(b_HH+\sum_i b_iX_i\) and a constant. This assertion concerns output density; the unmodified target map \(T_s\) in (1) does not describe the extra affine terms.

Condition on \(X_C\). For a bank \(B\) of two physical coordinates with \(d_{ij}\ne0\), the linear form \(\sum_{i\in B}b_iX_i\) is some \(a_LL_B+a_VV_B\). The same observation applies to a larger bank whenever its added affine term belongs to the span of \(L_B,V_B\). With \(l_0,v_0,p_0\) fixed, write \(P=\alpha L+\eta V+n_0\) as in the proof. All terms depending on \(X_C\) are now constants or contribute linear terms in \(H,L,V\). The conditional output has the form
\[
 z^{\mathsf T}A z+d^{\mathsf T}z+c,\qquad
 z=(H,L,V)^{\mathsf T},\quad
 A=\begin{pmatrix}
 0&1&0\\
 1&\beta+2\varepsilon\alpha&\varepsilon\eta\\
 0&\varepsilon\eta&1
 \end{pmatrix}.
\]
Crucially, \(\det A=-1\), regardless of \(\beta,\varepsilon,\alpha,\eta\). Set \(z'=z+\tfrac12A^{-1}d\). Then
\[
 z^{\mathsf T}A z+d^{\mathsf T}z+c
 ={z'}^{\mathsf T}Az'+c-\tfrac14d^{\mathsf T}A^{-1}d.
\]
Conditional on \(X_C\), these are deterministic coordinate translations. Hence \(H'\) retains a density cap of one and remains independent of \((L',V')\); the latter retains its planar density cap \(M\). The translated quadratic is
\[
 2H'L'+(\beta+2\varepsilon\alpha)L'^2+{V'}^2
 +2\varepsilon\eta L'V',
\]
plus a constant. The square-root proof above applies with \(P'=V'\). Thus its conditional density is bounded by \(\tfrac12+4\sqrt2 M\), uniformly in the conditioned values; averaging over \(X_C\) proves the same unconditional bound. In particular, for exactly three light original coordinates and an orthonormal three-frame, the arbitrary-affine output density is at most \(\tfrac12+4\sqrt6\). A hub self-square term \(aH^2\) is outside this extension.

## Relation to previous reports

The [restricted weak-L² target](https://github.com/yspennstate/math-open-problems/blob/62f9d598de628104d39ed19a9851b60f6eccded5/proofnet24/QFORM-density/interactive/20260923T204500Z-restricted-weak-l2-hub-target/REPORT.md) proved the case \(P=\alpha L+\eta V+N\) with \(N\) independent of \((L,V)\). The present conditioning proof permits arbitrary correlations in the residual block \(C\). The [positive-level RW2 theorem](https://github.com/yspennstate/math-open-problems/blob/af7be62ab5fdd74d2dcd8d9796cb099da0ac21ae/proofnet24/QFORM-density/interactive/20260923T204700Z-positive-level-rw2/REPORT.md) instead handles arbitrary dependent triples at \(s\geq0\) using only planar projection caps.