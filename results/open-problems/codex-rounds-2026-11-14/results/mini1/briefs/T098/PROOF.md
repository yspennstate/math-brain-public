# Exact diagonalization with Bernoulli transverse-field barriers

## Statement and scope

Let Lambda = {1,...,L}, with open boundary conditions, and write X_i and Z_i
for Pauli matrices, with eigenvalues of Z_i equal to +1 and -1. Consider

\[
 H_\Lambda=\sum_{i=1}^L h_iZ_i+
 \sum_{i=1}^L\xi_i g_iX_i+
 \sum_{i=1}^{L-1}J_iZ_iZ_{i+1}.                         \tag{1}
\]

The indicators xi_i are independent, with P(xi_i=1)=p, where 0<p<1.
The real coefficients h_i, g_i, J_i can be arbitrary finite numbers. In
particular, the h_i may have the iid random-field law in T098, independently
of the indicators. No smallness or level-spacing assumption is made.

There is a unitary U_Lambda such that D_Lambda=U_Lambda^* H_Lambda U_Lambda
is diagonal in the Z basis. The operators

\[
 \tau_i=U_\Lambda Z_iU_\Lambda^*                         \tag{2}
\]

are commuting Hermitian involutions, commute with H_Lambda, and have
one-dimensional joint eigenspaces. Thus H_Lambda is a function of a complete
set of l-bits, at every energy.

For every realization there are sets S_i containing i such that, for either
choice of sign and every one-site operator A_i,

\[
 \operatorname{supp}(U_\Lambda^{\pm1}A_iU_\Lambda^{\mp1})
 \subset S_i.
\]

Put R_i=max{|j-i|:j in S_i}. For every L, i, and integer r>=1,

\[
 \mathbb P(R_i>r)\le 2p^r-p^{2r}.                       \tag{3}
\]

If i-r-1>=1 and i+r+1<=L, equality holds in (3) for the sets S_i
constructed below. These are support envelopes, not necessarily the minimal
supports of particular operators. The bound is uniform in L and holds
simultaneously for all A_i on the same event.

For a finite set X and an operator A supported on X, let E_{N_r(X)} be the
normalized partial-trace conditional expectation onto the algebra of the
r-neighborhood of X, intersected with Lambda. Then

\[
 \mathbb E\left\|\alpha(A)-E_{N_r(X)}\alpha(A)\right\|
 \le 4|X|\|A\|p^r,                                    \tag{4}
\]

where alpha(A) is either U_Lambda A U_Lambda^* or its inverse conjugation.

The exact zeros xi_i=0 are essential to the proof. This is a solvable
restricted family of the Hamiltonians in T098; it does not establish
stability for generic transverse fields that are nonzero at every site.

## 1. Conditional block Hamiltonians

Call a site frozen if xi_i=0, and let F be their set. Each Z_f, f in F,
commutes with H_Lambda: the only term in (1) not commuting with Z_f would
be xi_f g_f X_f, which is zero.

Let B=[a,b] be a maximal nonempty interval of sites with xi_i=1. Define

\[
 \partial B=\{a-1,b+1\}\cap\Lambda,\qquad
 \overline B=B\cup\partial B.
\]

Every site of partial B is frozen by maximality. For an assignment
s=(s_f)_{f in partial B} in {+1,-1}^{partial B}, define on the spins in B

\[
 K_B(s)=\sum_{i=a}^b(h_iZ_i+g_iX_i)
 +\sum_{i=a}^{b-1}J_iZ_iZ_{i+1}
 +\mathbf1_{a>1}J_{a-1}s_{a-1}Z_a
 +\mathbf1_{b<L}J_b Z_bs_{b+1}.                        \tag{5}
\]

Missing boundary terms are omitted. Let

\[
 P_{\partial B}(s)=\prod_{f\in\partial B}(I+s_fZ_f)/2,
 \qquad
 \widehat K_B=\sum_s P_{\partial B}(s)K_B(s).            \tag{6}
\]

The empty-boundary product is I. Every term of H_Lambda belongs to exactly
one of the following: a frozen on-site term; a bond with both endpoints
frozen; or the on-site, internal-bond, or boundary-bond terms of a unique
active block. Therefore

