C0044: a density bridge for directional zero-one laws

2026-10-10. Author w585; referee w587; adversary w586. All new proofs below await independent mathematical review. No parent-problem solution or novelty claim is made.

Exact target and source

For d>=3, take a static, site-iid nearest-neighbor environment on Z^d with strictly positive transition probabilities summing to one at every site. For each fixed nonzero l in R^d, under the annealed law from 0, prove P_0(A_l) is zero or one, where A_l={X_n dot l -> +infinity}. The original intake cites Drewitz-Ramirez, Selected topics in random walks in random environment, Open question 3.2, p.42; the intake's (E) must not be silently strengthened to uniform ellipticity. STATEMENT_FOR_ADVERSARY.md gives the model precisely.

Current openness is UNKNOWN. A September 23, 2026 preprint linked by openai/math/lean/docs/220.md claims a strict-elliptic resolution. The comparator DirectionalWalk.lean, lines 78-81 in one-based numbering, states the desired theorem with the correct static product model but closes it with `by sorry`. That comparator is a statement skeleton, not a formal-check receipt. Its placeholder does not prove the separate preprint false. No Lean execution or trusted-axiom receipt is claimed here.

Prior-attempt digest

The 2026-09-07 C0044-A001 attempt tried to transfer the planar two-walk intersection argument to d>=3. C0044-A002 corrects its first sentence: A_l and A_-l are disjoint by definition; the planar theorem's substantive conclusion is P_0(A_l) in {0,1}. Kalikow's union law alone does not determine P_0(A_l). A001 correctly identified the absence of a planar intersection substitute and the danger of treating q_l as local. The scoped intake search found no C0044 record in named H/I directories; other-candidate comparisons are excluded from this digest. The Team O board assigns C0043 to w338 and C0040 to w341; this packet neither attempts their computations nor asserts the invariant-measure converse.

Lane and notation

The lemmas require only translation stationarity and ergodicity of the environment law P, together with strict ellipticity; iid is sufficient. Write tau_x omega(y,e)=omega(x+y,e), q(omega)=P_0^omega(A_l), q_x(omega)=q(tau_x omega), eta_n=tau_{X_n} omega, mu_n=Law_{P_0}(eta_n). The direction is fixed throughout. Let F_n contain the full sampled environment and X_0,...,X_n. The full environment in this filtration is deliberate; finite-region measurability is unnecessary.

Lemma 1: bounded harmonic posterior

For P-almost every omega and every x,
q_x=sum_e omega(x,e) q_{x+e}.
The Markov property gives this because deleting finitely many initial steps preserves A_l. Also q(eta_n)=P_0(A_l|F_n), so q(eta_n) is a [0,1]-valued martingale and converges almost surely and in L1 to 1_{A_l}. Indeed A_l is measurable with respect to F_infinity, and Levy's upward theorem identifies the limit of these conditional expectations. This is a posterior identity, not an independent-trial argument.

Lemma 2: positivity propagation, not zero-one

If p=P_0(A_l)>0, then q>0 P-almost surely. For each environment in the countable simultaneous full-measure set where harmonicity and strict ellipticity hold, q_x=0 forces q_{x+e}=0 for every e, hence q_y=0 for every y. Thus the event {q=0} is translation invariant. Ergodicity makes its P-probability zero or one, and E_P q=p>0 excludes one. Applying the same argument to 1-q shows that p<1 implies q<1 P-almost surely. Consequently 0<p<1 implies 0<q<1 P-almost surely. Neither conclusion turns strict positivity into probability one.

Lemma 3: exact finite-time density

For every integer n>=0,
f_n(omega)=d mu_n/dP(omega)=sum_{x:|x|_1<=n} P_{-x}^omega(X_n=0).
In particular f_n>=0 and E_P f_n=1. Terms that cannot be reached in exactly n steps are zero. To verify the formula, for each bounded measurable g write
E_{P_0} g(eta_n)=sum_x integral P_0^omega(X_n=x) g(tau_x omega) dP(omega).
Change variables omega'=tau_x omega using translation invariance. Translation covariance of quenched paths changes P_0^omega(X_n=x) to P_{-x}^{omega'}(X_n=0), giving integral f_n g dP. The sum is finite; no interchange of infinite sums is required.

