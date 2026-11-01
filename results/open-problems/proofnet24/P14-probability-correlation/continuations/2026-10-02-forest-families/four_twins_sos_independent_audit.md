# Independent audit of the four-twins third-coefficient theorem

Audit date: 2 October 2026. This audit did not use the author's transfer audit
implementation. Verdict: **the displayed theorem and the zero-spoke extension
pass**. No algebraic or combinatorial gap was found under the stated hypotheses.
This is a restricted result, not a solution of the general forest conjecture;
this audit does not certify novelty.

## Core contraction

For a fixed core forest F, each connected component is a tree. Contracting all
its edges preserves whether the remaining selected edges create a cycle.
Connecting a terminal twice to the same component creates a cycle, even if the
two attachments use different core vertices. Otherwise the attachment choices
are independent, and the sum of their weights is exactly the component sum
c_j. When some terminals have already been merged, choosing two terminals from
the same block likewise creates a cycle. Thus the four-terminal partition
transfer is exact. It does not presume that a core component consists of one
vertex, and it loses neither conductance factors nor multiplicities.

In particular the diagonal weight is 1+4x, even for partition shapes 211 or 22:
selecting one terminal gives four choices in total, while selecting two from
one block is forbidden. Every non-diagonal entry of the five-shape table checks
by selecting at most one representative of each block. The path weights through
this table give the stated A/P, B/P, and D/P formulas.

## Independent check of the coefficient table

Write h=sum(1/c_j), d=sum(c_j), and r for the number of hubs. Direct expansion
of the exact five-shape formulas, before expanding P, yields

\[
\begin{aligned}
A/P&={d^3\over4}\lambda^3
 +{3(6-r)d^2\over16}\lambda^2
 +{3d^2h+3(r^2-13r+38)d\over64}\lambda+O(1),\\
B/P&={d^2\over2}\lambda^2
 +{(11-2r)d\over8}\lambda
 +{r^2-12r+32\over32}+{dh\over16}+O(\lambda^{-1}),\\
D/P&=d\lambda+{4-r\over4}+{h\over16}\lambda^{-1}
 +O(\lambda^{-2}).
\end{aligned}
\]

These follow from t_j=c_j lambda/4-1/16+1/(64 c_j lambda)+...,
u_j=c_j lambda t_j, v_j=c_j^2 lambda^2 t_j. For example the cubic coefficient
of A/P is

\[
\frac14\sum_jc_j^3+\frac34\sum_{i\ne j}c_i c_j^2
 +\frac32\sum_{i<j<k}c_i c_j c_k=\frac{d^3}{4}.
\]

In the linear coefficient of A/P, the reciprocal terms combine as
3h(sum c_j^2+2 sum_{i<j}c_i c_j)/64=3d^2h/64, and the remaining
coefficient is 3(r^2-13r+38)d/64. Multiplication by

\[
P=4^r\Bigl(\prod_jc_j\Bigr)\lambda^r
\Bigl(1+q_1\lambda^{-1}+q_2\lambda^{-2}+O(\lambda^{-3})\Bigr).
\]

recovers every entry of the author's coefficient table. For one hub, the exact
identities A=(1+x)^4, B=(1+2x)(1+x)^2, D=(1+2x)^2 provide a separate check.

## Moment, degree, and normalization checks

The weighted rooted-forest determinant is det(L_H+4z D_a), since a component
chooses one root and the sum of root weights is 4z c_j. Hence nu is genuinely
normalized by W. The core factor lambda^(s-r) turns the leading powers of the
hub polynomials into s+3, s+2, and s+1 for A, B, and D, respectively. Therefore
the candidate Rayleigh powers are 2s+4, 2s+3, and 2s+2, as claimed.

The ratios satisfy beta=(alpha+delta)/2 and
alpha-delta=(7-r)/(2d). Independent simplification gives

\[
2b_2/b_0-a_2/a_0-d_2/d_0
={-r^2+15r-50\over16d^2}.
\]

