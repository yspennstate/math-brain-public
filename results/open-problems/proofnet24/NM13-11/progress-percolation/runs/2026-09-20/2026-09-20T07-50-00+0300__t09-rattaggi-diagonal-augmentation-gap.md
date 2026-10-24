Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

# NM13-11 / T09 — finite generator perturbations of a product-of-trees lattice; explicit Rattaggi fixed-graph gap

Status: **PARTIAL / CANDIDATE_FULL for the restricted theorem below; the universal T09 problem remains OPEN.** External priority of the exact fixed graph and perturbation criterion is **UNVERIFIED** after the bounded current search recorded below. The theorem argument is complete as a candidate but has not had independent review.

## 1. Original problem: before/after scope and gap

The frozen source problem is the Benjamini--Schramm Cayley-graph question for iid bond percolation:

> For every locally finite Cayley graph `G` of every finitely generated nonamenable group, prove `p_c(G)<p_u(G)`.

The universal parent remains **OPEN**.

### Before this run

NM13-11 had no certificate for the fixed Rattaggi Cayley graph introduced below, so its source-level quantitative metric was **UNMEASURED**, not zero. The latest own theorem instead treated specially engineered degree-9 Cayley graphs built from a `C_3 * Z` core and one involution, with a certified gap `>0.01053`, including an S-arithmetic application. Earlier own runs gave degree-34, degree-14 and degree-11 free-core/complement constructions.

### After this run

Let `Sigma` be Diego Rattaggi's explicit `(12,8)`-group from Example 3.4 of *A finitely presented torsion-free simple group* (J. Group Theory 10 (2007), 363--371). Let

`S0={a_1^{+-1},...,a_6^{+-1},b_1^{+-1},...,b_4^{+-1}}`.

Rattaggi's `(2m,2n)`-group construction identifies `Cay(Sigma,S0)` with `T_12 square T_8`. Choose any `k` new inverse pairs

`C={c_1^{+-1},...,c_k^{+-1}}`, `1<=k<=3`,

such that the `2k` new elements are pairwise distinct and disjoint from `S0`, and put

`G_C=Cay(Sigma,S0 union C)`.

Then the following uniform fixed-graph certificates hold:

- `k=1`: `p_c(G_C)<3/50` and `p_u(G_C)>819/10000`, hence
  `p_u-p_c>219/10000=0.0219`;
- `k=2`: `p_c(G_C)<3/50` and `p_u(G_C)>698/10000`, hence
  `p_u-p_c>49/5000=0.0098`;
- `k=3`: `p_c(G_C)<3/50` and `p_u(G_C)>609/10000`, hence
  `p_u-p_c>9/10000=0.0009`.

The proof actually uses only the `(12,8)`-group product Cayley structure and therefore applies verbatim to **every** `(12,8)`-group, not only Rattaggi's `Sigma`. Rattaggi's group is singled out because it gives a concrete virtually simple nonamenable ambient group outside the currently checked hyperbolic/acylindrically-hyperbolic all-Cayley scopes.

For an explicit non-standard perturbation take, for example,

`c_1=a_1 b_1`.

This edge joins vertices at standard-product distance two and creates the triangle

`1 --a_1--> a_1 --b_1--> a_1 b_1 --c_1^{-1}--> 1`,

so the new graph is certainly not the original tree product `T_12 square T_8`. The proof below does not use any qualitative product-percolation theorem for the augmented graph: it proves a new `p_c` comparison and an independent `p_u` operator lower bound on the augmented graph itself.

**Original-problem delta:** one previously UNMEASURED explicit fixed Cayley graph now has `p_u-p_c>0.0219`, and more generally up to three arbitrary added inverse pairs retain a certified positive gap.

**Mechanism delta:** the product-of-trees graph is used only as a spanning subgraph for `p_c`; a finite-radius fibre Galton--Watson construction gives a strict numerical upper bound `p_c<0.06`, while a nonbacktracking `l^2` bound survives arbitrary addition of up to three generator pairs. This is a perturbative stability theorem, not merely a product example.

## 2. Compact continuity handoff

Controlling policy is `operations/PROGRESS20_2026-09-20.md`; LIVE20 maps NM11 to T09 under `proofnet24/NM13-11/progress-percolation/`.

The June Benjamini--Schramm archive was preserved rather than restarted. In particular, the following already-attempted routes remain in the handoff from
`probability_campaign_2026_09/benjamini_schramm_attempt_2026_06/research/proof_strategy.md` and `open_status.md`:

