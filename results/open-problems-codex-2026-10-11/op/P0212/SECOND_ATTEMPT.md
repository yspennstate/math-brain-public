# Second serious attempt — 2026-10-11

## Two approaches not used in the first attempt

**A. Mobile-target range + subadditive ergodic theorem + rare-event Poisson approximation.** Replace the interacting equilibrium background temporarily by independent walks started from Bernoulli(p) sites. Conditional on a tagged walk, background particles are independent rare categorical marks. Their total first-hit intensity is a random mobile-target Wiener-sausage volume. Prove a deterministic linear growth constant for that volume by Kingman's theorem, identify the constant using the range of the relative walk, and bound late repeat contacts. Then extend to several tags by bounding background particles that hit more than one tag. This attacks the missing fresh-encounter and clock-independence assertions in a stronger comparison model, rather than another isolated birth trial.

**B. Stationary rooted-graph incidence / mass transport counterexample search.** Make the occupation-Palm and pruned-lineage conventions precise, derive birth/merge edge-incidence identities through a finite torus limit, and test whether the proposed equal-clock recursive graph satisfies those identities. The raw 1:2 hazard calculation in the first attempt suggests a possible normalization or root-bias obstruction. However, it does not yet survive pruning or distinguish an ordinary Palm root from a distinguished immortal spine. A counterexample to an arbitrarily chosen convention would not settle Aldous's underspecified original formulation.

Pursue A first: it promises a fully specified theorem with a direct proof of joint Poisson clocks and negligible late returns. B remains a diagnostic, not a claimed counterexample.

Brain queries: the actual gap's words (Palm genealogy, fresh collisions, repeat encounters, Wiener sausage, Poisson limit), and separately Kingman subadditive ergodic theorem / moving target / rare events. Retrieved cards are hints, not proofs. A moving-Boolean-model scar warns that a void-probability reduction alone does not solve a Wiener-sausage problem. Our task needs only an asymptotic linear growth constant, not an exact finite-time sausage volume.

## Work in progress

The first comparison system has a rate-one simple tagged walk X on Z^d, d>=3, and independent rate-one simple background walks Y^z, each included independently with probability p at time zero. Included backgrounds never branch or coalesce. Bernoulli initial occupancy is not preserved by these free walks: multiple walkers can later occupy a site. Corollary 11 below replaces Bernoulli inclusion by a Poisson(p) number of independent walks at every site, which does give a stationary comparison background. No coupling to the interacting system is assumed.

For a fixed tagged path define A_T(X)=sum_z P(Y^z hits X during [0,T] | X). Next: prove subadditivity, identify the Kingman constant as 2/G(0,0), establish conditional Poisson first-hit counts, and bound repeat contacts and shared background particles for multiple tags. Each step must be proved before claiming a stronger special case.

## Lemma 6: deterministic contact-volume growth

Write q=1/G(0,0), where G is the discrete-time simple-walk Green function from the first attempt. Almost surely in a rate-one tagged walk X,

    A_T(X)/T -> 2q as T -> infinity,

and the convergence is in L1 under the law of X.

Proof. First A_T is finite for every finite-jump tagged path. Count contact entries rather than just first contacts. Initial contact contributes total mass 1 when summed over all background starting sites. Each jump of the tagged path contributes at most 1 in total expected background mass, since sum_z P_z(Y_t=y)=1 for every site y and t. Background jumps onto the current tagged site contribute total expected mass at most T: at any time the sum over all starting sites of rates from its neighbors onto that site is 1. Thus

    0 <= A_T(X) <= 1 + N_X(T) + T.

This bound does not require the backgrounds to be thinned. Simultaneous jumps of the tagged walk and a background walk have probability zero. A contact that is not initial must arise from one of these entries, so the bound covers all first contacts. In particular E A_T <= 1+2T.

