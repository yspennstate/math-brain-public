# Further attempt at P0287 — 2026-10-12

## Gap inherited from the first attempt

The earlier results classify product laws and zero-incoming-current laws, reduce zero-outgoing-current laws to ordinary half-line TASEP, and construct explicit killed-flow laws with occupied downstream tail. They do not establish a positive-outgoing-current full-line invariant law or exhaust correlated laws. The remaining-gap paragraph of ATTEMPT.md was read before this attempt.

## Two approaches not previously tried

**A. Attractive coupling, discrepancy conservation and time averaging.** Start ordinary TASEP xi from its invariant iid Bernoulli(rho) law; start the killing process eta from the same configuration and use the same bond clocks, with extra removals only in eta. Order eta<=xi is preserved. The finite number of discrepancies at any finite time should give a pathwise incoming-current comparison by summing their balance on the left half-line. A Cesaro limit of the coupled laws is stationary and is stochastically dominated by Bernoulli(rho). The promising additional observation is that domination controls the adjacent-pair probability at the defect, not merely its occupancy. Combining this with current conservation could produce a strictly positive outgoing-current lower bound for every kappa, at sufficiently small rho. This is the selected approach.

**B. A genuinely two-sided defect matrix ansatz.** Use two bulk alphabets satisfying D_L E_L=c_L(D_L+E_L) and D_R E_R=c_R(D_R+E_R), with a defect tensor at site 0 absorbing the bulk telescoping residue and the killing term. Solve finite-dimensional representations or truncated noncommutative recurrences, first on short intervals, checking positivity and consistency. The required defect relation would have to encode c_L-c_R=kappa p_0. The earlier half-line scalar word functional has only one boundary and does not address this two-current junction. This route could provide explicit cylinder formulas but currently has no positive representation or consistent defect relation, making A more promising.

## Brain query

Read-only math_recall.py query: "TASEP killing defect positive transmitted current invariant coupling Liggett". The useful returned cards were only the earlier current/product obstruction, not a theorem about transmitted current. The Liggett cards concerned the subadditive ergodic theorem and smoothing transforms, and were not used as premises.

## Working observation, not yet claimed proved

Under the common-clock ordered coupling, discrepancies xi_i-eta_i are binary and are created only by killing at 0. If D_left(T)=sum_(i<=-1)(xi_i(T)-eta_i(T)) is finite, conservation predicts N_(-1)^eta(T)-N_(-1)^xi(T)=D_left(T)>=0, where N_i counts jumps across bond i. In a stationary time-average limit, this would imply J_-^eta>=rho(1-rho). Domination gives E eta_0 eta_1<=rho^2. Then p_0=J_++E eta_0 eta_1<=J_++rho^2, so J_-<= (1+kappa)J_++kappa rho^2. Therefore a candidate rigorous bound is

J_+ >= rho[1-(1+kappa)rho]/(1+kappa),

positive for 0<rho<1/(1+kappa). Every passage to an infinite sum, invariant limit and cylinder inequality still needs checking; no theorem is claimed at this stage.

## Stronger route found while checking

The laws S_t^kappa nu_rho are stochastically decreasing in t: the coupling gives S_s^kappa nu_rho<=nu_rho, and attractiveness then gives S_(t+s)^kappa nu_rho<=S_t^kappa nu_rho. This suggests an actual weak limit mu_(kappa,rho), invariant by the Feller property, rather than just a Cesaro subsequence. It would be the greatest invariant law dominated by nu_rho.

For every binary configuration and n>=1,

eta_0 = sum_(j=0)^(n-1) [prod_(i=0)^j eta_i](1-eta_(j+1)) + prod_(i=0)^n eta_i.

Each summand is <=eta_j(1-eta_(j+1)). Thus any stationary law dominated by nu_rho satisfies p_0<=n J_++rho^(n+1). Together with the incoming-current comparison this suggests

J_+ >= [rho(1-rho)-kappa rho^(n+1)]/(1+kappa n).

For every 0<rho<1 and finite kappa, some n makes this positive. The finite binary identity, coupling conservation and limit step are the critical checks now being pursued. This observation supersedes the small-density restriction in the first working bound, but is not yet entered as a proved claim.

