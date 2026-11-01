# BT4 fleet03/B05 — pairwise-overlap switching and dual-wall collapse

Run: `20260922T024158Z-b05-bt4-r11`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Candidate: `BT4-TCEX-v4-switchwall`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Exact target and assignment

Target: prove that every finite loopless digraph with at most one arc per ordered pair of distinct vertices and minimum outdegree at least seven contains four pairwise vertex-disjoint genuinely directed cycles. Opposite arcs are allowed in the source problem, so directed digons count.

This slot's exact assignment is to prove the disjointness-preserving exchange promised by the current two-partition/linkage candidate; average degree is not substituted for minimum outdegree. The named cross-account partner is `fleet04/B06`.

The campaign source boundary remains the one recorded in the current owner target file: Bessy--Muis--Sereni--Steiner--Wiederrecht, *A relaxation of the Bermond--Thomassen conjecture*, arXiv:2608.12948 (13 August 2026), leaves the genuine conjecture unresolved for every `k>=4` and proves only the same-threshold relaxation allowing one reversed arc per packed cycle. No near-directed cycle is counted below.

## Exact inherited state consumed

The common normal form is the current campaign lead's oriented exact-outdegree-seven minimum counterexample: a globally minimum-total packing `(A,B,C)` of three directed cycles, nonempty acyclic remainder

`R = V(D) \ (V(A) union V(B) union V(C))`,

chordless packed cycles, domination of every arc, and 3-vertex-strongness. Equality in the existing path/exchange bounds produces another globally minimum packing, whose exchanged remainder is acyclic because otherwise the exchanged three cycles plus a remainder cycle form a forbidden four-pack.

I read and use the current lead correction at

`proofnet24/collective-BT4/fleet02/B04/20260922T022208Z-b04-bt4-r11/correction.md`,

which in particular keeps cross-packed transitions as an explicit unpaid splice interface and requires hypothesis-correct use of the marked-segment inequality.

The named OTHER-account partner result applied directly is

`proofnet24/collective-BT4/fleet04/B06/20260922T021002Z-b06-bt4-r12/report.md`,

candidate `BT4-SIX-DUAL-COLLAR-v1`. In its difficult exact-six companion branch it supplies two incoming support-entry ladders

`L_i : s_i -> ... -> u_i -> z`,

and two predecessor-origin boundary rays

`P_j : p=z^- -> r_j -> ... -> t_j`,

with all nonpacked interior vertices in `R`. Its only residual local obstruction is the **dual reachability wall**: for every `i,j`, no vertex on the `R` part of `L_i` reaches any vertex on the `R` part of `P_j` inside `D[R]`.

I also retain this slot's immediately preceding exact linkage state

`proofnet24/collective-BT4/fleet03/B05/20260922T014230Z-fleet03-B05-BT4-r12/report.md`.

There, in the three-sink distinct-heavy all-long-light no-six core, fleet04/B06's linkage cycles `Q_A,Q_B,Q_C` were shown not to be mutually vertex-disjoint; triple overlap was converted by an odd-sign rule into an `R`-internal support bypass. The remaining unstructured compatibility branch was pairwise-only `R` overlap or packed-port collision.

No peer outcome label is used as a theorem.

## Part I — pairwise-only linkage overlap is already a cross-or-support-switch

The previous run needed a triple-overlap vertex for its odd-sign argument. The next lemma shows that two overlapping linkage cycles already suffice. This removes pairwise-only `R` overlap as an independent obstruction.

### Lemma 1 — two-linkage sign switch

Let `Q_1,Q_2` be two of the partner's linkage cycles in the three-sink all-long-light core. Suppose they share one packed support cycle `X` and have different other packed support cycles. Thus, after relabeling, `Q_1` joins `X` to `Y` and `Q_2` joins `X` to `Z`, where `X,Y,Z` are the three distinct packed cycles.

Assume an internal remainder vertex

`w in int_R(Q_1) intersect int_R(Q_2)`.

For each incidence of `Q_i` with one of its packed ports, give that port sign `+` if the directed subpath from the port to `w` has all internal vertices in `R`, and sign `-` if the directed subpath from `w` to the port has all internal vertices in `R`.

Then at least one of the following holds.

1. There is a genuine cross-packed directed path between two distinct packed cycles, all of whose internal vertices lie in `R`.
2. There is an `R`-internal directed path between two distinct ports of the same packed cycle `X`.
3. There is a directed closed walk based at a common `X` port whose other vertices lie in `R`.

#### Proof

On each directed linkage cycle, the two packed-port signs are opposite: traversing the directed cycle, one packed port reaches `w` before `w` reaches the other packed port.

Let the signs of the two `X` ports be `sigma_1,sigma_2`.

