MINOR

Both stated partial results are correct under the definitions in the submitted report. I found no gap in the strip entropy argument, the planar argument with two-sided bounded conditional odds, the identification by internal spanning, or the elementary planar FA-2f bootstrap proof. In particular, the planar proof does address the borderline shell count; it does not merely discard a surface term by dividing by volume.

The main correction concerns value and attribution. Result (1) follows directly from the source after enumerating the strip as a one-dimensional system with site-dependent finite-range constraints. It should be described as a corollary of the source, rather than an extension of its scope. Result (2) is a valid adaptation of the classical Holley–Stroock argument to degenerate rates under a hypothesis on the stationary measure. I did not locate an existing theorem with precisely its all-q hypotheses, but this search does not certify novelty. Neither result resolves Conjecture 3.

The verdict is MINOR for the submitted PARTIAL claim, which expressly disclaims a general solution and does not assert established novelty. It would not justify accepting this work as a solution of D0028.

The required corrections and limitations are as follows. Locations refer to claim_files/REPORT.md.

1. Lines 5–10, 52, and Section 3: the strip theorem is already a corollary of source Theorem 2.5 and its internal-spanning argument. Write H={h_0,...,h_(m−1)} and send (k,h_i) to mk+i. A constraint of longitudinal range r then has one-dimensional range at most mr+m−1. This preserves individual binary spins, the Bernoulli reference measure, the semigroup, and stationarity. The transformed constraints can depend on the site, which source Section 2 and Theorem 2.5 allow; the source explicitly treats inhomogeneous East-polluted models. Its proof does not require translation covariance of the constraints. Internal spanning of the connected strip boxes then gives the classification exactly as in Lemma 2.8. Fix: call (1) a strip corollary and retain Section 3 as a self-contained proof. This applies also to the claimed monotone additions of legal moves.

2. Section 6, especially lines 308–313: the literature assessment omits the named Mountford complete-convergence paper and the principal 1977 Holley–Stroock comparison, as well as Moulin-Ollagnier–Pinchon and Georgii. Mountford (1997) does not cover FA-1f: its nearest-particle systems have unconditional death rate 1 and an attractive birth mechanism. FA-1f is not attractive and its last vacancy cannot heal. Holley–Stroock supplies the classical non-translation-invariant, dimension-two entropy mechanism, but an applicability claim must check rate positivity. The recent general theorem of Jahnel–Köppl explicitly imposes strictly positive rates and thus does not directly cover hard KCM. Fix: include these comparisons and distinguish a valid degenerate-rate adaptation from a proved priority claim. Precise sources, checked hypotheses, and retrieval limitations are recorded below and in sources/literature_audit.txt.

There is no remaining mathematical repair needed for (1) or (2) as formulated in Sections 1, 3, and 4. The qualifications about null conditioning, finite volume, and the meaning of reversibility below are essential scope clarifications; the submission already acknowledges the first two rather than using them as hidden assumptions.