## Verification checkpoint

`coupling_checks.py` passed 9 ordered two-site common-clock cases, 16,380 exhaustive occupied-run identities through length 13, 50,000 finite-window path events checking both cut balances and total discrepancy count, and 8 exact rational stationary finite open chains with killing. The finite chains use the matching Bernoulli boundary rates alpha=rho and beta=1-rho and check the positive current bound. A negative control using independent bond clocks destroys order. These are checks of local/conservation/algebra steps, not substitutes for the infinite-process argument.

A further gap-specific brain query, "exclusion process translation invariant stationary measures mixtures Bernoulli Liggett Spitzer", returned no usable classification theorem. To check the neighbouring classical result, fetched Basu–Sarkar–Sly, *Invariant Measures for TASEP with a Slow Bond*, arXiv:1704.07799, full PDF to slowbond.pdf and extracted text slowbond.txt. Its background cites Liggett's homogeneous full-line TASEP invariant classification. The slow-bond results themselves do not apply to killing. A verified homogeneous classification could identify the **upstream Bernoulli tail** of the newly constructed laws for rho<=1/2 by examining translated limits; this is being pursued separately from the elementary existence proof.

## Theorem A: canonical positive transmitted flow (proved)

For every kappa>0 and 0<rho<1, let nu_rho be the iid Bernoulli(rho) law on Z, and S_t^kappa the killing-TASEP semigroup. There is an actual weak limit

mu_(kappa,rho)=lim_(t->infinity) S_t^kappa nu_rho.

It is invariant, stochastically dominated by nu_rho, and is the greatest invariant law in that order interval. Its stationary currents satisfy

rho(1-rho)<=J_-<=rho,
0<J_+<=min{rho(1-rho), rho/(1+kappa)},
J_-=J_++kappa p_0,

and, for every integer n>=1,

J_+ >= [rho(1-rho)-kappa rho^(n+1)]/(1+kappa n).

In particular, choosing rho=1/[2(1+kappa)] gives J_+>=1/[4(1+kappa)^2]>0. Thus positive stationary **transmitted** flow exists for every finite positive killing rate. This is an existence and selection theorem, not a classification of all stationary laws.

### Proof, including the infinite-volume steps

**1. Ordinary Bernoulli invariance and attractiveness.** On a finite ring the iid Bernoulli(rho) law gives the same weight to all configurations with a fixed number of particles. For each configuration the number of possible outgoing 10 jumps equals the number of incoming 01 jumps, because the numbers of 10 and 01 interfaces on a binary ring agree. Thus the finite forward equation vanishes at this law. Couple larger and larger rings with full-line TASEP using identical initial bits and clocks around a fixed observation interval. For a boundary discrepancy to reach that interval by fixed time T it must traverse an ordered chain of distance d ring clocks; its probability tends to zero, bounded for example by 2(2T)^d/d!. Hence finite-ring stationarity passes to full-line Bernoulli invariance.

The bond update 10->01 is order preserving when applied simultaneously to two coordinatewise ordered configurations. This can be checked in the 9 ordered two-site cases (and is kernel-checked in CouplingChecks.lean). Removal at 0 is likewise order preserving when applied to both configurations. Common-clock coupling therefore proves attractiveness of S_t^kappa. Comparing the killed process eta and ordinary TASEP xi, with eta_0=xi_0 sampled from nu_rho, keeps eta_t<=xi_t because extra removals act only on eta. Since xi_t has law nu_rho, S_t^kappa nu_rho<=nu_rho for all t.

**2. Monotone weak convergence and invariance.** Attractiveness and the preceding domination imply S_(t+s)^kappa nu_rho=S_t^kappa(S_s^kappa nu_rho)<=S_t^kappa nu_rho. For every finite set A, the increasing cylinder moment m_A(t)=E prod_(i in A) eta_i(t) thus decreases and has a limit. For disjoint finite A,B, the probability of ones on A and zeros on B is the finite inclusion-exclusion sum sum_(C subset B)(-1)^|C| m_(A union C)(t), so every cylinder probability has a limit. Limits of these finite distributions are nonnegative, normalized and consistent, defining a probability law mu. Cylinder functions are uniformly dense in continuous functions on the compact product space; their convergence implies weak convergence of the whole time family to mu, not just a subsequence.

