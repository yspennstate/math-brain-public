# A competing pure ground state is distinguishable in one direction

Let \(\mathfrak A\) be the quasi-local algebra of a chain with a fixed finite-dimensional spin at each site. Let \(\alpha_t\) be the dynamics of a uniformly bounded nearest-neighbor interaction. For local \(A\), write
\[
 D(A)=[H,A],\qquad \left.\frac{d}{dt}\alpha_t(A)\right|_{t=0}=iD(A).
 \tag{1}
\]
The commutator is a finite sum. A ground state \(\theta\) satisfies
\[
 \theta(B^*D(B))\geq0\qquad(B\text{ local}).              \tag{2}
\]
Assume that a pure ground state \(\omega\) satisfies
\[
 \omega(A^*D(A))\geq\gamma\{\omega(A^*A)-|\omega(A)|^2\},
 \qquad \gamma>0,\quad A\text{ local}.                   \tag{3}
\]

For the spin-1 Heisenberg chain, purity and (3) are the external conclusions of Hal Tasaki, *On the uniqueness of translation-invariant ground states of the S=1 Heisenberg and J–D antiferromagnetic chains*, [arXiv:2610.34330v2, Theorem 2.1 and equation (2.12)](https://arxiv.org/html/2610.34330v2). Its finite numerical premises are not verified here. The abstract deductions below do not require translation invariance of a competitor.

For an integer \(a\), put
\[
 L_a=(-\infty,a]\cap\mathbb Z,\qquad
 R_a=[a,\infty)\cap\mathbb Z.
\]
For a set \(X\) of sites, \(\mathfrak A_X\) is its quasi-local observable algebra, and \(\|f\|_X\) is the norm of the restriction of a functional \(f\) to that algebra. State distances have no factor of one half. Two states are called disjoint on \(X\) if their restricted GNS representations have no nonzero quasi-equivalent subrepresentations.

**Theorem.** If \(\rho\ne\omega\) is a pure ground state, at least one of the following holds:

1. For every integer \(a\), \(\rho|_{\mathfrak A_{L_a}}\) and \(\omega|_{\mathfrak A_{L_a}}\) are disjoint, and
   \(\|\rho-\omega\|_{L_a}=2\).
2. For every integer \(a\), \(\rho|_{\mathfrak A_{R_a}}\) and \(\omega|_{\mathfrak A_{R_a}}\) are disjoint, and
   \(\|\rho-\omega\|_{R_a}=2\).

Both alternatives may hold. In particular, if a pure ground state satisfies
\[
 \|\rho-\omega\|_{L_a}<2,\qquad
 \|\rho-\omega\|_{R_b}<2                              \tag{4}
\]
for some integers \(a,b\), then \(\rho=\omega\). The integers need not coincide or be adjacent.

In the right-hand alternative, for every fixed \(a\),
\[
 \lim_{m\to\infty}\|\rho_{[a,m]}-\omega_{[a,m]}\|_1=2.
                                                               \tag{5}
\]
In the left-hand alternative the analogous limit holds on \([-m,a]\). Thus a witness can lie in a single connected interval entirely beyond any prescribed cutoff. Its length is not bounded by this theorem.

## 1. The normal-sector exclusion

We record the ground-state consequence of (3) needed below. For every ground state \(\theta\), its GNS triple \((\pi_\theta,\mathcal H_\theta,\Omega_\theta)\) has a strongly continuous implementing group
\[
 e^{itK_\theta}\pi_\theta(A)e^{-itK_\theta}
      =\pi_\theta(\alpha_t(A)),\qquad
 K_\theta\geq0,\qquad K_\theta\Omega_\theta=0.             \tag{6}
\]
Here are details for the passage from the local test to (6). Applying (2) to \(1+zB\) for all complex \(z\) forces \(\theta(D(B))=0\). If every bond norm is at most \(J\) and \(A\) is supported on \(\ell\) sites, nested commutators obey
\[
 \|D^n(A)\|\leq(4J)^n\frac{(n+\ell)!}{\ell!}\|A\|.       \tag{7}
\]
At step \(k\) there are at most \(\ell+2k+1\leq2(k+\ell+1)\) overlapping bonds and each commutator costs at most \(2J\). Multiplying proves (7). The resulting local power series converges for \(|t|<1/(4J)\). Every \(D^n(A)\) is local, so stationarity of all its coefficients proves invariance of \(\theta\) for small times; the group law gives all times. Invariance constructs the implementing group on cyclic vectors. On local vectors,
\[
 K_\theta\pi_\theta(A)\Omega_\theta
       =\pi_\theta(D(A))\Omega_\theta.
\]
Bound (7) makes these vectors analytic. The analytic-vector essential-self-adjointness theorem makes their span a core. The test (2) gives positivity on this core, hence positivity of the implementing generator. Applying the same core argument to (3) gives
\[
 K_\omega\geq\gamma(1-P_\Omega),\qquad
 \ker K_\omega=\mathbb C\Omega_\omega,
 \quad P_\Omega=|\Omega_\omega\rangle\langle\Omega_\omega|.
                                                               \tag{8}
\]

Suppose a ground state \(\eta\) is normal in \(\pi_\omega\), so
\(\eta(A)=\operatorname{Tr}(T\pi_\omega(A))\) for positive trace-class \(T\) of trace one. Write
\(T=\sum_j\lambda_j|\psi_j\rangle\langle\psi_j|\), omitting zero eigenvalues. For \(F\in C_c^\infty((-\infty,0))\), choose the Schwartz function \(f\) with
\[
 F(s)=\int f(t)e^{its}\,dt,\qquad
 A_f=\int f(t)\alpha_t(A)\,dt.                            \tag{9}
\]
Equation (6) implies \(\pi_\theta(A_f)\Omega_\theta=F(K_\theta)\pi_\theta(A)\Omega_\theta=0\) for every ground state. Apply this to \(\eta\). Positivity of the trace summands yields \(\pi_\omega(A_f)\psi_j=0\) for every \(j\). Pair with \(\Omega_\omega\); covariance gives
\[
 \langle\Omega_\omega,\pi_\omega(A)F(-K_\omega)\psi_j\rangle=0.
                                                               \tag{10}
\]
Cyclicity of \(\Omega_\omega\), with \(A^*\) ranging over \(\mathfrak A\), implies \(F(-K_\omega)\psi_j=0\). Choose such functions positive on \([-n,-1/n]\), \(n\geq2\). These tests remove the spectral components with energy in \([1/n,n]\), whose union is \((0,\infty)\). Equations (6) and (8) then give \(\psi_j\in\mathbb C\Omega_\omega\). Thus
\[
 \eta\text{ a ground state normal in }\pi_\omega
       \quad\Longrightarrow\quad\eta=\omega.             \tag{11}
\]
This is the normal-sector lemma of rounds 4 and 5. The sign in (10) is fixed by (9); on \(K=\operatorname{diag}(0,E)\), the operator \(|0\rangle\langle1|\) evolves with frequency \(-E\).

## 2. The split representation of the reference state

We use Taku Matsui, *Boundedness of Entanglement Entropy, and Split Property of Quantum Spin Chains*, [arXiv:1109.5778, Corollary 1.6](https://arxiv.org/pdf/1109.5778). For a bounded finite-range spin interaction, its GNS gap assumption (1.3) is exactly (3). The conclusion is the split property between the two half-chains. Its definition and the type I formulation are given in Definition 1.3 and Section 2. Unique finite-volume ground states are not an assumption.

At the cut \(L_0,R_1\), purity of \(\omega\) and this split property give Hilbert spaces \(\mathcal H_L,\mathcal H_R\) such that, after a unitary identification,
\[
 \begin{split}
 \mathcal H_\omega&=\mathcal H_L\otimes\mathcal H_R,\\
 \pi_\omega(\mathfrak A_{L_0})''&=B(\mathcal H_L)\otimes1,\\
 \pi_\omega(\mathfrak A_{R_1})''&=1\otimes B(\mathcal H_R).
 \end{split}                                                 \tag{12}
\]
To explain the role of purity, a split inclusion supplies an intermediate type I factor and hence a spatial tensor decomposition with the two algebras contained in the two tensor factors. If either contained algebra had a non-scalar commutant on its factor, that commutant would commute with both halves. It would therefore commute with all of \(\pi_\omega(\mathfrak A)\). Purity makes that commutant scalar. The bicommutant theorem forces each contained algebra to be the entire corresponding \(B(\mathcal H_h)\), proving (12). No finite-block density matrix is assumed to be pure. Write \(\pi_L,\pi_R\) for the half-chain representations in (12).

## 3. Half-chain sectors of a pure state

Let \(\rho\) be any pure state, not yet assumed to be a ground state, and write \(\pi=\pi_\rho\) on \(\mathcal K\). Put
\[
 N_L=\pi(\mathfrak A_{L_0})'',\qquad
 N_R=\pi(\mathfrak A_{R_1})''.
\]
These algebras commute and generate \(B(\mathcal K)\), since \(\rho\) is pure. If \(Z\) belongs to the center of \(N_L\), it commutes with \(N_L\) by definition and with \(N_R\) because the two algebras commute. Hence \(Z\) commutes with \(B(\mathcal K)\), so it is scalar. Thus \(N_L\) is a factor. The same argument makes \(N_R\) a factor.

The representation of either half on all of \(\mathcal K\) is quasi-equivalent to the GNS representation of that half's marginal. Indeed, let \(\mathcal K_h=\overline{\pi(\mathfrak A_h)\Omega_\rho}\). It is reducing for \(N_h\), and compression to it is a nonzero normal representation of \(N_h\). The kernel of a normal representation is a weakly closed two-sided ideal, hence a central summand. Since \(N_h\) is a factor and the compression is nonzero, its kernel is zero. The compression therefore gives a faithful normal isomorphism onto the marginal GNS von Neumann algebra. The same observation applies to the reference marginal, including when its reduced density operator in (12) has a kernel.

Recall the representation-theoretic dichotomy being used here. A representation \(\nu\) of a C*-algebra \(C\) extends to a normal surjection
\[
 \bar\nu:C^{**}\longrightarrow\nu(C)'',\qquad
 \ker\bar\nu=(1-z_\nu)C^{**}
\]
for a central projection \(z_\nu\). On \(z_\nu C^{**}\) it is an isomorphism. If the image is a factor, the center of this summand is scalar, so \(z_\nu\) is a minimal nonzero central projection. Two such projections are equal or orthogonal. Equality gives quasi-equivalence, meaning the normal isomorphism intertwining the original represented observables; orthogonality gives disjointness. Consequently two factor representations are either quasi-equivalent or disjoint.

Suppose that neither marginal of \(\rho\) is disjoint from its reference marginal at this cut. The preceding factor argument gives normal isomorphisms
\[
 q_L:B(\mathcal H_L)\longrightarrow N_L,\qquad
 q_R:B(\mathcal H_R)\longrightarrow N_R,
 \quad q_h(\pi_h(A))=\pi(A).                              \tag{13}
\]
Normality in this statement matters; mere abstract isomorphisms of factors would not suffice.

## 4. Joining the two normal half representations

For clarity, the type I representation argument is explicit. If \(q:B(\mathcal H_0)\to B(\mathcal K_0)\) is a normal unital representation, choose matrix units \(e_{ij}\) on \(\mathcal H_0\). Normality gives \(\sum_iq(e_{ii})=1\) strongly. Put \(\mathcal V=q(e_{11})\mathcal K_0\). The map
\[
 e_i\otimes v\longmapsto q(e_{i1})v
\]
is isometric by the matrix-unit relations and onto by that strong sum. It is a unitary from \(\mathcal H_0\otimes\mathcal V\) onto \(\mathcal K_0\), and it identifies \(q(x)\) with \(x\otimes1\). Equality for arbitrary \(x\) follows from equality on matrix units by normality.

Apply this to \(q_L\) in (13). It gives \(\mathcal K=\mathcal H_L\otimes\mathcal V\) and \(q_L(x)=x\otimes1\). Since \(q_R(y)\) commutes with every \(q_L(x)\), it has the form \(1\otimes r(y)\). The map \(r\) is a normal unital representation of \(B(\mathcal H_R)\). Normality follows, for example, by taking a vector slice on \(B(\mathcal H_L)\) of the normal map \(q_R\). Apply the same matrix-unit construction to \(r\). There is a Hilbert space \(\mathcal E\) such that
\[
 \mathcal K=\mathcal H_L\otimes\mathcal H_R\otimes\mathcal E,
 \qquad
 \pi(A_LA_R)=\pi_L(A_L)\otimes\pi_R(A_R)\otimes1.
                                                               \tag{14}
\]
Products of the two half-chain algebras have norm-dense linear span in \(\mathfrak A\). Thus (14) identifies \(\pi\) as an amplification of \(\pi_\omega\) on the full algebra. In particular, the partial trace of \(|\Omega_\rho\rangle\langle\Omega_\rho|\) over \(\mathcal E\) is a positive trace-class operator of trace one representing \(\rho\) in \(\pi_\omega\).

If \(\rho\) is a ground state, (11) now gives \(\rho=\omega\). Its contrapositive proves that a distinct pure ground state is disjoint from \(\omega\) on at least one half at the cut \(L_0,R_1\). No gap or split property of \(\rho\) has been used.

There is a second check of the normality step in (14). Work directly with the two commuting normal maps in (13). Choose increasing finite-rank projections \(P_n\uparrow1\) on \(\mathcal H_L\) and \(Q_n\uparrow1\) on \(\mathcal H_R\). Put \(r_n=q_L(P_n)q_R(Q_n)\). These are projections converging strongly to one. The positive functional
\[
 \eta_n(A)=\langle r_n\Omega_\rho,\pi(A)r_n\Omega_\rho\rangle
\]
factors through the finite matrix corner on \(P_n\mathcal H_L\otimes Q_n\mathcal H_R\). For a product observable its compressed operator is precisely the image of
\(P_n\pi_L(A_L)P_n\otimes Q_n\pi_R(A_R)Q_n\); finite-dimensional matrix algebra duality therefore gives a positive density operator on this corner representing \(\eta_n\). Its extension by zero represents a normal positive functional in \(\pi_\omega\). Meanwhile
\[
 \|\rho-\eta_n\|\leq2\|\Omega_\rho-r_n\Omega_\rho\|\longrightarrow0.
\]
Normal functionals in a fixed representation form a norm-closed linear subspace of the algebra's dual: restriction from the von Neumann predual is isometric by Kaplansky density, and that predual is complete. Thus \(\rho\) is normal. This obtains the same conclusion by finite-rank approximation instead of the second spatial matrix-unit decomposition.

## 5. The same direction persists after every cutoff

We need disjointness, not merely orthogonality of two state functionals. Disjointness is preserved when a finite set of sites is removed from a half-chain. Here is the finite matrix argument, including its application to marginal GNS representations.

Let \(C=M_d\otimes B\). Every nondegenerate representation \(\nu\) of \(C\) can, by its matrix units, be written
\[
 \nu(a\otimes b)=a\otimes\eta(b).
\]
The extension to \(C^{**}=M_d\otimes B^{**}\) acts entrywise. If \(z_\eta\) is the central support of \(\eta\), its kernel is the matrices with entries in \((1-z_\eta)B^{**}\). Hence
\[
 z_\nu=1\otimes z_\eta.                                  \tag{15}
\]
Disjoint representations of \(C\) therefore give disjoint representations \(\eta\) of \(B\).

An independent check uses intertwiners. For two representations \(\mathrm{id}_{M_d}\otimes\eta_j\), an intertwiner of the full algebra must commute with the matrix units, so it is \(1_d\otimes T\), with \(T\eta_1(b)=\eta_2(b)T\). An intertwiner of the restrictions to \(B\) is a \(d\)-by-\(d\) matrix whose entries satisfy that same relation. Hence a nonzero intertwiner exists for the full representations exactly when one exists for their restrictions. This proves preservation of disjointness without the bidual identity (15).

If \(\nu\) is the GNS representation of a state \(\theta\), expand its cyclic vector as \(\sum_{i=1}^d e_i\otimes\xi_i\). Cyclicity says that the span of \(\eta(B)\xi_i\), over all \(i\), is dense in the second factor. The restricted state is \(\sum_i\langle\xi_i,\eta(\cdot)\xi_i\rangle\). Its normal functional has full central support in \(\eta(B)''\): a central projection killing it kills every \(\xi_i\) and then their dense cyclic span. Thus the restricted state's GNS representation is quasi-equivalent to \(\eta\). Equation (15) consequently proves the assertion for the restricted states themselves.

Suppose the disjoint half at the original cut is \(R_1\). Removing sites \([1,a-1]\), for \(a>1\), proves disjointness on \(R_a\). For \(a\leq1\), disjointness on the smaller half \(R_1\) also implies disjointness on \(R_a\): any intertwiner on the larger algebra would intertwine its restriction to the smaller one, where there are no nonzero intertwiners. Equivalently the restrictions of the larger GNS representations are amplifications of the smaller marginal representations by the finite matrix argument. This proves disjointness on every \(R_a\). The proof for \(L_0\) is identical, deleting finitely many sites when the cutoff moves left and enlarging the half when it moves right.

Disjoint states have norm distance two. To see the constant directly, their normal extensions to the bidual have orthogonal central supports \(z_1,z_2\). The self-adjoint contraction \(z_1-z_2\) has difference of expectations two. Extension to the bidual preserves functional norm, and the triangle inequality bounds the distance above by two. Alternatively the difference has mutually singular positive and negative parts of mass one each. These two calculations agree. This proves the norm statements in the theorem and their contrapositive (4).

The increasing finite algebras on \([a,m]\) have norm-dense union in \(\mathfrak A_{R_a}\). The norms of a functional restricted to them therefore increase to its half-chain norm. On a finite matrix algebra the functional norm is the trace norm of its density matrix, by operator-norm/trace-norm duality. This proves (5), and the left limit follows in the same way. In particular, for every \(\varepsilon>0\) a local effect \(0\leq E\leq1\) in the appropriate half can be chosen with
\[
 \rho(E)>1-\varepsilon,\qquad\omega(E)<\varepsilon.
                                                               \tag{16}
\]
Indeed choose a sufficiently large interval in (5) with trace distance greater than \(2(1-\varepsilon)\), and let \(E\) be the positive spectral projection of the difference of its density matrices. That difference has trace zero, so its positive mass is half its trace norm. Thus \(\rho(E)-\omega(E)>1-\varepsilon\), which implies both inequalities in (16).

## 6. Tests of the conclusions and of stronger claims

The two-level ferromagnetic Ising chain provides an actual ground-state test:
\[
 h_{x,x+1}=\tfrac12(1-Z_xZ_{x+1}),\qquad
 H_{\mathrm I}=\sum_xh_{x,x+1}.
                                                               \tag{17}
\]
Let \(\omega_0\) be the all-zero product state and \(\kappa\) the product state with zeros on \(L_0\) and ones on \(R_1\), where \(Z|0\rangle=|0\rangle\) and \(Z|1\rangle=-|1\rangle\). Both states are pure: each finite marginal has rank one, so any convex decomposition must agree on every local algebra. Product states also have the spatial split representation.

The state \(\omega_0\) obeys (3) with \(\gamma=2\). In its GNS space, the vectors indexed by finite flipped subsets \(F\) form an orthonormal basis. Their energies count the bonds with exactly one endpoint in \(F\). For nonempty finite \(F\), this count is twice the number of its connected components, hence at least two; for \(F=\varnothing\) it is zero. A single finite interval attains two. This diagonal implementing Hamiltonian gives exactly the inequality (3).

The kink \(\kappa\) is a ground state, although it has one unfavorable bond. For any local \(B\), choose an interval \([u,v]\) containing its support. The bonds that can change are \((u-1,u),\ldots,(v,v+1)\). Keep the two exterior endpoint spins fixed at their values in the product configuration. The diagonal Hamiltonian on these bonds counts walls. If the endpoint spins agree its minimum is zero; if they disagree its minimum is one, since the wall count has odd parity. The original kink has exactly that minimum in this interval: zero walls if the interval misses the kink bond, and one otherwise. Denote the minimum by \(e\) and this finite Hamiltonian by \(H_{u,v}\). Acting on the local product vector \(\xi\),
\[
 \kappa(B^*[H_{\mathrm I},B])
   =\langle B\xi,(H_{u,v}-e)B\xi\rangle\geq0.
                                                               \tag{18}
\]
Other bonds commute with \(B\). This proves the full local-stability condition, including non-diagonal \(B\), rather than checking only classical flips.

The left marginal of \(\kappa\) agrees with \(\omega_0\) on every \(L_a\) with \(a\leq0\). For every \(a\), however, \(R_a\) contains a site \(x\geq1\) where the projection \(|1\rangle\langle1|_x\) has expectations one and zero. Thus its right norm distance is two. Right disjointness can also be checked independently: in the all-zero right GNS space, projections onto all-one spins on \([\max(a,1),m]\) converge strongly to zero, since they eventually annihilate every finite-excitation basis vector. Every normal state has expectations tending to zero, while \(\kappa\) assigns them one. The factor dichotomy in Section 3 then makes the representations disjoint. This confirms the fixed right direction and disproves a claim that both directions must work.

Purity of the competitor cannot be dropped from criterion (4). For \(0<p<1\),
\[
 \rho_p=p\omega_0+(1-p)\kappa
                                                               \tag{19}
\]
is a ground state by (2). Its distance on every \(L_a\), \(a\leq0\), is zero. Its distance on every \(R_b\) is \(2(1-p)<2\): convexity gives the upper bound, and a one-site \(Z_x\) at \(x\geq\max(1,b)\) gives the same lower bound. Independently the one-site density-matrix difference is diagonal with eigenvalues \(1-p,-(1-p)\), whose absolute values sum to the same number. Thus two half-chain distances strictly below two do not imply equality for mixed ground states. This Ising model is not a counterexample to translation-invariant uniqueness in the Heisenberg model.

It would also be incorrect to replace disjointness by norm distance two in the finite-deletion argument. Two orthogonal vectors in the same finite-dimensional representation have distance two and can become identical after that finite factor is removed. Indeed the kink and vacuum on \(L_1\) differ at just site 1, have distance two, and become identical on \(L_0\). Section 5 uses disjoint representation sectors, which excludes this failure.

The split property is used only for the reference state in (12)–(14). No clustering, gap, translation invariance or split property of the competitor is assumed. Without the spatial type I factors, the matrix-unit gluing argument is unavailable. The theorem supplies a half-chain criterion; it does not prove (4) for any hypothetical Heisenberg competitor. The fixed-block density estimates of round 3 provide no bound uniform in the interval length in (5). Unrestricted uniqueness and the general integer-spin assertion remain unresolved here.
