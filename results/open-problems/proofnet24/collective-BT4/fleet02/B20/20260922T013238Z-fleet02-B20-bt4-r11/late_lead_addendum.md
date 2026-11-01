# BT4 fleet02/B20 late-lead addendum — two-pivot fork in the no-six linkage branch

Run: `20260922T013238Z-fleet02-B20-bt4-r11`
Status: `ESSENTIAL_STEP_APPLIED`
Target-level change: `NONE`.

This immutable addendum records research that became necessary after the scientific master advanced during the same invocation. It does not modify or retract `report.md`; the six-fan port-triangle lemmas there remain a separate attack on the lead's six-fan closure statement.

## Later exact dependencies consumed

Fresh scientific master: `78d3b49ef1610c2175c40c8a0952a84817486572`.

Newest campaign-lead report now available:

- `proofnet24/collective-BT4/fleet02/B04/20260922T011943Z-b04-bt4-r11/report.md`, blob `ee3294c169f9736cd8f0fdb943b5cefab5906a9e`, outcome `ESSENTIAL_STEP_APPLIED`.

Its live conditional proof has three explicit unpaid closures: six-fan closure, cross-linkage closure, and long neutral-orbit closure. Its new off-pivot witness lemma says that in the global no-six `(3,2,2)` sink regime, a neutral light pivot either creates a six-fan or regenerates a five-witness for the complementary pair on a vertex outside the pivot pair.

Newest named OTHER-account partner report:

- `proofnet24/collective-BT4/fleet04/B06/20260922T011432Z-b06-bt4-r11/report.md`, blob `44774a85169331dcf5b4cc7d79f3bef31ccb6dbc`, outcome `ESSENTIAL_STEP_APPLIED`.

Its sink-inneighborhood localization says that for a no-six sink `x` with heavy cycle `A` and light cycles `B,C`, either a light cycle has order at most `|R|`, or there are `b in B,c in C` with `b->x,c->x` and a genuine two-way `B`/`C` linkage through `R-{x}`. In the latter branch both direct light returns exist simultaneously.

The result below uses both later reports, not their outcome labels.

## Lemma A — partner linkage creates two distinct neutral pivot directions

Work in the global no-six branch at a sink `x` with fan triple

`(a_A(x),a_B(x),a_C(x))=(3,2,2)`.

Assume the named partner's linkage alternative. Thus there are `b in B,c in C` with `b->x` and `c->x`.

Then

`N+(x)∩B={b+,b++}` and `N+(x)∩C={c+,c++}`,

and both

`B*=b->x->b++->...->b`,

`C*=c->x->c++->...->c`

are globally minimum size-neutral one-cycle replacements.

### Proof

The inherited one-vertex minimum-packing exchange says that for a direct return from a light cycle, its two fan targets must be the first two successors of the return vertex; orientation excludes the reverse arc. Since each light fan has size exactly two, the displayed equalities hold. Each displayed replacement removes one cycle vertex (`b+` or `c+`) and inserts `x`, so it preserves the cycle length and therefore the globally minimum total packing size. QED.

This matters because the partner's linkage alternative does not merely supply one rerouting: it makes the current state branch in two different neutral directions.

## Lemma B — persistent no-six dynamics regenerates two off-pivot five-witnesses

Assume neither pivot enters a six-fan branch when the strengthened `k=2` deficit theorem is reapplied.

After the `B` pivot, there exists a five-witness `z_B` for the pair `A union C` with

`z_B notin {x,b+}`.                                          (B1)

After the `C` pivot, there exists a five-witness `z_C` for the pair `A union B` with

`z_C notin {x,c+}`.                                          (B2)

### Proof

This is the lead's off-pivot witness lemma applied twice. In the `B`-pivot state, `x` itself is a residual degree-two vertex after deleting `A union C`, and the other pivot vertex `b+` is the only vertex paired with it by the canonical reverse move. If the first branch of the strengthened `k=2` theorem does not create a six-fan, there are at least three residual degree-two vertices, so at least one lies outside `{x,b+}`. The `C` pivot is symmetric. QED.

