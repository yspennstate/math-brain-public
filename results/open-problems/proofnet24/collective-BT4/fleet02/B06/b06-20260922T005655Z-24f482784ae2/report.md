# BT4 fleet02/B06 — coalesced-exit adversary, saturated multi-port exception, and collar-or-bottleneck repair

Run: `b06-20260922T005655Z-24f482784ae2`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Outcome: `CANDIDATE_REFUTED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Target and exact peer state consumed

Target: prove that every finite loopless digraph with at most one arc per ordered pair, minimum outdegree at least seven, and opposite arcs allowed contains four vertex-disjoint genuinely directed cycles. Digons count as directed cycles.

I used the campaign lead's latest complete fleet02/B04 package `20260922T001806Z-b04-bt4-a1ceeb3c`: main report blob `d82fc84180bc66fd660c6c79f9a7f26332bdae72` and correction blob `ef92cfc95fab44c1e256757de5fae4ec4b28e36b`. Its surviving normal form is an exact-seven oriented spanning counterexample, a globally minimum-total three-cycle packing `(C1,C2,C3)`, DAG remainder `R`, arc domination, 3-vertex-strongness, the pair-deletion `6-fan / three-5-fan` dichotomy, and the repaired warning that a pair witness on the third packed cycle cannot be treated as a remainder witness.

I then consumed the named partner fleet03/B04's newest complete version `20260922T005218Z-fleet03-B04-r11b`, report blob `935647d4b652f8f27101c88c832fc0e00039e41c`, candidate `BT4-SUPPORT-SWITCH-v1`. Its key repair is the neutral support switch: a cycle-supported witness `w in C` becomes a legal remainder witness if there is `q in R` with `w^- -> q -> w^+`; after all such switches are exhausted, every unresolved singleton witness obeys

`N_R^+(w^-) ∩ N_R^-(w^+) = ∅`.

For compatibility I also used fleet03/B06's tight-port result, report blob `81a20ff15088e74009551fffd8e9f4812b781819`: single-port rigidity is proved only in the nonsaturated case `m<|C|`.

## Conditional end-to-end chain retained

The current proof skeleton is still conditional but source-valid:

1. reduce a hypothetical BT4 counterexample to the lead's exact-seven, oriented, globally minimum three-cycle packing with DAG remainder;
2. apply the strengthened `k=2` theorem to each deleted pair of packed cycles;
3. remainder-supported witnesses feed the valid one-vertex/path-fan exchange machinery;
4. cycle-supported five-witnesses have exact `5-cross/1-R-exit` structure, while six-witnesses have `6-cross/0-R-exit` structure;
5. fleet03/B04 moves any witness admitting a neutral `R` bypass into the remainder;
6. therefore the first genuinely hard saturation configuration is a cycle-supported certificate for which all neutral bypasses fail.

A tempting next augmentation statement is that three distinct cycle-supported five-witnesses provide at least two distinct `R` exit heads (or at least two vertex-disjoint sink collars), after which a simultaneous two-cycle splice can be attempted. That statement is false. The exact adversary below survives substantially more of the current normal form than a toy degree example.

## Adversary A — exact-seven, non-tournament, dominated, highly connected, but all three five-witness exits coalesce

The attached checker verifies a 16-vertex oriented digraph `D*` with vertices

`A0,A1,A2, B0,B1,B2, Z0,Z1,Z2, R0,...,R6`.

Take

`C1=(A0,A1,A2)`, `C2=(B0,B1,B2)`, `C3=(Z0,Z1,Z2)`, `R={R0,...,R6}`.

The complete adjacency list is in `adversary_checker.py`. The checker establishes all of the following simultaneously.

### Global local-normal-form properties

- every vertex has outdegree exactly seven;
- there are no loops or digons;
- the graph is not a tournament: exactly eight unordered pairs are nonadjacent;
- the graph remains strongly connected after deletion of any zero, one, or two vertices;
- every arc is dominated by a third vertex;
- `C1,C2,C3` are directed triangles, so their total size nine is globally minimum among all three-cycle packings in an oriented graph;
- `D*[R]` is acyclic with unique sink `R6`.

Thus this is not merely a low-degree or weak-connectivity obstruction to the proposed support/augmentation step.

### Exact pair-deletion certificate

Delete `C1 ∪ C2`. In the residual graph on `C3 ∪ R`, every vertex has residual outdegree at least two. Hence there is **no six-fan witness** for this pair. Instead the three distinct vertices `Z0,Z1,Z2` all have residual outdegree exactly two and therefore are exact five-fan witnesses.

For each `Zi` the two residual outarcs are precisely

`Zi -> Zi^+` and `Zi -> R0`.

Equivalently, each `Zi` sends exactly five arcs into `C1 ∪ C2`, has its mandatory successor on `C3`, and has the unique `R` exit `R0`.

The three distinct five-witnesses therefore have only **one** distinct exit head:

`H={R0}`.

This refutes the augmentation shortcut

> three cycle-supported five-witnesses imply two distinct exit heads / two independently launchable `R` collars.

The failure is highly asymmetric even though the ambient graph is 7-outregular: each `Zi` spends its budget as `5 cross + 1 cycle-successor + 1 common R-exit`, while the common head `R0` spends its seven arcs as packing fans `(2,1,0)` plus four arcs inside `R`.

### It also survives the named partner's neutral support switch

For every `w=Zi`, its predecessor `w^-` is another `Zj`. Every `Zj` has only one `R` outneighbor, namely `R0`. But `R0` has **no** outarc to any vertex of `C3`.

Therefore for every `w in C3`,

`N_R^+(w^-) ∩ N_R^-(w^+) = ∅`.

So none of the three witnesses admits the fleet03/B04 singleton neutral bypass. Since `C3` is a triangle, singleton segments are the only proper segments allowed by the partner's segment-switch lemma. The current support-switch mechanism is therefore fully exhausted on this example.

### The downstream sink is the saturated multi-port exception

The unique sink `x=R6` has packed-cycle fan counts

`(|N+(x)∩C1|, |N+(x)∩C2|, |N+(x)∩C3|)=(2,2,3)`.

In particular `m=|N+(x)∩C3|=3=|C3|`. For **each** `Zi` there is a tight return path

`Zi -> R0 -> R6`

of length two, which is exactly `m-1`. Moreover `R6 -> Zi` for all three `Zi`. Thus three different tight ports coexist.

This is an exact adversary to extending the fleet03/B06 nonsaturated single-port lemma from `m<|C|` to the saturated case `m=|C|`. In the saturated case the `m`-block is the entire cycle and has no unique predecessor; `P + x->b` is merely an equal-size cycle, not a shorter one. Port uniqueness is false.

### This is not a BT4 counterexample

The checker also gives the explicit four-pack

`(A0,A1,A2)`, `(B0,B1,R2)`, `(B2,R3,Z0)`, `(R0,R1,Z1)`.

So `D*` refutes only the **local closing implication**. Precisely as required, it shows which extra global input a valid proof must use: the true counterexample's no-four-pack condition cannot be replaced by exact degree, domination, 3-strongness, global minimum packing, DAG remainder, pair-witness multiplicity, or neutral-support-switch separation alone.

## Repair 1 — exit heads are light on their source cycle

The coalescence failure does not destroy all structure.

Let `z in C3` be a cycle-supported five-witness with unique exit `z->h`, `h in R`. Because `h` is a genuine remainder vertex and `z in C3` sends an arc to it, the valid one-vertex minimum-packing exchange applies **to h**, not to z. Therefore

`|N+(h) ∩ C3| <= 2`.

So every exit head of a cycle-supported five-witness is light on the source cycle. In the adversary, the common head has fan zero on `C3`, showing the bound can be very far from equality.

This is a safe replacement for trying to apply heavy-target avoidance directly to the cycle-supported witness.

## Repair 2 — collar-or-bottleneck dichotomy

Let `H` be the set of distinct `R` exit heads of a collection of cycle-supported five-witnesses, and let `T` be the sinks of the finite DAG `R`. Every `h in H` reaches some vertex of `T`.

Give every vertex of `R` capacity one, add a supersource adjacent to the heads and a supersink after the sinks, and apply integral max-flow/min-cut to the vertex-split network. Exactly one of the following holds:

1. there are two vertex-disjoint `H`-to-`T` paths, necessarily with distinct used heads and distinct used sink vertices; or
2. one vertex `s in R` meets every `H`-to-`T` path.

This is the correct replacement for the false automatic-two-collars statement.

If `|H|>=2` and branch 2 holds, choose a head different from `s` and let `U` be the vertices reachable from the remaining heads in `R-s`. Pick a sink `u` of `R[U]`. Any `R`-outneighbor of `u` different from `s` would also be reachable and belong to `U`, contradicting the choice of `u`. Hence

`d_R^+(u) <= 1`.

Exact outdegree seven now gives

`sum_i |N+(u)∩Ci| >= 6`.

Because `u` is a legitimate remainder vertex, this yields a source-valid branch split:

- some packed cycle receives at least three arcs from `u`, in which case the ordinary heavy-target avoidance/path-fan machinery is legal; or
- every packed fan is at most two, forcing the unique balanced possibility

`d_R^+(u)=1` and `(a1(u),a2(u),a3(u))=(2,2,2)`.

Thus distinct exit heads cannot simply disappear: failure of two disjoint collars feeds back either a legal heavy remainder witness or a rigid balanced `(2,2,2)+one-R-edge` bottleneck predecessor.

The adversary shows why a third branch must be retained: `|H|=1` total coalescence. Then the one-vertex cut is the common head itself and the preceding `u` argument has no non-cut head from which to start.

## Repair 3 — sharpen the equality-window statement, including the digon boundary

The lead already quarantined an overbroad equality exchange because the target `b` itself may occur when `x->b` is present. The exact repair is slightly sharper.

For a return path

`P: b=p0 -> ... -> p_L=x`

with internal vertices in `R`, let `m=|N+(x)∩C|` and suppose `m=L+1`.

- If `m<|C|`, then `x->b` is impossible in a globally minimum packing even without invoking orientation: `P+x->b` would be a directed cycle of length `m<|C|` disjoint from the other packed cycles, shortening the packing. Hence the equality fan is the consecutive `m`-successor block and the nonsaturated port argument is safe.
- If `m=|C|`, this shortening disappears. The fan is all of `C`, and port uniqueness can fail exactly as in Adversary A.
- If one drops the minimum-packing/orientation hypotheses altogether, even `m<|C|` can fail because a digon can realize the exceptional target `b`.

The attached second adversary makes the last point at the exact BT4 degree threshold. On ten vertices take every ordered arc except `d4->d2` and `d4->d3`. The minimum outdegree is seven. Let `C=(d0,d1,d2,d3)`, `x=d4`, `b=d0`. Then `b->x` and `x->b` form a digon, `L=1`, and

`N+(x)∩C={d0,d1}`, so `m=2=L+1<|C|`.

The claimed successor window would be `{d1,d2}`, which is false. This is not a BT4 counterexample (it has many digons); it proves that the no-digon/minimum-packing hypothesis is logically doing work and must not be silently dropped when the reduction is stated for the original problem class, where digons are allowed.

## First essential missing implication after the repair

The saturation branch is now narrower and honest.

For three cycle-supported five-witnesses on one complementary cycle:

- neutral bypasses move witnesses into the remainder and are already handled by fleet03/B04;
- with at least two distinct exit heads, either obtain two disjoint collars or a one-vertex bottleneck producing a legal heavy remainder witness / rigid `(2,2,2)` remainder vertex;
- the exact adversary leaves the **total-coalescence branch** `H={h}` as the first indispensable obstruction.

In the especially sharp triangle case realized above, all three vertices of `C3` point to the common head `h`, hence orientation forces `N+(h)∩C3=∅`. If `d_R^+(h)<=2`, then h itself has at least five outneighbors in `C1∪C2` and becomes an R-supported pair witness, returning to the clean branch. Therefore the truly hard triangle-coalescence case must satisfy

`d_R^+(h)>=3`.

The adversary realizes this with `d_R^+(R0)=4`, showing even that strengthened local condition is feasible.

The next proof step should therefore use the **global no-four-pack condition** (or an equivalent arc-maximal missing-arc certificate) to rule out or exploit a common light head with at least three `R` outneighbors. Re-running only degree, domination, connectivity, support-switch, or nonsaturated tight-port arguments cannot eliminate it: the exact graph above satisfies all of those local conditions and still realizes the obstruction.

## Exact computation and provenance

`adversary_checker.py` is a deterministic verifier containing the complete adjacency list. It checks the exact-seven oriented adversary, two-vertex-deletion strong connectivity, arc domination, global-minimum triangle packing, DAG remainder, pair residual degrees, common exit head, support-switch obstruction data, sink fan, and an explicit four-pack. It also checks the 10-vertex digon adversary.

Archived checker output has SHA-256 `3de8ae5dbed98a4a674effca6e7e2d982fbf408208f61258460ca02de6bfeb24` for the exact JSON text used in this run. The checker is an adversarial local-lemma verifier only; no finite computation is promoted to a proof of BT4.

## Outcome

`CANDIDATE_REFUTED` for the proposed automatic exit-separation / automatic two-collar augmentation and for any extension of nonsaturated single-port rigidity to `m=|C|`.

The repaired collar-or-bottleneck lemma and exit-head lightness are `ESSENTIAL_STEP_APPLIED` auxiliary progress, but BT4 itself remains open in this run. No full-proof or novelty claim is made.
