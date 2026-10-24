# D0024 — exact scope and counterexamples

Date: 2026-10-11. Source downloaded as source.pdf; searchable transcription source.txt.

## Source scope

Seppäläinen, arXiv:math/9906194v1, PDF p.9, Problem 3 asks for weak convergence from a spatially ergodic initial law at density rho, with the environment fixed, and for convergence to the critical equilibrium above the critical density. Standing assumptions on pp.3–4: any dimension d, finite-range translation-invariant probability kernel p, bounded nondecreasing r with 0=r(0)<r(1), and a spatially ergodic environment law Q supported in [c,1], c>0 its marginal essential infimum. A nonzero drift is described as typical, not always necessary. The irreducibility condition (A.1) appears on p.6 as a hypothesis of Theorem 1, not as a standing assumption of Problem 3.

The examples below have nonzero drift and genuine site disorder. They refute the literal statement without a connectivity hypothesis. They do NOT settle a version that imports (A.1) into Problem 3.

## Counterexample 1: stationary, spatially ergodic, nonproduct initial law

Let d=1, p(2)=1 and r(k)=1 for k>=1, r(0)=0. Let a=1/2, b=1. The environment law Q gives probability 1/2 to each of the two alternating sequences (a,b,a,b,...) and (b,a,b,a,...). Translation by one exchanges these two atoms, so Q is translation invariant and ergodic. Its marginal essential infimum is c=a. Fix either environment realization alpha. Thus each parity class has a constant rate, but the rates of the two classes differ.

Write G_q(k)=(1-q)q^k, k>=0, for 0<q<1. Define pi_0 to be the product law with G_u on even sites and G_v on odd sites, and pi_1 with the parameters swapped. Take u=1/3, v=2/3 and mu=(pi_0+pi_1)/2. The initial law does not depend on alpha.

### Spatial ergodicity and density

Translation by one exchanges pi_0 and pi_1, and translation by two preserves each. Under translation by two, the pairs (eta(2n),eta(2n+1)), n in Z, are independent and identically distributed under either pi_i. This pair shift is ergodic: for a shift-invariant event A, approximate A in probability by a cylinder event B, shift B to disjoint coordinates, and use independence. If the approximation error is epsilon, invariance of A and the two approximations give |P(A)-P(A)^2|<=4 epsilon. Let epsilon tend to zero; P(A) is 0 or 1. This argument applies under each pi_i to any event invariant under translation by two.

If A is invariant under translation by one, it is invariant under translation by two. Its probabilities under pi_0 and pi_1 are therefore each 0 or 1. Since translation by one exchanges these laws and preserves A, the two probabilities agree. Consequently mu(A) is 0 or 1. Hence mu is spatially ergodic for the full translation group, despite not being mixing.

The strong law applied to the iid pairs, in each direction on Z and under each pi_i, gives almost surely the density

rho = (u/(1-u)+v/(1-v))/2 = (1/2+2)/2 = 5/4.

### Stationarity: full justification

The dynamics splits into independent even and odd copies of a nearest-neighbor totally asymmetric constant-rate zero-range process after relabelling 2n+s by n. Each copy has rate a or b. For any constant rate lambda>0 and any q in (0,1), the iid G_q law is stationary. Here is a direct finite-to-infinite proof.

On a finite cyclic chain of m sites, define w(eta)=prod_j (1-q)q^{eta_j}. An allowed move preserves the sum of the coordinates, hence preserves w. Outgoing transitions from eta are in one-to-one correspondence with occupied departure sites. Incoming transitions to eta from a move j to j+1 are possible exactly when eta_{j+1}>0. Their rates are lambda, and the incoming state has the same w. Both total weighted rates thus equal lambda w(eta) times the number of occupied sites. Global balance proves invariance of this probability law on the cycle. The total transition rate is at most lambda m, so global balance does give stationarity of this bounded-rate countable-state chain.

Couple a large cyclic chain and the infinite chain using the same site Poisson clocks in their common region and initial occupations sampled from the same iid law. On a sufficiently short interval [0,t_0], the Harris dependency components of any fixed finite set are almost surely finite, by the percolation construction in source Lemma 5.1. Once the cycle is larger than that component, the occupations in the finite set agree at time t. Bounded convergence transfers the finite-cycle stationary cylinder expectations to the infinite system for t<=t_0. Repeating intervals using the Markov property proves invariance for every t>=0. The argument applies independently on both parities. Thus pi_0, pi_1 and their mixture mu are invariant for the fixed alpha.

### The invariant law is not any nu_phi^alpha

All nu_phi^alpha in the source are product laws. Let I_x=1{eta(x)=0}. For sites 0 and 2, which have the same parity,

