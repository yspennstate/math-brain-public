# BT4 account02/B04 — correction and peer-integrated third-cycle witness collar

Run: `20260922T001806Z-b04-bt4-a1ceeb3c`
Status: `ESSENTIAL_STEP_APPLIED_WITH_CORRECTION`
Brain status: `WITHOUT_VERIFIED_BRAIN`

This is an immutable correction/addendum to the same run's `report.md` (commit `a95b20d733b75b91a40c16c2faa225846f54973e`, blob `d82fc84180bc66fd660c6c79f9a7f26332bdae72`). The original report remains preserved. No target-level proof is claimed.

## Later compatible control and peer snapshots consumed

During the run, fresh main advanced to owner-control revision `2026-09-22.2`. That later control keeps B04 on the same BT4 collective-research assignment and introduces no stop for this slot.

Two exact later OTHER-account snapshots materially affect the argument:

1. account01/B04 `BT4-MCR-v2`, complete report commit `6784701dec457ccf70a7d33151ae06770f04658a`, blob `79c91a55da8f23489bf3a18c8fc874e588b5ce12`, shared handoff blob `30622855b617296a4430c0073244c39c44516f58`.
2. account03/B04 repaired seven-budget split, shared handoff blob `4c16f36c8a711b9730a5abf2ed529cd967329c53`. It records complete report commit `0ea8fe6265827eb76c5fb8f15cd7f6ee092e9003`, blob `c301702a30b2c9a55fb6f07d63a8b084ff47a888`.

## Correction 1 — quarantine the overbroad equality-exchange sentence

The main report correctly uses the account01 one-vertex exchange for a **direct** arc `b->x`, and its light-return lemma is sound. However, its Step 8 stated too broadly that equality `m=L+1` in a general `R`-internal return path automatically forces the fan to be exactly the first `L+1` successors of `b`.

The account01/B04 v2 repair identifies the exceptional fan target `b` itself. For a path

`P: b=p0 -> p1 -> ... -> p_L=x`

with internal vertices in `R` and `m=|N+(x)∩C|`, minimum packing shows only that every fan target `a!=b` lies among the first `L+1` successors of `b`. The additional possibility `x->b` must be handled separately. Under a *strict-short-return contradiction* `L<=m-2`, `P+x->b` would have length `L+1<m<=|C|`, hence would shorten the packing, so `x->b` is impossible and the corrected path-fan conclusion `L>=m-1` follows. At the equality boundary `L=m-1`, that strict argument no longer excludes `x->b`.

Therefore the general neutral-exchange assertion from Step 8 is **quarantined unless `x->b` is independently known to be absent**.

A repaired version is valid:

> If `x->b` is absent and `m=L+1`, then the fan is exactly the first `L+1` successors of `b`, and the cycle obtained by replacing those `L` intervening cycle vertices with the `L` remainder vertices is a size-preserving packing exchange.

The direct light-return special case used elsewhere in the report remains valid without extra work: when `L=1` and `b->x`, the exact-seven counterexample is oriented, so `x->b` is impossible by absence of digons. Hence if that light cycle has fan `m=2`, the equal-size exchange replacing `b+` by `x` is valid.

This correction does not weaken the strict short-return target `L<=m-2`; account01/B04 v2 proves that target still contradicts minimum packing.

## Correction 2 — witness location matters in the pair-deletion dichotomy

The main report's sharp pair-deletion dichotomy is valid: in the exact-seven spanning counterexample, for every pair of packed cycles `Ci,Cj`, the remainder after deleting them contains either a vertex of residual outdegree at most one (a pair fan of at least six) or at least three vertices of residual outdegree exactly two (each a pair fan of exactly five).

But account03/B04 correctly records a location trap: such a witness may lie on the **third packed cycle `Ck`**, not in the DAG remainder `R`. The one-vertex minimum-packing exchange cannot then be applied as though that witness were a remainder vertex, because a replacement cycle through the witness may intersect `Ck`.

In the exact-seven/global-minimum normal form of this run, a third-cycle witness has an exact structure because `Ck` is chordless:

- six-fan witness `z in Ck`: its only residual outarc after deleting `Ci,Cj` is the cycle-successor `z+`; therefore it has **no outarc to `R`**;
- five-fan witness `z in Ck`: residual outdegree is exactly two, namely the successor `z+` plus **one unique outarc `z->r` with `r in R`**.

Thus the safe pair-witness split is: `R`-supported witnesses may feed the one-vertex/path-fan machinery; third-cycle-supported witnesses require a genuine two-cycle exchange.

## New lemma — the five-fan third-cycle witness has a canonical sink collar

This is the new inference added after applying account03/B04's repair to the exact-seven normal form.

Let `z in Ck` be a five-fan witness for the pair `Ci,Cj`. By the preceding exact structure, `z` has a unique outarc `z->r` into `R`. Since `D[R]` is a finite DAG, extend from `r` along outgoing arcs inside `R` until reaching a sink `x` of `D[R]`. Hence there is a canonical directed path

`z -> r -> ... -> x`

whose internal vertices lie in `R` and whose first vertex lies on the complementary packed cycle `Ck`.

At the terminal sink `x`, the light-return lemma from the main report applies: because every arc is dominated, `D[N-(x)]` contains a directed cycle; since `R` is acyclic, some packed cycle `C_l` has an arc `b->x`, and the one-vertex exchange forces

`|N+(x)∩C_l| <= 2`.

So every third-cycle **five-fan** saturation witness comes with a source-valid two-ended collar:

`Ck --(unique exit)--> R ... -> x <-- C_l`, with `x` receiving a direct arc from a light packed cycle.

If `l=k`, the corrected path-fan lemma applies to the `Ck`-to-`x` collar and constrains its length relative to `|N+(x)∩Ck|`; if `l!=k`, the collar is already a cross-cycle object suitable for the required two-cycle splice. No claim is made that either alternative by itself closes BT4.

By contrast, a third-cycle **six-fan** witness has no `R` exit at all, so this collar mechanism is unavailable there. That rigid branch must be attacked using its six cross-arcs, the cycle successor, and/or missing-arc saturation certificates.

## Corrected live candidate

The conditional end-to-end proof remains:

1. obtain the global minimum three-cycle packing with DAG remainder in a minimum counterexample;
2. a heavy sink/cycle strict return of length at most `m-2` contradicts the corrected path-fan lemma;
3. otherwise use pair-deletion witness amplification to force a disjoint two-cycle exchange or to reach a remainder satisfying the strengthened `k=2` degree-sequence theorem.

The first missing inference is now split honestly into two source-valid branches:

- **all-R branch:** exploit the multiplicity of five/six-fan witnesses that actually lie in `R` to force a strict short return or a legal exchange;
- **third-cycle saturation branch:** for a five-fan witness use the canonical sink collar above to build a two-cycle splice, while for a six-fan witness use the exact `6-cross/0-R-exit` rigidity to build the splice directly or prove the branch impossible.

This is narrower than the original unexplained short-return obligation and avoids both known traps: the exceptional `x->b` equality case and treating a third-cycle witness as a remainder witness.

## Honest outcome

`ESSENTIAL_STEP_APPLIED_WITH_CORRECTION`. The direct light-return lemma, exact eight sink fan types, exact-seven arc domination, 3-vertex-connectivity, and pair-deletion dichotomy from the main report survive. The overbroad general equality-exchange sentence is not to be used without the explicit `x->b`-absent hypothesis. The new five-fan sink-collar lemma is auxiliary but directly targets the remaining two-cycle exchange branch.
