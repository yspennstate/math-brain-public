# P0212 — research record, 2026-10-11

## Exact target and conventions

Aldous, *The low-density limit of coalescing branching random walk*, Problem A (posted 2012; March 2018 update), https://www.stat.berkeley.edu/~aldous/Research/OP/cbrw.html, downloaded as source.html.

The source takes Z^3 for concreteness and says that transience is what matters. Model 1: continuous-time simple random walks, binary branching at rate beta with daughter at a neighboring site, immediate coalescence on meeting, in a translation-invariant stationary law of intensity p(beta). Model 2: the constrained Ising process of slides 16–17 of persi-ising.pdf, on Z^3, with equilibrium iid Bernoulli(p). The desired limit forgets positions, keeps splits and merges, and is rooted at a reference particle at time zero. Its doubly infinite reference lineage has rate-one Poisson split and merge processes; each new forward/backward lineage recursively has such events. Short parent–daughter reunion jitter is discarded, and the proposed convergence is finite-dimensional in time. Problem B (changing graphs) is excluded here.

Verbatim Problem A:
> The issue is to show that, for Models 1 and 2 and related models where there is a stationary distribution, as the intensity (which depends on model parameters) tends to 0, the suitable time-rescaled process in which we track the ``lineages" (splits and merges) but not the spatial positions, of the particles, converges in distribution to the following simple limit process.

The page does not define a topology on sampled genealogical graphs, a particular pruning operation, a spine selection convention at binary vertices, or a normalization of the simple-walk rate. These are formulation gaps, not a counterexample. A natural root law for Model 1 is occupation Palm measure (condition on occupancy at the origin). For the concrete calculations below total walk rate is 1, daughters choose each of 2d neighbors uniformly, and d>=3 unless otherwise stated. Equal symmetric walk/birth kernels are essential to the exact equilibrium calculation. No claim for arbitrary transient graphs or arbitrary daughter kernels follows from it.

## Proposition 1: exact equilibrium for the concrete symmetric Model 1

On Z^d, in any dimension, iid Bernoulli(p) with p=beta/(1+beta) is invariant and reversible for the above CBRW. On a finite connected regular graph with symmetric neighbor choices, its restriction conditioned on nonemptiness is also invariant and reversible. This proves existence of this equilibrium law; no uniqueness assertion in infinite volume is needed or claimed. More generally replace walk rate 1 by a>0 to get p=beta/(a+beta).

Proof. First work on a finite regular graph of degree k. For each directed edge x->y, a particle at x jumps to y at rate 1/k, and creates a particle at y at rate beta/k. Occupied-target births have no configuration effect; a jump onto an occupied site removes x and retains y. Let mu be product Bernoulli(p), initially unconditioned, including the empty absorbing state.

Every configuration transition is one of the following, with other sites fixed:

1. An edge 10 becomes 01 by a jump. Its reverse has the same rate 1/k and the configurations have the same product weight.
2. An edge 10 becomes 11 by a birth x->y, at rate beta/k. Its reverse is a coalescing jump y->x, at rate 1/k. The local weights are p(1-p) and p^2, respectively. The balance identity is p(1-p) beta = p^2, equivalent to beta(1-p)=p, which holds for p=beta/(1+beta).
3. A coalescing jump 11->01 is the reverse of the analogous birth 01->11.

If several arrows cause the same configuration transition, add their individually balanced contributions. Thus mu(s)Q(s,t)=mu(t)Q(t,s) for every distinct s,t. Including the diagonal Q(s,s)=-sum_{t!=s}Q(s,t) gives sum_s mu(s)Q(s,t)=0. This establishes invariance and reversibility of the finite chain. No nonempty configuration jumps to the empty one, so conditioning on nonemptiness preserves all balance identities and invariance.

For completeness the passage to infinite volume can be justified directly using the graphical construction. Put independent Poisson jump and birth arrows of rates 1/(2d) and beta/(2d) on directed lattice edges. The occupation at a finite collection A of sites up to time t depends only on a finite backwards arrow ancestry almost surely. To see finiteness, a backwards dependence reaching distance at least R contains an ordered nearest-neighbor arrow path of length at least R. For each step one must allow both orientations of the edge: their combined arrow rate is (1+beta)/d. A path of length n has expected number of time-ordered realizations at most ((1+beta)t/d)^n/n!; there are at most |A|(2d)^n paths. Loops are allowed in this upper bound; ordered distinct times are counted using Poisson factorial moments even when an edge repeats. Hence the probability of reaching distance R is at most |A| sum_{n>=R}(2(1+beta)t)^n/n!, which tends to zero. Local updates can add a dependency only across such an arrow. This also constructs the infinite system by stabilization of finite neighborhoods.

