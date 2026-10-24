Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED.** GPT-6 / maximum was requested in prompt text, but the exposed runtime provides no authenticated model-family selector or reasoning-effort selector, so I do not claim otherwise. **NO MOVEMENT: `n_recon^cert: 13 -> 13`; I0126 unchanged count `1 -> 2`. Methods this run: #6 DEFORM TO A POINT YOU CAN SOLVE, #12 FIND WHAT IS CONSERVED, #24 FIND THE EXTREMAL OBJECT.**

# P03 HARD OUTSIDE — I0126 conserved extension profiles and threshold-card rigidity

Run date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.  
Current claim: `operations/claims/I0126.md`, creation commit `a8a6793fc851824ab1e85568ab729e3c52291fda`, blob `7bc60b5449d3cef5b461da8b635f57d6c9fb963c`.  
Predecessor report: `proofnet24/P03-fei/runs/2026-09-17/2026-09-17T15-38-30Z__i0074-scope-resolution-i0126-admission.md`, creation commit `25c9ad0d6fc6b4cc088adab804328c0673bd3a49`, blob `9afeb6a965f252f2a9888de6fc0b6196ba015946`.

## 1. Metric and source status

The frozen source-matching metric remains

`n_recon^cert` = the largest integer `n` for which every finite simple graph on at most `n` vertices is rigorously known reconstructible from its full vertex deck.

Before / after:

`n_recon^cert: 13 -> 13` — **NO MOVEMENT**.

The supported baseline remains Brendan D. McKay, *Reconstruction of Small Graphs and Digraphs*, Australasian Journal of Combinatorics 83 (2022), arXiv:2102.01942v4, proving reconstruction (and set reconstruction) for all graphs through 13 vertices and restricted classes beyond 13.

The unrestricted Kelly--Ulam conjecture remains **OPEN / PARTIAL** in the checked 2026 record. Emilie Dufresne, Gabriela Jeronimo, Jenny Kenkel, Haydee Lindo and Nelly Villamizar, *Shuffling the Deck: Invariant Theory and the Graph Reconstruction Conjecture*, arXiv:2604.16567v1 (17 Apr 2026), still states the full conjecture and develops an invariant-theoretic reformulation rather than a resolution. J. Antony Aravind and S. Monikandan, arXiv:2601.00620v1 (2 Jan 2026), likewise state the conjecture and prove the reduction used below.

A fresh bounded 2026-09-17 search recovered no accepted full proof or counterexample after those sources. This is dated negative search evidence only, not a novelty certificate.

## 2. Repository continuity

Before the mathematical attack I reread or recovered by exact path / exact ID the root `README.md`, `proofnet24/HOURLY_PROTOCOL_2026-09-15.md`, `FLEET_RULES.md` / NEW-METHODS controls, `operations/FLEET_2026-09-16.md`, campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the current I0126 claim, the complete predecessor report, the R09 I0126 admission screen, repository-wide I0126 search results, and the P04/I0101 report used for the directed audit.

Large shared ledgers and the intake corpus are connector-truncated when rendered wholesale. I therefore used exact-path and exact-ID reads and do **not** claim a byte-for-byte visible reread of every intake row. No shared root, peer file, prior P03 report, or historical handoff was edited.

The predecessor theorem remains in force:

`P03-I0126-EXTENSION-COLLISION-247 = PROVED / EXACT-REFORMULATION / PARTIAL / PUBLICATION-NOVELTY-UNVERIFIED`.

For an `(n-1)`-vertex graph `C` and `A subseteq V(C)`, let `G_A` be the graph obtained by adjoining a new vertex `z` adjacent exactly to `A`. Then reconstruction fails at order `n` iff some `C,A,B` satisfy `G_A not~= G_B` but `D(G_A)=D(G_B)`. Every such collision has `|A|=|B|`, and `A,B` in the same `Aut(C)` orbit yield isomorphic extensions.

## 3. New idea before code and refutation-first target

