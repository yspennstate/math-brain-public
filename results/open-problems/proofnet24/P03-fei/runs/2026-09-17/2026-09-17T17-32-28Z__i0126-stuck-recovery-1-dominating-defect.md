Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED.** GPT-6 / maximum was requested in prompt text, but the exposed runtime provides no authenticated model-family selector or reasoning-effort selector, so I do not claim otherwise. **NO MOVEMENT: `n_recon^cert: 13 -> 13`; I0126 unchanged count `2 -> 3`; formal HARD stuck protocol FIRED and recovery episode 1/2 is consumed. Methods this run: #3 PROVE SOMETHING STRONGER, #15 BREAK THE SYMMETRY ON PURPOSE, #25 COUNT THE SAME THING TWICE.**

# P03 HARD OUTSIDE — I0126 card-rooted dominating-pair defect and first HARD recovery

Run date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.  
Current claim: `operations/claims/I0126.md`, creation commit `a8a6793fc851824ab1e85568ab729e3c52291fda`, blob `7bc60b5449d3cef5b461da8b635f57d6c9fb963c`.  
Predecessor report: `proofnet24/P03-fei/runs/2026-09-17/2026-09-17T16-33-08Z__i0126-degree-profile-threshold-card.md`, creation commit `b776907f40b464f25bf0ba60479d29de04ec8d8e`, blob `dfc04a4db189fe0ab2ad50c64e5366716912844d`.

## 1. Frozen metric and status

The source-matching metric remains

`n_recon^cert` = the largest integer `n` for which every finite simple graph on at most `n` vertices is rigorously known reconstructible from its full vertex deck.

Before / after:

`n_recon^cert: 13 -> 13` — **NO MOVEMENT**.

The supported baseline is still Brendan D. McKay, *Reconstruction of Small Graphs and Digraphs* (2022; arXiv:2102.01942), which proves reconstruction for every graph through 13 vertices. The unrestricted Kelly--Ulam conjecture remains **OPEN / PARTIAL** in the current 2026 sources checked below. Because this is the third consecutive unchanged I0126 run, the formal HARD stuck protocol is mandatory in this report.

Retained P03 claims remain:

- `P03-I0126-EXTENSION-COLLISION-247 = PROVED / EXACT-REFORMULATION / PARTIAL / PUBLICATION-NOVELTY-UNVERIFIED`;
- `P03-I0126-DEGREE-PROFILE-THRESHOLD-RIGIDITY-249 = PROVED / STRUCTURAL-PARTIAL / PUBLICATION-NOVELTY-UNVERIFIED`.

## 2. Repository continuity and current-source check

Before the mathematical attack I reread/recovered the root `README.md`, `proofnet24/HOURLY_PROTOCOL_2026-09-15.md`, current `FLEET_RULES.md`, `operations/NEW_METHODS_2026-09-16.md`, `operations/FLEET_2026-09-16.md`, campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the current I0126 claim, the complete predecessor P03 report, the R09 I0126 admission screen, repository-wide I0126 hits, and the newest accessible P04/I0101 report used for the directed audit.

Large root/intake surfaces are connector-truncated when rendered wholesale. I used exact paths and exact IDs for the live dependencies and do **not** claim a byte-for-byte visible reread of every intake row. No shared root, peer file, historical report, or handoff was edited.

Fresh dated source/literature checks on 2026-09-17 recovered:

1. **McKay 2022**, arXiv:2102.01942: all graphs through 13 vertices are reconstructible. This is the metric baseline.
2. **Dufresne--Jeronimo--Kenkel--Lindo--Villamizar 2026**, arXiv:2604.16567: *Shuffling the Deck: Invariant Theory and the Graph Reconstruction Conjecture* still states the unrestricted conjecture and gives an invariant-theoretic program rather than a solution.
3. **Aravind--Monikandan 2026**, arXiv:2601.00620: `gamma(G)=2` is recognizable; the full reconstruction conjecture reduces to 2-connected parents with either `gamma(G)=2` or `diam(G)=diam(complement G)=2`; their conclusion explicitly leaves weak reconstructibility of connected `gamma=2` graphs as Problem 1.
4. The same Aravind--Monikandan source recalls the reconstructible pair parameters `pv(G,i)` and `pav(G,i)`, counting respectively nonadjacent and adjacent pairs with exactly `i` common neighbors. In particular `pv(G,0),pav(G,0)` are reconstructible.
5. Fresh bounded searches for a later accepted full proof/counterexample and for the exact card-rooted dominating-pair defect identity below found no source-matching resolution. This is negative search evidence only, not a novelty certificate.

