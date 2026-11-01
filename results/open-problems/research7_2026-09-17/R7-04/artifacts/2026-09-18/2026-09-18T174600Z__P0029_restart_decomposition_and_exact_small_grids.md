Model actually running: GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum; no authenticated runtime model/effort telemetry or binding selector is exposed.

# P0029 — descending-label restart decomposition and exact small-grid certificates

## 1. Source target and idea before code

For the `n x n` grid `G_{n,n}`, choose a uniformly random bijective labeling by `1,...,n^2`, condition on exactly two peaks, and let `rho_n` be the graph distance between the peaks. Burdzy Problem 9 asks whether `rho_n/n -> 0` in distribution.

The useful change of category is to reveal vertices in **descending label order**. Write the reveal order as

`v_1, v_2, ..., v_N`, `N=n^2`,

and `S_k={v_1,...,v_k}`. When `v_k` is revealed, it is a peak of the completed labeling if and only if it has no neighbor in `S_{k-1}`. Indeed, vertices in `S_{k-1}` have larger labels, while all unrevealed vertices have smaller labels. Thus

> **peaks are exactly restart/birth times of the descending reveal process.**

Conditioning on exactly two peaks is therefore conditioning the reveal process to have exactly two births. This yields an exact subset dynamic program and a factorized double-counting formula that keep the peak distance visible.

## 2. B18 — exact translation theorem

Let `G=(V,E)` be any finite graph and `sigma=(v_1,...,v_N)` a permutation of its vertices, interpreted as descending label order. Define a birth at time `k` when

`N(v_k) ∩ {v_1,...,v_{k-1}} = empty`.

### Proposition 2.1

The peaks of the labeling corresponding to `sigma` are exactly the birth vertices. Hence labelings with exactly two peaks are in bijection with vertex permutations having exactly two births, and the distance between the peaks is the distance between the two birth vertices.

### Proof

The label at `v_k` exceeds precisely the labels of vertices appearing after time `k`. Therefore `v_k` is a local maximum exactly when none of its neighbors appears before it, which is exactly the displayed birth condition. This correspondence is bijective because every labeling has one and only one descending vertex order. QED.

A useful immediate corollary is that two peaks can never be adjacent: the later/lower of two adjacent candidates has the earlier/higher one as a previously revealed neighbor.

## 3. B25 — exact restart DP

For `S subset V` and `r in S`, define `A_S(r)` to be the number of orderings of `S` whose descending reveal process has exactly one birth, namely the first vertex `r`. Set

`A_{ {r} }(r)=1`.

For `v notin S`:

- if `N(v) ∩ S != empty`, then appending `v` creates no new birth and contributes

  `A_{S union {v}}(r) += A_S(r)`;

- if `N(v) ∩ S = empty`, appending `v` creates the second birth.

Let `B_S` be the number of orderings of `S` having exactly two births, and `M_S` the sum, over those orderings, of the graph distance between their two birth vertices. When a one-birth state `(S,r)` appends a birth `v`,

`B_{S union {v}} += A_S(r)`,

`M_{S union {v}} += d_G(r,v) A_S(r)`.

Once two births have occurred, only a vertex `v` with `N(v) ∩ S != empty` may be appended; otherwise a third birth is created. Thus for every such legal `v`,

`B_{S union {v}} += B_S`,

`M_{S union {v}} += M_S`.

At `S=V`, Proposition 2.1 gives the exact identities

`B_V = #{labelings of G with exactly two peaks}`,

`M_V = sum_{two-peak labelings L} d_G(peak_1(L),peak_2(L))`,

and therefore

`E[d_G(peak_1,peak_2) | exactly two peaks] = M_V/B_V`.

All quantities are integers until the final division.

## 4. Factorized ordered-pair formula

There is a second exact form useful for asymptotics. Let `F(T)` count completions from an already revealed set `T` with **no further births**. Then

`F(V)=1`,

and

`F(T) = sum_{v notin T : N(v) ∩ T != empty} F(T union {v})`.

For an ordered pair of nonadjacent vertices `(r,v)`, let `W(r,v)` denote the number of full labelings in which `r` is the first (higher) peak and `v` is the second peak. Then

`W(r,v) = sum_{S: r in S, v notin S, N(v) ∩ S = empty} A_S(r) F(S union {v}).`    (4.1)

### Proof of (4.1)

Immediately before the second birth, the already revealed set is a unique set `S` containing the first peak `r`; its one-birth prefix can be ordered in `A_S(r)` ways. The second peak `v` must have no neighbor in `S`. Once it is revealed, every remaining reveal must touch the current set, and there are exactly `F(S union {v})` such completion orders. Conversely every term in the sum gives a unique full ordering with exactly those ordered peak identities. QED.