Couple a large periodic box and the lattice with identical initial Bernoulli variables and arrows on a neighborhood of A. For a fixed finite time interval their observations agree unless the backwards dependency reaches that box's boundary; the preceding bound tends to zero. The stationary product distributions of finite tori therefore imply stationarity on the lattice. The same coupling applied to any finite list of local observations transfers finite-chain time reversal symmetry and proves reversibility. For general a, replace 1+beta by a+beta and the reverse coalescence rate by a/k. QED.

The source's statement that no simple formula is apparent should not be inherited as an obstruction for this precise equal-kernel model. It can apply to variants; it does not invalidate the balance proof. This proposition alone contains no independence assertion about genealogy events.

## Proposition 2: isolated reunion probability and its tail

Let X and Y be independent rate-one simple walks on Z^d, starting at 0 and a nearest neighbor e. Put tau=inf{t>=0:X_t=Y_t}. Let G(z,0)=sum_{n>=0} P_z(S_n=0) for the discrete-time simple walk. For d>=3,

q=P(tau=infinity)=1-G(e,0)/G(0,0)=1/G(0,0)>0.

Also, with q_L=P(tau>L), for L>=1,

0<=q_L-q<=C_d L^{1-d/2}.

Proof. Z=Y-X has nearest-neighbor steps uniform over 2d directions and total jump rate 2. Its embedded chain is S. The discrete walk has finite Green function in d>=3, as also follows from the continuous-time heat-kernel bound below. If H is its first hitting time of 0 from e, the strong Markov property and Tonelli give G(e,0)=P_e(H<infinity) G(0,0). The first-step decomposition at 0 gives G(0,0)=1+(1/(2d))sum_{z~0}G(z,0)=1+G(e,0), using coordinate and sign symmetries. These two identities yield q=1/G(0,0). Finiteness and G(0,0)>=1 imply q>0.

Here is a direct tail estimate, including the needed heat-kernel justification. The characteristic exponent of the rate-two walk is (2/d)sum_j(1-cos(theta_j)). Fourier inversion bounds every k_t(z,0) in absolute value by

(2pi)^(-d) integral_{[-pi,pi]^d} exp(-(2t/d)sum_j(1-cos(theta_j))) dtheta.

On [-pi,pi], 1-cos(theta)>=2theta^2/pi^2: this follows from 1-cos(theta)=2sin^2(theta/2) and the concavity bound sin(u)>=2u/pi for u in [0,pi/2]. Extending the resulting Gaussian integral to R^d gives k_t(z,0)<=C_d t^{-d/2} for t>=1. For smaller t use k_t<=1; thus k_t<=C'_d(1+t)^(-d/2). The continuous expected occupation time of 0 equals G(z,0)/2, because each embedded visit has independent mean holding time 1/2; the bound proves finiteness for d>=3.

On {L<tau<infinity}, the holding interval immediately after tau contributes mean 1/2 to integral_L^infinity 1_{Z_t=0}dt, by the strong Markov property. Therefore

P(L<tau<infinity)<=2 integral_L^infinity k_t(e,0)dt<=C_d L^{1-d/2}.

Hitting times have no atom at a fixed positive L, since jumps occur at continuous random times. The left side is q_L-q. QED.

Boundary check: in dimensions 1 and 2 the embedded walk is recurrent and q=0. Thus thinning by a positive isolated escape probability is unavailable there. This confirms why transience enters this method, rather than proving failure of any differently scaled recurrent limit.

## Proposition 3: a first-event theorem for an actual finite family

Start the concrete CBRW from one particle, without equilibrium background. Choose L=L(beta) with L->infinity and beta L->0. Define a precise first-event statistic T_beta^L as follows. While there is one particle, wait for its next birth. Follow the resulting pair until its reunion or until L time units after that birth, whichever occurs first. If any additional birth occurs before that resolution, return the cemetery value infinity. If the pair reunites before L, repeat from the singleton. If the pair survives to age L with no further birth, return the time of that birth, and stop. Then

