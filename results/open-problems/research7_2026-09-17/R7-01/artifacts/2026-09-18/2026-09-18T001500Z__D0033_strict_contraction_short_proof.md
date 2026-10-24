# D0033 — strict-contraction short proof and operator/path reformulation

Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum reasoning was requested, but no authenticated runtime reasoning telemetry or binding model/effort selector is exposed.

Target: Richard C. Bradley, *Basic Properties of Strong Mixing Conditions. A Survey and Some Open Questions*, *Probability Surveys* 2 (2005), Question 5 in Section 3: if a Markov chain is phi-mixing, must it be rho-star-mixing?

This note is additive to the existing D0033 package. It gives a shorter source-level candidate proof that uses only a robust one-edge estimate, Peyre's N-against-M tensorization, and Bradley's own Theorem 3.3(6). It deliberately avoids the later SDPI sharpening and avoids proving a quantitative rho-star limit directly.

## 1. Scope correction from the primary source

The admission/claim metadata described a strictly stationary scope. The primary source is broader. Immediately before Theorem 3.3, Bradley states that in the rest of Section 3 the state space need not be countable; Theorem 3.3 then begins:

> Suppose X is a (not necessarily stationary) Markov chain.

Question 5 follows immediately after Theorem 3.3 and asks about "a given Markov chain" without reinstating stationarity. Thus the source-safe target for this note is the full not-necessarily-stationary real-state Markov-chain setting of Section 3. The proof below uses no stationarity.

We do not edit the historical claim file in this run; this scope mismatch is recorded for coordinator reconciliation.

## 2. Definitions and two external inputs

Let X=(X_k)_{k in Z} be a (not necessarily stationary) real-state Markov chain. Let

phi(n)=sup_j phi(F_{-infty}^j,F_{j+n}^{infty}).

For disjoint nonempty S,T subset Z with dist(S,T)>=n, write

rho(S,T)=rho(sigma(X_s:s in S),sigma(X_t:t in T)),

and let rho-star(n) be the supremum over such interlacings.

We use two published inputs only.

1. Bradley's standard comparison for two sigma-fields A,B:

   rho(A,B) <= 2 sqrt(phi(A,B) phi(B,A)) <= 2 sqrt(phi(A,B)).

2. Bradley Theorem 3.3(6), explicitly for a not-necessarily-stationary Markov chain:

   if rho-star(n0)<1 for some n0>=1, then rho-star(n)->0 at least exponentially fast.

The tensorization input is Remi Peyre, *Tensorizing maximal correlations*, arXiv:1004.1602v2 (2010), Theorem 3.3.1 with the minimal-hypothesis formulation in Section 3.4(a): it is enough to bound the subjective correlation of U_i,V_j after conditioning on the separate earlier U- and V-prefixes.

## 3. B1 — change category: a robust local channel coefficient

For s<t let K_{s,t}(x,.) be a regular Markov transition kernel from X_s to X_t, and let mu_s,mu_t be the one-time laws. Define the robust local HGR coefficient

kappa(s,t)=sup_lambda rho(U,V),

where U~lambda, V|U=x~K_{s,t}(x,.), and lambda ranges over probability laws supported on a common full-mu_s row-good set defined below. Put

kappa(n)=sup_{t-s>=n} kappa(s,t).

This changes the problem from event mixing to an L2 channel-contraction statement. The only fact needed is that phi controls kappa uniformly over the input law.

### Lemma 3.1 — row-to-marginal control

For every s<t there is a Borel set A_{s,t} with mu_s(A_{s,t})=1 such that for all x in A_{s,t},

||K_{s,t}(x,.)-mu_t||_TV <= phi(t-s).

Consequently, for x,x' in A_{s,t},