The order-14 problem is not attacked by enumerating all 13-vertex bases. Instead, try to force any extension collision through invariants that are already visible in the common deck.

The first proposed strong statement was deliberately adversarial:

> perhaps equality of decks already forces the added neighborhoods `A,B` to lie in the same `Aut(C)` orbit once one remembers the degree classes and the lowest subgraph moments.

This turns the problem into a conserved-profile question and immediately interacts with the requested `gamma(G)=2` route: a dominating pair containing the deleted/new vertex forces a large, explicitly described part of `A`.

I first derived the exact conserved profile, then tried to falsify its orbit-separation power before using it. The falsification succeeds on a five-vertex base (Section 6), so the profile is a necessary invariant, not a universal reconstruction theorem. The useful deformation is then to bases for which degree classes are genuine twin classes. Threshold graphs are exactly such a broad solvable family, and that yields a uniform common-card rigidity theorem.

No code was required for the theorem or the route-kill; no checker was manufactured merely to produce a receipt.

## 4. #12 FIND WHAT IS CONSERVED — exact extension-profile theorem

Let `C` have vertex-degree classes

`V_d(C)={v in V(C): deg_C(v)=d}`.

For `A subseteq V(C)`, define

`a_d(A)=|A intersect V_d(C)|`.

Also define

`e_C(A)=|E(C[A])|`

and

`q_C(A)=sum_{w in V(C)} binom(|N_C(w) intersect A|,2)`.

The quantity `q_C(A)` is exactly the number of (not necessarily induced) 4-cycles of `G_A` that contain the new vertex `z`.

### Claim 249

**`P03-I0126-DEGREE-PROFILE-THRESHOLD-RIGIDITY-249 = PROVED / STRUCTURAL-PARTIAL / PUBLICATION-NOVELTY-UNVERIFIED`.**

If `D(G_A)=D(G_B)` for two one-vertex extensions of the same base `C`, then:

1. `|A|=|B|` (retained from Claim 247);
2. for every integer `d`,
   `a_d(A)=a_d(B)`;
3. `e_C(A)=e_C(B)`;
4. `q_C(A)=q_C(B)`.

Moreover, if `C` is a threshold graph, then these equal decks already imply

`G_A ~= G_B`.

Equivalently, **no nonisomorphic hypomorphic pair can have a threshold graph as a common card.**

### Proof, part I: the full degree-class occupancy vector is conserved

A vertex deck reconstructs the parent degree multiset directly. If `G` has `n` vertices and `m` edges, then

`sum_{v in V(G)} |E(G-v)| = (n-2)m`,

so `m` is determined by the deck; and the degree of the deleted vertex on a card `G-v` is

`deg_G(v)=m-|E(G-v)|`.

Thus equal decks have equal parent degree sequences.

Let

`n_d=|V_d(C)|`, `a_d=|A intersect V_d(C)|`, `b_d=|B intersect V_d(C)|`,

and put `k=|A|=|B|` by Claim 247. In `G_A`, an old base vertex of degree `d` keeps degree `d` if it is outside `A` and becomes degree `d+1` if it lies in `A`. Therefore the number of vertices of degree `r` in the parent `G_A` is

`n_r-a_r+a_{r-1}+1_{r=k}`,

where `a_{-1}=0`, and the final indicator is the new vertex `z`. For `G_B` the same formula is

`n_r-b_r+b_{r-1}+1_{r=k}`.

Equality of parent degree sequences gives

`a_r-b_r = a_{r-1}-b_{r-1}`

for every `r`. Starting from `a_{-1}-b_{-1}=0` and inducting upward yields

`a_r=b_r`

for every degree `r`.

This is stronger than the previously recorded scalar constraint `|A|=|B|`: a collision must choose the same number of neighbors from **every base-degree class**.

### Proof, part II: the first two intersection moments are conserved

For any fixed graph `F` on `h<n` vertices, its number of (not necessarily induced) copies is reconstructible from the deck by the elementary Kelly count