The graphical process is Feller: local dependence is approximated by finite boxes with the same clock-path estimate, uniformly over initial states. Thus for every continuous f and fixed s, mu(S_s^kappa f)=lim_t (S_t^kappa nu_rho)(S_s^kappa f)=lim_t (S_(t+s)^kappa nu_rho)(f)=mu(f). This proves invariance. Domination also passes to the limit. If lambda is any invariant probability with lambda<=nu_rho, then lambda=S_t^kappa lambda<=S_t^kappa nu_rho for all t; taking the limit gives lambda<=mu. This proves the greatest-law assertion and specifies the law unambiguously by its initialization/limit rule; it does not assert uniqueness for arbitrary tail conditions.

**3. Finite discrepancies and cut conservation.** In the ordered common-clock pair (eta,xi), write delta_i=xi_i-eta_i. At time zero all delta_i are zero. A common bond clock preserves the total number of discrepancies on its two sites; it can move a discrepancy one step left or right, but cannot create one. An accepted killing at 0 creates one discrepancy there because eta_0=1 implies xi_0=1. There are at most the finitely many rings of the rate-kappa clock during [0,T]. Each discrepancy can move only at its two adjacent rate-one clocks, with total instantaneous rate at most 2. A finite number of births and uniformly bounded movement rates make the discrepancy system nonexplosive, so only finitely many discrepancies and visited discrepancy sites occur during every finite time interval. Equivalently, stopping after a finite number of discrepancy events and using the total movement intensity <=2 times the number of killing-clock rings gives a finite expected movement count <=kappa T^2, allowing removal of the stopping bound. This justifies summing delta over either half-line without subtracting two infinite particle counts.

Let N_i^eta(T), N_i^xi(T) count accepted bond-i jumps. At the left cut immediately before site 0, finite-support conservation gives

D_left(T):=sum_(i<=-1) delta_i(T)=N_(-1)^eta(T)-N_(-1)^xi(T)>=0.

To see the absence of an infinity boundary term explicitly, choose a (sample-dependent) site a to the left of every discrepancy site visited up to T. At bond a-1 both configurations always agree, so their jump counts agree. Sum the local occupation equations on [a,-1]; killing at 0 lies outside it, and the displayed identity follows. Similarly, choosing a site beyond all visited discrepancies on the right gives

D_right(T):=sum_(i>=1) delta_i(T)=N_0^xi(T)-N_0^eta(T)>=0.

The killing site belongs to neither sum. The signs are opposite at the two cuts. No stationarity of the coupled discrepancy field and no finite total particle count are assumed.

**4. Passing currents to the stationary limit.** The compensator of N_i^eta(T) is integral_0^T eta_i(t)(1-eta_(i+1)(t)) dt. For xi its expected value is T rho(1-rho), by ordinary Bernoulli invariance. Taking expectations of the two nonnegative cut identities gives

(1/T) integral_0^T E[eta_(-1)(t)(1-eta_0(t))]dt>=rho(1-rho),
(1/T) integral_0^T E[eta_0(t)(1-eta_1(t))]dt<=rho(1-rho).

The integrands converge as t->infinity, since the laws converge weakly and these are bounded continuous cylinders. Their Cesaro averages therefore converge to J_- and J_+. Thus J_->=rho(1-rho)>0 and J_+<=rho(1-rho). Also J_-<=E eta_(-1)<=rho by domination. The exact invariant current-loss formula from ATTEMPT Section 1 gives J_-=J_++kappa p_0.

**5. Strict outgoing positivity, including large rho.** For each binary configuration the first-hole decomposition gives the finite identity

eta_0=sum_(j=0)^(n-1) [prod_(i=0)^j eta_i](1-eta_(j+1))+prod_(i=0)^n eta_i.