\[
 H_\Lambda=H_F+\sum_B\widehat K_B,\qquad
 H_F=\sum_{f\in F}h_fZ_f+
       \sum_{i:\,i,i+1\in F}J_iZ_iZ_{i+1}.             \tag{7}
\]

This is an operator identity before choosing a frozen-spin sector.

## 2. Controlled diagonalizers commute

For each B and s, choose an orthonormal eigenbasis of the finite Hermitian
matrix K_B(s), order it, and let V_B(s) have those basis vectors as its
columns. Then

\[
 V_B(s)^*K_B(s)V_B(s)=D_B(s)
\]

is diagonal in the fixed product basis on B. Degeneracies do not obstruct
this step. A measurable rule can be fixed: order distinct eigenvalues,
project the ordered coordinate vectors into each eigenspace, and apply
Gram--Schmidt, discarding zero projections. Spectral projections and these
operations give a Borel choice on each multiplicity stratum.

Define the controlled unitary, extended by I elsewhere,

\[
 \widehat V_B=\sum_s P_{\partial B}(s)V_B(s).            \tag{8}
\]

The projectors in this sum are orthogonal and sum to I; they commute with
all V_B(s), since controls and targets are disjoint. Hence
Vhat_B^* Vhat_B = Vhat_B Vhat_B^* = I. Its support is contained in Bbar,
and it commutes with every Z_f, f in F.

For distinct blocks B and C, B and C are disjoint and neither contains
a boundary site of the other. Their padded intervals can overlap only at
a frozen boundary site. Expanding (8) for B and C, each target operator
V_B(s) commutes with the other target V_C(t) and with both sets of boundary
projectors; the projectors also commute with each other. Each summand in
one expansion therefore commutes with every summand in the other. Thus

\[
 [\widehat V_B,\widehat V_C]=0.                        \tag{9}
\]

The same argument gives [Vhat_B,Khat_C]=0 for B!=C, and
[Vhat_B,H_F]=0. It also applies with either unitary replaced by its adjoint.

Set

\[
 U_\Lambda=\prod_B\widehat V_B.
\]

The order is immaterial. Equations (5)--(9) give

\[
 D_\Lambda=U_\Lambda^*H_\Lambda U_\Lambda
 =H_F+\sum_B\sum_sP_{\partial B}(s)D_B(s).             \tag{10}
\]

Every term on the right is diagonal in all the physical Z coordinates.
This proves the diagonalization.

## 3. Completeness and the eigenstate quantifier

Conjugation preserves adjoints, products, and commutators. Therefore
tau_i^*=tau_i, tau_i^2=I, and [tau_i,tau_j]=0. Since [D_Lambda,Z_i]=0,
equation (10) also gives [H_Lambda,tau_i]=0. For frozen f,

\[
 \tau_f=Z_f.                                         \tag{11}
\]

For every t in {+1,-1}^L, the joint spectral projection is

\[
 Q_t=\prod_i(I+t_i\tau_i)/2
     =U_\Lambda\left(\prod_i(I+t_iZ_i)/2\right)U_\Lambda^*.
\]

The middle product has rank one, so Q_t has rank one. Consequently the
vectors U_Lambda|t> form a complete eigenbasis at all energies, and

\[
 H_\Lambda=\sum_t E(t)Q_t
\]

is a function of the l-bits. No energy restriction or discarded eigenstate
occurs.

If an energy is degenerate, arbitrary superpositions within its eigenspace
need not be joint eigenvectors of the l-bits. The unconditional statement
for arbitrary coefficients is a complete localized eigenbasis, not a claim
about every vector in a degenerate eigenspace. For iid absolutely continuous
h_i, independent of xi, g, J, the finite-volume spectrum is almost surely
simple, as proved in Section 7. In that case every energy eigenvector is,
up to phase, a vector of this basis. This handles the literal all-eigenstate
quantifier for this usual random-field law.

## 4. Deterministic support envelope

For i in Lambda define

\[
 S_i=\{i\}\cup\bigcup_{B:\,i\in\overline B}\overline B. \tag{12}
\]

If i is active, exactly its own padded block appears. If i is frozen,
at most its left and right active blocks appear. The two blocks can share
i, but their gates commute by (9).

