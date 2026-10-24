# BT4 account02/B20 — cross-cycle collar and six-fan port-triangle reduction

Run: `20260922T013238Z-account02-B20-bt4-r11`
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`
Campaign: `BT4`
Outcome: `ESSENTIAL_STEP_APPLIED`
Target-level change: `NONE` — no full proof of k=4 is claimed.
Mechanism change: `YES` — the surviving neutral cycle-supported branch gains a cross-cycle distance collar; its symmetric six-fan `(3,3)` subbranch collapses to a three-port directed triangle with a forced triple-dominator, and the remainder-supported triple-dominator feeds directly into the named partner's fan-avoiding saturation certificate.
Brain status: `WITHOUT_VERIFIED_BRAIN`.

## Exact target and source discipline

Target: every finite loopless digraph `D`, with at most one arc per ordered pair of distinct vertices and minimum outdegree at least seven, contains four pairwise vertex-disjoint genuinely directed cycles. Opposite arcs and directed digons are allowed by the source problem. The extremal counterexample normal form used below is oriented only because the already-proved minimal-counterexample reduction eliminates digons inside a hypothetical counterexample.

No edge-disjoint surrogate, nearly-directed cycle, one-reversed-arc relaxation, larger degree threshold, bounded-order search, or routine subclass is substituted for this target.

Fresh scientific master consumed: `251d29fd53dcbaa31df0f9b550871bf2e315f87c`.

## Exact inputs consumed

Lead package:

- `proofnet24/collective-BT4/account02/B04/20260922T001806Z-b04-bt4-a1ceeb3c/report.md`, blob `d82fc84180bc66fd660c6c79f9a7f26332bdae72`;
- its correction/addendum `correction.md`, blob `ef92cfc95fab44c1e256757de5fae4ec4b28e36b`.

Named completed OTHER-account partner result actually used:

- `proofnet24/collective-BT4/account04/B06/20260922T001024Z-b06-bt4-r43/report.md`, blob `08cf8f4283de825d533677d6edf5707523744a22`.

That result supplies the missing-arc saturation lemma: if `x,b` are nonadjacent in the vertex-minimal/arc-maximal counterexample, adding `x->b` produces three directed cycles disjoint from a directed `b`-to-`x` path `P`, and `P-{x}` avoids the full outneighborhood `N+(x)`.

Compatible linkage input:

- account03/B05 `linkage_addendum.md`, blob `f1545c2e4a546d17150bb20bbc59650a29eb2672`;
- corrected Menger proof `linkage_correction.md`, blob `f19feaaea52a2a892e510bd8fe03dbb18290fcb5`.

Prior own mechanism state:

- account02/B20 `20260922T010226Z-account02-B20-r11/report.md`, blob `84451c87a169ff1fb2d75188c0e2b498005a0428`.

Only two earlier substantive account02/B20 BT4 reports exist in the fresh archive, so a three-prior-run stagnation trigger is not available. Both earlier runs made mechanism changes; no unchanged-three-run pivot is claimed.

## Conditional end-to-end candidate before this run

Assume BT4 false and take the current extremal normal form: a vertex-minimal, then arc-maximal counterexample, sparsified to exact outdegree seven while preserving a globally minimum-total packing `(A,B,C)` of three directed cycles. The remainder `R` is acyclic; the packed cycles are chordless; every arc is dominated; the digraph is 3-vertex-strong.

For a sink of `R`, exact-seven fan accounting and the corrected path-fan lemma reduce the proof to forcing a strict heavy-cycle return or an equivalent disjoint splice. Pair deletion plus the strengthened `k=2` theorem produces exact five/six-fan witnesses. A five-fan witness on the complementary packed cycle has exactly one `R` exit; a six-fan witness has none. Account03/B05 turns 3-connectivity into an `R`-bypass / two-packed-cycle-linkage trichotomy around a cycle-supported heavy witness.

For an `R`-internal bypass `Q` of a proper `B`-segment `S` containing a heavy witness `w`, write

- `s=|S|`,
- `ell=length(Q)`,
- `m=|N+(w)∩A|>=3`,
- `b in A` with `b->w`.

The corrected marked-segment exchange gives

`ell >= m+s-1`.

The hard equality branch is

`ell = m+s-1`.                                             (E)

The prior B20 run chose, among minimum-total packings, one minimizing `Phi=|A|^2+|B|^2+|C|^2`, and proved that under (E):

1. `|A|-|B| <= m-2` when `B` is the source cycle in the exchange;
2. the heavy target `A` has exactly one inport to `w`;
3. 3-vertex-strongness forces an additional inlink into `w` from `R union C`;
4. for a five-fan witness with unique exit `w->r` to `R`, if that extra inlink is `y->w` with `y in R`, then there is no `r`-to-`y` path in `R-int(Q)`.

Thus the first unpaid implication is no longer an arbitrary exchange orbit: one must eliminate or splice the near-balanced, unique-inport equality cage.

## Lemma 1 — cross-cycle collar at neutral equality

Assume (E). Let `c in C` satisfy `c->w`, and put

`n = |N+(w)∩C|`.

For every `d in N+(w)∩C`, let `q=d_C(d,c)` be the directed distance in edges from `d` forward along `C` to `c`. Then

`q >= |C|-m`.                                               (1)

Equivalently,

`d_C(c,d) <= m`,                                            (2)

so every outneighbor of `w` on `C` lies among the first `m` successors of the inport `c` on `C`.

### Proof

Let `B_Q` be the bypass cycle obtained by replacing the segment `S` of `B` with `Q`. It has

`|B_Q| = |B|-s+ell-1`.

For any `d in N+(w)∩C`, the arcs `c->w` and `w->d`, followed by the directed `C`-path from `d` to `c`, form a genuinely directed cycle

`W_{c,d} = c -> w -> d -> C[d,c]`

of size `q+2`. The cycles `A`, `B_Q`, and `W_{c,d}` are pairwise vertex-disjoint: `B_Q` omits the entire segment `S` and hence omits `w`, its new internal vertices lie in `R`, and `W_{c,d}` otherwise uses only `C`.

Global minimum of the total size of a three-cycle packing therefore gives

`|A| + (|B|-s+ell-1) + (q+2) >= |A|+|B|+|C|`,

hence

`ell+q+1 >= s+|C|`.

Using the neutral equality `ell=m+s-1` yields `q>=|C|-m`, proving (1), and the complementary cyclic distance identity gives (2). QED.

### Equality consequence

If `n=m`, then necessarily

`N+(w)∩C = {c^+, c^{++}, ..., c^{+(m)}}`,                  (3)

and `c` is the unique vertex of `C` sending an arc to `w`.

Indeed, (2) gives `m` distinct outneighbors inside an `m`-vertex forward window, so the window is filled. It is proper: if `|C|=m`, the last listed vertex would be `c`, contradicting orientation because `c->w`. A proper cyclic interval has a unique predecessor. Any second inport `c'->w` would, by the same argument, have to be the predecessor of the same interval, hence `c'=c`.

This is the exact cross-cycle analogue of the unique-inport phenomenon on the heavy target. It is not a degree average; it comes from a legal disjoint three-cycle replacement.

## Lemma 2 — the symmetric `(3,3)` six-fan equality is double-neutral and near-balanced

Assume `w in B` is a **six-fan** witness for the pair `A union C`, so exact outdegree seven and chordlessness of `B` give

`N+(w) = {w^+} union (N+(w)∩A) union (N+(w)∩C)`

and `w` has no outarc to `R`.

Suppose the split is

`|N+(w)∩A| = |N+(w)∩C| = 3`,                              (4)

and the bypass `Q,S` satisfies neutral equality (E) for target `A`. If `w` has no inneighbor in `R`, then:

1. there is an inport `c in C` with `c->w`;
2. `c` is the unique `C`-inport and the three `C`-fan vertices are exactly `c^+,c^{++},c^{+++}`;
3. the **same** bypass is neutral for target `C` as well;
4. if `B` is a shortest cycle in the chosen `Phi`-minimum packing, then

`|A|, |C| in {|B|, |B|+1}`.                              (5)

### Proof

The prior unique-inport lemma supplies a unique `A`-inport `b->w`. Chordlessness of `B` supplies exactly one `B`-inport, namely `p=w^-`. Since the digraph is 3-vertex-strong, `d-(w)>=3`. The prior third-side lemma says an additional inlink comes from `R union C`; by the present no-`R`-inlink assumption, one comes from `C`.

Lemma 1 with `m=n=3` gives the exact consecutive `C` fan and uniqueness of `c`.

The account03 marked-segment inequality applied with target `C` now reads `ell>=3+s-1`. But the original neutral equality for `A` is already `ell=3+s-1`, so equality also holds for target `C`.

The prior quadratic confinement applied once with target `A` gives `|A|-|B|<=1`; applied again with target `C` gives `|C|-|B|<=1`. Since `B` was chosen shortest, both differences are nonnegative, proving (5). QED.

So the hardest symmetric six-fan equality does not retain arbitrary cycle lengths: unless an `R`-inlink exists, all three packed cycles are balanced to within one vertex and both heavy targets are simultaneous neutral exchanges through the same bypass.

## Lemma 3 — the three inports form a directed triangle

Continue under Lemma 2 and put

`T={p,b,c}`, where `p=w^-`.

Then `D[T]` is a directed 3-cycle.

### Proof

Under the no-`R`-inlink hypothesis and the uniqueness conclusions above,

`N-(w) = {p,b,c}`.                                         (6)

Every arc of the extremal exact-seven counterexample is dominated. For each `t in T`, apply arc domination to `t->w`. Its dominator `z` satisfies both `z->t` and `z->w`; by (6), `z` lies in `T-{t}`. Hence every vertex of `D[T]` has indegree at least one.

A finite digraph on three vertices with minimum indegree at least one contains a directed cycle. The extremal counterexample is oriented, so there is no digon; therefore the cycle has length three and uses all of `T`. QED.

This converts the abstract equality cage into an actual short directed cycle crossing the three packed cycles.

## Lemma 4 — a triple-dominator of the port triangle is forced

Under the same hypotheses, there is a vertex

`q in V(D)-T`

with

`q->p, q->b, q->c`.                                       (7)

Moreover, by chordlessness of the packed cycles, `q` lies in exactly one of the following four location classes:

`q in R`, `q=b^- in A`, `q=c^- in C`, or `q=p^- in B`.    (8)

### Proof

The directed triangle `T` is already one directed cycle. If `D-T` had minimum outdegree at least five, the known `k=3` Bermond-Thomassen theorem would give three pairwise vertex-disjoint directed cycles in `D-T`; together with `T` these would be four disjoint directed cycles in `D`, contradiction.

Therefore some `q outside T` has

`d+_{D-T}(q) <= 4`.

But the exact-seven normal form has `d+_D(q)=7`, and only the three vertices of `T` were deleted. Thus `q` must lose all three outgoing arcs, proving (7).

If `q` lies on `A`, chordlessness of `A` and `q->b` force `q=b^-`. The same argument gives `q=c^-` on `C` and `q=p^-` on `B`. Otherwise `q` lies in `R`. QED.

This is a genuinely global consequence of the source-valid `k=3` theorem: the port triangle cannot sit in the counterexample without a vertex simultaneously dominating all three ports.

## Lemma 5 — the remainder location feeds the named partner's saturation certificate

If the forced vertex `q` in Lemma 4 lies in `R`, then the exact account04/B06 missing-arc saturation lemma applies to the pair `(w,q)` and yields three vertex-disjoint directed cycles `K1,K2,K3` and a directed path

`P: q -> ... -> w`

such that:

1. `P` is disjoint from `K1 union K2 union K3`;
2. `P-{w}` avoids `N+(w)`;
3. `|V(P)| <= |R|`;
4. the penultimate vertex of `P` is one of the three ports `p,b,c`.

### Proof

A six-fan witness has no outarc from `w` to `R`. Equation (6) gives `q not->w`, so `w,q` are nonadjacent. The named partner's Lemma 8 therefore applies directly and gives items 1-2.

Because `q not->w`, the path has at least two edges and hence at least three vertices. The three `K`-cycles leave all vertices of `P` uncovered. Global minimum of the old three-cycle packing gives

`|A|+|B|+|C| <= |K1|+|K2|+|K3| <= |V(D)|-|V(P)|`.

Since `|R|=|V(D)|-(|A|+|B|+|C|)`, this yields `|V(P)|<=|R|`, proving item 3. Finally, the predecessor of `w` on `P` is an inneighbor of `w`, and (6) gives item 4. QED.

This is the promised substantive use of the named completed OTHER-account result. The remainder-supported triple-dominator is not left as an abstract degree witness: it immediately produces a bounded fan-avoiding saturation path plus a disjoint replacement three-packing, funneled through one of exactly three ports.

## Five-fan side consequence

Lemma 1 also completes the structural alternative left by the prior five-fan reachability lemma. If a neutral five-fan witness `w in B` has target `A` fan `m>=3`, unique exit `w->r` to `R`, and its forced third-side inlink is:

- `y->w` with `y in R`, then the prior run proves there is no `r`-to-`y` path in `R-int(Q)`;
- `c->w` with `c in C`, then every `C`-outneighbor of `w` lies in the first `m` successors of `c` by Lemma 1.

Thus both locations of the compulsory third-side inlink now carry an explicit disjointness restriction. This still does not close the five-fan branch.

## Exact before/after and first remaining implication

Before this run, the neutral equality cage was known to have a unique heavy-target inport, a third-side inlink, a near-balance constraint, and (for a five-fan with an `R` inlink) one forbidden reachability relation.

After this run:

- every cross-cycle inport in a neutral equality collars the opposite fan into an explicit forward window of length `m`;
- the symmetric six-fan `(3,3)` branch with no `R` inlink is **double-neutral**, has all three cycle lengths within one, and has exactly three inports to `w`;
- those three inports form a genuine directed triangle `T`;
- avoiding immediate BT4 closure after deleting `T` forces a vertex `q` dominating all three ports;
- chordlessness reduces `q` to four exact locations: `R,b^-,c^-,p^-`;
- in the `q in R` location, the named account04/B06 saturation lemma supplies a bounded fan-avoiding `q`-to-`w` path and three disjoint replacement cycles, with the path forced through one of the three ports.

The first unpaid universal implication is correspondingly smaller:

> Eliminate the four triple-dominator locations in (8), or splice one of them into four genuinely directed vertex-disjoint cycles. In the `q in R` case this means combining the partner's fan-avoiding saturation certificate with the three-port triangle; in the three cycle-predecessor cases it means exploiting the forced cross-arcs from `b^-`, `c^-`, or `p^-` to the other two ports without losing vertex-disjointness. The asymmetric six-fan splits `(4,2),(5,1),(6,0)` and the five-fan cage remain separate live branches.

This is not yet a universal proof of the original missing implication, so no target-level promotion is made.

## Stagnation / next method

The two prior B20 BT4 runs and this run all change mechanism: first fan-only abstractions were refuted/narrowed, then neutral equality was confined by a quadratic potential and inport/reachability constraints, and now the symmetric six-fan equality is reduced to an actual port triangle plus a forced triple-dominator and partner saturation funnel. The same exact implication has therefore not remained unchanged for three substantive runs.

Next method: attack the four exact locations in (8), beginning with `q in R` by using the partner saturation path and its three disjoint cycles; do not repeat static fan counts. For the cycle-predecessor locations, use the explicit directed port triangle and the three forced `q` cross-arcs to attempt simultaneous two-cycle surgery. Treat asymmetric six-fans and five-fans separately if this symmetric branch closes.

## Status

`ESSENTIAL_STEP_APPLIED`, not `FULL_PROOF_CANDIDATE`.

No claim of BT4 closure, unrestricted Bermond-Thomassen closure, or literature novelty is made.
