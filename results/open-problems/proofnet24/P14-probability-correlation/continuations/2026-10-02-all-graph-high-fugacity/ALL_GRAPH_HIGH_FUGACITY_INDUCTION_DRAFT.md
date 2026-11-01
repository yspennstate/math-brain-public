# Candidate all-graph high-fugacity forest theorem by response absorption

2 October 2026. **Assembled candidate proof for independent full review.**
The local transfer lemma, geometric closure, and initial H2/H3 calculations
have separate independent audits. This file assembles them into one induction,
with its invariants explicit. It must receive a complete independent reading
before being promoted to a theorem. Historical novelty is not certified.
This statement concerns sufficiently large common fugacity; it does not
settle Kahn's conjecture at arbitrary fugacity or the q<1 random-cluster
conjecture.

## Proposed theorem and normalization

Let G be a loopless finite graph (parallel edges are allowed) with positive
conductances c_g. Loops, if present in an initial graph, never occur in a
forest and can be removed; a marked loop has identically zero Rayleigh
polynomial. Its unrooted forest
polynomial and marked Rayleigh polynomial are

\[
 Z(\mathbf z)=\sum_{F\text{ acyclic}}\prod_{g\in F}z_g,
 \qquad R_{ef}=(\partial_eZ)(\partial_fZ)-Z\partial_{ef}Z.
\]

**Candidate theorem.** For every distinct marked pair e,f, there exists a
finite \(\lambda_0(G,\mathbf c,e,f)\) such that
\(R_{ef}(\lambda\mathbf c)\ge0\) for every \(\lambda\ge\lambda_0\).
If e,f lie on a common cycle, the inequality is strict for sufficiently large
\(\lambda\). If they lie in different graphic-matroid components, their
indicators are independent for every \(\lambda>0\).

For a finite graph, taking the maximum of the pair thresholds gives one
threshold for all pairs. Covariance has sign opposite to R:
\(\operatorname{Cov}(1_e,1_f)=-z_ez_fR_{ef}/Z^2\).

Disconnected graphs factor, so reduce to a connected graph on n vertices.
Bridges factor as independent Bernoulli edges and can be removed from the
marked discussion. Write \(\tau_k\) for the k-component forest sum and
\(\tau=\tau_1>0\). Set \(t=1/\lambda\). Then

\[
 Z(\lambda c)=\lambda^{n-1}\tau F(t),\qquad
 F(t)=\sum_{j\ge0}(\tau_{j+1}/\tau)t^j.
\]

Activity derivatives are formed before common scaling. Consequently

\[
 R_{ef}(\lambda c)
 =-\lambda^{2n-4}\tau^2F(t)^2
       \partial_{ef}[\log\tau+\log F(t)].                 \tag{1}
\]

All marked derivatives on the right are conductance derivatives. Write
\(R_{ef}(\lambda c)=\sum_{k\ge0}H_k\lambda^{2n-4-k}\).
Once all earlier mixed logarithmic coefficients vanish, a negative coefficient
of \(t^k\) in the mixed logarithmic derivative gives \(H_k>0\).

## 1. Exact formal forest representation

Ground a vertex r and write \(K=L_r^{-1}\), extended by zero at r. Use the
Grassmann Gaussian convention
\(\int\exp(+\bar\psi L_r\psi)=\det L_r\), so
\(\langle\prod_{i\in I}q_i\rangle=\det K_{I,I}\), with
\(q_i=\bar\psi_i\psi_i\) and \(q_r=0\). Define

\[
 V=\sum_{i\ne r}q_i-\sum_{xy\in E(G)}c_{xy}q_xq_y.
\]

The all-minors matrix-tree theorem gives

\[
 F(t)=\langle\exp(tV)\rangle.                            \tag{2}
\]

For a direct coefficient proof, every non-root component of an unrooted
forest chooses either a vertex (+) or an edge (-). Remove its chosen edge if
there is one and mark the selected vertices/endpoints as roots. The rooted
forest is counted by the corresponding Green principal minor. Distinct roots
give exactly the nilpotence restrictions in the expansion of V. Each component
has net multiplicity vertices minus edges equal to one. Thus the coefficient
of \(t^j\) is \(\langle V^j\rangle/j!=\tau_{j+1}/\tau\).
All calculations below are finite exterior algebra or formal power series.
No positive Grassmann probability measure is assumed.