`N_F(G) = (1/(n-h)) sum_v N_F(G-v)`,

because each copy survives exactly the deletions of the `n-h` vertices outside it.

Take `F=K_3`. Every triangle of `G_A` either lies entirely in `C` or contains `z`. The triangles containing `z` correspond exactly to edges with both endpoints in `A`. Hence

`N_{K3}(G_A)=N_{K3}(C)+e_C(A)`.

Equal decks give equal triangle counts, and the base term is common, so

`e_C(A)=e_C(B)`.

Now take `F=C_4`. A 4-cycle of `G_A` containing `z` has a unique opposite vertex `w in C`. Its other two vertices are an unordered pair of distinct members of `N_C(w) intersect A`. Conversely every such choice gives a 4-cycle through `z` (chords do not matter because these are ordinary subgraph copies, not induced copies). Therefore

`N_{C4}(G_A)=N_{C4}(C)+sum_w binom(|N_C(w) intersect A|,2)`

and equal decks yield

`q_C(A)=q_C(B)`.

### Proof, part III: threshold bases are collision-rigid

Use the standard weight characterization of a threshold graph: there are real weights `w(v)` and a threshold `T` such that for distinct `u,v`, adjacency is determined by whether `w(u)+w(v)` crosses `T`.

If `u,v` have the same degree and, say, `w(u)<=w(v)`, then for every third vertex `x`,

`ux in E(C) => vx in E(C)`.

Hence

`N_C(u)\{v} subseteq N_C(v)\{u}`.

The two vertices have equal degrees, while the edge `uv` contributes symmetrically to both degree counts, so the two external neighborhoods have equal cardinality. The inclusion is therefore equality. Thus any two vertices in the same degree class are twins, and their transposition fixes all other vertices and is an automorphism of `C`.

Consequently the full symmetric group on each degree class acts by automorphisms. Since Part I gives

`|A intersect V_d(C)|=|B intersect V_d(C)|`

for every `d`, choose independently within each degree class a permutation sending the selected vertices of `A` to the selected vertices of `B`. The product of those classwise permutations is an automorphism `sigma of C` with

`sigma(A)=B`.

Extending `sigma` by fixing the new vertex gives an isomorphism

`G_A ~= G_B`.

This proves Claim 249. QED.

### Scope and novelty label

The conservation identities are elementary consequences of the deck and are plausibly implicit in the classical hypomorphism/Kelly-count literature. Threshold graphs themselves are highly structured and reconstructible. The point used here is the stronger **common-card** statement: a threshold card cannot serve as the shared `(n-1)`-vertex base of a nonisomorphic hypomorphic pair. A bounded search (`"common card" threshold graph reconstruction`, `"one vertex extension" threshold graph reconstruction`) did not locate this exact formulation, but that search miss does not establish publication novelty. Claim 249 therefore remains `PUBLICATION-NOVELTY-UNVERIFIED`.

The nearby 2023 paper by Sciriha--Borg, *Reconstruction from one labelled card and more*, is relevant prior art on reconstructing from a common/labelled card plus extra invariants and is not silently treated as absent.

## 5. #6 DEFORM TO A POINT YOU CAN SOLVE — antiregular common cards are impossible

The most degree-separated possible `m`-vertex graph has exactly `m-1` distinct degree values; such graphs are antiregular. They form the extremal end of the threshold family, but the needed fact can also be proved recursively from scratch.

### Lemma: antiregular graphs are threshold and their repeated-degree pair is a twin pair

Let `C` have `m>=2` vertices and `m-1` distinct degree values. A graph cannot simultaneously contain a vertex of degree `0` and a vertex of degree `m-1`. Since the degree set has size `m-1` inside `{0,...,m-1}`, it must therefore be exactly one of

`{0,1,...,m-2}` or `{1,2,...,m-1}`.

