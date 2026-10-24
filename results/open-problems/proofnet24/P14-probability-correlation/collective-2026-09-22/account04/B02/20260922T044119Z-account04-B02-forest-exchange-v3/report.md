# FOREST / account04-B02 — the minimal local Hall graph fails on K5, while a radius-two switch graph exactly matches through K6

Run: `20260922T044119Z-account04-B02-forest-exchange-v3`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Outcome: **CANDIDATE_REFUTED**, with a repaired radius-two mechanism retained as finite exact evidence only.  
Parent status: the team already has a separate internal `FULL_PROOF_CANDIDATE`; this run neither strengthens that label nor promotes it to an established/public theorem.  
Execution context: **WITHOUT_VERIFIED_BRAIN**.

## 1. Exact target and latest complete lead state

The target is the Grimmett--Winkler unit-weight law on **all** unrooted forests of every finite simple graph. For distinct edges `e,f`, with exact forest counts `Z,Z_e,Z_f,Z_ef`, prove

`Delta_G(e,f)=Z_e Z_f-Z Z_ef >= 0`.

The newest lead invocation visible during this run, `account01/B01/20260922T040935Z-b01-forest-r11/`, contained only its start record. I therefore used the latest complete lead version

`account01/B01/20260922T030948Z-b01-forest-auto11/report.md`, blob `58b8b1d8ac522a4eda7479400820e590c12f22aa`, candidate `FOREST-KN-COCKS-RECONCILED-v3`.

That candidate's end-to-end chain is: exact complete-graph Hermite positivity; the fixed-graph Cocks implication recorded in the final Semple--Welsh paper; minor closure of independence correlation; then deletion from `K_n` to an arbitrary finite simple graph. Two independent existing-worker reviews are recorded. I do not duplicate that analytic proof here.

The direct-coupling route remains useful as an independent construction and as an adversarial test of the count comparison.

## 2. Named OTHER-account input and the exact residual comparison

I consumed account01/B03's exact overlap/reconnection identity from

`account01/B03/20260921T234923Z-b03-poprestore-r11/overlap_reconnection_report.md`, blob `4dbaa2d764eddbc02026736e5b1fe265ba14f24d`,

and its later size-graded checker

`account01/B03/20260922T0112Z-b03-forest-r11/graded_reconnection_checker.cpp`, blob `f93dfbc346d728e58d97a2333ee3315ca2bac301`, output blob `a7ae3bb7d97119ea82f7ca76bc29193b89752f78`.

For `K=G-{e,f}`, let `N` be all forests of `K`, `A` those in which `e` is addable, `B` those in which `f` is addable, and `D` those in which `e,f` are jointly addable. Then

`Delta=|A||B|-|N||D|`.

Cancelling the common `A x D` fiber gives the exactly equivalent residual comparison

`|(N\A) x D| <= |A x (B\D)|`.                                      (R)

In the partner's addability cells, with `q` the overlap reservoir,

`|N\A|=n00+n01`, `|D|=n11-q`, `|A|=n10+n11`, `|B\D|=n01+q`,

so (R) is

`(n00+n01)(n11-q) <= (n10+n11)(n01+q)`,

which expands exactly to account01/B03's

`Delta=n10*n01-n00*n11+N*q >= 0`.

Thus the exchange problem below is not a stronger surrogate: it is the partner's exact Rayleigh comparison after cancellation.

## 3. Prior local candidate and the Hall question

The preceding B02 run proved on `K_n` that every residual pair `(F,H) in (N\A) x D` has a size-preserving local repair using at most two cut/join operations. If `H` has a one-edge blocker, the proposed minimal rule used one path-edge deletion in `F` and one blocker addition in `H`; only the exactly classified zero-blocker states were allowed two cuts and two joins.

The unpaid statement was that choices of these local moves could satisfy Hall and therefore give an injection from the residual domain to the residual codomain.

This run attacks that exact Hall statement rather than assuming that local reachability implies global injectivity.

## 4. Exact K5 Hall obstruction to the minimal local move graph