Consequently

`B_V = sum_{r != v} W(r,v)`,

`M_V = sum_{r != v} d_G(r,v) W(r,v)`,

where adjacent pairs automatically have weight zero.

For any connected graph and any nonadjacent `r,v`, `W(r,v)>0`: reveal `r`, then `v`, then take any ordering that grows the revealed set by boundary vertices. Thus the asymptotic question is not support of the pair law but its **weight profile**.

## 5. B2 — obstruction/counterexample-first finite test

The source asks whether conditioned peak distance is sublinear. The first falsification test is therefore to compute the exact finite pair-distance law, not to simulate a guessed limiting shape.

The recurrence above was executed using Python arbitrary-precision integers. It was independently checked by exhaustive enumeration of every vertex permutation for `2 x 2`, `2 x 3`, and `3 x 3`; the brute-force counts and distance sums agree exactly with the subset DP.

### Exact checks

| grid | two-peak labelings `B_V` | distance sum `M_V` | conditional mean distance | `E[rho_n/n]` when square |
|---|---:|---:|---:|---:|
| `2 x 2` | `8` | `16` | `2` | `1` |
| `2 x 3` | `424` | `1008` | `1008/424 = 2.377358...` | — |
| `2 x 4` | `21,504` | `59,392` | `2.761904...` | — |
| `3 x 3` | `143,808` | `383,616` | `1998/749` | `666/749 = 0.889185580774...` |
| `3 x 4` | `83,995,376` | `251,626,864` | `2.995722812170...` | — |
| `4 x 4` | `779,299,174,080` | `2,538,510,905,280` | `377754599/115967139` | `377754599/463868556 = 0.814356985646...` |

For the `4 x 4` square, the exact distance distribution is

| peak distance `d` | number of conditioned labelings with distance `d` |
|---:|---:|
| 2 | `173,341,437,440` |
| 3 | `313,977,112,960` |
| 4 | `217,620,337,600` |
| 5 | `66,746,375,360` |
| 6 | `7,613,910,720` |

Thus, at `n=4`,

`P(rho_4 >= 3 | exactly two peaks) = 1893617927/2435309919 = 0.77756753349...`,

and

`P(rho_4 >= 4 | exactly two peaks) = 101382161/270589991 = 0.37467077265...`.

These figures are **finite certificates only**. They do not prove that the source answer is no, nor do they move the frozen asymptotic metric `D_*`. What they do show is that a proof of `rho_n/n -> 0` cannot be justified by an already-visible small-grid collapse: through `n=4`, the exact conditioned measure still places most of its mass at distances at least `3` and a substantial mass at distances at least the side length.

## 6. What the old orientation formulation was hiding

Orienting every edge toward the larger label correctly identifies peaks with sinks, but summing linear-extension counts over all acyclic orientations with two sinks mixes two difficulties: choosing the sinks and counting the compatible orders. Formula (4.1) separates them at the **second restart**. The prefix term `A_S(r)` asks for a one-birth connected growth from `r`; the suffix term `F(S union {v})` asks for a no-further-birth growth from the two-seed set. The only interface is the avoidance condition `N(v) ∩ S = empty`.

This identifies the exact gluing bottleneck for an asymptotic proof: compare the aggregate values `W(r,v)` for close versus macroscopically separated pairs. There are `Theta(n^4)` macroscopically separated pairs but only `o(n^4)` pairs at distance `o(n)`; therefore any sufficiently uniform comparison of `W(r,v)` across nonadjacent pairs would refute convergence to zero. What is missing is a source-valid bound showing that pair weights cannot concentrate strongly enough on the `o(n)`-distance pairs.

## 7. Frozen metric and outcome

The admitted metric is

`D_* = limsup_n E[rho_n/n | exactly two peaks]`.

Before this run: `UNKNOWN/UNMEASURED`.  
After this run: `UNKNOWN/UNMEASURED` — **NO MOVEMENT**.

The recurrence and exact finite table are new reusable mathematics/certificates, but no asymptotic positive lower bound for `D_*` has been proved.

## 8. Next mathematical attack

The next run should avoid repeating B2/B18/B25. The most promising target exposed by (4.1) is a comparison theorem for the no-further-birth completion count `F(T)` under moving the second seed. A useful sufficient statement would be any polynomial/subpolynomial pair-weight comparison strong enough that the `Theta(n^4)` entropy of macroscopic pairs beats the number of close pairs. If that fails, the failure should be localized by constructing seed sets for which `F({r,v})` or the full `W(r,v)` changes exponentially with separation.