## 2. Intrinsic local scores and the exact invariant

Let I,J be connected disjoint interiors with no edge between them. Put
\(S=V(G)\setminus(I\cup J)\), and their full geometric port sets
\(A=N(I)\cap S\), \(C=N(J)\cap S\). Each is nonempty.
The e endpoints lie in I and the f endpoints in J. The physical unit-current
potential of e is supported inside I; that of f is supported inside J.

Define every local polynomial with **all its port fields free**, before
choosing a global ground. Let \(V_I\) contain vertex terms at I and quartic
edge terms for every original edge incident to I. Let

\[
 M_I(t;\psi_A)=\langle e^{tV_I}\mid\psi_A\rangle_I,
 \qquad U_e(t)=\partial_e\log M_I(t),                    \tag{3}
\]

where the local interior covariance is \(L_{II}^{-1}\) and its mean is the
Dirichlet harmonic extension of the free port fields. Define M_J,U_f similarly.
Since each original marked current is compactly supported in its interior,
the marked endpoint harmonic rows are equal. Changing its marked conductance
leaves the local harmonic rows and Dirichlet Schur complement fixed. This
remains true for every larger interior containing the original current support.

The induction invariant at level \(\ell\ge1\) is precisely:

\[
\begin{aligned}
 U_e(t)&=C_e(t)+t^\ell Q_{B_e}+t^{\ell+1}P_e+O(t^{\ell+2}),\\
 U_f(t)&=C_f(t)+t^\ell Q_{B_f}+t^{\ell+1}P_f+O(t^{\ell+2}),\tag{4}
\end{aligned}
\]

where C_e,C_f are boundary-field scalar series, \(Q_B=\bar\psi B\psi\),
and \(B_e,B_f\) are real PSD matrices on the full port coordinates satisfying

\[
 B_e\mathbf1=0,\quad\operatorname{range}(B_e)=\mathcal C(A),\qquad
 B_f\mathbf1=0,\quad\operatorname{range}(B_f)=\mathcal C(C).\tag{5}
\]

Here \(\mathcal C(A)\) is the complete zero-sum contrast space supported on A.
All scalar coefficients below \(\ell\) and at higher orders are harmless in
covariances. Zero response means a singleton port set and an exact stop.
The fixed local Schur complement, intrinsic free ports, physical compact
original current, and exact scalar/leading-bilinear expansion are part of the
invariant; geometric termination alone cannot replace them.

After grounding any r in S, let p_x be the harmonic row from S to each vertex
and T the grounded inverse Schur complement on S. Gaussian elimination gives

\[
 F(t)=\langle e^{tV_S}M_I(t)M_J(t)\rangle_S.             \tag{6}
\]

The covariance T and rows p are fixed by either marked variation. Only M_I
depends on c_e and only M_J on c_f. Hence

\[
 \partial_{ef}\log F(t)
   =\operatorname{Cov}_{S,t}(U_e(t),U_f(t)),             \tag{7}
\]

where the tilt is the normalized formal density in (6).

## 3. Ward identity at an arbitrary delayed order

The local raw integral corresponding to (3) is

\[
 I_I(t)=\int_I\prod_{i\in I}(1+tq_i)
   \exp\left\{\sum_{xy\text{ incident }I}c_{xy}
    [q(\psi_x-\psi_y)-tq_xq_y]\right\}.                 \tag{8}
\]

With left derivatives, the odd fields
\(Q_t=\sum_i(1-tq_i)\partial_{\psi_i}\) and
\(\bar Q_t=\sum_i(1-tq_i)\partial_{\bar\psi_i}\)
annihilate each deformed edge bracket. Interior integration by parts cancels
the derivative of \(1-tq_i\) against the vertex measure \(1+tq_i\).
Thus the raw integral is invariant under the port transformations.
The normalization is
\(I_I(t)=\det L_{II}\,e^{\bar\psi_A N_I\psi_A}M_I(t)\).
Its marked Schur derivative is zero and its determinant derivative scalar.
Consequently \(Q_tU_e=\bar Q_tU_e=0\) exactly on the free local ports.

Applying this identity to (4) yields

\[
 P_e=\sum_{a<b}(B_e)_{ab}q_aq_b+R_e,
 \qquad Q_0R_e=\bar Q_0R_e=0.                         \tag{9}
\]

