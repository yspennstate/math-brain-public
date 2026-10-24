# BT4 account04/B05 — dependency-exact twofold witness selection and domination descent

Run: `b05-20260922t011020z-bt4-r11`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Candidate: `BT4-COUNT-v2-HALL-DESCENT`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Exact target and source boundary

Target: every finite loopless digraph with at most one arc per ordered pair of distinct vertices and minimum outdegree at least seven contains four vertex-disjoint genuinely directed cycles. Opposite arcs are allowed and a directed digon counts as a cycle.

Current external source check:

- S. Bessy, M. Muis, J.-S. Sereni, R. Steiner, S. Wiederrecht, *A relaxation of the Bermond-Thomassen conjecture*, arXiv:2608.12948, 13 August 2026, https://arxiv.org/abs/2608.12948. Its abstract explicitly says the exact conjecture remains unresolved for every `k>=4`; its theorem at threshold `2k-1` permits each packed cycle to be directed or made directed by reversing one arc. That relaxation is not promoted to BT4 here.
- N. Lichiardopol, A. Por, J.-S. Sereni, *A Step toward the Bermond-Thomassen Conjecture about Disjoint Cycles in Digraphs*, SIAM J. Discrete Math. 23 (2009), 979-992, DOI 10.1137/080715792. The exact lower-k inputs used by the current team are: minimum outdegree five forces three disjoint directed cycles, and a digraph in which every vertex has outdegree at least three except at most two vertices of outdegree two has two disjoint directed cycles.

No literature-search miss is treated as a novelty certificate.

## Exact team state consumed

I read the BT4 lead's latest complete available version:

- `account02/B04`, run `20260922T001806Z-b04-bt4-a1ceeb3c`, report blob `d82fc84180bc66fd660c6c79f9a7f26332bdae72`;
- its controlling correction/addendum blob `ef92cfc95fab44c1e256757de5fae4ec4b28e36b`.

I also applied the named OTHER-account partner result:

- `account01/B06`, candidate `BT4-REROUTE-v1-support-transfer`, run `20260922T003740Z-b06-bt4-r11`, report blob `0af4b6dbda55cf1126d73d0688744bb2ba4496d9`.

Two compatible OTHER-account dependencies are also used because they directly repair or strengthen the present counting route:

- `account03/B04`, repair of the old `BT4-COUNT-v1`, blob `2d69f4c982db6bf08315db98a9a215dfe2b58177`;
- `account03/B04`, `BT4-SUPPORT-SWITCH-v1`, blob `935647d4b652f8f27101c88c832fc0e00039e41c`.

The repair is controlling: the previous B05 counting report was too broad when it applied the one-vertex heavy-target avoidance exchange to a pair-deletion witness lying on the complementary packed cycle. That inference is valid directly only for a witness in the DAG remainder. I do not reuse the invalid blanket statement.

The inherited source-valid normal form is therefore:

1. Work in an oriented exact-outdegree-seven minimum counterexample `D0` carrying a globally minimum-total packing `(C1,C2,C3)` of three directed cycles and acyclic remainder `R`.
2. Each packed cycle is chordless, every arc is dominated, and `D0` is 3-vertex-strong.
3. For every pair of packed cycles, deletion of that pair leaves no two vertex-disjoint directed cycles. Hence either one surviving vertex sends at least six arcs into the pair, or at least three distinct surviving vertices send exactly five arcs into the pair.
4. A pair-deletion witness on the complementary packed cycle has the repaired exact form: six-fan means `6-cross/0-R-exit`; five-fan means `5-cross/1-R-exit`. Such a witness is not silently treated as a remainder witness.
5. In the **global no-six branch**, every remainder sink has fan pattern `(3,2,2)` up to permutation. The partner further proves that if there are at least four remainder sinks then some packed-cycle pair has at least three distinct sink-supported five-witnesses. If no pair has three sink-supported witnesses, the hard remainder has at most three sinks.
6. A cycle-supported witness admitting the exact two-edge bypass `w^- -> q -> w^+` with `q in R` can be neutrally support-switched into the remainder; otherwise the precise separation `N_R^+(w^-) cap N_R^-(w^+)=emptyset` holds.

## Conditional end-to-end route

