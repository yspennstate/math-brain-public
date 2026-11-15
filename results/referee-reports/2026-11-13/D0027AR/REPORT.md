ACCEPT

Theorem A is correct as stated. I found no counterexample or load-bearing gap. It proves Conjecture 2 restricted to every fixed q in (1/2,1), with the survey's genuinely centered gap assumption, for arbitrary correlated and nonstationary initial laws. It also covers a single infection at the origin. Theorem B is correct and belongs to the existing CMST near-equilibrium method. The submission's PARTIAL status is appropriate: neither argument resolves general initial laws for 0<q<=1/2.

The value is a useful localization corollary of BCMRT, rather than a new relaxation mechanism. Mountford–Valle already proves the centered-hypothesis conclusion for q sufficiently close to 1. I did not find Theorem A's exact q>1/2, arbitrary-law, nearest-infection-tail formulation stated in the inspected published works. Being a consequence of published methods and being explicitly stated in print are different claims; the former is verified here, the latter should not be asserted without a reference.

## Errors, gaps, and corrections

There are no required mathematical corrections to claim_files/REPORT.md Sections 3–5. The following qualifications concern its cited input, literature coverage, and numerical interpretation.

1. **A loose exit-event bound in the cited BCMRT proof needs a harmless repair.** Location: BCMRT Section 3.2, PDF p. 8, the passage from fixed-time bad-block probabilities to the event of ever leaving A; indirectly relevant to claim Section 4, line 79. The printed bound with only 2t times a fixed-time bad-event probability does not account adequately for all the clocks in the volume. For a chain X with total jump rate at most |Lambda|, a valid replacement is

   P(there exists u<=h with X_u outside A)
   <= P(X_h outside A) + E[number of jumps from A-complement to A by h]
   <= (1+|Lambda|h) sup_{u<=h} P(X_u outside A).

   The first inequality holds pathwise: a visit to the bad set either persists to h or is followed by an exit from that set. This requires no stationarity. Here |Lambda|=O(h), so the extra polynomial factor is absorbed into the exponential bound. Blondel–Deshayes–Toninelli's reproduction of the argument, Section 3, PDF p. 8 of arXiv:1803.08761, already includes a volume factor. This repairs the input without changing Theorem A or its uniformity. The final union bound in BCMRT Section 5 should likewise be read as a sum over both half-block centers, or a bound using their maximum, rather than assuming identical distributions at those centers.

2. **The exponential-moment parameter must remain fixed when quoting uniform constants.** Location: claim Section 4, lines 79 and 133–141; BCMRT Theorem 2.1, PDF p. 4. The printed BCMRT list of constant dependencies does not display its parameter theta_0. The proof uses a theta between 1 and min(theta_0,q/p), and its rate depends on this choice. The claim correctly fixes both theta and the moment bound K before invoking the theorem. For complete explicitness, choose theta=sqrt(q/p) throughout. No uniformity as theta approaches 1, or as q decreases to 1/2, is established or needed. This is a clarification, not a flaw in (4.3).

3. **The bounded literature search can be supplemented, without changing the verdict.** Location: claim Section 6. Chleboun's September 2026 preprint arXiv:2609.30585 proves linear mixing for oriented update families; it does not apply to FA-1f and does not cite 2510.20461. Recent Shapira and Blondel papers located below concern conservative lattice gases/exclusion. Also, the source survey's own Section 6, especially Theorem 6.2, already gives all-q almost-sure linear growth of the radius and diameter of a finite infection set. That result does not give local equilibration or an exponential relaxation estimate. These should be distinguished when describing the remaining obstruction.

4. **The requested single-seed numerical evidence has a transient and cannot be described by one exponential at all times.** Location: the additional independent experiment in this report, not an error in the submitted proof. The origin probability crosses equilibrium and approaches it from below. A prespecified later window for q=.75 still rejects an exact single-exponential shape. Preserve the signed data and that failure; do not fit log absolute bias across its zero crossing or call a finite-time fit a proof. Details and all fits are below.

## Verification of the proof

References to claim line numbers refer to the supplied, unchanged claim_files/REPORT.md. Its SHA256 is `385c41cb0b69c2cc97bf136e456efe18ce2867ab6e80e9061f191aeff8bc3682`.

