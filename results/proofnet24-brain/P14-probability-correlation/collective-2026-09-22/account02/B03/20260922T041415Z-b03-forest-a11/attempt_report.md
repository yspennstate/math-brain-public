# FOREST B03 — theta-response lifting and arbitrary parallel-class adversary

Run: `20260922T041415Z-b03-forest-a11`  
Outcome: **ESSENTIAL_STEP_APPLIED**.  
Context: **WITHOUT_VERIFIED_BRAIN**.  
Parent target remains internal research; no public solved-problem or novelty claim is made.

## 1. Fresh scope and source state

Fresh mandatory controls were read from main `ce72b9684df98f15d78737598a2abcc0dd4f32fb`; a pre-publication refresh observed main `4ff58cf512913453685f8b04955e4789896a410b` with no newer lead/partner FOREST handoff and no applicable owner/platform stop. OWNER CONTROL remains `2026-09-22.2`, active programme `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`. B03 remains assigned to exact FOREST graph adversaries / corrected separator statements; old installation and benchmark duties stayed stopped.

Latest accessible lead version consumed: account01/B01 `FOREST-KN-COCKS-RECONCILED-v3`, shared handoff blob `e02a4281a67d992d06d7c2c70586efa656353cab`. It records an internal `FULL_PROOF_CANDIDATE`:
`U(K_n) -> Cocks FIXED(K_n) weighted independence correlation -> Semple--Welsh minor closure -> deletion subgraphs -> unit FOREST`.
The handoff's referenced canonical report object was not reachable on the fresh default branch, so this run treats the read-back v3 handoff itself as the exact accessible lead version and does not silently import unavailable details.

Essential newer dependency consumed: account03/B02 `fixed-graph-lifting-gate`, blob `811e7901a8cc51d7171f3240f3a5e7f2b738e8bd`. It confirms that the final Semple--Welsh paper states the needed fixed-graph Cocks implication, but the accessible proof body for Cocks remains unavailable; the global class-level parallel-copy equivalence is not a substitute because using it here would be circular. Thus the first source-verification gate on the lead chain remains a line-check of `FIXED(G)`, or an independent proof of the specialization `U(K_n) => W(K_n)`.

Named OTHER-account partner consumed and directly applied: account03/B01 `activity-det-no-go`, blob `582e0c8baca21284b3538d96763a0dafd31755d4`. Its exact activity identity is
`4 Delta = W10 W01 - W00 W11 + R (W10 + W11)`,
where `R` is its exchange-reservoir count (renamed here from `Q` to avoid collision with the separator polynomial). This run identifies exactly how that two-channel quantity transforms under a two-terminal separator response.

## 2. Exact two-terminal response lemma

Let `H` and `N` be finite simple graphs sharing exactly two vertices `u,v` and no edges. Let marked edges `e,f` lie in `H`. Write

- `D_N` = number of forests of `N` in which `u,v` are disconnected;
- `C_N` = number of forests of `N` in which `u,v` are connected;
- `r_N = C_N / D_N`.

`D_N>0` because the empty forest is counted.

For a forest `S` of `H` and a forest `T` of `N`, the union `S union T` is acyclic iff it is not the case that both `S` and `T` connect `u` to `v`: because the two graphs meet only at the terminals, a cycle crossing the separator is exactly the union of a `u-v` path from each side.

Introduce a virtual edge `g=uv` in `H` with weight `w`. A forest `S` of `H` admits `g` iff `S` disconnects `u,v`. Therefore, for each of the four marked counting functions `X in {Z,Z_e,Z_f,Z_ef}`,

`X_{H union N} = D_N X_{H+g}(r_N)`.

Consequently the Rayleigh/negative-correlation gap satisfies the exact factorization

**`Delta_{H union N}(e,f) = D_N^2 Delta_{H+g}(e,f; w=r_N)`.**

This is an equality of the actual unrooted all-sizes forest counts; no rooted measure, spanning-tree replacement, or probabilistic approximation is used.