This follows by telescoping P_j-P_(j+1), where P_j=prod_(i=0)^j eta_i. Each summand is <=eta_j(1-eta_(j+1)). Under the invariant law these n bond currents are all J_+. The final all-occupied cylinder is increasing, so stochastic domination bounds its probability by rho^(n+1). Consequently p_0<=n J_++rho^(n+1). Current balance and Step 4 now yield rho(1-rho)<=J_-<= (1+kappa n)J_++kappa rho^(n+1). Divide by the strictly positive denominator to obtain the theorem's bound. Since rho^n tends to zero, choose n so that kappa rho^n<1-rho; the numerator is then strictly positive. This proves J_+>0 for every 0<rho<1, without imposing the small-density restriction.

**6. Quantitative dilute bound.** Let q=E eta_0 eta_1. The identity J_+=p_0-q is exact. Domination gives 0<=q<=rho^2. Therefore J_-=(1+kappa)J_++kappa q. Combining Step 4's lower and upper bounds on J_- gives

rho/(1+kappa)-rho^2 <= J_+ <= rho/(1+kappa).

The lower inequality is the n=1 bound; it is valid even when its right side is negative. At rho=1/[2(1+kappa)], it becomes 1/[4(1+kappa)^2]. Thus as rho decreases to zero, J_+/rho converges to 1/(1+kappa), with an explicit error <=rho. This rigorously recovers the single-particle survival factor as the dilute limit. The algebraic lower and upper implications are separately formalized in CouplingChecks.lean.

This completes the proof of Theorem A.

## Theorem B: reservoir construction with the same positive bound (proved)

Fix kappa>0 and 0<rho<1. On each finite interval [-M,M], M>=1, use injection alpha=rho at -M, extraction beta=1-rho at M, ordinary internal TASEP and killing kappa at 0. Its unique stationary law pi_M is dominated by iid Bernoulli(rho) on that interval. Every infinite-volume weak limit is stationary for full-line killing, dominated by nu_rho, and obeys the current bounds of Theorem A. In particular it has positive outgoing current.

**Proof.** Without killing, the finite product law is stationary for alpha=rho, beta=1-rho, by the exact boundary telescoping calculation already proved in ATTEMPT Section 4. Add killing and use the ordered common-clock coupling, with the same injection and extraction clocks; this yields domination of the killed law at all times when both are initialized with the product law. The finite killed chain is irreducible: move every particle successively to the right extraction boundary to reach the empty state, then use injections and selected rightward jumps to build any desired configuration, arranging the rightmost desired particle first. Each specified finite sequence has positive probability; intervening killings can be avoided for its finite duration. Thus the stationary law is unique and is the long-time limit, and its domination follows.

At stationarity the incoming boundary current is rho(1-p_(-M))>=rho(1-rho), by domination. It equals every internal left current by conservation. The outgoing boundary current is (1-rho)p_M<=rho(1-rho), and equals every right current. Current loss at 0 remains exact. Domination of occupied pair/run cylinders gives exactly the same bounds as Steps 5 and 6 of Theorem A, whenever the run fits inside the interval. For any fixed n this holds for all M>=n.

Extend pi_M outside [-M,M] by independent iid Bernoulli(rho) sites. These extended laws are dominated by nu_rho and have weak subsequential limits by compactness. To verify invariance, couple the finite open system, whose outside sites remain frozen, with the infinite graphical killing process from identical initial coordinates. Only differences at the two distant boundaries can influence a fixed observation interval by time T. Ordered rate-one bond-clock paths yield a probability tending to zero as M grows, uniformly over the initial configurations. The finite extended laws are stationary, so the infinite evolved cylinder distributions differ from them by a quantity tending to zero. Feller continuity then passes this identity through any weakly convergent subsequence and proves invariance of its limit. All inequalities and current formulas concern bounded cylinders and therefore pass to that limit. For every fixed n take M>=n before passing to the limit; the positive-n argument then proves J_+>0. This is an independent finite-reservoir route to existence, not an extrapolation of short-chain numerical data.

The reservoir parameters alpha=rho and beta=1-rho are explicit boundary data. This theorem alone does not claim their equality to stationary tail densities of the infinite limit, nor equality of all limits to the canonical law of Theorem A. Every limit is an invariant law dominated by nu_rho, so Theorem A's greatest-law property does place it below mu_(kappa,rho).

