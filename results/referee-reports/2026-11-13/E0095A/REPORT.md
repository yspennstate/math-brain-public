PARTIAL

# E0095: adding an edge or a perfect matching

13 November 2026. All spectral gaps in the new results below are identified by their kernel; no claim of novelty is made for elementary perturbation or comparison arguments. The general exact optimizer requested by Diaconis remains unsettled by this investigation. A bounded-degree random-matching version is resolved in the literature.

## 1. What the source actually asks, and what later work settles

The supplied quotation is a paraphrase, not the wording of arXiv:1309.7754. The complete extracted source is [sources/diaconis_2013.txt](sources/diaconis_2013.txt), with PDF page delimiters.

- Question 3, PDF p. 9, fixes a generating set of a group and asks which extra generator speeds mixing most. Its example concerns a transposition and an n-cycle generating S_n; cutoff is mentioned separately.
- Question 4 starts on PDF p. 9 and continues on p. 10. Its principal operation is adding n/2 edges forming a perfect matching to a connected d-regular graph, producing a (d+1)-regular graph. It asks which matching gives fastest mixing, mentions the cycle, cites Chung's diameter results, and asks for accurate rates of convergence to uniformity.
- Its separate weighted-edge variation preserves a specified stationary law by Metropolization and asks about improving mixing or spectral gap. This is distinct from ordinary SRW after an edge addition.
- Total variation is explicitly defined earlier, on PDF p. 2. Q4 does not fix a threshold, equate fastest mixing with spectral-gap maximization, or impose laziness. Non-lazy walks can remain bipartite, so a general finite TV-mixing-time optimization needs an aperiodicity convention. We use a half-lazy walk for our finite optimization results. Cutoff is an asymptotic property of sequences, not an objective for one finite graph.

The Chung–Diaconis–Graham walk discussed elsewhere in the survey is affine doubling followed by noise. It is not a cycle with a random perfect matching. Reference [15] in Q4 is Fan Chung, *Diameters and eigenvalues*, J. Amer. Math. Soc. 2 (1989), 187–196. Likewise, the directly relevant random-matching author triple is Hermon–Sly–Sousi; Hermon–Lacoin–Peres studied distinctions between total-variation and separation cutoff.

