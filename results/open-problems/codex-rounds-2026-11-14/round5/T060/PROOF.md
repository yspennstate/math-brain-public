# Removing a finite interval cannot hide a competing ground state

Let \(\mathfrak A\) be the quasi-local algebra of a chain with a finite-dimensional spin at each site. Let \(\alpha_t\) be the dynamics of a bounded nearest-neighbor interaction, with
\[
 \left.\frac{d}{dt}\alpha_t(A)\right|_{t=0}=iD(A),\qquad
 D(A)=[H,A]
\]
for local \(A\). A ground state satisfies
\[
 \rho(B^*D(B))\geq0\qquad(B\text{ local}).                 \tag{1}
\]
The commutator in (1) is a finite sum. No infinite Hamiltonian is taken to be an element of \(\mathfrak A\).

Assume that a ground state \(\omega\) obeys
\[
 \omega(A^*D(A))\geq\gamma\bigl(\omega(A^*A)-|\omega(A)|^2\bigr)
 \qquad(A\text{ local}),\quad\gamma>0.                    \tag{2}
\]
For the spin-1 Heisenberg chain this is an external premise from Hal Tasaki, *On the uniqueness of translation-invariant ground states of the S=1 Heisenberg and J–D antiferromagnetic chains*, [arXiv:2610.34330v2, Theorem 2.1, equation (2.12)](https://arxiv.org/html/2610.34330v2). The finite numerical inputs underlying that theorem are not verified here. No other conclusion of that theorem is needed below.

For a finite interval \(I\), let \(\mathfrak A_{I^c}\) be the norm closure of the local observables supported in its complement. It includes joint observables on both sides of \(I\). For a functional \(f\), set
\[
 \|f\|_{I^c}=\sup\{|f(A)|:A\in\mathfrak A_{I^c},\ \|A\|\leq1\}.
                                                               \tag{3}
\]
State distances have no factor of one half.

**Theorem.** Every ground state \(\rho\) has a decomposition
\[
 \rho=p\omega+(1-p)\sigma,\qquad 0\leq p\leq1,             \tag{4}
\]
where, if \(p<1\), \(\sigma\) is a ground state disjoint from the GNS representation of \(\omega\). The coefficient \(p\) is uniquely determined. For every finite interval \(I\),
\[
 \boxed{\quad\|\rho-\omega\|_{I^c}=\|\rho-\omega\|=2(1-p).\quad} \tag{5}
\]
Consequently, if \(\|\rho-\omega\|_{I_n^c}\to0\) for expanding finite intervals, then \(\rho=\omega\). If \(\rho\) is pure and differs from \(\omega\), its distance from \(\omega\) on every such complement is two.

There is a finite-matrix formulation. With \(I_n=[-n,n]\cap\mathbb Z\) and \(J_{n,m}=I_m\setminus I_n\), for every fixed \(n\geq0\),
\[
 \lim_{m\to\infty}\|\rho_{J_{n,m}}-\omega_{J_{n,m}}\|_1
       =\|\rho-\omega\|.                                     \tag{5a}
\]
The reduced density matrices here live on two separated finite intervals.

## 1. Ground-state implementers and the normal-sector lemma

Write \((\pi_\theta,\mathcal H_\theta,\Omega_\theta)\) for the GNS representation of a ground state. Its dynamics is implemented by
\[
 V_\theta(t)=e^{itK_\theta},\qquad K_\theta\geq0,\qquad
 K_\theta\Omega_\theta=0,\qquad
 K_\theta\pi_\theta(A)\Omega_\theta
       =\pi_\theta(D(A))\Omega_\theta.                         \tag{6}
\]
Here is a justification of the characterization used in (6). Testing (1) on \(1+zA\) for arbitrary small complex \(z\) gives \(\theta(D(A))=0\). Local observables are analytic for sufficiently small times. For nearest-neighbor bond norm at most \(J\), support length \(\ell\), and integer \(n\geq0\), a sufficient bound is
\[
 \|D^n(A)\|\leq(4J)^n\frac{(n+\ell)!}{\ell!}\|A\|.        \tag{7}
\]
There are at most \(\ell+2k+1\) overlapping bonds at step \(k\), each commutator costs at most \(2J\), and \(\ell+2k+1\leq2(k+\ell+1)\); multiplication proves (7). Since \(D^{n-1}(A)\) is local, stationarity also gives \(\theta(D^n(A))=0\) for every \(n\geq1\). Dividing (7) by \(n!\) shows that the norm power series for \(\alpha_t(A)\) converges for \(|t|<1/(4J)\). Thus this series proves invariance of \(\theta\) for small times, and the group law gives invariance for all times. Invariance constructs \(V_\theta(t)\) by sending \(\pi_\theta(A)\Omega_\theta\) to \(\pi_\theta(\alpha_t(A))\Omega_\theta\); invariance of the state makes this isometric, invertibility makes it unitary, and norm continuity of the dynamics makes it strongly continuous. Differentiation gives the last equation in (6). The local GNS vectors are analytic by (7), and their linear span is invariant under the generator because \(D(A)\) is local. The analytic-vector essential-self-adjointness theorem makes this span a core. Condition (1) makes its quadratic form nonnegative on that core. Graph-norm approximation gives nonnegativity on the full operator domain, and the spectral theorem then gives \(K_\theta\geq0\). Invariance also gives \(K_\theta\Omega_\theta=0\). This proves (6).

For \(\theta=\omega\), (2) on the same core gives
\[
 K_\omega\geq\gamma(1-|\Omega_\omega\rangle\langle\Omega_\omega|),
 \qquad \ker K_\omega=\mathbb C\Omega_\omega.                 \tag{8}
\]

The normal-sector lemma from round 4 can be re-derived as follows. A state normal in \(\pi_\omega\) is represented by a positive trace-class operator \(T\) of trace one. Purify \(T\) to a unit vector \(\Psi\in\mathcal H_\omega\otimes\mathcal L\). For \(F\in C_c^\infty(( -\infty,0))\), choose a Schwartz function \(f\) with
\[
 F(s)=\int_{\mathbb R}f(t)e^{its}\,dt,
 \qquad A_f=\int_{\mathbb R}f(t)\alpha_t(A)\,dt.             \tag{9}
\]
By (6), \(\pi_\theta(A_f)\Omega_\theta=F(K_\theta)\pi_\theta(A)\Omega_\theta=0\) in every ground-state representation. If the state represented by \(T\) is a ground state, this implies
\[
 (\pi_\omega(A_f)\otimes1)\Psi=0.                           \tag{10}
\]
Pairing the first tensor factor with \(\Omega_\omega\), covariance and \(K_\omega\Omega_\omega=0\) turn (10) into
\[
 \bigl(\langle\Omega_\omega|\pi_\omega(A)F(-K_\omega)
       \otimes1\bigr)\Psi=0.                                \tag{11}
\]
The vectors \(\pi_\omega(A)^*\Omega_\omega\) are dense by cyclicity. Pairing also with any vector of \(\mathcal L\) therefore yields
\((F(-K_\omega)\otimes1)\Psi=0\).
Choose such functions positive on \([-n,-1/n]\) for each integer \(n\geq2\). The spectral theorem removes all components of \(\Psi\) with first-factor energy in \([1/n,n]\); these intervals cover \((0,\infty)\). Equations (6) and (8) imply
\(\Psi\in\mathbb C\Omega_\omega\otimes\mathcal L\).
Its state is \(\omega\). Thus:

**Normal-sector lemma.** Every ground state normal in \(\pi_\omega\) equals \(\omega\).

Neither the lemma nor the finite-interval argument below requires purity of \(\omega\).

## 2. Splitting off the normal component preserves the ground-state condition

The bidual \(\mathfrak A^{**}\) is the enveloping von Neumann algebra. Every functional on \(\mathfrak A\) has a unique normal extension to it, with the same norm. Every nondegenerate representation \(\pi\) extends to a normal surjection
\(\bar\pi:\mathfrak A^{**}\to\pi(\mathfrak A)''\).
Its kernel is \((1-z_\pi)\mathfrak A^{**}\) for a central projection \(z_\pi\); restriction to \(z_\pi\mathfrak A^{**}\) is an isomorphism onto \(\pi(\mathfrak A)''\). A positive functional is normal in \(\pi\) precisely when its extension is supported on \(z_\pi\). Functionals supported on \(1-z_\pi\) are disjoint from \(\pi\). These facts follow by taking the weakly closed kernel of the normal extension; weakly closed two-sided ideals of a von Neumann algebra are its central summands.

Put \(z=z_{\pi_\omega}\). The covariance in (6) implies that the extension \(\bar\alpha_t\) preserves \(\ker\bar\pi_\omega\), since
\[
 \bar\pi_\omega(\bar\alpha_t(X))
       =e^{itK_\omega}\bar\pi_\omega(X)e^{-itK_\omega}.
\]
Hence \(\bar\alpha_t(z)=z\).

For an arbitrary ground state \(\rho\), let \(\bar\rho\) be its normal extension, and define positive functionals
\[
 \rho_{\rm n}(A)=\bar\rho(zA),\qquad
 \rho_{\rm s}(A)=\bar\rho((1-z)A),\qquad p=\bar\rho(z).       \tag{12}
\]
They have masses \(p\) and \(1-p\), and sum to \(\rho\).

Each nonzero functional in (12), after normalization, is a ground state. To verify this rather than infer it from convexity, work in the GNS representation of \(\rho\). The projection
\(Z=\bar\pi_\rho(z)\) is central in \(\pi_\rho(\mathfrak A)''\) and commutes with \(e^{itK_\rho}\), because \(z\) is invariant. Therefore
\[
 \psi=Z\Omega_\rho\in\ker K_\rho,
 \qquad
 \rho_{\rm n}(A)=\langle\psi,\pi_\rho(A)\psi\rangle.         \tag{13}
\]
For local \(B\), norm differentiability of \(\alpha_t(B)\) gives the bounded commutator
\([K_\rho,\pi_\rho(B)]=\pi_\rho(D(B))\) on the domain of \(K_\rho\), and \(\pi_\rho(B)\) preserves that domain. Indeed, for \(v\) in this domain, use
\(e^{itK_\rho}\pi_\rho(B)v=\pi_\rho(\alpha_t(B))e^{itK_\rho}v\)
and differentiate at zero. The derivative exists and equals
\(i\pi_\rho(D(B))v+i\pi_\rho(B)K_\rho v\).
Applying the commutator identity to \(\psi\) gives
\[
 \rho_{\rm n}(B^*D(B))
   =\langle\pi_\rho(B)\psi,K_\rho\pi_\rho(B)\psi\rangle
   \geq0.                                                     \tag{14}
\]
Replacing \(Z\) by \(1-Z\) proves the same statement for \(\rho_{\rm s}\).

By construction \(\rho_{\rm n}/p\), when \(p>0\), is normal in \(\pi_\omega\). The lemma gives \(\rho_{\rm n}=p\omega\). When \(p<1\), set \(\sigma=\rho_{\rm s}/(1-p)\). This proves (4) including the ground-state and disjointness assertions. Also \(p\) is the largest coefficient \(q\) for which \(\rho-q\omega\) is positive. One direction follows from (4). Conversely positivity extends to the bidual, where evaluation on \(z\) gives \(p-q\geq0\). This proves uniqueness of the coefficient without choosing a representation for \(\rho\).

## 3. Removing a finite matrix factor preserves the sector weight

Fix \(I\), put \(\mathfrak B=\mathfrak A_{I^c}\), and let \(d\) be the Hilbert-space dimension on \(I\). Regrouping tensor factors gives
\[
 \mathfrak A=M_d\otimes\mathfrak B,
 \qquad \mathfrak A^{**}=M_d\otimes\mathfrak B^{**}.          \tag{15}
\]
The second identity holds because the first factor is finite dimensional: both algebras consist of \(d\)-by-\(d\) matrices with entries in the indicated algebra.

The matrix units of \(M_d\) identify the Hilbert space and representation as
\[
 \mathcal H_\omega=\mathbb C^d\otimes\mathcal K,
 \qquad \pi_\omega(a\otimes b)=a\otimes\eta(b),              \tag{16}
\]
where \(\eta\) is a representation of \(\mathfrak B\). Explicitly, take \(\mathcal K=\pi_\omega(e_{11})\mathcal H_\omega\) and send \(e_i\otimes v\) to \(\pi_\omega(e_{i1})v\). The matrix-unit relations make this map unitary and give (16). No irreducibility is needed.

Let \(z_{\mathfrak B}\) be the central projection of \(\eta\) in \(\mathfrak B^{**}\). The extension in (16) acts entry by entry. Its kernel consists of matrices whose entries lie in \((1-z_{\mathfrak B})\mathfrak B^{**}\). Comparing kernels with the definition of \(z\) proves
\[
 z=1_d\otimes z_{\mathfrak B}.                               \tag{17}
\]
The restriction \(\omega|_{\mathfrak B}\) is normal in \(\eta\): expand its GNS vector in the finite \(\mathbb C^d\) factor to obtain a sum of at most \(d\) vector functionals. In particular its extension takes value one on \(z_{\mathfrak B}\). Equations (12) and (17) give
\[
 \bar\rho|_{\mathfrak B^{**}}(z_{\mathfrak B})=p,
 \qquad
 \bar\omega|_{\mathfrak B^{**}}(z_{\mathfrak B})=1.           \tag{18}
\]
Thus the same weight \(p\) survives deletion of \(I\). When \(p<1\), the restriction of \(\sigma\) is supported on \(1-z_{\mathfrak B}\); it cannot acquire a component normal in \(\eta\) after the deletion.

## 4. Norm identity and local distinguishing measurements

The convex decomposition (4) gives
\(\|\rho-\omega\|_{I^c}\leq2(1-p)\) and
\(\|\rho-\omega\|\leq2(1-p)\).
The contraction \(2z_{\mathfrak B}-1\) in the bidual of the complement algebra gives, by (18),
\[
 |(\bar\rho-\bar\omega)(2z_{\mathfrak B}-1)|=2(1-p).         \tag{19}
\]
Normal extension to the bidual preserves the norm of a functional. Equivalently, its unit ball is weak-* approximated by the unit ball of the original algebra, and the extended functional is weak-* continuous. Therefore (19) is a lower bound for the supremum in (3). Together with the upper bounds and restriction of functionals, this proves (5). It also covers \(p=0\) and \(p=1\).

To obtain (5a), the finite matrix algebras on \(J_{n,m}\) increase with \(m\), and their union is norm dense in \(\mathfrak A_{I_n^c}\). The norm of a functional restricted to them therefore increases to its norm on that complement. On each finite matrix algebra, the functional norm is the trace norm of the difference of the density matrices, by duality between matrix operator norm and trace norm. Equation (5) identifies the limit and proves (5a).

If \(\rho\) is pure and \(p>0\), (4) and extremality force \(\rho=\omega\). Consequently a distinct pure ground state has \(p=0\), as asserted.

For such a distinct pure state, for every \(\varepsilon>0\) and finite interval \(I\), there is a positive local contraction \(E\) supported in \(I^c\) with
\[
 \rho(E)>1-\varepsilon,\qquad \omega(E)<\varepsilon.         \tag{20}
\]
Indeed the effect \(1-z_{\mathfrak B}\) has expectations one and zero. The effects of \(\mathfrak B\) are weak-* dense in the effects of \(\mathfrak B^{**}\): approximate the self-adjoint contraction \(2(1-z_{\mathfrak B})-1\) by self-adjoint contractions and rescale. Choose an effect with difference of expectations greater than \(1-\varepsilon/2\). Approximate it in norm, while preserving positivity and its norm bound, by a local effect: the conditional expectation onto finitely many sites, taking normalized traces on the remaining sites, is positive, unital, contractive, and converges in norm to the identity on \(\mathfrak B\). With approximation error less than \(\varepsilon/4\), the resulting local difference exceeds \(1-\varepsilon\). Since both expectations lie in \([0,1]\), (20) follows.

For any ground state, (5) also says that a discrepancy seen on a central block can be recovered to arbitrary accuracy by a finite observable outside any prescribed interval. The required observable can have large, disconnected support. Nothing here bounds its support size.

## 5. Checks and limits

The normalization in (5) has two independent checks. First, (19) gives its value from the sector projection. Second, for \(p<1\), normal and disjoint positive functionals have orthogonal central supports. The positive and negative parts of
\((\rho-\omega)|_{\mathfrak B}=(1-p)(\sigma-\omega)|_{\mathfrak B}\)
therefore each have mass \(1-p\). The norm is their sum, \(2(1-p)\). In a two-sector matrix model with orthogonal unit vectors \(v,w\), the difference
\(p|v\rangle\langle v|+(1-p)|w\rangle\langle w|-|v\rangle\langle v|\)
has eigenvalues \(1-p\) and \(-(1-p)\), giving the same value directly.

An independent spin-chain check uses the two-level ferromagnetic Ising interaction
\[
 h_{x,x+1}=\tfrac12(1-Z_xZ_{x+1}),\qquad H_{\rm Ising}=\sum_xh_{x,x+1}.
                                                               \tag{21}
\]
Let \(\omega_0,\omega_1\) be the all-zero and all-one product states, with \(Z|0\rangle=|0\rangle\), \(Z|1\rangle=-|1\rangle\). Both are ground states: each local positive bond annihilates the product vector, so the local ground-state test is a sum of nonnegative terms \(\omega_i(B^*h_{x,x+1}B)\). In the GNS representation of \(\omega_0\), the vectors obtained by flipping a finite set \(F\) are an orthonormal basis. Their energies are the numbers of bonds with exactly one endpoint in \(F\). The energy is zero for \(F=\varnothing\) and at least two for every nonempty finite \(F\). Thus (2) holds with \(\gamma=2\), and the kernel is one dimensional.

The mixture \(\rho=p\omega_0+(1-p)\omega_1\) is a ground state. For any \(x\notin I\), the contraction \(Z_x\) has difference of expectations \(2(1-p)\) between \(\omega_0\) and \(\rho\). The convex upper bound is the same number. This checks (5) directly in a finite-range chain satisfying (2), including every \(p\in[0,1]\). It also shows that the coefficient two is sharp and that a positive normal component need not exhaust a mixed ground state. This Ising model has more than one translation-invariant ground state; it is not a counterexample to the earlier density theorem.

The sign in (11) can be checked on \(K=\operatorname{diag}(0,E)\) and \(A=|0\rangle\langle1|\). Its time evolution is \(e^{-itE}A\), and its average is \(F(-E)A\). Thus the proof tests positive-energy components with negative frequencies. A degenerate zero-energy space would invalidate the normal-sector lemma; (8) is necessary at that point.

Deletion of a finite interval uses its full matrix algebra, not a half-chain split property or a pure finite-block marginal. The restriction of \(\omega\) to the complement can be mixed. Equations (16)–(18) preserve its representation sector nevertheless. Finite dimensionality is essential to this argument; removing a half-chain is not covered by (15).

The norm on the complement in (3) is much stronger than convergence of every fixed-size block marginal. For example, on a two-level chain let \(\omega\) be the all-zero product state and let \(\nu\) be the product state with ones at sites \(2^n\), \(n\geq0\), and zeros elsewhere. For every fixed finite interval, the mean block trace distance of its translates from \(\omega\) tends to zero uniformly over interval starts. Indeed, for each fixed integer \(R\geq1\), at most \(R\) defect sites have exponent below \(R\); the remaining defect sites have gaps at least \(2^R\). Any interval of \(N\) consecutive sites therefore contains at most \(R+1+N/2^R\) defects. A block of \(\ell\) sites can meet a given defect in at most \(\ell\) translates, so the exceptional fraction is at most
\[
 \frac{\ell}{N}\left(R+1+\frac{N+\ell}{2^R}\right).         \tag{22}
\]
For fixed \(R\), take the limit superior as \(N\to\infty\), then let \(R\to\infty\). The bound vanishes. Each changed block has trace distance two, so the mean distance also vanishes. Nevertheless every finite interval has a defect outside it, and the one-site projection at that defect distinguishes \(\nu\) from \(\omega\) perfectly. Their norm distance on every complement is two. This is a counterexample to replacing (3) by a density condition, not an asserted Heisenberg ground state.

In particular, this sparse state is not a ground state of (21). At any defect with both neighboring sites zero, flipping the defect removes two unfavorable bonds. For the on-site flip unitary \(X_x\), the exact local test is \(\nu(X_x[H_{\rm Ising},X_x])=-2\). Thus this example does not evade local stability in a Hamiltonian for which the gap premise has just been checked.

Finally, a tail distance strictly less than two only forces \(p>0\). It forces equality for a pure ground state. It does not do so for a general mixed ground state: if a disjoint ground state \(\sigma\) existed, then every convex mixture \(p\omega+(1-p)\sigma\) would be a ground state and would have distance \(2(1-p)<2\) for \(0<p<1\). The zero-tail-distance criterion has no such restriction.

The theorem does not establish a tail norm estimate for an arbitrary Heisenberg ground state. It supplies a necessary condition for any competitor and a sufficient uniqueness criterion for states with norm-localized discrepancies. Unrestricted uniqueness and the general higher-spin statement remain open in this argument.
