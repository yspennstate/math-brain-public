# Three-port Hessian lemma for an arbitrary weighted forest backbone

2 October 2026. Complete derived lemma and exact literal-graph checks. The
ordinary matroid log-concavity input is established prior work and is credited
explicitly. The argument was proposed independently in the parent research
thread and audited/rederived here. Historical novelty is unverified. This file
proves the scalar and matrix backbone constraints; the full matching negative
association corollary is owned by the separate matching proof.

## Statement

Let \(G\) be an arbitrary finite weighted multigraph, with three specified
port vertices \(1,2,3\). Its edge activities are nonnegative and its measure
assigns each unrooted forest the product of its edge activities. Loops are
never selected. Let \(v_0,v_{12},v_{13},v_{23},v_{123}\) be the total forest
weights according to the five induced port partitions: all separate, just the
indicated pair connected, or all connected. Put

\[
F=v_0+v_{12}+v_{13}+v_{23}+v_{123}>0,\qquad r=v_0,
\]

\[
A_{12}=r+v_{13}+v_{23},\quad
A_{13}=r+v_{12}+v_{23},\quad
A_{23}=r+v_{12}+v_{13},\qquad
\mathbf A=(A_{12},A_{13},A_{23})^T.
\]

Thus \(A_{ij}\) is the total weight of forests in which ports \(i,j\) are
disconnected. Write \(K=\mathbf1\mathbf1^T-I_3\). Then

\[
\boxed{\mathbf A\mathbf A^T-rF K\succeq0.}                 \tag{1}
\]

There is a quantitative strengthening. Let \(N=|E(G)|+3\) be the number of
edges of the augmented graph used below, including the three distinguished
new edges. Then

\[
\boxed{(N-1)\mathbf A\mathbf A^T-NrF K\succeq0.}           \tag{2}
\]

Edges of zero activity may be deleted before choosing \(N\), but this is not
required. Including loops in its count is harmless.

For arbitrary column factors \(b_1,b_2,b_3\geq0\), put

\[
B=b_1+b_2+b_3,\quad
M=A_{12}b_1b_2+A_{13}b_1b_3+A_{23}b_2b_3,\quad
J=r b_1b_2b_3.
\]

The corresponding scalar constraints are

\[
\boxed{M^2\geq2BJF,\qquad
M^2-2BJF\geq M^2/N.}                                  \tag{3}
\]

In particular the first inequality is strict whenever \(M>0\). These
conclusions also hold after any backbone-edge conditioning of positive
probability and after arbitrary nonnegative fields. Port identifications
caused by required-present edges are allowed. The degenerate cases \(r=0\),
\(J=0\), or \(M=0\) are included.

## 1. An exact hypothetical-triangle polynomial

Add three new distinguished edges between ports \(12,13,23\), with independent
activities \(z_{12},z_{13},z_{23}\). They are distinct edges even if a parallel
backbone edge already exists. Denote the ordinary forest partition sum of
this augmented graph by \(Z(\mathbf z)\).

For any backbone forest, one new edge \(ij\) can be selected exactly when
\(i,j\) are disconnected. Any two of the new edges form a two-edge path on
the three ports. They can both be selected exactly when **all three ports
are initially in distinct backbone components**. If any pair is already
connected, either one selected new edge closes that connection into a cycle,
or the selected two-edge path closes it. Conversely, with three different
components, the two new edges join them acyclically. Selecting all three
new edges always creates the distinguished triangle and is forbidden.

Consequently the full polynomial is exactly

\[
Z(\mathbf z)=F+\mathbf A^T\mathbf z
 +r(z_{12}z_{13}+z_{12}z_{23}+z_{13}z_{23}).               \tag{4}
\]

This is a literal deletion/contraction identity for unrooted forests. There
are no determinant root multiplicities, factorial coefficients, or cubic
term. Parallel edges cause no difficulty: selecting both parallel edges is
a cycle in the graphic matroid, exactly as in the literal forest test.

## 2. The precise prior log-concavity input

