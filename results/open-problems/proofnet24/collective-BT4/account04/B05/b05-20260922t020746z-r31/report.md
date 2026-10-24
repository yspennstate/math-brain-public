# BT4 account04/B05 — four-remainder exit-footprint escape

Run: `b05-20260922t020746z-r31`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Candidate: `BT4-COUNT-v3-FOUR-R-ESCAPE`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Exact target and source boundary

Target: prove that every finite loopless digraph with at most one arc per ordered pair of distinct vertices and minimum outdegree at least seven contains four vertex-disjoint genuinely directed cycles. Digons are allowed in the target statement.

The current source check is Bessy--Muis--Sereni--Steiner--Wiederrecht, *A relaxation of the Bermond-Thomassen conjecture*, arXiv:2608.12948 (13 August 2026). Its abstract states that the exact Bermond--Thomassen conjecture remains unresolved for every `k>=4`; its theorem at threshold `2k-1` permits each packed cycle either to be directed or to become directed after reversing one arc. No such relaxed cycle is promoted here to a directed cycle.

I read and use the campaign lead's newest complete account02/B04 state:

- `proofnet24/collective-BT4/account02/B04/20260922T011943Z-b04-bt4-r11/report.md`, blob `ee3294c169f9736cd8f0fdb943b5cefab5906a9e`.

I consume and apply the named OTHER-account partner result:

- account01/B06, `proofnet24/collective-BT4/account01/B06/20260922T013522Z-b06-bt4-r11/report.md`, blob `0ffb3fb1b521920e0a9cb3693fda8fd5bbb6a588`.

Its exact input used below is the support-transfer/collar trichotomy: an `R`-supported five-witness heavy on a packed cycle with fan `m>=3` yields either a cross-packed transition, an equality return with a size-neutral minimum-packing exchange, or three strict pure-`R` channels forcing `|R|>=3m-2>=7`.

I also apply account02/B05 `BT4-RSC-v4-boundary-lift`, report blob `2ea38c8ce3130b68fcce58e2b09fa32a8b6b37f4`: repeated domination of an internal remainder arc `y->t` terminates, by acyclicity, in a packed-cycle apex and produces a transitive ladder whose vertices also point directly to `t`.

As an adversarial boundary check I consumed account03/B06 `BT4-G1-PORT-EXCLUSION-v1`, report blob `1e45b25528a0a5f5b87edcf80290f33d4f394894`. Its exact 20-vertex certificate shows that pure cardinality of regenerated five-witnesses does not force them out of the immediate support collar. Accordingly the argument below changes mechanism: it counts **R-exit footprints** and then uses domination/boundary lifting, rather than treating witness choices as independent.

No peer outcome label is used as proof; only the stated hypotheses and lemmas above are imported.

## Inherited normal form and the lead's live small-remainder branch

Assume BT4 false and work in the lead's inherited minimum-counterexample normal form. Thus there is an oriented spanning counterexample `D` with:

1. `d_D^+(v)=7` for every vertex;
2. a globally minimum-total packing `(C1,C2,C3)` of three directed cycles;
3. nonempty acyclic remainder `R=V(D)\(V(C1) union V(C2) union V(C3))`;
4. each `Ci` chordless;
5. every arc dominated; and
6. `D` 3-vertex-strong.

For each packed pair `Ci,Cj`, the strengthened `k=2` deletion theorem used by the lead gives either a residual vertex of outdegree at most one (equivalently a six-or-more cross-fan into `Ci union Cj`) or at least three residual vertices of outdegree exactly two (five-cross witnesses in the exact-seven normal form).

The **global NO-SIX** branch is the branch in which the latter alternative holds for all three packed pairs. The lead's newest report leaves, among its explicit obligations, the no-six state with `|R|=4` and at most two remainder sinks after escaping the three-sink core. The result below is stronger with respect to sink count: it applies to every global-NO-SIX state with `|R|=4`.

## Lemma 1 — with four remainder vertices, a remainder-supported five-witness already exits to established geometry

Assume `|R|=4` and global NO-SIX. Let `u in R` be a five-witness for some packed pair. Then `u` sends five arcs into that pair, so one of the two packed cycles receives a heavy fan of size `m>=3`.

By the exact account01/B06 collar trichotomy, at least one of the following occurs:

1. a cross-packed transition;
2. an equality return producing a size-neutral globally minimum packing exchange; or
3. `|R|>=3m-2>=7`.

The third alternative is impossible when `|R|=4`.

