# BT4 account01/B05 — common-port triangle forces reverse crosses; equality collars are not terminal

Run: `20260922T055714Z-b05-bt4-r11b`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Candidate: `BT4-HT-COMMONPORT-REVERSE-CROSS-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Target status: `OPEN_NOT_PROVED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Exact target and current source boundary

Target: every finite loopless digraph with at most one arc per ordered pair of distinct vertices and minimum outdegree at least seven contains four pairwise vertex-disjoint genuinely directed cycles. Opposite arcs, hence digons, are allowed in the source statement.

The current source check remains Bessy--Muis--Sereni--Steiner--Wiederrecht, *A relaxation of the Bermond--Thomassen conjecture*, arXiv:2608.12948 (13 August 2026): the genuine conjecture is explicitly stated there to remain unresolved for every `k>=4`; their threshold-seven result for `k=4` permits a one-arc reversal and is not target closure.

## Exact inherited state actually consumed

Latest complete lead state consumed: account02/B04 run `20260922T051543Z-b04-bt4-r11`, whose lexicographic normal form chooses an oriented exact-outdegree-seven, arc-dominated, 3-vertex-strong counterexample and a three-cycle packing `(H,S,U)` minimizing total packed order and then maximizing the number of arcs in the acyclic remainder. In its four-remainder heavy-triangle cage,

`H=h0->h1->h2->h0`, `R={x,r0,r1,r2}`,

with saturation triangles `hi->ri->x->hi`, and the old remainder is exactly

`r0->r1->r2`, `r0->x`, `r1->x`, `r2->x`.

The fresh account01/B06 handoff `BT4-HT-ALIGNED-CROSS-COLLAPSE-v1` plus its same-run common-port strengthening is also used. It closes the aligned long-support branch and forces the remaining aligned support to be the directed triangle

`A=p->u->v->p`,

with

`x->u,v`, `p->h0,r0,x`, `h1->p,u,v`,

and, in the same-heavy-`A` subbranch treated here,

`h2->p,u,v`, `A not->h1,h2`.

It proves that

`N_R^+(u)=N_R^+(v)={r_k}`

for one `k in {0,1,2}`. The case `k=0` already forces a cross. In the two no-cross equality alternatives:

- `k=1`: a shortest pure-remainder return is `b->r0->r1`, `m_B(r1)=3`, and `r1->p`;
- `k=2`: it is `b->r0->r1->r2`, `m_B(r2)=4`, and `r2->p`.

Named OTHER-account result actually consumed and applied: assigned partner account02/B06 `BT4-HT-ARCMAX-CAGE-COLLAPSE-v2`, shared commit `96fade26b836cc344b686fe1dee722a2d071703e`, controlling scientific blob `96fa9bdb0033fc6e6c3c42092e8259f882f8cd26`. Its exact cage conclusion gives

`d^+_{H union R}(h0)=d^+_{H union R}(h1)=d^+_{H union R}(h2)=d^+_{H union R}(r2)=2`,

and excludes every extra cage arc, in particular `r0->r2`, `h0->r1`, and the other nonlisted directions. I use this exactness below to localize dominators in the equality collars.

## Compact conditional route

The campaign reductions leave a finite set of explicit interfaces: SIX/HX closure, triangular F2/F3 witness-cover closure, the heavy-triangle packed-port closure, and the seven-remainder triangle pinwheel. On the heavy-triangle branch, the newest account01/B06 result reduces the aligned same-heavy-`A` state to a common-port triangle plus either a genuine `B`-to-`H/A` cross or one of two exact pure-`R` equality collars above. The first unpaid local implication is therefore to turn that common-port state into source-valid opposite packed transitions or an actual packing improvement. This report does exactly that for the reverse direction and removes the equality collars as terminal states.

## Lemma 1 — the two non-p vertices are exact five-witnesses heavy on B

For `z in {u,v}`, the only outneighbors of `z` in `A union R` are its directed successor on `A` and the common port `r_k`.

Indeed `A` is chordless, `N_R^+(z)={r_k}`, and orientation excludes `z->x` because `x->z`. Therefore

`d^+_{A union R}(z)=2`.

Exact outdegree seven gives exactly five outneighbors of `z` in `H union B`. Since `A not->h1,h2`, the only possible target of `z` on `H` is `h0`. Hence

`|N^+(z) intersect B| >= 4`.                                    (1)

Thus both `u` and `v` are exact five-witnesses for the fixed pair `H union B`, and both are heavy on `B` with fan at least four.