In the first case the isolated vertex is unique: if two vertices were isolated, a required degree-`m-2` vertex would have at least two non-neighbors. In the second case the universal vertex is unique: if two vertices were universal, a required degree-1 vertex would have degree at least two.

Remove that unique isolated or universal vertex. The remaining graph again has one fewer vertex and one fewer distinct degree value, hence is antiregular. Induction constructs `C` by successive additions of isolated or universal vertices, so `C` is threshold.

The same induction shows that the unique repeated-degree pair are twins: the pair survives removal of the unique extreme vertex, is a twin pair inductively, and adding an isolated or universal vertex treats both members identically. Thus their transposition fixes every other vertex.

### Order-14 corollary

A 13-vertex card can have at most 12 distinct degrees. If it has all 12, it is antiregular and hence threshold, so Claim 249 rules out using it as a common card of a reconstruction counterexample.

Therefore:

> **Any order-14 reconstruction counterexample would have every one of its common 13-vertex cards carrying at most 11 distinct degree values.**

This is a concrete extremal exclusion at the first unverified order. It does not prove order 14, so `n_recon^cert` stays 13.

## 6. Refutation-first check: the conserved profile does not separate arbitrary bases

It would be false to infer from Part I--II that equal conserved profiles force `A,B` into the same `Aut(C)` orbit for a general base.

Take

`C = P_3 disjoint_union K_2`,

with path vertices `0-1-2` and edge `3-4`. Let

`A={0}`, `B={3}`.

Vertices `0` and `3` both have base degree one, so the full degree-class occupancy vectors of `A,B` coincide. Both induced subgraphs `C[A]`, `C[B]` have zero edges, and because the sets are singletons,

`q_C(A)=q_C(B)=0`.

Yet `0` and `3` are not in the same automorphism orbit: they lie in nonisomorphic connected components. The extensions are visibly nonisomorphic:

`G_A = P_4 disjoint_union K_2`,

whereas

`G_B = P_3 disjoint_union P_3`.

This is **not** a reconstruction counterexample; their full decks differ. It is an exact route-kill showing that degree occupancy plus the first two subgraph moments are necessary but not sufficient to force an extension orbit on an arbitrary base.

The threshold theorem succeeds precisely because equal-degree classes become twin modules, eliminating this component/orbit ambiguity.

## 7. First attack on the `gamma(G)=2` reduced parent class

Aravind--Monikandan Theorem 7 (2026) proves that the full Reconstruction Conjecture is equivalent to reconstruction of the 2-connected graphs satisfying either

- `gamma(G)=2`, or
- `diam(G)=diam(complement G)=2`.

Their paper also proves that the class `gamma(G)=2` is recognizable from the deck, but explicitly leaves weak reconstruction of connected `gamma=2` graphs as an open problem. Thus it is legitimate prior art to restrict a hypothetical order-14 counterexample to this class, but not to assume that a dominating pair itself is canonically marked by the deck.

Let `G_A` be an extension of `C` and suppose the **new vertex** `z` belongs to a dominating pair `{z,w}`. Define the anti-neighborhood of `w` inside the base

`R_C(w)=V(C) \ (N_C(w) union {w})`.

Every vertex of `R_C(w)` is not adjacent to `w`, so domination by `{z,w}` forces it to be adjacent to `z`. Therefore

`R_C(w) subseteq A`.

Write

`e=1_{w in A}`, `S=A intersect N_C(w)`.

Then there is the exact disjoint decomposition

`A = R_C(w) disjoint_union S disjoint_union (e {w})`.

For each base-degree class put

`r_d(w)=|R_C(w) intersect V_d(C)|`,

`s_d=|S intersect V_d(C)|`,

`n_d(w)=|N_C(w) intersect V_d(C)|`.

The conserved vector of Claim 249 must then satisfy

`a_d(A)=r_d(w)+s_d+e*1_{deg_C(w)=d}`,

with

`0 <= s_d <= n_d(w)`.

