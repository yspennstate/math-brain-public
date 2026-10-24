# Projection-entropy submodularity survives unitary gluing at one coordinate

Root constructive proof, 2026-09-15. This closes a new compositional consequence of C056 and C036. Historical priority is unverified. General unitary frames and full Lyons concavity remain open.

## 1. Entropy set functions of unitary frames

For a unitary \(U\) on a finite coordinate set, define
\[
F_U(I)=H(P_{U P_I U^*}),\qquad
P_I=\sum_{i\in I}e_i e_i^*.
\]
Say the frame has projection-entropy submodularity if, for every set \(I\) and distinct \(p,q\notin I\),
\[
\beta_U(I;p,q):=F_U(I+p)+F_U(I+q)-F_U(I)-F_U(I+p+q)\ge0.
\tag{1}
\]
C056 proves (1) for every rank-one phase frame \(U=I+(z-1)hh^*\), \(|z|=1\), without restricting the phase or dimension.

**The gluing theorem.** If \(U_1,U_2\) have supports \(S_1,S_2\) intersecting in at most one coordinate, and each local entropy set function is submodular, then the frame \(U_2U_1\) has submodular projection entropy. Thus any sequence of such frames whose next support meets the accumulated previous support in at most one coordinate inherits (1). This includes arbitrary-rank tree-overlap products of rank-one phase factors throughout their full physical phase ranges.

## 2. An exact entropy identity

The disjoint-support case is additive. Suppose \(S_1\cap S_2=\{c\}\). For an input set \(I\), write
\[
A=I\cap S_1,\qquad B=I\cap(S_2\setminus\{c\}),\qquad
s(A)=\sum_{j\in A}|(U_1)_{cj}|^2.
\]
Let \(F_1,F_2\) denote the local entropy set functions. Then
\[
\boxed{F_{U_2U_1}(I)=F_1(A)+(1-s(A))F_2(B)+s(A)F_2(B+c).}\tag{2}
\]
Input coordinates outside the union contribute deterministic bits and zero entropy.

Here is a direct proof that includes the entropy, rather than only the transition probabilities. Cauchy-Binet expands each fixed-cardinality minor as
\[
\det(U_2U_1)_{Y,I}=\sum_R\det(U_2)_{Y,R}\det(U_1)_{R,I}.
\]
A nonzero term fixes \(R\) outside \(S_1\) from \(I\), and outside \(S_2\) from \(Y\). Only membership of \(c\) can remain undecided; the fixed cardinality decides it. Therefore at most one intermediate set \(R\) contributes. Squared minor probabilities are exactly those of the two-step occupation channel, and \(R\) is a deterministic function of \(I,Y\) on its support.

For fixed input \(I\), this gives
\[
H(Y)=H(R)+H(Y\mid R).
\]
The first term is \(F_1(A)\). At the second step, \(R\cap S_2\) is either \(B\) or \(B+c\). The determinantal one-coordinate marginal is \(\Pr(c\in R)=s(A)\), proving (2). No common random permutation or individual middle-label coupling is assumed.

## 3. All submodular differences

Because \(s\) is modular and lies in \([0,1]\), every two-update difference of (2) has a nonnegative explicit expression.

- If both updates belong to \(S_1\), the difference is \(\beta_1(A;p,q)\). The second-step contribution is affine in \(s\) and has zero mixed difference.
- If both updates belong to \(S_2\setminus\{c\}\), the difference is
\[
(1-s(A))\beta_2(B;p,q)+s(A)\beta_2(B+c;p,q)\ge0.
\]
- If \(p\in S_1\) and \(q\in S_2\setminus\{c\}\), the difference is
\[
\boxed{|(U_1)_{cp}|^2\,\beta_2(B;c,q)\ge0.}\tag{3}
\]
- If an update is outside both supports, the difference is zero.

These cases exhaust the coordinates, including an update at \(c\), which belongs to the first group. They prove the theorem and propagate quantitative lower bounds from C056. Repeated application is legitimate even though an accumulated product need no longer be a rank-one phase: the one-intermediate-set argument uses only its support and unitarity.

## 4. Consequence for two varying eigenvalues

Let \(U\) be a tree-overlap product of rank-one phase factors as above. Fix a coordinate set \(I\) and distinct \(p,q\notin I\). Then throughout the square \((x,y)\in[0,1]^2\),
\[
\boxed{(x,y)\longmapsto
H(P_{U(P_I+x e_pe_p^*+y e_qe_q^*)U^*})
\text{ is jointly concave}.}\tag{4}
\]
For clarity, the inference uses two distinct completed inequalities.

First, (1) holds by the present proof and C056. For slopes with the same sign, the projection-mixture entropy identity in ROOT_PROJECTION_ENTROPY_LEAD.md consists of the concave two-Bernoulli count entropy, a term with coefficient \(-\beta_U(I;p,q)xy\), affine terms, and a homogeneous Jensen-Shannon perspective. The latter has nonnegative first derivatives and is concave in its two mixture weights \(x(1-y),y(1-x)\). Thus its affine-line curvature is nonpositive for same-sign slopes.

Second, C036 constructs all required unlabeled projection diamonds for these tree-overlap frames, using C035's full-phase local constructions. With frozen supermodular weights \(-\log p\), those diamonds give nonpositive frozen acceleration for opposite-sign slopes; the Fisher term is also nonpositive. This proves the other sign class. Boundary probabilities follow by continuity. Neither input is replaced by an assumption that arbitrary entropy functions of random permutations are submodular.

This extends the two-varying-eigenvalue theorem from individual phase frames to arbitrary tree-overlap products. It still keeps all other eigenvalues at zero or one; unrestricted background eigenvalues and arbitrary affine changes of eigenvectors are outside (4).

## 5. Further closure and limits

C040's projection-block substitution changes projection entropy by a constant plus a modular function of \(I\): each kernel diagonal is linear in the selected frame columns. Hence every \(\beta\) is preserved exactly. Both the submodularity theorem and (4) therefore also survive those arbitrary projection-block encodings.

For the quadrature two-coordinate overlap in C036, squared-minor transition channels can compose even though \(R\) is no longer determined by \(I,Y\). Formula (2) then has an additional subtraction \(H(R\mid I,Y)\); this proof makes no claim about its mixed entropy difference. Thus the present gluing theorem does not automatically extend to the two-overlap or general overlapping cases.