If i is not in Bbar, the gate Vhat_B commutes with any A_i. By (9), all
such gates can be moved next to their adjoints in U A_i U^* and cancelled.
The only gates remaining have i in Bbar. Conjugation by them is supported
in the union (12). The identical cancellation works for U^* A_i U.

More generally, an operator A supported on X commutes with every gate
whose padded block misses X. Cancelling those gates shows that both
conjugations are supported in the union of S_i for i in X. Commutativity
of the gates is needed here: there is no cascade through further blocks.

## 5. Exact Bernoulli tail and norm locality

Fix integer r>=1. If i+r>=L, S_i cannot extend to the right of i+r.
If i+r<L, the following equivalence holds:

\[
 \max S_i>i+r
 \quad\Longleftrightarrow\quad
 \xi_{i+1}=\cdots=\xi_{i+r}=1.                        \tag{13}
\]

For the forward direction, suppose there is a frozen site j among
i+1,...,i+r, and take the first one. If i is active, its block and its
right frozen boundary stop at j. If i is frozen, its adjacent right block,
if present, also stops at j. Any block to the left of i has right endpoint
at most i. In each case max S_i<=j<=i+r.

For the reverse direction, first let i be active. Its block contains
i,...,i+r. If that block continues to i+r+1, its padded support does too;
if it ends at i+r, then the existing frozen site i+r+1 is its boundary.
Next let i be frozen. Since r>=1, the active site i+1 starts a block
adjacent to i that contains all sites through i+r. The same alternatives
give i+r+1 in its padded support. This proves (13).

There is a reflected equivalence on the left whenever i-r>1. If that
inequality fails, extension beyond i-r is impossible. When both events
are possible, they depend on disjoint sets of r independent indicators.
Each has probability p^r, and their intersection has probability p^(2r).
The union therefore has probability 2p^r-p^(2r). If only one side is
possible its probability is p^r, which is no larger; if neither is
possible it is zero. This proves (3), including its equality statement.

On the event that R_i<=r for every i in X, alpha(A) belongs to the
algebra of N_r(X), so its conditional-expectation error is zero. On the
complement, the error is at most 2||A||: conjugation is isometric and
normalized partial-trace conditional expectation is contractive. By a
union bound and (3),

\[
 \begin{split}
 \mathbb E\|\alpha(A)-E_{N_r(X)}\alpha(A)\|
 &\le 2\|A\|\,|X|(2p^r-p^{2r})\\
 &\le 4|X|\|A\|p^r.
 \end{split}
\]

Contractivity can be seen by writing the conditional expectation as the
average of conjugations by the finite Pauli group on the traced-out sites;
each conjugation preserves norm. This proves (4).

For comparison, a specified interval of m sites is active with probability
p^m. If M_L is the largest active-block length, then

\[
 \mathbb P(M_L\ge m)\le (L-m+1)p^m\le Lp^m,
 \qquad 1\le m\le L.                                \tag{14}
\]

Indeed, a block of length at least m contains an all-active interval of
length m, and there are L-m+1 such intervals. The factor L in this
all-sites bound does not occur in the fixed-site bound (3). For p>0,
arbitrarily long active blocks occur almost surely on the infinite chain:
for each fixed m, disjoint intervals of length m are independently active
with probability p^m, and the probability that the first n all fail is
(1-p^m)^n, tending to zero. Taking the countable intersection over m
establishes the claim. Thus the proof makes no deterministic uniform
bound on the radii at every site.

## 6. Infinite-volume interpretation

Put iid Bernoulli indicators on Z and assume the other coefficients are
uniformly bounded, so that the usual finite-range spin dynamics exists.
Almost surely every active interval is finite. For example, an infinite
rightward run beginning at a fixed site has probability at most p^n for
every n, hence probability zero; take a countable union over sites and
over the two directions.

For each finite block use the rule in Section 2 with its two frozen
boundaries. For a local A, only finitely many padded blocks meet its
support. Define alpha(A) by conjugation with the product of their gates.
Gates missing the original support commute with A and with all the other
gates, so adding or removing them has no effect. A common finite product
therefore implements alpha on any given finite collection of local
operators. It follows that alpha is linear, multiplicative, *-preserving,
and isometric on the local algebra.