beta q T_beta^L => Exponential(1) as beta->0.

The recognition time, T_beta^L+L on a non-cemetery outcome, has the same limit. In an auxiliary isolated-walk continuation of the accepted pair, the probability it reunites after age L is (q_L-q)/q_L ->0. This last statement concerns the auxiliary unbranched pair, not descendants in the full CBRW.

Proof. Construct an auxiliary stopped process identical to CBRW except that all births are suppressed during pair resolution windows. The single particle waits E_i~Exp(beta) before trial i. During each trial its two independent walks reunite after a time tau_i with the law of Proposition 2. Translation invariance, the strong Markov property at reunion, and independent future walk/birth increments make these trial data iid, with E_i independent of all tau_j. This independence can also be implemented by sampling independent copies of the trial walks and concatenating them at reunions; it does not assert independence of a survival mark from the parent walk inside its own window.

Let K=min{i:tau_i>L}. Then K is geometric on {1,2,...}, with parameter q_L. The accepted birth time in the auxiliary process is

S_beta = sum_{i=1}^K E_i + D_beta,
where D_beta=sum_{i<K}tau_i and 0<=D_beta<=L(K-1).

For W_beta=sum_{i=1}^K E_i and s>=0, summing the geometric series gives

E exp(-s W_beta)=q_L beta/(s+beta q_L).

Thus W_beta is exactly exponential of rate beta q_L. In particular beta q W_beta tends to Exp(1), since q_L->q. Also

E[beta q D_beta]<=beta q L (1-q_L)/q_L<=beta L,

where q<=q_L. Consequently beta q D_beta tends to zero in probability by Markov's inequality, and beta q S_beta=>Exp(1). Recognition adds deterministic beta q L->0.

To couple the actual and auxiliary stopped processes, retain all the suppressed birth clocks as extra marks. Conditional on the auxiliary walk data, extra births form Poisson clocks of total rate at most 2beta throughout every pair window (there are at most two particles until disagreement). The total length of windows up to and including the accepted window is at most LK. The union bound 1-exp(-x)<=x, conditioning on the auxiliary data, gives

P(coupling fails)<=2beta E[LK]=2beta L/q_L<=2beta L/q.

If there is no extra mark the two stopped processes have identical paths and return the same accepted birth time. Hence their laws differ in total variation by at most that failure probability, including the cemetery outcome. This proves the stated convergence for the actual statistic. Conditional on an auxiliary success tau>L, late reunion probability is exactly P(L<tau<infinity)/P(tau>L)=(q_L-q)/q_L; apply Proposition 2. QED.

For d=3 one may take L=beta^(-2/3). Both beta L and the late-reunion upper bound then are O(beta^(1/3)). This is a rigorous local justification for the clock beta q, not a stationary genealogical limit and not a Poisson process theorem for successive stationary events.

## Proposition 4: constrained-Ising local motif and scale separation

Use exactly the per-directed-edge rates on slide 16: if x is occupied, its neighbor y becomes occupied at rate p if vacant and becomes vacant at rate 1-p if occupied. On Z^d the occupied-neighbor count n_y is unchanged by flipping y. Product Bernoulli(p) is reversible: for fixed neighboring configuration, the weights of y=0 and y=1 are in ratio (1-p):p, and their rates are n_y p and n_y(1-p), so their probability fluxes agree. The graphical finite-volume-to-infinite-volume argument of Proposition 1 applies with bounded rates and proves invariance on Z^d. Finite nonempty conditioning is valid since the last particle cannot be deleted.

Starting from a single occupied site, the first creation rate is 2dp. Once the first adjacent pair has formed, it has two deletion arrows of rate 1-p each, and 4d-2 creation arrows of rate p to vacant neighbors. The next effective configuration change deletes one of the pair with probability

2(1-p)/[2(1-p)+(4d-2)p],

and conditional on deletion either endpoint survives with probability 1/2. These formulas follow by competing exponential clocks; null clocks need not be counted. Therefore an isolated creation/deletion cycle moves to a particular chosen neighbor with probability 1/(2d) times 1/2+O(p). Its long waiting time has mean 1/(2dp); the resolution time has bounded mean. This identifies the leading jump rate p/2 per oriented edge (total dp), in agreement with the slides, only for these isolated cycles.

