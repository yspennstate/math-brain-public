# POS3 account03/B19 — exact ideal-state counterexample to two tempting width-three induction shortcuts

**Outcome:** `CANDIDATE_REFUTED` for two stronger proof routes; parent POS3 remains **OPEN / NOT PROVED**.  
**Target:** every finite nonchain poset of width at most three has an incomparable pair whose order probability under the uniform linear-extension law lies in `[1/3,2/3]`.  
**Assigned subproblem:** construct and execute exact ideal-state linear-extension counting for targeted new counterexamples; finite nonviolations alone are not the objective.  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Source-bound collective state consumed

The current owner allocation superseded the old brain-installation / benchmark duties for this slot. I therefore worked on POS3, not on the superseded installation prompt.

The designated partner `account04/B10` had no source-bound collective-POS3 artifact in the authorized mathematical archive at the start snapshot, so I did not wait or fabricate uptake. I consumed two exact other-account results instead:

1. `account02/B11`, `proofnet24/collective-POS3/account02/B11/20260921T235736Z-b11-44e20585/REPORT.md`, blob `b71c5087c4982769946c31f1ec76242bf297fe17`. It proves exact ordinal factorization by incomparability components, so a cardinality-minimal counterexample may be assumed to have connected incomparability graph.
2. `account01/B10`, `proofnet24/collective-POS3/account01/B10/20260921T235306Z-account01-B10/REPORT.md`, blob `3a0d4e63665646adc853bb48192eba0f81629a15`. It gives the exact three-chain ideal-state path encoding and edge-flux formula. Its Corollary 4.1 says that if, for some element `x` and another chain `C_b`, every insertion-slice mass across the incomparability interval is at most `E/3`, then `x` has a balanced incomparable partner in `C_b`. Its suggested next route was to combine connectedness with the heavy-slice normal form and try to force such a light-slice vector or a balanced cumulative cut.

The present run attacks the first of those routes directly with exact integer counting.

## 2. A nine-element width-three test poset

Let `P` have elements `0,...,8` and Hasse covers

```text
0<2, 0<3, 0<4,
1<4,
2<5,
3<6,
4<7, 4<8,
5<8,
6<8.
```

Use the explicit three-chain partition

```text
A = (0<3<6),
B = (1<4<7),
C = (2<5<8).
```

The poset is self-dual under the involution

```text
0<->8, 1<->7, 2<->6, 3<->5, 4<->4,
```

which is useful as an independent symmetry check on the exact counts below.

The companion standard-library verifier constructs the transitive closure, performs exact ideal-state dynamic programming over subsets, checks the width by exact antichain enumeration, checks incomparability-graph connectedness, computes every incomparable-pair numerator exactly, and computes the account01/B10 edge-flux slices by summing `A(I) B(I union {x})` over legal ideals `I` at the relevant chain level.

The verifier proves the following finite certificate:

```text
number of linear extensions E = 420,
width(P) = 3,
Inc(P) is connected,
minimal elements = {0,1},
maximal elements = {7,8}.
```

The script SHA-256 at execution was

`ef5611d96320726f4fd3412c64177a9a8125f21027973e21c961e314719ed6c9`,

and the captured output SHA-256 was

`74139277ae9a53d479bf4ec284f12edec2ad7fd6137a78aebabcff4d5b97bc3c`.

These are finite exact certificates for the two refutations below, not evidence that POS3 itself is solved.

## 3. Refutation A — an extremal-anchor induction is false

A natural strengthening for an induction is:

> **False extremal-anchor claim.** Every connected-incomparability width-at-most-three nonchain has a balanced incomparable pair with at least one endpoint minimal or maximal.

The poset above is an exact counterexample.

For all incomparable pairs touching a minimal or maximal element, the largest balance value is

`43/140 < 1/3`.

The full extremal-endpoint list is:

```text
pair    Pr(first before second)     balance
0,1     5/7                         2/7
1,2     97/140                      43/140
1,3     97/140                      43/140
1,5     32/35                       3/35
1,6     32/35                       3/35
2,7     32/35                       3/35
3,7     32/35                       3/35
5,7     97/140                      43/140
6,7     97/140                      43/140
7,8     5/7                         2/7
```

Nevertheless `P` itself is not a POS3 counterexample: the interior incomparable pairs `(2,3)` and `(5,6)` each have probability exactly `1/2` in either orientation.

**Consequence.** A minimal-counterexample induction cannot in general be closed by proving only that some minimal or maximal element has a balanced partner. Any valid induction must retain genuinely interior incomparable pairs or prove an additional structural reduction that is absent here.

## 4. Refutation B — connectedness does not force a light insertion-slice vector