For deterministic s,t and a tagged path, ignore any prior contact when counting contacts in [s,s+t]. The Markov property of the background at s and conservation of counting measure give

    sum_z P_z(Y hits X during [s,s+t] | X)
      = sum_w P_w(Y hits (X_{s+u})_{0<=u<=t})
      = A_t(theta_s X),

where theta_s X is the increment path X_{s+u}-X_s; the last equality is translation invariance. This ignores prior hits intentionally, and hence the union bound gives

    A_{s+t}(X) <= A_s(X) + A_t(theta_s X).

Place the tagged walk on a two-sided iid sequence of unit-time increment path blocks. Define the subadditive array B_{m,n}=A_{n-m}(theta_m X) for integer m<n. The preceding inequality gives B_{m,n}<=B_{m,k}+B_{k,n}. The full array is covariant under the unit shift of the increment blocks, not merely stationary separately in each row. That shift is measure preserving and ergodic because the blocks are iid. The bound above gives E B_{0,1}<=3 and B_{0,n}>=0. The stationary ergodic, integrable subadditive theorem of Kingman therefore applies: A_n/n converges almost surely and in L1 to a deterministic constant a, and a=lim_n E A_n/n=inf_n E A_n/n. These are the exact hypotheses used; no assertion that Kingman alone identifies a is made.

To identify a, average over X as well. For each z, Y^z-X is a rate-two simple walk started at z (translate X_0 to zero). Therefore, by symmetry and Tonelli,

    E A_T = sum_z P_z(rate-two walk hits 0 by T)
          = sum_z P_0(rate-two walk hits z by T)
          = E R_{N_{2T}},

where R_n is the number of distinct sites visited by a discrete simple walk through step n and N_{2T} is an independent Poisson(2T) variable.

For completeness, E R_n=sum_{j=0}^n q_j, with q_0=1 and q_j=P_0(S_1,...,S_j all differ from 0). Indeed the site at step j is new exactly when its reversed last j increments have no zero partial sum; iid symmetric increments make that probability q_j. The decreasing sequence q_j tends to the probability of no positive-time return, equal to q=1/G(0,0) by the first-step calculation in Proposition 2. Cesaro averaging gives E R_n/n->q. Given epsilon>0, choose K with |E R_n-qn|<=epsilon n for n>=K; for n<K the absolute error is bounded by a constant C_K. Consequently

    |E R_{N_{2T}} - 2qT| <= 2epsilon T + C_K.

Hence E A_T/T->2q and a=2q. Monotonicity A_floor(T)<=A_T<=A_ceil(T) extends the almost sure convergence to real T. It also gives L1 convergence, using the corresponding integer L1 limits and the factors floor(T)/T and ceil(T)/T. QED, invoking only the stated classical subadditive ergodic theorem as an external theorem.

## Theorem 7: Poisson fresh-contact clock in the free background

For each included background particle define tau_z=inf{t>=0:Y^z_t=X_t}. Its mark is counted only once, at its first contact. For any fixed 0=t_0<t_1<...<t_k, let C_{p,j} be the number of included particles whose first contact lies in (t_{j-1}/p,t_j/p]. Conditional on almost every complete tagged path X, the vector (C_{p,j}) converges in total variation to independent Poisson variables of means 2q(t_j-t_{j-1}). An initial contact at time zero has probability p and can be excluded without changing the limit.

Proof. Given X, let a_{z,j}=P(tau_z lies in interval j | X). For each z the categorical mark has probabilities p a_{z,j} and otherwise no mark. These marks are independent across z, including the Bernoulli inclusion variables and the background trajectories. Their cumulative parameter sums are

    lambda_{p,j}=p[A_{t_j/p}(X)-A_{t_{j-1}/p}(X)]

with the interval convention at zero requiring subtraction of A_0=1 (rather than assigning it to the first interval). This changes the first parameter by at most p. Lemma 6 gives lambda_{p,j}->2q(t_j-t_{j-1}).

