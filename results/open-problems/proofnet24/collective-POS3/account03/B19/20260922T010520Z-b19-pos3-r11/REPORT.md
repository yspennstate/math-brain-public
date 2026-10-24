# POS3 account03/B19 — module-prime heavy-slice counterexample to the strengthened induction route

**Run:** `20260922T010520Z-b19-pos3-r11`  
**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Outcome:** `CANDIDATE_REFUTED` for a strengthened proof route; parent POS3 remains **OPEN / NOT PROVED**.  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Current assignment and source-bound state

The latest owner control reassigns account03/B19 from the older brain-installation prompt to POS3 and explicitly stops new installation/benchmark work. The exact B19 assignment is to construct and execute exact ideal-state linear-extension counting for targeted new counterexamples; finite nonviolations alone are not the objective.

The designated partner `account04/B10` still had no archived `proofnet24/collective-POS3/account04/B10/` root at the final pre-write source check, so this run did not fabricate partner uptake. It instead substantively consumed these completed results:

1. `account01/B10`, blob `3a0d4e63665646adc853bb48192eba0f81629a15`: exact three-chain ideal-state path encoding and the heavy-slice normal form. In a true POS3 counterexample, every relevant cross-chain insertion distribution has a `>E/3` slice at the strong-majority gap.
2. `account04/B19`, blob `ce30dae79d698103f026d4d871033238489b1fb1`: uniform restriction to autonomous subsets and the consequence that a cardinality-minimal counterexample has no proper autonomous nonchain.
3. `account03/B11`, blob `5b65cb3c68a668e553dc6465252bc6cb82b68b8d`: exact order-polytope swap-defect identity and the double-blocker certificate for adjacent strong-majority boundaries in a true counterexample.
4. This slot's previous exact witness, blob `106c46c118f9863c6fc7867d2ae536dd0786818e`, which showed that connected incomparability alone neither forces an extremal balanced pair nor a light insertion-slice vector.

The present run tests whether the autonomous-module reduction repairs the second failure.

## 2. The strengthened route tested

A natural next induction shortcut is:

> **False strengthened route.** If a width-at-most-three nonchain has connected incomparability graph, is module-prime (no proper nontrivial autonomous subset), and has no balanced incomparable pair touching a minimal or maximal element, then for some element `x` and some other chain `C_b` containing an element incomparable with `x`, every exact insertion slice has mass at most `E/3`, where `E=e(P)`.

By the account01/B10 anti-concentration certificate, such a light slice vector would force a balanced pair. If true, this would combine the connectedness reduction, the autonomous-module reduction, and an endpoint induction into a direct escape from the hard core.

It is false.

## 3. Exact self-dual 9-element certificate

Let `P*` have elements `0,...,8` and generating relations

```text
0<2, 0<3, 0<4,
1<4, 1<5,
2<5,
3<6, 3<7,
4<7, 4<8,
5<8, 6<8.
```

Use the three-chain partition

```text
A=(0<3<6),   B=(1<4<7),   C=(2<5<8).
```

The involution

```text
0<->8, 1<->7, 2<->6, 3<->5, 4<->4
```

is order-reversing, so the poset is self-dual.

The standard-library verifier computes the transitive closure, exact ideal-state forward/backward path counts, all incomparable-pair numerators, exact width, incomparability connectivity, every proper autonomous subset, and every account01/B10 cross-chain edge-flux vector. It proves:

```text
e(P*) = 349
width(P*) = 3
incomparability graph connected
proper nontrivial autonomous subsets = none
minimal elements = {0,1}
maximal elements = {7,8}
```

Thus `P*` is module-prime in the strongest relevant sense: there is no proper autonomous subset of size at least two at all.

## 4. No extremal balanced pair, but exactly two interior balanced pairs

For every incomparable pair touching a minimal or maximal element, the largest balance numerator is `105`, so

```text
max_extremal_balance = 105/349 < 1/3.
```

The exact endpoint rows `(x,y,#{L:x<y}, min(count,349-count))` are

```text
(0,1,244,105)
(1,2,261,88)
(1,3,247,102)
(1,6,325,24)
(2,7,325,24)
(5,7,247,102)
(6,7,261,88)
(7,8,244,105)
```

