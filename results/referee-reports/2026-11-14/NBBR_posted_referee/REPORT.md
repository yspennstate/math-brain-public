# Referee report

15 November 2026, Asia/Tbilisi. Manuscript: `claim_files/paper/main.tex`. Line numbers below refer to the supplied files, which were not edited.

Overall verdict: MINOR. The theorem and both corollaries follow from the propositions as written. I found no counterexample to a lemma, no failure of excursion reversal, and no missing multiplicity factor in transport. Two minor corrections concern the degree-ratio remark and the numerical threshold field. The script also cites the wrong theorem number. Literature-search limitations are recorded below.

## Verdicts

| Item | Verdict | Location |
|---|---|---|
| Sources as quoted | SOUND | main.tex:54–75 |
| Section 2, lem:derangement | SOUND | 143–152 |
| Section 2, lem:simple | SOUND | 154–167 |
| Section 3, lem:certified | SOUND | 190–202 |
| Section 3, lem:nonreturning | SOUND | 204–221 |
| Section 3, lem:terminal | SOUND | 223–231 |
| Section 3, lem:reversal | SOUND | 233–275 |
| prop:certified | SOUND | 277–304 |
| prop:flow | SOUND | 308–335 |
| Theorem thm:main | SOUND | 82–88, 339–355 |
| Corollary cor:constants | SOUND | 93–102, 357–361 |
| Corollary cor:expectation | SOUND | 104–114, 363–373 |
| Remark rem:ratio | MINOR | 375–385 |
| Numerics | MINOR | check_bound.py:3,6,11,132,138 |
| Bibliography | SOUND | main.tex:457–474 |
| Novelty | SOUND, within the search coverage below | main.tex:100–114,382 |

## 1. Source statements and hypotheses

The five research papers were downloaded from arXiv and converted with `pdftotext -layout`. The PDFs, extracted texts and metadata receipts are in `audit/sources/`. The extracted-text line numbers below are reproducible with `nl -ba`. Short quoted fragments are verbatim; the complete passages are available in those extracted texts.

Dozier's current record is [arXiv:2608.26321v1](https://arxiv.org/abs/2608.26321), submitted 26 August 2026. In `dozier.txt:29` he restricts to graphs “without multiple edges or self-loops”. At lines 29–30 he also specifies that edges carry orientations. There is no connectedness assumption. Theorem 1.1, lines 35–39, fixes d≥3 and gives C(d,ε), uniformly over graphs and starting directed edges. This matches main.tex:54–55.

Conjecture 1.5 is at `dozier.txt:65–69`. Its degree hypothesis is “all degrees at least 3”; its start is a walk “starting with δ”. Its mathematical content is: for every ε>0 there is C(ε) such that every simple n-vertex graph of minimum degree at least 3, every directed edge δ, and every integer k>C(ε)√n have p_k(δ)<ε. This is the statement at main.tex:58–61. Connectedness, regularity, or a bounded maximum degree are not hypotheses of the conjecture.

BGJ's current record is [arXiv:2608.09729v1](https://arxiv.org/abs/2608.09729), submitted 10 August 2026. Its setup at `bgj.txt:27–37` assumes a connected graph with minimum degree at least 3, starts at a specified vertex u, and makes the first neighbor “chosen uniformly”. The definition of T agrees with main.tex:64–66. The distinction between graphs and multigraphs is explicit at `bgj.txt:129–135`; ordinary graphs here are simple.