Here is a direct categorical-to-Poisson bound, so no undeclared independence theorem is needed. If a single mark has total probability b and conditional type distribution v, compare it with a Poisson(b) number of independent types with law v. Couple the types identically when both counts equal 1. The total variation distance of Bernoulli(b) and Poisson(b) is b(1-exp(-b))<=b^2, obtained by summing the probabilities at 0,1 and >=2. Thus the categorical vector is within b^2 of independent Poisson variables of its category means (Poisson splitting follows by their joint probability generating function). Taking independent couplings for all starting sites, the distance for the sum is at most sum_z b_z^2, where b_z=p sum_j a_{z,j}<=p. Because sum_z b_z<=p A_{t_k/p}(X)<infinity,

    sum_z b_z^2 <= p^2 A_{t_k/p}(X) -> 0.

Countably many sites cause no problem: restrict to a growing finite set, and the probability of a mark from its complement is at most the tail of the summable parameter series. Pass to the limit in the finite-set coupling. Finally independent Poisson laws with mean vectors lambda and mu have total variation distance at most sum_j |lambda_j-mu_j|, by coupling each component through their common minimum rate. This proves the claimed conditional convergence. Integrating bounded conditional errors gives the annealed result and asymptotic independence from any bounded measurable function of the tagged path. QED.

## Lemma 8: all late repeated contacts are negligible

For T>=1 and L>=1, the probability that some included background particle first meets X by T and meets it again at a time >=tau_z+L is at most

    C_d p (1+2T) L^(1-d/2).

Proof. For a single background walk, at its first meeting the pair (X,Y^z) is at the same site. This is a stopping time for the joint pair filtration. By the strong Markov property, their subsequent difference is a fresh rate-two simple walk started at zero. For that relative walk let sigma=inf{u>=L:Z_u=0}. On {sigma<infinity}, the holding interval beginning at sigma has mean 1/2. This is also valid when sigma=L and Z_L=0. Therefore

    r_L=P_0(exists u>=L with Z_u=0)
       <=2 integral_L^infinity k_u(0,0)du
       <= C_d L^(1-d/2),

using the heat-kernel bound proved in Proposition 2. For each z, independence of inclusion and the pair's strong Markov property give

    P(z included, tau_z<=T, late contact) = p P(tau_z<=T) r_L.

Summing over z and applying the union bound proves the result using E A_T<=1+2T. Other backgrounds need not be independent of these contact events for the union bound. Take T=H/p and any L->infinity with pL->0. With probability tending to one, every encountered background particle has all of its contacts inside a window of length L after its first hit; those windows have vanishing rescaled duration. This is an actual repeat-contact estimate, not just a thinning heuristic. It concerns repeats with the same free background particle. QED.

## Lemma 9: a background particle almost never reaches two independent tags

Let X^1,X^2 be independent rate-one simple tagged walks, with arbitrary deterministic starting sites a,b. Put B_T=number of included background particles that hit both tags by T. Uniformly in a,b,

    E B_T <= C_d p [1 + integral_0^T (1+s)^(1-d/2) ds].

At T=H/p this is O_H(sqrt(p)) in d=3, O_H(p log(1/p)) in d=4, and O_H(p) in d>=5. In particular P(B_T>0)->0.

Proof. Let h(w)=P_w(rate-two relative walk ever hits 0). Strong Markov at its first hit gives

    h(w) = (2/G(0,0)) integral_0^infinity k_u(w,0)du,

including w=0. Here k is the rate-two transition kernel; its occupation Green function at zero is G(0,0)/2. If D_s=X^1_s-X^2_s, convolution and symmetry give

    E h(D_s+c) = (2/G(0,0)) integral_s^infinity k_v(a-b+c,0)dv
               <= C_d (1+s)^(1-d/2)

for every fixed c, uniformly in a-b+c, by the heat-kernel bound. This controls both c=0 and each nearest-neighbor c.

A particle that hits both tags has an initial contact with one tag, or a contact entry with that tag by time T, followed by a contact with the other tag (allow a tie). Use all contact entries, even repeated ones, to upper bound such particles. Initial contacts contribute at most 2p when summed over starting sites and both possible orders.