So every possible dominating partner `w` constrains the common collision profile to an explicit integer box, and a partner producing an impossible box can be eliminated without enumerating extensions.

### Exact obstruction discovered

The tempting next step would apply the same formula to `B`. That step is **not valid automatically**.

If `G_A,G_B` have equal decks and `gamma(G_A)=2`, recognizability gives `gamma(G_B)=2`. But Claim 247 obtains the common base by deleting some vertex from each parent. Even if I deliberately choose the deleted vertex `z` in `G_A` to belong to a dominating pair, the vertex deleted from `G_B` to produce the same card `C` need not itself belong to any dominating pair of `G_B`.

In other words, the deck preserves the class `gamma=2`, but it does not presently supply a marked correspondence

`deleted vertex <-> member of a dominating pair`.

This is exactly the marker-loss obstruction that prevents the one-sided forced-set formula from immediately becoming an orbit proof. It also matches the boundary of Aravind--Monikandan: recognition of `gamma=2` is proved, while weak reconstruction of the class is left open.

A successful continuation must therefore do one of two things:

1. reconstruct enough **incidence data between cards and dominating pairs** to align the deleted vertex role across hypomorphic parents; or
2. avoid marking the pair entirely and derive a symmetric deck invariant strong enough to force the extension orbit.

The conserved degree profile is the first such symmetric invariant, but Section 6 proves it is not sufficient on arbitrary bases.

## 8. #24 FIND THE EXTREMAL OBJECT — the new smallest structural residue

The threshold-card theorem identifies a precise extremal residue at order 14.

- Maximum degree diversity on a 13-card is 12 distinct degrees; all such cards are antiregular and are now excluded.
- More generally **every threshold card** is excluded, regardless of degree multiplicities.
- Therefore any genuine order-14 counterexample must have every card nonthreshold, hence every card contains an induced `P_4`, `C_4`, or `2K_2` by the classical threshold characterization.
- In particular every common card has degree diversity at most 11.

The sharp next finite structural case is therefore not “all 13-vertex bases.” It is the first nonthreshold / degree-defect-two layer:

`13 - |{deg_C(v):v in V(C)}| = 2`.

That layer has either one degree class of size three or two degree classes of size two. Claim 249 forces a collision to keep the same occupancy in each repeated class; the remaining ambiguity is entirely inside those few equal-degree non-twin cells. This is the smallest class where the degree-profile proof can fail and is a much sharper target than arbitrary order-13 bases.

I did **not** claim that all degree-defect-two bases are rigid; that is the next theorem-sized question.

## 9. Current-literature boundary

The current source/prior-art boundary used this run is:

- **McKay 2022:** all graphs through 13 vertices reconstructible; plus restricted larger classes. This is the certified metric baseline.
- **Dufresne--Jeronimo--Kenkel--Lindo--Villamizar 2026:** current invariant-theoretic formulation, no full resolution.
- **Aravind--Monikandan 2026:** `gamma=2` recognizable; full RC reduces to 2-connected `gamma=2` or `diam(G)=diam(complement G)=2`; their pair-parameter reconstruction theorem assumes `gamma>=3` in the stated large connected regime and therefore does not fill the `gamma=2` marker gap used here.
- **Threshold/antiregular graph literature:** threshold graphs are recursively isolated/universal and have nested neighborhoods; antiregular graphs maximize degree diversity. These structural facts are prior art.
- **Farhadian / older anchor literature:** unique-anchor/asymmetric-subgraph gluing is prior art and is not relabelled as P03 progress.
- **Sciriha--Borg 2023:** reconstruction from one labelled card plus spectral/invariant side information is nearby common-card prior art.

Fresh bounded searches on 2026-09-17 for a full 2026 reconstruction proof/counterexample and for the exact threshold-common-card statement found no source-matching closure. Negative search evidence is not proof of openness beyond the sources above and is not a novelty certificate.

## 10. Methods and failure record

### #6 DEFORM TO A POINT YOU CAN SOLVE