E_mu I_0 = E_mu I_2 = ((1-u)+(1-v))/2,
E_mu I_0 I_2 = ((1-u)^2+(1-v)^2)/2,
Cov_mu(I_0,I_2) = (u-v)^2/4 = 1/36 > 0.

Thus mu is not a product law, and cannot equal any nu_phi^alpha (including nu_0). The law at every time is exactly mu. In the product topology on N^Z, these indicators are bounded continuous cylinder functions. A constant sequence of laws cannot converge weakly to a different probability law; alternatively the displayed first and second cylinder moments contradict any product limit. This answers the first question negatively under the literal standing hypotheses. Q(alpha_0=c)>0, so here rho*=infinity; this example alone does not address finite critical density.

## Counterexample 2: finite critical density, supercritical start

Again d=1, p(2)=1 and r(k)=1{k>=1}. Let Q be iid with marginal density

f(a)=32(a-1/2) on (1/2,3/4), zero elsewhere.

Its integral is 16(1/4)^2=1, its essential infimum is c=1/2, and iid Q is spatially ergodic. The source critical-density formula gives

rho* = c E[(alpha_0-c)^(-1)]
     = (1/2) integral_{1/2}^{3/4} 32 da = 4.

For Q-almost every alpha, all coordinates lie strictly between c and 3/4. Fix any such alpha. The critical product law exists, with G_{c/alpha_x} marginals. It is indeed the critical equilibrium: its stationarity follows by letting phi increase to c in the source Proposition 1. The marginals converge and hence their products converge weakly. For a bounded cylinder function the bounded-rate Harris construction makes S_t f continuous and bounded (dependency outside larger finite sets has probability tending to zero, uniformly in the initial state), so invariance passes to the limit. Its annealed mean occupation is 4, agreeing with the critical-density formula.

Let the initial law put probability 1/2 on each deterministic configuration

eta(2n)=0, eta(2n+1)=10 for every n,
eta(2n)=10, eta(2n+1)=0 for every n.

The full translation group acts transitively on these two configurations, so this probability law is spatially ergodic. Both have density rho=5>4=rho*. It is independent of alpha.

On the event that the parity of 0 is initially empty, that entire parity remains empty forever: every allowed arrow joins two sites of the same parity, and r(0)=0. This can be checked directly on each finite Harris dependency component and then propagated through the construction intervals. Therefore

P(eta(0,t)=0) >= 1/2 for every t>=0.

But under the critical equilibrium

nu_c^alpha(eta(0)=0)=1-c/alpha_0 < 1- (1/2)/(3/4)=1/3 <1/2.

The indicator of {eta(0)=0} is bounded continuous. Weak convergence to nu_c^alpha would force its expectations to converge to a number below 1/3, contradicting the lower bound 1/2. This refutes precisely the supercritical convergence assertion under the literal assumptions, for Q-almost every fixed environment.

## Hostile-referee issues

1. Missing connectivity is decisive, not cosmetic. p(2)=1 fails (A.1): no sequence of +/-2 steps can join opposite parities. If (A.1) is intended implicitly, neither counterexample applies. We do not claim a new resolution of the irreducible disordered-ZRP convergence problem.
2. Ergodic is weaker than mixing. Both initial laws are ergodic under translation by one; their two-phase construction is legitimate. The stationary mixture is not a mixture of two translation-invariant laws: neither component is translation invariant under translation by one.
3. Q is genuinely disordered and spatially ergodic in both examples. The first is periodic but ergodic, not iid; iid was only an assumption of source Theorem 2. The second is iid.
4. Quenched quantifiers: the first works for each of Q's two environments; the second for every environment with all coordinates in (1/2,3/4), a full-Q-probability event.
5. Nonzero drift, bounded monotone rate, positive lower bound, finite-range jumps and finite initial density all hold.
6. No inference from preservation of mean to local convergence is used. The contradiction uses bounded continuous observables.
7. The first example establishes failure of convergence to *every* member of the specified product family. The second establishes failure of convergence to the critical member only; no assertion about its actual long-time law is needed.

## Strengthening: actual limit in the iid counterexample

This paragraph uses the published nearest-neighbor convergence theorem (Bahadoran–Mountford–Ravishankar–Saada, Theorem 2.5, arXiv:1804.06148, PDF p.18), whose precise statement and restrictions are recorded in LITERATURE.md. It is a reduction to that theorem, not a claim that the theorem itself states a counterexample to Problem 3.

For each s in {0,1}, relabel site 2n+s by n, and set alpha^(s)(n)=alpha(2n+s). Under iid Q, each of these two environments is an iid realization of the same marginal distribution, almost surely satisfying the averaging and slow-defect hypotheses of the published theorem. Their infimum is c, attained nowhere. Take the intersection of these two full-probability sets of environments. In the phase in which parity s is active, its initial configuration is identically 10, so its left asymptotic density in the relabelled lattice is 10. The process on that parity is exactly a nearest-neighbor totally asymmetric zero-range process with g(k)=1{k>=1}. By Theorem 2.5 it converges weakly to the product critical law on that parity, since 10>rho*=4. The other parity stays identically zero.