The terms involving q_1, q_2, and h all cancel. After averaging, the quadratic
contribution is (7-E r)^2/(16d^2), so the remaining expression is exactly
(E r-1-Var r)/(16d^2). Multiplying W^2 a_0 d_0 gives the claimed prefactor
d^2 W^2/64. This also confirms H_0=H_1=0.

## Positivity and the adjugate formula

For positive a, conjugating by D_a^{-1/2} gives the probability generating
function product with p_i=4/(4+mu_i). The component count is consequently a
sum of independent Bernoulli variables, and E r-Var r=sum p_i^2. At least one
p_i is one, and any additional eigenvalue contributes a strictly positive
square. Thus the strictness claim for s>=2 holds even when H is disconnected.

The matrix Q=4 D_a^(1/2) M^{-1} D_a^(1/2) is symmetric positive definite,
has those eigenvalues, and fixes u=sqrt(a)/sqrt(d). Hence

\[
\|Q-uu^T\|_F^2=\operatorname{tr}(Q^2)-1.
\]

Multiplication by d^2 W^2/64 and substitution M^{-1}=adj(M)/W gives exactly
the author's ordered double sum. There is no missing factor of two: diagonal
terms occur once and off-diagonal terms occur twice.

For two core vertices of spoke weights a,b and core-edge conductance w,
M=[[w+4a,-w],[-w,w+4b]] and W=4w(a+b)+16ab. The three distinct square
arguments are 16b^2, 16a^2, and -16ab. The result simplifies to
4a^2b^2(a+b)^2, independently of w.

## Zero-spoke extension

Let a_v>=0, and assume that every connected component of H contains a vertex
with positive a_v. The quadratic form of M is a sum of the Laplacian energy
and 4 sum a_v x_v^2. Vanishing forces x to be constant on each component and
then zero on each component, so M is positive definite and d>0.

The original coefficients and the adjugate expression are polynomials in the
spoke and core weights. Replacing a by a+epsilon and taking epsilon down to
zero proves H_0=H_1=0 and the same H_2 identity. This is sufficient even though
the intermediate coefficient table contains 1/c_j, and the original
D_a^{-1/2} spectral representation is unavailable at zero weights.

Now Q is positive semidefinite of rank exactly |support(a)|, and Qu=u still
holds because M 1=4a. Therefore the Frobenius-square formula implies H_2>0
when at least two spoke weights are positive. If only one is positive, H has
one connected component under the support assumption. The two marked triangles
and the rest of the core meet only at that common hub. Forest weights factor
over these blocks, giving independence of the two marked indicators and a
Rayleigh polynomial identically zero.

This extension correctly allows additional twins to be regarded as zero-spoke
vertices of the core. In particular it includes K_{m,s} with two additional
matching edges within the m-side, for m>=4, s>=2. The extension does not make
any assertion about arbitrary edge pairs in that bipartite graph.

## Direct full-graph enumeration

The companion script `four_twins_sos_independent_audit.py` enumerates every
edge subset of the entire graph, rejects cycles directly by disjoint-set
connectivity, and sorts the accepted forest monomials by matching-edge
inclusion. It computes BC-AD without using hub transfers or core contractions.
It separately constructs M and computes its determinant and cofactors by a
recursive exact determinant. All weights use exact Fraction arithmetic.

Nine cases passed: one hub; two hubs without a core edge and with two different
core-edge weights; three hubs with empty, path, and triangular cores; and two
three-hub cases with zero spoke weights. The zero-spoke cases have support two
and support one, respectively, and confirm strictness and identically zero
Rayleigh difference in those respective cases. The complete polynomials and
coefficient results are in `four_twins_sos_independent_audit_results.json`.

## Restricted prior-art comparison

The primary source https://arxiv.org/html/2610.00549v1 proves positivity of the
first coefficient and, conditionally, the second. Its Theorem 4.8 characterizes
simultaneous equality; the immediately preceding discussion explicitly leaves
the third coefficient or the full Rayleigh difference to further investigation.
Its Example 4.11 places marked endpoints in four distinct join parts and obtains
a positive second coefficient. Our four-twin geometry has both marked matching
edges within one part and has zero second coefficient. These stated results do
not subsume the audited H_2 theorem. No broader novelty conclusion follows from
this comparison alone.