## Further direct consequences (proved)

For the canonical law in Theorem A, each distinct pair of sites satisfies E eta_i eta_j<=rho^2. Write q_i=E eta_i eta_(i+1). Since p_i=J_i+q_i,

rho-rho^2<=p_i<=rho for all i<=-1,
rho/(1+kappa)-rho^2<=p_i<=rho/(1+kappa)+rho^2 for all i>=0.

These are uniform-in-position dilute density bounds, not an assertion of a fixed-rho tail limit. Combined with all two-particle probabilities O(rho^2), they identify the leading small-rho density on either side. These consequences hold for Theorem B's limit laws too, since the same current and domination estimates apply.

The canonical law increases in stochastic order with rho, since the initial Bernoulli laws do and S_t^kappa is attractive. It decreases with kappa, by sharing the smaller-rate killing clock and adding independent extra removals for the larger rate. Its incoming current is nondecreasing with kappa and its outgoing current is nonincreasing with kappa: start the two killing processes from the same Bernoulli configuration. Discrepancies are created or annihilated only at 0. Away from 0 the same finite-discrepancy cut identities as Step 3 apply, giving larger-kappa incoming jump counts at least as large and outgoing jump counts at most as large. Taking expected time averages and the actual weak limits proves the stated current monotonicities. No monotonicity of current in rho is asserted.

No invariant law constructed here with J_+>0 can be an independent product law, by the complete product-law classification in ATTEMPT Sections 2-4.

## External input for the next two results

We use the classical **homogeneous full-line nearest-neighbor TASEP invariant-measure classification**: its invariant laws are mixtures of iid Bernoulli(u) laws, 0<=u<=1, and absorbing ordered step configurations 0 to the left, 1 to the right. The positive-current extremal part is Liggett's classification; the zero-current absorbing configurations also follow directly from nonnegative bond rates, as in ATTEMPT Section 2 without a killing constraint.

Reference: T. M. Liggett, "Coupling the Simple Exclusion Process," Annals of Probability 4(3) (1976), 339–356, DOI 10.1214/aop/1176996084. The exact bibliographic record was fetched from Crossref. The classification is explicitly reported in Basu–Sarkar–Sly, arXiv:1704.07799, PDF pp.1 and 4 (background, not their slow-bond theorem). The primary PDF requests returned an Incapsula HTML challenge, not a PDF; no primary theorem number is invented here. This standard classification is an external known theorem, not re-proved or Lean-verified in this attempt. Theorems A and B did not use it. Theorems C and D below give complete reductions to this stated external input; none is an assertion that the killing problem was solved in that literature.

A useful consequence is that an ordinary full-line invariant law lambda dominated by nu_rho, rho<1, must be a mixture of nu_u with 0<=u<=rho. Indeed the ordered step components are excluded: for any fixed start j the probability of an arbitrarily long occupied block j,...,j+n is <=rho^(n+1), so the event of a fully occupied right ray has probability zero; every ordered step has such a ray. For the remaining Bernoulli mixture, integral u^n dF(u)<=rho^n for every n. If F gave positive mass to u>=rho+epsilon this inequality would fail for large n; a countable union over epsilon>0 proves u<=rho almost surely. These arguments also exclude the all-one law; the empty law is nu_0.

## Theorem C: upstream density and exact incoming current (proved using the external classification)

Fix 0<rho<=1/2. For the canonical law mu_(kappa,rho), and for every limit in Theorem B, the finite-dimensional distributions of a translated observation window converge to iid Bernoulli(rho) as the window moves to minus infinity. In particular the upstream local tail density is rho, and J_-=rho(1-rho) exactly. More generally this holds for every killing-invariant lambda<=nu_rho with J_->=rho(1-rho).