I independently downloaded arXiv:2510.20461v1 and extracted it to sources/mst_2510.20461v1.txt. The download was converted through pdftotext on standard input/output; no PDF was saved. The source PDF SHA-256 is 85e5ecf910fb839a21a2ab38516e4dff41a536cfb61cc4169d963fb951d74f4d. The extracted-text SHA-256 is e35ae92d97c699662ee4c2ea450a8e53d410d0caf9ae533d135220d935774f0b. Both requested statements occur on PDF page 8. I checked the definitions and the relevant proofs in Section 2 against this version, rather than relying on the submitted paraphrases. [Martinelli–Shapira–Toninelli, v1](https://arxiv.org/abs/2510.20461v1).

Here are the exact mathematical statements, with the quantifiers and measures made explicit. Spins are 0 for vacant and 1 for filled, p=1−q, 0<q<1, and π=⊗_(x∈Z^d)Ber(p). Write E={β:BP(β)=β}. Conjecture 3 asserts

    for every stationary probability μ of a KCM, there is μ*∈P(E) such that
    μ = ∫_E π_β μ*(dβ),       π_β = π( · | BP(η)=β).

Theorem 2.13 asserts, for the d-dimensional East model on the infinite lattice Z^d and every stationary probability μ,

    μ* = BP_#μ,               μ = ∫_E π_β μ*(dβ).

There is no translation-invariance or finite-energy assumption in this theorem, and μ* is specified, not merely asserted to exist. The source gives the East kernel by its explicit product formula (2.6). In its notation I_β and P_a^+,

    π_β(η_y=1) = 1,   y ∉ ⋃_(a∈I_β)(P_a^+ ∪ {a});
                 0,   y ∈ I_β;
                 p,   otherwise,

with independent site coordinates. This explicit prescription is what defines the East measures even when the conditioning event has π-probability zero. Extended-coordinate indices in I_β describe interfaces arriving from infinity. The displayed source statements and formula are transcribed mathematically, rather than weakened to a finite-volume or typical-component statement.

Stationary here means invariant under the infinite-volume Feller semigroup: μP_t=μ for every t≥0. In particular μ(Lf)=0 for every local function. The generator is Lf=Σ_x c_x(π_xf−f); equivalently its flip rate is c_xq at a filled site and c_xp at a vacancy. The reference π is reversible. A stationary measure is not, by definition, required to be reversible, ergodic, translation invariant, or absolutely continuous with respect to π. Finite-volume models in the source are different chains, with the exterior frozen and the sum restricted to the finite domain.

For a general model, the phrase π(·|BP=β) does not define a unique law at every null fiber. Disintegration specifies a kernel only BP_#π-almost everywhere. When the desired mixing measure charges an exceptional set, arbitrary modifications of that kernel matter. The source does not give a general canonical rule at all such fibers; its East formula supplies one in that example. This is an ambiguity of the general formulation, not a counterexample to either partial result. It would be invalid to disprove the conjecture merely by selecting a malicious version on a null fiber.

For nearest-neighbor FA-1f on a connected strip, E={0,1}. Indeed, if a stable configuration has a vacancy and a filled site, a finite graph path between them contains a vacant/filled edge; that filled endpoint is bootstrap-unstable. Conversely both constant configurations are stable. Starting from any vacancy, bootstrap propagates along every finite path, so every non-full configuration has BP=0. Thus the two fibers are Ω\{1} and {1}. Under infinite-volume π, the first has probability one and π_0=π; among fiber-supported extensions the singleton fiber forces π_1=δ_1 despite being null. The conjectured form is exactly λπ+(1−λ)δ_1, with μ*=λδ_0+(1−λ)δ_1. Additional monotone moves containing all FA-1f moves and leaving the full state blocked have the same two BP-values.

One source-scope distinction matters: Theorem 2.4 on page 6 proves detailed balance for stationary translation-invariant laws; Theorem 2.5 proves detailed balance in dimension one. Corollary 2.9 then classifies one-dimensional FA-1f, while Theorems 2.12 and 2.13 classify East. A statement of detailed balance should not silently be promoted to the complete general fiber classification. The source's internal- and external-spanning lemmas perform separate identification work.

I checked the strip proof as follows. For V_n=[−nr,nr]×H, I_n=V_(n−1), and B_n=V_n\I_n, the exact shell size is 2r|H|. Increasing r to dominate the longitudinal constraint range ensures that a site in I_n has its whole constraint in V_n and that every site of B_n becomes interior in V_(n+1). Both ends of the strip are included in this shell; there is no unstated condition at either infinity.

Use the submission's a_V, b_V, A_V, and ℓ_V. The following checks cover each load-bearing step in Section 3.

| Location | Independent check | Result |
|---|---|---|
| Lines 80–98 | a_V is the integrated outgoing flip flux; marginalizing its extensions gives a smaller-box flux. Log-sum gives monotonicity of A, and the triangle inequality gives monotonicity of b. | Correct. |
| Line 96 | (u−v)log(u/v)≥2(u−v)^2/(u+v), followed by Cauchy–Schwarz and Σ(a+a^x)≤2. | b^2≤2A is valid, with room in the constant. |
| Line 100 | Apply stationarity to each cylinder indicator of zero mass. All incoming terms are nonnegative, and their sum is zero. | No flow into a zero-mass cylinder. The zero conventions are justified. |
| (3.1), lines 106–114 | Apply stationarity to a finite local function equal to log(μ_V/π_V) on its support, and pair each configuration with its flip. | The sign and factor S_n=2H_n are correct. |
| (3.2), lines 116–120 | Bound large positive ℓ by incoming flux, exchange the pair for negative ℓ, and use t exp(−t)≤λ exp(−λ) for t≥λ≥1. | Correct without any positive lower bound on c_x or μ. |
| (3.3), line 122 | Apply the same positive-part estimate with sup t exp(−t)=1/e. | 0≤S_n≤(2M/e)|B_n|. |
| (3.4), lines 126–128 | Old interior terms increase with the box; new interior terms include every x∈B_n. | Correct shell-increment direction. |
| (3.5), lines 130–132 | Enlarge b to V_(n+1), use b^2≤2A, then Cauchy–Schwarz over B_n. | Σ_(B_n)b_(V_n)≤sqrt(2|B_n|(S_(n+1)−S_n)). |
| Lines 134–136 | S_n is bounded and increasing, so its increments vanish. First fix λ, then exhaust boxes, then let λ grow. Sum enlarged-cylinder flux identities to obtain smaller ones. | All cylinder detailed-balance identities follow. |

For clarity, the entropy sign can be checked directly. The contribution at a site x is

    Σ_ζ a_V(x,ζ)[logρ_V(ζ^x)−logρ_V(ζ)]
      = −½ Σ_ζ [a_V(x,ζ)−a_V(x,ζ^x)] ℓ_V(x,ζ).

At an interior site this is −A_V(x)/2, since the constraint is unchanged by flipping x and π_V(ζ)r_x(ζ)=π_V(ζ^x)r_x(ζ^x). At a boundary site it need not be nonpositive. If ℓ>λ, its positive part is bounded using

    a_V(x,ζ^x)ℓ ≤ μ_V(ζ^x)ℓ
      = μ_V(ζ)[π_V(ζ^x)/π_V(ζ)] ℓ exp(−ℓ).

The ratio of π-probabilities is at most M=max(p/q,q/p). This gives the claimed uniform tail estimate. At zero marginal masses the paired rates vanish, so the arbitrary finite extension of logρ contributes nothing. This resolves the possible singular-law objection to the argument.

On the strip, the bounded shell makes S_n uniformly bounded, not merely small after normalization by volume. Equation (3.5) then makes the total boundary current tend to zero. Taking limits in (3.2) gives lim S_n≤2Mbλ exp(−λ) for every fixed λ, hence lim S_n=0. Nonnegativity and monotonicity force every S_n to be zero. No shift average of μ is taken anywhere.

The conclusion is also genuine semigroup reversibility, if that stronger terminology is desired. Cylinder detailed balance says that the measure c_xr_x μ is invariant under the flip at x. These identities extend from cylinders to bounded measurable tests. Hence each single-site generator is symmetric in L²(μ), and so is their sum on local functions. Equivalently, the finite-set dynamics with the outside configuration frozen is reversible under μ. The bounded finite-range graphical construction gives its infinite-volume limit on local observables, preserving the symmetry μ(fP_tg)=μ(gP_tf). Thus no additional reversibility hypothesis has been smuggled into the identification.

For the identification step, G_V consists of configurations which empty V with a filled exterior. Emptying in a legal bootstrap order, and then reversing another emptying order, connects any two states in G_V. Each flip is legal with every actual exterior because the constraints are monotone in vacancies. Apply detailed balance on a set containing V and its constraint boundary, and sum over that boundary. The ratio μ_V/π_V is constant on G_V, giving (3.6). This proves equality of the two conditional laws on the spins of V, not an assertion of independence from the exterior.

If both probabilities of G_(V_n) tend to one, the conditional-law identity implies equality of all fixed-cylinder probabilities. The bound (3.7) is valid; its factor 2 is merely loose. For FA-1f, connectedness gives G_V={V contains a vacancy}. Removing a=μ({1}) times the stationary atom leaves a stationary probability ν supported on configurations with a vacancy, unless a=1. Thus ν(G_(V_n))→1 without any density or energy assumption. Also π(G_(V_n))=1−p^|V_n|→1. Consequently ν=π and μ=(1−a)π+aδ_1. The same paths prove the claimed extension to monotone constraints containing every FA-1f move.

The planar proof uses the bounded-odds assumption in exactly two places. First, (4.1) bounds every adjacent finite-cylinder probability ratio, and therefore

    |ℓ_V(x,ζ)| ≤ K = log((1−ε)/ε)+|log(p/q)|.

The entire-complement version of (4.1) is equivalent: conditional expectation gives each finite bound, and martingale convergence recovers the entire-complement bound. Successively revealing spins shows μ_V(ζ)≥ε^|V|, so all logarithms in this argument are finite. Neither local absolute continuity with respect to π nor mere positivity of each finite-cylinder mass supplies this uniform K.

The exact planar shell count is

    |B_n|=(2nr+1)^2−(2(n−1)r+1)^2
         =8r²n−4r²+4r ≤8r²n       (r≥1).

Combining the constant K with the entropy identity and the shell-current estimate gives

    S_n ≤ K sqrt(2bn(S_(n+1)−S_n)),
    S_n² ≤ Cn(S_(n+1)−S_n),       S_n ≤ Dn.

These inequalities do force S≡0. Suppose S_m=s>0. Monotonicity yields S_(n+1)≥S_n(1+s/(Cn)); the product of these factors diverges because Σ1/n diverges. After S reaches 3C, the same inequality yields

    S_(n+1)≥S_n(1+3/n)≥S_n((n+1)/n)^2.

This gives quadratic growth and contradicts S_n≤Dn. Thus the step at lines 194–202 is sound. Simply using |B_n|/|V_n|→0 would not prove this conclusion for a non-translation-invariant law. Without bounded odds, the cutoff produces an extra logarithmic factor, as source Remark 2.16 explains; this proof does not remove that obstruction. In d≥3 the corresponding shell argument no longer has the same harmonic divergence.

Second, the lower vacancy bound in (4.1) gives stochastic domination of Bernoulli vacancies of density ε. Reveal any finite set using independent uniform variables. At each reveal the vacancy probability is at least ε, so the sites whose uniform variables lie below ε form an independent vacancy subset. For monotone update families G_V is increasing in vacancies, hence

    μ(G_(V_n))≥π_ε(G_(V_n))→1.

The assumed internal-spanning property at density q also gives π_q(G_(V_n))→1. The already-checked conditional-law identification gives μ=π_q. The detailed-balance part itself only needs finite-range constraints independent of the updated spin; monotonicity is used for the bootstrap and identification assertions. This is consistent with the update-family definitions at the start of the submission. Nothing here proves bounded odds for an arbitrary stationary law, or infers full-lattice uniqueness merely from finite legal connectivity.

I also checked the full FA-2f argument for (4.4). Keep a>0 fixed, t=1−a, m=ceil((log N)^(1/3)), and L=ceil(C log N), C>3/|log t|. A vacant m-square can grow to an L-square if, at each step, the next column of length k and next row of length k+1 each contain an initial vacancy. An already vacant square supplies one neighbor; propagation from the initial vacancy supplies the second neighbor along each new strip. All the queried initial strips and the seed are disjoint. Thus the successful-block probability is at least

    a^(m²) ∏_(k=m)^(L−1)(1−t^k)(1−t^(k+1)) ≥ a^(m²)/2

for large N, since the sum of strip-failure probabilities is at most 2t^m/(1−t). With J=floor(N/L)^2 independent disjoint blocks,

    P(no successful block) ≤ exp(−J a^(m²)/2) → 0.

Indeed log(J a^(m²))=2log N−O(log log N)−O((log N)^(2/3))→∞. Independently of that calculation, a union bound over at most 2N² segments bounds the probability of any fully filled horizontal or vertical length-L segment by 2N²t^L→0. The successful-block event and this global event need not be independent; the sum of their failure bounds suffices.

On their intersection, any emptied L-block grows left and right across the square, because each adjacent column segment has an initial vacancy. The resulting full-width vacant band grows upwards and downwards, because each adjacent row has a vacancy. All operations occur within [1,N]^2, so the exterior may stay filled. The claimed fixed-density internal-spanning limit follows. This is a correct elementary proof of a classical bootstrap fact, not a new sharp-threshold result. Its scales are not uniform as a tends to zero, and the submission does not claim that they are.

I wrote code/independent_fa1.py from scratch. It imports no submitted code and uses no submitted data to construct its tests. It builds the generator explicitly with rational q, solves ker(Q^T) over the rationals using SymPy, searches the legal-transition graph separately, computes bootstrap closures separately, and checks every stationary extremal vector and every returned kernel-basis vector. In particular it checks that the full kernel consists of product weights restricted to the independently found classes, rather than only checking that a guessed vector is stationary.

There are 52 completed cases. They use longitudinal lengths 2–5, path widths 1–3, periodic longitudinal identification or fixed filled/empty/one-vacancy/alternating end boundaries, and q=1/3, 2/5, 5/7. Additional larger cases are Z_4×P_2 and Z_3×C_3, the latter a genuine 3×3 torus with 512 configurations. Neighbor sets exclude the updated site and identify duplicated neighbors on length-two cycles. Every exact residual is zero; every kernel dimension equals both the communicating-class count and the BP-fiber count.

Representative independent results are:

| Graph/domain | Boundary | q | States | Rank Q | Kernel dimension | Class sizes | Active vacancy marginal |
|---|---|---:|---:|---:|---:|---|---:|
| Three-site interval | filled | 1/3 | 8 | 6 | 2 | 7, 1 | 9/19 |
| Three-site interval | one exterior vacancy | 1/3 | 8 | 7 | 1 | 8 | 1/3 |
| Four-site ring | periodic | 1/3 | 16 | 14 | 2 | 15, 1 | 27/65 |
| 3×P_2 | filled | 1/3 | 64 | 62 | 2 | 63, 1 | 243/665 |
| 3×P_2 | empty ends | 1/3 | 64 | 63 | 1 | 64 | 1/3 |
| Z_4×P_2 | periodic | 5/7 | 256 | 254 | 2 | 255, 1 | 823543/1152909 |
| Z_3×C_3 | periodic | 5/7 | 512 | 510 | 2 | 511, 1 | 5764801/8070619 |

There is an important finite-volume distinction. For a connected finite graph with filled exterior or no exterior vacancies, put G=Ω_V\{1}. Its full stationary simplex is

    θ π_V(·|G)+(1−θ)δ_1,       0≤θ≤1.

With an exterior vacancy adjacent to the connected domain, the unique stationary law is π_V. The closed-graph active extremal law is not λπ_V+(1−λ)δ_1 with 0≤λ≤1: its vacancy marginal is q/(1−p^|V|)>q. For example, the three-site q=1/3 active law has weights 1,2,4 according to the number of filled sites, total 1+3·2+3·4=19, and vacancy marginal 9/19. This hand calculation independently checks the matrix result. In infinite volume p^|V| tends to zero, so this finite conditioning is fully consistent with the strip conclusion. The submission's Section 5 uses the correct finite fiber formulation; there is no finite-volume counterexample to its actual claim.

The new data are data/independent_fa1_results.json and data/independent_fa1_run.txt. The completed run took 143.92 seconds, used nice 10, limited numerical libraries to one thread, and recorded peak RSS 82,968,576 bytes, about 79.1 MiB. The largest matrix was 512×512. These limits are far below four threads and 4 GB. Reproduction from an ordinary shell can use `nice -n 10 python3 code/independent_fa1.py`; the script asserts niceness at least 10 and sets the thread limits before importing SymPy. These finite calculations verify implementations and finite statements, not passage to an infinite stationary law.

The independent literature outcome is as follows. Downloaded full texts are listed with hashes in data/source_manifest.jsonl; failed downloads are recorded rather than presented as inspected sources.

| Primary source | Checked result or hypothesis | Consequence for this claim |
|---|---|---|
| [Martinelli–Shapira–Toninelli, arXiv:2510.20461v1](https://arxiv.org/abs/2510.20461v1), pp.6–8, 8–13 | Theorems 2.4–2.5, Lemma 2.8, Corollary 2.9, Theorem 2.10, Remark 2.16. | Directly supplies (1) after finite-width enumeration. The planar extra-hypothesis argument addresses the identified logarithmic obstruction. |
| [Mountford, Can. J. Math.49 (1997), 321–337](https://doi.org/10.4153/CJM-1997-016-7), definitions pp.321–323 and complete-convergence statement | Attractive reversible nearest-particle systems, with unconditional death and renewal birth rates. | Does not apply to FA-1f; similar names and two-extremal conclusions do not establish applicability. |
| [Mountford–Valle, arXiv:1609.01364](https://arxiv.org/abs/1609.01364), Theorem 1.1 and Remark 1.2, pp.2–3 | FA-1f on bounded-degree subexponential-growth graphs, facilitating density sufficiently close to one, with specified initial configurations or vacancy-distance tail bounds. | Relevant high-density convergence, not the stated all-q classification of arbitrary stationary laws. Spins use the opposite vacancy convention. |
| [Cancrini–Martinelli–Roberto–Toninelli, math/0610106](https://arxiv.org/abs/math/0610106), Proposition 2.4 in the arXiv text, pp.6–7 | Bootstrap threshold equals the threshold for simplicity of the equilibrium generator's zero eigenvalue. Published as PTRF140 (2008), 459–504, with changed numbering. | Equilibrium ergodicity does not classify all possibly singular stationary measures. |
| [Blondel et al., arXiv:1205.4584](https://arxiv.org/abs/1205.4584), Theorem 2.1, pp.4–5 | FA-1f convergence for q>1/2 under a uniform exponential moment for distance to a vacancy. | Bounded odds gives such vacancy-distance control, so this overlaps the high-q FA-1f part of (2), but not all q or general KCM. |
| [Blondel, ALEA22 (2025), 1335–1345](https://alea.impa.br/articles/v22/22-52.pdf), Theorem 2.3 and Lemma 4.1 | Entropy classification for one-dimensional constrained exchange dynamics, including frozen and product components. | Close precedent for adapting entropy to zero rates; the conserved exchange model is outside these binary heat-bath statements. |
| [Hartarsky–Toninelli, Kinetically Constrained Models, 2025](https://arxiv.org/abs/2412.13634), Sections 3.1–3.3, 4.4, Chapter 7 | Bootstrap background, finite legal paths, equilibrium ergodicity, inhomogeneous one-dimensional relaxation bounds, and limitations out of equilibrium. | No direct all-stationary-law planar classification found. Corollary 3.7 assumes finite disagreement; it cannot replace an infinite-volume uniqueness argument. |
| [Hartarsky–F. L. Toninelli, arXiv:2212.08437v2](https://arxiv.org/abs/2212.08437), Theorem 3.3 and footnote 2, p.9 | General KCM convergence when the dynamical vacancy parameter is sufficiently close to one; initial product laws can be replaced by dominating laws. | Overlaps a high-q part of (2) under its spanning and domination assumptions. Does not supply the all-q conclusion. Fabio Lucio Toninelli here is distinct from Cristina Toninelli, coauthor of the book. |
| [Holley, CMP23 (1971), 87–99](https://doi.org/10.1007/BF01877751) | Publisher abstract gives the entropy/Gibbs conclusion for shift-invariant states. | Foundational precedent, not a substitute for the non-translation-invariant proof. Full PDF retrieval was blocked. |
| [Holley–Stroock, CMP55 (1977), 37–45](https://doi.org/10.1007/BF01613147) | Publisher abstract explicitly includes non-translation-invariant stationary laws and potentials in dimensions one and two. | Classical source of this geometry-sensitive mechanism. Full PDF retrieval was blocked, so I do not certify a sharper original-rate hypothesis from its abstract alone. |
| [Moulin-Ollagnier–Pinchon, CMP55 (1977), 29–35](https://www.lix.polytechnique.fr/~moulin/papiers/05.Free_Energy_in_Spin-flip_Processes_is_Non-increasing.pdf), setup p.30, Theorem 2 and corollary p.34 | Requires spatial-group-invariant measures for the free-energy argument and strictly positive continuous flip factors. | Does not directly imply either hard-KCM assertion for arbitrary non-translation-invariant μ. |
| [Georgii, Probabilistic aspects of entropy](https://www.math.lmu.de/~georgii/papers/Dresden.pdf), Section 6, especially (6.2), p.11 | The relative-entropy-density variational result assumes translation invariance of the compared law. | General Gibbs/entropy formalism does not eliminate that hypothesis. No direct non-translation-invariant hard-KCM theorem was found there. |
| [Jahnel–Köppl, arXiv:2303.10640v2](https://arxiv.org/abs/2303.10640v2), (R3) p.7, Theorem 3.1 p.8 | The modern non-translation-invariant theorem assumes transition rates uniformly bounded away from zero. | Not directly applicable to KCM. The submission correctly replaces this kind of rate assumption by a bounded-odds assumption for its stationary-law argument. |
| [Martinelli, ICM 2026 survey](https://epubs.siam.org/doi/10.1137/25M180425X), Section 1.2, Theorem 1.5 and Conjecture 1.6, p.499 | Restates the internal-spanning uniqueness theorem and the general stationary decomposition conjecture; reference 48 is arXiv:2510.20461. | An independently verified 2026 citer still treating the full statement as conjectural. |

For the 2025–2026 search I used the exact arXiv identifier, title variants, stationary/invariant-measure queries with the model and author names, and the current publication pages of Shapira, Cristina Toninelli, and Hartarsky. The concrete later citer located is the ICM survey. A direct OpenAlex query independently returned that survey as its single indexed citer; Semantic Scholar returned HTTP 429. The responses are saved in data/citation_index_check.json. No later proof of the full conjecture or direct duplicate of (2) was found. This is a search result, not a claim that every citer or unpublished result has been excluded. The survey even miscites the dimension-one result as source Theorem 2.4; the checked v1 numbers it 2.5. I used the original rather than propagating that numbering discrepancy.

What remains of D0028 is substantial: unrestricted non-translation-invariant stationary laws in the plane, higher-dimensional stationary laws, and identification of appropriate laws on general bootstrap fibers, including a precise interpretation at null fibers. The strip corollary does not enlarge the genuinely higher-dimensional case. The planar result removes the stationarity-to-balance obstacle only within its bounded-odds class; it neither proves that all active stationary laws belong to that class nor resolves the general fiber problem. A complete decomposition also requires identification, not merely reversibility.

Task: “Break it if it is wrong.” — received 2026-11-13 09:18 +04 (Asia/Tbilisi; launcher clock).
