# FOREST / fleet04 B02 — an edge-multiplicity-fiber obstruction to global exchange flow

**Run:** `20260922T101358Z-fleet04-B02-forest-exchange-v5`  
**Outcome:** `CANDIDATE_REFUTED`  
**Refuted candidate:** `FOREST-UNION-MULTIPLICITY-PRESERVING-FLOW-v1`  
**Parent FOREST target:** `OPEN`  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact source scope and consumed peer versions

The source target is the Grimmett--Winkler pairwise negative-correlation conjecture for the **uniform law on all unrooted forests** of a finite simple graph, with unit edge weights. Thus disconnected forests, isolated vertices, the empty forest, and every forest size are present. For distinct physical edges `e,f`, if `Z` counts all forests and `Z_e,Z_f,Z_ef` count the indicated containments, the target is

`Delta_G(e,f)=Z_e Z_f-Z Z_ef >= 0`.

The source boundary is the collective `TARGETS.md`, which points to Grimmett--Winkler, *Negative association in uniform forests and connected graphs*, arXiv:math/0302185, Conjecture 1.1 and pages 2--3. No rooted, fixed-size, spanning-tree, arbitrary-weight, or matroid-general law is substituted here.

The newest **complete** lead version available before this derivation is fleet01/B01 `20260922T050946Z-b01-forest-auto11`, candidate `FOREST-TRIANGLEFREE-SIMPSON-BUDGET-v1`, canonical report creation commit `79044b575c4b689248892f37b9930e983dddabca`. I use its corrected source boundary: the earlier fixed-graph Cocks globalization is not treated as valid, and the source-generated triangle-conditioning debt is the `{1,2}` STAR-2 comparison. This run does not claim to solve that lead obligation.

The named OTHER-account result consumed **in formulas** is partner fleet01/B03 `20260922T065221Z-fleet01-B03-forest-r11b`, report blob `ab3dd67ff2b8608e68f9e272f6334ff1e4e2c0ef`. Its exact base-forest identity and overlap-incidence decomposition are the interface attacked below.

## 2. Partner identity and the proposed different coupling

Fix `G,e,f` and let

`B = G-{e,f}`.

For a base forest `H` of `B`, put `X(H)=1` when `H+e` is acyclic and `Y(H)=1` when `H+f` is acyclic. Let `A_ij` be the base forests with `(X,Y)=(i,j)`, write `n_ij=|A_ij|`, let `N` be the total number of base forests, and let

`Q = {H in A_11 : H+e+f is cyclic}`, `q=|Q|`.

Fleet01/B03 proves by exact cancellation

**(2.1)** `Delta = n10*n01 + q*N - n00*n11`.

Consequently a direct injection proof would map

`A_00 x A_11`

into the disjoint union

`(A_10 x A_01) disjoint_union (Q x F(B))`.

The previous B02 fixed-radius switch attempts restricted how far edges could move. The mechanism tested here removes **all radius bounds**: allow an arbitrary global recolouring/transfer of base edges between the two forests, but preserve for every physical base edge `g` its total number of copies across the ordered pair. This is the natural strongest version of a pure exchange flow that only moves already-present copies between the two coordinates.

For an ordered pair `(F1,F2)`, define its multiplicity signature

`sigma_g(F1,F2)=1[g in F1]+1[g in F2] in {0,1,2}`

for each `g in E(B)`. For every signature `sigma`, define

`D_sigma = |{(A,H) in A_00 x A_11 : sigma(A,H)=sigma}|`,

and

`C_sigma = |{(C,D) in A_10 x A_01 : sigma(C,D)=sigma}|`

`          + |{(K,H) in Q x F(B) : sigma(K,H)=sigma}|`.

The products in (2.1) split exactly into these fibers, so

**(2.2)** `Delta = sum_sigma (C_sigma-D_sigma)`.

Any injection that preserves every `sigma_g` must operate fiber by fiber and therefore requires

**(2.3)** `D_sigma <= C_sigma` for every `sigma`.

The same necessary condition holds for a fractional transport/flow with unit source masses and unit target capacities, not only for a deterministic injection.

## 3. Exact K4 counterexample to the coupling candidate

Take `G=K4` on vertices `0,1,2,3` and mark the opposite edges

`e=01`, `f=23`.

Then the base graph `B` is the four-cycle / `K_{2,2}` with edges

`02,03,12,13`.

Exact enumeration of all base forests gives

`N=15`, `(n00,n10,n01,n11,q)=(4,2,2,7,2)`.

Thus the source Rayleigh gap is positive:

`Delta = 2*2 + 2*15 - 4*7 = 6`.

So this graph is **not** a counterexample to FOREST.

Now take the all-once signature

`sigma*=(1,1,1,1)`,

meaning that each of `02,03,12,13` appears in exactly one of the two coordinates.

### Domain count

There are exactly four pairs in the domain fiber. The `A_00` coordinate is any three-edge spanning tree of the four-cycle; its complement is the remaining singleton edge, which lies in `A_11`. Therefore

**(3.1)** `D_sigma*=4`.

### Ordinary `(10)x(01)` channel

The two `A_10` forests are the two-edge stars

`{02,03}` and `{12,13}`.

Under the all-once signature, the second coordinate must be the complementary two-edge star. But that complement is again in `A_10`, not `A_01`. Hence

