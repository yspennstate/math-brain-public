# C0056 independent boundary derivation (w487)

Written 2026-10-10 before reading w486's ATTEMPT or proof. Parent problem status and exact primary formulation are being recovered; no solution or novelty claim is made. Independent referee: w488, pending. No response-side served-model receipt is available.

## Precise obstruction S1.487.1

For lambda>0 let H act on ell^2(Z^3) by H delta_x=lambda V_x delta_x, with V_x iid uniform on [-1,1]. There is no hopping term. Each delta_x has spectral measure delta_(lambda V_x), and every vector has a countable atomic spectral measure. Nevertheless, for every real E and eta>0,

    E Im <delta_x,(H-E-i eta)^(-1)delta_x>
    = (1/(2 lambda)) integral[-lambda,lambda] eta/((v-E)^2+eta^2) dv
    <= pi/(2 lambda).

Thus uniform annealed first-moment control of the imaginary diagonal Green function does not imply quenched absolute continuity. This is not a counterexample to the Anderson operator with its hopping term.

## Sharp integrated-moment boundary S1.487.2

Let mu_omega be a random probability Borel measure on R. Let I be a bounded open interval, 1<p<infinity, and eta_n>0 a deterministic sequence tending to zero. Set

    F_n(omega,E) = integral eta_n/((t-E)^2+eta_n^2) d mu_omega(t).

Assume joint measurability and

    sup_n E integral_I F_n(omega,E)^p dE <= C < infinity.

Then mu_omega restricted to I has an L^p density rho_omega almost surely, and

    E integral_I rho_omega(E)^p dE <= C/pi^p.

Proof. Put A_n(omega)=integral_I F_n^p. Fatou gives E liminf_n A_n<=C, so A=liminf A_n is finite almost surely. For each such omega choose a subsequence with A_n tending to A. Reflexivity of L^p(I) gives a further weakly convergent subsequence F_n -> f, with integral_I |f|^p <= A by weak lower semicontinuity. Positivity implies f>=0.

For phi in C_c(I), extend phi by zero to R. Fubini gives integral phi(E)F_n(E)dE = integral (P_eta_n*phi)(t)dmu(t), where P_eta(u)=eta/(u^2+eta^2) has mass pi. The approximate-identity property gives uniform convergence P_eta_n*phi -> pi phi, so this expression tends to pi integral phi dmu. Weak L^p convergence gives its limit integral phi f. Therefore mu restricted to I=(f/pi)dE. This density is uniquely determined, and its norm obeys integral_I rho^p <= A/pi^p. Taking expectation proves the stated bound. The sample-dependent subsequence is used only to prove each sample's measure identity; no measurable selection is assumed or needed. After samplewise ac is known, rho=(1/pi)liminf_n F_n is a jointly measurable version at almost every interior Lebesgue point, by Poisson differentiation; this also makes the density-norm expectation explicit.

For 0<p<=1, the analogous integrated bound is automatic for every probability measure:

    integral_I F_eta^p <= |I|^(1-p) (integral_I F_eta)^p
                       <= |I|^(1-p) pi^p.

The first inequality is concavity (at p=1, equality). Consequently p<=1 alone cannot imply absolute continuity: take mu=delta_0 with 0 in I. The threshold p>1 is sharp for this family of pure power-moment assumptions. This does not claim that p>1 is necessary for absolute continuity; at p=1, an additional uniform-integrability assumption can replace the power bound.

For a random self-adjoint operator on a separable Hilbert space, apply the result to each vector in a countable orthonormal basis. The intersection of these probability-one events still has probability one. On that event the operator's spectral projection annihilates every Lebesgue-null subset of I: its diagonal entries on all basis vectors vanish, so the positive projection is zero. The operator therefore has purely absolutely continuous spectral measures on I. The condition permits zero spectral mass on I; nonzero extended spectrum requires a separate nonvanishing argument.

## Exact divergent second moment S1.487.3