A useful prior-art correction from the degree-diversity literature was also retained: the defect-one extremal case (antiregular/quasi-perfect graphs, `n-1` distinct degree values) is classical Behzad--Chartrand territory. The present target is the next degree-defect-two layer, not a rediscovery of antiregular structure.

## 3. Idea before code; refutation-first target

The previous run isolated the exact `gamma=2` marker-loss obstruction: from a common card `C=G-z`, one parent may have the deleted vertex `z` in a dominating pair, but equality of decks does not directly mark the corresponding deleted vertex in the other parent as a member of a dominating pair.

The new idea was to **avoid marking a partner and instead decorate each card by the net change in the number of dominating pairs caused by deleting its missing vertex.** This is symmetric, reconstructible from the deck, and can be written exactly in the one-vertex-extension coordinates of Claim 247.

Before treating that statistic as sufficient, I deliberately tried to break it. Section 7 gives an explicit pair of nonisomorphic, 2-connected, domination-number-two extensions for which the old conserved profile **and** the new dominating-pair defect all agree. Their decks are not equal. Thus the new statistic is a genuine necessary invariant and a partial repair of marker loss, but not a hidden proof of the reduced `gamma=2` class.

No code was needed for the theorem. A small graph was used only as a hand-checkable route-kill; no all-13-vertex-base enumerator was run.

## 4. #25 COUNT THE SAME THING TWICE — a card-rooted dominating-pair defect

For any graph `G`, let

`D2(G) = # { unordered {u,v} subset V(G) : {u,v} is a dominating set of G }`.

This parameter is reconstructible from the deck by known pair-parameter theory. Indeed a pair `{u,v}` dominates `G` iff there is no third vertex nonadjacent in `G` to both `u,v`, equivalently iff `u,v` have no common neighbor in the complement `bar G`. If `uv` is an edge of `G`, then the pair is nonadjacent in `bar G`; if `uv` is a nonedge of `G`, it is adjacent in `bar G`. Hence exactly

`D2(G) = pv(bar G,0) + pav(bar G,0)`,                                        (4.1)

and `pv,pav` are reconstructible in the cited Gupta/Aravind--Monikandan framework. Complementing the deck is itself canonical.

For a vertex `v` define two rooted counts:

`P_G(v) = # { w != v : {v,w} dominates G }`,

`Q_G(v) = # { {x,y} subset V(G)\{v} : {x,y} dominates G-v but not G }`.

Then count the dominating pairs of the card `G-v` in two classes. A dominating pair of `G` not containing `v` remains dominating after deleting `v`; the `P_G(v)` pairs containing `v` disappear; and exactly the `Q_G(v)` new pairs become dominating only because the sole offending vertex `v` was removed. Therefore

`D2(G-v) = D2(G) - P_G(v) + Q_G(v)`.                                        (4.2)

Define the **card defect**

`delta_G(v) := D2(G)-D2(G-v) = P_G(v)-Q_G(v)`.                              (4.3)

Because `D2(G)` is reconstructible and `D2(G-v)` is computed from the card itself, an unlabeled deck determines the multiset of pairs

`( [G-v], delta_G(v) )`.

This is the first symmetric replacement for the lost marker used below.

## 5. New theorem — exact defect formula in extension coordinates

Let `C` be a graph, `A subseteq V(C)`, and `G_A` the one-vertex extension obtained by adjoining `z` adjacent exactly to `A`. For `w in V(C)` define the base anti-neighborhood

`R_C(w) = V(C) \ (N_C(w) union {w})`.

Define

`P_C(A) = # { w in V(C) : R_C(w) subseteq A }`,                              (5.1)

and

`Q_C(A) = # { dominating pairs {u,v} of C : u notin A and v notin A }`.      (5.2)

Finally put

`Delta_C(A) = P_C(A)-Q_C(A)`.                                                (5.3)

### Claim 251