## Lemma 2 — support-correct no-inport: B cannot send to u or v

We prove `B not->u`; the proof for `v` is symmetric.

Assume `c->u` for some `c in B`. Let `n=|B|`. For every `a in N^+(u) intersect B`, orientation gives `a!=c`. Put

`t=dist_B(c,a)`

for the forward distance on the directed cycle `B`. Then

`K_a = c -> u -> a -> B[a,c]`

is a genuine directed cycle of order

`|K_a| = 2+n-t`.

The common-port triangle

`W_v = v -> r_k -> x -> v`

is genuine, and it is disjoint from both `H` and `K_a`. Hence

`H, W_v, K_a`

is a legal three-cycle packing in the original digraph. Its total order is

`3+3+(2+n-t)=n+8-t`,

whereas the original packing `H,A,B` has order `3+3+n=n+6`. Global minimum therefore forces `t<=2` for every `a in N^+(u) intersect B`.

But (1) gives at least four distinct `B`-targets of `u`, while only the first two successors of `c` have positive forward distance at most two. Contradiction. Thus `B not->u`.

For `v`, use instead the disjoint repair triangle

`W_u = u -> r_k -> x -> u`

and the identical cycle `c->v->a->B[a,c]`. Therefore

`B not->u,v`.                                                     (2)

This is a support-correct exchange: it does not remove `u` or `v` from `A` without repairing the damaged packed support. The repair consumes exactly the other `A`-vertex, the common port, and `x`; all three old cycles and all replacement vertices have been accounted for.

## Lemma 3 — two target-distinct x-free reverse crosses

Let

`X=N^+(x) intersect B`.

In the inherited global-NO-SIX cage `|X|=2`. By (1), each of

`Y_u=(N^+(u) intersect B)\X`, `Y_v=(N^+(v) intersect B)\X`

has size at least two. Hence the two-set Hall condition is automatic: choose distinct

`a_u in Y_u`, `a_v in Y_v`.                                    (3)

Fix `z in {u,v}` and its chosen `a_z`. Dominate the arc `z->a_z`. Thus there is `q0` with

`q0->z,a_z`.

Because `a_z notin X`, `q0!=x`. By (2), `q0 notin B`. If `q0` is packed, it lies on `H` or `A`, and `q0->a_z` is already a direct packed-to-`B` cross.

If `q0 in R`, dominate the arc `q0->z`, obtaining `q1->q0,z`. Again `q1 notin B` by (2). Also `q1!=x`: every non-sink old remainder vertex points to `x`, so orientation forbids `x->q0`. Continue whenever the new dominator is in `R`. Since `D[R]` is acyclic, this process cannot remain in `R` indefinitely. It terminates at a packed vertex `q_s`, necessarily on `H` or `A`, and yields a directed path

`q_s -> q_{s-1} -> ... -> q0 -> a_z`

whose internal vertices all lie in `R`, which avoids `x`, and which ends at the chosen `B`-port `a_z`.

Applying this to `z=u,v` and using (3) gives two genuine packed-to-`B` cross transitions with distinct `B` endpoints and x-free remainder interiors. Their interiors are not asserted disjoint; coalescence remains a real issue.

## Lemma 4 — the two pure-R equality collars force an additional packed cross

The corrected path-fan proof says the following equality completion. If a path

`b -> ... -> z`

from `B` to a remainder-supported heavy vertex `z` has length `L=m-1`, where `m=|N^+(z) intersect B|`, and `|B|>m`, then

`N^+(z) intersect B = {b^+,b^{++},...,b^{+m}}`.                 (4)

Indeed every fan target other than possibly `b` lies among the first `L+1=m` successors; when `|B|>m`, the arc `z->b` would close a cycle shorter than `B`, so it is impossible, and the `m` targets fill those `m` successor positions exactly.

### k=1

Here

`b->r0->r1`, `m=3`, `r1->p`.

Assume first `|B|>3`. By (4), with `a=b^{+3}`,

`r1->a`.

Dominate this arc: choose `y->r1,a`. The heavy-target exchange already gives `B not->r1`, so `y notin B`. By the exact cage, the only old-remainder in-neighbor of `r1` is `r0`. If `y=r0`, then

`C = b -> r0 -> a -> B[a,b]`

is a genuine cycle of order

`2+(|B|-3)=|B|-1`.

It is disjoint from the untouched packed cycles `H` and `A`, so replacing `B` by `C` strictly decreases the globally minimum packing, contradiction. Therefore `y notin R`.

