# POS3 fleet03/B11 — crossed two-distinguisher bias amplification

**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair whose ordering probability under the uniform law on all linear extensions lies in `[1/3,2/3]`.  
**Parent status after this report:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

This run implements `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`. The exact fleet03/B11 assignment is the distinct order-polytope/correlation route; named partner: `fleet04/B19`. No installation or benchmark work is resumed.

## 1. Exact source-bound state used

The current team lead input is fleet04/B10,

- `proofnet24/collective-POS3/fleet04/B10/20260922T034709Z-B10-POS3-r12/REPORT.md`, commit `838f837e53739dab6bf7143a5a8f59d183618b32`, blob `4759a4ecb5f2963a3d190f66fc6728459bb1a46e`.

It proves the crossed-neighborhood identity. If `x||y`, `Pred(x) subseteq Pred(y)`, `Succ(y) subseteq Succ(x)`, and

`D=Pred(y)\Pred(x)`, `U=Succ(x)\Succ(y)`,

then under the actual uniform full-extension law

`2 Pr(x<y)-1 = Pr(A_D union B_U)`,                         (1.1)

where `A_D={some d in D has x<d}` and `B_U={some u in U has u<y}`. In the inherited strict-chain/no-internal-descent branch, the canonical lower and upper fringe minority events are each below `1/3`.

The required named OTHER-account partner result consumed and applied is fleet04/B19,

- `proofnet24/collective-POS3/fleet04/B19/B19-20260922T031150Z-r46/REPORT.md`, commit `d543daee045673b95d5c6b3179902def33b19837`, blob `9079d05dcdf18d3afdb391d39148ed8c4653768d`.

It proves that repeated equal-predecessor clean-fork escalation in a finite no-balanced width-three poset terminates at an extreme incomparable pair with unequal predecessor sets. The terminal pair has at least two distinguishers, at least one lower. It also records the exact TP2 fork budget before that exit.

The immediate fleet03/B11 predecessor is

- `proofnet24/collective-POS3/fleet03/B11/20260922T031248Z-fleet03-B11-r11/REPORT.md`, commit `510dba7e1991d1e820e69358f8f7a54b2c6b0778`, blob `e6cf43b104d7d072d21362a4af2c21739c703506`.

It proves the exact two-distinguisher sign theorem: if an incomparable pair has exactly two distinguishers of opposite signs, then its ordering probability lies in `[1/3,2/3]`. Hence an extreme orientation with exactly two distinguishers forces both to have the same positive sign.

The new result below directly attacks the partner's first missing lower-distinguisher transport implication.

## 2. Crossed exact-two configuration

Let `P` be any finite poset and let `x||y`. Assume that relative to the orientation `x<y` the **only** two distinguishers are one positive lower witness `d` and one positive upper witness `u`:

`d<y`, `d||x`, `x<u`, `u||y`.                               (2.1)

Every other vertex has the same three-valued relation to `x` as to `y`. The relation `u<d` is impossible, because `x<u<d<y` would force `x<y`. Thus either `d<u` or `d||u`.

This report pays the `d||u` branch exactly and shows that it cannot propagate twice in a no-balanced counterexample.

## 3. Exact deletion-fiber words

Assume `d||u`. Delete the four special vertices and set

`R=P\{x,y,d,u}`.

Fix an arbitrary `tau in L(R)`. Number the external insertion gaps of `tau`. Since every vertex of `R` sees `x` and `y` identically, their exact admissible gap intervals coincide:

`I_x(tau)=I_y(tau)=I`.

Because `d<y`, the interval `I_d` is weakly left-shifted from `I`: its lower and upper endpoints are no larger than the corresponding endpoints of `I`. Because `x<u`, `I_u` is weakly right-shifted from `I`. Therefore `I_u` is weakly right-shifted from `I_d`.

The induced special poset consists of the two disjoint chains `d<y` and `x<u`. There are exactly six special words:

`W1=d y x u`,
`W2=d x y u`,
`W3=d x u y`,
`W4=x u d y`,
`W5=x d u y`,
`W6=x d y u`.

Let `n_i(tau)` be the exact number of lifts of `tau` with word `W_i`.

Two exact adjacent-swap facts hold fiber by fiber.

### Lemma 3.1 — equal central swap

`n_1(tau)=n_2(tau)`.                                          (3.1)

Indeed `W1` and `W2` differ only by exchanging the adjacent incomparable labels `x,y`, and these labels have identical external gap intervals.

### Lemma 3.2 — crossed outer swap

`n_4(tau)<=n_5(tau)`.                                         (3.2)

