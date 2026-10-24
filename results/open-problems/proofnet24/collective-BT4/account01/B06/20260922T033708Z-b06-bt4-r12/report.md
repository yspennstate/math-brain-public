# BT4 account01/B06 — four-remainder post-pivot two-arm saturation

Run: `20260922T033708Z-b06-bt4-r12`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Candidate: `BT4-R4-POSTPIVOT-TWOARM-SATURATION-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Target status: `OPEN_NOT_PROVED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Exact target and current source boundary

The target is the genuine `k=4` Bermond--Thomassen statement: every finite loopless digraph with at most one arc per ordered pair and minimum outdegree at least seven has four pairwise vertex-disjoint genuinely directed cycles. Digons are allowed in the source problem. The inherited minimum-counterexample reduction may be taken oriented: if a counterexample contained a digon, deleting its two vertices leaves minimum outdegree at least five, and the genuine `k=3` theorem gives three disjoint directed cycles in the remainder.

A fresh 22 September 2026 source check still finds Bessy--Muis--Sereni--Steiner--Wiederrecht, *A relaxation of the Bermond-Thomassen conjecture*, arXiv:2608.12948 (13 August 2026), explicitly stating that the genuine conjecture remains unresolved for all `k>=4`. Their theorem permits each packed cycle to be directed or made directed by reversing one arc and is not substituted for the target below.

## Latest complete lead state consumed

The current campaign lead is account02/B04. I source-read its complete run `20260922T031823Z-a02-b04-bt4-r11`:

- primary report commit `14ef93ae71f52c019c679c29fca4624e510f7b95`, blob `17d49d472779d5304d30b93c07ce89c289ab20d1`;
- controlling frontier addendum commit `6424f407ecb508fb5dcb4612a1d976441f34910c`, blob `28fe813aa044e57bbb3c6934a9ea76525bc04968`.

The frontier addendum is controlling. In particular the old globally-no-cross residual is auxiliary only: account01/B04's canonical sink-cross theorem shows that every acyclic-remainder sink already yields a genuine packed-to-packed cross. The actual unpaid implication is `SC+`: after the exact neutral source pivot, use the resulting x-free cross family / four-remainder configurations to obtain a legal replacement, strict packing reduction, exchanged-remainder cycle, or fourth disjoint cycle.

## Named OTHER-account result applied

I apply account02/B05 `BT4-RSC-v6-postpivot-wall`, run `20260922T032614Z-b05-bt4-777e9239`, canonical report creation commit `a51ee60d3162960774aa0e45e3c2bdda59e7a017` and shared handoff blob `7c14eaf41ddd4761ee256eb82e7e2994fac4806a`.

The exact imported facts are these. Work in the inherited oriented exact-outdegree-seven counterexample with globally minimum three-cycle packing `(S,T,U)` and acyclic remainder `R`. For a remainder sink `x`, choose the canonical direct source inport `p->x`, `p in S`. In the neutral source-fan-two branch,

`N+(x) intersect S = {p^+,p^{++}}`.

Putting `q=p^+`, the legal equality pivot is

`S' = p -> x -> p^{++} -> S[p^{++},p]`,

with new acyclic remainder

`R'=(R-{x}) union {q}`.

The freed vertex `q` has exactly one outneighbor on `S'`, namely `p^{++}`. If

`e=d^+_{R'}(q)`,

then `e=0` is a SIX witness and `e=1` is a five-witness. For `e>=2`, directed Menger in `D-x` gives two paths from distinct exits `r_1,r_2 in N^+_{R'}(q)` back toward `q`; truncating each at its first packed hit produces two escape arms. If an arm first hits `T union U`, it is a genuine cross. Otherwise the two first packed hits `a_1,a_2` lie on `S'`, are distinct, and the corresponding full paths

`P_i = p -> q -> r_i -> ... -> a_i`

have internal vertices in `R'`; their internal sets intersect exactly in the common vertex `q`. At most one return can be `a_i=p`. For a return with `a_i != p`, global minimum gives

`ell_i >= d_i := d_{S'}(p,a_i)`,

with equality a neutral exchange. The difficult wall is the branch in which neither arm reaches `T union U` and the relevant same-support returns are strict.

No peer outcome label is used as proof; only the source-bound statements above are imported.

## New lemma 1 — a return to the source port forces a five-vertex source cycle

Assume now the lead's four-remainder branch `|R|=4`, so after the neutral pivot also `|R'|=4`. Suppose one B05 Menger arm returns to `p` itself. Then there is a genuine directed cycle

`W = p -> q -> r_i -> ... -> p`

whose only packed vertex is `p` and whose remaining vertices lie in `R'`. Hence

`|W| <= 1+|R'| = 5`.

Since `W` is disjoint from the untouched packed cycles `T,U`, global minimum of `(S',T,U)` implies

`|S'| <= |W| <= 5`.

Thus in the four-remainder post-pivot wall, a return to the source port is not an unstructured obstruction: it immediately reduces `SC+` to a source cycle of order at most five.

### Proof

The full arm begins with the ambient arc `p->q`, follows a nonempty remainder path, and first returns to the packing at `p`. By the truncation definition no internal vertex is packed, so every other vertex of the closed walk lies in `R'`. The Menger path is simple before its terminal first hit, hence this is a simple directed cycle. Replacing `S'` by `W` while keeping `T,U` is a legitimate three-cycle packing; global minimality gives the size inequality. QED.

## New lemma 2 — strict two-arm saturation when neither arm returns to p

Continue with `|R'|=4`. Assume:

1. `e>=2`;
2. neither selected arm reaches `T union U`;
3. neither return vertex is `p`;
4. both same-support returns are strict, so `ell_i>d_i`.