For the order first tag 1, then tag 2, classify contact entries of Y^z onto X^1:

1. Y^z jumps from a neighbor onto X^1_s. Conditional on the positions immediately after this entry, the probability of subsequently meeting X^2 is h(X^1_s-X^2_s), because Y^z and X^2 have independent fresh future increments. The entry time is a stopping time for the pair (Y^z,X^1); X^2 remains independent of that pair. More formally one may include all three walks in the filtration and apply their joint strong Markov property. Summing the compensator over z and neighbors uses sum_z P_z(Y_s=x)=1 and total Y jump rate 1. Its expected marked-entry contribution is integral_0^T E h(D_s) ds.
2. X^1 jumps by a nearest-neighbor vector e onto Y^z. Sum over all background starting sites at the jump destination: their total unconditioned mass is again 1. The probability of a later contact with X^2 is h(X^1_{s-}+e-X^2_s). Averaging the tag's rate-one jump directions gives contribution integral_0^T (1/(2d))sum_{e~0} E h(D_s+e) ds. The value at a deterministic time s is unaffected by replacing the pre-jump walk by its ordinary law; the compensator is integrated over deterministic s.

These are expectations of unconditioned free walks. They do not assume the background has avoided prior contacts. One justifies the marked compensator calculation first for finitely many z and a finite time horizon, then sums by Tonelli; the finite bound above guarantees convergence. The future-contact indicator is not predictable, but its conditional expectation at each entry is h, so conditional expectation precedes the ordinary predictable compensator calculation.

Multiply these sums by p for inclusion, apply the heat bound, and repeat for the reverse order of the two tags. Every doubly hitting particle is counted at least once in the resulting upper bound, proving the claim. The three rates in the statement are obtained by directly integrating (1+s)^(1-d/2). QED.

## Theorem 10: joint independent fresh-contact clocks

For any fixed m independent rate-one tags X^1,...,X^m (with arbitrary deterministic starting sites), their vectors of first-contact counts from the same Bernoulli(p) free background, at finitely many rescaled time intervals up to H, converge jointly to m independent rate-2q Poisson processes. Conditional on the tagged paths, the finite vectors of counts converge in total variation in probability over those paths. Their annealed total variation distance to the deterministic Poisson product tends to zero.

The statement also holds after conditioning two initially adjacent tags never to meet: that conditioning has probability q>0. It even holds under any tag-path conditioning events with probabilities bounded below by a fixed positive constant, including no meeting up to a diverging pruning time.

Proof. Given all tags, let b_z be the probability that Y^z hits at least two tags by H/p. Lemma 9 and the union bound over tag pairs imply

    E[p sum_z b_z] -> 0.

Therefore the conditional expected number p sum_z b_z tends to zero in probability, and the actual probability of any included multiply hitting particle tends to zero. Replace each background mark by a categorical mark that records its first contact time interval and tag only if it hits exactly that one tag by the horizon; discard all other marks. The replacement changes the original count vector with probability at most p sum_z b_z, conditional on the tags.

The exclusive marks are independent across initial sites given the tags. Their total probability per site is at most p. The categorical coupling of Theorem 7 consequently has error at most

    p^2 sum_{i=1}^m A_{H/p}(X^i) -> 0 almost surely.

For each tag and interval its exclusive parameter differs from the original first-hit parameter by at most p sum_z b_z. (The original first hit of that tag is counted regardless of earlier hits of other tags; exclusion removes it only for multiply hitting walks.) Lemma 6 applies to every tag simultaneously, so all original parameters tend almost surely to 2q times the interval length. The exclusive parameters converge to those same deterministic limits in probability. Poisson minimum-rate couplings now give conditional total variation convergence in probability. As this distance lies in [0,1], its expectation tends to zero, proving annealed total variation convergence.