Hence in a four-remainder NO-SIX state, **if neither a cross-packed transition nor a neutral equality exchange is present, no five-witness can lie in `R`.**

This is the first place where the named partner result is used essentially.

## Lemma 2 — a cycle-supported five-witness has exactly one remainder exit

Fix a packed pair, say `Ci,Cj`, and let `Ck` be the complementary packed cycle. Suppose `w in Ck` is a five-witness for `Ci union Cj`.

After deleting `Ci union Cj`, the residual outdegree of `w` is exactly two. Chordlessness of `Ck` says that among vertices of `Ck`, the only outneighbor of `w` is its directed-cycle successor `w+`. Therefore the second residual outarc is forced to a unique vertex of `R`.

Write this unique remainder exit as

`e(w) in R`, with `w -> e(w)`.

Thus every cycle-supported five-witness spends its exact-seven budget as

`5 cross arcs + 1 support-successor arc + 1 remainder-exit arc`.

## Lemma 3 — proper exit footprints force a cross transition or an R-internal same-cycle bypass

Let `C` be one of the chordless packed cycles and let `r in R`. Define the exit footprint

`S_C(r) = {v in V(C) : v -> r}`.

Assume `S_C(r)` is nonempty and proper. Then either there is a genuine cross-packed transition, or there is a directed path with both endpoints on `C` and all internal vertices in `R`.

### Proof

Because `S_C(r)` is a nonempty proper subset of a directed cycle, choose `w in S_C(r)` whose predecessor `p=w-` on `C` is not in `S_C(r)`.

The arc `w->r` is dominated, so some vertex `d` satisfies

`d->w` and `d->r`.

The dominator `d` cannot lie on `C`. Indeed, chordlessness of `C` implies that the only vertex of `C` sending to `w` is its predecessor `p`; but `p` was chosen not to send to `r`.

If `d` lies on another packed cycle, `d->w` is already a cross-packed transition.

Otherwise `d in R`, and `d->r` is an internal remainder arc. Apply account02/B05's domination-ladder lemma to `d->r`. Acyclicity of `R` forces the backward domination process to terminate at an apex `z` on a packed cycle, with a directed ladder

`z -> ... -> d -> r`

whose internal vertices lie in `R`. Replace the last ladder edge `d->r` by the simultaneously available edge `d->w`. This gives a directed path

`z -> ... -> d -> w`.

If the apex cycle of `z` is not `C`, this is a cross-packed transition ending on `C`. If `z in C`, it is an `R`-internal path from `C` back to `C`; if `z=w`, it is a closed directed return through `R`. In either case it is a legitimate same-cycle bypass/exchange input. QED.

For distinct endpoints `z,w in C`, global minimum of the three-packing gives the usual exact tax: if `ell` is the path length and `d_C(z,w)` the forward directed distance on `C`, then `ell>=d_C(z,w)`. Equality is a size-neutral exchange; strict inequality is a strict collar rather than an immediate contradiction.

## Lemma 4 — in the absence of cross/bypass geometry, all opposite-pair five-witnesses on a support cycle share one universal exit

Assume `|R|=4`, global NO-SIX, and suppose there is neither a cross-packed transition nor an `R`-internal same-cycle bypass. By Lemma 1, there is then no `R`-supported five-witness. Therefore for each packed pair, all of its at least three required five-witnesses lie on the complementary packed cycle.

Fix one complementary cycle `C`. Each of these cycle-supported witnesses has its unique exit `e(w)` by Lemma 2.

For any exit value `r=e(w)`, the footprint `S_C(r)` is nonempty. Lemma 3 and the assumed absence of cross/bypass geometry force

`S_C(r)=V(C)`.

There cannot be two distinct exit values `r != r'` among the five-witnesses on `C`: if both occurred, the preceding equality would imply that every vertex of `C` points to both `r` and `r'`, whereas each five-witness on `C` has exactly one remainder outarc by Lemma 2.

Hence there is a unique vertex `r_C in R` such that

- every opposite-pair five-witness on `C` has exit `r_C`; and, more strongly,
- **every vertex of `C` sends an arc to `r_C`.**

Call `r_C` the universal exit of `C`.

This is the dependency-aware replacement for the false idea that witness exits can simply be chosen independently.

## Lemma 5 — three universal exits are impossible when `|R|=4`

Continue under the assumptions of Lemma 4. For each packed cycle `C`, let `r_C` be its universal exit and put

`q_C = d_R^+(r_C)`.

Because every vertex of `C` sends to `r_C` and the normal form is oriented, `r_C` sends no arc back into `C`. Exact outdegree seven therefore gives