Then, after relabeling the two arms,

`d_1=2,  d_2=3`,

`ell_1=3, ell_2=4`,

and the two internal vertex sets satisfy

`int(P_1) intersect int(P_2) = {q}`,

`int(P_1) union int(P_2) = R'`.

Equivalently, writing

`s=p^{++}`

for the second successor of `p` on `S'` (the first successor is `x`) and `t=s^+` on `S'`, the geometry is exactly

`P_1: p -> q -> u -> s`,

`P_2: p -> q -> v -> w -> t`,

for a partition

`R'={q,u,v,w}`.

In particular the two strict arms have excess exactly one over the skipped source segments, their packed return vertices are forced to be the first two allowable vertices after the pivoted sink, and their interiors exhaust the entire four-vertex remainder.

### Proof

Because the two B05 Menger prefixes are internally vertex-disjoint and begin at distinct exits of `q`, the full paths `P_1,P_2` share exactly the prefix endpoint data `p,q` and have no common internal vertex other than `q`. A path of edge length `ell_i` with packed endpoints has `ell_i-1` internal vertices, all in `R'`. Therefore

`4 >= |int(P_1) union int(P_2)|`
`  = (ell_1-1)+(ell_2-1)-1`
`  = ell_1+ell_2-3`.                                      (1)

Since the Menger construction is in `D-x`, neither first packed hit is `x`. We have excluded `p`. On the directed cycle `S'`, the first successor of `p` is exactly `x`; hence each allowed return satisfies

`d_i=d_{S'}(p,a_i)>=2`.

The two first packed hits are distinct, so `d_1,d_2` are distinct positive forward distances. Consequently

`d_1+d_2 >= 2+3 = 5`.                                      (2)

Strictness and integrality give

`ell_i >= d_i+1`.                                           (3)

Combining (1)--(3),

`4 >= ell_1+ell_2-3`
`  >= d_1+d_2-1`
`  >= 4`.

Every inequality is equality. Hence `d_1+d_2=5`; since the distinct distances are each at least two, `{d_1,d_2}={2,3}`. Equality in (3) termwise gives `{ell_1,ell_2}={3,4}` matched to the corresponding distances. Equality in (1) means the union of the two internal sets has all four vertices of `R'`. The B05 disjointness already gives their intersection exactly `{q}`. The displayed path forms follow immediately. QED.

## Corollary — exact R4 post-pivot wall

Under the lead's actual `SC+` four-remainder source-fan-two pivot, apply the B05 freed-vertex wall. Then one of the following occurs:

1. a SIX object (`e=0`);
2. an R-supported five-witness plus its wall path (`e=1`);
3. a genuine cross from one of the two Menger arms to `T` or `U`;
4. a neutral same-support return (`ell_i=d_i`);
5. a source-return cycle forcing `|S'|<=5`;
6. the exact strict saturation pattern of Lemma 2.

Thus the previous residual description

`e>=2 + no cross + two strict same-support arms`

has no free metric parameters at `|R|=4`: unless the source cycle is already at most five, the two chosen strict arms necessarily have distances `(2,3)`, lengths `(3,4)`, unit excess, and exhaust `R'`.

This is a directed vertex-disjoint rerouting statement; no edge-disjoint surrogate is used.

## Compact conditional end-to-end argument after this step

Assume a BT4 counterexample and take the inherited oriented exact-seven globally minimum packing. A remainder sink exists. The canonical sink-cross theorem gives a direct source inport. Source fan at most one enters the separate SIX interface. Source fan two gives the exact neutral pivot. After the pivot, account02/B05 classifies the freed vertex by `e=d^+_{R'}(q)`.

At `|R|=4`, the new lemmas above remove all metric freedom from the only B05 branch not already named as SIX/five/cross/neutral: either a return-to-port produces a source cycle of order at most five, or the two strict arms are the explicit `(2,3)/(3,4)` saturation and use every remainder vertex. Therefore a complete proof on this branch now reduces to a finite-looking structural statement rather than an arbitrary linkage problem:

> `R4-STRICT-SAT+`: in the exact configuration
>
> `S': p -> x -> s -> t -> ... -> p`,
>
> `R'={q,u,v,w}`,
>
> `p->q->u->s` and `p->q->v->w->t`,
>
> with `D[R']` acyclic and the inherited exact-seven / 3-vertex-strong / chordless / arc-dominated conditions, combine the lead's x-free heavy-target cross family and regenerated pair-deletion deficits to force a legal two-cycle replacement, a strict global-minimum reduction, a directed cycle in an exchanged remainder, a SIX object, or a fourth disjoint directed cycle.

Together with the lead's separate exact-six closure and the remaining `SC+` configurations, proving this final explicit saturation closure would complete the four-remainder post-pivot wall. This report does not prove those remaining closures and therefore does not prove BT4.

## Failure checks

- I do not use the account04/B04 no-cross polarity-orbit addendum as current frontier evidence: the lead's later controlling addendum says global no-cross is already empty. That result remains auxiliary only for conditional geometry.
- The opposite-cross-pair configuration is not promoted to two replacement cycles; one opposite pair yields only one alternating cycle without another compatible interface.
- The two full strict arms share `p,q`; they are not claimed vertex-disjoint. Only their post-`q` Menger prefixes are disjoint, which is exactly what the counting proof uses.
- The target allows digons; orientation is used only in the inherited minimum-counterexample normal form after the digon case is discharged.
- No near-directed cycle from the 2026 relaxation is counted.
- No full BT4 proof or novelty claim is made.

Outcome: `ESSENTIAL_STEP_APPLIED`.  
Target: `OPEN_NOT_PROVED`.  
Brain: `WITHOUT_VERIFIED_BRAIN`.