- normalized finite-set escape and the BK finite-volume/last-exit decomposition;
- killed-SAW interior growth and susceptibility-weighted boundary energy;
- global `l^2` SAW growth;
- scalar nonbacktracking polynomial bounds and product stress tests;
- quotient/fibre-shell and fixed-endpoint bridge criteria.

Several of those were conditional because the percolation transfer was missing; tree/product calculations were later recognized as overlapping known qualitative product results. None is relabelled as source-level progress here.

The recent NM13-11 sequence then developed a load-bearing nonbacktracking transfer, first on a degree-34 `SL_3(Z)` graph and then through lower-degree free-core and triangle-fibre constructions. The immediate predecessor was the degree-9 `C_3*Z`/S-arithmetic theorem. This run changes route again: rather than engineer a free core, it starts from an explicit virtually simple lattice whose standard Cayley graph is exactly a tree product and proves that a finite **generator perturbation** keeps a strict gap.

A neighboring PROB10-09 route has already worked on unperturbed standard surface products; those are not counted as a new qualitative class here.

## 3. The group-theoretic fixed graph

Rattaggi's paper is available at
`https://www.rattaggi.ch/tsg2.pdf` (published as J. Group Theory 10 (2007), DOI `10.1515/JGT.2007.028`).

The preliminary `(2m,2n)`-group construction states that the defining square complex has universal cover

`T_{2m} square T_{2n}`,

that its fundamental group acts freely and transitively on the vertices, and that the group is torsion-free. Example 3.4 then defines

`Sigma=<a_1,...,a_6,b_1,...,b_4 | R_Sigma>`

as the corresponding `(12,8)`-group. Theorem 3.5 proves that the canonical index-four subgroup `Sigma_0` is finitely presented, torsion-free and simple.

The free and transitive vertex action identifies the standard Cayley graph with

`Cay(Sigma,S0) ~= T_12 square T_8`.

In particular it is 20-regular. If `C` consists of `k` pairwise-new inverse pairs then `G_C` is simple and `(20+2k)`-regular.

The group is nonamenable since its standard Cayley graph contains (indeed is) a product with a nonamenable regular-tree factor.

### Why this ambient group is outside the checked Choi--Seo all-Cayley class

This point is useful because a new numerical certificate on a graph whose entire group class was already known would not satisfy the present directive.

Rattaggi proves that `Sigma_0` is an infinite finitely generated simple normal subgroup of index four in `Sigma`. If `Sigma` were acylindrically hyperbolic, the standard normal-subgroup theorem for acylindrically hyperbolic groups would make the infinite normal subgroup `Sigma_0` acylindrically hyperbolic as well. But every acylindrically hyperbolic group is SQ-universal (Dahmani--Guirardel--Osin / Osin), and a finitely generated SQ-universal group has uncountably many non-isomorphic quotients, impossible for a simple group. Hence `Sigma` is not acylindrically hyperbolic.

Therefore Choi--Seo's 2025 theorem for every Cayley graph of an acylindrically hyperbolic group does not cover these graphs. Since a non-elementary hyperbolic group is acylindrically hyperbolic and `Sigma` is nonamenable/non-virtually-cyclic, Hutchcroft's hyperbolic theorem does not cover it either.

The **unperturbed** graph `Cay(Sigma,S0)` is a known Cartesian product and is not claimed as new. What is new in this run is the fixed augmented generating set and the direct perturbative transfer below. A bounded search did not locate a theorem asserting `p_c<p_u` for these finite diagonal/general generator augmentations of Rattaggi's product lattice. This is negative evidence only: exact external novelty remains **UNVERIFIED**.

## 4. `p_c` side: an exact finite-radius fibre Galton--Watson comparison

Everything in this section takes place inside the standard spanning subgraph

`T_12 square T_8 subset G_C`.

Thus any strict upper bound proved for the product also upper-bounds `p_c(G_C)`.

Root the `T_12` factor. Every non-root base vertex has 11 forward child fibres after discarding its unique parent direction. Suppose exploration reaches a fibre `{x} times T_8` at a single seed `(x,y)`. Inside this fibre expose only the open cluster of `y` in the radius-two ball of `T_8`; call its number of vertices `Z_2`.

For each of the 11 forward base children `x'` of `x`, inspect the 11-direction horizontal edges from every vertex of this truncated fibre cluster into the child fibre `{x'} times T_8`. Conditional on `Z_2`, the probability that at least one such edge is open is

`1-(1-p)^{Z_2}`.

