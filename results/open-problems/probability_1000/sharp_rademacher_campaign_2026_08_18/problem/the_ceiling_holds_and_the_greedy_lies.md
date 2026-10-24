# The 1/β ceiling survives a falsification sweep — and the greedy that measures it is loose by up to 3×

> ## CORRECTION BANNER (05:0x, one hour after this was written)
>
> **§2 of this document is WRONG and Conjecture R is FALSE.** See `the_rooting_must_not_explain_away_the_constraints.md`.
>
> - The book (theta `m=1`) has **exact `d_cb` = 1, not 2**, so it does *not* attain the ceiling — that claim was a greedy artifact, produced by exactly the failure this document's own §3 describes.
> - Rooted at its own shared pair (`nW=2`) the book gives exact ratios **2.5, 3.0, 4.25, 6.6** for `p = 2..5`, growing without bound. `d_cb ≤ C·L_{Q|W}` fails for **every** constant `C`.
> - Mechanism: putting the constraints' shared support into `W` **explains away the constraints**, driving `L → 0` while the dual is untouched.
> - Still standing: §3 (the greedy is loose by up to 3×), §4 (my registered predictions confirmed the heuristic, not the mathematics), §5's control finding, and `L = kβ` for the star. The *verified* ceiling-attaining objects reduce to two — the NAE triangle and star `k=3` at `nW=3`, both with exact `d_cb`.
> - This does **not** falsify the packet's target (41)/(3), whose left side is a quotient `dim((R+R_<)/R_<) ≤ d_cb`. See §4 of the correcting note for the dichotomy.

Author: main session c53c1d50, 2026-08-19 ~04:2x. Two findings, one of which undercuts the other and matters more.

## 1. What was tested

The rooted target asks `dim((R+R_<)/R_<) ≤ C·L_{Q|W}`. The campaign's floor for `C` is `1/β = 1/log₂(4/3) = 2.40942`, derived from NAE three-circuit products. The obvious question is whether that floor is also a **ceiling** on computable objects:

> **Conjecture R.** For every NAE-constraint sign fibre, rooted at any boundary set `W`, `d_cb / L_{Q|W} ≤ 1/β`.

Tested across six families — the k-arm NAE star, the wheel (hub plus cyclic rim), the open path rim, the double-star, the theta/book, the dense hub, and several hundred random NAE hypergraphs at `r = 5..9` — under three rootings (`nW = 1, 2, 3`). Machinery: the campaign's own exact-rational code path, factored into `scratchpad/rooted_machinery.py` so no experiment runs a different variant of `rank_of`/`full_dual` than another.

## 2. Conjecture R was not falsified, and the ceiling is attained repeatedly

No configuration exceeded `1/β` once computed correctly. Several **attain it exactly**:

| object | `L` | `d_cb` | ratio |
|---|---|---|---|
| NAE triangle (one arm) | `β` | 1 | `1/β` exactly |
| theta `m=1` — three NAE triples sharing a pair, i.e. a 3-page book | `2β` | 2 | `1/β` exactly |
| star `k=3` re-rooted at `nW=3` | `2β` | 2 | `1/β` exactly |
| star `k=4` re-rooted at `nW=3` | `3β` | 3 | `1/β` exactly |
| star `k=5` re-rooted at `nW=3` | `4β` | 4 | `1/β` exactly |

Two things are worth noting. The theta/book is the campaign's own floor family (NAE three-circuit products) **recovered independently** by a blind sweep that was not looking for it — an unplanned positive control. And re-rooting is a *lever*: raising `nW` shrinks `L` while `d_cb` holds, driving a comfortably-interior star exactly onto the ceiling. The extremal set is therefore much larger than the single triangle I had assumed.

An exact closed form did come out of the star family: **`L = kβ` exactly** for the k-arm star at `nW = 1`, confirmed by `L/β = 1.000, 2.000, 3.000, 4.000` at `k = 1..4`.

## 3. The finding that undercuts the first: the greedy is loose by up to 3×

The sweep initially reported **six violations**, ratios to 3.6141. I had written the safety direction into the script before running it: `d_cb` from the greedy selector search is an **upper** bound, so a reported ratio *above* the ceiling proves nothing — the true `d_cb` may be smaller. Every apparent violation had to be recomputed exactly (all bases exhaustively, all selector assignments by DFS with a rank bound) before it could count.

**All ten violating configurations collapsed to exact `d_cb = 1`, against a greedy value of 2 or 3.** Both positive controls landed exactly in the same pass: the NAE triangle at `d_cb = 1`, and the crosspolytope `A_4` at `d_cb = 1` (dossier tag (31)).

So the greedy overestimates by a factor of up to 3 on random NAE fibres. That is not a footnote. **Every `d_cb` this campaign has computed with the greedy is an upper bound of unmeasured quality**, and any argument that reads a computed `d_cb` as a value — rather than as a bound — inherits the looseness.

Where exact computation was affordable the greedy happened to be tight: star `k = 1, 2, 3` gave exact `d_cb = 1, 1, 2`, matching. Past `k = 3` the exhaustive search does not finish (star `k=4` truncated at a *worse* bound, 4, than the greedy's 3 — the truncation makes it uninformative, not a correction). So:

> **`d_cb = k−1` for the star is verified exactly only at `k ≤ 3`. Beyond that it is an upper bound.**

## 4. What this costs me, stated plainly

Earlier tonight I derived `ratio = (1/β)(1 − 1/k)` with margin exactly `(1/β)/k` for the star family, and registered two predictions (`k=5 → d_cb=4`, `k=6 → d_cb=5`) that both hit. **Those predictions confirmed the greedy's output, not the mathematics.** A heuristic can be perfectly predictable and still be wrong about the quantity it estimates; predicting it successfully measures my model of the heuristic, not the object. The formula stands as a statement about upper bounds and as a conjecture about the truth — not as a result.

The same correction applies to the wheel and path numbers from the same run.

## 5. What survives, and what it is worth

- **Conjecture R is not falsified** by any of the several hundred configurations tested, including the exact recomputations. Since `d_cb` is an upper bound, every **MEETS** verdict is *safe* — the true ratio is at most the reported one. The sweep's conclusion is therefore sound in the direction it matters.
- **The `1/β` ceiling is attained by a family, not a point** — triangle, book, and re-rooted stars — which strengthens the campaign's floor `C ≥ 1/β` by recovering it from independent objects.
- **A control killed my motivation for the experiment.** I built the wheel to test whether *non-separability* forces failure. The open path — same constraints minus the wrap edge, so separable — behaves identically (ratios 1.00–1.57 against the wheel's 1.00–1.64). Non-separability is **not** the operative variable, so the wheel result must not be reported as being about it.
- Everything here is still measured on **known non-members** of the residual class, which remains the campaign's standing exposure.
