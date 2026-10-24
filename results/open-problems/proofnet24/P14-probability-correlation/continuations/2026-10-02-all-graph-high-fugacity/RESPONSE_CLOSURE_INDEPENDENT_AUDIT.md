# Independent audit of response closure and finite geometric enlargement

Research checkpoint, 2 October 2026. The geometric statements below are proved. They do **not** prove that the later forest Rayleigh coefficients equal the proposed iterated electrical expressions. That coefficient identification remains a separate algebraic obligation.

## 1. Abstract electrical setup

Let G be a connected finite graph with positive conductances c_g and Laplacian L. Let I,J be nonempty disjoint regions with no graph edge between them, and set

\[
 S=V(G)\setminus(I\cup J),\qquad A=N(I)\cap S,\qquad C=N(J)\cap S.
\]

Both port sets are nonempty. Let q_l be a finite collection of zero-sum charges supported on A whose span is the complete contrast space

\[
 \mathcal C(A)=\{q:\operatorname{supp}q\subseteq A,\ \mathbf1^Tq=0\}.
\]

Let r_m span the corresponding space on C. Associate positive channel weights \mu_l,\nu_m with nonzero charges. Their Gram matrices are positive semidefinite without any off-diagonal sign assumption.

Suppose the cross Green products vanish:

\[
 q_l^TL^\dagger r_m=0\quad\text{for all }l,m.
\]

A potential a_l satisfying La_l=q_l is then constant on C, because its pairing with every C contrast vanishes. Shift it to be zero on C. It is harmonic inside J and has zero boundary values, so it vanishes throughout J. Similarly choose b_m with Lb_m=r_m and b_m=0 on A\cup I. These shifts are independent of grounding.

Assume also the nonnegative wedge energy vanishes:

\[
 \sum_{l,m,g=xy}\mu_l\nu_m c_g
       (a_l(x)b_m(y)-a_l(y)b_m(x))^2=0.\tag{1}
\]

Every channel and edge weight is positive, so each individual wedge vanishes.

## 2. Aggregate support separation

Put W_I={x:a_l(x)\ne0 for some l} and W_J={x:b_m(x)\ne0 for some m}. Then W_I,W_J are disjoint and no graph edge joins them.

For a single pair a,b, the edgewise wedge condition makes [a:b] constant on each connected component where (a,b)\ne(0,0). If both projective coordinates were nonzero, the component could meet neither A nor C, since b=0 on A and a=0 on C. Both potentials would be harmonic on that component with zero boundary values; the maximum principle would force them to vanish. Thus their nonzero supports are disjoint. An edge joining the two supports would have a nonzero wedge. Applying this argument to every pair proves the aggregate assertion.

Now enlarge

\[
 I'=I\cup W_I,\qquad J'=J\cup W_J,\qquad
 S'=V(G)\setminus(I'\cup J').\tag{2}
\]

These regions remain disjoint. There is no I–W_J edge: a neighbor outside I is in A, where every b_m is zero. The J–W_I case is identical. Together with the original and aggregate separations, this proves there is no I'–J' edge. Connectivity consequently forces S'\ne\varnothing.

The union with the old regions in (2) is necessary. An auxiliary potential can vanish at old interior vertices, including an entire symmetric twin pair. One must not silently replace I' by W_I or assume that auxiliary supports cover the old interior.

## 3. Common harmonic rows at every old port

Let H be any function harmonic on I'\cup J' with arbitrary prescribed values z on S'. Each a_l is zero outside I', so symmetry of L gives

\[
 \langle q_l,H\rangle=\langle La_l,H\rangle
                      =\langle a_l,LH\rangle=0.
\]

Since the q_l span \mathcal C(A), H is constant on A. Hence the new full harmonic extension rows p'_x satisfy

\[
 p'_x=\pi_I\quad(x\in A).
\]

Similarly p'_x=\pi_J on C. This proof uses physical zero-sum source charges and full boundary rows, so it remains valid when an old port lies on the new boundary or is chosen as the ground. Every old port lies either inside I' or on its new port set A'=N(I')\cap S'.

## 4. New response Gram has the full port contrast range

Define, for each old channel l and original edge g=xy,

\[
 \rho_{l,g}=a_l(x)p'_y-a_l(y)p'_x
                     -(a_l(x)-a_l(y))\pi_I,
\qquad
 B'_I=\sum_{l,g}\mu_l c_g\rho_{l,g}^{T}\rho_{l,g}.\tag{3}
\]