The established theorem is N. Anari, K. Liu, S. Oveis Gharan and C. Vinzant,
*Log-Concave Polynomials III: Mason's Ultra-Log-Concavity Conjecture for
Independent Sets of Matroids*, arXiv:1811.01600v1, 5 November 2018.
The primary PDF is [https://arxiv.org/pdf/1811.01600](https://arxiv.org/pdf/1811.01600).
Its Theorem 4.1 proves complete log-concavity of the homogeneous polynomial

\[
g_{\mathcal M}(y,z_1,\ldots,z_N)
 =\sum_{I\text{ independent}}y^{N-|I|}\prod_{i\in I}z_i.   \tag{5}
\]

The coefficients in this displayed formula are one. There is **no factorial
normalization**. Lemma 2.2 preserves complete log-concavity under affine maps
which send the nonnegative orthant into itself. In a graphic matroid,
independent edge sets are exactly unrooted forests. Setting \(y=1\), fixing
backbone coordinates at their activities, and leaving the three hypothetical
edge coordinates free therefore makes (5) exactly (4). We use only ordinary
log-concavity for (1), and log-concavity of the homogeneous polynomial for
(2). The prior theorem itself is not claimed as a new result here.

Since \(Z(0)=F>0\), its logarithm and Hessian are continuous in a full
neighborhood of zero. Log-concavity on positive \(\mathbf z\) implies by
continuity that

\[
\nabla^2\log Z(0)\preceq0.
\]

Using (4), \(\nabla Z(0)=\mathbf A\) and \(\nabla^2 Z(0)=rK\), so

\[
-F^2\nabla^2\log Z(0)=\mathbf A\mathbf A^T-rFK.
\]

This proves (1). In particular it is a **full three-direction Hessian
inequality**, not a claim that all of its off-diagonal entries are
nonnegative.

## 3. Homogeneous Euler identity gives strictness

Take the degree-\(N\) polynomial \(g=g_{\mathcal M}\) of the augmented graphic
matroid and evaluate at the vector \(a\) having dummy coordinate \(y=1\),
backbone coordinates their nonnegative activities, and hypothetical edge
coordinates zero. Let

\[
S=-\nabla^2\log g(a)\succeq0.
\]

The boundary value is justified by the same continuity argument because
\(g(a)=F>0\). Homogeneity gives Euler's identity
\(a^T\nabla\log g(a)=N\). Differentiating it gives

\[
S a=\nabla\log g(a),\qquad a^T S a=N.                     \tag{6}
\]

For any real three-vector \(x\), let \(h\) be zero on all other coordinates
and equal to \(x\) on the hypothetical edges. Then

\[
h^TSa=\frac{\mathbf A^Tx}{F},\qquad
h^TSh=\frac{x^T(\mathbf A\mathbf A^T-rFK)x}{F^2}.
\]

Cauchy–Schwarz for the positive semidefinite bilinear form \(u^TSv\), valid
also when \(S\) is singular, and (6) imply

\[
x^T(\mathbf A\mathbf A^T-rFK)x
 \geq\frac{(\mathbf A^Tx)^2}{N}.                           \tag{7}
\]

Multiplying (7) by \(N\) proves (2). This derivation establishes the precise
degree-dependent margin rather than assuming strictness of a general
log-concavity theorem.

For completeness, when \(r>0\), the matrix in (1) is positive definite.
Indeed a vector in its kernel must have \(\mathbf A^Tx=0\) by (7). Equation
\((\mathbf A\mathbf A^T-rFK)x=0\) then gives
\(x=\mathbf1(\mathbf1^Tx)\); summing its three coordinates forces
\(\mathbf1^Tx=0\), hence \(x=0\). When \(r=0\), (1) reduces to the rank-one
matrix \(\mathbf A\mathbf A^T\), and (7) remains valid.

## 4. The required matching-background cone

Choose

\[
x=(b_1b_2,b_1b_3,b_2b_3)^T.
\]

Then \(\mathbf A^Tx=M\), while direct multiplication gives

\[
x^TKx=2(b_1^2b_2b_3+b_1b_2^2b_3+b_1b_2b_3^2)
      =2B b_1b_2b_3.
\]

Applying (1) and (7) proves both parts of (3), without division by any
column factor or by \(r\). The formulas therefore include zero columns.
If \(M=0\), the left side is zero and nonnegativity forces \(BJ=0\);
there is no hidden nonzero denominator. If \(M>0\), (7) gives a positive
gap. In particular positive columns with \(r>0\) are strictly inside the
needed cone.

Two additional elementary bounds hold even for arbitrary nonnegative
frontier rows. Let \(e_2=b_1b_2+b_1b_3+b_2b_3\). Each forest permits at most
all three pair joins, and every all-separated forest permits all of them.
Thus

\[
r e_2\leq M\leq F e_2\leq FB^2/3,
\qquad BM\geq rBe_2\geq9r b_1b_2b_3=9J.                 \tag{8}
\]

The last bound follows from AM–GM applied to the six monomials \(b_i^2b_j\),
or by continuity if a column vanishes. Combining (3),(8) gives the actual
backbone constraints used in the separate matching forced-subset argument.

The missing factor two cannot be obtained merely by applying scalar
complete log-concavity to the one-apex polynomial
\(F(1+Bx)+Mx^2+Jx^3\): its first derivative yields only
\(M^2\geq\tfrac32BJF\). The hypothetical triangle removes the cubic term
and retains all three Hessian directions; that distinction is essential.

## 5. Conditioning and fields

Required-present backbone edges under a positive-probability conditioning
form an acyclic set. Contract them, delete required-absent edges, and retain
the remaining weighted graphic matroid. The fixed required-edge activity
product is a positive common factor in all partition coefficients. Removing
it leaves an ordinary forest partition on the contracted multigraph, so
the prior theorem applies again. Restoring the common factor multiplies
both sides of every matrix and scalar inequality by its square.

Some ports can now coincide. If any two do, \(r=0\), and corresponding
hypothetical edges may be loops or parallel edges. Nevertheless the literal
polynomial (4) remains valid: every two-edge hypothetical selection is
forbidden, while single-edge coefficients are the indicated disconnection
weights. The contraction graphic matroid includes these loops normally.
The proof and the zero-\(r\) formulas already cover this case. If all ports
coincide, \(\mathbf A=0\), so \(M=J=0\).

For the quantitative bound after conditioning, take \(N\) to be the number
of remaining edge elements plus the three hypothetical elements. The
normalizing fixed-edge constant has no logarithmic derivatives. Arbitrary
positive fields merely replace backbone activities. Nonnegative fields
are handled by the same theorem or by limits, provided the conditioned
event still has positive weight. This closure concerns actual conditioned
forest laws, not arbitrary reweighting of the five partition masses.

## 6. Literal exact verification and a preserved failed route

[`forest_three_port_hessian_lemma_k_exact.py`](forest_three_port_hessian_lemma_k_exact.py)
checks all 33864 unweighted simple backbones on three through six vertices.
For each complete labeled graph, it first tests every edge subset directly
for cycles, records its port partition, and then uses an exact subset zeta
transform to obtain the weights for **every** contained graph. For each
backbone it checks all principal minors of both the matrix in (1) and the
degree-sharpened matrix in (2), and checks (3),(8) at six nonnegative column
profiles. The checks use exact integers, not eigenvalue tolerances.

A different connectivity-DP route checks 106 weighted cases, including
parallel edges, loops, rational activities, required/absent conditioning,
and identifications of two or all ports. It enumerates the full augmented
graph by ordinary cycle rejection and compares all eight hypothetical-edge
configuration coefficients with (4). It does not invoke the matrix theorem
or a special three-port transfer formula to compute those coefficients.
All checks exited zero; the full record is
[`forest_three_port_hessian_lemma_k_exact_results.json`](forest_three_port_hessian_lemma_k_exact_results.json).

The arbitrary-row route really fails. For the formal row
\((v_0,v_{12},v_{13},v_{23},v_{123})=(1,0,0,0,1)\), take \(b=(1,1,1)\).
Then \(F=2,B=3,M=3,J=1\), and

\[
M^2-2BJF=9-12=-3.
\]

Its hypothetical Hessian matrix has diagonal entries one and off-diagonal
entries minus one; the all-ones quadratic form is \(-3\). It therefore
violates the proved matroid log-concavity constraint and cannot be an
actual weighted forest backbone row. The checker preserves this exact
counterexample. Nonnegativity of partition masses alone is insufficient.

Another tempting coefficientwise route would seek
\(A_{12}A_{13}\geq rF\), and its two symmetric counterparts. Those are the
zero-activity Rayleigh inequalities for two adjacent hypothetical edges.
The present proof does **not** establish these off-diagonal entry signs:
a PSD Hessian matrix is not entrywise nonnegative. It proves exactly the
quadratic combination needed for the matching cone. No general
adjacent-edge forest negative correlation is inferred.

## Scope

This is a full arbitrary-backbone three-port scalar/matrix lemma, derived
from established ordinary matroid log-concavity. It supplies the missing
actual-forest constraint for the separately written proportional-spoke
matching theorem. It does not prove negative association of arbitrary
backbone indicators, does not cover unrestricted marked positions or
arbitrary nonproportional spoke fields, and does not resolve the full
forest negative-correlation conjecture. Those scope limits are independent
of the exact finite tests above.