**Proof.** Translate lambda so that an observation window originally near x, x->minus infinity, sits at the origin. The defect then goes to plus infinity. Every weak subsequential limit lambda_* is stationary for ordinary TASEP. To justify this at the semigroup level, compare the translated killing process with ordinary TASEP for a fixed time T and cylinder f. Their difference originates only at the distant killing site. A discrepancy can influence f only through an ordered chain of rate-one bond clocks from that site to its support; the probability is bounded by a quantity tending to zero with that distance, for example kappa T times 2(2T)^d/d!. This bound is uniform in the initial configuration. The translated measure is stationary for its own shifted-defect process, so its expectation of P_T^ordinary f differs from its expectation of f by a quantity tending to zero. Feller continuity and weak convergence prove ordinary invariance of lambda_*.

Domination by nu_rho is translation invariant and passes to the limit. The preceding consequence of the homogeneous classification therefore writes lambda_* as a mixture of nu_u, 0<=u<=rho. The ordinary bond current of lambda_* equals J_-, because all sufficiently far-left bonds of the original law have that exact current. For 0<=u<=rho<=1/2,

rho(1-rho)-u(1-u)=(rho-u)(1-rho-u)>=0,

with equality only when u=rho. Since J_->=rho(1-rho), the mixture must be concentrated on u=rho. Thus every subsequential translated limit is nu_rho, and compactness implies convergence of the whole translated family. Its bond current is rho(1-rho), proving the exact value. This proves the theorem, including its general version.

For the canonical law, current loss and q=E eta_0 eta_1 now give the sharper upper bound

[rho(1-rho)-kappa rho^2]/(1+kappa)<=J_+<=rho(1-rho)/(1+kappa),
p_0=[rho(1-rho)+q]/(1+kappa), 0<=q<=rho^2.

Thus the selected law for rho=1/[2(1+kappa)] has a rigorously identified Bernoulli upstream tail, not merely a formal initialization parameter. The upstream-tail conclusion is local finite-dimensional convergence; it is not a claim of an almost-sure spatial law of large numbers for the nontranslation-invariant measure.

Every downstream translated subsequential limit is similarly a homogeneous Bernoulli mixture supported on [0,rho], with mean flux integral u(1-u)dF(u)=J_+. This does **not** yet show that a downstream mixture is a single Bernoulli law or that all downstream translated limits agree.

## Theorem D: restricted uniqueness at maximal low-density input (proved using the external classification)

Fix kappa>0 and 0<rho<=1/2. Among all invariant probability laws lambda dominated by nu_rho and having incoming current rho(1-rho), the unique law is mu_(kappa,rho). Equivalently, among laws dominated by nu_rho and with upstream local Bernoulli(rho) tail, the canonical law is unique. This is a genuine restricted classification; global domination is essential to its hypotheses and is not deduced from an upstream tail alone.

**Proof.** Theorem A's greatest-law assertion gives lambda<=mu:=mu_(kappa,rho). Start an ordered coupling of lambda and mu, use the same bonds and killing clocks, and time-average the joint law. The marginals remain lambda and mu, the order is preserved, and the joint process is Feller on a compact product space. A weak limit of the averages is a joint invariant ordered law pi: for any fixed time s, the difference between a time average and its evolution has expectation at most 2s||f||/T for a bounded continuous f, which tends to zero. This stationary coupling may have infinitely many discrepancies initially; no finite-discrepancy assertion is used in this proof.

Write the upper configuration as x, lower as y, and delta_i=x_i-y_i. Then Delta p_0=E_pi delta_0>=0. The two incoming currents are equal, so subtracting their stationary killing balances gives

K_+:=J_+^mu-J_+^lambda=-kappa Delta p_0<=0.

Translate the joint law toward plus infinity and take a weak subsequential limit. Exactly the clock-path argument of Theorem C proves this limit invariant for the common-clock **ordinary** two-process coupling. Its marginals are ordinary TASEP invariant and dominated by nu_rho. They are therefore Bernoulli mixtures with random densities U for the upper and V for the lower, both in [0,rho]. The marginal mixture descriptions imply that each configuration's empirical density on sites 1,...,N converges almost surely to its mixture parameter (conditional iid strong law). The preserved coordinatewise order then forces U>=V almost surely in the joint limit. Since u(1-u) increases on [0,rho],

K_+=E[U(1-U)-V(1-V)]>=0.

The equality to K_+ holds because every translated sufficiently far-right bond has the original marginal outgoing currents. Thus K_+=0, Delta p_0=0, and pi(delta_0=1)=0.