Using the exact cage and orientation (`r1->p`), the packed possibilities reduce to

`y in {h1,u,v}`.                                                 (5)

Hence the equality collar forces a direct cross `y->a` from `H union A` to `B`.

### k=2

Here

`b->r0->r1->r2`, `m=4`, `r2->p`.

If `|B|>4`, (4) gives `a=b^{+4}` and `r2->a`. Dominate this arc by `y->r2,a`. Again `y notin B`. In the exact cage the only old-remainder in-neighbor of `r2` is `r1` (`r0->r2` is excluded). If `y=r1`, then

`C = b -> r0 -> r1 -> a -> B[a,b]`

has order

`3+(|B|-4)=|B|-1`,

is disjoint from `H,A`, and strictly improves the minimum packing. Hence `y notin R`. Exactness and `r2->p` now give

`y in {h2,u,v}`.                                                 (6)

Again the equality collar forces a direct packed-to-`B` cross.

### No short-support exception

The only omitted equality-completion boundaries would be `|B|=3` in the `k=1` case or `|B|=4` in the `k=2` case. They cannot occur in the inherited oriented exact-outdegree-seven normal form. Since the three packed cycles and the four-vertex remainder partition all vertices,

`|V(D)|=|H|+|A|+|B|+|R|=3+3+|B|+4=10+|B|`,

so these two boundaries have `|V(D)|=13` or `14`. But an oriented graph on `N` vertices has at most `N(N-1)/2` arcs, whereas exact outdegree seven gives exactly `7N` arcs. Thus `7N<=N(N-1)/2`, hence `N>=15`, contradiction.

Therefore **both pure-R equality collars force a genuine packed-to-`B` cross; there is no surviving short-support boundary**.

## Theorem — BT4-HT-COMMONPORT-REVERSE-CROSS-v1

In the aligned triangular same-heavy-`A` four-remainder cage, after the account01/B06 common-port reduction and the account02/B06 exact-cage refinement:

1. `u` and `v` are exact five-witnesses into `H union B`, each with at least four `B`-targets;
2. `B` has no arc into either `u` or `v`, by an explicit support-repair packing exchange;
3. there are two x-free packed-to-`B` cross transitions ending at distinct `B` ports;
4. each of the two previously surviving pure-`R` equality collars (`k=1,m=3` and `k=2,m=4`) itself forces an additional direct packed-to-`B` cross by arc domination plus a strict `|B|-1` replacement exchange;
5. the apparent `|B|=m` boundary is impossible because the oriented exact-seven normal form has at least fifteen vertices.

Thus the common-port equality states are not terminal neutral collars. They feed the same packed-port/cross splice frontier as the other heavy-triangle outputs.

If the collar dominator in (5) or (6) is `u` or `v`, then appending the equality path by `r_k->p` gives a `B`-to-`A` cross while `u/v->a` gives the reverse `A`-to-`B` cross with distinct packed endpoints and disjoint remainder interiors (the reverse cross is direct). If the dominator is `h1` or `h2`, the result is instead an `H`-to-`B` cross together with the `B`-to-`A` equality path; that three-support case remains to be spliced.

## Remaining obligation

Full BT4 is not proved. On this branch the first remaining implication is now narrower:

**HT-CROSS-COALESCE-CLOSE.** Starting from the target-distinct x-free reverse crosses of Lemma 3 and the forward `B`-to-`H/A` return supplied either directly or by the equality path `B->R->r_k->p`, prove one of: two vertex-disjoint replacement cycles, a strict lexicographic packing decrease, a directed cycle in the exchanged remainder, a SIX witness, or a fourth disjoint directed cycle. The remaining difficulty is packed-source / R-ladder coalescence, not target-port scarcity or a pure equality collar.

Separate campaign branches (global SIX/HX, triangular F2/F3 witness-cover, nonaligned port closure, and seven-remainder triangle-pinwheel) remain open.

## Failure checks and nonclaims

- Every packing comparison above uses genuine vertex-disjoint directed cycles in the original digraph.
- The no-inport argument repairs the support triangle after using `u` or `v`; it does not silently delete a packed vertex.
- The equality-collar strict cycles are disjoint from the untouched `H,A` packing.
- The two reverse cross paths are not claimed internally disjoint; only their endpoints on `B` are proved distinct and their interiors avoid `x`.
- A cross transition is not itself a fourth cycle.
- No near-directed one-reversal cycle is counted.
- No full BT4 proof or novelty claim is made.

Honest outcome: `ESSENTIAL_STEP_APPLIED`.