For conditioning, denote that bounded conditional distance by epsilon_p(paths). We have E epsilon_p->0. If E_p is any event determined only by the tag paths with P(E_p)>=delta>0, then E[epsilon_p | E_p]<=E epsilon_p/delta->0. The conditional backgrounds are still independent given the complete tagged paths. This proves the conditioned version, including adjacent tags' nonmeeting probability q established in the first attempt. This conditioning argument does not mistakenly apply a free strong Markov property after conditioning; all estimates are first proved under the unconditioned law and then transferred by absolute continuity. QED.

The analogous repeat-contact assertion under these conditioning events follows by dividing Lemma 8's probability bound by delta and summing over the finitely many tags. For adjacent surviving siblings this gives independent external encounter clocks in the *free* comparison model, together with jitter windows of vanishing duration.

## Corollary 11: the same theorem with an actually stationary background

Put independent Poisson(p) numbers of rate-one free walks at every lattice site. Their occupation counts form a stationary reversible independent-walk system, with product Poisson(p) marginal at every fixed time. Theorems 7 and 10 and Lemmas 8 and 9 hold for this background as well. Thus the joint encounter-clock theorem is a theorem for a stationary comparison system, not only a dilute initial condition.

Proof. At time t, the particles from initial site z split into independent Poisson counts at sites w, of means p k_t^{(1)}(z,w). This follows by the generating function of a Poisson number of independent marks. Summing over z gives independent counts at different sites with means p sum_z k_t^{(1)}(z,w)=p. These countable sums are well defined because their means are finite. This proves stationarity of the product law under the Markov semigroup.

Here is a direct lattice proof of reversibility. For nonnegative finitely supported functions phi,psi, Poisson marking gives the joint Laplace functional of the counts at times 0 and t:

    E exp[-sum_x phi(x)N_0(x)-sum_y psi(y)N_t(y)]
      = exp[p sum_{x,y} k_t^{(1)}(x,y)(exp(-phi(x)-psi(y))-1)].

The exponent is absolutely summable, since its summand vanishes when both test functions vanish and the heat kernel has both row and column sums 1. Symmetry k_t^{(1)}(x,y)=k_t^{(1)}(y,x) makes the functional invariant under swapping phi and psi, proving the two-time law's symmetry. Laplace transforms determine the finite collections of counts. This symmetry says the stationary semigroup is self-adjoint: E[f(N_0)g(N_t)]=E[g(N_0)f(N_t)] for cylinder f,g, and then for bounded functions by approximation. The Markov property and this identity, applied successively across a finite list of time increments, reverse every finite-dimensional stationary law. Thus the system is reversible. No use of reversibility is required for the contact limits.

Conditional on one tagged path, the number of particles first hitting in different time intervals is now *exactly* a vector of independent Poisson variables with means p times the corresponding A increments. It is a Poisson marking of the background trajectory cloud, so the categorical approximation error of Theorem 7 is absent. Lemma 6 still sends these means to 2q times interval length. For multiple tags, exclusive-contact marks are likewise independent Poisson categories; multiply hitting particles are the only obstruction, and Lemma 9 bounds their expected number because the expected number of particles per starting site is p. Lemma 8 uses only the same first moment and pair Markov property, so it too carries over. The rest of Theorem 10's parameter and conditioning argument is unchanged.

A typical particle at time zero in the stationary free system has a further useful Palm description. Size bias the site's count N~Poisson(p), then distinguish one of its N particles: P(N=n under particle Palm)=n P(N=n)/p=P(1+Poisson(p)=n). The other particles at that site and at all other sites are an independent Poisson(p) cloud, and the distinguished particle's future walk is independent of them. Thus the one-tag theorem is also a genuine particle-Palm theorem for this stationary free system. It is not an occupation-indicator Palm statement, which would condition N>=1 instead of size biasing N. QED.

For d=3 take L=p^(-2/3). On a horizon H/p, late-repeat probability is O_H(p^(1/3)), and its jitter duration is pL=p^(1/3). Shared-particle probability for any fixed number of independent tags is O_H(sqrt(p)). The intensity self-averaging argument gives convergence but no claimed quantitative rate for it.