In `W4` the adjacent labels are `u,d`. Since `I_u` is weakly right-shifted from `I_d`, keep the numerical weakly increasing gap sequence fixed and exchange the two labels. If the old gaps are `i<=j` with `i in I_u` and `j in I_d`, the interval nesting gives both `i in I_d` and `j in I_u`; this injects lifts of `x u d y` into lifts of `x d u y`.

No induced distribution has been treated as uniform. These are exact multiplicities inside every deletion skeleton.

Sum `n_i(tau)` over all `tau` and denote the totals simply by `n_i`. Let

`E=e(P)=sum_i n_i`.

Define

`p = Pr(x<y)`,
`epsilon = Pr(y<x)=1-p`,
`alpha = Pr(x<d)`,
`beta = Pr(u<y)`,
`gamma = Pr(u<d)`,
`eta = Pr(x<d and u<y)`.

The six words give exactly

`epsilon = n_1/E`,                                             (3.3)

`alpha = (n_4+n_5+n_6)/E`,                                    (3.4)

`beta  = (n_3+n_4+n_5)/E`,                                    (3.5)

`gamma = n_4/E`,                                               (3.6)

`eta   = (n_4+n_5)/E`.                                        (3.7)

Using `n_1=n_2`,

`2p-1 = alpha+beta-eta`.                                      (3.8)

Using `n_4<=n_5`,

`eta>=2 gamma`.                                                (3.9)

Equation (3.8) is the singleton crossed-neighborhood identity recovered directly from exact extension words; (3.9) is the new order-polytope/exchange input.

## 4. Bias-amplification theorem

### Theorem 4.1 — one crossed incomparable-fringe expansion gains more than `1/6`

Under (2.1) with `d||u`, suppose

`Pr(x<y)>2/3`,
`Pr(x<d)<1/3`,
`Pr(u<y)<1/3`.                                                 (4.1)

Then

`2/3 < Pr(x<y) < 5/6`,                                        (4.2)

and the outer incomparable pair satisfies

`Pr(d<u) > Pr(x<y)+1/6 > 5/6`.                                (4.3)

Equivalently, if `epsilon=Pr(y<x)` and `gamma=Pr(u<d)`, then

`gamma < epsilon-1/6`.                                        (4.4)

### Proof

From (3.8)-(3.9) and the two strict fringe bounds,

`1-2 epsilon = alpha+beta-eta`
`              <= alpha+beta-2 gamma`
`              < 2/3-2 gamma`.

Hence

`gamma < epsilon-1/6`.

Since `gamma>=0`, necessarily `epsilon>1/6`, proving `p<5/6`. Finally

`Pr(d<u)=1-gamma > 1-(epsilon-1/6)=p+1/6`.

This proves (4.2)-(4.4). `square`

The theorem is arbitrary-size and does not use width three. Width three is used to force the crossed exact-two configuration from the campaign's minimal-counterexample funnel.

## 5. No-repeat corollary for the live POS3 branch

In a hypothetical no-balanced poset, the inherited no-internal-descent branch has exactly the two fringe inequalities in (4.1): the strong-majority order places

`d prec_* x prec_* y prec_* u`,

so `Pr(x<d)<1/3` and `Pr(u<y)<1/3`.

Therefore, whenever the partner's lower-distinguisher exit has exactly two positive distinguishers and their lower/upper witnesses are incomparable, Theorem 4.1 transports the proof to the outer pair `(d,u)` and **strictly increases the majority probability by more than `1/6`**.

In particular the same exact-two crossed/no-internal-descent mechanism cannot occur again at `(d,u)`: Theorem 4.1 itself says any pair satisfying that mechanism has majority probability strictly below `5/6`, whereas the transported pair has majority probability strictly above `5/6`.

Thus the incomparable-fringe exact-two residual terminates after one outward expansion. At the next stage at least one of the following must occur: a balanced fringe pair, at least three distinguishers, a comparable lower/upper fringe, the non-crossed successor branch, or a strong-majority span descent. In a hypothetical counterexample the first alternative is excluded, so the structure genuinely changes.

This is stronger than merely saying that the local quartet is not enough: it gives a strict quantitative potential that rises by more than `1/6` and therefore cannot cycle.

## 6. Exact-two funnel in the inherited strict-chain branch

Combine the partner and lead results with the previous fleet03/B11 sign theorem.

The partner supplies an extreme terminal pair with at least two distinguishers and at least one lower. If there are exactly two distinguishers, the previous sign theorem forces both to be positive.

In the inherited strict-chain branch the positive lower discrepancy `D` is a chain. If both of the two positive distinguishers were lower, there would be no positive upper discrepancy. Let `d=max D`. Then the lead's crossed identity reduces to