Thus a partner-produced two-way light linkage plus persistent no-six behavior forces two regenerated deficits, one for each complementary pair.

## Lemma C — if the two regenerated witnesses coincide, they lie in the original remainder and have an exact three-type fan profile

Suppose

`z_B=z_C=z`.

Then `z` lies in the original remainder `R-{x}`. Write

`a=|N+(z)∩A|`, `b_z=|N+(z)∩B|`, `c_z=|N+(z)∩C|`,

and `r_z=|N+(z)∩R|`.

There is a number `t in {0,1,2}` such that

`(a,b_z,c_z,r_z)=(5-t,t,t,2-t)`.                            (C1)

In particular the only coincidence types are

`(5,0,0,2)`, `(4,1,1,1)`, `(3,2,2,0)`.                    (C2)

The last type makes `z` a second sink of the original remainder, heavy on the same cycle `A`.

### Proof

A witness for the pair `A union C` must lie outside `A union C`; after excluding the pivot-specific vertices in (B1), its possible original support is `B\{b+}` or `R\{x}`. Similarly a witness for `A union B` satisfying (B2) has original support in `C\{c+}` or `R\{x}`. Since the packed cycles are disjoint, a common witness lies in `R\{x}`.

Its five-fan conditions are

`a+c_z=5`, `a+b_z=5`,

so `b_z=c_z=t` and `a=5-t`. Exact outdegree seven gives

`a+b_z+c_z+r_z=7`,

hence `r_z=2-t`. Nonnegativity gives `t<=2`; clearly `t>=0`, yielding (C1)-(C2). If `t=2`, then `r_z=0`, so `z` is a sink of `D[R]`, and its fan triple is `(3,2,2)` with heavy label `A`. QED.

## Consequence — the long neutral-orbit closure now has a fork/collision alternative

In the named partner's linkage branch, the lead's long neutral-orbit obligation can be sharpened as follows.

After the two neutral pivots supplied by Lemma A, either:

1. one pivot immediately enters the six-fan closure branch; or
2. two **distinct** off-pivot five-witnesses `z_B,z_C` are regenerated for two different complementary pairs; or
3. the regenerated witnesses collide at a single original-remainder vertex `z`, and that vertex has one of the three exact profiles in (C2).

The collision endpoint `(3,2,2,0)` regenerates another no-six sink with the same heavy label, so the named partner's sink-inneighborhood localization applies again at `z`. The other collision profiles have only one or two `R` outarcs, respectively, and are therefore much more rigid than an arbitrary five-witness.

This does not yet close the long neutral orbit or the cross-linkage branch. It does eliminate the possibility that the partner's two-way linkage simply produces two indistinguishable unconstrained copies of the old obstruction.

## Relation to the earlier same-run six-fan result

The original same-run `report.md` proves a separate reduction for a symmetric cycle-supported six-fan `(3,3)` equality cage: its three inports form a directed triangle and a triple-dominator is forced, with the remainder location feeding the earlier fleet04/B06 saturation certificate. The late lead now explicitly lists six-fan closure as one of three missing universal statements, so that result remains directly relevant.

This addendum attacks the other two live statements at their intersection: the newest partner's no-six cross-linkage alternative combined with the newest lead's off-pivot regeneration forces the two-pivot fork/collision trichotomy above.

## First unpaid step after the addendum

Prove that the fork/collision alternative cannot persist without one of:

- a six-fan closure event;
- two compatible cross-packed linkages giving a strict two-cycle exchange or four disjoint directed cycles;
- a strict minimum-packing reduction.

For collision type `(3,2,2,0)`, iterate the partner's localization at the new sink and control overlap of the two linkage cycles. For `(4,1,1,1)` and `(5,0,0,2)`, exploit the one/two `R`-outarc funnels before another neutral pivot; do not replace this by average-degree counting.

Status remains `ESSENTIAL_STEP_APPLIED`, not `FULL_PROOF_CANDIDATE`.