**`P03-I0126-DOMINATING-PAIR-CARD-DEFECT-251 = PROVED / STRUCTURAL-PARTIAL / PUBLICATION-NOVELTY-UNVERIFIED`.**

If two extensions of the same base satisfy

`D(G_A)=D(G_B)`,                                                              (5.4)

then

`Delta_C(A)=Delta_C(B)`.                                                      (5.5)

Moreover, suppose

`A=S union {x}`, `B=S union {y}`,                                             (5.6)

where `x != y` and `x,y notin S`. Define

`U_x(S) = # { w : R_C(w)\S = {x} }`,                                        (5.7)

and

`T_x(S;y) = # { t notin S union {x,y} : {x,t} dominates C }`.                (5.8)

Then every equal-deck extension collision of the one-swap form (5.6) satisfies the exact **swap-balance law**

`U_x(S)+T_x(S;y) = U_y(S)+T_y(S;x)`.                                        (5.9)

If this is a genuine collision, Claim 249 supplies two further local balances:

`deg_S(x)=deg_S(y)`,                                                         (5.10)

and, writing `c_w(S)=|N_C(w) intersect S|`,

`sum_w c_w(S) ( 1_{w~x} - 1_{w~y} ) = 0`.                                  (5.11)

Thus the first degree-defect-two ambiguity is no longer an unconstrained orbit search: every surviving one-swap candidate must lie in the simultaneous zero set of (5.9)--(5.11), in addition to the full degree-class occupancy constraints.

### Proof of Claim 251

First compute the two rooted terms for the new vertex `z`.

A pair `{z,w}` dominates `G_A` iff every base vertex other than `w` is adjacent either to `z` or to `w`. The vertices not adjacent to `w` in the base and distinct from `w` are exactly `R_C(w)`, while the vertices adjacent to `z` are exactly `A`. Hence

`P_{G_A}(z)=P_C(A)`.                                                         (5.12)

Next let `{u,v}` be a pair of base vertices. It becomes a newly dominating pair after `z` is deleted iff it dominates the base `C` but fails to dominate `G_A`. Since it already dominates every base vertex, the only possible failure in `G_A` is the vertex `z`; that happens exactly when neither `u` nor `v` belongs to `A`. Therefore

`Q_{G_A}(z)=Q_C(A)`.                                                         (5.13)

Applying (4.3),

`D2(G_A)-D2(C)=Delta_C(A)`.                                                  (5.14)

The same equation holds for `B`. Equal decks imply equal reconstructible values `D2(G_A)=D2(G_B)`, and the deleted card is the same base `C`, so (5.5) follows.

Now assume (5.6). Let

`P_0 = # { w : R_C(w) subseteq S }`.

A base vertex `w` is counted by `P_C(A)` but not by `P_0` exactly when the only element of `R_C(w)` outside `S` is `x`. Thus

`P_C(A)=P_0+U_x(S)`,
`P_C(B)=P_0+U_y(S)`.                                                         (5.15)

For the `Q` terms, the dominating pairs of `C` disjoint from `S union {x,y}` occur in both counts. The pair `{x,y}` occurs in neither count. The only additional pairs in `Q_C(A)` are those using `y` and a vertex outside `S union {x,y}`; the only additional pairs in `Q_C(B)` are those using `x`. Hence

`Q_C(A)-Q_C(B)=T_y(S;x)-T_x(S;y)`.                                          (5.16)

Subtracting the two `Delta` values and using (5.5) yields (5.9).

For (5.10), Claim 249 gives `e_C(A)=e_C(B)`. Since both sets contain the same induced subgraph on `S` and only one of `x,y`, their edge-count difference is exactly

`deg_S(x)-deg_S(y)`,

so it vanishes.

For (5.11), Claim 249 gives `q_C(A)=q_C(B)` where

`q_C(A)=sum_w binom(|N_C(w) intersect A|,2)`.

Put `c_w=|N_C(w) intersect S|`. Because the added indicator is binary,

`binom(c_w+1_{w~x},2)-binom(c_w+1_{w~y},2)
 = c_w(1_{w~x}-1_{w~y})`.

Summing over `w` and using equality of the two `q` values gives (5.11). QED.

### Prior-art / novelty label