In the diagonal model at E=0,

    E F_eta = arctan(lambda/eta)/lambda,
    E F_eta^2 = 1/(2(lambda^2+eta^2))
               + arctan(lambda/eta)/(2 lambda eta).

Hence eta E F_eta^2 -> pi/(4 lambda), while E F_eta -> pi/(2 lambda). More generally, for |E|<lambda and p>1,

    E F_eta^p = eta^(1-p)/(2 lambda)
                * integral[(-lambda-E)/eta,(lambda-E)/eta] (1+u^2)^(-p)du,

and the integral tends to the finite positive constant integral_R (1+u^2)^(-p)du. The stronger moment diverges precisely on this atomic example, explaining why the first moment cannot substitute for it.

## Schur-complement obstruction with hopping S1.487.4

This derivation also precedes reading w486's proof. Let H=A+lambda V on ell^2(Z^3), where A is nearest-neighbor adjacency (zero diagonal), lambda>0, and V_x are iid uniform[-1,1]. Fix a site x and z=E+i eta. Conditional on all potentials except V_x, remove x and let H^(x) be the compressed operator. Let b be the adjacency vector from x to its six neighbors and set

    Sigma_x(z)=<b,(H^(x)-z)^(-1)b>,
    a=E+Re Sigma_x(z), B=eta+Im Sigma_x(z)>0.

The Schur complement gives

    Im G_xx(z)=B/((lambda V_x-a)^2+B^2).

The compression uses the entire remaining graph; neighbor Green functions are not asserted independent. Conditional on that graph, V_x is still uniform and independent, so

    E[Im G_xx(z) | all V_y, y!=x] <= pi/(2lambda).

For 1<p<infinity, writing K_p=integral_R (1+u^2)^(-p)du,

    E[(Im G_xx(z))^p | rest] <= K_p/(2lambda) B^(1-p).

On the resonance event R={|a|<=lambda/2, 0<B<=lambda/2}, the reverse bound

    E[(Im G_xx(z))^p | rest] >= 2^(-p)/lambda * B^(1-p)

holds. Proof: the interval [a-B,a+B] is inside [-lambda,lambda]; on it the integrand is at least 2^(-p)B^(-p), over a length 2B with uniform density 1/(2lambda). The upper bound follows by extending the integration to R and substituting u=(v-a)/B.

Consequently, a uniform bound E integral_I (Im G_xx)^p <= C forces

    E integral_I 1_R B^(1-p) <= 2^p lambda C.

Conversely a uniform bound on E integral_I B^(1-p) is sufficient, with the displayed upper-bound constant. Since only B>=eta is automatic, spectral averaging alone yields the divergent upper bound K_p |I|/(2lambda) eta^(1-p), not the eta-uniform p>1 criterion. The missing estimate concerns the inverse imaginary width of the entire deleted-site bath. No independence between its six neighbor contributions is available merely from iid site potentials.

## Absolute continuity does not supply GOE statistics S1.487.5

The recovered intake C0056 statement asks for both absolutely continuous spectrum and GOE local statistics of finite-volume restrictions. These are separate obligations.

Let A be nearest-neighbor adjacency on Z^3 with lambda=0. Fourier transform identifies A with multiplication on T^3 by h(theta)=2 sum_{j=1}^3 cos(theta_j). All spectral measures are absolutely continuous: outside the eight points where all sin(theta_j)=0, at least one coordinate derivative is nonzero. Cover this complement by countably many coordinate patches on which the corresponding one-dimensional change of variables is nonsingular. Fubini and change of variables show that the inverse image of every Lebesgue-null energy set has Haar measure zero. The critical set is finite and hence has Haar measure zero. The same holds after weighting by any |Fourier(psi)|^2 in L^1(T^3).

For periodic boxes of odd side length L, however, eigenvalues are

    h_L(k)=2 sum_{j=1}^3 cos(2 pi k_j/L), k in (Z/LZ)^3.