**Conjecture and conventions.** I independently downloaded and read the survey, including Conjectures 1–2 on PDF p. 2 and its account of known results. Infection is spin 0, its equilibrium probability is q, and p=1-q. The gap event is exactly {R>ell}. It excludes the fully healthy configuration but permits finitely many infections. There is no translation-invariance, product-law, independence, or infinite-infection condition. Mountford–Valle uses the opposite spin convention. [Survey, arXiv:2510.20461](https://arxiv.org/abs/2510.20461).

**Finite propagation, claim Section 3, lines 57–66.** This is valid, with generous constants. Under common clocks and coins, creating a disagreement at a previously agreeing site requires an earlier neighboring disagreement. Tracing creation times backwards gives a chronological nearest-neighbor path from the initially disagreeing exterior. It uses at least d=r-m rings; the actual boundary distance can require one additional step, which only makes the stated bound looser. There are at most |S|2^n spatial sequences. For each sequence, including sequences returning to an earlier site, Poisson factorial moments give expected ordered ring tuples u^n/n!. Thus the union bound is exactly

    |S| sum_{n>=d} (2u)^n/n!.

Repeated visits do not create an independence error. Infinite backwards paths have probability zero by the same factorial bound. If d>=8eu, each summand is at most (2eu/n)^n<=4^(-n), and the geometric sum is (4/3)|S|4^(-d). Multiplication by 2||f|| gives the expectation comparison used later. This is a graphical comparison, with no attractiveness claim.

**Distance drift, claim Section 4, lines 81–110.** Fix x and write V=theta^(D_x). For d>=1, a closest infection enables a birth at distance d-1 at rate at least q. A change increasing D_x requires that the unique nearest infection heals, at rate at most p. That healing is legal only if it has another infected neighbor; hence the new closest distance is at most d+1. On Z, if there are two nearest infections, healing one does not increase D_x. These observations give

    LV <= theta^d [p(theta-1)+q(theta^(-1)-1)] = -lambda theta^d,
    lambda = (theta-1)(q/theta-p).

For d=0 the upward drift is at most p(theta-1). Therefore

    LV <= -lambda V + b,
    b=q(theta-1)/theta,
    b/lambda=q/(q-p theta)=B.

The sign and rate agree algebraically with BCMRT Proposition 4.1, pp. 10–11. In particular lambda>0 iff 1<theta<q/p. The claim's q>1/2 threshold is correct. At q<=1/2 this particular uniform pointwise drift is unavailable; a configuration with zeros at 1,2 and healthy sites elsewhere realizes the unfavorable inward/outward competition for D_0=1. This says nothing about a critical density of the actual process.

Dynkin–Gronwall in a finite interval with infected boundary gives the slightly stronger bound

    E V(eta_s) <= exp(-lambda s)V(eta_0)+B(1-exp(-lambda s)).

Dropping the last negative term yields (D). The finite-volume initial distance is no larger than the original distance. For fixed M, min(V,M) is a local function. Finite propagation followed by monotone convergence justifies the infinite-volume passage. No equilibrium assumption enters this argument.

**Expanding interval, lines 112–129.** The triangle inequality D_x(eta)<=|x|+R is deterministic; conditioning on R therefore requires no assumption on correlations. With a=log(theta), rho=gamma=lambda/(8a), epsilon<=1/4 and s=(1-epsilon)t,

    -lambda(1-epsilon)t+2a rho t
    =-lambda(3/4-epsilon)t <= -lambda t/2.

Consequently every |x|<=floor(rho t) has E theta^(D_x(eta_s))<=1+B. This is a uniform bound on expectations at all these sites, not an assertion that every block is infected on every realization. Empty regions farther away than this interval are allowed to persist.

**Replacement law and BCMRT uniformity, lines 131–141.** Replacing the exterior of [-r,r] by zeros reduces nearest-infection distances inside; outside, the distance is zero. Thus the replacement law mu_{eta,t} satisfies

    sup_x E_mu theta^(D_x) <= K=1+B.

The law can depend on eta and t. It is generally correlated and is not stationary. BCMRT Theorem 2.1 permits such a law, and its proof gives uniform constants for fixed q, theta, K and support. Here is the dependency check rather than an appeal to the theorem's wording alone:

- In its finite box of length O(h), take blocks with length proportional to delta h. Proposition 3.4 supplies a positive restricted spectral gap and a log-Sobolev constant bounded by a constant times block length.
- The repaired Proposition 3.1 comparison involves equilibrium bad-block probabilities, a path-exit term, and a relaxation term of the form exp[-h/C+C|Lambda|exp(-h/(C M))], where M is maximum block length. Taking delta small makes the coefficient of h negative.
- Split each block into two halves. A block with fewer than two zeros has an empty half; at its center D_x is at least a fixed fraction of the block length, up to integer rounding. Drift bounds its moment at every u in [0,h] by K+B. Markov's inequality and a union bound over centers give at most 2n(K+B)theta^(-c delta h). Independence between blocks is unnecessary.
- The factor (1+|Lambda|h) controlling visits to bad configurations is polynomial. So are any looser block-count factors. They are absorbed by reducing the exponential rate. All initial-law dependence is through theta and K.

This verifies (4.3), including its use for an entire family of replacement laws. Centering f at pi(f) can cost a factor two in its norm; that is absorbed in C_0. [BCMRT, arXiv:1205.4584](https://arxiv.org/abs/1205.4584).

**Returning to the original chain, lines 143–161.** The original and replacement configurations agree inside [-r,r] at deterministic time s. Fresh clocks are independent of the past by the Markov property; the common initial spins need not be independent. For t>=2(m+1)/rho,

    r-m >= rho t/2,
    8eh=8e epsilon t <= rho t/4 <= r-m.

The finite-propagation comparison is therefore valid, and its prefactor is 2(4/3)|S|=8|S|/3 as printed. Enlarging C covers this threshold, h<2 and all other bounded times. The resulting deterministic estimate is uniform on {R<=gamma t}. Integrating it gives the tail term 2||f||nu(R>gamma t), without conditioning the dynamics on a future event. The centered gap hypothesis then gives rate at least min(c,kappa gamma), with integer rounding absorbed into the prefactor. Every constant in the deterministic estimate can depend only on q and S once theta is fixed as a function of q.

**Single infection checked directly.** Let eta have its sole zero at 0. Then R=0 and D_x=|x|, so its initial law fails BCMRT's original uniform hypothesis. Nevertheless, for |x|<=rho t,

    E_eta theta^(D_x(eta_s)) <= exp[-lambda(1-epsilon)t+a rho t]+B
                            <= exp(-5lambda t/8)+B.

This is stronger than the estimate used in the claim. After replacement the same K works, and the short remaining evolution cannot import an exterior difference except with exponentially small probability. It proves |P_t f(eta)-pi(f)|<=C||f||exp(-ct). This argument does not assume a surviving contact process or infinitely many initial infections. The last infection cannot heal while isolated; if one heals legally, another infection remains. There is no finite-seed extinction counterexample.

**Section 5, Theorem B, lines 167–200.** All inequalities check. For the independently equilibrated exterior, the global density h_r is the finite-window density, pi(h_r)=1 and 0<=h_r<=M_r. Hence

    ||h_r-1||_2^2 = pi(h_r^2)-1 <= M_r-1 <= K exp(br).

At r=ceil(16et)+m+1, finite propagation controls the change of initial law. Cauchy–Schwarz and the L2 spectral gap give sqrt(K)exp(br/2-gt)sqrt(Var_pi f). The ceiling contributes a fixed factor only. The claimed exponent g-bv/2 is positive under b<2g/v. Positive infinite-volume spectral gap for all q is an equilibrium statement and is sufficient here because the patched law has this controlled L2 density. [CMST, Theorem 2.1 and proof, pp. 4–5](https://arxiv.org/abs/0810.4237); [CMRT 2008, Theorem 6.3, journal p. 484](https://perso.pages.math.cnrs.fr/users/cyril.roberto/Articles/Cancrini-Martinelli-Roberto-Toninelli-PTRF-08.pdf).

The Markov-law calculation in lines 202–213 is also correct: a length-(2r+1) word has 2r transition factors, giving M_r<=K_0 exp(2dr). Positive transition entries imply exponential spatial mixing, and alpha_1 T_11^(2r) is the exact probability of an all-healthy word. Distinct rows arbitrarily close to pi give actual correlated examples.

These examples add no new class beyond the cited methods. CMST's theorem already allows general initial measures with sufficiently slow exponential growth of window likelihood ratios. The explicit numerical allowance b<2g/(16e) refines the sufficient constants in that method; the old theorem does not optimize or specify its maximal allowance. For q>1/2, every stationary positive two-state Markov example here also satisfies BCMRT's uniform moment condition, since its healthy-word probabilities are geometric. For sufficiently high q, its centered tail is also covered by Mountford–Valle.

Theorem B can include inhomogeneous laws failing BCMRT's condition: start from pi, force healthy blocks of length n at positions 2^(2^n), and leave other spins independent. The number of forced sites inside [-r,r] is o(r), so M_r<=K_b exp(br) for every b>0, while the distance moments at the centers of the forced blocks are unbounded. This was already in the scope of CMST's local-density argument. Thus failure of BCMRT's condition does not establish novelty of Section 5.

The single-infection law is outside this perturbative class. Its one-zero word has density ratio 1/(q p^(2r)), requiring b>=-2log p. The single-site test function gives g<=1-p^2, and consequently 2g/v<-2log p for v=16e. Conversely (B) itself implies the centered gap hypothesis, since nu(all healthy in [-r,r])<=Kp exp[(b+2log p)r] with a negative exponent. Section 5 therefore supplies a valid, much stronger sufficient assumption, not the missing general low-q theorem.

## Independent simulation evidence

I wrote simulate_referee.cpp and validate_referee.py independently; I did not read or reuse claim_files/code. Internal spin 1 in this simulator denotes infection, so the recorded origin indicator is exactly the requested f=1{eta_0=0} in the papers' convention.

The simulator uses exact Gillespie flip rates: each healthy legal site flips at rate q; each infected legal site flips at rate p. Legality is an OR of infected neighbors. Two infected neighbors do not double a site's rate. Omitting proposals that leave the state unchanged is the usual exact thinning of the rate-one proposal construction. The interval is [-512,512], initially healthy except for the infection at 0, with a frozen healthy exterior.

For this particular initial state, a sharper boundary estimate than generic (FP) is available. Reaching site 512 requires ordered infection-coin rings at sites 1,...,512. Their expected number is (qT)^512/512!, regardless of subsequent healing. The two-sided probability of reaching a boundary is at most twice this value. The largest qT among all exploratory and confirmation runs is .55*96=52.8, giving a bound below 5.61e-285. Thus boundary error is negligible. No trajectory hit either boundary.

Exploratory runs used 500,000 paths per q through t=24, then independent one-million-path runs through t=96,80,40 respectively. They revealed the sign changes. Before the final independent runs I fixed the later fitting windows recorded in LOG.md. Each final run has five million independent trajectories, divided into 100 independent batches of 50,000. Pointwise SE uses the Bernoulli count; 2,000 whole-batch bootstrap resamples retain correlation between observations of the same trajectory.

| q | Fixed fit times | OLS slope c in log(abs bias)=log A-ct | 95% batch bootstrap interval | Log R^2 | Exact exponential shape check, approximate p |
|---|---|---:|---|---:|---:|
| .55 | 24,32,40,48,64 | .05438 | [.04821,.06276] | .9974 | .373 |
| .60 | 20,24,32,40,48 | .07167 | [.06367,.08258] | .9866 | .267 |
| .75 | 8,10,12,16,20 | .13578 | [.11241,.16922] | .9579 | .000111 |

The last column is a separate generalized least-squares fit of -A exp(-ct) to signed bias, using the batch covariance matrix, with three residual degrees of freedom. Its fitted rates, respectively .05080,.06564,.10425, need not equal the log-OLS slopes. Covariance is estimated, so these p values are approximate. They are checks of exact shape over the stated finite window, not tests of an asymptotic exponential upper bound.

At q=.55 the absolute bias decreases from .0116164 at t=24 to .0013332 at t=64, with SE about .000223. At q=.6 it decreases from .0094220 at t=20 to .0011978 at t=48, with SE about .000219. At q=.75 it decreases from .0041136 at t=12 to .0010744 at t=20, with SE about .000194. These data support relaxation on exponential-looking later scales. The q=.75 primary window includes the rounded undershoot and does not fit one exact exponential; that outcome is retained. Finite simulation cannot prove the conjecture or distinguish all possible ultimate asymptotics.

All batch counts and seeds, signed summaries, fit diagnostics, and a standalone plot are saved in data/confirm_q*.csv, data/summary.csv, data/fits.json, and [data/referee_decay.svg](data/referee_decay.svg). Exploratory counts are retained separately.

For implementation validation, I constructed the full seven-site generator independently, verified its row sums, detailed balance and pi-stationarity, and compared matrix-exponential expectations to 200,000 simulated paths at each q. Dense numerical-library calls emitted floating-point warnings despite finite outputs, so I checked all expectations again using sparse Poisson uniformization with omitted tail below 1e-30. The methods agree within 6.78e-15; the final validator uses uniformization and emits no warnings. The largest standardized simulation discrepancy over 24 comparisons was 2.4933. Exhaustive nine-site generator checks at six q values and three theta values verify the drift bound, including its unfavorable low-q signs, to residual at most 1.20e-15. A separate smoke run verifies active-site bookkeeping after every flip. Full results are in data/validation.json, with the first calculation retained in data/validation_dense_first.json.

All simulation processes inherited nice 10 and were single threaded; at most three ran concurrently. The three final runs took 206.15,99.97,42.93 wall seconds and performed about 4.02,1.91,.741 billion flips. Simulation arrays are O(1025) integers/bytes; analysis recorded an RSS high-water mark of 133,840,896 bytes (about 128 MiB). Numerical-library thread counts were set to one. No workload approached 4 GB.

To reproduce the principal evidence from this directory:

```sh
clang++ -O3 -std=c++17 simulate_referee.cpp -o simulate_referee
# Run at nice >=10; these are serial commands.
nice -n 10 ./simulate_referee .55 5000000 20261113255 1025 0 100 0 data/confirm_q055.csv 80
nice -n 10 ./simulate_referee .60 5000000 20261113260 1025 0 100 0 data/confirm_q060.csv 48
nice -n 10 ./simulate_referee .75 5000000 20261113275 1025 0 100 0 data/confirm_q075.csv 24
nice -n 10 python3 validate_referee.py
nice -n 10 python3 analyze_referee.py
```

## Literature result and what remains open

The four requested texts were independently downloaded, with PDF bytes held only in memory and piped to pdftotext. Their saved filenames are sources/2510.20461.txt, sources/1205.4584.txt, sources/1609.01364.txt, and sources/0810.4237.txt. sources/manifest.txt records URLs, dates, PDF hashes, text hashes, and page counts. Further primary texts and citation-query responses are also plain text. No downloaded PDF or page image was retained.

| Work and checked location | What is actually available |
|---|---|
| BCMRT, MPRF 19 (2013), 383–406; arXiv:1205.4584v1, Theorem 2.1 p. 4, Sections 3–5 pp. 5–12 | q>1/2, arbitrary initial laws satisfying a uniform exponential nearest-infection moment bound. Its proof gives the uniform input used here. A single seed fails its stated hypothesis. Theorem A's replacement argument is an additional corollary argument, not its theorem statement. |
| Mountford–Valle, J. Theoret. Probab. 32 (2019), 282–302; arXiv:1609.01364v1, Theorem 1.1 p. 2 and Remark 1.2 p. 3 | Single-seed exponential local relaxation, and explicitly the centered exponential distance-tail extension, for q sufficiently close to 1. This already proves a portion of Theorem A's consequence. [Primary text](https://arxiv.org/abs/1609.01364). |
| CMST, J. Stat. Phys. 138 (2010), 1109–1123; arXiv:0810.4237v1, Theorem 2.1 pp. 4–5 | General local-density control near equilibrium at every q with positive spectral gap; arbitrary initial measures. Theorem B is the same finite-propagation/density/spectral-contraction mechanism with explicit sufficient constants. Its stronger East results use orientation. |
| Blondel–Deshayes–Toninelli (2019), arXiv:1803.08761v1, Theorems 2.1–2.2 p. 5, Section 3 pp. 7–9 | Front invariant law and LLN/CLT above a contact-process-related threshold; useful explicit BCMRT-derived relaxation estimates. These statements do not give Theorem A for every q>1/2. [Primary text](https://arxiv.org/abs/1803.08761). |
| Ertul (2022), ALEA 19, 511–536, Theorems 2.1–2.2, journal pp. 513–514 | Finite-interval mixing and cutoff for q above a threshold, not arbitrary-q infinite-line local relaxation. [Journal text](https://alea.impa.br/articles/v19/19-20.pdf). |
| Hartarsky–Fabio Toninelli (2024), arXiv:2212.08437v2, Theorems 3.1 and 3.3 pp. 8–9 | Broad KCM finite-box linear mixing and infinite-volume relaxation from suitable product laws, with equilibrium q sufficiently close to 1. [Primary text](https://arxiv.org/abs/2212.08437). |
| Hartarsky–Cristina Toninelli, Kinetically Constrained Models (2025), Theorems 7.19–7.21 and Conjecture 7.29 | Reviews high-q general results and the outstanding full-ergodic-regime temperature-quench problem; not a missing theorem covering arbitrary-law low-q FA-1f. [Author book text](https://www.normalesup.org/~hartarsky/files/research/publi/KCM_book.pdf). |
| Chleboun (September 2026), arXiv:2609.30585, Theorem 2.4 p. 5 | Linear pre-cutoff for oriented update families throughout their open ergodic regime. FA-1f's two opposite neighbor directions violate its orientation assumption. Its bibliography does not cite 2510.20461. [Primary text](https://arxiv.org/abs/2609.30585). |

I also checked the current [Shapira](https://assafshap.github.io/), [Hartarsky](https://www.normalesup.org/~hartarsky/research.html), and [Blondel](https://perso.lpsm.paris/~blondel/recherche.html) publication lists. Shapira's [arXiv:2608.13208](https://arxiv.org/abs/2608.13208) concerns conservative lattice gases. Blondel and collaborators' [arXiv:2606.15233](https://arxiv.org/abs/2606.15233) concerns freezing in facilitated exclusion. Neither is a result on this FA-1f semigroup. These searches supplied no additional claimed resolution.

For papers citing 2510.20461, OpenAlex independently returned one indexed citing work: Martinelli's 2026 ICM chapter, *Kinetically Constrained Spin Models: A Short Survey*, DOI 10.1137/25M180425X. Its indexed publisher Section 2.2.1 still presents Conjecture 2.11 and says available nonstationary FA-1f results require q above a threshold. Direct publisher download returned HTTP 403, so I do not claim to have inspected the full chapter. Semantic Scholar returned zero citations, illustrating incomplete index coverage. Query responses are saved as sources/openalex_*.txt and sources/semantic_scholar_citations.txt. [Publisher chapter](https://epubs.siam.org/doi/full/10.1137/25M180425X).

No inspected paper states the exact uniform tail estimate (A), and no all-q resolution was found in the bounded searches through 13 November 2026. This is not a certificate of unpublished or unindexed novelty. The justified classification is: Theorem A is a correct, short consequence of BCMRT with a useful weakening of its initial-law hypothesis; its very-high-q consequence overlaps Mountford–Valle explicitly; Section 5 is established CMST-type work.

For ordinary FA-1f on Z, what remains unresolved by these arguments is Conjecture 2 for general laws satisfying only the centered exponential gap tail when 0<q<=1/2. In particular, Section 5 does not settle low-q single-seed relaxation. The corresponding arbitrary-start qualitative convergence in Conjecture 1 also remains outside this proof in that range. The survey's all-q linear radius/diameter growth for finite infections, equilibrium spectral gaps, and all-q results for East-polluted/West/BABP generators do not supply the missing local mixing estimate. At q>1/2, integrating (A) also proves qualitative convergence whenever at least one infection exists almost surely, even without an exponential tail.

Task: “Break it if it is wrong.” Received 2026-11-13 07:36:31 +04 (Asia/Tbilisi).