## 3. A source-simple dense family of exact responses

Let `Theta_{k,m}` be `k` internally vertex-disjoint `u-v` paths, each of length `m>=2`, with all edges unit weight. It is a finite simple graph. Put `d_m=2^m-1`.

On one path, exactly one edge subset connects its terminals (the full path), while `d_m` subsets disconnect them. In the parallel union, a forest can contain at most one terminal-connecting full path. Hence exactly

`D_{k,m}=d_m^k`,
`C_{k,m}=k d_m^(k-1)`,
and therefore

**`r_{k,m}=k/(2^m-1)`.**

The set `{k/(2^m-1): k>=1, m>=2}` is dense in `(0,infinity)`: for fixed `x>0`, choose `m -> infinity` and the nearest positive integer `k` to `x(2^m-1)`, giving error at most `1/(2(2^m-1))` for all sufficiently large `m`.

Therefore, for any fixed simple core `H` with a nonedge `uv` and marks `e,f`, if
`q_H(w)=Delta_{H+g}(e,f;w)`, then the following are equivalent:

1. `q_H(w)>=0` for every real `w>0`;
2. `q_H(k/(2^m-1))>=0` for every `k>=1,m>=2`;
3. every bona fide unit-simple theta extension `H union Theta_{k,m}` has nonnegative `e,f` gap.

The only step from (2) to (1) is continuity of the quadratic `q_H`.

This is the corrected source-valid separator formulation: an arbitrary positive virtual boundary weight need not be postulated as an unrelated hypothesis. It is exactly the closure of responses produced by finite simple unit graphs. In particular, if a weighted virtual-edge core counterexample `q_H(w0)<0` is ever found, continuity plus a theta response in its negative interval immediately lifts it to a genuine finite simple unit source counterexample.

## 4. Relation to the earlier sharp separator envelope

Writing
`Z=A+wB`, `Z_e=a0+w a1`, `Z_f=b0+w b1`, `Z_ef=c0+w c1`,
let
`D0=a0 b0-A c0`, `D1=a1 b1-B c1`,
`P_e=B a0-A a1`, `P_f=B b0-A b1`.

The previously derived identity
`AB q_H(w)=(A+wB)(B D0 + A w D1)-w P_e P_f`
shows, when `D0,D1>=0`, that the all-response theta criterion is equivalent to the sharp envelope

**`P_e P_f <= (B sqrt(D0)+A sqrt(D1))^2`.**

So the square-root envelope is not merely a convenient weighted strengthening: failure of it would have a source-valid simple-graph witness obtained by theta lifting.

Combining the present factorization with account03/B01's activity identity yields, on every theta extension,

**`W10 W01 - W00 W11 + R(W10+W11)
   = 4 d_m^(2k) q_H(k/d_m)`.**

Thus the partner's two indispensable activity channels are exactly the activity-coordinate representation of the same separator response gap. A one-channel activity bound is not stable under this reduction; only their sum is the source invariant.

## 5. Exact induced-parallel-edge adversary

The same theta family is an adversary to any recursive contraction rule that assumes a simple source can create only single or double parallel classes.

Already `Theta_{k,2}=K_{2,k}` is simple. Contract the `k` edges from terminal `u` to the `k` internal degree-two vertices, one after another. The remaining `k` edges become a parallel class between `u` and `v`. Hence recursive contractions of a simple graph create a parallel class of **arbitrary size `k`**.

For that class the forest polynomial is
`1 + y_1 + ... + y_k`;
at unit member weights its aggregate class weight is `k`, and its count is `k+1`, not the value `2` obtained by resetting it to a single unit simple edge. The exact safe simplification is to retain the sum `Y=sum_i y_i`, with marked-member derivative semantics if a marked edge belongs to the class.

This is stronger than the local observation that a *single first contraction* of a simple graph produces multiplicity at most two: repeated contractions pass through multigraphs, and multiplicities accumulate without bound.