The current global route has two support branches after the six-fan/three-five-fan pair-deletion theorem.

- **Saturation branch:** a necessary witness is on the complementary packed cycle. Use the support-switch / segment-exchange machinery; if no neutral switch exists, exploit the explicit predecessor-successor separation and the exact `6-cross/0-exit` or `5-cross/1-exit` form.
- **All-R clean, global no-six branch:** each of the three pair labels has at least three five-witnesses in `R`. This is the branch attacked below. The previous counting argument used a hand-chosen orientation and did not fully isolate all dependencies. I replace that with an exact capacitated Hall selection and classify every possible failure.

The aim is not to assume independent random choices. It is to prove exactly when six collision-free witness ports can be selected, and to turn selection failure into a graph-theoretically rigid low-`R`-outdegree vertex that can feed the rerouting machinery.

## 1. Exact collision algebra for remainder five-witnesses

For `v in R`, write

`m_i(v)=|N^+(v) cap V(C_i)|`, and `q(v)=d_R^+(v)`.

Exact outdegree seven gives

`m_1+m_2+m_3+q=7`.                                                (1)

In the global no-six branch, each pair fan is at most five. Define

`S_12={v in R: m_1+m_2=5}`, and similarly `S_13,S_23`.

The all-R clean hypothesis is

`|S_12|,|S_13|,|S_23| >= 3`.                                    (2)

A vertex cannot belong to all three sets: the three equations

`m_1+m_2=m_1+m_3=m_2+m_3=5`

would force `m_1=m_2=m_3=5/2`.

More strongly, every double membership has an exact form. If, for example,

`v in S_12 cap S_13`,

then `m_2=m_3`, and solving (1) gives

`(m_1,m_2,m_3,q)=(3+q,2-q,2-q,q)`, with `q in {0,1,2}`.           (3)

Thus a double witness is heavy on the common cycle and has one of the three exact types

`q=0: (3,2,2;0)`,
`q=1: (4,1,1;1)`,
`q=2: (5,0,0;2)`.                                                (4)

The analogous statement holds after permuting the cycle labels. In particular, every collision between two pair-witness systems is a low-`R`-outdegree collision; there is no arbitrary dependence class hidden in the count.

## 2. Twofold Hall lemma — exact handling of the witness dependencies

The desired collision-free certificate is to choose two distinct witnesses for each of the three pair labels, with all six selected vertices distinct.

**Lemma 1 (twofold witness Hall alternative).** Under (2), exactly one of the following is available:

A. there are subsets `T_12 subset S_12`, `T_13 subset S_13`, `T_23 subset S_23`, each of size two, with the three subsets pairwise disjoint; or

B. a dependency obstruction occurs of one of the following two exact forms:

- **common triple:** for two pair labels, say `12` and `13`, `S_12=S_13=W` with `|W|=3`; every vertex of `W` is a double witness heavy on the common cycle `C1` and has one of the types (4);
- **global five:** `|S_12 union S_13 union S_23|=5`. Then at least four of these five vertices are double witnesses. More exactly, the membership pattern is, up to permuting the three pair labels, either
  - five double witnesses with double-membership counts `(1,2,2)` and pair-set sizes `(3,3,4)`, or
  - four double witnesses plus one single witness, with double-membership counts `(2,1,1)` and all three pair-set sizes exactly three; the single witness belongs to the pair opposite the common cycle carrying the two double collisions.

**Proof.** Duplicate each pair label twice and connect both copies of label `ij` to every vertex of `S_ij`. A six-distinct selection is exactly a matching saturating these six label copies.

For any fixed support `J` of pair labels, the neighborhood does not depend on whether one or two copies of a label in `J` are selected. Therefore Hall's condition reduces to

`|union_{e in J} S_e| >= 2|J|`                                  (5)

for every nonempty `J subset {12,13,23}`. Singletons satisfy (5) because every `|S_e|>=3`.

If (5) fails for two labels, their union has size at most three. Since each set already has size at least three, the two sets are the same three-element set. Triple membership is impossible, so all three elements are double witnesses for precisely those two labels. This is the common-triple obstruction.

