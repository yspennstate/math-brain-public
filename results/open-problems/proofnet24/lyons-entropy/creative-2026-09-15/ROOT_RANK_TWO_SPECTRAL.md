# Full spectral concavity on every rank-two commuting square

Root creative proof, 2026-09-15. This extends the equal-modulus restriction in C069 to arbitrary orthonormal eigenvectors. It uses the completed two-trial weighted entropy theorem in C075, and does not establish general Lyons concavity or historical priority.

## Theorem

For arbitrary fixed orthonormal vectors \(u,v\in\mathbb C^n\), the function
\[
(p,q)\longmapsto H(P_{p uu^*+q vv^*})
\]
is jointly concave on the whole square \([0,1]^2\). There is no equality-of-moduli hypothesis. Complementary kernels \(I-puu^*-qvv^*\) have the same conclusion. Direct sums with independent coordinate blocks preserve it.

The two varying eigenvectors are fixed. General varying eigenvectors, an arbitrary nonzero projection background, and arbitrary Hermitian perturbations at these bases are not covered.

## 1. Exact atom and entropy decomposition

Put
\[
m_i=|u_i|^2,\quad n_i=|v_i|^2,\quad
r_{ij}=|u_i v_j-u_j v_i|^2\quad(i<j).
\]
Here \(m,n\) are probability laws, \(r\) is a probability law on unordered pairs, and
\[
\sum_{j\ne i}r_{ij}=m_i+n_i.
\]
Write \(a=p(1-q)\), \(b=q(1-p)\), \(f_0=(1-p)(1-q)\), \(f_1=a+b\), \(f_2=pq\). The atoms are exactly
\[
P(\varnothing)=f_0,\qquad P(\{i\})=a m_i+b n_i,\qquad
P(\{i,j\})=pq\,r_{ij}.
\]
This is the standard spectral Bernoulli/projection expansion, or follows directly from inclusion determinants.

For \(a,b>0\), define the homogeneous Jensen-Shannon perspective
\[
G(a,b)=(a+b)H\left(\frac{am+bn}{a+b}\right)-aH(m)-bH(n).
\]
Let \(F=H(\operatorname{Bern}(p)+\operatorname{Bern}(q))\) and
\(\beta=H(m)+H(n)-H(r)\). Conditioning on the cardinality gives the exact identity
\[
\boxed{H(P_K)=F-\beta pq+pH(m)+qH(n)+G(a,b).}\tag{1}
\]

## 2. A dimension-independent projection entropy bound

We prove
\[
\boxed{0\le\beta\le2\log2.}\tag{2}
\]

For the lower bound, an unordered pair with law \(r\) can be oriented so that its first-coordinate law is \(m\), and its second-coordinate law is \(n\). Here is a complete feasibility justification. Allocate the mass \(r_{ij}\) of each edge to its two endpoints, prescribing endpoint totals \(m_i\). The finite max-flow/min-cut criterion is
\[
\sum_{\{i,j\}\subset S}r_{ij}\le m(S)\quad\text{for every }S.
\]
Indeed an edge node supplies its fixed mass and is connected only to its two endpoint nodes; taking complements gives the equivalent upper inequalities for incident mass. The required inequality holds because Cauchy-Binet gives
\[
\sum_{\{i,j\}\subset S}r_{ij}
=\|u_S\|^2\|v_S\|^2-|\langle u_S,v_S\rangle|^2
\le m(S)n(S)\le m(S).
\]
A feasible flow therefore specifies an ordered law \(Q\) with \(Q_{ij}+Q_{ji}=r_{ij}\) and first marginal \(m\). Its second marginal is \(n\), by the displayed degree identity. Thus
\(H(r)\le H(Q)\le H(m)+H(n)\), proving \(\beta\ge0\).

For the upper bound, orient the pair fairly instead, giving
\(\widetilde Q_{ij}=r_{ij}/2\) and both marginals \(s=(m+n)/2\).
Cauchy-Schwarz on the two-vectors \((u_i,v_i)\), \((u_j,v_j)\) gives
\[
r_{ij}\le(m_i+n_i)(m_j+n_j)=4s_i s_j.
\]
Hence \(\widetilde Q\le2s\otimes s\) pointwise, and
\[
0\le D(\widetilde Q\Vert s\otimes s)\le\log2.
\]
Since \(H(\widetilde Q)=H(r)+\log2\), this proves
\(H(r)\ge2H(s)-2\log2\ge H(m)+H(n)-2\log2\).
Zero coordinates have no mass and cause no exception. This completes (2).