Equation (4.2) is an elementary deletion identity, and the reconstructibility of the zero-common-neighbor pair counts is published prior art. Domination-polynomial deletion recurrences are also established literature. I do **not** claim that the raw identity is new. The source-specific use as a common-card collision constraint, and especially the one-swap balance (5.9), was not located in the bounded search; publication novelty remains **UNVERIFIED**.

## 6. #3 PROVE SOMETHING STRONGER — complete reduction of the one-triple defect-two ambiguity to a one-swap kernel

Let `C` be a 13-vertex common card with exactly 11 distinct degree values. There are only two multiplicity patterns:

1. one degree class has size three and all other degree classes are singletons; or
2. two degree classes have size two and all others are singletons.

In the first pattern, Claim 249 forces `A` and `B` to agree on every singleton class and to choose the same number of vertices from the unique triple class. If they differ at all, then after putting all common chosen vertices into `S`, their difference has exactly the one-swap form

`A=S union {x}`, `B=S union {y}`

for two vertices `x,y` in that equal-degree triple. Therefore **every** extension collision over a one-triple degree-defect-two card must satisfy (5.9)--(5.11).

In the two-doubleton pattern the same conclusion holds whenever only one repeated class changes. The only new ambiguity not reduced to a one-swap kernel is a simultaneous swap in both repeated degree classes.

This is a complete structural reduction of the first degree-defect-two layer to:

- balanced one-swap candidates satisfying three exact local equations; and
- in the `2+2` multiplicity pattern, a possible two-swap cancellation.

It is not yet a proof that those kernels are empty, so it does not move `n_recon^cert`.

## 7. #15 BREAK THE SYMMETRY ON PURPOSE — the new invariant is still insufficient, even inside the reduced parent class

A strong but false hope would be that the old conserved profile plus `Delta_C` already forces the extension orbit, at least for 2-connected `gamma=2` parents. The following hand-checkable example kills that hope.

Let `C` have vertices `{0,1,2,3,4,5}` and edges

`04, 05, 12, 13, 23, 34`.

Its degrees are

`deg(0)=2, deg(1)=2, deg(2)=2, deg(3)=3, deg(4)=2, deg(5)=1`.

Take

`x=1`, `y=4`, `S={0,2,3,5}`,

so

`A=S union {1}=V(C)\{4}`,
`B=S union {4}=V(C)\{1}`.

The two neighborhoods have the same degree-class occupancy. Directly:

- `e_C(A)=4=e_C(B)`;
- `q_C(A)=4=q_C(B)`;
- `P_C(A)=3=P_C(B)`;
- `Q_C(A)=0=Q_C(B)` because each complement has only one vertex;
- hence `Delta_C(A)=3=Delta_C(B)`.

For the one-swap formula,

`U_1(S)=2=U_4(S)`,
`T_1(S;4)=0=T_4(S;1)`,

so (5.9) also holds exactly. Further,

`deg_S(1)=2=deg_S(4)`,

and the `q`-balance (5.11) vanishes because the two `q` values coincide.

Nevertheless the extensions `G_A,G_B` are nonisomorphic. In both, the new vertex `z` has degree five and is the unique vertex of that degree, so any isomorphism would fix `z` and restrict to an automorphism of `C` sending `A` to `B`, equivalently sending `4` to `1`. But vertex `1` lies in the triangle `1-2-3-1`, whereas vertex `4` lies in no triangle of `C`, so no automorphism of `C` sends `4` to `1`.

Both parents lie squarely inside the difficult reduced regime:

- each has `gamma=2` because `z` is not universal but belongs to a dominating pair (`{z,0}` in `G_A`, for example, and `{z,1}` in `G_B`);
- both are 2-connected because both contain the spanning cycle

`0-4-3-1-2-z-5-0`.

This is **not** a reconstruction counterexample. It has order seven, and McKay's theorem already guarantees its two nonisomorphic members have different decks. Its purpose is sharper: even after repairing marker loss with the scalar card defect, the current finite set of conserved local moments does not force isomorphism inside the exact 2-connected `gamma=2` reduction.

## 8. Why the new invariant matters despite the route-kill

The previous marker loss was qualitative: the deck recognized that a parent belongs to the `gamma=2` class but did not tell us how a particular deleted vertex participates in dominating pairs.

