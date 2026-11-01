# B06 controlling strengthening — global exclusion of the transitive slide

Run: `b06-20260922T052855Z-e8af6c7c2c69`  
Candidate revision: `BT4-HT-ARCMAX-CAGE-COLLAPSE-v2`  
Classification: `ESSENTIAL_STEP_APPLIED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

This addendum is controlling over the same-run primary report `report.md` at commit `8d2b1f93ec4dcd73d802fc5a1eacd4a69f8b36c6`, blob `749fdea9d8a7a1508c13878452324bcb3ac2b510`.

The primary report deliberately retained a transitive-slide equality branch because the remainder-arc potential alone does not exclude it. After that report was published, I source-read a newer compatible OTHER-account result, fleet04/B05 `BT4-HT-XFREE-HALL-v1`, run `b05-20260922t051421z-r34`, handoff blob `1ac9d889a7aba352f13e6d43b19c376a679d7a3c`. Its explicit global no-four-pack certificates show that one arc used by the local slide adversary, `r0->r2`, cannot occur in a genuine counterexample. I independently checked the displayed cycles below. Thus the local adversary remains valid only for its stated purpose—refuting a *purely local* implication—and the true counterexample branch is stronger.

## Exact global correction

Retain the lead's exact-two-predecessor cage:

`H=h0->h1->h2->h0`, `R={x,r0,r1,r2}`,  
`hi->ri->x->hi`,  
`r0->r1,h1,x`, `r1->r2,h2,x`,  
`N^+_{H∪R}(h1)={h2,r1}`,  
`N^+_{H∪R}(h2)={h0,r2}`,  
`N^+_{H∪R}(r2)={x,h0}`.

### Lemma 1 — `r0->r2` is globally impossible

If `r0->r2`, then

`C = h0 -> r0 -> r2 -> h0`

and

`C' = h1 -> r1 -> x -> h1`

are vertex-disjoint directed triangles. They are also disjoint from the untouched packed light cycles `S,U`. Hence `C,C',S,U` are four vertex-disjoint directed cycles, contradiction.

Acyclicity of `R` already forbids `r2->r0`. Therefore `r0,r2` are nonadjacent.

Consequently the old remainder has exactly five arcs:

`r0->r1`, `r1->r2`, and `ri->x` for `i=0,1,2`.

Thus `Phi(P)=5`, not six.

### Lemma 2 — the last optional arc `h0-r1` is also absent

Use the neutral triangle

`T2=h2->r2->x->h2`

to replace `H`. Its exchanged remainder is

`R2={h0,r0,h1,r1}`

with five forced arcs

`h0->r0`, `r0->h1`, `h1->r1`, `h0->h1`, `r0->r1`.

If `r1->h0`, then even before invoking the potential there are four disjoint cycles:

`r1 -> h0 -> h1 -> r1`,  
`h2 -> r2 -> x -> h2`,  
`S`,  
`U`.

So `r1->h0` is impossible.

If `h0->r1`, then `R2` has six induced arcs. But `T2,S,U` is an equal-size globally minimum packing and the original packing was chosen, among minimum-total packings, to maximize the remainder-arc potential. Since the old remainder has exactly five arcs, `Phi(P2)=6>5=Phi(P)` is impossible.

Therefore `h0,r1` are nonadjacent.

### Corollary 3 — four exact five-witnesses

Inside `G=D[V(H)∪R]`, the lead already gave residual outdegree two for `h1,h2,r2`. Lemma 2 now gives

`N_G^+(h0)={h1,r0}`

as well.

Exact outdegree seven yields

`|N^+(v)∩(S∪U)|=5`

for every

`v in {h0,h1,h2,r2}`.                                      (1)

Thus all three heavy-triangle vertices are cycle-supported exact five-witnesses for the fixed light pair, and `r2` is a fourth, remainder-supported exact five-witness.

Among `h0,h1,h2`, choose a heavy light target for each. There are only two light cycles `S,U`, so two of the three cycle-supported witnesses are heavy on the same target. The exact-two-predecessor cage therefore always enters the campaign's same-heavy interface; there is no genuine transitive-slide exception.

## Named fleet03/B04 partner applied: the fourth witness is clean

Let `A in {S,U}` be any heavy target of the remainder witness `r2`, so

`|N^+(r2)∩A|>=3`.

Suppose some `t in A` satisfied `t->r2`. The named partner fleet03/B04 `BT4-R4-F3-TWOFAN-COLLAPSE-v1` proves the generic minimum-packing inport localization:

if `t->q` from a packed cycle `A`, then all `q`-targets on `A` lie in `{t+,t++}`.

Applying it with `q=r2` would force at most two `r2`-targets on `A`, contradicting heaviness. Hence

`A not->r2`.                                                  (2)

So the four-witness cage contains not merely a same-heavy cycle-supported pair, but also a remainder-supported exact-five witness whose heavy target is completely free of inarcs into it.

## Relation to the newer fleet04/B05 Hall result

The newer compatible fleet04/B05 handoff goes farther in a different direction: using the same four-witness cage, domination, and the lead's heavy-target no-inport theorem, it constructs x-free cross transitions from the three `h_i` and reduces the pair of same-heavy cycle-supported witnesses to either distinct target representatives with disjoint remainder interiors or an exact common-extra-port collision. It then applies a collar theorem to `r2`.

This addendum does not duplicate that Hall/collar proof. Its new source-bound contribution is the clean conclusion (2) attached to the exact remainder witness via the named fleet03/B04 inport-localization theorem, while correcting the primary report's equality branch with the global four-pack certificate.

## Corrected first unpaid implication

The true local frontier is now `HT-PORT-CLOSE`, not transitive-slide termination:

- three cycle-supported exact five-witnesses `h0,h1,h2`;
- two of them heavy on one common light target;
- a fourth remainder-supported exact five-witness `r2`;
- every chosen heavy target of `r2` has no inarc into `r2`;
- compatible fleet04/B05 supplies either a distinct-port x-free pair with disjoint remainder interiors or the exact common-extra-port collision, plus a cross/equality return from the fourth witness.

The next implication is to turn one of those two port configurations together with the clean fourth-witness return into a legal two-cycle splice, a strict lexicographic packing reduction, a directed cycle in the exchanged remainder, a SIX exit, or the fourth disjoint directed cycle.

The primary report's 16-vertex exact graph is still a valid `CANDIDATE_REFUTED` witness against the false *local* claim that equal-six-arc transitive remainders are structurally impossible: that graph explicitly has a four-pack and therefore is excluded precisely by Lemma 1. The highly asymmetric digon example and its sharp threshold-five deletion conclusion are unchanged.

No full BT4 proof or novelty claim is made.
