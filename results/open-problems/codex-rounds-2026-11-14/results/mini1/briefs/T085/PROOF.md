# A finite obstruction to detecting Cayley gaps with subset actions

All cycles in this file use the points 1,2,3,4,5. Let

\[
s=(3\ 4\ 5),\qquad t=(1\ 5\ 4\ 2\ 3),\qquad
P=\frac{R_s+R_{s^{-1}}+R_t+R_{t^{-1}}}{4}.
\]

Here \(R_g\) denotes right translation on the generated group. The upper gap is \(1-\lambda_2(P)\), with eigenvalues in decreasing order and multiplicity. There are four distinct generators, so the multiset and simple graph conventions agree for this pair.

**Proposition.** The generated group is \(A_5\). Its Cayley gap is

\[
\gamma=\frac{3-\sqrt5}{8}=0.095491502812526\ldots.
\]

On the natural action on five points, the gap is

\[
\gamma_{\rm nat}=1-\frac{\sqrt5}{4}
=0.440983005625053\ldots.
\]

More generally, every nontrivial eigenvalue in the direct sum of the permutation actions on unordered k-subsets, for all \(0\leq k\leq5\), is less than \(3/4\). Thus those actions have upper gap greater than \(1/4\), and miss the Cayley bottleneck. The bottleneck occurs in the exterior square of the four-dimensional standard representation. The sign twist changes none of these actions, since all generators are even.

## The generated group

Both generators are even, so \(H=\langle s,t\rangle\leq A_5\). Their orders are 3 and 5. By Lagrange's theorem, \(|H|\) is divisible by 15 and divides 60, hence is 15, 30 or 60.

If \(|H|=15\), its number of Sylow 5-subgroups divides 3 and is congruent to 1 modulo 5. It is therefore 1. Conjugation by \(s\) acts on the normal cyclic group \(\langle t\rangle\) of order 5. Its automorphism group has order 4; an automorphism whose order divides 3 must be the identity. Consequently \(s\) and \(t\) would commute. They do not: \(st(1)=3\) while \(ts(1)=5\), with composition evaluated right to left.

If \(|H|=30\), it has index two and is normal in \(A_5\), giving a surjection \(A_5\to C_2\). Every 3-cycle must map to the identity. The 3-cycles generate \(A_5\): pair transpositions in an even-length transposition expression, and replace each pair by either the identity, a 3-cycle, or two 3-cycles. For disjoint transpositions one may use
\((a\ b)(c\ d)=(a\ c\ b)(a\ c\ d)\).
Thus the surjection would be trivial, a contradiction. It follows that \(|H|=60\), so \(H=A_5\).

## Exact finite matrix certificate

Write \(A=4P\). For any finite action on a set \(\Omega\), define its integer adjacency matrix by

\[
A_\Omega(u,v)=\sum_{g\in(s,s^{-1},t,t^{-1})}\mathbf1_{v=g(u)}.
\]

For the regular action use the vertex set \(H\), with right multiplication instead. In both cases the matrix is symmetric and each row sums to four. Let \(\chi_M(x)=\det(xI-M)\).

The exact characteristic polynomials for the natural and two-subset actions are

\[
\begin{aligned}
\chi_{A_{[5]}}(x)
&=(x-4)(x-1)(x+1)(x^2-5),\\
\chi_{A_{\binom{[5]}2}}(x)
&=(x-4)(x-1)(x+1)(x^2-5)
(x^2+3x+1)(x^3-x^2-7x+4).
\end{aligned}
\]

Here the notation in the second subscript means the set of two-element subsets. Both matrices are explicitly constructed in `exact_a5.py`: map each vertex by each generator and add one to the corresponding entry. These two formulas can therefore be checked with determinants of matrices of orders five and ten.

For the regular action the exact result is

\[
\begin{aligned}
\chi_A(x)={}&(x-4)(x-1)^4(x+1)^4x^6
(x^2-5x+5)^3(x^2-5)^4\\
&\quad\cdot(x^2+3x+1)^8(x^3-x^2-7x+4)^5.
\tag{1}
\end{aligned}
\]

Equation (1) has two independent exact certificates. First, the script constructs the 60 by 60 integer matrix by enumerating the group with the Schreier–Sims algorithm and computes its characteristic polynomial. Second, it computes word returns using image tuples, without that matrix or group enumeration. The second certificate is as follows.

Let \(a_0(h)=\mathbf1_{h=e}\), and recursively set

\[
a_{j+1}(h)=\sum_{g\in(s,s^{-1},t,t^{-1})}a_j(g^{-1}h).
\]

Then \(a_j(e)\) counts the words of length j evaluating to the identity. Every vertex in the regular action has that same return count, so
\(T_j=\operatorname{tr}(A^j)=60a_j(e)\).
For \(\chi_A(x)=\sum_{k=0}^{60}c_kx^{60-k}\), Newton's identities give