||K_{s,t}(x,.)-K_{s,t}(x',.)||_TV <= 2 phi(t-s).

#### Proof

Fix a Borel B and put h_B(x)=K_{s,t}(x,B)-mu_t(B). For every Borel D with mu_s(D)>0, the event {X_s in D} is in F_{-infty}^s and {X_t in B} is in F_t^infty. Hence

| mu_s(D)^(-1) int_D h_B dmu_s | <= phi(t-s).

If h_B exceeded phi(t-s)+epsilon on a positive-mass set, choosing that set for D would contradict the inequality; the same applies to -h_B. Thus |h_B|<=phi(t-s) mu_s-a.e. for each fixed B.

Take a countable algebra generating the Borel sigma-field of R, intersect the corresponding full-measure sets, and then use a monotone-class argument in B. This gives one full-measure A_{s,t} on which the displayed total-variation bound holds simultaneously for all B. The row-diameter estimate is the triangle inequality. QED.

### Lemma 3.2 — robust local HGR bound

For every input probability lambda supported on A_{s,t}, if U~lambda and V|U=x~K_{s,t}(x,.), then

rho(U,V) <= min{1, 2 sqrt(2 phi(t-s))}.

In particular,

kappa(n) <= min{1, 2 sqrt(2 phi(n))}.

#### Proof

Let C be an event measurable with respect to U, with positive probability. The law of V conditional on C is one convex mixture of the rows K_{s,t}(x,.); the unconditional law of V is another convex mixture of the same rows. Because every two row laws on A_{s,t} are within 2 phi(t-s) in total variation, any two convex mixtures are also within 2 phi(t-s). Therefore

phi(sigma(U),sigma(V)) <= 2 phi(t-s).

Bradley's two-sigma-field comparison yields

rho(U,V) <= 2 sqrt(2 phi(t-s)).

Cap by 1. Since phi is nonincreasing in the lag, the bound for kappa(n) follows. QED.

### Version-safe conditioning consequence

If G is any sigma-field generated by coordinates no later than time s, then a regular conditional input law lambda_omega=Law(X_s|G)(omega) is supported on A_{s,t} for almost every omega, because P(X_s notin A_{s,t})=0. The Markov property leaves K_{s,t} unchanged under such past conditioning. Thus the bound in Lemma 3.2 is valid under every prefix conditioning that arises at an adjacent block boundary.

## 4. B21 — import the one-dimensional Dobrushin/d-separation picture

Fix finite disjoint S,T with dist(S,T)>=n. Order S union T chronologically and merge consecutive selected times of the same color into maximal monochromatic blocks. The resulting blocks B_1<...<B_m form an alternating path. Enumerate S-block vectors as U_1,...,U_I and T-block vectors as V_1,...,V_J.

For Peyre's minimal hypotheses define

H_{ij}=sigma(U_{i'}:i'<i, V_{j'}:j'<j).

### Lemma 4.1 — the prefix interdependence graph is exactly the block path

For every i,j,

{U_i:V_j}_{H_{ij}} <= kappa(n)

if U_i and V_j are adjacent in the full chronological block path, and the subjective maximal correlation is exactly 0 if they are nonadjacent.

#### Proof: adjacent case

Assume U_i immediately precedes V_j. Let s be the final time in U_i and t the first time in V_j. Then t-s>=n. Every generator of H_{ij} lies strictly before U_i. Conditional on H_{ij}, the Markov factorization is

U_i -> X_s -> X_t -> V_j.

The transition X_s -> X_t remains K_{s,t}; only the input law of X_s changes, and that conditional law remains on A_{s,t}. Lemma 3.2 and maximal-correlation data processing therefore give subjective correlation at most kappa(n). The opposite chronological orientation is symmetric.

#### Proof: nonadjacent case

Assume U_i lies before V_j and they are not adjacent. The T-block immediately following U_i has T-index <j, so it lies in H_{ij}. Choose r in that intervening block. Conditional on X_r, the entire pre-r path and post-r path are independent by the Markov property.

The remaining generators of H_{ij} split into a pre-r sigma-field C^- and a post-r sigma-field C^+. Side-separated conditioning preserves a product disintegration: if A and B are independent given R, C=c(A,R), and D=d(B,R), then A and B remain independent given (R,C,D). Applying this with the two path sides and R=X_r gives U_i independent of V_j given H_{ij}. Hence the subjective correlation is 0. The reverse chronological orientation is symmetric. QED.

This is exactly the dependency geometry of a one-dimensional Dobrushin interdependence matrix: the only surviving cross-color influences are nearest-neighbor edges of a path. It is also a d-separation statement with no conditioned collider: the conditioned variables split sidewise once an intervening Markov state is fixed.

### Exact finite path norm

Let E_m be the bipartite incidence matrix of the m-vertex path, with every path edge assigned weight a>=0. The symmetric adjacency matrix of the full path is

A_m = [[0,E_m],[E_m^T,0]].

Its spectral radius is the classical path value

2 a cos(pi/(m+1)).

Therefore

||E_m||_{2->2}=2 a cos(pi/(m+1)) < 2a.

If actual edge weights are only bounded by a, entrywise monotonicity for nonnegative matrices gives the same upper bound. As m->infinity, the supremum tends to 2a. Thus the abstract path method has an exact uniform strict-contraction threshold a<1/2. At a=1/2 every finite path has norm <1, but the supremum over arbitrarily long interlacings reaches 1.

This identifies the correct structural meaning of the factor two: it is not an artifact of the crude row estimate. It is the limiting spectral radius of the alternating block path.

## 5. B4 — prove the weaker fact that completely closes the source implication

The source asks only whether phi-mixing forces rho-star-mixing. By Bradley Theorem 3.3(6), it is enough to prove the weaker statement that rho-star(n0)<1 at one lag n0.

### Theorem 5.1 — one-lag strict contraction

If, for some n0,

phi(n0) < 1/32,

then

rho-star(n0) <= 4 sqrt(2 phi(n0)) < 1.

Consequently X is rho-star-mixing, in fact with eventual exponential decay.

#### Proof

Set a=2 sqrt(2 phi(n0)); then a<1/2. For each finite admissible interlacing S,T, Lemma 4.1 gives Peyre's subjective-correlation matrix supported on the alternating path with every nonzero entry at most a. Peyre Theorem 3.3.1 therefore gives

rho(S,T) <= ||E||_{2->2} <= 2a = 4 sqrt(2 phi(n0)) < 1.

The bound is uniform in the number and sizes of blocks. For arbitrary countable S,T, approximate L2 functions measurable with respect to the two generated sigma-fields by conditional expectations onto increasing finite coordinate sets. Covariances and variances converge, so the same uniform bound passes to the full sigma-fields. Taking the supremum gives

rho-star(n0) <= 4 sqrt(2 phi(n0)) < 1.

Bradley Theorem 3.3(6) now gives rho-star(n)->0 at least exponentially. QED.

### Corollary 5.2 — affirmative answer to Bradley Question 5, conditional only on the checked Peyre interface

If X is phi-mixing, then phi(n)->0. Hence there exists n0 with phi(n0)<1/32. Theorem 5.1 applies and yields rho-star-mixing.

No stationarity was used. No asymptotic tensorization estimate is needed beyond one strict lag. No Dobrushin-to-chi-square SDPI theorem is needed. The only post-2005 ingredient is Peyre's tensorization theorem with its 2010 minimal-prefix hypothesis.

## 6. Relation to the stronger quantitative package

The existing D0033 package proves stronger bounds, including a Dobrushin-SDPI route and an arcsine path bound. They are mathematically useful but not needed to answer the source question.

If one imports the already-recorded classical inequality kappa(n)^2<=Delta(n)<=2 phi(n), the same one-lag argument improves the sufficient threshold from phi(n0)<1/32 to phi(n0)<1/8. This sharpening is irrelevant to the yes/no source question and is intentionally not used in the minimal proof above.

## 7. What this run resolves and what it does not

The artifact strengthens the **proof candidate**, not the frozen binary metric, which was already 1. The source-level candidate now has a shorter dependency chain:

1. phi gives a common row-good transition family;
2. every past-conditioned boundary channel has HGR <=2 sqrt(2 phi);
3. the interlacing prefix graph is a path;
4. if phi<1/32 once, Peyre gives rho-star<1 once;
5. Bradley's own Theorem 3.3(6) finishes the asymptotic conclusion.

Still missing under repository closure protocol:

- independent P26 full-proof audit: 0/1;
- distinct OTHER-track full-proof audit: 0/1;
- broader publication-level prior-art adjudication: unresolved.

Therefore the honest repository label remains **PROVED CANDIDATE / protocol closure open**, not CLOSED.

## 8. Dated literature check

Fresh bounded searches on 2026-09-18 used the exact Bradley question, combinations of `phi-mixing`, `rho*`, `interlaced`, and `Markov chain`, plus later Bradley reversible-chain work and Peyre tensorization. They recovered Bradley's 2005 source, Bradley's later reversible Markov-chain papers, Peyre's 2010 tensorization monograph, and special-class/follow-up mixing literature, but no paper explicitly announcing a proof or counterexample to Bradley Question 5 in its full source scope. This is negative evidence only and is not a novelty certificate.

Primary source: https://arxiv.org/abs/math/0511078

Peyre: https://arxiv.org/abs/1004.1602
