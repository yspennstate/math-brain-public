# I0022 — research record, 2026-10-11

## Exact question and verified literature boundary

Janson (2012), Problem 20.11, Section 20.4, printed p. 136:
“Is there some kind of similar limiting object in the case ν < 1 (after suitable scaling)?”
The preceding paragraph discusses the compact continuum random tree and stable trees. The question specifies neither a topology nor a nondegeneracy condition. It applies to simply generated trees with general weights, not just regularly varying weights.

Igor Kortchemski, *Limit theorems for conditioned non-generic Galton–Watson trees*, Annales de l’Institut Henri Poincaré, Probabilités et Statistiques 51(2) (2015), 489–511, DOI 10.1214/13-AIHP580, arXiv:1205.3145v4:
Assumption (Hθ) is 0 < m = sum j μ_j < 1 and μ_j = L(j)/j^(1+θ), θ > 1, L slowly varying. Theorem 4 gives H(T_n) − log(n)/log(1/m) tight. Theorem 5 gives non-tightness of T_n/log(n) in compact Gromov–Hausdorff topology. The paper explicitly calls this a partial answer to Janson Problem 20.11. Theorem 6 gives finite-dimensional limits of unscaled lexicographic heights: (1+e_0+e_1,…,1+e_0+e_k), with independent geometric e_i of parameter 1−m.

This does not settle all weights ν<1, nor rule out limits in other topologies. In particular, “no logarithmic compact GH limit” must not be reported as “no limiting object of any kind”.

## Read-only prior research

Brain recall on subcritical conditioned Galton–Watson condensation and mistakes found warnings about irregular/lacunary tails. Math recall on Kortchemski condensation scaling returned largely irrelevant cards; no claim from those cards is used.

Read origin/master:probability_1000_attempts_I_20260914/Probability_F0064b_Janson_problems_20_3_20_4_20_11_2026-09-14.md in ~/math-open-problems. It treats Problem 20.11 as unresolved beyond regular variation. Its assertion that lacunary laws have no limit “of any of these kinds” is not accompanied there by a proof and is not adopted.

## Later literature: a positive limit under complete condensation

Svante Janson, *Tree limits and limits of random trees*, Combinatorics, Probability and Computing 30(6) (2021), 849–893, DOI 10.1017/S0963548321000055, arXiv:2005.13832. Theorem 10.1 assumes an offspring law of mean m in (0,1), no finite positive exponential moment, and complete condensation

    Δ(T_n)/n → 1−m in probability.

It proves convergence in probability, without changing edge lengths, to the long dendron Υ_Ge(1−m). For r uniformly sampled vertices, its distance array is

    D_ii=0,   D_ij=Y_i+Y_j (i≠j),

where Y_i are independent with P(Y_i=k)=(1−m)m^(k−1), k≥1. A long dendron permits extra arm lengths in addition to a separable base tree; here the base consists of one point. It is a sampling-limit object, not a compact metric tree with the usual GH topology. It records that typical sampled vertices belong to distinct small branches of the same hub. The common ancestral stem above the hub is omitted in this unrooted limit.

Theorem 11.1 proves the analogous sampling limit Υ_1 in the zero-radius case, assuming Δ(T_n)=n−o_p(n). Remark 10.8 explicitly leaves incomplete condensation open; Remark 11.3 also leaves multiple-hub zero-radius limits open. Thus this is a substantial partial answer beyond the local limits, but its extra maximum-degree hypothesis cannot be dropped by citation alone.

A newer boundary result is Igor Kortchemski and Leonard Vetter, *Condensation in subcritical Cauchy Bienaymé trees*, Electronic Communications in Probability 30 (2025), 1–13, DOI 10.1214/25-ECP726, arXiv:2503.07530v2 (8 October 2025). Its local hypothesis is p_n∼L(n)/n² with a slowly varying positive L and mean m<1. Theorem 1.1 gives Δ(T_n)/((1−m)n)→1, second degree o_p(n), geometric hub height, and H(T_n)/log n→1/log(1/m). Centered heights H(T_n)−log n/log(1/m) are tight if and only if Σ(n log n)p_n<∞. Thus Janson 2021 Theorem 10.1 applies to this additional boundary class, giving the same geometric-arm long dendron. The positive mean follows from the eventually positive tail; the no-exponential-moment condition follows from regular variation. This is not a result for arbitrary irregular tails. In particular the asymptotic survival estimate c m^k used in Proposition A must not be extended automatically to the Cauchy boundary: the 2025 paper explicitly warns that it can fail there.

## Precise hypotheses from Janson (2012)

Let w_k≥0, w_0>0, and w_k>0 for some k≥2. A rooted ordered tree t of size n has probability proportional to ∏_{v∈t}w_{d^+(v)}, whenever the normalizing constant is positive. Limits are along admissible n. Put Φ(z)=Σw_k z^k, let ρ be its radius of convergence, and set ν=lim_{t↑ρ}tΦ'(t)/Φ(t), with ν=0 when ρ=0. Problem 20.11 includes both 0<ν<1 and ν=0. When ρ>0 and ν<1, the equivalent offspring distribution is p_k=w_kρ^k/Φ(ρ), with mean ν. With ρ=0 this representation as a conditioned Galton–Watson tree does not exist. The original question adds no regular variation, complete-condensation, finite-variance or topology hypothesis.