`|N^+(r_C) intersect (V(C_i) union V(C_j))| = 7-q_C`,

where `Ci,Cj` are the other two packed cycles.

Global NO-SIX implies `7-q_C<=5`, so `q_C>=2`.

If `q_C=2`, then `r_C in R` has exactly five outneighbors in the other two packed cycles, i.e. `r_C` itself is an `R`-supported five-witness for that opposite pair. This contradicts Lemma 1 under the current no-cross/no-neutral branch. Thus

`q_C>=3`.

Since `|R|=4`, necessarily `q_C=3`.

An acyclic oriented digraph on four vertices has at most one vertex of outdegree three: two such vertices would have to send to one another, creating a digon (and in particular a directed cycle). Therefore

`r_C1 = r_C2 = r_C3 =: r`.

But every vertex of all three packed cycles sends to this common `r`. Orientation then forbids `r` from sending to any packed-cycle vertex. Its only possible outneighbors are the other three vertices of `R`, so

`d_D^+(r) <= 3`,

contradicting the exact outdegree-seven normal form. QED.

## The four-remainder escape theorem

Combining Lemmas 1--5 gives the reusable step:

> **BT4-COUNT-v3-FOUR-R-ESCAPE.** In the inherited exact-seven, oriented, globally minimum three-cycle-packing normal form, a global-NO-SIX state with `|R|=4` cannot be featureless. At least one of the following must occur:
>
> 1. a genuine cross-packed transition;
> 2. a neutral minimum-packing exchange supplied by an `R`-supported five-witness equality collar; or
> 3. an `R`-internal path joining two vertices of one packed cycle (possibly a closed return), produced by a proper exit footprint.
>
> For the distinct-endpoint form of (3), global packing minimality gives `ell>=d_C`; equality is another neutral exchange and strictness is a strict collar.

The theorem does **not** assume anything about the number of sinks of `R`. In particular it applies to, and removes the featureless possibility from, the lead's live `|R|=4, s<=2` NO-SIX branch.

## Compact conditional end-to-end route after this step

The lead's current conditional BT4 proof has three universal unpaid closures: the SIX branch, cross-linkage/two-cycle-splice closure, and long neutral-orbit closure. The present theorem plugs the small-remainder NO-SIX branch into that same geometry rather than leaving it as an additional fourth obstruction.

Indeed, assume a minimum counterexample. The pair-deletion deficit puts each globally minimum packing state into SIX or NO-SIX. SIX still goes to the lead's six-fan closure. In NO-SIX with `|R|=4`, the theorem above forces either an actual cross-packed transition or an explicit neutral/strict bypass object. Equality moves to another globally minimum packing and regenerates all pair deficits; a strict bypass is an input to the support-correct segment/cross-linkage machinery. Thus a four-remainder state cannot persist merely because all deficit witnesses sit on packed cycles with correlated exits.

For `|R|>=5`, or after a forced bypass/cross transition, the existing cross-linkage and neutral-orbit obligations remain. Therefore this is not a target-level proof, but it directly pays the lead's first isolated small-remainder structural gap.

## Failure boundary and adversarial checks

- I do **not** claim that a strict same-cycle bypass alone yields four cycles. Its disjoint two-cycle reconstruction remains part of the lead's cross-linkage obligation.
- I do **not** close the SIX branch.
- I do **not** infer independent witness exits. The proof does the opposite: if exits are too dependent, domination plus chordlessness forces a universal-exit structure, and that structure contradicts exact outdegree seven when `|R|=4`.
- The proof uses the cycle-supported/remainder-supported split explicitly; no cycle-supported witness is fed into a remainder-only collar lemma.
- The exact account03/B06 20-vertex sharpness certificate is consistent with this result: it has a larger remainder (`|R|=8`) and therefore does not contradict the four-remainder theorem.
- No computation is used in the proof.
- Digons are allowed in the original conjecture; the use of orientation is confined to the inherited minimum-counterexample normal form in which digons have already been eliminated by the lead's reduction.

## Honest status

`ESSENTIAL_STEP_APPLIED`.

New proved step: every global-NO-SIX state with exactly four remainder vertices necessarily exports a cross-packed transition or an explicit neutral/strict `R`-bypass object; the previously possible-looking configuration in which all required five-witnesses remain cycle-supported with arbitrarily correlated exits is impossible.

Full BT4 remains OPEN / NOT PROVED. The next mathematical obligation is to consume the forced cross/bypass object with the team's support-correct two-cycle reconstruction, while the SIX branch remains separate.