If `sigma_1` and `sigma_2` are opposite, concatenate the `X`-port-to-`w` directed piece from the `+` incidence with the `w`-to-`X`-port piece from the `-` incidence. This gives a directed walk whose endpoints are the two `X` ports and whose internal vertices lie in `R`. If the ports are distinct, delete repeated directed subwalks to obtain case 2. If the ports coincide, retain the resulting closed directed walk, giving case 3.

If `sigma_1=sigma_2`, then the non-`X` port of each linkage has sign `-sigma_1`. Choose the `X` port of one linkage and the non-`X` port of the other. Their signs are opposite, so the same concatenation through `w` gives a directed path between `X` and one of `Y,Z`, with all internal vertices in `R`. This is case 1.

The simplification cannot introduce a packed internal vertex because each constituent piece has `R`-only interior. QED.

### Lemma 2 — disjointness-preserving exchange produced by Lemma 1

In case 2, orient the resulting path as

`P : u -> ... -> v`,

where `u,v` are distinct vertices of packed cycle `X`, all internal vertices of `P` lie in `R`, `ell=|E(P)|`, and `d=d_X(u,v)` is the forward directed distance on `X` from `u` to `v`.

Then

`ell >= d`.

If `ell=d`, replacing `X` by

`X_P = P + X[v,u]`

is a size-neutral, vertex-disjoint, globally minimum one-cycle exchange. Its new remainder

`R_P = (R \ int(P)) union int(X[u,v])`

is acyclic.

If the two `X` ports coincide, case 3 contains a simple directed cycle `W` through that common port and otherwise in `R`. Hence

`|W| >= |X|` and `|W| <= |R|+1`.

In the all-long-light core, where `|X|>|R|`, equality is forced:

`|W|=|X|=|R|+1`,

and `W` uses every remainder vertex. Thus coincident-port pairwise overlap forces an exact whole-remainder neutral replacement.

#### Proof

The replacement cycle `X_P` is disjoint from the other two packed cycles because `P` has only its endpoints on `X` and otherwise lies in the old remainder. Its order is

`|X_P| = |X| + ell - d`.

If `ell<d`, keeping the other two packed cycles gives a smaller three-cycle packing, contradicting global minimum. Equality gives another global minimum. A cycle in its new remainder would be vertex-disjoint from the new three-cycle packing and hence produce four disjoint directed cycles, so the new remainder is acyclic.

For a coincident port, extract a simple directed cycle from the closed directed walk. It must use the packed port because `D[R]` is acyclic. It may replace `X`, so global minimality gives `|W|>=|X|`; it uses at most the one packed port plus all `|R|` remainder vertices. The all-long inequality finishes the equality statement. QED.

### Consequence 3 — pairwise-only `R` overlap is no longer an unstructured branch

In the three-sink linkage core, whenever two linkage interiors overlap in `R`, that overlap itself yields either

- a genuine cross-packed transition;
- an `R`-internal same-support bypass with the exact minimum-packing tax, equality giving a legal disjointness-preserving exchange; or
- a whole-remainder neutral replacement in the coincident-port case.

Therefore the previous residual label “pairwise-only overlap with empty triple intersection” can be retired as an independent compatibility obstruction. What remains after this reduction is not overlap itself but the already explicit **cross-to-two-cycle splice** problem or a **strict** same-support bypass (`ell>d`) that does not by itself improve the minimum packing.

This is stronger than the previous triple-overlap parity lemma: no third linkage and no triple-intersection vertex is required.

## Part II — the named partner's dual reachability wall also collapses to cross-or-support exchange

The named partner's newest exact-six report leaves a `2 x 2` wall in the acyclic remainder. The wall says an incoming ladder cannot reach an outgoing ray while staying in `R`. The inherited 3-vertex-strongness forces any attempted connection to leave `R`, which is exactly enough to expose a packed support path.

### Lemma 4 — wall-breaking support path

Use the partner's exact-six `(C4)` setup. Let

`L : s -> ... -> q -> ... -> u -> z`

be one of its incoming support-entry ladders, with `s` packed and every vertex between `s` and `z` in `R`. Let

`P : p=z^- -> r -> ... -> t`

be one of its predecessor-origin boundary rays, with every vertex between packed endpoints in `R`.

Assume the partner's dual wall: no vertex on the `R` part of `L` reaches any vertex on the `R` part of `P` by a path contained in `D[R]`.

Choose any `q` on the `R` part of `L` and take `r`, the first `R` vertex on `P`. Because `D` is 3-vertex-strong,

`D-{p,z}`

is strongly connected. Hence there is a directed `q`-to-`r` path `H` in `D-{p,z}`.

By the wall, `H` is not contained in `R`. Let `a` be the first packed vertex met by `H`. Then the prefix `H[q,a]` has every internal vertex in `R`, and

`a notin {p,z}`.

Concatenating the prefix of `L` from `s` to `q` with `H[q,a]` gives a directed walk from packed vertex `s` to packed vertex `a` with all nonendpoint vertices in `R`. In fact it has no repeated `R` vertex: if the `H` prefix first met an earlier remainder vertex of the ladder prefix, the ladder segment from that vertex to `q` followed by the `H` segment back to it would form a directed cycle in `D[R]`, impossible.