Claim 251 recovers an exact card-attached signed quantity

`delta_G(v)= (# dominating pairs containing v) - (# pairs newly dominating after deleting v)`.

Thus equal cards in hypomorphic parents carry the same signed defect. This is strictly more information than recognition of `gamma=2` and turns the first repeated-degree-cell ambiguity into explicit equations.

The failure example also says exactly what is missing: **the scalar difference can hide a rearrangement of the dominating partners themselves.** A successful proof needs more card-rooted incidence information than the total signed defect.

## 9. Formal HARD stuck-thinking protocol — unchanged run 3

Because `n_recon^cert` stayed at 13 for the third consecutive I0126 run, the formal stuck protocol fires here.

### 9.1 Exact blocking formula

At the first one-triple degree-defect-two common card, every possible extension collision reduces to a one-swap pair `A=S union {x}`, `B=S union {y}` with equal-degree `x,y` and must satisfy simultaneously

`U_x(S)+T_x(S;y)=U_y(S)+T_y(S;x)`,                                           (B1)

`deg_S(x)=deg_S(y)`,                                                         (B2)

`sum_w |N_C(w) intersect S|(1_{w~x}-1_{w~y})=0`.                            (B3)

These conditions, even together with the full degree-class occupancy vector, do **not** force `x,y` into the same automorphism orbit: Section 7 gives an exact 2-connected `gamma=2` witness to that failure.

The scalar card defect itself is

`delta_G(v)=P_G(v)-Q_G(v)`,                                                   (B4)

so the deck-visible quantity loses the two nonnegative terms separately. This signed cancellation is the precise current blocker.

### 9.2 Routes tried and precise failure reasons

1. **Extension-collision reformulation (Claim 247):** exact and useful, but leaves a universal quantifier over all 13-vertex common cards.
2. **Degree occupancy + triangle/C4 moments (Claim 249):** enough for threshold/twin-module bases, but the earlier `P3 disjoint_union K2` route-kill already showed these low moments do not separate arbitrary extension orbits.
3. **Threshold/antiregular deformation (Claim 249):** excludes every threshold common card and all 12-distinct-degree 13-cards, but the first nonthreshold degree-defect-two layer remains.
4. **`gamma=2` forced anti-neighborhood formula:** if the deleted/new vertex is in a dominating pair, it forces `R_C(w) subseteq A`, but equal decks do not mark the same role in the other parent.
5. **Card-rooted dominating-pair defect (Claim 251):** repairs the marker loss only up to the signed scalar `P-Q`. Section 7 shows even equal `P`, equal `Q`, equal degree occupancy, equal triangle/C4 moments and 2-connected `gamma=2` do not force extension isomorphism.
6. **Brute-force all 13-vertex bases:** deliberately not used. An unaudited enumeration would violate the source/metric standard and would not explain the obstruction.

### 9.3 What a proof must add

A successful order-14 structural proof must reconstruct **more than the scalar number of dominating partners of the deleted vertex**. It needs a card-rooted incidence object that separates the possible partners, for example a degree-/anti-neighborhood-refined multiset of partners, or an equivalent invariant that survives unlabeled card matching and cannot cancel as `P-Q` does.

On the one-triple defect-two layer, it is enough to obtain an invariant that distinguishes the two sides of every nonautomorphic balanced one-swap `(x,y;S)` satisfying (B1)--(B3). On the `2+2` layer it must also prevent simultaneous-swap cancellation.

### 9.4 Simplest unproved special case

The cleanest unresolved special case is:

> `C` is a 13-vertex graph with exactly one degree class of size three and all ten other degree classes singleton; `G_A,G_B` are 2-connected `gamma=2` one-vertex extensions with equal decks. Prove that their one-swap neighborhoods are conjugate under `Aut(C)` (or produce an exact source counterexample).

Claim 251 reduces every ambiguity in this special case to the balanced one-swap kernel (B1)--(B3). I do not know how to prove that kernel empty.

### 9.5 Nearest solved literature analogue