Declare at most one child in each child fibre (choose a deterministic first successful edge if several are open). Different child fibres use disjoint horizontal edges. A child base vertex has a unique parent in the rooted `T_12`, and the internal radius-two edges in its fibre have not previously been exposed. Consequently these particles form a genuine one-type Galton--Watson process with offspring mean

`m(p)=11 E[1-(1-p)^{Z_2}]`.

This is an exact stochastic domination/subprocess construction, not a simulation.

Write `s=1-p`. The radius-two fibre pgf is elementary. For one outward branch of `T_8`, set

`h_0=s`,

`h_1=s(s+p h_0)^7`.

The root has eight branches, so

`E[s^{Z_2}]=C_2=s(s+p h_1)^8`.

At

`p_0=3/50`

the executed exact-rational checker verifies

`11(1-C_2)-1 > 1/15 > 0`.

Numerically the exact values are

`1-C_2 = 0.09699226173438381299041740788444212344397...`,

`m(p_0)=1.066914879078221942894591486728863357884...`.

Thus the embedded Galton--Watson process is supercritical at `p_0`. Since `m(p)` is a polynomial/continuous function of `p` and the inequality is strict, it remains supercritical at some `p<p_0`. Hence

`p_c(T_12 square T_8) < 3/50`,

and therefore for every augmentation considered here

`boxed(p_c(G_C)<3/50)`.

This strictness is important: the displayed final gaps are strict, not endpoint equalities.

## 5. `p_u` side: nonbacktracking operator transfer stable under added generators

I record the transfer completely because an auxiliary operator inequality without the percolation step does not count for T09.

Let `G` be a simple `D`-regular graph, `A` its adjacency operator, and suppose

`||A||_{2->2} <= a`.

Put `Q=D-1`. Let `N_n(x,y)` be the number of length-`n` nonbacktracking walks. Then

`N_0=I`, `N_1=A`, `N_2=A^2-DI`,

and for `n>=3`,

`N_n=A N_{n-1}-Q N_{n-2}`.

Spectral calculus for this recurrence gives

`limsup_n ||N_n||_{2->2}^{1/n} <= beta_D(a)`,

where

`beta_D(a)=sqrt(Q)` if `a<=2sqrt(Q)`, and otherwise

`beta_D(a)=(a+sqrt(a^2-4Q))/2`.

Every open connection contains a self-avoiding path and every self-avoiding path is nonbacktracking, so entrywise

`T_p(x,y)=P_p(x<->y) <= sum_{n>=0} p^n N_n(x,y)`.

If `p beta_D(a)<1`, the series on the right converges as an `l^2` operator. Positivity then gives `||T_p||_{2->2}<infinity`. Therefore

`p_{2->2}(G) >= beta_D(a)^{-1}`.

On an infinite Cayley graph, if `p>p_u`, uniqueness of the infinite cluster and FKG give

`T_p(x,y) >= P_p(x<->infinity,y<->infinity) >= theta(p)^2>0`.

A kernel bounded below by a positive constant on an infinite vertex set is not bounded on `l^2`; hence

`p_{2->2}(G) <= p_u(G)`.

This proves the actual percolation transfer

`p_u(G) >= p_{2->2}(G) >= beta_D(a)^{-1}`.

### Adjacency norm under `k` arbitrary added inverse pairs

For the standard product,

`||A_0|| = 2 sqrt(11)+2 sqrt(7)`.

Each added inverse pair contributes `R_c+R_{c^{-1}}`, whose operator norm is at most 2. Hence for `k` pairs

`||A_{G_C}|| <= 2 sqrt(11)+2 sqrt(7)+2k`.

The checker uses the exact rational upper bounds

`sqrt(11)<331663/100000`,

`sqrt(7)<264576/100000`,

whose squared slacks are respectively

`345569/10000000000 > 0`,

`449/9765625 > 0`.

Thus

`||A_{G_C}|| < 11.92478+2k`.

For each `k=1,2,3`, instead of evaluating the quadratic root with floating point, test a rational `z>sqrt(Q)` against the increasing function `z+Q/z`. If

`z+Q/z > a`,

then the larger recurrence root is `<z` and `p_{2->2}>1/z`.

The exact executed certificates are:

### `k=1`

`D=22`, `Q=21`, `a<13.92478`, `z=10000/819`.

`z+21/z-13.92478 = 52541/10237500 > 0`.

Therefore

`p_u>p_{2->2}>819/10000=0.0819`,

and with the strict `p_c<0.06`,