If no two-label condition fails but the three-label condition fails, the full union has size at most five. It cannot have size at most four, because every witness belongs to at most two pair sets, while (2) supplies at least nine incidences. Hence the union has exactly five vertices. Let `d` be the number of double witnesses. The total incidence count is `5+d`, and is at least nine, so `d>=4`. If `d=5`, the three set sizes sum to ten and are each at least three, hence are `(4,3,3)`; solving for the three double-membership counts gives `(1,2,2)` up to permutation. If `d=4`, there is one single witness and total incidence nine, so all three pair sets have size three. If the single lies only in the third pair label, the three equations force double counts `(2,1,1)`, again up to permutation. This exhausts the possibilities. QED.

This is the exact dependency-aware replacement for an independence or random-choice assumption. The six selected ports in case A are genuine remainder vertices, so every subsequent one-vertex avoidance/exchange argument is support-legal.

## 3. Combining Hall failure with the partner's sink-incidence theorem

The partner `account01/B06` proves that in the global no-six branch, if no pair has three sink-supported five-witnesses, then `R` has at most three sinks.

**Corollary 2 (Hall obstruction forces a non-sink double witness).** Assume the all-R clean global no-six branch and assume no pair already has three sink-supported five-witnesses. If Lemma 1 does not give six distinct ports, then there exists a double witness `v` with

`q(v) in {1,2}`.                                                   (6)

Equivalently, after relabeling cycles,

`(m_1,m_2,m_3,q)=(4,1,1,1)` or `(5,0,0,2)`.                       (7)

**Proof.** In the common-triple obstruction, all three obstruction vertices are double witnesses. If all had `q=0`, then all three would be sinks and both incident pair labels would already have three sink-supported witnesses, contrary to hypothesis. Hence one has `q>=1`, and (4) gives (7).

In the global-five obstruction, at least four of the five vertices are double witnesses. Since there are at most three sinks, at least one of those double witnesses has `q>=1`, and again (4) gives (7). QED.

So dependence does not merely destroy the collision-free selection. In the genuinely sink-sparse hard core it produces a vertex that sends four or five arcs to one packed cycle while using only one or two arcs inside `R`.

## 4. Four-target domination descent — reconstructing an explicit fork from the collision

The low-`q` vertex in (7) can be pushed to a concrete rerouting interface using arc domination.

**Lemma 3 (four-target domination descent).** Let `v in R` satisfy

`|N^+(v) cap C_i| >= 4`.                                          (8)

Choose four distinct vertices

`A subset N^+(v) cap C_i`, `|A|=4`.

Then there exists `u in R` and an `R`-internal directed predecessor chain from `u` to `v` (possibly of length zero) such that

1. `A subset N^+(u) cap C_i`;
2. no vertex of `C_i` sends an arc to `u`;
3. there is no single vertex `z in R` satisfying simultaneously `z->u` and `A subset N^+(z)`;
4. for every `a in A`, domination of `u->a` supplies a vertex `d_a` with `d_a->u` and `d_a->a`, and each `d_a` lies in `R union C_j union C_k`.

Consequently at least one of the following explicit forks exists:

- **cross-cycle fork:** for some `a in A`, a vertex `d` on one of the other packed cycles satisfies `d->u` and `d->a`;
- **split-R fork:** all four arcs are dominated from `R`, but at least two distinct `R` predecessors of `u` are required to cover the four targets in `A`.

**Proof.** Because `u` is a remainder vertex with at least three outneighbors on `C_i`, the valid one-vertex minimum-packing exchange gives the heavy-target avoidance statement `C_i not-> u`.

Start with `u=v`. If there exists `z in R` with `z->u` and `A subset N^+(z) cap C_i`, replace `u` by `z`. The new vertex is again heavy on `C_i`, so `C_i not->z`. Repeating this operation follows arcs backwards inside the finite DAG `R`. It cannot continue forever or revisit a vertex, so it terminates at a vertex satisfying 1-3.

For each `a in A`, the arc `u->a` is dominated in the exact-seven normal form, so there is `d_a` with `d_a->u` and `d_a->a`. Since no vertex of `C_i` points to `u`, `d_a` cannot lie on `C_i`. Hence it lies in `R` or one of the other two packed cycles. If any dominator is on another packed cycle, the cross-cycle fork holds. If all are in `R`, condition 3 says they cannot all be the same vertex, so at least two distinct remainder predecessors are needed. QED.