The nearest published/source-level analogue is Aravind--Monikandan 2026: zero-common-neighbor pair counts are reconstructible and `gamma=2` is recognizable, but they explicitly explain that the degrees of a dominating pair are indeducible by their direct card argument and leave weak reconstruction of connected `gamma=2` graphs as Problem 1. The nearest P03 solved common-card analogue is Claim 249: threshold bases work because equal-degree cells are twin modules, so degree occupancy already determines the orbit. McKay's all-graphs theorem through order 13 is the finite baseline immediately below the target order.

### 9.6 Exactly one recovery action — episode 1/2 consumed

The single recovery action executed in this stuck run was:

> **replace the lost marked-dominating-pair role by the reconstructible deleted-card defect `delta_G(v)=D2(G)-D2(G-v)` and derive its exact extension/swap formulas.**

That action produced Claim 251 but did not move the frozen all-graphs metric. Therefore **HARD recovery episode 1/2 is consumed**.

The second and final permitted recovery should stay on one coherent refinement of this same obstruction: reconstruct (or rigorously prove non-reconstructible from the current data) a **degree-/anti-neighborhood-refined dominating-partner profile for the deleted vertex in the one-triple 13-card case**. No third I0126 recovery is permitted if the metric still does not move.

## 10. Directed P04/I0101 independent audit — finite claim 28

Peer report audited:

`proofnet24/P04-closure-local-paley/runs/2026-09-17/2026-09-17T17-03-00Z__run-report.md`

Creation commit: `584d74855bb90e8c13d4989d7fb9080ace9d070f`.  
Blob at that exact commit: `f23150281acd72c839401c51c1aa1413a379496a`.  
Peer claim: `P04-I0101-P4057-S3-ORBIT-DUAL-28 = PROVED / FINITE-PARTIAL`.

Supporting exact checker:

`proofnet24/P04-closure-local-paley/artifacts/2026-09-17T16-45-53Z__p4057_s3_orbit_dual_exact.py`, creation commit `134ab5c61ae18d314f44ea510d821afd4b20a7fe`, blob `224a3a074e64e792f021b9acb36c63ce393703d5`.

Supporting exact output:

`proofnet24/P04-closure-local-paley/artifacts/2026-09-17T16-45-53Z__p4057_s3_orbit_dual_exact.out`, creation commit `eca9b89697831b27a84dce85cff5314ee8d08dfd`, blob `28546d7b8464b6c2a2145e3ebe6b0e272cc00e17`.

### Independent derivation of the certificate implication

The report uses the standard theta dual

`theta(complement H)=min lambda_max(B)`

over symmetric matrices with `B_ii=1` and `B_ij=1` on graph edges. Therefore any exact feasible `B` with `tI-B` positive definite proves

`theta(complement H)<t`.

For `p=4057`, the checker builds `H=G_{4057,2}` exactly and fixes one rational value on each S3 nonedge orbit. Floating alternating projection is candidate generation only; the accepted matrix is rebuilt from integer orbit weights. The checker exactly verifies symmetry, unit diagonal, edge entries equal to one, and S3 invariance.

Set

`t=422/10`, `D=5120`, `M_int=D(tI-B)`.

The accepted integer factor data satisfy the exact identity

`M_int = Lq Lq^T / 1024^2 + 512 I + Rnum/1024^2`.                       (10.1)

The archived output gives

`max_i sum_j |Rnum_ij| = 142755197`,

while

`512*1024^2 = 536870912`,

so the exact slack is

`536870912-142755197 = 394115715 > 0`.                                     (10.2)

Because `Rnum` is symmetric,

`lambda_min(Rnum) >= -||Rnum||_infinity >= -142755197`.

Hence

`512 I + Rnum/1024^2` is strictly positive definite. The first term of (10.1) is positive semidefinite, so `M_int` is strictly positive definite and therefore `tI-B` is strictly positive definite. This proves

`theta(complement G_{4057,2}) < 422/10`.

The source threshold comparison is also exact:

`422/10 < (2/3)sqrt(4057)`

because, after squaring positive quantities,

`400*4057 - 9*422^2 = 20044 > 0`.

The checker also verifies the p=4057 localized vertex/orbit construction exactly and records `|V_2|=1013`, `256000` graph edges and `256578` nonedges, with a complete S3 nonedge-orbit census.

### Audit verdict

**`P03-AUDIT-P04-I0101-P4057-S3-ORBIT-DUAL-252 = PASS (CLAIM-SCOPED)`.**