The account01/B10 exact flux certificate says that for fixed `x` and another chain `C_b`, if every relevant slice has mass at most `E/3`, then one of the cumulative cuts is balanced. It is therefore tempting to try to prove:

> **False light-slice claim.** In every width-three poset with connected incomparability graph, there is some `x` and some other chain containing an element incomparable with `x` for which every edge-flux slice has mass at most `E/3`.

The same nine-element poset refutes this stronger route for the displayed chain partition.

Here `E/3=140`. For **every** ordered pair `(x,C_b)` with `C_b` another chain containing at least one element incomparable with `x`, the maximum exact slice mass is strictly greater than `140`. The smallest such maximum is already

`154 = (11/30) E > E/3`,

attained for the central element `x=4` against each outer chain:

```text
W_{4,A} = (0,133,154,133),
W_{4,C} = (133,154,133,0).
```

The complete exact flux table is preserved in `verify_ideal_counterexample.out`.

Thus connectedness alone cannot guarantee the sufficient hypothesis of the one-chain anti-concentration certificate. More strongly, this example has a `>E/3` heavy slice in every relevant cross-chain insertion distribution and still contains perfectly balanced pairs.

**Consequence.** The mere existence of heavy slices is not the decisive obstruction. A hypothetical POS3 counterexample needs the much stronger **alignment** asserted by the account01/B10 heavy-slice normal form: the unique `>E/3` jump must occur at the strong-majority gap for every relevant element/chain interval, and those gap choices must be globally compatible with one transitive strong-majority order. The next proof step should attack that global alignment, not try to obtain a light slice from connectedness alone.

## 5. Exact ideal-state method used

For every ideal `I` of `P`, let

`A(I)` be the number of ideal paths from the empty ideal to `I`, and

`B(I)` the number of ideal paths from `I` to the full set.

They obey the standard exact recurrences

```text
A(empty)=1,
A(I)=sum_{x maximal in I} A(I-{x}),

B(P)=1,
B(I)=sum_{x minimal in P\I} B(I union {x}).
```

Hence `E=A(P)=B(empty)=420`.

For incomparable `x,y`, the exact numerator `#{L:x before y}` is computed independently by adjoining the relation `x<y`, taking transitive closure, and re-running the same integer dynamic program. This yields every pair probability as an exact rational with denominator `420` before simplification.

For the B10 flux vector of `x` against a fixed chain `C_b`, sum

`A(I) B(I union {x})`

over every ideal `I` for which `x` is currently legal to add, grouped by the number of elements of `C_b` already in `I`. This is exactly the edge-flux definition in the consumed account01/B10 report; no projected/uniformized two-chain law is substituted.

The executable ends with

`POS3_B19_IDEAL_DP_CERTIFICATE_PASS`.

## 6. What this changes in the collective proof chain

Before this run, one concrete suggested route after the heavy-slice normal form was to combine connectedness with three-chain geometry to force at least one insertion distribution whose jumps are all at most `E/3`.

That route is now **refuted at that universal scope**: connected incomparability and width exactly three can coexist with a heavy slice in every relevant insertion distribution.

The surviving sharper conditional chain is:

1. By account02/B11, reduce a minimal counterexample to connected incomparability.
2. By account01/B10, in a true counterexample every relevant chain interval has a unique jump `>E/3`, and that jump is pinned to the strong-majority gap.
3. **Remaining essential implication:** prove that a width-three ideal-state system with connected incomparability cannot realize these heavy jumps **simultaneously at the gaps of one common transitive strong-majority order**, using the at-least-five-majority-block structure or another global compatibility identity.

The finite certificate here shows why step 3 must use the *positions/alignment* of the heavy slices and not only their magnitudes.

A promising exact invariant for the next run is to sum signed flux across consecutive boundaries of the common majority order and exploit conservation of each path's chain-coordinate crossings. Such a sum sees where the heavy slice sits, whereas the refuted maximum-slice criterion loses that information.

## 7. Claim status

- POS3 parent target: **OPEN / NOT PROVED**.
- Exact nine-element ideal-state certificate: **PROVED by finite integer DP with executable readback**.
- Extremal-anchor strengthening: **REFUTED**.
- Universal connectedness-to-light-slice strengthening for the displayed three-chain cover: **REFUTED**.
- Account01/B10 one-chain anti-concentration certificate itself: **NOT refuted**; its hypothesis simply need not occur.
- Account02/B11 connected-incomparability reduction: **NOT refuted** and directly used.
- New residual: global compatibility/alignment of `>E/3` heavy slices with a single transitive strong-majority order.

No novelty or priority claim is made. No benchmark gold, held-out labels, credentials, scheduler identifiers, machine paths, unrelated private data, email, Drive action, paid model/API/Codex call, remote workflow, public posting, or permission change was used.