There is also an exactly computable two-creation motif: from singleton create an adjacent pair; before a deletion create a third site; then delete the central site of the three-site path before any other change. Z^d is triangle-free, so every third site created from an adjacent pair makes a path of length two. Its occupied-neighbor degrees are 1,2,1. Thus the total deletion rate is 4(1-p), the central deletion rate is 2(1-p), and the total creation rate to vacant sites, counted by arrows, is (6d-4)p. The probability of this motif after the first birth is exactly

M_d(p) = [(4d-2)p / (2(1-p)+(4d-2)p)]
         [2(1-p) / (4(1-p)+(6d-4)p)]
       ~ ((2d-1)/2) p.

The rate of first-birth attempts from a singleton multiplied by this motif probability is 2dp M_d(p)~d(2d-1)p^2. This is an instantaneous attempt-rate calculation, not the intensity of lasting splits in equilibrium. The two remaining sites are nonadjacent; they can still reunite later. Four-site excursions and encounters with unrelated particles are not covered. QED.

## Checks and hostile-referee audit

### Proposition 5: a Palm incidence warning (unpruned events only)

In the product equilibrium of Proposition 1, condition on occupancy at the origin. The instantaneous rate of a non-null birth from that particle is beta(1-p)=p. The rate of a merge involving that particle is 2p: its own jump hits an occupied neighbor at mean rate p, and jumps from occupied neighbors onto it have total mean rate p. Each neighbor is occupied independently with probability p under this Palm law. These rates follow by summing the directed clocks; simultaneous events have probability o(dt), and all rates in the finite neighborhood are bounded. This proves the asserted instantaneous hazards.

Equivalently, per unit volume, births have rate beta p(1-p)=p^2 and coalescence events have rate p^2, but a coalescence has two incoming particle incidences whereas a birth has one. Equal event intensities must not be read as equal hazards for a typical incoming particle. This is not a counterexample to Problem A: these are raw events, the pruning and reference-spine convention are not fixed in the source, and passage from incidence rates to limiting point-process laws requires more work. It is an additional concrete test any precise version of the conjecture must pass.

Exact finite checks: checks.py enumerates all directed transition rates on the four-cycle (16 configurations) and three-dimensional cube (256 configurations), for beta=1/7,1,3. It verifies every nonzero configuration-transition detailed-balance identity with Fraction arithmetic for both models. Results are in checks.json. This includes the empty-state boundary, singleton jumps, birth suppression on occupied targets, and coalescing jumps. These are checks of the local proof, not simulations of the proposed limit.

Numerical checks: checks.py integrates the rate-one return kernel [i0e(t/3)]^3 over t>=0, obtaining G(0,0) about 1.516386059 and q about 0.659462670. Quadrature is not a certified enclosure. It simulates the auxiliary renewal experiment of Proposition 3 for four beta values with 3000 trials each, seed 21220261011. The finite-L acceptance probabilities exceed q, as they must; the rescaled means and distribution values are compatible with the limit. These experiments contain no background particles and supply no evidence for independent stationary merge clocks.

Formal algebra: LocalBalance.lean contains proposed proofs of the local birth/coalescence balance, equal-number jump weights, Ising flip balance, and the Green identity algebra. The command `lake env lean ~/brain_workers/TRIO_1011/op/P0212/LocalBalance.lean` was launched from ~/lean_verify and is waiting for a shared Lean slot as of 2026-10-11 16:09 UTC. None of these lemmas is called Lean-checked while that command remains pending. No analytic or probabilistic part is formalized; the handwritten proofs do not depend on Lean completing.

Potential failures tested or isolated:

- Different birth and walk kernels invalidate Proposition 1's matching-arrow argument. The proof is deliberately restricted to equal symmetric kernels.
- Reversibility of occupation configurations does not define a reversible *marked genealogy*: occupied-target null births, merger orientations, and spine choices require a separate construction.
- Escape marks depend on parent increments during their own trial. Proposition 3 uses regenerative trials, not independent marking of the original Poisson process.
- Other births during a trial are not silently neglected: the coupling failure is explicitly bounded by 2beta L/q_L.
- Survival to L is not survival forever: Proposition 2 bounds the omitted tail.
- q=0 in recurrent dimensions prevents the argument; it is not replaced by division by zero.
- Exact product equilibrium gives no pathwise independence after Palm sampling and conditioning on genealogy exploration.
- The Ising motif does not produce the eventual escape constant and cannot be substituted for a limiting split clock.