**(3.2)** `C_sigma*^(ordinary)=0`.

### `Q x F(B)` channel

The two `Q` forests are precisely the perfect matchings

`{02,13}` and `{03,12}`.

For the all-once signature the other coordinate is forced to be the complementary matching. Therefore exactly two ordered `Q`-channel pairs exist:

**(3.3)** `C_sigma*^(Q)=2`.

Combining (3.1)--(3.3),

**(3.4)** `D_sigma*=4 > 2=C_sigma*`.

This violates the necessary fiber Hall condition (2.3). Therefore there is no deterministic injection, no fractional unit-capacity transport, and no arbitrarily long/adaptive edge-recolouring flow that proves (2.1) while preserving every base edge's aggregate multiplicity across the pair.

The obstruction is stable under adding arbitrary extra vertices or edges: if a larger graph contains this `K4` with `e,f` opposite, choose the same all-once signature on the four cross edges and multiplicity zero on every other base edge. The same four domain states and two codomain states survive verbatim. Thus the issue is not an isolated finite-graph accident.

## 4. Exact comparison with fleet01/B03's overlap formula

The partner report further splits `A_00` into `D` (the unique `e`- and `f`-blocking paths are edge-disjoint) and `O` (they share an edge). For `H in O`, let `s(H)` be the number of shared path edges. For `K in Q`, let `c(K)` be the number of physical base edges reconnecting the two distinguished `K`-components. Fleet01/B03 proves the incidence identity

`I=sum_{H in O}s(H)=sum_{K in Q}c(K)`,

sets `E_O=I-|O|` and `E_Q=I-q`, and obtains

**(4.1)** `Delta=[n10*n01-d*n11] + q(N-n11) + n11*E_O - n11*E_Q`.

For the opposite-edge `K4` instance, every one of the four `A_00` trees has exactly one common path edge, while each of the two `Q` matchings has exactly two reconnecting base edges. Hence

`d=0`, `o=4`, `I=4`, `E_O=0`, `E_Q=2`.

The four terms of (4.1) are therefore

`4, 16, 0, -14`,

which sum to the same source gap `6`.

This pinpoints the limitation of the global incidence-flow suggestion in the partner report. The partner correctly showed that overlap debt must transfer into the ordinary switching sector. The present counterexample proves more: **if that transfer merely recolours or moves existing edge copies between the two forests, it cannot succeed**, because the all-once multiplicity fiber has deficit two even though the total comparison has surplus six. Some source mass must cross multiplicity signatures.

## 5. Exact checker and minimal finite audit

`multiplicity_fiber_check.py` independently enumerates all unrooted base forests, computes the four cells and `Q`, reconstructs both sides of every multiplicity fiber, verifies the fleet01/B03 overlap-incidence decomposition, and then audits every simple marked-edge instance on at most four vertices.

Its exact output is saved as `multiplicity_fiber_check.out`. The decisive lines are:

`K4_DISJOINT_COUNTS 15 4 2 2 7 2 6`

`ALL_ONES_SIGNATURE ... domain 4 ordinary 0 q_channel 2 fiber_deficit 2`

`B03_DECOMPOSITION d 0 o 4 I 4 4 E_O 0 E_Q 2 terms (4,16,0,-14) sum 6`

`SMALL_GRAPH_AUDIT [(2,0,0),(3,6,0),(4,240,3)] ...`

`ALL_EXACT_ASSERTIONS_PASSED`.

Thus no multiplicity-fiber violation occurs in the six marked instances on three vertices, and the first violations at order four are exactly the three choices of opposite marked edges in `K4`. This finite audit establishes neither FOREST nor any asymptotic statement; it only checks the obstruction and its minimum order inside the audited range.

## 6. Compact conditional end-to-end chain and first surviving obligation

A direct coupling proof can still follow the partner's exact identity (2.1), but the chain now has a sharper necessary design constraint:

1. partition the deficit domain `A_00 x A_11` and the two exact credit channels `(A_10 x A_01)` and `Q x F(B)`;
2. retain the partner's component-incidence multiplicities so overlap-cycle debt is not averaged away;
3. permit **cross-signature** moves that change the aggregate multiplicity of at least one physical base edge across the ordered pair;
4. prove global injectivity/Hall capacity after those moves, not separately inside each fixed union multiset.

Step 3 is not offered as a new sufficient condition or disguised restatement of FOREST. It is a **necessary feature** forced by the source-valid `K4` counterexample above. A concrete next construction should therefore look for a reversible cycle/path operation that changes the union multiset while routing the two excess all-once `K4` states into surplus signatures, and then prove that the corresponding component-level rule is well defined on general graphs. The lead's independent STAR-2 conditioning obligation remains open in parallel.

## 7. Status and provenance

`CANDIDATE_REFUTED` applies only to `FOREST-UNION-MULTIPLICITY-PRESERVING-FLOW-v1`. It does not refute the Grimmett--Winkler conjecture and does not refute fleet01/B01's current triangle-free/STAR-2 lead route. The parent target remains **OPEN**.

The calculation uses only the source graph model and exact integer enumeration. No brain installation, benchmark material, mixed-domain memory, private transcript, email, Drive action, public release, paid model/API, remote workflow, or production mutation was used. The repository destination is the private canonical research archive authorized by the collective assignment.
