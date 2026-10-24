# BT4 account03/B04 — Menger collar amplification and cycle-entry caps

Run: `20260922T011921Z-account03-B04-BT4-r12`
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`
Candidate: `BT4-MENGER-COLLAR-v1`
Outcome: `ESSENTIAL_STEP_APPLIED`
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Scope

The active owner control supersedes this slot's historical brain-retrieval/FEI prompt. The current target is the exact k=4 Bermond–Thomassen statement: every finite loopless digraph with at most one arc per ordered pair and minimum outdegree at least seven contains four vertex-disjoint directed cycles. Digons are allowed by the target, but the inherited minimum-counterexample reduction used below is oriented.

This run uses the current cross-account BT4 candidate rather than restarting. Exact other-account inputs consumed:

- assigned partner account04/B05 `BT4-COUNT-v1`, shared blob `9ce99798e661e4d14b2b27a0f647b909eff715b4`;
- BT4 lead account02/B04 exact-seven / 3-vertex-strong / path-fan state, shared blob `19ca9eec91aba2f3a1373ec2e8815bfc7bae65cc`, scientific report blob `d82fc84180bc66fd660c6c79f9a7f26332bdae72`, correction blob `ef92cfc95fab44c1e256757de5fae4ec4b28e36b`;
- account01/B06 support-transfer state, shared blob `796cfa70d678e0483b2e8100d9748cda4eca9afc`;
- account02/B05 dominator-escape state, shared blob `7c02367dae5f5cf3a4ca1f7d4c47e15fdc705630`.

No full BT4 proof is claimed.

## Inherited normal form

Assume a BT4 counterexample has been reduced as in the lead state to an oriented spanning subdigraph `D` with exact outdegree seven, minimum order, and a globally minimum-total three-cycle packing

`P=(C1,C2,C3)`

whose remainder `R` is acyclic. The lead proves `D` is 3-vertex-strong. For a remainder vertex `x` and packed cycle `C`, write

`m_C(x)=|N+(x)∩C|`.

The corrected path-fan statement used here is:

> If `b=p0 -> p1 -> ... -> p_L=x` is a directed path whose start `b` lies on `C` and whose other vertices lie in `R`, then `m_C(x) <= L+1`. If equality holds, the outneighbors of `x` on `C` are exactly the `L+1` consecutive successors of `b` allowed by the exchange proof.

Equivalently, when `m=m_C(x)>=3`, every such return path has `L>=m-1`.

## Lemma 1 — exact cycle-entry multiplicity cap

Let `v∈R`, let `C` be one packed cycle, let

`S=N+(v)∩C`, `m=|S|`, and `E=N-(v)∩C`.

Then

- `m>=3  => |E|=0`;
- `m=2   => |E|<=1`;
- `m=1   => |E|<=2`.

### Proof

Fix `b∈E`. For every `a∈S`, the arc pair `b->v->a` followed by the directed `C`-segment from `a` back to `b` forms a directed cycle disjoint from the other two packed cycles. Replacing `C` by that cycle cannot decrease total packing size. If `n=|C|` and `d_C(a,b)` is the forward length from `a` to `b`, then

`2+d_C(a,b) >= n`.

Since the counterexample is oriented, `a!=b`, and `d_C(a,b)+d_C(b,a)=n`; hence

`d_C(b,a) <= 2`.

Thus for every entry `b->v`,

`S ⊆ {b+,b++}`.

If `m>=3`, no such `b` exists. If `m=2`, the two-element successor window is forced, and two distinct starts cannot have the same two-successor window on a directed cycle, so there is at most one entry. If `m=1` with unique exit `a`, an entry can only be `a-` or `a--`, so there are at most two. QED.

### No-six sink consequence

In the partner's global no-six branch, later confirmed by account01/B06, every remainder sink `x` has fan pattern `(3,2,2)` up to permutation. Let `A` be the heavy cycle and `B,C` the two light cycles. Lemma 1 gives

`|N-(x)∩A|=0`, `|N-(x)∩B|<=1`, `|N-(x)∩C|<=1`.

Because `D` is 3-vertex-strong, every vertex has indegree at least three: otherwise deleting its at-most-two inneighbors leaves it unreachable in a graph with at least eight vertices. Therefore every no-six sink has at least one inneighbor in `R`. More sharply, if only one light cycle returns directly then it has at least two `R`-inneighbors, and if neither light cycle returns directly then it has at least three.

So the no-six branch has no terminal sink supported only by packed-cycle returns. This is a new explicit seven-budget restriction.

## Lemma 2 — three disjoint heavy-cycle return channels

Let `x` be any remainder vertex and `C` any packed cycle. Because `D` is 3-vertex-strong and `|C|>=3`, there exist three directed `C`-to-`x` paths `P1,P2,P3` that are pairwise vertex-disjoint except for the common endpoint `x` and have distinct starts on `C`.

### Proof

If not, the directed vertex form of Menger's theorem gives a set `S` of at most two vertices, not containing `x`, meeting every directed path from `C` to `x`. Since `|C|>=3`, choose `c∈C\S`. But `D-S` is strongly connected, so it contains a directed path from `c` to `x`, contradiction. QED.

Trim each `Pi` to begin at its last vertex of `C`. The paths remain disjoint except at `x`, have distinct starts, and have no internal vertex on `C`.

Hence there is an exact dichotomy:

1. some `Pi` internally meets one of the other two packed cycles, yielding a directed cross-cycle transition whose segment from `C` to its first other packed-cycle hit has interior entirely in `R`; or
2. all three `Pi` have all internal vertices in `R`, so the corrected path-fan inequality applies simultaneously to all three.

This is the promised packing/linkage amplifier: 3-vertex-strongness turns a single unpaid return into either an immediate packed-cycle transition object or three disjoint genuine remainder collars.

## Lemma 3 — nonsaturated pure-R collars force a large remainder

Assume case 2 above. Put `m=m_C(x)>=3`, and let `L_i` be the edge length of `Pi` after trimming.

Then `L_i>=m-1` for every `i`. Moreover, if `m<|C|`, at most one of the three paths can satisfy `L_i=m-1`.

### Proof of the second assertion

Equality in the path-fan lemma forces

`N+(x)∩C = {b_i+, b_i++, ..., b_i^(+m)}`

for the start `b_i` of every tight path. When `m<|C|`, a proper cyclic interval of `m` consecutive vertices determines its predecessor uniquely. Thus two tight paths would have the same start, contradicting the disjoint-path construction. QED.

Therefore in the nonsaturated case `m<|C|`, after ordering the lengths,

`L_1>=m-1`, `L_2>=m`, `L_3>=m`.

The three paths share only `x`. A path of length `L_i` contributes `L_i-1` vertices of `R` before `x`. Hence

`|R| >= 1 + sum_i (L_i-1) >= 3m-3`.

The only way multiple tight collars can coexist without this gain is the saturated case `m=|C|`, where `x` sends to every vertex of the heavy cycle.

### Applied no-six form

For a no-six sink the heavy fan is `m=3`. Thus for its heavy cycle `A`:

- if `|A|=3`, this is the saturated triangle branch;
- if `|A|>=4` and all three Menger paths avoid the other packed cycles, then `|R|>=6`;
- consequently, if `|R|<=5` and `|A|>=4`, one of the three disjoint heavy-cycle return paths must hit another packed cycle before reaching `x`, producing a source-valid cross-cycle transition with `R`-internal interior.

This also applies at the endpoint of the account03/B04 five-fan collar from the previously separated third-cycle-saturation branch whenever that endpoint is in the no-six `(3,2,2)` sink configuration.

## Interaction with the newest exchange state

Account02/B05 isolates a nonsaturated no-six `m=3` terminal geometry with an external fork and says any repair must become packed-cycle-assisted/two-cycle. Lemma 2 provides exactly three disjoint heavy-cycle return channels at that same sink. Lemma 3 shows that, outside the saturated triangle case, either one channel already enters another packed cycle or the pure-R alternative occupies at least six remainder vertices and at most one channel is the tight two-edge return. Thus two channels are strictly longer than the path-fan boundary.

This does not yet complete the splice, but it removes the possibility that the hard terminal fork is supported by a single short heavy return. The exchange workers can now attack a finite structural split:

- saturated heavy triangle;
- cross-cycle transition channel;
- or three disjoint pure-R collars with at least two strict collars and `|R|>=6`.

## Earliest remaining implication

The next decisive step is to combine one cross-cycle transition channel, or two of the strict pure-R collars, with the partner's six-fan/three-five-fan witness structure and the account02/B05 external-fork certificate to construct a genuine vertex-disjoint two-cycle splice. In the saturated triangle case, the exact seven-outdegree budget should be attacked directly because the sink sees all three triangle vertices.

Primary recipient: assigned partner `account04/B05`. Secondary recipients: BT4 lead `account02/B04`, exchange worker `account02/B05`, and linkage workers B05/B06.

No full proof, novelty claim, finite-search closure, near-directed substitution, brain PASS, or truth promotion is made.