Replacing each gate by its adjoint defines its inverse. To check the
inverse on alpha(A), any additional gate that meets the expanded support
but missed the original support commutes with A and with the implementing
gates; hence it also commutes with alpha(A). Such gates cancel. The maps
therefore extend by norm continuity to inverse automorphisms of the
quasi-local C*-algebra. Finite-volume conjugations stabilize on any fixed
local A once the volume contains all the blocks meeting its support and
their frozen boundaries. Bounds (3) and (4) continue to hold.

The operators tau_i=alpha(Z_i) commute with one another. Each has finite
support for a fixed realization. Its commutator with the Hamiltonian
derivation is zero: it is the same finite commutator as in a sufficiently
large finite interval. Equation (10) gives the corresponding diagonal
interaction block by block. This construction asserts an automorphism;
it does not assert that an infinite product of gates is a unitary on a
chosen infinite tensor-product Hilbert space.

## 7. Almost-sure simplicity for absolutely continuous fields

Fix L, the indicators, and finite g and J, independently of the fields.
For a 2^L by 2^L matrix (1), every coefficient of its characteristic
polynomial is a polynomial in h_1,...,h_L. Its discriminant is consequently
a polynomial in these variables: for a monic polynomial with roots
lambda_1,...,lambda_N, the discriminant is the symmetric polynomial
product_{a<b}(lambda_a-lambda_b)^2, which is a polynomial in the elementary
symmetric functions, hence in the polynomial's coefficients. It vanishes
exactly when an eigenvalue is repeated.

This polynomial is not identically zero. To see this, set

\[
 h_i=t3^{i-1},\qquad
 M=\sum_i|\xi_i g_i|+\sum_i|J_i|,
 \qquad t>M.
\]

For distinct Z configurations, the difference of eigenvalues of
sum_i h_i Z_i equals 2t sum_i c_i3^{i-1}, where c_i is in {-1,0,1} and
not all zero. If k is its largest nonzero index, then

\[
 3^{k-1}-\sum_{i<k}3^{i-1}
 = (3^{k-1}+1)/2>0.
\]

Thus the integer sum is nonzero and has absolute value at least one.
The unperturbed eigenvalues are distinct with consecutive gaps at least
2t. The remaining operator has norm at most M by the triangle inequality.
The min--max principle puts its ordered eigenvalues within M of the
unperturbed ordered eigenvalues, so consecutive gaps of H are at least
2t-2M>0. This proves that the discriminant is nonzero at one point.

A nonzero real polynomial has a Lebesgue-null zero set. For completeness,
in one variable it has finitely many roots. Inductively write a polynomial
in the last variable, with coefficient polynomials in the preceding
variables. The set where all coefficients vanish is contained in the
zero set of one nonzero coefficient and has measure zero by induction.
Outside it, the last variable has only finitely many roots. Fubini's
theorem, applied first on bounded boxes, proves the assertion.

The joint field law has a density, so the probability of a repeated
eigenvalue is zero. Conditioning first on any independent random g and
J gives the same conclusion. Countably many finite intervals have
simultaneously simple spectra almost surely. This is not a quantitative
small-gap estimate and does not imply Imbrie's LLA assumption.

## 8. Why nonzero barrier perturbations remain open

Let f be a frozen site and add epsilon X_f to (1). The previously exact
l-bit tau_f=Z_f then satisfies

\[
 [H_\Lambda+\varepsilon X_f,\tau_f]
 =-2\mathrm i\varepsilon Y_f,\qquad
 \|[H_\Lambda+\varepsilon X_f,\tau_f]\|=2|\varepsilon|. \tag{15}
\]

Also, U_Lambda^* X_f U_Lambda anticommutes with Z_f, because U_Lambda
commutes with Z_f. It has zero diagonal in the joint Z basis and norm one.
Thus the old diagonalizer leaves an off-diagonal perturbation of norm
exactly |epsilon|. Blocks can no longer be diagonalized separately with
classical frozen controls. Controlling new rotations and the small
energy denominators they encounter is an additional problem; no
uniform-in-volume stability bound follows from (1)--(15).