The finite p=4057 source inequality follows from exact integer feasibility and positive-definiteness data. The audit does **not** certify P04's eventual-prime Conjecture 27 or turn finite evidence into an asymptotic theorem.

## 11. Methods record

### #3 PROVE SOMETHING STRONGER

Instead of a statistic only for order 14, Claim 251 is valid for every common-base extension collision. In the one-triple degree-defect-two case it reduces the entire neighborhood ambiguity to a one-swap kernel with three exact balance equations.

### #15 BREAK THE SYMMETRY ON PURPOSE

I deliberately left the threshold/twin regime and built an exact nonthreshold 2-connected `gamma=2` pair where all current low invariants, including the new defect, coincide but the extensions are nonisomorphic. This prevents a false orbit-separation theorem.

### #25 COUNT THE SAME THING TWICE

Counting dominating pairs before and after deleting a vertex gives (4.2), then translating the two rooted terms into extension coordinates produces `Delta_C(A)` and the swap balance (5.9). This directly attacks the previous marker-loss obstruction without choosing a labeled partner.

## 12. Exact remaining obligation

The source remains the unrestricted Graph Reconstruction Conjecture. The order-14 metric does not move until **every** 14-vertex graph is covered.

The immediate structural obligation is narrower and exact:

> decide the balanced one-swap kernel for 13-vertex common cards with one repeated degree class of size three, preferably within 2-connected `gamma=2` parents, by reconstructing a partner-refined card invariant or by constructing a genuine equal-deck collision.

The two-doubleton degree-defect-two pattern adds a possible simultaneous two-swap cancellation after this case.

## 13. `ledger_delta` for P26

```json
{
  "worker": "P03",
  "lane": "HARD_OUTSIDE",
  "target": "I0126_KELLY_ULAM_GRAPH_RECONSTRUCTION",
  "metric": "n_recon^cert",
  "before": 13,
  "after": 13,
  "movement": false,
  "unchanged_count_before": 2,
  "unchanged_count_after": 3,
  "stuck_protocol": "FIRED",
  "hard_recovery_episode_consumed": "1_of_2",
  "status": "OPEN_PARTIAL",
  "new_claim": {
    "id": "P03-I0126-DOMINATING-PAIR-CARD-DEFECT-251",
    "status": "PROVED_STRUCTURAL_PARTIAL_PUBLICATION_NOVELTY_UNVERIFIED",
    "content": "equal-deck common-base extensions preserve Delta_C(A)=P_C(A)-Q_C(A); one-swap collisions satisfy exact dominating-pair, triangle and C4 balance equations"
  },
  "retained_claims": [
    "P03-I0126-EXTENSION-COLLISION-247",
    "P03-I0126-DEGREE-PROFILE-THRESHOLD-RIGIDITY-249"
  ],
  "first_unproved_special_case": "13-vertex common card with one degree class of size 3 and ten singleton degree classes; balanced one-swap extensions inside 2-connected gamma=2 parents",
  "exact_blocker": "deck-visible deleted-card defect is only P_G(v)-Q_G(v); partner incidence can rearrange/cancel and current local moments do not force the extension orbit",
  "recovery_action_executed": "replace marked dominating-pair role by reconstructible card defect and derive exact extension/swap formulas",
  "next_and_final_recovery": "degree-/anti-neighborhood-refined dominating-partner profile in the one-triple 13-card case",
  "peer_audit": {
    "id": "P03-AUDIT-P04-I0101-P4057-S3-ORBIT-DUAL-252",
    "verdict": "PASS_CLAIM_SCOPED",
    "peer_claim": "P04-I0101-P4057-S3-ORBIT-DUAL-28",
    "peer_report_creation_commit": "584d74855bb90e8c13d4989d7fb9080ace9d070f",
    "peer_report_blob": "f23150281acd72c839401c51c1aa1413a379496a"
  },
  "methods_used": [3, 15, 25],
  "shared_roots_edited": false,
  "peer_files_edited": false,
  "artifact_created": false
}
```

No shared root ledger was edited; P26 alone owns those reconciliations. No Gmail/email, Drive, public posting, paid compute, access change, workflow execution, or additional schedule was used.

**End of complete run report.**