The same holds for P_f. There is **no \(\ell\) factor**: these are ordinary
power-series coefficients and Q_t has exactly one t correction. In particular
\(D_{\mathbf1}P_e=-Q_{B_e}\), since
\(D_{\mathbf1}=-\bar Q_0Q_0\) and B_e has zero row sums.
The remainder in (9) can contain higher Grassmann degree; only its ordinary
translation invariance is asserted.

## 4. The even/odd cross coefficients at every level

Choose Gram decompositions
\(B_e=\sum_\rho\rho\rho^T\), \(B_f=\sum_\sigma\sigma\sigma^T\), with full
physical zero-sum charges on A and C. Positive channel weights can equivalently
be retained outside these vectors. Equation (7) and (4) give the first possible
nonzero mixed coefficient at \(t^{2\ell}\):

\[
 [t^{2\ell}]\partial_{ef}\log F
 =-\operatorname{tr}(TB_eTB_f)
 =-\sum_{\rho,\sigma}(\rho^TT\sigma)^2.               \tag{10}
\]

If this trace is positive, (1) proves eventual strict negative correlation.
If it is zero, every A contrast is Green-orthogonal to every C contrast.
Their overlap has at most one vertex. Unless a port set is a singleton, choose
a root in A minus C. Name the grounded response potentials
\(a^0_\rho(x)=p_xT\rho\), \(b^0_\sigma(x)=p_xT\sigma\).
Every \(b^0_\sigma\) vanishes on A and throughout I; every \(a^0_\rho\)
has a common value \(k_\rho\) on C and throughout J. Define
\(\alpha_\rho=a^0_\rho-k_\rho\), \(\beta_\sigma=b^0_\sigma\).
These opposite-port-zero physical representatives satisfy

\[
 L\alpha_\rho=\rho,\quad \alpha_\rho|_{C\cup J}=0,
 \qquad L\beta_\sigma=\sigma,\quad \beta_\sigma|_{A\cup I}=0.\tag{11}
\]

At \(t^{2\ell+1}\), (7) has exactly the three terms

\[
 \operatorname{Cov}(P_e,Q_{B_f})
 +\operatorname{Cov}(Q_{B_e},P_f)
 +\operatorname{Cum}(Q_{B_e},Q_{B_f},W_1),             \tag{12}
\]

where \(W_1=V_S+\langle V_I\mid S\rangle+\langle V_J\mid S\rangle\).
No lower scalar score can contribute. The proof of the audited H3 formula
applies unchanged to (12): the first covariance vanishes under the convenient
root; the second is the constant-mode correction
\(\sum_\rho k_\rho^2\operatorname{tr}(TB_f)\) by (9). The bilinear tilt
has zero third cumulant because the whitened PSD matrices have product zero.
The quartic tilt is minus the sum of the uncontracted edge quartics.
For orthogonal response charges its third cumulant is their unshifted wedge
square using \(a^0_\rho,b^0_\sigma\), with no factor of two. Completing the electrical wedge flow by
subtracting its opposite-port constant times the electrical response flow
subtracts exactly the second-score correction. Thus

\[
 -[t^{2\ell+1}]\partial_{ef}\log F
 =\sum_{\rho,\sigma,xy}c_{xy}
     [\alpha_\rho(x)\beta_\sigma(y)-\alpha_\rho(y)\beta_\sigma(x)]^2.    \tag{13}
\]

The potentials in (13) are explicitly the shifted representatives (11), so
the expression is independent of the chosen ground. Equations (10),(13) are
the even trace and odd shifted-wedge alternatives at every delayed order.

## 5. If both cross expressions vanish, exact score absorption

Suppose both (10)'s trace and (13)'s energy vanish. Let W_e be the union of
nonzero supports of the alpha_rho, and W_f the union of those of beta_sigma. For each
pair the edgewise wedge is zero. The same projective-direction and maximum-
principle argument used in the initial electrical equality geometry proves
that W_e,W_f are disjoint with no joining edge. Put

\[
 I'=I\cup W_e,\qquad J'=J\cup W_f,
 \qquad S'=V(G)\setminus(I'\cup J').                   \tag{14}
\]