\[
c_0=1,\qquad
c_k=-\frac1k\sum_{j=1}^k c_{k-j}T_j
\quad(1\leq k\leq60).
\tag{2}
\]

All 60 coefficients obtained from (2) agree exactly with the integer matrix calculation and the expanded right side of (1). The complete integers \(a_k(e),T_k,c_k\) are in `exact_a5_newton.csv`. As a short check, the traces for k=1 through 8 are

\[
0,240,120,1920,2520,18720,40320,210240.
\]

Thus (1) is an exact computation, not a factorization inferred from floating point eigenvalues. The script, factorization data and full recurrence data are part of this finite certificate.

## Ordering the roots

The largest root of \(x^2-5x+5\) is
\(\alpha=(5+\sqrt5)/2>3\).
The other root is \((5-\sqrt5)/2<3\). The roots of \(x^2-5\) have absolute value \(\sqrt5<3\). Both roots of \(x^2+3x+1\) are negative. The linear factors in (1), apart from \(x-4\), have roots at most 1.

For \(f(x)=x^3-x^2-7x+4\), one has \(f(3)=1\), \(f'(3)=14\), and \(f''(x)=6x-2>0\) for x>=3. Hence \(f\) is positive and increasing on [3,infinity), and has no root there. All its roots are below 3: they are real because this factor occurs in the characteristic polynomial of a real symmetric matrix.

It follows from (1) that the largest eigenvalue below 4 is exactly \(\alpha\). Dividing by four gives

\[
\gamma=1-\frac\alpha4=\frac{3-\sqrt5}{8}.
\]

For the natural action, the largest eigenvalue below 4 is \(\sqrt5\), giving the claimed natural gap. For the two-subset action every eigenvalue below 4 is less than 3, by the same polynomial checks. Its upper gap is therefore greater than \(1/4\).

The complement map is equivariant and identifies the k-subset action with the (5-k)-subset action. The actions for k=0 and k=5 are trivial; those for k=1,4 and k=2,3 are the actions already checked. This proves the assertion about all subset actions, after removing their invariant constant vectors.

## Locating the missing eigenvalue

Let \(V=\{z\in\mathbb R^5:\sum_i z_i=0\}\). In the ordered basis
\((e_1-e_5)\wedge(e_2-e_5),
(e_1-e_5)\wedge(e_3-e_5),
(e_1-e_5)\wedge(e_4-e_5),
(e_2-e_5)\wedge(e_3-e_5),
(e_2-e_5)\wedge(e_4-e_5),
(e_3-e_5)\wedge(e_4-e_5)\)
of \(\Lambda^2V\), the four-term adjacency operator is

\[
D=\begin{pmatrix}
2&-1&0&-1&0&2\\
0&0&1&-1&0&0\\
-2&1&-1&2&1&-1\\
1&-1&0&-1&-1&0\\
1&0&1&-1&0&1\\
2&-1&1&-2&0&2
\end{pmatrix}.
\]

To reproduce this matrix, the matrix for g on V in the basis \(e_i-e_5\) has entries
\(B_g(i,j)=\mathbf1_{i=g(j)}-\mathbf1_{i=g(5)}\), for i,j in {1,2,3,4}. The matrix of \(\Lambda^2B_g\) consists of its two by two minors, with pairs ordered as above. Summing over the four generators gives D. Although this basis is not orthonormal, it is a basis of a unitary representation, so all eigenvalues are real.

A determinant of order six gives

\[
\chi_D(x)=x^2(x^2-5x+5)(x^2+3x+1).
\]

This contains \(\alpha\). Independently, `exact_a5.py` constructs \(\Lambda^2\mathbb R^5\) on the ten oriented pairs: a generator sends \(e_i\wedge e_j\) to \(e_{g(i)}\wedge e_{g(j)}\), using a minus sign when reordering the image pair. Since \(\mathbb R^5=\mathbf1\oplus V\), its exterior square is \(V\oplus\Lambda^2V\). The ten-dimensional characteristic polynomial is checked to equal \(\chi_{A_{[5]}}(x)/(x-4)\) times \(\chi_D(x)\). This provides a second construction of the six-dimensional factor.

This proposition concerns one finite pair. It gives no asymptotic bound for uniform random pairs, and does not refute the expansion conjecture.

## Coverage of the accompanying enumeration

For completeness, the benchmark enumerates one first-generator representative s per conjugacy class C in S_n, every possible second generator t, and gives each pair weight |C|. If s'=csc^-1, then t maps bijectively to ctc^-1 as t runs over S_n. Conjugation gives an isomorphism of the generated Cayley graphs and intertwines the natural actions and their sign twists. Consequently every statistic tabulated for (s,t) is invariant under this change of coordinates. Summing the weights over a first-generator class recovers every ordered pair with first coordinate in that class exactly once in distribution. The total weight is therefore
\(\sum_C |C|\,n!=(n!)^2\).
The direct audit uses every ordered pair without this reduction.