`2Pr(x<y)-1 = Pr(x<d)`.

The no-internal-descent condition gives `Pr(x<d)<1/3`, while `Pr(x<y)>2/3` gives the left side `>1/3`, a contradiction.

Therefore the exact-two terminal branch consists of **exactly one positive lower distinguisher `d` and one positive upper distinguisher `u`**. Since `u<d` is impossible, only two residual geometries remain:

1. `d||u`: Theorem 4.1 gives immediate `>1/6` bias amplification and forbids a second consecutive crossed exact-two expansion.
2. `d<u`: the comparable-fringe corridor branch remains. This is the geometry realized by the lead's sharp 1810-extension adversary, so it cannot be discarded by a local constant.

This is the exact new difficulty reduction delivered by this run.

## 7. Two-sided support escalation

The exact-two endpoint cannot remain a closed four-vertex obstruction in a no-balanced poset.

### Incomparable-fringe case `d||u`

For the fringe pair `(d,x)` oriented `d<x`, the quartet already supplies two distinguishers of opposite sign:

- `y` is positive because `d<y` and `x||y`;
- `u` is negative because `x<u` and `d||u`.

If these were its only two distinguishers, the previous fleet03/B11 two-distinguisher theorem would make `(d,x)` balanced. Hence an extreme `(d,x)` has at least one additional distinguisher outside `{x,y,d,u}`. The order-dual argument gives an additional outside distinguisher for `(y,u)` as well.

### Comparable-fringe case `d<u`

For `(d,x)`, `y` is a distinguisher while `u` is neutral because both `d<u` and `x<u`. The inherited one-distinguisher theorem cited by the partner report says an extreme pair cannot have exactly one distinguisher, so another outside distinguisher is forced. Dually, `(y,u)` has the known distinguisher `x`, while `d` is neutral below both, so another outside distinguisher is forced there too.

Hence both residual geometries export new support to the two outward fringe pairs. The new witnesses may coincide; no distinctness claim is made without further geometry.

## 8. Exact regression and a sharp local failure boundary

The companion standard-library verifier checks 350 exact interval fibers. In every fiber it verifies `n1=n2`, `n4<=n5`, (3.8), and (3.9); 58 fibers satisfy the strict hypotheses of Theorem 4.1 and all satisfy its two conclusions.

It also reconstructs the six-element poset with transitive relation generated by

`0<1, 0<3, 0<4, 0<5, 1<4, 1<5, 2<3, 2<4, 3<4`.

It has exactly 14 linear extensions. For

`(x,y,d,u)=(1,3,2,5)`,

exact counts give

`Pr(x<y)=5/7`,
`Pr(x<d)=2/7`,
`Pr(u<y)=2/7`,
`Pr(d<u)=13/14`.

Thus

`Pr(d<u)-Pr(x<y)-1/6 = 1/21 > 0`.

This example is useful because the endpoint and both fringe pairs are all extreme while the outer pair is even more extreme. It is **not** a POS3 counterexample: `(0,2)` has probability `9/14` and `(4,5)` has probability `5/14`, both balanced. So one amplification step need not itself expose the balanced pair; the theorem's value is the strict nonrepeatable transport.

Verifier terminator:

`POS3_CROSSED_BIAS_AMPLIFICATION_CHECK_PASS`.

Verifier source commit: `b925bc1109a4029b72334a9d72ac7c24f275aa6b`; blob `88b3fa6de3c5a2b0d06b937c9295391d1cd801d6`.

Captured output commit: `76974126f9bb3fdbf1078f79a61ec53f1256e71e`.

## 9. Remaining first obligation

The first unpaid implication is now strictly narrower than the partner's generic lower-distinguisher transport:

> Analyze the **comparable-fringe corridor** `d<u`, or the support-expanded `>=3`-distinguisher/non-crossed branch forced after the one permitted incomparable-fringe amplification. Use the three-chain path/TP2/corridor constraints to force a balanced pair, a strong-majority span descent, a four-antichain contradiction, or a proper autonomous nonchain.

A second consecutive exact-two crossed incomparable-fringe step is no longer a residual. The lead's 1810-extension example shows that the `d<u` corridor is the genuinely sharp local obstruction and must be attacked globally.

No claim of novelty or priority is made. The full POS3 theorem remains open.

## 10. Provenance and scope

Only the source-bound mathematical reports named above and deterministic standard-library finite regressions were used. No benchmark gold or keys, FEI proof material, credentials, scheduler identifiers, machine paths, unrelated private data/transcripts, email, Drive, paid model/API/Codex execution, remote workflow, public posting, permission change, or production-brain mutation was used.