The decisive later result is Jonathan Hermon, Allan Sly and Perla Sousi, *Universality of cutoff for graphs with an added random matching*, Ann. Probab. 50(1) (2022), 203–240, DOI [10.1214/21-AOP1532](https://doi.org/10.1214/21-AOP1532), [arXiv:2008.08564](https://arxiv.org/abs/2008.08564). Theorem 1.1, published pp. 203–204 (saved arXiv v3 p. 2), assumes even diverging sizes, bounded maximum degree and original components of size at least three. A uniform random matching gives non-lazy discrete-time TV cutoff with mixing time Θ(log n) and window O(sqrt(log n)), with high probability. Proposition 1.2, published p. 204 (arXiv p. 2), gives a positive absolute spectral gap with high probability. Thus random matchings are optimal in order for bounded degree. The theorem does not identify the exact best matching, its sharp leading mixing constant among all matchings, or an exact finite optimizer. The saved arXiv PDF retains the earlier title *Universality of cutoff for quasi-random graphs*.

The detailed title-by-title audit, theorem locations and source distinctions are in [sources/LITERATURE.md](sources/LITERATURE.md). Other main conclusions are:

| Reference | Exact relevant location | Scope |
|---|---|---|
| Krivelevich–Reichman–Samotij, *Smoothed analysis on connected graphs*, SIAM J. Discrete Math. 29 (2015), 1654–1669 | Theorem 5, saved author revision PDF p. 4 | Lazy TV mixing O(log² n) for bounded-degeneracy connected graphs plus independent G(n,ε/n) edges; not a perfect matching. |
| Boyd–Diaconis–Xiao, *Fastest mixing Markov chain on a graph*, SIAM Review 46 (2004), 667–689 | §§1.1, 2.1–2.2 | Convex/SDP optimization of transition weights and SLEM on fixed support; not unit-weight edge/matching selection. Symmetry and continuous-time follow-ups retain the weight-optimization distinction. |
| Ghosh–Boyd, *Growing well-connected graphs*, CDC 2006, 6605–6611 | §III, equation (7), p. 6607; §III-B, (8)–(11), p. 6608 | Established unnormalized Fiedler derivative, finite-update bounds and approximate edge-selection heuristic. |
| Yoonsoo Kim, *Bisection algorithm of increasing algebraic connectivity by adding an edge*, IEEE TAC 55 (2010), 170–174 | Saved author draft §II-B, (2.1), Table I, PDF pp. 2–3 | Secular-equation algorithm for the unnormalized Laplacian. The cited Kim–Mesbahi paper, IEEE TAC 51 (2006), 116–120, instead concerns distance-dependent weights and vertex positions. |
| Ding–Peres, *Sensitivity of mixing times*, ECP 18 (2013), paper 88 | Theorem 1, saved arXiv p. 1 | Bounded conductance perturbations can change lazy TV mixing by order log n/log log n. |
| Hermon–Peres, *On sensitivity of mixing times and cutoff*, EJP 23 (2018), paper 25 | Theorem 3, saved arXiv p. 7 | Optimal order-logarithmic TV sensitivity and changes in cutoff; not a single-edge theorem. |
| Hermon–Kozma, *Sensitivity of mixing times of Cayley graphs*, Canad. J. Math. 76 (2024), 1400–1431 | Published Theorem 1.1, p. 1401; saved arXiv Theorem 1, p. 2 | Nested generating sets can slow lazy TV mixing substantially; growing degrees and different augmentation constraints. |
| Chatterjee–Diaconis, *Speeding up Markov chains with deterministic jumps*, PTRF 178 (2020), 1193–1214 | Theorems 2.1–2.2, saved arXiv pp. 2–3; 2021 republication pp. 379–380 | Alternates a permutation with a transition step; does not add undirected matching edges. |
| Baran–Hermon–Šarković–Sousi, *Phase transition for random walks on graphs with added weighted random matching*, PTRF 193 (2025), 989–1074 | Journal Theorems 1–4, pp. 991–993; arXiv v2 Theorems 1.2, 1.3, 1.5, 1.6, pp. 3–4 | Vanishing matching weights, polynomial-growth and linear-entropy families; cutoff phase transitions, not deterministic optimization. |
| Eldan–Rácz–Schramm, *Braess's paradox for the spectral gap in random graphs and delocalization of eigenvectors*, RSA 50 (2017), 584–611 | Theorem 1.3 and Remark 1.4, p. 586; Lemma 3.2, p. 593 | Adding an edge can reduce the normalized random-walk gap. |

The Chatterjee–Diaconis publisher correction/republication, PTRF 181 (2021), 377–400, DOI [10.1007/s00440-021-01049-1](https://doi.org/10.1007/s00440-021-01049-1), was also checked. Its notice concerns assignment to the wrong issue, not a mathematical correction; it republishes the same relevant theorems.

A later targeted search also found a C_8 chord-deletion example in Jamadandi–Rubio-Madrigal–Burkholz, *Spectral Graph Pruning Against Over-Squashing and Over-Smoothing*, NeurIPS 2024, Proposition 3.2, PDF p. 4. This overlaps the cycle phenomenon proved below. No novelty is asserted for that phenomenon. Some requested publisher copies were unavailable; exact locations above distinguish downloaded author/arXiv versions from published versions.

## 2. Three precise versions and conventions

Let G be a finite connected simple d-regular graph on even n vertices. Let A be its adjacency matrix, D=dI, and L=D-A. For any connected weighted augmentation H, write

    P_H = D_H^{-1} A_H,       K_H = (I+P_H)/2,
    0=μ_1(H)<μ_2(H)≤...≤μ_n(H)

for the eigenvalues of D_H^{-1/2} L_H D_H^{-1/2}. We abbreviate μ(H)=μ_2(H).

The one-sided non-lazy gap is μ(H). The half-lazy gap is γ(H)=μ(H)/2 and its relaxation time is t_rel(H)=2/μ(H). The non-lazy absolute gap is 1-max(|1-μ_2|,|1-μ_n|); it can be zero on bipartite graphs. The unnormalized algebraic connectivity λ_2(L_H) describes a different process, the continuous-time walk with unit rate on each edge.

Our finite optimization uses new simple edges: an edge is a nonedge of G, and a matching is a perfect matching in its complement. Such a matching need not exist on every small input, for example K_3,3 has complement two odd triangles. Those inputs have an empty matching candidate set, explicitly recorded as such. If parallel copies of existing edges are allowed instead, matching degrees still increase uniformly and the comparison theorems below remain valid. The random-matching literature uses the unrestricted matching/edge-superposition convention; it must not silently be equated with sampling only complement matchings.

**A. Local edge and matching design.** For an eligible edge e={u,v}, add conductance t≥0 and maximize μ_e'(0+). Determine when a scalar Fiedler score applies, how multiplicity changes the answer, and whether a first-order winner remains optimal at t=1. A matching version adds conductance t on every edge of the matching.

**B. Extremal gap and mixing comparisons.** Bound μ(G+e)/μ(G) and μ(G+M)/μ(G), and the corresponding relaxation-time changes. Distinguish what these bounds imply for half-lazy TV mixing from what they do not prove.

**C. Cycle and torus augmentation.** Determine the optimal single chord on an even cycle, compare an antipodal matching with an order-optimal random matching, and exhaust finite cycle/torus examples. Exact optimal perfect matchings for every cycle size or every torus are left open here.

Adding one weighted edge changes the stationary law:

    π_t(x) = [d+t·1_{x∈{u,v}}]/(dn+2t).

For a full matching, every degree becomes d+t and stationarity stays uniform. These formulas also hold for K_H. A Metropolized chain with fixed target π is a different kernel and is not substituted for SRW in the computations.

## 3. First-order perturbation, with full proofs

### Proposition 1: the normalized derivative

Suppose μ=μ(G) is simple. Let f be a real unit Euclidean eigenvector, Lf=dμf. Put b=e_u-e_v and C=e_ue_u^T+e_ve_v^T. Then

    μ_e'(0) = [(f(u)-f(v))² - μ(f(u)²+f(v)²)]/d.             (1)

The half-lazy gap derivative is half of (1). For the unnormalized Laplacian the derivative is just (f(u)-f(v))². Thus the raw difference heuristic is exactly the local optimizer for fixed vertex mass/unnormalized Laplacian. For SRW it is exactly correct only when it orders the candidates in the same way as (1); a sufficient condition is that f(u)²+f(v)² is constant over the candidate set. There is no general license to drop the correction.

**Proof.** The augmented eigenproblem is

    (L+tbb^T)g(t)=μ(t)(dI+tC)g(t).

Normalize g(t)^T(dI+tC)g(t)=1. A simple eigenvalue and eigenvector can be chosen differentiably near zero: transform the pencil by the positive square root of its mass matrix and apply the simple-root implicit function theorem to its characteristic polynomial and normalized eigenvector equations. Differentiate and multiply by g(0)^T. Terms in g'(0) cancel because Lg(0)=μd g(0). Consequently

    μ'(0)=g(0)^T[bb^T-μC]g(0).

Since g(0)=f/sqrt(d), equation (1) follows. Keeping dI fixed instead gives the unnormalized formula. ∎

For finitely many candidate edges, if the corrected score has a unique strict maximizer e*, then e* also maximizes μ_e(t) for all sufficiently small positive t. Indeed, for every other e,

    μ_e*(t)-μ_e(t)=t[μ_e*'(0)-μ_e'(0)]+O(t²),

and the finitely many strictly positive derivative differences admit a common small interval. A tied derivative does not decide the next order. This argument provides no conclusion at t=1.

### Proposition 2: matching design at first order

Under the same simplicity assumption, for a perfect matching M,

    μ_M'(0) = [Σ_{uv∈M}(f(u)-f(v))²-μ]/d.                 (2)

Thus a maximum-weight perfect matching with weights (f(u)-f(v))² solves the local matching problem exactly, with the specified allowed pairs.

**Proof.** Here L(t)=L+tL_M and D(t)=(d+t)I. Proposition 1's differentiation gives [f^TL_Mf-μf^Tf]/d, which is (2). The subtracted term is independent of M. ∎

### Proposition 3: multiplicity and the next order

If μ has multiplicity r, let the columns of F be a dI-orthonormal basis of its eigenspace. For an augmentation L+tB, D+tC, the derivatives of the r eigenvalue branches are the eigenvalues of

    W=F^T(B-μC)F.                                        (3)

The right derivative of μ_2 is the smallest eigenvalue of W. One arbitrarily chosen scalar eigenvector cannot replace this matrix.

**Proof.** Write a differentiable eigenbranch g(t)=Fa+t h+O(t²), μ(t)=μ+tν+O(t²). The coefficient of t in the pencil equation is

    (L-μD)h=-(B-μC)Fa+νDFa.

Multiplication by F^T gives Wa=νa. Conversely, diagonalizing this symmetric compressed perturbation gives the first-order branches; the same conclusion follows from the first-order min–max principle on the isolated eigenspace. Branches below or above the μ-cluster stay separated for small t. The lowest branch of the cluster is μ_2. ∎

In particular, for the unnormalized Laplacian a positive rank-one edge update cannot increase λ_2 when its multiplicity is at least two. There is an old Fiedler eigenvector orthogonal to b, hence an unchanged eigenvalue λ_2; positive semidefinite monotonicity prevents a decrease. For normalized SRW the value may instead decrease, as proved below.

For completeness, a full second-derivative formula explains the finite-weight obstruction. Let g_j be a D-orthonormal eigenbasis of the original pencil, with g_i belonging to a simple μ_i=μ. Write w_ji=g_j^T(B-μC)g_i and c=g_i^TCg_i. Then

    μ''(0)=2 Σ_{j≠i} w_ji²/(μ-μ_j)-2μ'(0)c.             (4)

**Proof.** Project the differentiated eigenvector equation onto g_j for j≠i to get g_j^TDg_i'=w_ji/(μ-μ_j). Differentiating the normalization gives g_i^TDg_i'=-c/2. Differentiate μ'=g_i^T(B-μC)g_i. Substitute this eigenbasis expansion of g_i'; the coefficient along g_i contributes -cμ', and differentiating -μC contributes another -cμ'. This is (4). ∎

Equation (4) is not an error bound at unit weight. The certified examples in §7 show that finite-weight terms beyond first order really change the optimizer even with a simple base gap.

## 4. Gap comparisons, sharp matching bounds and relaxation

For positive vertex masses D_H define

    V_H(h)=min_a Σ_x D_H(x,x)(h(x)-a)²,
    E_H(h)=Σ_{xy∈E(H)}c_xy(h(x)-h(y))².

The normalized Poincaré variational principle is

    μ(H)=inf_{h nonconstant} E_H(h)/V_H(h).              (5)

It follows by subtracting the D_H-weighted mean and applying the ordinary Rayleigh principle after conjugation by D_H^(1/2). This formulation explicitly handles the changed stationary law.

### Proposition 4: a single edge

For an eligible unit edge e={u,v}, let R_G(u,v) be its original effective resistance (unit conductances). Then

    [d/(d+1)]μ(G) ≤ μ(G+e)
       ≤ min{ μ_3(G), μ(G)+2/d, [1+R_G(u,v)]μ(G) }.       (6)

Also R_G(u,v)≤dist_G(u,v)≤n-1. These are useful bounds, not a claimed sharp extremal single-edge theorem as a function of n,d.

**Proof.** Pointwise dI≤D'≤(d+1)I implies V_G≤V_G+e≤(1+1/d)V_G. The energy increases, giving the lower bound in (6).

Let f be a unit Euclidean eigenvector of L at dμ, with zero ordinary mean. Since V_G+e(f)≥d and (f(u)-f(v))²≤2, its quotient is at most μ+2/d.

The ordered generalized eigenvalues for mass D'≥dI are bounded above by the corresponding eigenvalues of L'/d, by the min–max principle on all subspaces. The positive rank-one update L'=L+bb^T satisfies λ_2(L')≤λ_3(L): intersect the span of the first three original eigenvectors with b-perp to obtain a subspace of dimension at least two where the update vanishes. Thus μ(G+e)≤λ_3(L)/d=μ_3(G).

By the variational characterization of effective resistance, (h(u)-h(v))²≤R_G(u,v)E_G(h). Hence E_G+e(h)≤(1+R_G(u,v))E_G(h), while V_G+e(h)≥V_G(h). Evaluate on a minimizing h for G to obtain the last bound. Cauchy–Schwarz along any u–v path gives the displayed distance bound. ∎

If μ_2(G)=μ_3(G), (6) proves that no single added edge increases the one-sided normalized gap, at any positive weight. It does not say that the gap remains unchanged.

### Proposition 5: sharp degree-dependent matching bounds

For any added unit perfect matching, including the parallel-edge convention,

    d μ(G)/(d+1) ≤ μ(G+M) ≤ [d μ(G)+2]/(d+1).           (7)

Both inequalities attain equality on simple graphs with genuinely new matching edges. In particular, relaxation can slow by at most (d+1)/d under any matching, and it can speed up by order n² for every fixed d≥2. The order n² is the largest possible for fixed d. The same relaxation slowdown bound follows for one edge from (6).

**Proof of (7).** The degrees become d+1. On 1-perp, L_G has minimum eigenvalue dμ, while 0≤L_M≤2I, because each two-vertex matching block has eigenvalues 0,2. Taking minimum Rayleigh quotients gives (7).

**Sharpness of the lower inequality.** Let G=K_{m,m}, m even and at least four. Add perfect matchings internally in the two parts. Originally d=m and μ=1. A nonzero vector constant on each matched pair, supported in one part, and summing to zero satisfies L_Mf=0 and L_Gf=mf. Thus the new gap is at most m/(m+1), and (7) gives equality.

**Sharpness of the upper inequality.** Let n≥4 be even and G be K_n with a perfect matching M removed. Then d=n-2. Decomposing into pair-symmetric and pair-antisymmetric vectors gives λ_2(L_G)=n-2, so μ=1. Adding precisely M gives K_n, whose normalized gap is n/(n-1)=(dμ+2)/(d+1). ∎

**Proof of the n² order.** For a zero-mean vector h,

    n Σ_x h(x)² = Σ_{u<v}(h(u)-h(v))²
                ≤ [n(n-1)/2] diam(G) E_G(h).

The inequality follows from Cauchy–Schwarz on a shortest path for each pair and bounding its path energy by total energy. Therefore

    μ(G) ≥ 2/[d(n-1)diam(G)] ≥ 2/[d(n-1)²].             (8)

Every normalized gap is at most 2. The improvement ratio for any augmentation is consequently at most d(n-1)², which is O(n²) for fixed d.

For a matching attaining this order, take G=C_m □ K_{d-1}, with m even and growing, and fixed d≥2 (K_1 for d=2). This is d-regular on n=m(d-1) vertices. The Cartesian-product spectrum gives μ(G)=(2-2cos(2π/m))/d=Θ(n^-2). HSS Proposition 1.2 supplies a matching with new gap bounded below by a positive constant depending only on d. This proves an improvement Θ(n²).

This conclusion also holds when added pairs must be nonedges. For fixed d, let X count original graph edges in an unrestricted uniform matching. For each fixed k, the number of k-edge matchings already in G is (dn/2)^k/k!+O(n^(k-1)); overlapping edge choices contribute only O(n^(k-1)) because d is fixed. A prescribed disjoint k-edge set occurs in the random matching with probability 1/[(n-1)(n-3)...(n-2k+1)]. Thus E[binom(X,k)]→(d/2)^k/k!. The upper and lower Bonferroni sums for P(X=0), followed by k→∞, show P(X=0)→exp(-d/2)>0. Conditioning an event of probability 1-o(1) on X=0 preserves probability 1-o(1). HSS therefore yields the required complement matching as well. ∎

This is sharp in n-order; (7) is sharp as a uniform inequality across all n,d. Neither statement asserts an asymptotically optimal expansion constant for every fixed degree.

## 5. What follows for TV mixing, and what does not

For K=(I+P)/2, write γ=μ/2, t_rel=1/γ and π_min=min_xπ(x). For 0<ε<1/2,

    (t_rel-1) log(1/(2ε)) ≤ t_mix(ε)
      ≤ ceil[t_rel log(1/(2ε sqrt(π_min)))].             (9)

**Proof.** Reversibility gives an orthonormal eigenbasis in L²(π). The L² distance of K^t(x,.)/π from 1 is at most (1/π(x)-1)^(1/2)(1-γ)^t. Cauchy–Schwarz bounds TV by half this quantity, and 1-γ≤exp(-γ) gives the upper bound. For the lower bound, normalize an eigenfunction of eigenvalue 1-γ to sup norm one and start at a vertex where its absolute value is one. The difference between its expectation at time t and at stationarity is (1-γ)^t, at most twice TV. Hence t≥log(1/(2ε))/[-log(1-γ)]≥(1/γ-1)log(1/(2ε)). If γ=1 the lower bound is interpreted as zero. ∎

For a single edge π_min=d/(dn+2); for a matching π_min=1/n. Thus (6)–(7) imply explicit relaxation comparisons and general TV upper bounds. They do not characterize exact TV speedup, its best matching, or cutoff. The Ding–Peres and Hermon–Peres results show why a robust gap comparison cannot generally be promoted to a constant-factor TV comparison.

For the cycle specifically, half-lazy unaugmented TV mixing is Θ(n²), while random matching augmentation gives Θ(log n); hence an achievable TV speedup is Θ(n²/log n). To verify the former order without losing a logarithm, the cycle eigenvalues of K are cos²(πk/n). The lower bound in (9) is Ω(n²). For the upper bound, Fourier expansion and Cauchy–Schwarz give

    4 ||K^t(x,.)-uniform||_TV²
       ≤ Σ_{k=1}^{n-1} cos^(4t)(πk/n)
       ≤ 2 Σ_{k≥1} exp(-8tk²/n²).

Here use sin(πk/n)≥2k/n for k≤n/2. Taking t=Cn² makes the last sum as small as desired. HSS supplies the augmented non-lazy logarithmic upper bound; lazifying preserves the logarithmic upper order by expressing K^t as a binomial mixture of powers of P. The support of a bounded-degree walk grows at most exponentially, giving the logarithmic lower bound. No claim is made here that Θ(n²/log n) is a proved universal maximum TV improvement over every regular base graph.

## 6. Exact cycle results and balanced tori

### Proposition 6: the best single chord of an even cycle

Let G=C_n, n≥4 even, and add one new unit chord. The largest possible one-sided normalized gap is the original value

    μ(C_n)=1-cos(2π/n).

It is attained exactly by antipodal chords. Every non-antipodal new chord strictly reduces it. Therefore this statement also determines the optimizer for the half-lazy gap and relaxation time. It makes no non-lazy absolute-gap assertion.

**Proof.** The original second eigenspace is spanned by cos(2πj/n) and sin(2πj/n), so its dimension is two. Proposition 4 prevents every chord from increasing μ.

Suppose u,v are not antipodal. There is an eigenfunction f in this two-dimensional space with f(u)=f(v)=a≠0: take the cosine centered at the midpoint of their angles. Its ordinary mean is zero. Its energy is unchanged by the chord, while its new weighted variance is

    V'(f)=2||f||²+2a²-(2a)²/(2n+2)
          >2||f||².

Thus its new quotient is strictly less than μ, proving strict decrease.

For an antipodal chord, relabel its endpoints 0,n/2. Translation by n/2 preserves the new weighted graph. Decompose into even and odd functions under this involution; these subspaces are orthogonal for both energy and mass. On the odd subspace the weighted mean is zero, f(n/2)=-f(0), and

    E'(f)≥2μ||f||²+4f(0)² ≥ μ[2||f||²+2f(0)²]=μ V'(f),

because μ≤1. On the even subspace, the original first positive normalized eigenvalue is μ_even=1-cos(4π/n). The variance argument used in (6) gives new even gap at least (2/3)μ_even. Since μ_even/μ=4cos²(π/n)≥2, this is greater than μ. Finally sin(2πj/n) vanishes at the two chord endpoints and remains an exact generalized eigenfunction at μ. The full new gap is therefore μ. ∎

### Proposition 7: all antipodal pairs are a poor large-cycle matching

Let M_ant pair j with j+n/2 on C_n. Then

    μ(C_n+M_ant) = [2-2cos(4π/n)]/3 = Θ(n^-2),          (10)

and its gap improvement ratio tends to 8/3. In contrast an order-optimal matching has gap Θ(1), by HSS and the trivial upper bound 2. In particular, pairing every vertex with its furthest cycle vertex is not an asymptotically optimal matching rule.

**Proof.** All three operators are circulant. The normalized Laplacian eigenvalue of Fourier mode k is

    [2-2cos(2πk/n)+1-(-1)^k]/3.

Among positive even modes, k=2 or n-2 minimizes the value. Among odd modes k=1 or n-1 minimizes it. Comparing these two values, with c=cos(2π/n), reduces to 4c²≥2c, valid for even n≥6; n=4 is an equality checked directly. This proves (10), and the Taylor expansion of cosine gives the ratio 8/3. ∎

For a balanced fixed-dimensional torus (Z/mZ)^k with m even and k fixed, n=m^k and d=2k, the Cartesian spectrum gives μ=(1-cos(2π/m))/k=Θ(n^(-2/k)). A random added matching gives gap Θ(1), an order-optimal spectral improvement Θ(n^(2/k)). This determines the achievable order, not the exact optimal torus matching.

## 7. Certified finite-weight counterexamples

Vertices below are numbered from zero. Full graphs are given by graph6 strings and edge lists in [data/examples_algebraic.json](data/examples_algebraic.json).

**A simple-gap edge failure.** The cubic graph with graph6 string ``I?`cmPoM?`` has n=10 and

    μ(G)≈0.37353825280939484.

Both the raw and corrected first-order edge-score maximizers are confined to {0,2} and {0,8}. Each resulting gap is approximately 0.476945558172555. The edge {2,4} gives approximately 0.481177965247610. A certificate encloses the original simple eigenspace and proves that *every* exact first-order maximizer is in that losing pair set. Rational inertia separates their resulting gaps from the witness. Exact characteristic-polynomial root isolation independently confirms the strict inequality for {0,2} versus {2,4}; see [data/audit_summary.json](data/audit_summary.json). Thus this is a failure at unit weight, with a simple original gap, even after correcting normalization. It cannot be dismissed as a basis choice at a multiple eigenvalue.

**An explicit matching failure.** The quartic graph `GEnfbW` has eight vertices and edges

    03,04,05,06, 13,15,16,17, 24,25,26,27, 34,36,47,57.

Its second unnormalized eigenvalue is 4-sqrt(2), simple. One corresponding eigenvector is

    f=(-1/sqrt(2),0,1/sqrt(2),-1,0,1/sqrt(2),-1/sqrt(2),1),

with ||f||²=4. The unique matching that maximizes Σ(f(u)-f(v))² is

    M_h={02,14,37,56}.

Indeed this sum is at most 2||f||² for every matching, with equality exactly when each pair has opposite coordinates. The two zero coordinates must pair, the coordinates ±1 must pair, and among the two choices for pairing ±1/sqrt(2), the alternative uses existing edges 05 and 26, hence is inadmissible. So M_h is the unique first-order winner.

Nevertheless,

    μ(G+M_h)=4/5,
    μ(G+{02,14,35,67})=(11-sqrt(5))/10 >4/5.

To check the base gap, its L-spectrum is

    0, 4-sqrt(2), 5-sqrt(3), 4,4,4+sqrt(2),6,5+sqrt(3).

The normalized characteristic polynomials of the two augmented graphs are respectively

    x(5x-6)²(5x-4)(25x²-60x+34)² / 78125,
    x(x-1)²(5x-8)(25x²-55x+29)² / 3125.

Their smallest positive roots are the two displayed gaps. The strict inequality is equivalent to 3>sqrt(5). These factorizations, direct eigenvector substitution and the elementary root ordering constitute an exact algebraic counterexample independent of numerical search.

**Multiplicity and normalization.** Adding an edge within one part of K_3,3 decreases its normalized gap from 1 to

    (33-sqrt(129))/24≈0.901757637850.

To verify this, partition the augmented graph into the two joined vertices, the remaining vertex in their part, and the opposite part. The transition quotient is

    [1/4  0  3/4]
    [  0  0    1]
    [2/3 1/3   0].

Its nontrivial eigenvalues solve x²+(3/4)x-1/12=0; the positive root is (-9+sqrt(129))/24. The remaining invariant subspaces give transition eigenvalues 0 (multiplicity two) and -1/4. Thus this positive quotient eigenvalue is the second largest, giving the claimed gap. The base second eigenspace is multiple, so the simple-eigenvector derivative is inapplicable.

## 8. Exhaustive computations and exact certification

[code/search.py](code/search.py) uses locally compiled nauty geng 2.9.3 (`geng -cq -dD -DD n`) to enumerate connected simple regular graphs up to isomorphism. The archive was read in memory, only source/text files were extracted, and no manual PDFs or images were retained. [data/nauty_provenance.json](data/nauty_provenance.json) records its URL and hash. Unused large vendor answer files were removed; the build sources, licence and compiler logs remain in code/vendor/nauty2_9_3.

For each graph every missing edge was evaluated. For matching runs the recursion pairs the smallest unused vertex with every allowed unused partner, so every perfect matching of the complement appears exactly once. Both edge and matching objectives are μ; multiplying all reported values by 1/2 gives the lazy gaps and does not change rankings. Matrix eigensolvers were used to find candidate optima; those optimum lists and ties are numerical to the stated tolerance, not certified global exact rankings for all graphs.

| d | n | Graphs | Edge candidates | Matching candidates | Raw edge failures | Corrected edge failures | Matching failures |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 3 | 6 | 2 | 12 | 2 | 0 | 0 | 0 |
| 3 | 8 | 5 | 80 | 74 | 0 | 0 | 0 |
| 3 | 10 | 19 | 570 | 2,754 | 1 | 1 | 6 |
| 3 | 12 | 85 | 4,080 | 146,038 | 9 | 9 | 58 |
| 3 | 14 | 509 | 35,630 | 11,946,770 | 109 | 109 | 470 |
| 3 | 16 | 4,060 | 389,760 | not run | 1,426 | 1,426 | not run |
| 4 | 6 | 1 | 3 | 1 | 0 | 0 | 0 |
| 4 | 8 | 6 | 72 | 41 | 0 | 0 | 1 |
| 4 | 10 | 59 | 1,475 | 3,828 | 2 | 2 | 27 |
| 4 | 12 | 1,544 | 64,848 | 1,263,912 | 269 | 269 | 1,185 |
| total | | 6,290 | 496,530 | 13,363,420 | 1,816 | 1,816 | 1,747 |

There are 6,191 simple-gap and 99 multiple-gap base graphs. Scalar-heuristic comparisons are made only for simple gaps; multiple cases are explicitly marked. In these censuses the raw and corrected edge rules happened to have the same maximizing candidate sets. This is an observation, not a theorem equating the rules.

A reported failure means that **all** exact maximizers of the relevant scalar score lose to an eligible witness. Ties are handled as sets, giving the heuristic its most favorable tie break. Individual unlucky tie choices are recorded numerically as `any_choice_loses` but are not counted as failures of this set-valued rule. Numerical score/gap tolerances are 10^-9 for comparisons (10^-10 for matching score accumulation). Near-tie optimum lists should be treated at that resolution.

Every one of the 5,379 reported failures has an exact certificate in [data/failure_certificates.jsonl](data/failure_certificates.jsonl): 3,632 edge records (the two rules separately) and 1,747 matching records. No certificate was left unresolved. A winner is a strict better witness; it need not itself be proved globally optimal to refute the heuristic.

The certificate construction and verification are [code/certify.py](code/certify.py). Its rigorous argument is as follows.

1. Integer fraction-free symmetric elimination computes inertia of qL-pD at a rational threshold p/q. All leading principal minors are nonzero for the saved thresholds. Signs of consecutive principal-minor ratios are LDL pivot signs; Sylvester's law gives the exact number of eigenvalues below p/q. Divisions are asserted exact. For every augmented comparison the witness has exactly one eigenvalue below the separator (only zero), while every possible heuristic choice has at least two. Hence the witness gap is strictly larger.
2. Three rational thresholds isolate the original λ_2(L) and put a lower bound on λ_3(L). A stored rational vector q, obtained by rounding an exploratory eigenvector to denominator 2^45, is checked entirely rationally. If c is the midpoint of the λ_2 interval and η a lower bound on its distance to every other original eigenvalue, the residual estimate

       ||(L-cI)q||² ≤ δ²η²

   implies that q differs by at most δ in Euclidean norm from its projection f onto the exact one-dimensional Fiedler eigenspace. The recorded norm bounds ensure f≠0. Its scale is immaterial for score comparisons.
3. Rational interval arithmetic using q_i±δ and the isolated μ interval encloses every raw/corrected edge score. Every true score maximizer lies in the saved candidate superset. For matchings, ||L_M||=2 and ||q||<2 give the uniform score error at most 8δ+2δ²; exact integer squared-difference sums then enumerate a superset of all true matching-score maximizers. The inertia comparison defeats every member of the superset. Thus numerical ordering of eigenvector coordinates is not being assumed exact.
4. The replay regenerates candidate supersets, checks eligibility of added pairs, recomputes the exact rational residual inequalities and all integer inertias. It reproduced all 5,379 certificates. An additional audit checked equality between the set of observed failure keys and certificate keys, graph degrees/connectivity/census sizes, and 10 independent lazy-transition eigenvalue calculations. Exact rational characteristic-polynomial root isolation independently checked both example comparisons in §7.

The census, graphs and every edge score/gap are in data/search_d*_n*.jsonl and data/graphs_d*_n*.g6. Matching records include total count, numerical best values/matchings, and maximizing heuristic choices; the full lists of millions of losing matchings are reproducibly generated rather than all retained. Summary files record elapsed time, nice level and peak RSS. The cubic n=14 run used about 146 MB peak RSS; the quartic n=12 run about 80 MB. All runs inherited nice 15 (lower priority than nice 10); trying `nice -n 10` was denied because that would raise priority on this Mac. Numerical libraries were restricted to one thread. No subagents, pushes or publication were used.

## 9. Additional exhaustive cycle/torus examples

[code/families.py](code/families.py) exhausts complement matchings for the following labeled families. These counts are separate from, and may overlap, the regular-graph census. The base gaps are multiple; no arbitrary scalar-vector heuristic is claimed canonical for these runs. Numerical maxima and representative matchings, not full global exact certificates, are in data/family_*.json.

| Base | Number of eligible matchings | Largest computed normalized gap |
|---|---:|---:|
| C_4 | 1 | 1.333333333333 |
| C_6 | 4 | 1.000000000000 |
| C_8 | 31 | 0.666666666667 |
| C_10 | 293 | 0.479482395730 |
| C_12 | 3,326 | 0.489303704587 |
| C_14 | 44,189 | 0.528595479209 |
| C_16 | 673,471 | 0.422649730810 |
| C_3 □ C_4 | 824 | 0.800000000000 |
| C_4 □ C_4 | 187,249 | 0.800000000000 |

For example, the antipodal matching on C_10 gives (2-2cos(2π/5))/3≈0.460655, strictly below the computed best ≈0.479482. Proposition 7 already supplies a proof of asymptotic suboptimality without depending on these numerical tables.

The analytic checks in [code/check_proofs.py](code/check_proofs.py) also tested 496 cycle chords through n=64, antipodal matchings at 31 sizes, seven matching-bound equality cases and the first/second derivative formulas against local finite differences. These are sanity checks; the proofs above are the justification.

## 10. Reproduction and limits

The environment has Python 3, numpy, scipy, sympy, networkx and pypdf. Run from this directory with OPENBLAS_NUM_THREADS=1, OMP_NUM_THREADS=1 and VECLIB_MAXIMUM_THREADS=1, at nice at least 10. The inherited priority was 15.

    code/vendor/nauty2_9_3/geng -cq -d3 -D3 12
    python3 code/search.py --d 3 --n 12 --matching
    python3 code/certify.py
    python3 code/certify.py --verify
    python3 code/audit.py
    python3 code/families.py
    python3 code/check_proofs.py

Other completed n,d combinations are listed in §8. The exact verifier performs no floating-point acceptance tests; numpy is used only during exploratory certificate generation. Fetching sources with code/fetch_sources.py retains only extracted text and provenance, never PDF bytes on disk.

Unfinished parts are substantive: an exact fastest-matching characterization for arbitrary regular graphs; sharp single-edge extremal improvement as a function of n,d; sharp universal TV improvement/slowdown under one edge or one matching; exact optimal matchings for all cycles/tori; and a complete matching census for cubic n=16 or quartic n≥14. The numerical global optimizer lists have not all been converted into exact optimality certificates. These omissions are why the status is PARTIAL, despite the proved local formulas, sharp matching comparisons, cycle results and fully certified heuristic failures.

Task: “Open problem E0095” — received/start recorded 2026-11-13 07:07 +04:00 (Asia/Tbilisi); the chat did not expose a separate user-message clock timestamp.