Every \rho has zero coordinate sum and is supported on A'. This follows from harmonic row sums and the fact that a_l is zero outside I'. The analogous construction defines B'_J on C'=N(J')\cap S'.

**Claim.** The kernel of B'_I consists exactly of boundary functions constant on A'. Equivalently its range is \mathcal C(A').

For a boundary vector z, let H be its harmonic extension and set k=H-\pi_Iz. Vanishing of z^TB'_Iz means

\[
 a_l(x)k(y)-a_l(y)k(x)=0
 \quad\text{on every edge and for every }l.\tag{4}
\]

By Section 3, k=0 on every old port in A.

Each connected component of the nonzero support of a_l meets A. Otherwise a_l would be harmonic there with zero boundary values, contradicting the maximum principle. On such a component, (4) makes k/a_l constant. At a vertex of that component in A the ratio is zero. Therefore k=0 throughout W_I.

Consider a new port s\in A' adjoining x\in I'. If some a_l(x)\ne0, then a_l(s)=0, and (4) forces k(s)=0. If every a_l(x)=0, then x belongs to the old region I: all added vertices lie in W_I. Since s is outside I' and adjacent to I, it is an old port in A, where k(s)=0 already. This last case is the essential dormant-interior correction.

Thus H is constant on every new port A'. Conversely, if H is constant on A', the maximum principle makes it constant on I'; its value on all old ports A\subseteq I'\cup A' is the same. Every response in (3) vanishes. This proves the claim. The J proof is identical.

In particular, the next response Gram is positive semidefinite by construction and has the full new contrast range. It need not be an M-matrix; no positive auxiliary-edge decomposition is required.

## 5. Strict enlargement and finite termination of the geometric procedure

If an old contrast family is nonzero, at least one a_l is nonzero at an old port in A. Indeed, if it were zero at all of A, it would be harmonic on V(G)\setminus A with zero Dirichlet data and would vanish everywhere, contrary to La_l=q_l\ne0. Old ports are outside I, so I' strictly contains I. The same applies to J.

Thus every stage at which both contrast families are nonzero and both the trace and wedge expressions vanish adds at least one vertex to each side. The two sides stay disjoint, have no joining edge, and leave a nonempty separating set. Starting at I,J, there can be no more than

\[
 \left\lfloor\frac{n-1-|I|-|J|}{2}\right\rfloor
\]

successful double-enlargement stages. A finite procedure must encounter a nonzero trace, a nonzero wedge, or a zero response family.

By the kernel theorem, a zero new response family is equivalent to its port set being a singleton (for a nonempty region in a connected graph). If the corresponding region contains one original marked edge and the opposite region contains the other, a singleton interface gives forest-block factorization at that vertex and exact independence of the marked edge indicators. This implication is geometric; it does not assert that a general vanishing trace or wedge alone gives independence.

For grounding, choose any root in the current nonempty S. All full source charges are zero-sum, and changing the root changes each potential only by a constant. The opposite-port shifts remove that freedom. At a Ward step requiring a root outside one port set, cross orthogonality and full contrast range imply that the two port sets share at most one vertex; if both contain at least two vertices, the required root exists in one set minus the other.

## 6. Precise unresolved coefficient obligation

The proved closure theorem establishes the electrical iteration as a finite geometric construction with positive channel weights. It does not identify that construction with the forest model at arbitrary orders.

The candidate iteration predicts, at level j, an even coefficient H_{2j} equal to the cross Green trace square of the j-th response families, and, when that trace vanishes, an odd coefficient H_{2j+1} equal to their shifted wedge square. This is proved for j=1 by [GENERAL_H2_SOS_PROOF.md](GENERAL_H2_SOS_PROOF.md) and [GENERAL_H3_SOS_PROOF.md](GENERAL_H3_SOS_PROOF.md). The later identities require a new algebraic lemma: after integrating the enlarged interiors, the first boundary-dependent marked score must advance by one order and have exactly the next response Gram as its leading bilinear coefficient, with every higher-degree term and lower-order scalar term correctly controlled.

Exact Ward invariance by itself does not state that lemma. The second original marked score already contains quartic terms; their cancellation was essential to H_3. A recursive proof must show how those and all later terms transform under enlargement. Merely repeating the port-kernel theorem, invoking finite growth, or checking chains of K_4 does not supply the missing score/coefficent identity.

The exact research checks in [response_iteration_research_heat.py](response_iteration_research_heat.py) and [response_iteration_research_heat.json](response_iteration_research_heat.json) agree with the candidate through positive H_4, H_5, and H_6 cases, including a non-M-matrix three-port example. They are examples, not an all-orders proof.

**Audit verdict:** full port-range closure, positive Gram representation, root management, strict enlargement, and finite geometric termination are proved under the explicit assumptions above. An all-orders forest conclusion remains conditional on the separate marked-score transfer lemma.