Nevertheless `P*` itself is not a POS3 counterexample. Its **only** balanced incomparable pairs are

```text
(2,3): 156/349
(5,6): 156/349,
```

both genuinely interior. Self-duality exchanges these two pairs.

This preserves the previous lesson that a valid induction cannot rely on extremal anchors, now inside a module-prime connected example.

## 5. Module-primality still does not force a light insertion distribution

For each element `x` and each other chain containing at least one element incomparable with `x`, let `W_{x,b}(t)` be the exact edge-flux/insertion-slice vector from account01/B10, computed as

```text
sum_I A(I) B(I union {x})
```

over legal ideals grouped by the number of `C_b` elements already present.

Here `E/3 = 349/3`. Every relevant vector has a slice strictly larger than `E/3`. The smallest possible maximum is already

```text
142/349 > 1/3.
```

The complete vectors are:

```text
x=0 vs B: (244,105,0,0)
x=3 vs B: (102,153,94,0)
x=3 vs C: (193,117,39,0)
x=6 vs B: (24,89,148,88)
x=6 vs C: (66,127,156,0)
x=1 vs A: (105,142,78,24)
x=1 vs C: (261,88,0,0)
x=4 vs A: (0,94,142,113)
x=4 vs C: (113,142,94,0)
x=7 vs A: (0,0,88,261)
x=7 vs C: (24,78,142,105)
x=2 vs A: (0,156,127,66)
x=2 vs B: (88,148,89,24)
x=5 vs A: (0,39,117,193)
x=5 vs B: (0,94,153,102)
x=8 vs B: (0,0,105,244)
```

Therefore connectedness + module-primality + failure of every extremal anchor still do **not** imply the one-chain anti-concentration hypothesis.

## 6. What this changes in the collective proof chain

The autonomous-module theorem remains valid and useful: a cardinality-minimal counterexample has no proper autonomous nonchain. This run shows that the reduction does **not** by itself repair the earlier light-slice route.

The surviving counterexample-specific structure is now more sharply identified:

1. minimal counterexample -> connected incomparability (account02/B11);
2. minimal counterexample -> no proper autonomous nonchain (account04/B19);
3. no balanced pair -> a transitive strong-majority order and `>E/3` heavy slices aligned at its gaps (account01/B10);
4. adjacent strong-majority boundaries -> double-blocker certificates, with endpoint three-antichain witnesses (account03/B11);
5. **remaining essential implication:** rule out the simultaneous global alignment of those heavy slices and double-blocker systems in the connected module-prime width-three core.

The new certificate demonstrates why any proof of step 5 must use genuinely counterexample-specific **alignment/blocker compatibility**, not only connectedness, absence of modules, endpoint structure, or the magnitudes of individual insertion slices.

A productive next exact target is a signed conservation identity across consecutive strong-majority boundaries that couples the account01/B10 flux location with the account03/B11 canonical blocker witnesses. A local or one-boundary inequality is insufficient.

## 7. Verification and scope

Verifier: `verify_module_prime_heavy.py`  
Executed SHA-256: `b31ace9f3b54cbb4cff33e9adcb8ce768b176a70583f8e09e3b263ebb1f7c322`  
Captured output SHA-256: `79f53971708a031c3abb7f15f8701c4978b7833d129e78d2d15d213ad8f15875`  
Terminal marker: `POS3_B19_MODULE_PRIME_HEAVY_CERTIFICATE_PASS`.

The certificate is exact integer arithmetic. The targeted search that found this witness is not an exhaustive classification and is not used as proof of any universal positive statement.

**Claim status**
- exact finite certificate above: **PROVED by deterministic integer DP/checks**;
- strengthened connected+module-prime+no-extremal-balance -> light-slice route: **REFUTED**;
- account04/B19 autonomous-module theorem: **not refuted**;
- account01/B10 heavy-slice theorem for a true counterexample: **not refuted**;
- account03/B11 double-blocker theorem for a true counterexample: **not refuted**;
- parent POS3: **OPEN / NOT PROVED**.

No novelty or priority claim is made. No benchmark gold, credentials, scheduler identifiers, machine paths, unrelated private data, email, Drive, paid model/API/Codex execution, remote workflow, public posting, or permission change was used.