## Proposition A: all deterministic compact GH scalings in the regularly varying case

Let p be an offspring distribution satisfying Kortchemski's (Hθ): 0<m=Σk p_k<1, p_k=L(k)/k^(1+θ) for k≥1, θ>1, with L slowly varying and eventually positive. Let T_n be its Galton–Watson tree conditioned to have n vertices and equipped with graph distance (the geometric realization with unit edges has the same conclusions). For any deterministic sequence a_n>0, the laws of a_n T_n are tight in the space of compact metric spaces with Gromov–Hausdorff distance **if and only if** a_n log n→0. In that case a_n T_n converges in probability to the one-point space. Thus no deterministic rescaling has a nontrivial compact GH limit in this special case.

This is a consequence of published results, not a claimed new general solution. The following proof writes out the reduction, including the stronger packing estimate behind Theorem 5.

### Published inputs and where they apply

Let γ=1−m. Write v*_n for the lexicographically first maximum-degree vertex and T_{n,i} for the descendant tree at its ith child. Kortchemski's Theorem 1 gives Δ(T_n)/n→γ. Corollary 2.7, with its parameter equal to 1/2, gives total-variation convergence between the joint law of the first M_n=⌊γn/2⌋ branches and M_n independent unconditioned p-Galton–Watson trees. The event that there are fewer than M_n children has probability tending to zero; it can be assigned any cemetery value. Equation (19) of that paper gives P(H(T)>k)∼c m^k, c>0; (Hθ) ensures E[ξ log ξ]<∞, needed there. Theorem 4 gives H(T_n)/log n→h=1/log(1/m) in probability.

These are invoked as existing theorems with matching hypotheses; they are not asserted to be formally verified here.

### Packing estimate, with complete argument

Set η=1/(2 log(1/m)) and k_n=⌈η log n⌉. In an independent forest of M_n unconditioned trees let N_n count branches of height at least k_n. It is binomial with parameters M_n and q_n=P(H(T)≥k_n). Equation (19), applied at k_n−1, and 0≤k_n−η log n<1 show that there are constants c_1,c_2>0 such that, for all sufficiently large n,

    c_1 n^(−1/2) ≤ q_n ≤ c_2 n^(−1/2).

Indeed m^(η log n)=n^(−1/2), and rounding multiplies this by a factor bounded away from zero and infinity. Thus μ_n=E N_n=M_n q_n≥c_3√n for some c_3>0, while Var N_n=M_n q_n(1−q_n)≤μ_n. Since μ_n/log n→∞, for large n μ_n−log n≥μ_n/2. Chebyshev's inequality then gives

    P(N_n≤log n) ≤ μ_n/(μ_n−log n)^2 ≤ 4/μ_n → 0.

Total-variation convergence transfers this event to the conditioned branch forest. This transfer is valid for an n-dependent event because total variation is the supremum over all measurable events, rather than only fixed cylinder events. Consequently with probability tending to one there are more than log n distinct branches of height at least k_n. Choose a vertex at height k_n in each such branch. Its distance from v*_n is k_n+1. The unique path between two vertices chosen in distinct branches passes through v*_n, so their mutual graph distance is 2(k_n+1)≥2η log n.

### Uniform covering property of compact GH families

For any r>0 and any compact subset K of the space of compact metric spaces, there is a finite constant C(K,r) such that every X∈K is coverable by at most C(K,r) closed balls of radius r. To prove this, fix Y∈K and choose a finite r/4-net in Y, possible by compactness of Y. For X with d_GH(X,Y)<r/8, realize X and Y isometrically in a common metric space at Hausdorff distance less than r/8. For each net center in Y choose a point of X within r/8. Any x∈X is within r/8 of some y∈Y, that y is within r/4 of a net center, and the center is within r/8 of its chosen point of X. Thus the chosen points form an r/2-net in X. The neighborhoods {X:d_GH(X,Y)<r/8}, Y∈K, have a finite subcover of K, and taking the largest of their finite net sizes proves the assertion.

A radius-r ball can contain no two points whose mutual distance is strictly greater than 2r, by the triangle inequality. Therefore a set of more than C(K,r) points at pairwise distances >2r excludes membership in K.

### Necessity and sufficiency

If a_n log n does not tend to zero, there are ε>0 and an infinite subsequence n_j such that a_{n_j}log n_j≥ε. By the packing estimate, with probability tending to one a_{n_j}T_{n_j} contains more than log n_j points separated by at least 2ηε. Fix r=ηε/2, so this separation is strictly greater than 2r. For each compact K the uniform covering property shows P(a_{n_j}T_{n_j}∈K)→0. This contradicts tightness, which would supply a compact K having probability at least, for example, 1/2 for every j. This argument handles bounded, divergent, and oscillating scaling sequences at once.