It remains to prove equality of the entire configurations, rather than only their occupations at the killing site. Under pi the local ordered-pair colors are 0=(y=0,x=0), 1=(y=0,x=1), 2=(y=1,x=1). A common bond clock swaps neighboring colors precisely when the left color is larger: the possible moves are 20->02, 10->01 and 21->12. Killing is suppressed in the following finite positive-probability clock event.

The upper marginal has infinitely many vacancies to the right almost surely: domination by nu_rho excludes every fully occupied right ray, by the occupied-block bound used above, and finitely many vacancies would leave such a ray. The lower marginal has infinitely many particles to the left almost surely, by Theorem C's upstream Bernoulli(rho) convergence. Explicitly, for any fixed m, the event of at most m particles on the whole negative half-line forces at most m particles in every far-left length-L block. Taking that block's translation limit bounds the event's probability by P(Binomial(L,rho)<=m), which tends to zero as L grows; a countable union over m excludes finitely many left particles.

Suppose pi(delta_i=1)>0 at some i<0. On every such configuration choose -i upper vacancies at finitely many sites to the right of the discrepancy. Move the nearest vacancy left, using permitted swaps with colors 1 or 2, until it lies immediately to the right of the selected color 1; then swap 10->01. This advances that discrepancy one site right. Repeat, using a fresh vacancy each time, until the discrepancy reaches site 0. Each step consumes one vacancy to its right; -i initial vacancies suffice, and there are infinitely many to choose from. All operations use a finite window and a finite sequence of allowed clocks.

If instead pi(delta_i=1)>0 for i>0, select i lower particles (color 2) at finitely many sites to its left. Move the nearest such color 2 right through colors 0 or 1 until it sits immediately to the left of the selected discrepancy; swap 21->12. This advances that discrepancy one site left and consumes one color 2 on its left. Repeat with fresh lower particles until the discrepancy reaches site 0. The infinitely many lower particles to the left supply the required finite number.

To make these configuration-dependent paths a probability argument, first choose a fixed finite resource window and then a fixed color word in it with positive pi probability; countability of window choices and finiteness of words ensures such a choice if pi(delta_i=1)>0. Require the resulting finite clock sequence to occur in prescribed successive small subintervals of [0,1], with all other clocks in the resource window, both window-boundary clocks, and the killing clock silent for the relevant duration. This event has strictly positive probability, independent of the initial word. After the discrepancy reaches 0, keep the window clocks silent until time 1. Then delta_0(1)=1 with positive probability. This contradicts stationarity and pi(delta_0=1)=0. A single vacancy cannot be reused to advance a left discrepancy repeatedly; the proof explicitly supplies one fresh vacancy per step. Similarly it supplies one fresh lower particle per leftward step.

Consequently pi(delta_i=1)=0 for every i!=0, and also for i=0. A countable intersection gives x=y almost surely. Their marginal laws are equal, so lambda=mu, proving restricted uniqueness.

`reachability_checks.py` checks the finite color-propagation step independently on all 243, 2,187 and 19,683 words of lengths 5,7,9. Whenever a discrepancy has enough right vacancies to reach the center, or enough left common particles to reach it, exact acyclic reachability under permitted color swaps succeeds. Every one of the 155+1,751+17,581 resource-sufficient words passed. This tests the new critical finite step; the arbitrary-distance proof is the explicit fresh-resource construction above.

### Corollary: convergence of finite reservoirs in the low-density range

For 0<rho<=1/2, the full sequence of Theorem B's finite stationary laws converges locally to mu_(kappa,rho) as M->infinity. Indeed every subsequential limit is invariant, dominated by nu_rho and has J_->=rho(1-rho). Theorem C makes its incoming current exactly rho(1-rho), and Theorem D then identifies it with mu_(kappa,rho). Compactness and uniqueness of every subsequential limit give full convergence. This settles the reservoir-limit uniqueness that was left open at the end of Theorem B **in this low-density range**; it does not settle rho>1/2 or arbitrary reservoir data.

## Hostile-referee audit of the second attempt

