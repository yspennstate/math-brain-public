# P0003 independent route (pre-proof checkpoint)

Saved before reading w399's proposed proof. Candidate method: compare critical finite-domain SAW partition functions under removal of an obstacle; derive the exact finite-lattice conditional law and partition ratio, then isolate the hypotheses needed to pass this ratio to a conformal restriction law. This is a route to a conditional reduction or a counterexample to an unjustified limit passage, not a proof of the SAW scaling conjecture.

## Independent derivation saved before paired-proof access

Let G be a finite graph, a and b distinct vertices, x>0, and Omega(G;a,b) its vertex-self-avoiding a-to-b paths. Assume Z_G=sum_gamma x^{length(gamma)}>0. For a deleted vertex set A disjoint from {a,b}, let E_A be the paths whose vertices avoid A and suppose Z_{G-A}>0. Direct cancellation of the weights gives

P_G(E_A)=Z_{G-A}/Z_G, and P_G(. | E_A)=P_{G-A}.

Proof: sum the same positive weights over the surviving paths, then divide by the appropriate partition function. The Radon-Nikodym density is 1_{E_A} Z_G/Z_{G-A}. This is exact for every positive fugacity, not a conformal-invariance theorem. Conditional on a feasible prefix eta=(a,...,v), its continuation has the same fugacity law in G with the prefix vertices except v deleted. Its normalization is the completion partition function; probabilities are not obtained by multiplying unconditional one-step bounds.

### Conditional-limit lemma (newly written proof; reviewer pending)

On a common metric space X let probability laws mu_n converge weakly to mu. Let E_n and E be Borel events with mu(boundary E)=0, mu_n(E_n symmetric-difference E)->0, and mu(E)>0. Then mu_n(. | E_n) converges weakly to mu(. | E).

Proof: for each bounded continuous f, the portmanteau extension for bounded functions with mu-null discontinuity set gives integral f 1_E dmu_n -> integral f 1_E dmu. The change to E_n costs at most ||f||_infinity mu_n(E_n symmetric-difference E). Taking f=1 gives denominators converging to mu(E)>0; division proves the assertion. This needs event compatibility and a positive limiting denominator. No independence is invoked.

### Explicit obstruction at an attached slit

Take D=(-2,2) x (-1,2), endpoints a=(-2,0), b=(2,0), and closed slit A={0} x [-1,0]. Let gamma_n^+ and gamma_n^- be the polygonal curves a -> (0,+1/n) -> b and a -> (0,-1/n) -> b, parametrized by the same two time intervals. Both are simple and converge uniformly to gamma=a -> (0,0) -> b. Every gamma_n^+ avoids A, every gamma_n^- meets A, and gamma meets the tip of A. For mu_n=(delta_gamma_n^+ + delta_gamma_n^-)/2, mu_n converges weakly to delta_gamma, mu_n(E_A)=1/2 for every n, but delta_gamma(E_A)=0. Thus weak convergence and even a positive convergent sequence of avoidance probabilities do not identify continuum avoidance or conditional restriction. This is a topology counterexample, not a counterexample to the critical SAW conjecture.

### Independent reduction and single hardest missing piece

For a subsequential SAW limit, exact lattice restriction passes to conformal restriction only after an admissible obstacle event can be passed to the limit, the domain laws are conformally compatible, and the limit has the simple-curve support required by the restriction classification. Lawler-Schramm-Werner's chordal restriction theorem then identifies a simple restriction curve as SLE(8/3). None of these continuum hypotheses follows from Z_{G-A}/Z_G alone. The hardest piece for this route is conformal compatibility of the limiting critical SAW domain laws, together with the existence/regularity needed to define them. A scalar partition ratio is a conditional reduction, not a proof of that piece.

NEXT: Read exact prior P0003 records, then audit the paired proof against this independently saved conditional-limit and normalization analysis.

## Exact-target correction after recovering the cited source

The local P0003 card is faithful to Grimmett's *Selected problems in probability theory*, Question 2.2, printed page 3 (arXiv:2205.07318): the actual question concerns a uniformly chosen n-step honeycomb SAW starting at the origin, suitably rescaled. It does not specify chordal boundary endpoints, a bounded domain, a precise rescaling, or an SLE variant. The critical-fugacity boundary-to-boundary conjecture from Duminil-Copin--Smirnov is a related formulation. The independent restriction route above is a conditional reduction for that related ensemble, not an equivalent restatement or a solution of P0003. This correction was saved before opening the paired proof.

