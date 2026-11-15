PROVED

# I0012: the critical random comb

For i.i.d. nonnegative heights satisfying P(H_0>t) ~ C t^(-1/3), with any C>0, almost every comb has the infinite collision property for two independent discrete-time simple random walks. In fact, walks started together on the backbone collide on the backbone infinitely often. The proof below combines Lemma 4.9 of the source with a backbone last-collision mass transport. It does not extend the source's uniform second-moment estimate to the endpoint.

This result concerns the source's exact asymptotic assumption. A general regularly varying tail t^(-1/3)L(t) with nonconvergent L is a broader problem; no classification of all such L is claimed here.

## Source and exact model

Umberto De Ambroggio, Jenson Ng, Maximilian Nitzschner, and Carlo Scali, *On the phase transition for the number of collisions on comb graphs*, arXiv:2609.05343v1 [math.PR], submitted Friday 4 September 2026, 16:45:39 UTC. The arXiv listing checked on 13 November 2026 lists only v1, 48 pages, 3 figures. [Listing](https://arxiv.org/abs/2609.05343), [version](https://arxiv.org/abs/2609.05343v1). Page numbers below are printed pages of this version, matching the 48 form-feed pages in sources/2609.05343v1.txt.

On a probability space (Omega,G,P), H=(H_x) indexed by x in Z is i.i.d., takes values in [0,infinity), and satisfies (1.7), p.3:

    lim_{t→infinity} P(H_0>t)/(C t^(-gamma)) = 1,
    C>0, gamma in (0,1].

This specifies an asymptotic class of probability laws, not a particular normalized density or mass function. There is no zeta normalizing constant, minimum height requirement, or nonconstant slowly varying multiplier in (1.7). Real heights are allowed; the actual tooth length is floor(H_x), which has the same tail asymptotic. The constant C need not be one.

The vertices are (x,h) with x in Z and integer 0≤h≤floor(H_x). Unit edges join (x,0) to (x±1,0) and consecutive vertical vertices in each tooth; see (1.1)–(1.2), p.2. The backbone B is {(x,0):x in Z}. Each walk is the non-lazy, synchronous discrete-time simple random walk, choosing a neighbor uniformly at each integer time; transition probability 1/deg(v) across an edge, zero otherwise, by (2.3), p.6. The walks are independent conditional on the same fixed environment. They are not independent after averaging the shared environment.

A collision means X_n=Y_n at the same integer n; crossing an edge in opposite directions is not a collision. Infinite collision property means P^omega_{v,v}(#{n:X_n=Y_n}=infinity)=1 for a common start v; it then holds at every common start. Opposite-parity starting vertices are not included: the graph is bipartite and the walks are non-lazy.

The exact exponent assumption is asymptotic equivalence to a constant times a power. It implies regular variation of index -gamma and log P(H>t)/log t→-gamma. The converse logarithmic definition, and regular variation with arbitrary slowly varying L, are weaker assumptions and should not be substituted into the theorem.

The critical conjecture is: under (1.7) with gamma=1/3, for P-almost every omega the above graph has the infinite collision property. It appears on p.16, immediately AFTER the statement of Theorem 4.1, rather than before that theorem. The quoted location in the question is slightly displaced.

## Proof

Write b_x=(x,0), d_x=deg(b_x), and

    K_n^omega(u,v)=P_u^omega(X_n=v).

Always 2≤d_x≤3. The source instead writes p_n^omega(u,v)=K_n^omega(u,v)/deg(v), its symmetric heat-kernel density; keeping these two notations distinct is essential.

### 1. Infinite expected backbone collisions, quenched

Section 4.1 (p.17) explicitly assumes gamma in (0,1) until Section 4.7. Lemma 4.9, p.30, equation (4.83), is in that range; it does not require gamma>1/3. Its conclusion gives constants 0<c_l<c_u, c_9>0 and b>1, and an almost surely finite N_2(omega), such that for N≥N_2 and

    c_l N^(4/(1+gamma)) ≤ n ≤ c_u N^(4/(1+gamma)),

its killed heat-kernel density from v in the stated enlarged rectangle to w in R_N(N) is at least c_9 n^(-(3-gamma)/4), whenever the time and distance have compatible parity. We only use v=b_0 and w=b_x with |x|≤N, a subset of its allowed vertices. Removing killing increases the kernel.

At gamma=1/3, the time scale is N^3 and the density lower bound is c_9 n^(-2/3). For every sufficiently large integer n choose N to be the nearest integer to (n/a)^(1/3), where a is strictly between c_l and c_u. Rounding changes n/N^3 by o(1), so the interval condition holds eventually. At least N of the integers x in [-N,N] satisfy x≡n (mod 2), the required parity. For each of them,

    K_n^omega(b_0,b_x) = d_x p_n^omega(b_0,b_x)
                        ≥ 2 c_9 n^(-2/3).

Conditional independence of the two walks gives

    Q_n^omega := P^omega_{b_0,b_0}(X_n=Y_n in B)
                = sum_x K_n^omega(b_0,b_x)^2
                ≥ 4 c_9^2 N n^(-4/3) ≥ c/n.

Consequently, for P-almost every environment,

    G_B^omega(0) := sum_{n≥0} sum_x K_n^omega(b_0,b_x)^2 = infinity.       (A)

Only the lower heat-kernel lemma is used here; neither Proposition 4.14 nor Theorem 4.1-(1) is being assumed at the boundary. Equivalently, use disjoint time blocks [c_l N_j^3,c_u N_j^3] with N_j=R^j and R^3>c_u/c_l. Each sufficiently large block contributes a fixed positive constant to (A). This independently checks the borderline exponent and the logarithmic divergence.

### 2. A backbone last-collision criterion

Here is the needed version of a Hutchcroft–Peres type criterion, with proof. It applies to any translation-invariant law of finite tooth profiles with E[d_0^2]<infinity, not only an i.i.d. law.

In a fixed environment let

    q_0^omega(x) = P^omega_{b_x,b_x}(no backbone collision at times n≥1),
    q_fin^omega(x) = P^omega_{b_x,b_x}(only finitely many backbone collisions),
    q_last^omega(x,y) = P^omega_{b_x,b_x}(last backbone collision is at b_y).

Time zero is a backbone collision, so on the finite-collision event there is a unique last one. The Markov property at a deterministic time, followed by summing the disjoint choices of last time, gives exactly

    q_last^omega(x,y) = sum_{n≥0} K_n^omega(b_x,b_y)^2 q_0^omega(y),
    sum_y q_last^omega(x,y) = q_fin^omega(x) ≤ 1.                        (B)

Define the nonnegative, translation-covariant transport on Z×Z

    F^omega(x,y)=d_x^2 q_last^omega(x,y).

Stationarity under every integer shift, followed by Tonelli, gives

    E[sum_y F(0,y)] = sum_y E[F(-y,0)] = E[sum_x F(x,0)].              (C)

The outgoing side is E[d_0^2 q_fin(0)]≤9. Detailed balance in the fixed graph gives

    d_x K_n(b_x,b_0)=d_0 K_n(b_0,b_x),

and hence, after squaring both sides and using (B), the incoming side in (C) is

    E[sum_{n≥0} sum_x d_0^2 K_n(b_0,b_x)^2 q_0(0)].                   (D)

All terms are nonnegative; there is no exchange of conditionally convergent sums. By (A), if q_0(0)>0 on an event of positive environmental probability, the inside sum in (D) is infinity there. This contradicts its expectation being at most 9. Therefore q_0(0)=0 almost surely. Stationarity and countability imply q_0(x)=0 for every integer x simultaneously, almost surely. Equation (B) then gives q_fin(0)=0, and likewise q_fin(x)=0 at every backbone start.

Thus, for almost every fixed environment, two conditionally independent walks from any common backbone start collide on the backbone infinitely often with quenched probability one. This is the quenched conclusion, not merely a positive annealed probability.

Notice the squared degree in F. Weighting this transport by d_x instead would not give (D) in this form. No probability distribution obtained by rooting uniformly among all tooth vertices is used; such a normalization would require a finite mean tooth length, which is absent here.

### 3. Other common starting vertices

All teeth are finite almost surely because their tails tend to zero. The comb is recurrent: the disjoint two-edge horizontal cutsets at distances r=1,2,... each have total unit conductance 2, so the resistance to infinity is at least sum_r 1/2=infinity. For a common start v above the backbone, both walks have positive probability of following the same finite downward path to its base. Thereafter they have infinitely many collisions with probability one. Thus the probability of infinitely many total collisions from (v,v) is positive. Barlow–Peres–Sousi, Proposition 2.1 (p.4 of the saved arXiv text), makes this probability zero or one on a connected recurrent graph. It is therefore one. Countability gives the assertion for all common starts on the same full-measure set of environments.

This completes the proof for every law P(H>t)~C t^(-1/3), C>0.

## Checks and limitations

The proof uses a printed heat-kernel lemma of the source as an input, not an unproved critical second-moment assertion. Its stated range includes 1/3. Its dependencies are environment concentration (Lemma 4.2 and Corollaries 4.3–4.4, pp.17–20), local times and exit times (Proposition 4.6 and Lemma 4.7, pp.21–28), and the lower diagonal and hitting estimates (Lemmas 4.8–4.9, pp.28–31). None of these steps uses 3gamma−1>0; that restriction first enters the collision second-moment estimates on pp.34–36. The numerical exponents in (A) were computed both directly at fixed time and by disjoint blocks. The transport was checked separately using stationarity and detailed balance, with no independence of the environment and future collision probabilities assumed.

The generalized tail t^(-1/3)L(t) is not classified by this proof unless L(t) tends to a positive finite constant. In particular, exponent alone in the logarithmic sense is not the source's hypothesis. A heuristic for arbitrary regular variation is recorded below separately from the proved theorem.

## Literature audit

The primary paper and supporting sources are saved as plain text in sources/. No later printed resolution was found in the searches recorded in sources/literature_search.txt. That is a search result, not a guarantee that every unindexed 2026 manuscript was checked. The result above is a new deduction from the saved sources, not RESOLVED_IN_LITERATURE.



### Theorems in the source

| Result | Printed page | Statement and role |
|---|---:|---|
| Theorem 3.1 | 8 | For the deterministic profile H_x=|x|log^gamma(|x|∨1), gamma>0: infinite collisions for gamma≤2, finite for gamma>2. This gamma is a growth parameter and must not be confused with the random-tail exponent. |
| Theorem 4.1-(1) | 16 | Under (1.7), for P-a.e. environment, infinite collisions for gamma in (1/3,1]. The case gamma=1 uses Lemma 4.15 and the Green-kernel criterion separately, pp.36–37. |
| Theorem 4.1-(2) | 16 | Under (1.7), for P-a.e. environment, finite collisions for gamma in (0,1/3). |
| Theorem 4.16 | 37 | Finite collisions for i.i.d. tooth heights with a lower tail bound C t^(-gamma), gamma in (0,1/3), without the additional upper-tail restriction in Koops [23]. Proof pp.37–40. |
| Corollary 5.2 | 41 | Under (1.7), finite triple collisions for every gamma in (0,1). |
| Theorem 5.3 | 41 | Under (1.7) with gamma=1, finite triple collisions. Proof pp.41–46. |

There is a literal typo in the hypothesis displayed as (4.137), p.37: it prints the lower bound C t^(-gamma) for every t in (0,infinity), which is impossible as t decreases to zero. The consistent tail hypothesis is for sufficiently large t (or C(1+t)^(-gamma) for all t). This does not affect the present proof, which uses (1.7) and Lemma 4.9, not (4.137). The source explicitly says Theorem 4.16 implies Theorem 4.1-(2).

### Method and the endpoint loss

The source's working tools are the symmetric density and killed Green kernel (2.4)–(2.5), pp.6–7, electric-network resistances, and the Green-kernel criterion (2.6), p.7, reproduced from Barlow–Peres–Sousi, Theorem 3.1. The random-environment argument for 1/3<gamma<1 first controls the geometry and the local time at roots of deep teeth; those produce uniform quenched fast-exit and heat-kernel estimates. It then counts backbone collisions in a rectangle of width N and height N^(2/(1+gamma)) up to time T of order N^(4/(1+gamma)). Lemma 4.13, pp.33–34, gives the first moment lower bound N^((3gamma−1)/(1+gamma)); Proposition 4.14, pp.34–36, controls the second moment. Paley–Zygmund and a conditional Borel–Cantelli argument at rectangle exits conclude the proof on p.36. Deep-tooth collisions form correlated clusters, which is why the source restricts this part of its count to the backbone.

At gamma=1/3 two explicit difficulties appear:

1. Equation (4.120), p.35, bounds the small-time-gap contribution by c_17 N^(8delta_4). The next paragraph chooses delta_4>0 to absorb this in N^((3gamma−1)/(1+gamma)). At the endpoint this is N^0, so no positive delta_4 works.
2. The large-time-gap contributions (4.123), p.35, and (4.126), p.36, contain sum_{k≤T} k^(-(5−3gamma)/4). At the endpoint this is sum 1/k, of order log T, whereas the single rectangle time-window first moment is only of order one. Thus the uniform constant lower bound on collision probability in (4.127) does not follow by substituting gamma=1/3.

These are distinct losses. It would be inaccurate to say the only missing step is an unspecified slowly varying multiplier. The source assumes a pure asymptotic power; the actual harmonic loss and small-gap polynomial error can be located. Our proof sums the first moment over many time windows and uses stationarity to replace the missing second-moment argument.

For gamma<1/3, the source adapts Krishnapur–Peres: count collisions in dyadic time-height boxes, upper-bound their expected count, and lower-bound the expected size of a collision cluster after a first meeting. Proposition 4.20, p.39, and the summation (4.152), p.40, make the box-hit probabilities summable. This is a cluster-corrected first-moment argument, not finiteness of the expected *total* collision count. On these recurrent bounded-degree combs that total expectation is infinite even in the finite-collision regime.

### Related sources and what they do, precisely

- **Krishnapur–Peres (2004)**, *Recurrent graphs where two independent random walks collide finitely often*, Electron. Commun. Probab. 9, 72–81; arXiv:math/0406487v2. Theorem 1.1, saved PDF p.2, proves finite collisions for Comb(G) with infinite two-sided teeth when G is an infinite recurrent regular graph. Lemmas 2.1 and 2.2, saved pp.3 and 6, bound the count and post-hit cluster size; the latter mechanism is used by the source in Section 4.8. The observation after Theorem 1.1 explains why infinite expected collisions alone does not imply infinite collisions on an arbitrary recurrent graph. There is no general implication “recurrent implies infinite collisions” available from this paper.
- **Barlow–Peres–Sousi (2012)**, *Collisions of random walks*, Ann. Inst. H. Poincare Probab. Stat. 48(4), 922–946; saved arXiv:1003.3255 text. Proposition 2.1, saved p.4, is the recurrent-graph collision zero–one law. Theorem 3.1, saved p.6, assumes a recurrent graph with an exhaustion B_r and g_{B_r}(x,x)≤C g_{B_r}(o,o) for all x in B_r, and concludes infinite collisions (and infinitely many simultaneous common edge crossings). Its proof uses a second moment; this is the precise Green criterion reproduced on p.7 of the main source. Theorem 1.4, saved p.2, gives the threshold alpha=1 for deterministic power-law teeth. These are page numbers of the saved preprint, not unverified journal-page mappings.
- **Chen–Wei–Zhang (2008)**, *A note on the finite collision property of random walks*, Statist. Probab. Lett. 78(13), 1742–1747. The author preprint saved here states Theorem 1 on p.3 for **continuous-time** walks and f(x)≤|x|^alpha eventually with alpha<1/5. Corollary 2 on that page gives a random-profile consequence with a finite moment of some order beta>5. The journal abstract describes the x^(1/5) bound; the saved author preprint has the strict alpha<1/5 statement. Do not silently change this older continuous-time theorem to the non-lazy discrete-time theorem being proved here. The main source cites it for early comb results on p.2.
- **Xinxing Chen–Dayue Chen (2011)**, *Some sufficient conditions for infinite collisions of simple random walks on a wedge comb*, EJP 16, no.49, 1341–1355; arXiv:1010.5366. Theorem 1.1 is the criterion sum_n 1/(1∨max_{|x|≤n}f(x))=infinity; Theorem 1.3 gives finite collisions for |x|log^beta(|x|∨1), beta>2; Theorem 1.4 gives infinite triple collisions for i.i.d. teeth of finite mean. These are the results invoked as (1.3), (1.4), (1.6), pp.2–3 of the main source. Their finite-mean hypothesis fails at the critical law here. The journal versions of Theorems 1.1 and 1.3 appear on p.1342, and Theorem 1.4 on p.1343. The saved arXiv v1 has different numbering: Theorem 1.1 on p.2, finite-mean Theorem 1.2 on p.3, and finite-collision Theorem 4.1 on p.19; it also defines two-sided teeth. These version differences are not hypotheses of the proof above, which uses the one-sided comb lemma from the main source.
- **Hutchcroft–Peres (2015)**, *Collisions of random walks in reversible random graphs*, ECP 20, no.63; arXiv:1505.02484v1. Theorem 1, saved p.1, gives infinite collisions for recurrent reversible random rooted graphs. The proof on saved p.4 uses last-collision probabilities and mass transport. Theorem 5, saved p.5, treats recurrent reversible networks. The law rooted at a backbone site is not stationary for the full comb walk, which can immediately move above the backbone. The theorem therefore cannot simply be applied to that root law. The backbone transport proved above is the needed variant, justified directly.
- **Ben Arous–Cabezas–Cerny–Royfman (2015)**, *Randomly trapped random walks*, Ann. Probab. 43(5), 2405–2457. The saved author text, Section 3.2, pp.13–14, gives the comb trap model and Theorem 3.5. With no tooth drift (beta=0) and tail parameter alpha<1, the horizontal projection has fractional-kinetics parameter (1+alpha)/2. Its model uses the specific law P(N=n)=Z(alpha)^(-1)n^(-1-alpha), n≥1; that zeta normalization belongs to this supporting example, **not** to (1.7) of the main paper. The main source uses this as trapping/scaling-limit context on pp.1,16–17; it does not infer collisions from a scaling limit.
- **Fontes–Isopi–Newman (2002)**, *Random walks with strongly inhomogeneous rates and singular diffusions: convergence, localization and aging in one dimension*, Ann. Probab. 30(2), 579–604, is reference [18] of the main source. Its FIN diffusion is contrasted on p.17 with transparent traps. No FIN collision theorem is an input here.
- **Xinxing Chen (2016)**, *Gaussian bounds and collisions of variable speed random walks on lattices with power law conductances*, Stochastic Process. Appl. 126(10), 3041–3064; saved arXiv:1507.05297v2. Theorem 1.1, saved p.2, gives heat-kernel bounds in an intrinsic metric. Theorem 1.3, saved p.3, distinguishes recurrence and collision behavior for that continuous-time weighted-lattice model. The conductances there are deterministic power laws, not random teeth or i.i.d. random conductances. It is context reference [9] in the main source, not a direct theorem proving the critical random-comb case. Likewise, it is not valid to transfer a conductance-model collision theorem merely by matching a spectral exponent.
- **Koops (2020)**, bachelor thesis, *Collisions of Independent Random Walks in Infinite Graphs*, is reference [23]. The main source pp.3,37 credits a finite-collision theorem for gamma<1/3 under a lower tail bound and an additional polynomial upper bound. The thesis was not retrieved, so no thesis theorem/page numbers are invented. Theorem 4.16 in the retrieved source covers the needed subcritical case directly.

## Expected counts and simulation

Let B_T count backbone collisions at times 1,...,T, and Z_T all collisions in that interval. At the critical law, almost surely in the environment,

    E^omega B_T = Theta(log T),          E^omega Z_T = Theta(T^(1/3)).   (E)

Here Theta means two-sided bounds up to positive constants for all sufficiently large T, not an exact asymptotic constant. The starting point is b_0.

For the backbone upper bound, take the ambient scale N=2n in Lemmas 4.10–4.12 and Proposition 4.11, pp.31–33, with their small positive delta parameters fixed below 1. Eventually the bounds hold for every n and all reachable backbone vertices (|x|≤n). The density is at most C n^(-2/3) when |x|≤n^(1/3), and at most C |x|^(-2) outside. Multiplying by d_x≤3 and summing squares gives

    Q_n^omega ≤ C [n^(1/3)n^(-4/3) + sum_{|x|>n^(1/3)} |x|^(-4)] ≤ C'/n.

The lower bound was proved in (A), including parity. Summing proves the first part of (E).

For all vertices, reversibility and Chapman–Kolmogorov give the exact identity

    p_{2n}^omega(b_0,b_0) = sum_v deg(v) p_n^omega(b_0,v)^2.

Since 1≤deg(v)≤3,

    p_{2n}^omega(b_0,b_0) ≤ P^omega(X_n=Y_n)
                          ≤ 3 p_{2n}^omega(b_0,b_0).

Lemmas 4.8 and 4.10 give p_{2n}^omega(b_0,b_0)=Theta(n^(-2/3)). Their use at even time avoids the zero odd-time diagonal of a non-lazy bipartite walk. Summing proves the second part of (E). In particular, the much larger total expectation is not the mechanism used in the mass transport.

For nearby gamma in (0,1), the same calculation gives

    Q_n^omega = Theta(n^(-(5−3gamma)/4)),
    E^omega Z_T = Theta(T^((1+gamma)/4)).

The backbone sum converges when gamma<1/3, is Theta(log T) at equality, and is Theta(T^((3gamma−1)/4)) when gamma>1/3. The total expectation still diverges below the transition; this agrees with, rather than contradicts, the finite-collision theorem there.

The simulations use gamma=0.28, 1/3, 0.40; 32 independent combs per gamma; 8 independent walk pairs conditional on each comb; T=2^17=131072; snapshots at powers of two. This is 100663296 single-walk steps (50331648 pair steps). All runs are sequential, at inherited nice 10. Only encountered teeth are stored. Memory use is far below 4 GB by construction; trajectories are not stored.

The sampled law is H=floor(U^(-1/gamma)), U uniform on (0,1), so P(H≥k)=k^(-gamma) for integer k≥1 and P(H>t)=(floor(t)+1)^(-gamma) for t≥0. Thus C=1, with no additional slowly varying factor. Very large sampled teeth are represented by H∧(T+1). A walk starting at height zero cannot reach height T+1 by time T, so this representation changes no transition used in the experiment; it is not a reached reflecting cutoff. Environment random numbers and the two trajectory random streams are separate. Pairs in one environment share that environment, as required. Time zero is excluded from the reported counts.

At T=131072:

| gamma | Mean all collisions | Mean backbone collisions | Median all collisions |
|---|---:|---:|---:|
| 0.28 | 45.844 ± 6.204 | 5.012 ± 0.378 | 13.5 |
| 1/3 | 43.609 ± 4.338 | 6.859 ± 0.479 | 20 |
| 0.40 | 51.711 ± 5.297 | 8.422 ± 0.746 | 24 |

The uncertainty is one standard error across the 32 environment means, after averaging the 8 pairs in each environment. It accounts for shared-environment clustering. Medians are over pairs. The wide gap between all-collision means and medians reflects occasional collision clusters. These finite runs cannot distinguish a finite limiting backbone count from very slow divergence close to 1/3.

[Growth plot](data/collision_growth.png) uses logarithmic time and count axes. Dashed lines show the theoretical count shapes, with their amplitudes aligned at the final observed means; this is a shape comparison, not a fitted asymptotic constant. At the boundary the backbone curve grows much more slowly than the total curve, as (E) predicts. Nearby exponents differ too little for a short Monte Carlo run to identify the phase boundary. The simulation is evidence only; the proof above does not use it.

Validation is saved in data/validation.txt. An independent probability propagation on a varied finite-height profile computed expected collision counts through time 12; 50000 simulated pairs using the same step function differed by -0.473 and -0.232 standard errors for all and backbone counts. The validation checks heights and parity at every step. A separate finite-matrix calculation with varying backbone degrees checked detailed balance and the squared-degree transport identity through time 12; maximum residual 8.88e-16. These checks test the code and algebra, not the infinite-time theorem.

Reproduce with a parent process at nice≥10, setting library thread counts to one:

    clang++ -O2 -std=c++17 code/simulate.cpp -o code/simulate
    ./code/simulate 32 8 17
    clang++ -O2 -std=c++17 code/validate.cpp -o code/validate
    ./code/validate > data/validation.txt
    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 code/analyze.py

### What an arbitrary slowly varying factor would change

Within (1.7), L(t) must tend to C in (0,infinity); the proved answer is infinite collisions for every such C, including lower-order deviations from that limit. Thus there is no unresolved choice of normalization or slowly varying part in the exact conjecture proved here.

For the broader class P(H>t)=t^(-1/3)L(t), with general slowly varying L, there is a natural candidate backbone criterion, but it is not proved here. The excursion-clock heuristic gives a horizontal scale

    a(t) ≈ t^(1/3)/sqrt(L(sqrt(t))),

a backbone probability at a specified typical site of order

    t^(-2/3)/sqrt(L(sqrt(t))),

and hence a simultaneous backbone-collision probability of order

    1/[t L(sqrt(t))^(3/2)].

This suggests the integral integral_1^infinity dt/[t L(sqrt(t))^(3/2)] for backbone recurrence. For L(t)=(log t)^beta, that integral diverges exactly for beta≤2/3. These scaling assertions for nonconstant L require heat-kernel estimates not supplied by the source under that hypothesis. They are a heuristic, not a proved criterion, counterexample, or assertion about *total* collisions. Even a proof of finiteness of expected backbone collisions would not alone prove finite total collisions. The present report therefore does not claim that exponent alone, interpreted only as a logarithmic tail limit, determines the answer.

Task: “Open problem I0012.” — 13 November 2026, 14:26 +04 (launch clock).