Lemma 4: mixed transience forces density concentration

Suppose 0<p<1. For 0<epsilon<1/2 put
B_epsilon={q<=epsilon or q>=1-epsilon},
b_epsilon=P(B_epsilon), a_n=mu_n(B_epsilon).
Then b_epsilon -> 0 as epsilon decreases to zero, by Lemma 2 and continuity from above; a_n -> 1 as n -> infinity, by Lemma 1 and dominated convergence. If b_epsilon=0 for any epsilon, absolute continuity gives a_n=0 for every n, already contradicting a_n -> 1. Otherwise Holder gives, for every r>1,
E_P[f_n^r] >= a_n^r / b_epsilon^(r-1).
For every prescribed M choose epsilon with b_epsilon^(1-r)>2M, and then n sufficiently large that a_n^r>1/2. It follows that E_P[f_n^r] -> +infinity for every r>1, with the convention that an infinite moment satisfies the bound. This is a full-sequence divergence, not merely an unbounded subsequence.

More generally the family {f_n:n>=0} has no uniformly integrable subsequence with times tending to infinity. If {f_{n_j}} were uniformly integrable, uniform absolute continuity of its integrals would give mu_{n_j}(B_epsilon)<1/2 whenever P(B_epsilon) is sufficiently small. The limit a_{n_j}->1 contradicts this.

Conditional theorem: subsequential uniform integrability is a sufficient bridge

Under stationary ergodic strict-elliptic static nearest-neighbor RWRE, if some deterministic sequence n_j->infinity has uniformly integrable densities {f_{n_j}}, then P_0(A_l) in {0,1} for every fixed direction l. A sufficient condition is sup_j E_P[f_{n_j}^r]<infinity for some r>1. Proof: if the probability were strictly between zero and one, Lemma 4 would contradict the assumed uniform integrability. The density hypothesis is direction independent; hence the conclusion holds separately for every deterministic direction. No simultaneous uncountable intersection of path events is asserted.

One can replace f_n by Cesaro averages F_N=(1/N)sum_{n=0}^{N-1}f_n. Lemma 1 gives (1/N)sum_n mu_n(B_epsilon)->1, so the identical argument proves the criterion if {F_{N_j}} is uniformly integrable along N_j->infinity. This version does not assert existence of an invariant probability measure; it uses only the displayed integrals.

Attempt to discharge the bridge and the single hardest gap

The exact density formula gives only the pointwise bound f_n<=#{x:|x|_1<=n}=O(n^d), since each incoming transition probability is at most one. This grows with n and does not supply any uniform integrability estimate. Independence of site vectors cannot be applied to the incoming terms: paths share sites, and mu_n samples the environment through a walk whose decisions depend on that environment. Spatial ergodicity controls deterministic translates; it does not give a stationary distribution for eta_n under the original P.

HARDEST GAP: establish subsequential uniform integrability of the Cesaro densities F_N, or an equally strong no-concentration estimate on B_epsilon, from the actual C0044 hypotheses. This packet does not establish it. It may be stronger than necessary, especially without a uniform ellipticity bound or a moment assumption; no universal existence claim is made. A finite-time polynomial upper bound, a simulation, or normalization E f_n=1 cannot fill this gap.

Refuted reasoning route

Normalization and finite-time absolute continuity alone do not imply uniform integrability: on ([0,1],Lebesgue), g_m=m*1_[0,1/m] has integral one, is absolutely continuous at every m, but is not uniformly integrable. If m>K, integral g_m 1_{g_m>K}=1. Also E g_m^r=m^(r-1). This is a counterexample to that inference, not a counterexample to C0044 or an RWRE realization.

Review requirements

w587 should check the full-environment filtration, the translation sign in Lemma 3, the positivity argument for both q and 1-q, the full-sequence quantifiers in Lemma 4, and the Cesaro variant. The invariant-measure route and the general open-problem claim remain outside what was proved. New referee results require w590's separate review. Numerical checks are algebraic regression evidence only; none certify the infinite-time theorem.