1. **Stochastic domination is not a current inequality.** eta_i(1-eta_(i+1)) is not increasing. No current comparison was inferred directly from stochastic order. Theorem A obtains it from accepted-jump counts and finite discrepancies; Theorem B obtains it from the increasing boundary vacancy/occupancy formula and stationarity. These independently yield the same lower incoming bound.
2. **The infinite sum contains discrepancies, not particles.** Step A3 proves finitely many discrepancy movements and births during each bounded time interval before summing over either half-line. The proof never subtracts two infinite total particle counts. The two signed cut identities are kernel-checked locally and tested after 50,000 random graphical events.
3. **Stationarity of a limit is not assumed from pointwise densities.** All increasing cylinder moments converge; inclusion-exclusion then gives every finite distribution. The Feller semigroup identity proves stationarity at every fixed time. The finite-reservoir proof uses a separate uniform boundary-distance estimate.
4. **No unjustified exchange of space/time limits.** Theorem A first takes the actual time-law limit and obtains currents by Cesaro averaging. Theorem C translates that stationary law and separately proves homogeneous stationarity of each spatial limit by remote-defect clock paths. It does not interchange the initial finite-time Bernoulli tails with t->infinity.
5. **No hidden small-kappa assumption.** The occupied-run bound holds for every n. For any 0<rho<1 and finite kappa, rho^n->0 makes some bound positive. The explicit n=1 positive bound uses a stated rho depending on kappa. Exact finite checks include kappa=8.
6. **No independence at the defect.** All pair and run bounds use increasing-cylinder domination by the reference iid law, not independence of eta. The relation p_0=J_++E eta_0 eta_1 is exact.
7. **Primary-source access is distinguished from theorem use.** The homogeneous classification is a classical external input, supported by the fetched Basu–Sarkar–Sly background and exact Liggett bibliographic record. The primary Liggett requests returned HTML challenges. Its proof was not re-established here. A and B are independent of that theorem; C and D explicitly use it. No slow-bond result is transferred to killing.
8. **Order of mixture densities is justified.** In the downstream translated coupling, each marginal is a mixture of entire iid configurations, not just matching one- and two-site moments. Conditional strong laws therefore supply densities U,V, and coordinatewise order gives U>=V. Monotonicity of u(1-u) is used only on [0,rho] with rho<=1/2.
9. **Zero discrepancy at 0 is not treated as global equality.** Theorem D proves a finite forcing path from any other discrepancy to 0. A fresh hole/common particle is supplied for each step. Infinite right vacancies follow from domination, and infinite left particles follow from the proved upstream local tail. Exact finite color reachability checks every resource-sufficient configuration through length 9. No finite total discrepancy count is required for this stationary uniqueness coupling.
10. **The restricted uniqueness hypothesis is retained.** Global domination by nu_rho is stronger than a Bernoulli upstream tail. The theorem does not silently remove this condition or claim uniqueness of all invariant laws with that upstream tail. Occupied downstream tails from the first attempt lie outside this class.
11. **Finite computations have a precise role.** Eight finite generators were solved in exact rational arithmetic; all forward residuals vanish. Their domination moment tests are necessary checks, not a stand-alone proof of stochastic domination. Exhaustive Boolean/color steps and Lean checks verify local mechanics and algebra, not the infinite stochastic theorem.

## Remaining gap after the further attempt

Positive transmitted-current existence is now proved for every kappa>0. A canonical limiting family and a finite-reservoir construction are available; for rho<=1/2 they have the Bernoulli(rho) upstream tail and restricted uniqueness under global Bernoulli domination. These settle substantial parts of the old gap.

The full question still lacks an exhaustion theorem for arbitrary correlated invariant laws. In particular this attempt does not classify laws outside a global low-density Bernoulli envelope, high-density/blocking downstream regimes, or mixtures of possible tail parameters. It does not prove that the canonical downstream translates converge to a single Bernoulli law, identify that downstream density explicitly, or give uniqueness for arbitrary prescribed pairs of tail densities. The zero-outgoing-current half-line family from the first attempt is still not shown here to exhaust all half-line laws. The two-sided defect matrix ansatz remains an unpursued route. Verdict remains PARTIAL.