Embedding a configuration on one parity into the full lattice by filling the other parity with zero is continuous in the product topologies. Composing an arbitrary bounded continuous full-lattice observable with this embedding and using the theorem proves full-lattice weak convergence in each initial phase. Taking their half-half mixture gives the actual limiting law

L_alpha = (1/2)[(critical product on even sites) x (zero on odd sites)]
        + (1/2)[(zero on even sites) x (critical product on odd sites)].

Let h_x=1-c/alpha_x, the critical probability of zero at site x. For sites 0 and 2,

E_L I_0=(1+h_0)/2, E_L I_2=(1+h_2)/2,
E_L I_0 I_2=(1+h_0 h_2)/2,
Cov_L(I_0,I_2)=(1-h_0)(1-h_2)/4=c^2/(4 alpha_0 alpha_2)>0.

Hence the actual limit is not any product equilibrium nu_phi^alpha, including nu_0. This single iid environment example therefore refutes both clauses, though the simpler zero-probability contradiction above already refutes the second without using any later convergence theorem.

The joint initial/environment law in this iid example is also spatially ergodic. Conditional on either initial phase, translation by two is an iid-pair Bernoulli shift of the environment, and hence ergodic by the cylinder-independence proof already given. Translation by one swaps the phases. Any event invariant under translation by one must have equal zero-or-one probabilities in the two phases, and is therefore trivial. Thus even requiring joint ergodicity does not repair the disconnected-kernel problem.

For completeness, the critical equilibrium has quenched spatial density 4 for Q-almost every environment: under its annealed law the pairs (alpha_x,eta_x) are iid, with E eta_x=4. The strong law gives density 4 almost surely under the joint law; Fubini then gives the same almost-sure density statement under nu_c^alpha for Q-almost every alpha. No unjustified quenched law of large numbers for nonidentical variables is being used.

## Verified positive specialization and full reduction

Restrict to d=1, nearest-neighbor jumps with nonzero drift, and almost every ergodic environment for which the published theorem's environment assumptions hold. Assume a finite-density spatially ergodic initial law mu, density rho>0. By the ergodic theorem applied to the shift (or its inverse),

lim_n n^(-1) sum_{x=-n}^0 eta_0(x)=rho

for mu-almost every configuration eta_0. The denominator n instead of n+1 does not affect the limit. For each such eta_0, the printed Theorem 2.5 yields conditional weak convergence to the same equilibrium indexed by min(rho,rho*). For any bounded continuous F on the configuration space, E^{alpha,eta_0}F(eta_t) converges to the equilibrium integral and is bounded by ||F||_infinity. Dominated convergence integrates this over mu, giving convergence for every bounded continuous F, exactly the definition of weak convergence. If rho=0, nonnegativity and E_mu eta_0(x)=0 imply eta_0(x)=0 almost surely for each x; their countable intersection is the empty configuration, which is invariant. Normalizing g=r/r(infinity) changes the time parameter to r(infinity)t and the fugacity to phi/r(infinity), so no restriction to r(infinity)=1 remains. Leftward nonzero drift is handled by reflecting the lattice. This proves the positive nearest-neighbor specialization by reduction to the verified published theorem.

When rho* is finite, the source formula forces Q(alpha_0=c)=0, and the constant observation site is typical as required in the proof of Theorem 2.5. For subcritical rho only the averaging assumption is needed in the local equilibrium step. No arbitrary exceptional deterministic environment is asserted to be covered.

## Exact and formal checks

checks.py uses Python Fraction arithmetic and checks finite cyclic global balance exhaustively for cycle sizes 2 through 6 and total occupations 0 through 8 (4,995 configurations). All assertions passed; output saved in checks.json. This supports the finite balance calculation but does not replace the infinite-volume proof.

ParityChecks.lean formalizes only the finite covariance identity, the chosen numerical covariance and density, and the empty-probability obstruction after multiplication by a positive site rate. The infinite-volume ergodicity, stationarity and convergence arguments remain handwritten proofs. Lean's queued check outcome is recorded separately; nothing is called formally checked before a successful return.

## Remaining scope

The literal question is answered negatively. The strengthened question with arbitrary kernels satisfying (A.1) is not answered by these counterexamples. The one-dimensional nearest-neighbor specialization is answered positively by reduction to the verified published theorem above. The exact computational checks passed; the submitted Lean check remains queued as recorded in LEAN_CHECK.md. No infinite-volume claim is described as formally checked, and no exhaustive literature-status assertion is made.