Applying Lemma 3 to the non-sink double witness furnished by Corollary 2 turns the Hall-dependency obstruction into a source-valid directed object of exactly the kind needed by the current two-cycle rerouting work: either an explicit cross-cycle-to-remainder fork hitting the heavy cycle, or a split predecessor structure entirely inside the acyclic remainder. This is strictly more information than the old statement that “some witnesses collide.”

The cross-cycle fork aligns with the `account02/B05` dominator-escape geometry, where a compulsory external dominator must be repaired by a simultaneous two-cycle exchange rather than by a path confined to an exchanged acyclic remainder. The split-R fork is a separate constrained branch and must not be treated as if its two predecessor paths were independent.

## 5. Exact finite sanity check and an independence trap

`check_twofold_hall.py` is a finite sanity check of the six membership-count classes, not a proof of BT4. It enumerates all membership-count patterns with union size at most eight, set sizes at least three and no triple membership. Its exact output is archived in `checker_output.txt` and ends:

`PASS True`.

It found 716 admissible count patterns in that bounded sanity range; 15 fail the twofold Hall condition, partitioning into 9 pair-obstruction count patterns and 6 full-union-five patterns, with no unexpected pattern. The six full-union-five patterns are exactly the permutations proved in Lemma 1.

The checker also records a local dependency witness showing why independent pair choices are invalid even under the exact degree-seven/no-six fan equations:

- three vertices `u1,u2,u3` have local type `(m1,m2,m3;q)=(3,2,2;0)` and therefore belong to both `S_12` and `S_13`;
- three separate vertices `v1,v2,v3` have local type `(1,3,2;1)` and belong only to `S_23`.

Thus `S_12=S_13={u1,u2,u3}` and `S_23={v1,v2,v3}`, so no twofold system of distinct representatives exists for the first two pair labels. This is only a local exact-incidence witness to the failure of an independence argument; it is **not** claimed to extend to a BT4 counterexample digraph.

## What is now paid, and what is still unpaid

Paid in this run:

- the old B05 support error is explicitly quarantined and the corrected all-R scope is used;
- witness dependencies in the all-R/no-six branch are handled exactly by a twofold Hall theorem, not probabilistically assumed away;
- every Hall failure is classified into a three-vertex or five-vertex support obstruction;
- every double collision has one of the exact low-`R`-outdegree forms `(3,2,2;0)`, `(4,1,1;1)`, `(5,0,0;2)`;
- after applying the partner's sink-incidence reduction, every unresolved Hall obstruction contains a non-sink type `(4,1,1;1)` or `(5,0,0;2)`;
- that non-sink collision is reconstructed by domination descent into either an explicit cross-cycle fork or a split-R predecessor fork.

Still unpaid:

1. **six-port branch:** given two pairwise distinct R-supported five-witnesses for each packed-cycle pair, use their heavy-target avoidance data to build a legal simultaneous two-cycle exchange/fourth directed cycle;
2. **cross-cycle-fork branch:** combine the fork from Lemma 3 with the current segment/support-switch machinery to obtain the reciprocal disjoint return needed for a two-cycle splice;
3. **split-R-fork branch:** exploit acyclicity and the regenerated pair-deletion witnesses to force either a neutral support switch, a strict exchange, or a cross-cycle escape. The two predecessor branches may merge later and are not assumed independent;
4. the six-fan / complementary-cycle saturation branch remains separate and is not hidden inside this no-six argument.

These are narrower graph-theoretic reconstruction obligations than the prior generic “choose witnesses without collisions” gap. No target-level proof is claimed.

## Status and handoff

`ESSENTIAL_STEP_APPLIED`, parent BT4 still open.

Primary next recipients: named partner `account01/B06` and campaign lead `account02/B04`. The most direct use is to splice their rerouting machinery into the exact dichotomy:

- either six collision-free R witness ports exist, two for each pair; or
- in the sink-sparse hard core, a Hall collision produces a non-sink four/five-heavy remainder vertex and then the domination-descent cross-cycle/split-R fork above.

No brain retrieval or receiver-context use occurred, so status remains `WITHOUT_VERIFIED_BRAIN`. No installation/benchmark work, private archive access, email/Drive use, paid compute, remote workflow, or public posting was performed.