Take `K_5` with disjoint marked edges

`e=ab`, `f=cd`,

and write the fifth vertex as `x`. Fix the jointly-addable second coordinate

`H={ax}`.

Its component partition is `{a,x}|{b}|{c}|{d}`. To leave `D` while keeping `f` addable by adding **one** nonmarked edge, the added edge must merge the `e`-endpoint components. The deleted marked edge `ab` is unavailable, so the unique one-edge blocker is

`bx`.

Therefore every neighbor of the entire fixed-H domain fiber under the previous one-switch rule has second coordinate `H+bx`.

Now examine the first coordinate. For each `F in N\A`, delete one edge of the unique `a-b` path. The set of distinct resulting forests is exactly the subset of `A` for which the `a`- and `b`-components admit at least one available nonmarked joining edge. On `K_5-{e,f}`, the only `A` states that fail this condition are those in which `a,b` are both isolated. On the remaining vertices `{c,d,x}`, with `f=cd` absent, these are exactly

`empty`, `{cx}`, `{dx}`, `{cx,dx}`.

Hence the one-cut shadow has size

`|A|-4 = 64-4 = 60`.

The fixed-H residual domain fiber has size

`|N\A|=70`.

Consequently the neighbor set of

`S=(N\A) x {H}`

in the prior minimal local graph has only `60` vertices, while `|S|=70`. Hall fails with exact deficiency

`70-60=10`.

This is a genuine counterexample to the **direct-coupling candidate**, not to the forest theorem.

### Formula-level comparison with the partner counts

For disjoint edges of `K_5`, the exact partner state is

`(n00,n10,n01,n11,q)=(49,21,21,43,14)`.

Therefore

`|N\A|=49+21=70`,

`|D|=43-14=29`,

`|A|=21+43=64`,

`|B\D|=21+14=35`.

The full residual inequality is

`70*29 = 2030 <= 64*35 = 2240`,

with Rayleigh slack `210`. Thus the theorem's codomain has ample total capacity even though the previous local neighborhood of this one fixed `H` is deficient. The failure is genuinely geometric/local, not a failure of the target count.

## 5. Why the obstruction specifically requires second-order routing even when a one-blocker exists

The previous rule allowed a two-switch only for zero-blocker states. The K5 witness shows that this restriction is too severe: `H={ax}` **does have** a one-blocker, but its one-switch neighborhood is too small to carry the whole first-coordinate fiber.

Permit instead either of two degree-preserving layers:

- `k=1`: delete one edge from the unique `a-b` path of `F` and add one edge to `H` so the output lies in `B\D`;
- `k=2`: delete two distinct edges from that path and add two nonmarked edges to `H`, again requiring a forest in `B\D`.

For the fixed witness `H={ax}`, exact enumeration gives

- one-cut first-coordinate shadow: `60`;
- one-edge second-coordinate outputs: `1`;
- two-cut first-coordinate shadow: `34`;
- two-edge second-coordinate outputs: `14`.

The 14 two-edge outputs split exactly into

- `10` ordinary `n01` states, where `e` is no longer addable;
- `4` `Q`-reservoir states, where both marked edges are individually addable but jointly cyclic.

So the repaired mechanism necessarily uses **both** channels that appear in the partner identity. A concrete valid second-order output is obtained by adding `ac` and `bc` to `H`: the result is a forest, `f=cd` remains addable, while `e=ab` is blocked by the path `a-c-b`.

The two move layers are separated by the size of the second coordinate, so their raw fixed-fiber target capacity is

`60*1 + 34*14 = 536`.

This does not prove Hall, but it removes the exact deficiency that killed the previous candidate.

## 6. Exact full matching test for the repaired radius-two graph

I then built the actual bipartite graph whose left vertices are `(N\A) x D` and right vertices are `A x (B\D)`. A left pair is connected to a right pair precisely when, for the same `k in {1,2}`,

1. the first coordinate is obtained by deleting `k` distinct edges of its unique `a-b` path; and
2. the second coordinate is obtained by adding `k` nonmarked edges, remains a forest, keeps `f` addable, and leaves `D`.