`boxed(p_u-p_c>219/10000=0.0219)`.

### `k=2`

`D=24`, `Q=23`, `a<15.92478`, `z=10000/698`.

`z+23/z-15.92478 = 126819/17450000 > 0`.

Therefore

`p_u>698/10000=0.0698`,

so

`boxed(p_u-p_c>49/5000=0.0098)`.

### `k=3`

`D=26`, `Q=25`, `a<17.92478`, `z=10000/609`.

`z+25/z-17.92478 = 275287/15225000 > 0`.

Therefore

`p_u>609/10000=0.0609`,

so

`boxed(p_u-p_c>9/10000=0.0009)`.

This is the advertised weakening: the new edges do **not** need to generate a free subgroup, preserve a fibre, have finite order, or satisfy any comparison relation. Up to three completely arbitrary new inverse pairs are allowed, provided they are genuinely new so that the displayed degree is correct.

The scalar estimate stops being sufficient at four arbitrary pairs: with the same `p_c<0.06` certificate its nonbacktracking floor drops below `0.06`. I therefore do not claim `k=4`; unknown is not zero.

## 6. Explicit diagonal member and what is / is not known already

Take `k=1` and `c_1=a_1 b_1`. Since the standard graph is `T_12 square T_8`, `c_1` is at standard-product distance two and is not one of the twenty standard generators. Torsion-freeness gives `c_1!=c_1^{-1}`. Thus the degree-22 graph is well-defined and has the `0.0219` gap above.

This graph is a finite generator perturbation of a known product graph. The old qualitative product theorem cannot simply be transferred through edge addition: `p_c` is monotone in the useful direction, but `p_u` does not inherit the required lower bound from a spanning subgraph. The whole point of Section 5 is to supply that missing transfer.

The diagonal edge creates triangles, so this graph is not the original bipartite tree product. I did **not** prove a full Cartesian-prime classification of the augmented graph in this run. The current novelty statement is therefore deliberately bounded: among the checked primary sources and repository history, I found no theorem covering this specific diagonal-generator perturbation, while the ambient group is rigorously outside the hyperbolic and acylindrically-hyperbolic all-Cayley classes. Exact worldwide priority remains **UNVERIFIED**.

## 7. Required current literature scopes, checked 2026-09-20

### Hutchcroft, arXiv:1804.10191