## External theorem checked against an actual text

The brain's named-result card was read in full: claim_ebec7808fe9525a999343d3c0f7cd49f6b8e5b5e3f851984870ca1aa89e16652. Its Kingman hypotheses were independently checked against Rick Durrett, *Probability: Theory and Examples*, fifth-edition author PDF dated in the filename January 11, 2019, downloaded from https://services.math.duke.edu/~rtd/PTE/PTE5_011119.pdf. In this PDF the applicable theorem is **Theorem 6.4.1**, printed page **343**, PDF page **351**, not the 6.6.1 numbering recalled by some cards. Its remark states Kingman's stronger full-array stationarity assumptions; the theorem itself is Liggett's version. Every fixed-block shift of iid unit increment blocks is ergodic, so this theorem's extra ergodicity hypothesis is also satisfied. The statement and relevant extracted pages are preserved in subadditive_reference.txt. The theorem supplies an almost sure and L1 constant, not a convergence rate or a numerical value; Lemma 6 separately identifies that value.

Kingman's standard references are J. F. C. Kingman, *The ergodic theory of subadditive stochastic processes*, Journal of the Royal Statistical Society, Series B **30** (1968), 499–510; and *Subadditive ergodic theory*, Annals of Probability **1**(6) (1973), 883–909, DOI 10.1214/aop/1176996798. The latter metadata was checked through Crossref; Durrett's bibliography confirms its pages. This is use of a known tool, not a literature solution to P0212.

## Hostile-referee checks

1. **Full stationarity and ergodicity of the subadditive array:** supplied by iid path blocks, not inferred from the spatial stationarity of a cloud. All fixed block shifts are ergodic. Integrability is provided by the explicit 1+N_X(T)+T bound.
2. **Quenched versus annealed intensity:** the annealed range identity alone would not give Poisson clocks; Kingman's almost sure, deterministic limit is essential. Conditional independence is only across free background trajectories. The interacting background does not satisfy this hypothesis.
3. **Subadditivity uses an unconditioned later segment:** it follows from conservation of counting measure when prior hits are ignored. Conditioning the cloud on prior avoidance would destroy that exact identity; the proof does not do so.
4. **Countably many initial particles:** conditional first-hit parameter is finite, with explicit tail control by summable mass. Poisson and categorical sums are justified by finite truncation, not by an unproved infinite-product manipulation.
5. **An initial point at time zero:** it has mean/probability O(p) and is explicitly removed or included as a vanishing error. It is not part of a continuous-rate Poisson process in the limit.
6. **Shared target histories:** one-tag conditional convergence is almost sure; multi-tag conditional convergence is only in probability, because the shared-path estimate is an annealed bound. No stronger quenched assertion is claimed.
7. **Repeated contacts:** the first-contact Poisson theorem alone would not control jitter. Lemma 8 proves a separate all-future late-return estimate. It uses unconditioned pair Markov properties before any tag-path conditioning.
8. **Conditioned surviving siblings:** estimates transfer by a positive-probability change of measure, not by claiming conditioned increments remain independent. Events whose probabilities vanish are not covered by this argument.
9. **Bernoulli versus stationary Poisson cloud:** Bernoulli is not invariant for independent free walkers. Corollary 11 fixes that and gives an actual stationary particle-Palm comparison. This is still a different microscopic model from CBRW and the constrained Ising process.
10. **Collision rate factor:** free encounters have rate 2q per unit rescaled time, while an isolated lasting CBRW birth has rate q in beta time. This does not prove a counterexample: an interacting cloud, pruning, and the reference-spine convention have not been identified with the free comparison. It is a concrete normalization/root-sampling check, not a conclusion about the original conjecture.
11. **Exact finite check:** second_checks.py checks conditional contact-volume subadditivity with Fraction arithmetic for all 256 four-step tagged paths on a four-cycle and all three interior splits (768 inequalities). It also checks categorical convolution normalization and moments exactly.
12. **Formal check:** LocalBalance.lean from the first attempt was rerun with minimal imports, from ~/lean_verify, with a one-hour timeout and one check at a time. It completed with exit code 0; lean_second.log contains only nonfatal linter warnings. Its four algebraic identities are kernel checked, with no sorry or native_decide. This does not formalize Kingman or the analytic/probabilistic comparison theorem.