| Source passage | Verbatim fragment | Full mathematical content checked against the manuscript |
|---|---|---|
| BGJ Theorem 1, `bgj.txt:101–103` | “connected n-vertex graph” | Fixed Δ≥3, minimum degree ≥3, maximum degree Δ, any u; E T=O_Δ(√n log n). Saying maximum degree at most Δ is equivalent after adjusting the constant over finitely many smaller degree bounds. |
| BGJ Theorem 2, `bgj.txt:107–109` | “λ(G) ≤ ∆ − ε” | Fixed Δ≥3 and ε>0; connected Δ-regular graph; any u; E T=O_{Δ,ε}(√n). Here λ excludes both trivial eigenvalues ±Δ (`bgj.txt:86–88,493–503`), so bipartite graphs are included. |
| BGJ Theorem 3, `bgj.txt:118–121` | “prime congruent to 1 (mod 4)” | Δ=p+1 with this restriction on p; an increasing sequence of regular graphs; every vertex u; E T≥√n/6. The introduction identifies these as high-girth expanders. The manuscript's phrase about certain regular expanders is accurate. |
| BGJ Question 4, `bgj.txt:126–127` | “δ ≥ 3” | Whether every n-vertex graph of this minimum degree satisfies E T=O(√n), with an absolute implied constant. Connectedness is inherited from the setup; it does not affect the question's substance. |

The multigraph counterexample at `bgj.txt:129–135` uses 2^(k²) parallel edges between k and k+1. Its expected collision time from 1 is Θ(n). The manuscript describes this correctly.