Conversely suppose a_n log n→0. Since H(T_n)/log n→h<∞ and diam(T_n)≤2H(T_n), we have diam(a_n T_n)→0 in probability. For a compact metric space X the correspondence pairing every point of X with a singleton has distortion diam(X), hence d_GH(X,{*})≤diam(X)/2. It follows that a_n T_n→{*} in probability. The GH space of compact metric spaces is Polish; a weakly convergent sequence of its probability laws is tight (and finitely many initial laws do not affect tightness). This proves the stated equivalence and the limit assertion.

## Proposition B: limits in a sampling topology are not ordinary separable metric-measure limits

For the geometric-arm distance array above, P(D_12<2)=0. No separable metric space with a Borel probability measure μ can have this distance law for independent μ-points. In fact choose a countable dense set {x_j}. The open balls B(x_j,1/2) cover the space, so at least one has positive μ-measure. Two independent μ-points both belong to this ball with probability μ(B)^2>0, and their mutual distance is <1 by the triangle inequality. This contradicts P(D_12<2)=0. Thus there is no contradiction between Janson's long-dendron convergence and failure of usual compact GH (or separable metric-measure) convergence. This proof also applies to the deterministic unit-arm law at ν=0 under complete condensation.

For reference, the pair-distance probability mass function is

    P(D_12=s)=(s−1)(1−m)^2 m^(s−2),  s≥2.

There are s−1 possible pairs of positive integers summing to s; each has probability (1−m)^2 m^(s−2). Summing over them proves the formula. This describes the published limiting object explicitly; it does not construct a new general-weight limit.

## Checks and hostile-referee audit

1. Exact source statement checked on PDF p. 136; weight hypotheses and ν definition checked on pp. 7–8. This includes ν=0, which a purely subcritical offspring-law argument would miss.
2. Full original Kortchemski PDF checked for (Hθ), Corollary 2.7, equation (19), and Theorems 4–6. The decay exponent in the packing proof is **negative**: q_n is of order n^(−1/2), not n^(+1/2). The height constant is the reciprocal 1/log(1/m).
3. Original Janson 2021 PDF checked for Theorems 10.1 and 11.1, and open-case Remarks 10.8 and 11.3. Complete condensation is an extra assumption; general ν<1 does not imply it.
4. Compact-family covering bounds are proved above; diameter alone cannot yield tightness. Many macroscopic disjoint branches are the essential obstruction.
5. Numerical checks in numerical_checks.py exhaust 59,049 finite collision inequalities and 156 exact rational convolution identities. Its nine packing examples use a normalized geometric survival-tail proxy, not conditioned-tree simulations and not numerical evidence for a new theorem.
6. FiniteChecks.lean formalizes the finite collision bound Σs_i²≤KΣs_i for 0≤s_i≤K and the triangle-inequality ball obstruction. The final lean_check.txt reports exit_code=0 (45.64 seconds). Only these finite algebraic steps are claimed as Lean-checked; the probabilistic inputs and analytic proof are not Lean-formalized. No sorry or native_decide is used. The first run failed because the finite-sum distributivity module was missing; adding the specific Ring.Finset import fixed it.

## Remaining gap and final scope

No complete answer to the unrestricted Problem 20.11 was obtained. The question does not specify a topology or what counts as a “similar” limiting object. Nontrivial compact GH limits already fail in the regularly varying class (Proposition A). There is a positive long-dendron limit under complete condensation, including beyond regular variation, by Janson 2021. For arbitrary ν<1 weights with incomplete condensation, the law and geometry of the large-degree skeleton and any general full-sequence sampling limit remain unestablished here. A failure of complete condensation by itself does not prove a failure of every possible rescaling or sampling limit. No such universal negative conclusion is claimed.

Bounded literature searches did not identify a paper removing this gap. API rate limits restricted citation coverage, so this is not certification that no subsequent solution exists. First-pass verdict: PARTIAL. A user-requested second attempt is recorded in SECOND_ATTEMPT.md; its later conclusions supersede this first-pass status where stated explicitly.

## Second attempt outcome (2026-10-11; supersedes the gap above in the stated scope)

SECOND_ATTEMPT.md records two new approaches and a complete explicit counterexample: w_0=w_1=1, w_{3^j}=2^((3^j)^3), and all other weights zero. It has ν=0<1 and is admissible at every size. Along n=3^j+1 it is a star with high probability; along n=2·3^j+1 it is a double star with high probability. All non-target ordered-tree entropy is included in the proof.

Theorems C and D show that **every full-sequence finite-valued sampling-distance limit after scalar rescaling is trivial**, even if the scale is random and depends on the tree before vertices are sampled. Corollary E gives the same negative conclusion for compact GH full-sequence limits. Explicit subsequential long-dendron objects are nevertheless constructed. Thus a universal full-sequence nontrivial scalar metric limit for all ν<1 weights is disproved, rather than merely unestablished.

What remains unresolved here is a general theory for 0<ν<1 incomplete condensation, or the original question's unrestricted “some kind” of object allowing subsequences, nonscalar representations or other topologies. Verdict remains PARTIAL for that original broad formulation. Four new finite algebraic lemmas passed Lean (sparse_lean_check.txt), and exact counting and graph checks are saved in sparse_exact_checks.json and sparse_graph_checks.json.