Current located version is `v3` (the repository's exact version check records revision 26 March 2019). The theorem proves iid bond-percolation `p_c<p_u` for connected locally finite **nonamenable Gromov-hyperbolic quasi-transitive graphs**. It is a genuine special-case proof of Benjamini--Schramm under hyperbolicity, not the universal Cayley theorem.

Source: `https://arxiv.org/abs/1804.10191`.

### Hutchcroft--Pan, arXiv:2409.12283

Current located version is `v1`, submitted 18 September 2024. It studies behavior **at `p_u`** using subgroup relativization. In particular it proves nonuniqueness at `p_u` for groups containing an amenable `wq`-normal subgroup of exponential growth and establishes a co-heredity framework for endpoint nonuniqueness. These are important endpoint results, but they do not by themselves give the fixed-graph strict inequality `p_c<p_u` proved here.

Source: `https://arxiv.org/abs/2409.12283`.

### Terlov--Timar, arXiv:2502.02560

Current located version is `v2`, revised 14 September 2025. It develops weighted/level amenability and proves a relaxed Pak--Smirnova-Nagnibeda-style statement involving the weighted threshold `p_h<p_u` in the nonunimodular/weighted setting. It is not the ordinary unimodular fixed-Cayley `p_c<p_u` theorem.

Source: `https://arxiv.org/abs/2502.02560`.

### Later essential scope check

Choi--Seo, arXiv:2508.08932 (2025), proves a nonuniqueness phase for **every Cayley graph of every acylindrically hyperbolic group**. This is a major later enlargement and must be excluded before claiming a new class. Section 3 gives the reason Rattaggi's `Sigma` is not acylindrically hyperbolic.

A bounded current search on 20 September 2026 did not locate a primary source resolving the universal nonamenable-Cayley problem, nor one treating the exact finite-generator perturbation theorem above. That is bounded negative evidence only.

## 8. Exact checker and archived output

The final load-bearing checker is

`proofnet24/NM13-11/progress-percolation/runs/2026-09-20/2026-09-20T07-50-00+0300__t09-rattaggi-k123-gap-check.py`

created at commit

`7efeaf17d280c8d051a5f07be55adc7a5b86e515`.

Its actually executed exact output is archived as

`proofnet24/NM13-11/progress-percolation/runs/2026-09-20/2026-09-20T07-50-00+0300__t09-rattaggi-k123-gap-check.out`

at commit

`5d873e5caf735f46b2a7ff2b6722536c4f692436`.

It ends

`ALL_EXACT_CHECKS_PASS`.

A preliminary one-pair checker was also created earlier in the same run at commit `b4e00d0d9dafb63c8bfccc97da10ea9e9dee488c`, with output commit `0766e8498a1bf2f69978faf78f7d9e7bcda56831`; it is superseded by the `k<=3` checker and is not the final certificate.

## 9. Failure boundary and next substantive move

The current coarse perturbation theorem fails to certify four arbitrary added inverse pairs: the adjacency-norm penalty `+2k` pushes the nonbacktracking floor below the present strict `p_c<0.06` fibre certificate. The infinite-depth version of the same fibre branching mechanism numerically approaches a threshold around `0.0553`, still not enough to beat the crude `k=4` scalar operator floor; this numerical observation is diagnostic only and is not used as a theorem.

A materially new next method is therefore required rather than deeper fibre polishing: retain the exact product-of-trees decomposition and build a **colored nonbacktracking operator** that distinguishes standard horizontal, standard vertical and added-generator edges. The scalar triangle inequality loses all cancellation/transition information and is precisely the obstruction at `k=4`. A successful colored recurrence could permit larger finite perturbations and move the theorem toward natural fixed generating sets.

## 10. ledger_delta

```yaml
ledger_delta:
  task: T09
  worker: NM13-11
  namespace: proofnet24/NM13-11/progress-percolation
  source_problem: "For every locally finite Cayley graph of a finitely generated nonamenable group, prove iid bond percolation p_c(G)<p_u(G)."
  universal_status: OPEN
  restricted_status: PARTIAL
  theorem_label: CANDIDATE_FULL_RESTRICTED_AWAITING_INDEPENDENT_REVIEW
  source_level_before:
    graph: "Rattaggi Sigma with standard generators plus diagonal c=a1*b1"
    metric: "certified lower bound on p_u-p_c"
    value: UNMEASURED
  source_level_after:
    graph: "Cay(Sigma,S0 union {c,c^-1}), c=a1*b1"
    pc_upper: "<3/50"
    pu_lower: ">819/10000"
    gap_lower: ">219/10000 = 0.0219"
  weakened_class:
    hypothesis: "any (12,8)-group standard product Cayley graph plus k arbitrary genuinely-new inverse generator pairs"
    k1_gap: ">219/10000"
    k2_gap: ">49/5000"
    k3_gap: ">9/10000"
    k4: "UNKNOWN by this method; no zero assigned"
  demonstrated_mechanism:
    pc: "exact radius-2 T8-fibre Galton-Watson subprocess inside T12 x T8"
    pu: "adjacency norm under finite generator perturbation + nonbacktracking l2 transfer + p_2to2<=p_u"
  prior_history_preserved:
    - finite_set_escape_BK_boundary
    - killed_SAW_and_boundary_energy
    - global_l2_SAW
    - quotient_fibre_shell
    - bridge_criteria
    - earlier_free_core_nonbacktracking_runs
    - earlier_triangle_fibre_degree9_runs
  checked_scope_exclusions:
    - "1804.10191: hyperbolic quasi-transitive"
    - "2409.12283: endpoint p_u subgroup relativization"
    - "2502.02560: weighted/level amenability and relaxed p_h<p_u"
    - "2508.08932: all Cayley graphs of acylindrically hyperbolic groups; Rattaggi Sigma excluded by virtual simplicity + AH normal-subgroup/SQ-universality facts"
  external_priority: "UNVERIFIED after bounded current search"
  checker: "proofnet24/NM13-11/progress-percolation/runs/2026-09-20/2026-09-20T07-50-00+0300__t09-rattaggi-k123-gap-check.py"
  checker_commit: "7efeaf17d280c8d051a5f07be55adc7a5b86e515"
  output: "proofnet24/NM13-11/progress-percolation/runs/2026-09-20/2026-09-20T07-50-00+0300__t09-rattaggi-k123-gap-check.out"
  output_commit: "5d873e5caf735f46b2a7ff2b6722536c4f692436"
  unchanged_substantive_runs: 0
  failed_recoveries: 0
  next_attack: "colored nonbacktracking recurrence for standard horizontal/vertical versus added edges, targeting k>=4 and less engineered fixed generating sets"
```