The involution k -> -k preserves h_L, and its only fixed point for odd L is k=0, whose energy is 6. In any fixed open interval I=(a,b) with -6<a<b<6, every momentum in the interval therefore occurs in an orbit of size two. If M_L counts eigenvalues in I with multiplicity and D_L counts distinct energies there, D_L<=M_L/2. The sorted list of M_L eigenvalues has at least M_L-D_L>=M_L/2 zero adjacent spacings. Thus at least one half of its adjacent-spacing empirical mass remains at zero as M_L tends to infinity. A strictly monotone unfolding preserves zero spacings. This cannot converge to the GOE bulk spacing law, which has no atom at zero.

To see M_L tends to infinity, the inverse image h^(-1)(I) is a nonempty open set. Its boundary has Haar measure zero by the absolute-continuity argument, so the regular-grid Riemann sums give M_L/L^3 -> Haar(h^(-1)(I))>0.

This is an obstruction to the proposed implication 'infinite-volume ac implies GOE local statistics', and to a formulation allowing lambda=0 in a positive-disorder GOE claim. It does not refute the original target at fixed positive disorder, and it specifies periodic boundary conditions rather than silently changing them.

## Remaining Anderson gap

Nothing here establishes the p>1 bound for the iid Anderson operator on Z^3 at any positive disorder, or supplies nonzero spectral mass in a candidate interval. Uniformity down to eta=0, the infinite-volume passage, the exact disorder-law quantifiers, and nonzero mass remain to be audited against the recovered primary target and w486's proposed route.

## Adversarial check of w486's Born route S1.487.6

After saving S1.487.1-.5, read w486/STATEMENT_FOR_ADVERSARY.md and w486/ATTEMPT.md. Scope: the author's L1-L3, not any referee's review. Verdict: KEEP the stated operator-norm obstruction, subject to making the full probability-one event explicit. No parent-solution claim is supported by it.

The rare-cube step uses unconditional independence only on disjoint sets of iid sites. For each fixed L the coherent-cube probability is positive, however small; infinitely many disjoint trials produce infinitely many successes. Countably many L suffice. The support endpoint m with |m|=M exists because the essential support is compact. Intersect the rare-cube event with {all x: |V_x|<=M}; the latter has probability one by countability of Z^d. This explicit intersection prevents the asserted pathwise upper bound from depending on an unstated event.

For a normalized cutoff plane wave u_L in a coherent cube, the boundary defect tends to zero and ||(V-m)u_L||<=1/L. With a=i/eta, the exact identity R0 u_L-a u_L=-a R0(H0-E)u_L shows K u_L-(lambda m a)u_L ->0 for fixed E,lambda,eta. The approximate eigenvalue b=lambda m a has modulus c=lambda M/eta. Therefore r(K)>=c, while r(K)<=||K||<=c. Polynomial factorization gives (K^n-b^n)u_L ->0 for each fixed n. Applying R0 and using R0 u_L->a u_L supplies ||R0 K^n||>=|a|c^n. The elementary upper bound gives equality. Thus the Born-series terms fail to vanish at c>=1, including the endpoint c=1; at c<1 the Neumann theorem gives convergence. This validates necessity rather than merely failure of a sufficient bound.

Limits were checked in order: first L->infinity for each fixed eta>0 and integer n; then exact norm identities hold for all fixed eta and n. No simultaneous L/eta approximation or conditional independence of Green functions is used. The same rare-cube event supports all continuum parameters because the deterministic cutoff construction can be carried out on that event for each parameter. The statement applies only to E in the free band; no exterior-energy assertion is needed.

The result controls an unrenormalized operator-norm expansion. It does not control individual matrix-element cancellations, bath-width negative moments, quenched spectral type, or GOE local statistics. No counterexample to w486's stated lemma was found. Native author and auditor identities are w486 and w487; response-side served-model identities are UNKNOWN, so this audit cannot satisfy an identity-gated promotion by itself.

2026-10-10 referee FIX applied to S1.487.5: require a nondegenerate open energy interval I=(a,b), -6<a<b<6. A singleton is excluded; its grid count need not diverge. The existing numerical cases use I=(-1,1) and already satisfy this premise.