## 3. All same-sign spectral directions

The ordinary two-trial count entropy \(F\) is jointly concave, as proved in C075 (its \(\theta=0\) case, with the explicitly cited Hillion-Johnson input). Along slopes \(\alpha,\zeta\) of the same sign, the lower bound in (2) gives
\[
D^2(F-\beta pq)=F''-2\beta\alpha\zeta\le0.
\]
Only \(\beta\ge0\) is needed here; the upper bound \(2\log2\) is a separate proved refinement. One can alternatively use C075's stronger weighted theorem to show \(F-\beta pq\) is concave in every direction, but that extra conclusion is unnecessary for this sign split.

The function \(G\) is concave in \((a,b)\): it is the concave entropy perspective minus linear terms. Moreover,
\[
G_a=D\left(m\middle\Vert\frac{am+bn}{a+b}\right)\ge0,\qquad
G_b=D\left(n\middle\Vert\frac{am+bn}{a+b}\right)\ge0.
\]
Along an affine spectral direction with slopes \(\alpha,\zeta\), one has
\(a''=b''=-2\alpha\zeta\). Therefore
\[
G''=(a',b')\,\nabla^2G\,(a',b')^T
-2\alpha\zeta(G_a+G_b)\le0
\quad\text{if }\alpha\zeta\ge0.
\]
Combining this with (1) proves nonpositive entropy curvature in every same-sign direction, including zero slopes.

## 4. All opposite-sign spectral directions

This sign can be proved directly without extending a frozen logarithm to impossible higher-cardinality atoms. Work at \(0<p,q<1\) on the fixed positive support. The atom acceleration is
\[
p''_{\bullet}
=2\alpha\zeta\sum_{i<j}r_{ij}
(\delta_\varnothing+\delta_{\{i,j\}}-\delta_{\{i\}}-\delta_{\{j\}}).
\]
Let \(p_i=am_i+bn_i\), \(p_{ij}=pq r_{ij}\). For every pair with \(r_{ij}>0\),
\[
\begin{aligned}
p_i p_j-p_\varnothing p_{ij}
&=a^2m_i m_j+b^2n_i n_j
+2ab\,\Re(u_i\overline v_i\,\overline u_j v_j)\\
&=|a u_i\overline u_j+b v_i\overline v_j|^2\ge0.
\end{aligned}
\]
Consequently the exact entropy Hessian is
\[
\boxed{
H''=-\sum_S\frac{(p'_S)^2}{p_S}
+2\alpha\zeta\sum_{i<j:r_{ij}>0}
r_{ij}\log\frac{p_i p_j}{p_\varnothing p_{ij}}\le0
\quad\text{when }\alpha\zeta\le0.}\tag{3}
\]
All logarithms here are finite. This is the rank-zero-background diamond sign written explicitly.

Every real direction has either sign of \(\alpha\zeta\), so Sections 3 and 4 establish a negative semidefinite two-parameter Hessian throughout the open square. Integrating along segments and using continuity of finite Shannon entropy gives the entire closed-square theorem.

## 5. Exact unequal-modulus example

Take
\[
u=(1,2,2)/3,\qquad v=(2,-2,1)/3.
\]
Their squared coordinate laws differ:
\(m=(1,4,4)/9\), \(n=(4,4,1)/9\), while
\((r_{12},r_{13},r_{23})=(4,1,4)/9\).
At \(p=1/4,q=3/4\), the seven positive atoms, in order
\(\varnothing,1,2,3,12,13,23\), are
\[
(27,37,40,13,12,3,12)/144.
\]
For the same-sign direction \((p',q')=(1,1)\), their first derivatives are
\((-1,0,0,0,4/9,1/9,4/9)\); their second derivatives are
\((2,-10/9,-16/9,-10/9,8/9,2/9,8/9)\).
Their sums are respectively one, zero, and zero. The exact Hessian formula is reproducible from these rational tables and natural logarithms. The global proof above, not a pointwise computation, establishes its sign on every spectral segment.

This example is outside C069's equal-modulus hypothesis. The result is a new extension within this campaign; no claim of literature-wide priority or a full ambient-Hermitian Hessian theorem is made. C069 supplied the equal-modulus count-mixture idea, C075 the weighted count theorem, and the root adds the orientation entropy bound and same-sign Jensen-Shannon compensation.