I deformed arbitrary bases to bases whose degree classes have the strongest possible orbit structure. Threshold bases are solved completely by the conserved degree-class vector; antiregular bases give the extremal order-14 corollary.

### #12 FIND WHAT IS CONSERVED

The deck collision preserves, relative to the common base, the entire degree-class occupancy vector `(a_d)`, the number of internal edges `e_C(A)`, and the C4-through-new-vertex moment `q_C(A)`. These are exact equalities, not numerical heuristics.

### #24 FIND THE EXTREMAL OBJECT

Antiregular 13-cards are the maximum-degree-diversity extremizers and are excluded. The smallest unresolved degree layer now has degree defect two. This identifies where an orbit argument first has genuine room to fail.

### Failed / killed routes

- **Degree profile alone forces the orbit:** false; `C=P3 disjoint_union K2`, `A={0}`, `B={3}` is an exact counterexample to that intermediate claim.
- **Degree profile + triangle/C4 moments force the orbit:** the same singleton example still defeats these low moments.
- **A dominating pair can be aligned across the common card automatically:** unsupported. `gamma=2` is deck-recognizable, but the deleted vertex's membership in a dominating pair is not currently marked by Claim 247 or by the cited reduction.
- **Threshold-card rigidity is already full order-14 reconstruction:** false; a hypothetical counterexample can have only nonthreshold cards.
- **A finite structural exclusion moves `n_recon^cert`:** false by metric definition; complete all-graph coverage is required.

## 11. Directed P04/I0101 independent audit — claim 26

Peer report:

`proofnet24/P04-closure-local-paley/runs/2026-09-17/2026-09-17T14-00-25Z__run-report.md`

Creation commit: `ef655e1ba4fbd5b9b0510437d8bcb89800dee19a`.  
Blob at that report: `69c25fc0c11d52d5af6cde80400dae53afa90578`.  
Peer claim: `P04-I0101-QUOTIENT-TYPICAL-SPECTRUM-26`.

This is distinct from P03's prior audits of claim 25 (level-4 six-channel lift), claim 23 (anharmonic parity), claim 24 (sparse tangent ODE), and earlier finite-prime / maxdet claims.

### Claim under audit

For primes `p == 5 (mod 24)`, let

`V={x !=0,1: chi(x)=chi(x-1)=1}`,

`U_p=J(V)`, `m=|U_p|=(p-5)/24`, and

`T_p=(chi(u-v))_{u,v in U_p}`, with zero diagonal.

Claim 26 states that fewer than

`[3(p-29)/(32p)] m`

eigenvalues of `T_p` have absolute value greater than `(2/3)sqrt(p)`. Hence more than `29/32` of the spectrum lies in the source-scale symmetric window.

### Independent verification

First, for `p == 5 (mod 24)`, `p == 1 (mod 4)` and `p == 5 (mod 8)`. The standard character count gives

`|V|=(p-5)/4`.

The anharmonic `S_3` action is free on this clean family: the transposition-fixed harmonic points are excluded because `(2/p)=-1`, and order-three fixed points would solve `x^2-x+1=0`, which has no root because `p == 2 (mod 3)`. Thus every orbit has size six and

`m=|U_p|=(p-5)/24`.

Since `chi(-1)=1`, `T_p` is a real symmetric matrix. Its diagonal is zero and every off-diagonal entry is `+1` or `-1`, so exactly

`tr(T_p^2)=||T_p||_F^2=m(m-1)`.

If `N_p` eigenvalues satisfy

`|lambda|>(2/3)sqrt(p)`,

then

`N_p*(4p/9) < sum_j lambda_j^2 = m(m-1)`.

Therefore

`N_p/m < 9(m-1)/(4p)`.

Using `m-1=(p-29)/24`, this becomes

`N_p/m < 3(p-29)/(32p) < 3/32`.

Thus strictly more than `29/32` of the eigenvalues lie inside the stated window. All constants and strict inequalities match the peer claim.