Therefore the concatenation is a clean `R`-internal support path, except possibly that the packed endpoints coincide.

QED.

### Corollary 5 — exact output of the dual wall

Let `X` be the packed cycle containing `s`.

- If `a` is on a different packed cycle, Lemma 4 gives a genuine cross-packed transition.
- If `a` is a distinct vertex of `X`, write the clean path as `T:s->...->a`, with length `ell`, and let `d=d_X(s,a)`. Then global minimum gives `ell>=d`; equality is a size-neutral disjointness-preserving one-cycle exchange with acyclic exchanged remainder.
- If `a=s`, the closed walk contains a simple directed cycle `W` through `s` and otherwise in `R`; hence `|W|>=|X|` and `|W|<=|R|+1`. In any surrounding branch with `|X|>|R|`, this again forces the exact whole-remainder neutral replacement `|W|=|X|=|R|+1`.

Thus the partner's `2 x 2` dual reachability wall is not a terminal coalescence obstruction. The wall itself forces an actionable cross transition or a support exchange/collar.

### Why the wall proof is hypothesis-correct

The argument does not infer disjointness from two paths and does not use an average-degree surrogate. It uses only:

1. the named partner's actual ladder/ray objects;
2. its exact reachability-wall negation inside `R`;
3. inherited 3-vertex-strongness to connect `q` to `r` after deleting the adjacent support vertices `p,z`;
4. acyclicity of `R` to prevent self-intersection of the concatenated support path;
5. global minimum of the three-cycle packing for the exchange inequality.

No marked-segment fan inequality is invoked unless its separate heavy-inport hypotheses are available. In particular this avoids the hypothesis error corrected in the newest lead report.

## Combined effect on the live proof frontier

Two formerly separate coalescence labels now reduce to the same small interface.

### Three-sink linkage compatibility

- mutually disjoint linkage cycles were already impossible by packing size;
- triple overlap was already converted to an exchange input by the previous run;
- **pairwise-only overlap is now converted by Lemmas 1-2 to cross or support exchange**.

Thus an `R` overlap among linkage cycles is no longer, by itself, the missing disjointness-preserving implication.

### Exact-six companion branch

- fleet01/B04 supplied incoming remainder companions/ladders;
- fleet04/B06 supplied two outgoing predecessor rays and isolated the dual wall;
- **the wall is now converted by Lemma 4 to cross or support exchange**.

Thus absence of forward `R` reachability from incoming to outgoing interfaces is no longer a terminal reason the exact-six branch can fail to expose an exchange object.

## First remaining essential implication

Full BT4 is not proved. After the reductions above, the first shared implication is more sharply stated:

> **Cross/strict-bypass splice closure.** In the inherited exact-seven globally-minimum normal form, whenever the overlap or dual-wall mechanisms above output either (i) a genuine cross-packed `R`-internal transition or (ii) a strict same-support `R`-internal bypass with `ell>d`, combine it with the already available return/linkage structure to construct two vertex-disjoint replacement directed cycles, a strict reduction of the three-cycle packing, a directed cycle in an exchanged remainder, or a transition to the six-fan closure.

Equality cases are no longer part of this unpaid implication: they already give explicit disjointness-preserving neutral exchanges with acyclic new remainder.

The separate G1-S simultaneous-long-collar branch and the broader high-witness SIX closure remain campaign obligations. One cross transition alone is not counted as two replacement cycles.

## Failure checks and nonclaims

- Digons are permitted in the target; orientation is used only in the inherited minimum-counterexample reduction.
- The two-linkage switch requires a genuine shared `R` vertex. A packed-port collision without an `R` overlap is not silently identified with it.
- A strict bypass (`ell>d`) is not itself a contradiction; it is a quantified collar.
- A cross transition is not itself a four-packing or even a two-cycle replacement.
- The dual-wall proof uses a path in `D-{p,z}` supplied by 3-vertex-strongness; it does not assert that the two incoming or two outgoing channels are mutually disjoint.
- No finite computation or average-degree argument is used.
- No full BT4 proof or novelty claim is made.

## Honest status and next recipients

Outcome: `ESSENTIAL_STEP_APPLIED`.

Named partner result actually applied: fleet04/B06 `BT4-SIX-DUAL-COLLAR-v1`, exact run path above. The partner's dual wall is reduced to the same cross/support-exchange interface as the pairwise linkage-overlap branch.

Next recipient: `fleet04/B06` should absorb Lemma 4 into its exact-six companion branch and remove the dual wall as a terminal case. Campaign lead `fleet02/B04` should update the cross-linkage/SIX conditional route so equality outputs are treated as completed neutral exchanges and the remaining local blocker is the cross/strict-bypass splice closure.