These remain disjoint with no joining edge: beta_sigma vanishes on every old
e port and on I, so no edge from I can meet W_f, and vice versa. They remain
connected, because every nonzero response-support component meets an old
source port adjacent to the old connected interior. Connectivity of G forces
S' nonempty. Every nonzero response family adds at least one old port to its
interior: otherwise its potential would vanish at all its source ports and
be harmonic with zero boundary everywhere else, contradicting its charge.

Let p'_x be full harmonic rows on S'. For every response source rho and every
harmonic extension h from S',
\(\rho^Th_A=\langle L\alpha_\rho,h\rangle=\langle \alpha_\rho,Lh\rangle=0\).
The sources span all A contrasts, so every old port row equals a common row
pi_e. Similarly all C rows equal pi_f. This holds even if an old zero-response
port remains on S'.

The exact score transfer is the following coefficient map:

\[
 U'_e(t)=C'_e(t)+t^{\ell+1}Q_{B'_e}+O(t^{\ell+2}),     \tag{15}
\]

\[
 B'_e=\sum_{\rho,xy}c_{xy}\,
   [\alpha_\rho(x)p'_y-\alpha_\rho(y)p'_x-(\alpha_\rho(x)-\alpha_\rho(y))\pi_e]^T
   [\alpha_\rho(x)p'_y-\alpha_\rho(y)p'_x-(\alpha_\rho(x)-\alpha_\rho(y))\pi_e].\tag{16}
\]

The f formula is identical. Here U'_e is the original marked derivative of
the new intrinsic local partition M_I'. It is not a newly invented response
observable.

For completeness, the exact transfer calculation is:

1. Eliminate I first, then the added vertices I' minus I. Its outer Gaussian
   covariance is fixed under e because the old local Schur complement is
   fixed. The determinant factors exactly into the old determinant and the
   outer Schur determinant; the second factor has zero marked derivative.
   Thus U'_e is the normalized tilted conditional average of U_e, without a
   missing boundary-dependent normalization term.
2. The coefficient at order ell is scalar: every old port field has the same
   harmonic part \(h=\pi_e\psi_{S'}\), and B_e annihilates constants. At order
   ell+1 the only possible terms are
   \(\mathbb E[P_e]+\operatorname{Cov}(Q_{B_e},W_1^{\rm local})\).
   Earlier scalar scores remain scalar under the exact tilt.
3. The remainder R_e in (9) is unchanged by adding a common barred and unbarred
   harmonic field to all old ports, so its conditional expectation is scalar.
   The Ward quartic's boundary bilinear is
   \(\sum_{a<b}(B_e)_{ab}(C_{aa}+C_{bb}-2C_{ab})q(h)
     =-\operatorname{tr}(C_{AA}B_e)q(h)\).
   Its fully uncontracted quartic vanishes because q(h)^2=0.
4. A bilinear local first tilt contributes only a scalar covariance since
   Q_B has no harmonic boundary part. The quartic first tilt contributes the
   raw boundary Gram
   \(\sum_{\rho,xy}c_{xy}(\alpha_\rho(x)p'_y-\alpha_\rho(y)p'_x)^T
      (\alpha_\rho(x)p'_y-\alpha_\rho(y)p'_x)\)
   by rank-one Wick differentiation. The conditional fluctuation response
   potential is exactly the physical alpha_rho: it solves the Dirichlet equation
   in I' with source rho and is zero outside. Its energy is
   \(\rho^TC_{AA}\rho=\sum_{xy}c_{xy}(\alpha_\rho(x)-\alpha_\rho(y))^2\).
5. For arbitrary new boundary values z, the flow
   \(c_{xy}[\alpha_\rho(x)h_y-\alpha_\rho(y)h_x]\) has divergence
   \((\pi_ez)\rho\). Subtracting \((\pi_ez)\) times its electrical source
   flow leaves a circulation orthogonal in energy to the electrical flow.
   The raw Gram minus the Ward energy term is therefore exactly (16).

This establishes the precise leading coefficient, including its Grassmann
degree, sign and order. The next coefficients still obey Ward because the
original marked current remains compact in I'. The calculation uses full
free port polynomials; no uniform translation through a fixed root is made.

## 6. Full port-range closure and finite termination

Let \(A'=N(I')\cap S'\). Every row in (16) is a zero-sum contrast supported
on A'. If its Gram vanishes on new boundary values z, let h be their harmonic
extension and put \(k=h-\pi_ez\). Each response then has zero wedge with k.
Every nonzero support component of alpha_rho meets an old source port in A;
otherwise it would be harmonic with zero boundary. On that component k/alpha_rho
is constant, and it is zero at the old source port because all old port rows
are pi_e. Thus k=0 throughout W_e.

A new port adjoining W_e is forced k=0 by that edge wedge. Any remaining new
port adjoins the dormant old interior I and is consequently an old port in A,
where k=0 already. Conversely constant values on A' have constant harmonic
extension through I' and annihilate every row in (16). Therefore

\[
 B'_e\succeq0,\quad B'_e\mathbf1=0,
 \quad\operatorname{range}(B'_e)=\mathcal C(A').        \tag{17}
\]

The same holds for f. The original physical current remains inside the
enlarged interior, so its marked harmonic and Schur data remain fixed. Thus
every invariant in section 2 holds again, with ell advanced to ell+1.

If a new port set is a singleton, its full marked score is scalar at every
order: the one-port Ward operator has invertible coefficient 1-tq, so both
Grassmann derivatives of the score vanish. Equivalently forest weights factor
at that one-vertex interface. The two marked indicators are then independent
for every fugacity, so the procedure stops exactly, not approximately.

Otherwise each continuing zero-zero step strictly increases both disjoint
interiors while leaving S' nonempty. A finite graph admits only finitely many
such steps. It must therefore encounter a positive even trace, a positive odd
wedge, or an exact one-port stop. In the first two alternatives the first
nonzero mixed logarithmic coefficient is negative; (1) gives a positive
leading coefficient of R. In the stop alternative R is identically zero.

## 7. Base case and proposed conclusion

The transfer-current formula gives
\(H_0=\tau^2(b_e^TL^\dagger b_f)^2\). If it is positive, the conclusion
already holds. If zero, use the special constants vanishing on opposite marked
endpoints. The weighted second-coefficient formula gives

\[
 H_1=\tau^2\sum_{xy}c_{xy}
   [v_e(x)v_f(y)-v_e(y)v_f(x)]^2.
\]

If it is positive, the conclusion again holds. If both vanish, the electrical
maximum principle gives disjoint nonzero current supports E,F with no joining
edge. If an original marked endpoint has zero special potential, the other
endpoint belongs to a connected nonzero support E with that zero endpoint b
as a port. The compact-current block equation makes the other endpoint's
harmonic exit row exactly the coordinate identity at b. In a connected
positive-conductance interior, every geometric port has strictly positive
exit probability from that endpoint; therefore b is its only port. This is
the one-port forest factorization and gives independence. Bridges were already
disposed of above. In the remaining
case E,F are connected interiors containing the two marked endpoints. Their
initial conditional scores have exactly the leading form (4) with ell=1,
and their response matrices have full port contrast ranges (the audited
general H2 calculation). Thus the induction begins.

The finite alternatives in section 6 prove the candidate large-fugacity
statement for every pair. A one-port decomposition cannot separate two edges
lying on a common simple cycle: a cycle entering the interior through its
single port could only leave through the same vertex, contradicting simplicity
if it also met the opposite marked interior. Thus such a pair must encounter a positive
coefficient. Conversely, when no common cycle exists, the forest condition
and weights factor over distinct graphic-matroid components, giving exact
independence for every fugacity.

The proof supplies the sign of the first nonzero high-fugacity coefficient.
It does not assert that all subsequent coefficients are positive, produce a
polynomial SOS for the full Rayleigh difference, or establish negativity at
arbitrary fixed fugacity.

## Independent supporting files and current audit boundary

The stable initial results are `GENERAL_H2_SOS_PROOF.md` and
`GENERAL_H3_SOS_PROOF.md`. The independent local transfer calculation is
`RESPONSE_INDUCTION_INDEPENDENT_AUDIT.md`; separate geometry audit is
`RESPONSE_CLOSURE_INDEPENDENT_AUDIT.md`. Exact local exterior-algebra tests in
`response_induction_local_audit.py/.json` obtain delayed leading score orders
1,2,2,3,3 without using the response formula. Exact complete forest frontier
tests in `response_iteration_research_heat.py/.json` match H4,H5,H6 chains and
a non-twin, positive-offdiagonal-response three-port H4 example.

These finite checks cannot establish the global theorem. The assembled
invariant, arbitrary-order coefficient extraction, and transfer map
(15)--(17) require a final independent full read of this file before any
promotion or novelty claim.