### Audit verdict

**`P03-AUDIT-P04-I0101-QUOTIENT-TYPICAL-SPECTRUM-250 = PASS (CLAIM-SCOPED)`.**

This verifies only the typical-spectrum statement. It does **not** control the extreme eigenvalue needed for the Paley-theta conjecture and does not upgrade P04's source status.

No peer file was edited.

## 12. Exact remaining obligation and next attack

Source-level obligation remains unchanged:

- prove every graph of order 14 reconstructible, which moves `n_recon^cert` to 14 but remains PARTIAL for the universal conjecture; or
- exhibit one exact nonisomorphic pair with identical full vertex decks, which REFUTES the universal source.

The most useful next structural target is now narrower than at admission:

> **degree-defect-two common cards in the reduced `gamma=2` parent class.**

A 13-vertex base in this layer has only one triple degree cell or two double degree cells. Claim 249 freezes the occupancy of those cells. The next proof should classify how the first non-twin equal-degree cells can support two nonconjugate extension neighborhoods and then use the domination-pair forced set or a higher reconstructible rooted moment to eliminate them.

Suggested next Section-B triple, different from this run and from the first I0126 attack:

- **#3 PROVE SOMETHING STRONGER** — attempt a degree-defect-two rigidity theorem rather than a single `gamma=2` configuration;
- **#15 BREAK THE SYMMETRY ON PURPOSE** — analyze the first equal-degree non-twin cell where the threshold proof fails;
- **#25 COUNT THE SAME THING TWICE** — derive a deck formula for a marked pair/incidence count that can align domination-pair membership across cards.

This is the second consecutive unchanged I0126 run. One more unchanged run triggers the formal HARD stuck-thinking protocol under the fleet rule unless the remaining obstruction changes materially.

## 13. `ledger_delta` for P26

```json
{
  "worker": "P03",
  "target": "I0126 / Kelly-Ulam Graph Reconstruction Conjecture",
  "claim_path": "operations/claims/I0126.md",
  "claim_creation_commit": "a8a6793fc851824ab1e85568ab729e3c52291fda",
  "claim_blob": "7bc60b5449d3cef5b461da8b635f57d6c9fb963c",
  "lane": "HARD_OUTSIDE",
  "status": "OPEN_PARTIAL",
  "metric": "n_recon^cert",
  "before": 13,
  "after": 13,
  "movement": "NO_MOVEMENT",
  "unchanged_count": 2,
  "new_claim": {
    "id": "P03-I0126-DEGREE-PROFILE-THRESHOLD-RIGIDITY-249",
    "status": "PROVED_STRUCTURAL_PARTIAL_PUBLICATION_NOVELTY_UNVERIFIED",
    "metric_movement": false,
    "content": "extension collisions conserve degree-class occupancy, induced-edge count and C4-through-new-vertex moment; threshold common cards are collision-rigid; order-14 counterexamples can have no antiregular 13-card"
  },
  "methods_used": [6, 12, 24],
  "next_methods": [3, 15, 25],
  "peer_audit": {
    "id": "P03-AUDIT-P04-I0101-QUOTIENT-TYPICAL-SPECTRUM-250",
    "peer_claim": "P04-I0101-QUOTIENT-TYPICAL-SPECTRUM-26",
    "peer_path": "proofnet24/P04-closure-local-paley/runs/2026-09-17/2026-09-17T14-00-25Z__run-report.md",
    "peer_creation_commit": "ef655e1ba4fbd5b9b0510437d8bcb89800dee19a",
    "peer_blob": "69c25fc0c11d52d5af6cde80400dae53afa90578",
    "verdict": "PASS_CLAIM_SCOPED"
  },
  "artifacts_created": false,
  "shared_roots_edited": false,
  "peer_files_edited": false,
  "email": false,
  "drive": false,
  "public_posting": false,
  "paid_compute": false,
  "permission_changes": false,
  "workflow_execution": false
}
```

**End of complete run report.**