The source family also has substantial cycle overlap: `Theta_{k,m}` contains a cycle for every pair of branches, so for `k>=3` these cycles overlap heavily while the exact response remains the one scalar `k/(2^m-1)`.

## 6. Concrete overlapping-cycle witness

Take the 5-vertex core

`H = K_5 minus {12,34}`,

terminals `u=1,v=2`, marks `e=13,f=24`, and virtual edge `g=12`. Exact affine counts are

`Z=[134,64]`,
`Z_e=[52,18]`,
`Z_f=[52,18]`,
`Z_ef=[19,5]`.

Hence

**`q_H(w)=158-14w+4w^2`.**

Glue `Theta_{4,2}=K_{2,4}` between terminals 1 and 2 using fresh vertices. This source graph is simple; the theta side contains six overlapping 4-cycles. Here
`D_N=3^4=81` and `r_N=4/3`, so

`q_H(4/3)=1318/9`

and the exact source-graph gap is

**`Delta = 81^2 * 1318/9 = 960822`.**

The same source theta, under successive contractions of its four `u-x_i` edges, produces a four-member parallel class. Thus this single explicit construction simultaneously exercises the overlapping-cycle and induced-large-parallel mechanisms.

## 7. Exact computation

`theta_response_checker.py` exhaustively scanned every labelled simple core on 2--5 vertices having at least two edges and a chosen nonedge boundary, and every marked pair. Totals:

- 1,071 core graphs;
- 46,563 marked `(H,e,f,uv)` instances;
- 540 instances with negative mixed coefficient `M`;
- **0** failures of nonnegativity for all `w>0`.

Among cases with `M<0,D0D1>0`, the largest exact discriminant ratio
`M^2/(4D0D1)` was `49/632`, attained by the concrete core above with `q_H(w)=158-14w+4w^2`.

The checker also brute-enumerated small theta responses and the full 16-edge concrete glued graph, verifying the exact gap `960822`.

Executed checker SHA-256: `3076de734d1a067b530f179fcff31b1100f2da18b0128af9886b918bc0f60cab` (5,822 bytes).  
Executed output SHA-256: `07b6a1bcccac401bdca54301260e9d717cf42b9b80732c20cde5b60ef74306bd` (872 bytes).  
Output ends `STATUS=PASS`.

The exhaustive range is regression/adversary evidence only; the response and density lemmas above are exact all-size proofs.

## 8. Conditional end-to-end argument and current first missing implication

The campaign lead's current conditional end-to-end argument remains:

`unit FOREST on every K_n`
`=> Cocks FIXED(K_n) weighted upgrade`
`=> weighted minor closure`
`=> every finite simple deletion subgraph`
`=> unit FOREST target`.

This run does not claim to close the external source-body gate identified by account03/B02. If the published Cocks fixed-graph theorem is accepted as stated, the lead candidate has no internal mathematical gap recorded here. If proof-body verification is required, the first essential missing implication is still an independently auditable proof of `U(K_n)=>W(K_n)` (or a line-check of Cocks `FIXED(G)`).

On the assigned separator route, however, the first formerly unsupported weighted implication has been sharpened to a purely source-valid equivalence: all positive virtual responses are equivalent to the dense family of unit-simple theta extensions. Any failure is therefore automatically convertible into a genuine source graph counterexample rather than remaining an artificial weighted obstruction.

## 9. Status

**ESSENTIAL_STEP_APPLIED.**

New essential step: exact two-terminal response factorization plus the dense theta realization, yielding a source-valid equivalence for the weighted separator envelope and an arbitrary-size parallel-class adversary from a simple graph. This directly applies the named account03/B01 activity identity and supplies a corrected sufficient statement without assuming a bounded `{1,2}` intermediate weight set.

Privacy/provenance review: PASS. No credentials, machine-local paths, raw private transcripts, unrelated private data, or unsafe serialized objects are present.
