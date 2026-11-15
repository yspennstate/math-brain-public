PARTIAL

# F0126: reconstruction, support, and the equivalence group

The general color-only reconstruction question was **not resolved in the literature located in this search**, and no proof resolving it modulo all natural walk symmetries is given here. Two precise negative statements are proved below:

1. Without the survey's irreducibility assumption, reconstruction of the full scenery fails with probability one, even modulo any countable family of spatial equivalences.
2. Even with irreducibility, a recurrent walk on Z² can have a non-Euclidean symmetry. For an explicit four-step walk and any nonconstant finite i.i.d. scenery law, no reconstruction rule modulo Euclidean lattice isometries has success probability greater than 1/2.

The second statement is a counterexample to the literal restriction to ordinary translations/reflections, even when “reflections” is enlarged to generate every Euclidean lattice isometry. It is **not** a counterexample when “natural equivalences” includes all symmetries of the walk kernel. This distinction is why the report is marked PARTIAL rather than treating the intended open question as settled.

## The source and the actual gap

The source is F. den Hollander and J. E. Steif, *Random walk in random scenery: A survey of some recent results*, IMS Lecture Notes–Monograph Series 48 (2006), 53–65, DOI 10.1214/074921706000000077. The full extracted text is in `sources/survey_2006.txt`; [arXiv source](https://arxiv.org/abs/math/0608219).

Section 1 assumes that the increment support generates all of Z^d as a semigroup. Section 3, printed pp. 61–62 / PDF pp. 9–10, asks for one measurable map A from the one-sided color record to a scenery, with P(A(Y) equivalent to C)=1 under the independent walk/scenery law. In one dimension, equivalence is C'(x)=C(a+epsilon*x), with integer a and epsilon=±1. Section 4, question 7, printed p. 63 / PDF p. 11, asks about arbitrary recurrent i.i.d. increments and arbitrary i.i.d. scenery.

For two fixed known sceneries c,c', distinction instead asks for a test separating their observation laws almost surely. Those laws must be mutually singular; merely being unequal is insufficient. Tests can depend on both candidate sceneries. Almost-every-pair distinction therefore does not establish a single reconstruction map. A family of exceptional indistinguishable deterministic sceneries does not establish failure for typical i.i.d. scenery.

There is a significant correction to the premise: the survey's Theorem 3.3 prints F **strictly containing** {-1,0,1}, not a subset. Its cited reports address binary reconstruction with bounded jumps. In particular, symmetric uniform {-2,-1,0,1,2} increments with fair binary scenery should not be presented as a new class.

The wider literature audit, including exact checked theorem statements and access limitations, is in [LITERATURE.md](LITERATURE.md). The general question remains unproved in this work after accounting for the following results:

| Setting | Checked literature locator |
|---|---|
| Binary fair scenery, symmetric nearest-neighbor walk, with or without holding | Matzinger, EURANDOM 2000-002, Theorem 1, internal p. 2 / PDF p. 4; published binary simple-walk paper, AAP 15(1B) (2005), 778–819 |
| Uniform scenery; finite-support mean-zero increments of gcd 1; more colors than increment types | Löwe–Matzinger–Merkl, EJP 9 (2004), 436–507, Theorem 1.1, p. 438 / PDF p. 3 |
| Fair binary scenery, symmetric irreducible bounded jumps | Survey Theorem 3.3, p. 62; Lember–Matzinger reports 2002-014 and 2002-042 supply localization and seeded extension. The latter's Theorem 1.1 is on internal p. 5 / PDF p. 6. The published fingerprint theorem is EJP 13 (2008), Theorem 1.1, p. 399 / PDF p. 4, and is not by itself a full reconstruction map. |
| Uniform five-color scenery; symmetric walk close to nearest-neighbor, holding, sufficiently fast exponential tails | Hart–Machado–Matzinger, MPRF 21(4) (2015), 939–970; arXiv 1110.6853, Theorem 1.1, PDF p. 4, conditions (1)–(4) on PDF p. 3 |
| Four-color improvement of the preceding localization/extension method | Matzinger–Pachon Pinzon, ALEA 9 (2012), 85–99: Theorem 1.1, p. 86, and extension discussion in Section 1.1, pp. 87–89 |
| Simple symmetric walk on Z², sufficiently many uniform colors | Löwe–Matzinger, AAP 12(4) (2002), 1322–1347. Earlier EURANDOM version: Theorem 1.1, internal p. 2 / PDF p. 4. |

The exponential-tail result is genuine single-walk reconstruction with unbounded support. Thus bounded jumps are a restriction of some methods, not a necessary condition for reconstruction. Its authors are Hart–Machado–Matzinger, and its published date is 2015. [Publisher record](https://www.math-mprf.org/journal/articles/id1400/).

Matzinger–Rolles' noisy reconstruction result, PTRF 125 (2003), 539–577, uses enough colors and sufficiently small noise. Hart–Matzinger, SPA 116 (2006), 807–829, constructs markers for noisy binary observations; its abstract explicitly does not claim full binary noisy reconstruction. Polynomial finite-piece results are also more restricted than arbitrary increment/scenery laws.

Lindenstrauss, *Indistinguishable Sceneries*, RSA 14(1) (1999), 71–86, gives uncountably many exceptional indistinguishable sceneries; preprint Theorem 2.1 was checked in the web-readable text, but its journal-page correspondence was not obtained. The search did not locate an i.i.d.-typical negative theorem for arbitrary irreducible recurrent walks modulo their full natural symmetries. Popov–Pachon (2011) and Matzinger–Popov–Pachon (2017) use branching observations. Lakrec (Israel J. Math. 248 (2022), 149–200) supplies the walk channel as well as colors. Neither observation model resolves F0126. No general resolution was found in the searches through 2026; that is a search finding, not a completeness guarantee.

## Why markers help, and where the arguments stop

Suppose the walk has bounded increments and maximal positive step L. If two locations at distance kL can be recognized, a crossing between them in exactly k steps must take +L at every step. The colors read are a *ladder word*: C(x),C(x+L),...,C(x+kL). Repeated crossings supply such words. Long overlaps assemble words along each residue class, and further adjacency information arranges the different residue classes. This last operation needs the whole increment support; it is not legitimate to declare every residue class an independent equivalence.

Finite words are not unique markers in an infinite i.i.d. scenery: each positive-probability word appears infinitely often. The proofs identify markers reliably inside growing finite observation/spatial windows, with summable error probabilities, and alternate reconstruction with construction of better localization times. The LMM explanation is on pp. 439–440, and its precise selection/filtering algorithm is in Section 4, pp. 448–450.

Here is a precise elementary estimate behind the color-versus-path-count issue. Let W be a uniform q-color word of length ell, independent of all scenery sites used by candidate paths. For any fixed path, even one revisiting sites, the chance its color record equals W is q^(-ell): condition on the remote scenery and then expose W. With N candidate starting sites and m possible increments, the union bound is

    P(some candidate path reads W) <= N m^(ell-1) q^(-ell).

For q>m this decreases exponentially in ell after controlling N. Independence is essential: the same formula cannot be applied indiscriminately to paths intersecting the sites defining W. The full proof handles overlaps separately. For nonuniform scenery a corresponding crude bound is N m^(ell-1) p_max^ell; this is only a remote-match bound, not a reconstruction theorem.

When there are too few colors, that path-count estimate no longer suppresses false matches. It does not prove impossibility. The binary method instead builds rare signal carriers and estimates the scenery-dependent frequency of a delayed color observation after a carrier visit. Schematically,

    h_t(x) = sum_z P(S_t=z-x) 1{C(z)=1}.

For bounded jumps, h_t(x) depends on a finite neighborhood. Widely separated carriers can have disjoint neighborhoods, producing independent information. Repeated visits allow empirical estimates; separated frequencies and thresholds identify carriers and encode bits. Lember–Matzinger (2008), Sections 1.5–1.6 and 3–5, construct observable proxies from long binary patterns and prove the required separation and error bounds. Treating the unknown visit times as already given would omit the main difficulty.

Unbounded jumps remove a maximal-step crossing certificate and allow the walker to skip a marker or enter its neighborhood from arbitrarily far away. Finite propagation, used to isolate carrier statistics, also fails. Over a time window of T increments, truncation at L has error at most T P(|X|>L); recurrence alone gives no estimate adequate for the existing multiscale constructions. Exponential tails close to nearest-neighbor motion permit weighted path estimates and one-point extension in Hart–Machado–Matzinger; that argument does not cover arbitrary tails or arbitrary binary increment laws. The survey's separate entropy question is also not answered by the elementary union bound.

## Theorem A: an unvisited sublattice prevents full recovery

Let H be a proper subgroup of Z^d, suppose every increment is in H and S_0=0, and let the scenery have a nondegenerate i.i.d. law p on a finite alphabet. Then for every measurable estimator A(Y) and every countable group Gamma of bijections of Z^d,

    P(A(Y) belongs to the Gamma-orbit of C) = 0.

**Proof.** Every S_n is in H. The record is measurable with respect to C restricted to H and the walk. Conditional on these two objects, the colors outside H remain independent with law p. The complement of a proper subgroup of Z^d is infinite: if x is outside H and H is infinite, x+H is an infinite disjoint coset; if H is finite, it is {0} and the complement is infinite.

Put p_max=max_g p(g)<1. Conditional on C|H and the walk, A(Y) is fixed. For a fixed gamma in Gamma, the event A(Y)=C composed with gamma specifies C at every site outside H, because gamma is bijective. Requiring the specified colors at any k distinct such sites has conditional probability at most p_max^k. Letting k increase gives conditional probability zero. A countable union over gamma still has probability zero, and integration proves the claim. An independently randomized estimator has the same property by conditioning on its extra randomness. QED.

For example, P(X=2)=P(X=-2)=1/2 gives a recurrent i.i.d.-increment walk. A change at any odd site leaves the entire observation law unchanged. The theorem gives failure for typical i.i.d. scenery, not just a selected exceptional pair.

This example is excluded by the source's irreducibility assumption. The appropriate restricted problem on H is isomorphic to the problem on Z^r, where r is the rank of H: choose a group isomorphism phi:Z^r→H, let T_n=phi^(-1)(S_n), and D(u)=C(phi(u)). The increments of T remain i.i.d., D remains i.i.d., independence and recurrence are preserved, and D(T_n)=Y_n. Applying an estimator and its inverse coordinate transformation proves equivalence of the two restricted reconstruction problems. It recovers no colors outside H.

Time periodicity alone is different. The simple walk with increments ±1 has period two, yet its all-time reachable set is Z. A recurrent irreducible walk visits every site almost surely: at successive returns to zero, attempt any fixed finite increment sequence reaching the site. That sequence has positive probability; repeated failures have probability tending to zero by the strong Markov property. Countably many sites can be handled simultaneously. No unvisited parity class remains when observations at every time are supplied.

## Theorem B: Euclidean equivalence is insufficient for some irreducible walks

Let the increments be uniform on

    F = {(1,0), (-1,0), (1,1), (-1,-1)}.

Let C be independent nondegenerate finite-alphabet i.i.d. scenery on Z². Let E be the group of all Euclidean lattice isometries x↦Qx+b, where b is integral and Q is a signed permutation matrix. Then every measurable reconstruction rule satisfies

    P(A(Y) is E-equivalent to C) <= 1/2.

In particular, a.s. reconstruction modulo translations and ordinary reflections is impossible for this walk, although it is recurrent, irreducible, and has bounded i.i.d. increments.

**Proof of recurrence and irreducibility.** Let

    B = [[1,1],[0,1]],  R = [[0,-1],[1,0]],
    A = B R B^(-1) = [[1,-2],[1,-1]].

The walk S has the law of B times a simple symmetric walk T on Z². Since B is an integral bijection with determinant one, the support generates Z² and all sites communicate. Its periodicity is two; this does not affect recurrence.

For completeness, write T=(U,V). At each step, the increments of U+V and U-V are independent uniform signs: the four original steps produce all four sign pairs equally. Thus

    P(T_(2n)=0) = [binom(2n,n) / 4^n]^2.

Set b_n=binom(2n,n)/4^n. We have b_1=1/2, and

    b_(n+1)/b_n = (2n+1)/(2n+2) >= sqrt(n/(n+1)),

since squaring and clearing denominators leaves 1>=0. Induction gives b_n>=1/(2 sqrt(n)). Consequently the expected number of visits to zero is at least sum_(n>=1)1/(4n)=infinity. If the return probability were r<1, the strong Markov property would give expected total visits 1/(1-r)<infinity. Hence r=1 and the walk is recurrent. The bijection B preserves returns, so S is recurrent as well.

**Proof of the hidden symmetry.** A sends (1,0) to (1,1), (1,1) to (-1,0), and their negatives accordingly. Therefore AS has the same increment law as S and starts at zero. But

    A^2 = -I,    A^T A = [[2,-3],[-3,5]] != I.

For every deterministic scenery c define c^A(x)=c(A^(-1)x). Coupling S'=AS gives, at every n,

    c^A(S'_n)=c(S_n).

Thus the two rooted infinite observation laws are exactly equal, for every c. This is stronger than failure of mutual singularity.

**Proof that the scenery classes differ almost surely.** We use the following elementary fact. If an affine lattice bijection T is not the identity and C is nondegenerate i.i.d., then P(C=C composed with T)=0. The map T moves infinitely many sites: otherwise its affine displacement would vanish off a finite set and hence everywhere. From the infinitely many moved sites choose successively pairs {x_i,Tx_i} with pairwise disjoint endpoints. This is possible because a finite set of excluded endpoints, and their preimages under a bijection, excludes only finitely many new choices. The equality of colors in each pair has probability rho=sum_g p(g)^2<1; the events for disjoint pairs are independent. Equality at all pairs has probability at most rho^k for each k, hence zero.

If C^A were E-equivalent to C, there would be h(x)=Qx+b with

    C(A^(-1)x)=C(hx) for every x.

Writing x=Au yields C(u)=C(hAu). The affine map hA is not the identity: its being the identity would force A=Q^(-1), contradicting A^T A!=I. The preceding fact gives probability zero for each h. E is countable, so with probability one C^A and C have disjoint E-orbits.

**Proof of the success bound.** The transformation

    (C,S) -> (C^A, AS)

preserves the joint law: A is a spatial permutation, preserves the increment law, and keeps the two objects independent. It leaves Y unchanged. On the full-probability set just proved, one output A(Y) cannot be equivalent to both C and C^A. The two success events therefore have disjoint intersection and equal probabilities. Their probabilities sum to at most one, proving the bound 1/2. Independent estimator randomization can be held fixed in the same coupling. QED.

**Scope.** For the walk above, the full kernel symmetry group contains B D4 B^(-1), including A. If equivalence includes this group, the two sceneries in the proof are equivalent and the obstruction disappears. In fact conjugating any known simple-walk reconstruction algorithm by B produces reconstruction modulo those conjugated symmetries in every scenery class where that algorithm applies. This example diagnoses an insufficient equivalence group; it does not defeat reconstruction up to all natural walk symmetries. There is no analogous extra *linear* lattice symmetry in dimension one, since an invertible integer 1-by-1 matrix is ±1. This observation says nothing about every conceivable nonlinear ambiguity.

## Computation: exact finite laws and a reconstruction experiment

Run from this directory:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 code/experiments.py
```

`code/experiments.py` uses one thread, nice 10, and peaked at 285,736,960 bytes of resident memory on this Mac. The measured run took 5.72 seconds. Source PDFs were fetched into memory and converted directly to text; none were saved. No publication or push was made.

For a fixed reproducible binary scenery, an exact forward recursion sums every hidden path and produces the distribution of Y_0,...,Y_n. The state records the current site and binary observation word. The retained spatial interval contains every possible position up to the final horizon, so there is no spatial truncation error. Independent brute-force enumeration through five increments agrees with the one-dimensional recursion. Probability normalization, monotonicity of finite-record TV, and the coupling bound TV<=P(hit modified site by n) are checked.

| Walk / pair of sceneries | Horizon n | TV distance | Check |
|---|---:|---:|---|
| ±2, flip color at site 1 | 14 | 0 | Modified site is unreachable; equality holds for every horizon |
| Uniform {-2,-1,0,1,2}, flip at site 1 | 14 | 0.3349641413 | Upper bound from hitting site 1: 0.6783699780 |
| Same five increments with probabilities (0.10,0.30,0.25,0.20,0.15), flip at site 1 | 14 | 0.4009555238 | Mean increment zero; hit upper bound 0.6939893679 |
| Theorem B walk, c versus c^A | 12 | 0 | Integer word-by-word counts agree across all 4^12=16,777,216 paths |

These are fixed-scenery finite-record distances. They do not estimate an i.i.d.-averaged law or discard the root observation. Positive TV below one at a finite horizon does not decide singularity at infinite time. Theorem B's equality of infinite laws follows from the coupling proof, not from extrapolating the finite calculation. Local changes of an irreducible scenery are separate from that global symmetry transformation.

The separate audit, `python3 code/audit.py`, also checks the cycle forward likelihood against exact enumeration of all 5^5 increment sequences for three candidate sceneries, checks the return-count formula against a spatial recursion through 20 steps, recomputes the reported success counts, verifies source-text hashes, and checks that the directory contains no PDFs or page images. Its saved result is `data/audit.json`: PASS.

The observation-only estimator enumerates every binary scenery on an 11-site cycle, uses the known asymmetric mean-zero five-step law above, sums over hidden walk paths by a normalized forward algorithm, and returns a maximum-posterior scenery. Uniform i.i.d. scenery is the prior; the hidden walk begins at zero. Its inputs contain no walk positions or seed scenery. Ground truth is used only to generate observations and score the result up to a cyclic translation/reflection.

| Increments observed | Successful MAP reconstructions / 8 trials | Mean posterior probability of the true translation/reflection orbit |
|---:|---:|---:|
| 100 | 0/8 | 0.06916 |
| 500 | 4/8 | 0.40332 |
| 2000 | 8/8 | 0.90055 |

The cycle wraparound changes the mathematical model. This is an implementable likelihood experiment for a candidate increment class, not an algorithm proved to reconstruct a new infinite-lattice class. Eight trials are evidence only. Exact records, estimates, seeds, likelihood summaries, and TV values are in `data/`; `data/experiment_summary.json` summarizes the run.

## What remains unresolved here

No new full reconstruction theorem is established for an irreducible walk on Z or for general recurrence modulo the walk's full symmetry group. The five-step symmetric binary example was already reported in the source, while the asymmetric five-step cycle calculation does not close its infinite-lattice counterpart. No claimed general negative result is inferred from Lindenstrauss's exceptional family, finite-group examples, slow returns, a failed marker bound, or finite numerical TV.

The durable outcome is an audited correction of the starting literature, explicit proofs separating missing spatial support from time periodicity, and an irreducible example showing why the equivalence group must be specified for arbitrary increments in dimension two.

Task: “Open problem F0126.” Received 2026-11-13 09:39 +04 (Asia/Tbilisi).