## Precise remaining gap

No proof or counterexample to the full stationary two-model Problem A has been obtained. Even in the equal-kernel CBRW, Propositions 1–3 leave the following unproved: under the stationary occupation-Palm law, after a specified pruning rule and on time scale 1/(beta q), every finite rooted exploration of splits and merges converges jointly to Aldous's recursive graph, with rate-one clocks independent across explored lineages and in both time directions, and with negligible identifications between branches already exposed except for their prescribed creation vertices.

One must control encounters with infinitely many initially present families, not just reject extra births in a two-particle trial. On a time interval of order 1/beta, equilibrium-background encounters are order one, and precisely generate the target merges, so simply showing all third-particle interactions vanish would be false. Required estimates must distinguish these fresh-family encounters from multiple contacts with a previously exposed family, account for Palm and exploration conditioning, and prove the point-process/independence assertions. Occupation reversibility and event-count balance alone do not imply them.

For Model 2 one additionally needs a controlled reduction of excursions of facilitated clusters to walk/split/merge events on the p^(-2) scale, including the lasting-split constant, before carrying out the stationary genealogical exploration argument. The exact equilibrium law and three-site motif do not supply that reduction. General transient variants require further assumptions and are not resolved here.

Verdict: PARTIAL. No result is labeled a solution in literature.

The research attempt is closed at the explicit stationary-genealogy gap. The queued optional Lean algebra check is not counted as completed validation; exact rational checks and handwritten proofs stand independently of that command.


## Second attempt, 2026-10-11: stationary free-cloud encounter theorem

Two new approaches and the complete new proofs are in SECOND_ATTEMPT.md. Approach A uses a mobile-target contact-volume law, Kingman's subadditive theorem, and rare-event/Poisson marking; approach B proposes a pruned incidence/mass-transport test but remains a diagnostic rather than a counterexample. The actual remaining-gap words and the named Kingman theorem were queried in the read-only brain, and the external theorem was checked against a downloaded textbook statement.

What is now proved: for a stationary product-Poisson(p) cloud of independent rate-one walks in Z^d, d>=3, first contacts with each of finitely many independent tagged walks converge jointly to independent rate-2/G(0,0) Poisson clocks on time scale 1/p. The conditional contact intensity self-averages almost surely by a fully checked subadditive reduction. A single cloud particle hitting two tags has probability O(sqrt(p)) in d=3, and late returns are O(p^(1/3)) with pruning time L=p^(-2/3). Positive-probability tag-path conditioning includes adjacent siblings conditioned never to reunite. Bernoulli-initial clouds have the same limits, though they are not stationary.

This is a genuine stronger comparison result, not the original two-model solution. The missing transfer is a pathwise approximation for unexposed interacting families under successive genealogy/Palm conditioning. Background branching and coalescence act for times of order 1/beta and cannot be dropped as an o(1) perturbation. Adaptively discovered tags and their two-sided marked histories also require additional estimates. The constrained-Ising effective-cluster reduction and the root/spine normalization remain unresolved. All details and hostile-referee tests are in SECOND_ATTEMPT.md, Lemmas 6,8,9, Theorems 7,10, Corollary 11.

Formal status update: the first attempt's previously queued LocalBalance.lean was rerun with a one-hour timeout and completed with exit code 0. Its four algebraic identities are kernel checked, without sorry or native_decide; log: lean_second.log. No stochastic theorem is claimed formally checked. Exact finite algebra and additional finite-torus free-cloud simulations are in second_checks.py / second_checks.json.

Current verdict remains PARTIAL; no complete proof, counterexample, or exact literature solution to P0212 has been obtained.

Second-attempt verification completed: 768 exact finite subadditivity inequalities and categorical checks passed; all four finite-torus simulation batches finished. Detailed limitations and the retained 2.1-standard-error deviation are in SECOND_ATTEMPT.md. Second attempt closed STATE: DONE, VERDICT: PARTIAL.