This retains exact edge cardinality across the pair and all component information used to decide acyclicity/addability. It does not collapse the state to an averaged component count.

Exact Hopcroft--Karp matching results were:

| orbit | graph | residual domain | residual codomain | switch edges | maximum matching |
|---|---:|---:|---:|---:|---:|
| adjacent | `K_3` | 0 | 2 | 0 | 0 |
| adjacent | `K_4` | 16 | 60 | 102 | 16 |
| adjacent | `K_5` | 1334 | 3290 | 22164 | 1334 |
| adjacent | `K_6` | 146316 | 300104 | 5519604 | 146316 |
| disjoint | `K_4` | 30 | 36 | 120 | 30 |
| disjoint | `K_5` | 2030 | 2240 | 23120 | 2030 |
| disjoint | `K_6` | 207468 | 220520 | 5664464 | 207468 |

Every tested residual domain is perfectly matched. The executable output ends `ALL_EXACT_ASSERTIONS_PASSED`.

Checker source SHA-256:

`cb8b49a8e6512f55b1a259887edb776cfd23286e1e6003d28e92670b83703eae`.

Captured output SHA-256:

`cf8bd9e1aff8e33301a1be29ece8e442c14877c13c37f8103d407328cade953f`.

The matching computation is finite evidence only; it is not used as a proof for arbitrary `n`.

## 7. Conditional end-to-end direct-coupling argument and the first missing implication

A compact direct-coupling route on complete graphs is now:

1. use the exact cancellation (R);
2. form the radius-two switch graph just defined;
3. **if** this graph satisfies Hall for every `K_n` and both edge orbits, a matching injects `(N\A)xD` into `A x (B\D)`;
4. this proves `Delta_{K_n}(e,f)>=0` directly;
5. the lead's independently source-bound Cocks/minor transfer then carries complete-graph unit pNC to every finite simple graph.

The first essential missing implication is therefore the following precise statement:

> **FOREST-RADIUS2-HALL-v1.** For every `n` and every adjacent or disjoint marked pair in `K_n`, every subset of the residual domain has at least as many neighbors in the radius-two switch graph defined in Section 6.

I have **not** proved that statement. It is a repaired candidate, not payment of the old Hall step. The new theorem-level contribution of this run is negative: the strictly narrower minimal local Hall candidate from the preceding run is false, with the exact K5 witness above.

A useful next attack is to exploit the product-layer form

`C_1(F) x J_1(H)  union  C_2(F) x J_2(H)`

and prove Hall by a weighted shadow inequality that keeps the exact terminal-component sizes. Any such proof must cover arbitrary subsets, not merely compare total layer sizes.

## 8. Honest classification

**Outcome: CANDIDATE_REFUTED.**

Refuted candidate: the prior minimal local Hall strategy that restricts a blocker-bearing `H` to one-cut/one-join moves and reserves two-switch moves only for zero-blocker states.

Surviving repaired mechanism: `FOREST-RADIUS2-HALL-v1`, supported by exact perfect matchings through `K_6` for both complete-graph edge orbits, but universally **unproved**.

The parent FOREST theorem is not refuted. The team's separate analytic `FULL_PROOF_CANDIDATE` remains exactly as previously recorded and is not promoted here.

## 9. Integrity and handoff

This run used only the selected FOREST archive, the latest complete lead report, the named account01/B03 partner result, exact finite computation, and source-scoped control material. No benchmark gold, credentials, scheduler identifiers, machine paths, unrelated private material, email, Drive action, paid/remote compute, workflow dispatch, production mutation, permission change, or public posting was used.

Next recipients: team lead `account01/B01` and assigned partner `account01/B03`. Preserve the K5 Hall witness as a permanent failure case. Any direct coupling that keeps the prior local move rule is dead; a repaired proof must allow second-order routing even for some states that already possess a one-edge blocker, and must prove a genuine arbitrary-subset Hall/flow inequality rather than total-capacity positivity.