### Exact bridge between ensembles and its missing premise

For any finite collection of rooted SAWs with positive length-dependent weights x^L, conditioning the normalized fugacity law on L=n gives the uniform law on the n-step paths in that collection. This follows because every surviving path has exactly the same weight x^n. Specifying a terminal vertex adds another condition, and bounding the domain changes the collection; neither matches the free endpoint n-step target automatically.

Weak convergence of a fugacity mixture does not imply convergence at a prescribed length. Let L_n be uniform on {1/n,2/n,...,1}, take n even, and let X_n=0 except at L_n=1/2. At that one atom set X_n=1 (or, in a second sequence, X_n=-1). Both joint laws (X_n,L_n) converge to (0,U), U uniform on [0,1], with exactly identical length marginals. The selected atom has probability 1/n, yet its conditional feature is identically +1 or -1 respectively. The joint limit and marginal length scaling cannot distinguish these conditional laws.

A sufficient transfer premise is a conditional local limit, with relative errors: for a scale h_delta->0, a prescribed discrete length n_delta, and rho(l)>0, require E[f(Gamma_delta) 1_{L=n_delta}]=h_delta rho(l) Q_l(f)+o(h_delta) for every bounded continuous f and P(L=n_delta)=h_delta rho(l)+o(h_delta). Division then gives the desired fixed-length limit Q_l. A weak joint shape/length limit supplies neither this relative error nor the conditional local limit. For this exact target, this ensemble-transfer premise is a separate hardest gap even if the related chordal scaling conjecture were established.

NEXT: Audit the paired proof for a legitimate fixed-length/free-endpoint transfer, then for obstacle-event continuity if it uses restriction.

## Paired-proof audit: three-probe route (read after the independent checkpoints)

w399's LEMMA_THREE_PROBE.md supplies a conditional three-probe Loewner lemma, not a full SAW proof. Independently expanding its commuting-map equation gives partial_t h'(W)=h''(W)^2/(2h'(W))-(4/3)h'''(W). With u=h''/h', c=h'''/h' and dW=mu dt+dN, d<N>=v dt, Itô then gives

dM/M = alpha u dN + alpha [mu u +(v/2-4/3)c + (1+v(alpha-1))u^2/2]dt.

Thus the actual zero-drift argument is sound under the stated semimartingale, common fixed alpha>0, reflection, localization and invertible-jet hypotheses. Invertibility is only local at the displayed initial configuration; global coverage is separately assumed. Its stated quantitative bounds are valid bounds, not an unconditional SAW identification.

### A concrete obstruction to using unnormalized small drift

Positivity of a mesh-dependent exponent is insufficient: it must have a positive fixed limit, or the error must be controlled after division by alpha. Take the deterministic Loewner driver W=0 (mu=v=0), and alpha_n=1/n>0. Before the hull reaches any of the three probes, localize so h', its reciprocal and its jets are bounded. Then M_{i,n}=(h_i'(0))^{alpha_n} tends uniformly to the constant 1, and its raw relative drift is O(alpha_n). The driver still has quadratic-variation rate zero, not 8/3.

At the initial three-probe matrix, the drift after division by alpha_n is exactly (9/8,9/8,33/32), since -4c_i/3+u_i^2/2 has these values. At n=128 the largest raw relative drift is 9/1024 < 1/100, while |v-8/3|=8/3. Hence a small raw drift of M_i/M_i does not meet the lemma's small e_i hypothesis. This does not refute w399's fixed-positive-alpha lemma; it isolates a quantitative requirement in its unproved SAW-to-martingale input.

### Exact-target scope verdict

w399's STATEMENT_FOR_ADVERSARY.md expressly selects the related critical chordal ensemble and distinguishes the fixed-n law. Preserve that specialization as a conditional result. To count it as P0003's cited fixed-length/free-endpoint problem would require the missing ensemble and endpoint transfer, with relative local-limit error at the selected length. No such transfer is provided in the read packet.

NEXT: Verify the explicit finite diagnostics, send the exponent-normalization and ensemble-transfer findings to w399/w401, and submit concept-only brain drafts for review.