### Numerical audit actually completed

The exact four-cycle checks all passed. The simulation used an exactly stationary Poisson(p) cloud on a finite 3D torus with two independent tags initially adjacent, 60 trials per density, seed 21210112. The observations span T=1/p. Background walks remain independent and are never merged or branched. Within each interval between tagged jumps and observation boundaries, independent Poisson counts of background jumps were generated; their ordered steps were followed against the fixed tags. Since particles do not interact, ordering steps of different background particles is immaterial. Observation intervals were split before assigning first-contact marks, so no discrete-time approximation was made. Torus rather than lattice and finite samples are explicit limitations.

| p | torus side | tag-1 mean | tag-2 mean | p times simulated relative range mean | mean shared particles |
|---|---:|---:|---:|---:|---:|
| .08 | 53 | 1.750 | 1.900 | 1.606 | .283 |
| .04 | 67 | 1.433 | 1.517 | 1.506 | .100 |
| .02 | 89 | 1.133 | 1.467 | 1.434 | .167 |
| .01 | 117 | 1.333 | 1.433 | 1.413 | .083 |

The asymptotic infinite-lattice mean is 2q=1.31892534, but the *finite-time* mean is p E R_{N_{2/p}}, including the initial point. Each relative-range value in the table is separately estimated from 1200 walks on the same finite torus. Thus comparisons to 2q alone would confuse finite-time range corrections with a theorem failure. Standard errors for tag means are about .13–.18 and are saved in second_checks.json. The .02 tag-1 mean lies about 2.1 estimated standard errors below its finite-time prediction; this is recorded rather than omitted. These small samples provide a sanity check, not a validated convergence rate or statistical proof. In particular shared-contact frequencies are not monotone in this sample, and no monotonicity was predicted. Empirical covariance is noisy and cannot establish independence.

The job finished in 253.64 seconds, with arrays of about 12,000–16,000 background positions per trial and 2 tags; there is no large stored trajectory tensor. Raw numerical results, variances, covariances, standard errors, and finite-time predictions are in second_checks.json. The mathematical independence claim rests on Lemma 9 and the exclusive-mark proof, not on these samples.

## What remains for P0212

The original stationary, branching/coalescing two-model theorem remains unproved. The new result establishes fresh Poisson clocks, independence between finitely many tags, and negligible repeated encounters for a stationary *free-walk* background. It therefore closes these steps in a stronger, precisely defined comparison problem, not in the original problem.

The missing transfer is now explicit: show that, after pruning, the conditional law of previously unexposed CBRW families along an explored tagged genealogy can be replaced by the free trajectory cloud (or by a comparably tractable process) with vanishing error on a time horizon H/beta. There is no such coupling here. Background births occur at rate beta per particle and run for times of order 1/beta, so ignoring them is an order-one change along a potential encountered lineage. Background coalescences are also order one. One-time product equilibrium or Bernoulli-to-Poisson marginal closeness cannot remove these pathwise interactions.

Moreover tags newly discovered in a genealogy are selected at random encounters, not fixed independent external walks. Theorem 10 covers positive-probability tag-path conditioning and independent starts; it does not by itself cover repeated Palm/exploration posterior laws of adaptively selected CBRW families, nor a two-sided marked genealogical graph. A successful transfer must identify the root/spine convention and its rate constants rather than replacing raw event intensities by participant hazards. The constrained-Ising effective-cluster reduction from the first attempt is still missing as well.

Approach B was formulated but not promoted to a counterexample: no pruned mass-transport identity for the source's precise reference-lineage law has been proved. With the remaining transfer and model-2 reduction recorded, the verdict remains PARTIAL.
