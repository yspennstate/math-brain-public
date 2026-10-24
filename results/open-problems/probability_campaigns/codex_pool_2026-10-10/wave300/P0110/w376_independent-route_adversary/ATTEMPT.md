# P0110 independent route checkpoint

2026-10-10 precommit checkpoint. Worker w376. The paired proof had not been opened when the independent route below was saved. Exact source recovery was pending at that checkpoint; later source checks and scoped audits are recorded in SOURCE_STATUS.json and PEER_AUDIT.md. Current openness remains UNKNOWN. Ranking row 551 labels P0110 tier 5, attempted_un; this is historical metadata, not a proof or an openness certificate.

## Dependency obstruction

Let B be Bernoulli(1/2), and A1=A2={B=1}. Conditional on either of two trivial sigma-fields, each event has probability 1/2. Their intersection has probability 1/2, not at most 1/4. Thus iid input edges do not by themselves make path-selected events independent, and unrelated row-wise conditional estimates cannot be multiplied.

The sufficient sequential replacement is: an increasing filtration (Fi), events Ai measurable in Fi, and P(Ai|F_(i-1))<=pi almost surely. Iterating conditional expectation then yields P(intersection Ai)<=product pi. The hypothesis must be derived for the actual optimized path events.

This elementary counterexample is a first saved result, not a claimed advance on KPZ.

## Independent route, fixed before opening the paired proof

The independent method is an oscillating-scale obstruction to exponent-collapse arguments. It differs from the recorded curvature balance, block-overlap/chaos recursion, and first-chaos covariance floor. The primary reference checked so far is Chatterjee, Annals of Mathematics 177 (2013), Theorem 1.1, printed pp. 665-666, https://annals.math.princeton.edu/wp-content/uploads/annals-v177-n2-p07-p.pdf. Its conclusion chi=2xi-1 requires chi_a=chi_b and xi_a=xi_b in addition to its law hypotheses.

For integer n>=2 let a_n=1/4 when n is even and a_n=1/3 when n is odd. Let Z be a symmetric random sign and set X_n=n^(a_n) Z and D_n=n^((1+a_n)/2). These are an abstract sequence of observables, NOT passage times/geodesics of an iid FPP law. Sharing Z is irrelevant to all marginal exponent calculations; independent signs at different n work equally well.

Define upper thresholds chi_a,xi_a using uniform exponential moments of |X_n|/n^q and D_n/n^r for every q>chi_a,r>xi_a. Define lower thresholds chi_b,xi_b using positive tail-uniform infima of Var(X_n)/n^(2q) and E D_n/n^r for every q<chi_b,r<xi_b, allowing a finite n cutoff depending on the exponents. These are the one-index analogues of A1-A4, not a claimed realization of all lattice-direction quantifiers.

Then exactly chi_a=1/3, chi_b=1/4, xi_a=2/3, xi_b=5/8. For any exponent above the corresponding maximum, each normalized deterministic magnitude is bounded, so the upper exponential bound holds. For any exponent below that maximum the odd subsequence diverges and defeats every positive exponential-moment parameter. For lower bounds, exponents at or below the minimum yield normalized ratios at least 1; exponents above the minimum give ratios tending to zero on the even subsequence, after every finite cutoff.

At EVERY scale sqrt(Var(X_n))=D_n^2/n. Also BOTH endpoint identities chi_a=2xi_a-1 and chi_b=2xi_b-1 hold. Nonetheless the two chi thresholds differ by 1/12 and the two xi thresholds differ by 1/24. Thus even a perfect scale-by-scale KPZ balance and endpoint KPZ identities do not imply existence of the common strong exponents. A proof must supply a mechanism excluding oscillations, or work with a different fully specified exponent notion and prove its own relation.

The single hardest missing piece for the conditional-theorem route to P0110 is verification of strong-exponent existence for one admissible iid nearest-neighbor lattice law. This example refutes an abstract inference only; it does not refute the target, prove nonexistence for FPP, or establish an FPP exponent. Independent referee target: w377.

## Exact source and boundary audit

The recovered intake asks for a nondegenerate iid undirected FPP law with well-defined fluctuation/wandering exponents satisfying chi=2xi-1. The primary source is Auffinger-Damron-Hanson, https://arxiv.org/pdf/1511.03262, Section 4.3, equation (4.19), Question 22 (PDF pp.88-89). The problem also includes choosing and proving existence of appropriate exponents; the strong-exponent route above is sufficient, not the only possible interpretation of a solution. Current openness remains UNKNOWN.

Chatterjee's lower bounds A3-A4 allow a finite radius cutoff. The literal lower-bound definition (2.2) in Auffinger-Damron, https://arxiv.org/pdf/1109.0523, takes an infimum over all nonzero lattice endpoints. These are different quantifiers. For iid Uniform[1,2] weights, from 0 to e1 the direct edge costs at most 2, whereas every other self-avoiding path has at least three edges and costs at least 3. Therefore the unique geodesic is the direct edge in every environment and D(0,e1)=0. The all-endpoint lower infimum for E D is consequently 0 for every exponent. This does not disprove their conditional theorem or any asymptotic FPP relation; it proves that this admissible continuous law fails that literal all-endpoint lower premise for a finite-scale reason. A referee must distinguish the definitions and justify any change to the invoked theorem.

STUCK: two remembered survey arXiv identifiers gave title mismatches; neither supports a claim. A title search recovered the correct 1511.03262 and its exact Question 22.

## Independent consequence of the paired proof: coupling cannot erase a raw drift gap

After the independent exponent obstruction was fixed, the original w375 proof PROVED_LEMMAS.md became available. Lemmas L1-L4 are audited in PEER_AUDIT.md. In particular its L2 proves a deterministic c>0 with limsup T(0,n e1)/n<=mu-c almost surely, whereas the directed axial cost divided by n tends to mu almost surely.

The raw comparison is stronger than a same-environment obstruction. Let U_n and V_n have respectively those unrestricted and directed marginal laws, with ANY joint coupling at each n (even a different coupling for every n). Fix epsilon in (0,c/2). Marginal convergence implies P(U_n/n>mu-c+epsilon)->0 and P(V_n/n<mu-epsilon)->0. A union bound, with no independence, gives

P((V_n-U_n)/n >= c-2epsilon) >= 1-P(U_n/n>mu-c+epsilon)-P(V_n/n<mu-epsilon) -> 1.

Thus no such coupling gives V_n-U_n=o_P(n) without a change of deterministic centering or model. This does not exclude matching centered fluctuation exponents or universality classes. w377 independently checked this consequence and returned a scoped KEEP; the exact verdict is bound in REFEREE_RECONCILIATION_RECEIPT.json. The different-model promotion gate remains pending and novelty is unverified. The consequence refines the caveat after w375 L2, whose mathematical block argument is sound.

For the explicit Uniform[1,2] witness above, delta >= (1/2)*4^(-14), so the L2 drift saving c=delta/7 is at least c0=1/3758096384. Therefore the arbitrary-coupling conclusion applies with this concrete c0; for example P((V_n-U_n)/n>=c0/2)->1. The small numerical size reflects the conservative finite-event certificate, not a measured physical time constant.