The attribution in main.tex:74–75 is also correct: BGJ's Section 4 explicitly combines KMPT Theorem 3.6 with Lubetzky–Peres, including their Proposition 3.1 (`bgj.txt:485–491,509–520,689`). KMPT's current [arXiv:0712.0220v2](https://arxiv.org/abs/0712.0220) has the cited theorem at `kmpt.txt:608–624`. It concerns finite ergodic chains with uniform stationary distribution and includes a pre-mixing term; it is not a theorem about arbitrary NBWs without further hypotheses. The manuscript makes no such erroneous application.

Neither Dozier nor BGJ proves the bounded-degree-ratio case or the general conjecture. Dozier states only the fixed regular degree theorem. BGJ's general bounded-degree result retains log n, and their result without it assumes a regular expander.

## 2. Plans

At main.tex:133–137, each local map is a bijection between incoming and outgoing directed edges. Their union is therefore a permutation of the entire directed-edge set, including when the graph is disconnected or degrees differ. Fixed-point-freeness is exactly the local non-backtracking requirement for a simple graph.

At lines 144–151, conjugation by a permutation fixing a acts transitively on possible images b≠a and preserves derangements. Thus exactly R_d/(d−1) choices have π(a)=b. This uses each vertex's actual degree; it does not require a common R_d. Direct enumeration through degree 10 independently checked the counts.

At lines 159–163, a prescribed simple path imposes one condition at each of the distinct internal vertices. Under the product measure its mass is exactly ∏_{i=1}^{k−1}(d(y_i)−1)^(−1), which is also its NBW probability. These simple-path events are disjoint and exhaust S, giving μ(S)=p_k(δ), including k=1 and the empty case k≥n.

A random plan does not give the full infinite NBW law: after an incoming directed edge is revisited, its successor is fixed by the plan rather than freshly sampled. The stopped trajectory through the first repeated vertex does have the correct law. Lines 166–167 already state this restriction, and every subsequent use needs only the simple-path identity. No correction is required here.

## 3. Departures, line by line

The total departure weight in lines 172–179 is correct: there are d−2 allowed exits and each has weight 1/(d−1), so each internal index contributes at least 1/2 and less than 1.

For lem:certified, lines 197–200, changing the plan at x_i preserves the original prefix because it has no earlier occurrence of x_i. The excursion's internal vertices are outside P, so their local maps are unchanged, even if an internal vertex occurs repeatedly. Consequently the modified walk follows the excursion through its certified collision. The collision index is at most i+L, which is within the first k edges precisely when i≤k−L. The count of vertices in the lemma is consistent with this indexing.

For lem:nonreturning, lines 209–211, a non-certified excursion has distinct vertices, hence distinct directed edges. At lines 213–217, if two excursions shared an edge, injectivity allows backward propagation until one reaches the first departure edge. A strictly positive offset would place a vertex of P in the other excursion before its first return, a contradiction. Thus the excursions are edge-disjoint. They need not be vertex-disjoint; the proof only claims edge-disjointness. Lines 219–220 give

    total weight ≤ (sum_v d(v))/[L(m−1)] ≤ Qn/L.

This is valid for varying degrees.

For lem:terminal, lines 228–230, backward propagation from a common last edge works even for excursions with repeated vertices: the proper internal vertices remain outside P. Equality of last edges forces equal lengths and equal departure edges. There are at most d(x_k) possible last edges, giving weighted mass at most d(x_k)/(m−1)≤Q. No simplicity assumption on the excursion is needed.

For lem:reversal, lines 233–267, all inverted vertices lie outside P; thus the reversed plan remains in S with the same P. Inversion preserves both derangements and uniform plan mass.

At lines 256–258 the new departure is legal. For r≥2 its new neighbor is outside P and hence differs from both path neighbors. For r=1 an illegal new departure would imply that the original edge was a forbidden forward or backward path edge. A loop r=1 with l=i is impossible in a simple graph. Returns with l=i and r>1 cause no problem.

At lines 260–265, every original internal transition π_{y_s}(y_{s−1})=y_{s+1} becomes π_{y_s}^{−1}(y_{s+1})=y_{s−1}. This remains true when a vertex occurs more than once: a single inverse permutation simultaneously reverses every prescribed transition at that vertex. The reversed excursion has the same length, encounters P first at x_i, and cannot leave the defining set T. It has no backtrack at either end: its departure is legal, and it stops immediately upon return. Any later continuation would be governed by a derangement and would also forbid a backtrack.

At lines 266–267 the set of internal vertices is unchanged, so a second reversal inverts exactly the same maps and restores the original marked departure. This is an actual involution, including fixed points.

The weight ratio at lines 269–270 is exactly (d(x_l)−1)/(d(x_i)−1). Its maximum is (M−1)/(m−1)≤Q. At lines 272–274, a repeated outside vertex certifies both departures. Otherwise certification is l≤i in one direction and i≤l in the other, so at least one is certified. All three assertions hold.

For prop:certified, lines 288–292 cover every departure. The displayed classes can overlap among already certified departures, but this only enlarges the right side of the inequality. Uncertified interior returns are mapped injectively into certified interior returns by the involution. Their μ-weighted departure masses change by at most Q. Lines 294–300 correctly apply this after summing over all simple plans, yielding (1+Q)B≥(k−1)/2−Qn/L−Q. A planwise comparison between u and c would not follow; lines 303–304 correctly avoid it.

Computational attempts to break these claims are described in Section 6 below.

## 4. Transport

Lines 308–310 omit exactly L−1 possible indices when L<k. Each has total weight below 1, so B_0≥B−L is a valid weakening.

At lines 317–322, the mass μ(ρ)/R_d assigned to each allowable replacement is correct. There are R_d/(d−1) replacements, so the total mass for the chosen exit is μ(ρ)/(d−1). Equivalently, conditional on that exit, the replacement is uniform over its fiber, and the exit is assigned its NBW weight. The local resampling is not supposed to preserve the uniform measure after conditioning on a certified departure; conservation of the specified transport mass is what is required and what is proved.

For a fixed target ψ, let j be its first collision index. Every contributing source satisfies i<j≤i+L. There are at most L possible integers i. For a fixed i, the target determines the entire prefix, the departure edge β, and its own replacement σ. A source can differ only in one degree-d derangement, so at most R_d sources contribute. Every source has the same plan mass μ(ψ), despite irregular degrees, since the graph is fixed and the product ∏_v R_{d(v)} is constant over plans. Its contribution is μ(ψ)/R_d, so the incoming mass from that i is at most μ(ψ).

Thus the target receives at most Lμ(ψ); summing gives the stronger bound p_k B_0≤L(1−p_k)≤L. The number of possible excursion lengths introduces no extra factor: it is already controlled by the first-collision window for i. The same source/target pair cannot carry multiple departure labels at a fixed i because β is determined by ψ's next edge.

## 5. Theorem, constants, expectation and connectedness

At lines 340–342 the only nontrivial regime is k<n and k²≥256Q(1+Q)n. Since n>k, this implies k>256Q(1+Q), which is more than enough for k≥16(1+Q), Q≤k/16 and k≥4.

Put A=1+Q and L=ceil(16Qn/k). Then

    L ≤ k/(16A)+1 ≤ k/(8A) < k,
    Qn/L ≤ k/16,
    B ≥ [(k−1)/2−k/16−k/16]/A ≥ k/(4A),
    B_0 ≥ k/(8A).

The rounding inequality uses 1≤k/(16A), already established. Transport gives

    p_k ≤ 8AL/k ≤ 128AQn/k² + 8A/k ≤ 136AQn/k².

The last step uses k<n≤Qn. The stated 256 bound therefore holds, including equality at the regime boundary. If S is empty the claim is immediate. No division by μ(S)=0 is used.

The constants corollary follows from Q≤3D/2 and

    256Q(1+Q) ≤ 384D+576D² ≤ 960D² < (32D)².

For M≤Δ, Q≤Δ/2 gives 256Q(1+Q)≤64Δ(Δ+2), producing the coefficient 8. For a regular graph, Q=d/(d−1)≤3/2, so 256Q(1+Q)≤960<31²=961. The strict inequalities in k produce the stated strict probability bounds.

For expectation, P(τ>t)=p_t for every integer t≥1, and P(τ>0)=1. For H=256Q(1+Q)n and a=ceil√H,

    Eτ ≤ a+1+H sum_{t>a} t^(−2) ≤ a+1+H/a ≤ 2√H+2.

One way to check the last rounding step independently is to bound a≤√H+1 and H/a≤√H separately. The initial t=0 contribution is included; there is no lost time step. Conditioning on the first neighbor of u gives exactly the mixture of directed-edge starts, so the same bound applies to E T(G,u).

The two expectation constants are also correct:

    32 sqrt[Δ(Δ+2)/4] = 16 sqrt[Δ(Δ+2)],
    32 sqrt(960/256) D = 8 sqrt(60) D < 62D.

All counting and transport arguments operate on the entire directed-edge set without connectedness. Alternatively, restrict to the starting component: its minimum degree is at least m, its maximum degree at most M, and its order at most n, so its bound implies the displayed global bound. The first-step mixture also stays within that component.

Minor correction to rem:ratio, main.tex:380–381: the claim that each of the three losses is of order M on a graph with a few high-degree vertices and the remainder of degree three is too strong. The packing proof itself gives (sum_v d(v))/[L(m−1)]. With a bounded number h of hubs and all other degrees three, sum_v d(v)≤3n+hM≤(3+h)n, since M<n. Thus this packing estimate has no order-M loss. For a wheel on n vertices, m=3, M=n−1 and sum_v d(v)=4(n−1), giving packing weight at most 2(n−1)/L, rather than an intrinsic order-M penalty. Terminal mass and reversal can still carry order-M factors.

Fix lines 380–381 to say: the displayed worst-case bounds depend on M and this proof does not give a degree-independent estimate; the packing loss can instead be expressed through the average degree. This changes neither the theorem nor the stated unresolved scope. The multigraph observation in lines 383–384 is consistent with the source.

## 6. Independent numerical audit

All numerical work used one process and one computational thread at a time, with macOS background QoS set successfully. The sandbox denied `nice`; no priority elevation was used. Each job finished within 20 minutes, and measured peak memory stayed below 200 MB. Scripts and full results are retained in `audit/`. No language-model workers or subagents were started.

### Finite plans and transport

`audit/check_plans.py` enumerated every plan, directed start, simple prefix length 1≤k<n, and cutoff 1≤L≤2n on K4, the triangular prism, K3,3, and wheels with five and six vertices. These include irregular degree ranges 3–4 and 3–5. There were 1,696 plans and 1,304,832 simple-plan/start/k/L configurations.

For each configuration the checks covered excursion packing, terminal-edge injection, reversal legality, equal path and mass, exact reverse excursion, involutivity, certification, weight ratios, and the certified-weight proposition after summing over plans. Every possible allowed local resampling was checked. Incoming target mass was summed exactly as a rational number, both per index and across indices; total sent and received mass were equal. There were 6,250,144 certified resampling checks. The largest incoming mass from one index was 3μ(ψ)/4; the asserted upper bound is μ(ψ).

The enumerated cases included 2,688 excursions with repeated internal vertices and 329,376 unequal-degree reversals. A further 5,000 sampled plans on the 11-vertex wheel (m=3,M=10) and 2,000 on the 21-vertex wheel (m=3,M=20) tested larger degree discrepancies. These additional cases included 163 repeated-interior excursions and 8,530 unequal-degree reversals. No assertion failed.

Results are in `audit/plan_checks.json`; exhaustive and sampled stdout are preserved separately. The JSON's timing and RSS fields explicitly cover only the resumed sampled run. Two harness bookkeeping mistakes were corrected during development: checking an unrestricted certified collision only through time k, and referring to the exhaustive replacement table during sampled checks. Neither was a manuscript counterexample; all exhaustive results completed before the second error and were preserved.

`audit/check_derangements.py` independently enumerates local derangements through degree 10 and checks every image count, without storing all permutations. Its result is `audit/derangement_checks.json`.

### Exact survival probabilities

`audit/check_probability.py` uses a different DP from the supplied code. Its state is (visited-set, current-vertex); the previous vertex need not be stored, since every previously visited neighbor is forbidden in a surviving path. Let B=lcm_v(d(v)−1). Path masses at length k are accumulated as integers with denominator B^(k−1), so the returned probabilities and maxima are exact rational numbers, not Monte Carlo estimates or floating-point approximations.

Every starting directed edge and every feasible length was checked on 20 graphs: six random cubic graphs on 12 vertices; nine irregular 12-vertex graphs with m=3 and M respectively 4, 6 and 10; a wheel with M=10; Petersen; Heawood; a 12-vertex prism; and two disjoint K4 components. Graph edge lists and seeds are stored with the results.

Write R=max_{δ,k}p_k(δ)k²/n and R_Q=R/[Q(1+Q)]. Representative results are:

| Family | n | m,M | R | R_Q |
|---|---:|---|---:|---:|
| Largest tested cubic case | 12 | 3,3 | 2.25 = 9/4 | 0.6 = 3/5 |
| Heawood | 14 | 3,3 | 2.1875 | 0.583333333 |
| Irregular, cap 4, largest R | 12 | 3,4 | 1.851851852 | 0.308641975 |
| Irregular, cap 6, largest R | 12 | 3,6 | 1.759375 | 0.146614583 |
| Irregular, cap 10, largest R | 12 | 3,10 | 1.722559799 | 0.057418660 |
| Wheel | 11 | 3,10 | 1.231060606 | 0.041035354 |

The overall maximum R_Q is 3/5, compared with 256. The largest raw value occurs at δ=(1,11), k=6 in `cubic_0`, with p_6=3/4. Exact expectations were checked as 1+sum_{k≥1}p_k and also satisfy the corollary.

These small-graph comparisons cannot stress the nontrivial part of the 256 bound: on these orders its right side is already at least 1 whenever p_k can be nonzero. Their role is to check laws, arithmetic and implementation, together with the separate plan enumeration.

### Larger graphs and attempts to force large R

There were 70,000 Monte Carlo walks on seven graphs: random cubic graphs of orders 2,000 and 20,000; irregular 2,000-vertex graphs with m=3,M=6 and 10; a wheel of order 2,001 with one degree-2,000 hub; a 2,000-vertex cubic prism; and a chain of 500 K4 blocks joined by bridges, with minimum degree three. Each graph had two batches of 5,000 walks; the regular graphs and wheel used the same directed start in both batches. These are sampled-start results, not a maximum over all starts.

The largest empirical R_Q was 0.60027912 on the 20,000-vertex cubic graph; the corresponding empirical R was 2.2510467. The mean τ/√n on the cubic graphs was about 2.15–2.17. The respective maximum empirical raw ratios for the degree-6 and degree-10 irregular graphs were 1.1648 and 0.961722.

The high-degree hub, long narrow prism and chained dense blocks were attempts to delay collision without expanding the number of vertices. They did not produce large R. The wheel's empirical R was about 0.00227; the prism's about 0.0148; the block chain's about 0.00337. Local short cycles or repeated visits to the hub dominate. An additional 15,000 walks started along a rim edge of wheels with 201, 2,001 and 20,001 vertices, so the hub was initially unvisited. Mean collision times were 6.9648, 6.9886 and 7.018 steps; the respective empirical raw ratios were 0.09271, 0.009305 and 0.0009282. These checks are reproducible with `audit/check_hub_rim.py` and recorded in `audit/hub_rim_checks.json`, bringing the independent Monte Carlo total to 85,000 walks. No tested family suggests growth of R with Q. This does not establish that Q is unnecessary, and no necessity claim for Q should be inferred from these experiments. Monte Carlo maxima over k have sampling noise and selection bias; mean standard errors are saved in the JSON.

The independent probability suite took 50.997 seconds and peaked at 198,148,096 bytes RSS. Full results: `audit/probability_checks.json`.

### Supplied script and data

The supplied script was rerun unchanged from a copy in `audit/rerun/code/`, preserving the submitted JSON. Its newly generated JSON is identical, as parsed data, to `claim_files/data/bound_checks.json`. The rerun took 12.915 seconds and peaked at 44,662,784 bytes RSS. See `audit/rerun_comparison.json`.

The submitted maximum exact-DP raw ratio is 2.15625, and its Monte Carlo mean ratios are 1.40069–2.18687. Thus main.tex:415–416 accurately summarize those particular runs. Its DP uses double precision; the independent integer DP above provides rational checks on additional graphs.

Minor error, check_bound.py:132,138: `ceil(sqrt(h))+1` is a conservative threshold but is not always the first integer k for which h/k²<1. The first such integer is `floor(sqrt(h))+1`. The four non-null fields currently read 1387, 4383, 7840, 12395; they should read 1386, 4382, 7839, 12394. The reported zero-survivor counts are unchanged, since even the maximum sampled τ is below each corrected threshold. Fix the formula and regenerate the JSON, or rename the field to describe a conservative threshold.

Minor documentation error, check_bound.py:3,6,11: the main theorem is numbered 1.2 under the present amsart shared theorem counter, since Conjecture 1.1 precedes it. The comments call it Theorem 1.1. Fix those three references to 1.2, or refer to the main theorem without a number. The script's reference to Corollary 1.4 is consistent with the current numbering.

## 7. Bibliography and literature search

All entries were checked online on 15 November 2026 local time. There are eight bibliography entries, not only the five research references.

| Key | Verification |
|---|---|
| ABLS07 | Noga Alon, Itai Benjamini, Eyal Lubetzky, Sasha Sodin; title matches; Communications in Contemporary Mathematics 9(4), 585–603 (2007); DOI [10.1142/S0219199707002551](https://doi.org/10.1142/S0219199707002551). Crossref metadata and [arXiv:math/0610550](https://arxiv.org/abs/math/0610550) agree. |
| BGJ26 | Ferenc Bencs, Leslie Ann Goldberg, Matthew Jenssen, Mark Jerrum, Gábor Pete, Guus Regts, Yitong Yin; title and year match; [arXiv:2608.09729](https://arxiv.org/abs/2608.09729). No journal reference is supplied in the checked record, so the preprint citation is appropriate. |
| Doz26 | Benjamin Dozier; title matches apart from capitalization; 2026; [arXiv:2608.26321](https://arxiv.org/abs/2608.26321). The record remains a preprint. |
| KMPT10 | Jeong Han Kim, Ravi Montenegro, Yuval Peres, Prasad Tetali; title matches apart from capitalization; Annals of Applied Probability 20(2), 495–521 (2010); DOI [10.1214/09-AAP625](https://doi.org/10.1214/09-AAP625). Crossref and the arXiv journal reprint agree. |
| LP16 | Eyal Lubetzky and Yuval Peres; title matches; Geometric and Functional Analysis 26(4), 1190–1216 (2016); DOI [10.1007/s00039-016-0382-7](https://doi.org/10.1007/s00039-016-0382-7). Crossref, [arXiv:1507.04725](https://arxiv.org/abs/1507.04725), and the author's publication list agree. |
| MathBrainRepo | The [public repository](https://github.com/yspennstate/math-brain-public) exists under the cited owner, was created 24 October 2026, and contains the stated snapshot, code and tests. The citation uses a descriptive title; the README heading is Math research brain. |
| MathBrainPaper | The [linked paper directory](https://github.com/yspennstate/math-brain-public/tree/main/papers/math-brain-2026-10-24) exists. Its main.tex gives the cited title and author and the date 26 October 2026. The manuscript's month and year agree. |
| BrainFramework | The [public repository](https://github.com/yspennstate/brain-framework-public) exists, was created 5 November 2026, and identifies itself as Brain framework. Its year and software description agree. |

Metadata receipts are the three `*-crossref.json` files, the two main arXiv record HTML files, GitHub API receipts, and downloaded README/paper sources. Repository citations could be pinned to commits for reproducibility, but their current metadata are not false. Journal volume/issue/pages/DOI are inapplicable to the three software/paper repository entries; none are invented in the manuscript.

Searches included arXiv title/abstract queries for non-backtracking with birthday and with self-intersection, the unhyphenated spelling, and a submitted-date restriction from 1 January 2024 through the audit date. The date-filtered self-intersection query returned Dozier and BGJ. The birthday query additionally found Dozier–Sapir's earlier random-regular-loop paper, published in Journal of Graph Theory 105(4), 562–579 (2024), DOI [10.1002/jgt.23056](https://doi.org/10.1002/jgt.23056). Its [arXiv record](https://arxiv.org/abs/2209.11218) concerns typical random regular graphs and closed loops, not every graph or the bounded-ratio case. The source was also checked on the author's publication page.

Broader web queries used Alon–Peres, bounded degree ratio, birthday bound, and non-backtracking self-intersection with 2024–2026 restrictions. I found no independent paper proving the bounded-ratio case or the general conjecture. This is a search result, not a guarantee that no such work exists. BGJ's author's page still presents the general expectation question as a question; Dozier's current record still describes only the fixed-degree resolution.

Google Scholar was requested by curl with `as_ylo=2024` for both Alon/Peres and self-intersection queries. It returned a JavaScript session-verification page, not usable results. The saved receipts are `scholar-alon-peres.html` and `scholar-self-intersection.html`. Scholar therefore supplies no evidence for the novelty verdict.

The title search also found this same manuscript in the author's [public numerical repository](https://github.com/yspennstate/nonbacktracking-birthday-irregular), created 13 November 2026. Its main.tex is identical to the submitted manuscript after newline normalization (`audit/sources/self-repo-diff.txt` is empty). This is the same work, not an independent predecessor. A secondary index lists Zenodo DOI 10.5281/zenodo.24189686 for it; the Zenodo API returned HTTP 403, so I did not independently verify that record's metadata or date. No novelty conclusion relies on the index.

## Required corrections

1. main.tex:380–381: remove the assertion that all three actual losses are order M for a few hubs. State the average-degree packing bound and limit the claim to the displayed worst-case estimates.
2. check_bound.py:132,138 and the four affected data fields: use `floor(sqrt(h))+1` for a field described as the first nontrivial threshold, or rename the field. Regenerate the data if the formula is changed.
3. check_bound.py:3,6,11: change Theorem 1.1 to Theorem 1.2, or use the main theorem.

No change to the theorem's bound, the transport proposition, or either corollary is required by this audit.

Task: “You are an independent referee for a short combinatorial probability paper.” Received/start recorded 15 November 2026, 00:38 +04; full assignment completed in this folder.
