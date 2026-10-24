# POS3 account04/B19 — autonomous-module reduction in a minimal counterexample

**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** for every finite nonchain poset of width at most three, some incomparable pair has ordering probability in `[1/3,2/3]` under the uniform law on linear extensions.  
**Parent status after this report:** **OPEN / NOT PROVED**.  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`.

This run follows the owner-directed `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z` programme. The older B19 brain-installation assignment was superseded by the later research-only control. No new brain-installation or benchmark work was performed.

## 1. Exact peer state consumed

The assigned integration step is to combine the other-account path, coupling, and structural reductions into an arbitrary-size induction and resolve the first uncovered case. I used the following exact peer results.

1. **account01/B10**, report commit `e72e4c5649ca5fa7e865d163e2e58d0c99b771d2`, report blob `3a0d4e63665646adc853bb48192eba0f81629a15`. For a fixed three-chain cover it gives the exact ideal-state path encoding of uniform linear extensions, exact cross-chain edge fluxes `W_{x,b}(t)`, and the heavy-slice normal form: in a counterexample, whenever `x` is incomparable with some element of chain `C_b`, the strong-majority insertion gap `g_b(x)` satisfies
   \[
   \sum_{t<g_b(x)}W_{x,b}(t)<E/3,\qquad
   \sum_{t\le g_b(x)}W_{x,b}(t)>2E/3,
   \]
   hence `W_{x,b}(g_b(x))>E/3`, where `E=e(P)`.

2. **account02/B11**, report blob `b71c5087c4982769946c31f1ec76242bf297fe17` plus integration addendum blob `cff32b77ee25194c25566e92e1836278ce820e64`. Exact ordinal factorization shows a cardinality-minimal counterexample may be assumed to have connected incomparability graph. The addendum also combines width-two balance with the chain-deletion weights and records the exact covariance obstruction for each deleted chain.

3. **account01/B19**, report commit `61e199cb10e0ef8a5ea86f03b0a1404b0c6f632e`, report blob `2c2a46da29d5b4114b5a7f71e6b0072d27b9c437`. For a deleted chain `C`, restriction of a uniform extension of `P` to `Q=P\C` has exact density proportional to the insertion multiplicity `W_C(tau)`. This is generally nonuniform; the corridor recurrence and its forward/backward counts retain the bias exactly.

4. **account03/B19**, handoff blob `20106d1d956c7b5428ea0dd32df8690fe34f44bc`. A 9-element exact certificate refutes two stronger shortcuts: connected incomparability does not force a balanced pair with a minimal/maximal endpoint, and it does not by itself force a relevant insertion-slice maximum at most `E/3`.

The surviving induction core therefore cannot discard the third-chain multiplicity and cannot rely on connectedness alone.

## 2. New structural theorem: autonomous subsets inherit the uniform extension law

Call `M` an **autonomous subset** of a finite poset `P` if for every `z in P\M`, exactly one of the following holds:

- `z < m` for every `m in M`;
- `m < z` for every `m in M`;
- `z` is incomparable with every `m in M`.

This is the standard module-type condition needed below; no assertion is made about terminology outside this report.

### Theorem 2.1 — uniform restriction to an autonomous subset

Let `P` be a finite poset and `M` an autonomous subset. If `L` is uniformly distributed on the linear extensions of `P`, then the restriction `L|_M` is uniformly distributed on the linear extensions of the induced subposet `P[M]`.

Equivalently, for every `sigma,sigma' in L(P[M])`,
\[
\#\{L\in L(P):L|_M=\sigma\}
=
\#\{L\in L(P):L|_M=\sigma'\}.
\]

### Proof

Fix `sigma,sigma' in L(P[M])`. Consider any full extension `L` of `P` whose restriction to `M` is `sigma`.

Keep fixed:

- the set of positions occupied by elements of `M`;
- every element of `P\M` in its original position and hence the complete external order.

Replace only the sequence of `M`-elements occupying those positions, changing it from `sigma` to `sigma'`.

Relations internal to `M` remain valid because `sigma'` is a linear extension of `P[M]`. Now fix an external element `z`.

If `z<m` for every `m in M`, then in every linear extension of `P`, `z` lies before **all** positions occupied by `M`. Reordering the labels inside those positions cannot violate any relation involving `z`.

If `m<z` for every `m in M`, the same argument applies with `z` after all `M`-positions.

If `z` is incomparable with every `m in M`, there is no order constraint between `z` and any label placed in an `M`-position.

Thus the replacement produces a valid linear extension of `P` restricting to `sigma'`. Replacing `sigma'` by `sigma` is the inverse map, so this is a bijection between the two fibers. All fibers therefore have equal size, which proves uniformity. ∎

No width assumption is used in Theorem 2.1.

## 3. Minimal-counterexample consequence for POS3

### Corollary 3.1 — a minimal POS3 counterexample has no proper autonomous nonchain

Assume the width-at-most-three target is false and choose a counterexample `P` of minimum cardinality. Then every proper autonomous subset `M` of `P` induces a chain.

### Proof

Suppose instead that a proper autonomous `M` induces a nonchain. Since `P` has width at most three, so does `P[M]`, and `|M|<|P|`. By minimality of `P`, the POS3 conclusion holds for `P[M]`. Hence there are incomparable `x,y in M` such that
\[
1/3\le \Pr_{\sigma\sim U(L(P[M]))}(x<_{\sigma}y)\le 2/3.
\]

By Theorem 2.1 the restriction to `M` of a uniform random extension of `P` is exactly uniform on `L(P[M])`. Therefore
\[
\Pr_{L\sim U(L(P))}(x<_L y)
=
\Pr_{\sigma\sim U(L(P[M]))}(x<_{\sigma}y),
\]
so the same pair is balanced in `P`, contradicting that `P` is a counterexample. ∎

### Immediate special case

A proper pair of incomparable elements that is autonomous is already balanced with probability exactly `1/2`, since the induced two-element antichain has two linear extensions and Theorem 2.1 makes them equiprobable in the ambient poset.

## 4. How this integrates the existing induction

Before this run, the collective minimal-counterexample core had the following exact surviving constraints:

- width exactly three;
- the inherited finite frontier excludes the already-checked small orders;
- connected incomparability graph by account02/B11;
- at least five maximal contiguous chain blocks in the inherited strong-majority order;
- every relevant cross-chain interval has the account01/B10 heavy slice `>E/3` at its strong-majority gap;
- chain deletion/projection must retain account01/B19's nonuniform insertion weights;
- connectedness alone does not force an easy endpoint pair or an `<=E/3` slice, by account03/B19.

Corollary 3.1 adds a genuine arbitrary-size structural reduction:

> **Every proper autonomous subset of a cardinality-minimal counterexample is a chain.**

So a decomposable induction can now eliminate **all proper nonchain autonomous modules**, not merely ordinal-sum factors. The only module-type decompositions that survive are chain modules. Those are exactly the case in which the account01/B19 chain-insertion corridor is the correct state variable rather than a uniform smaller-poset law.

This resolves one previously uncovered induction branch without weakening the parent target.

## 5. Regression check

The companion standard-library script `verify_autonomous_module.py` has Git blob `ea7870828446235bd65ff097f2c17614164d76ba`. Its output has Git blob `819f8c97f271350b66e927dea1704421efa78764` and ends with

`POS3_AUTONOMOUS_MODULE_CHECK_PASS`.

It enumerates linear extensions in four small posets with autonomous modules having respectively 2, 2, 6, and 3 internal linear extensions. In every example the number of ambient lifts is identical for every internal extension. These finite checks are regression evidence only; Theorem 2.1 is proved by the explicit fiber bijection.

## 6. Remaining obligation

The parent problem is still open. The exact next obstruction is now narrower:

> In a cardinality-minimal width-three counterexample with connected incomparability graph and no proper autonomous nonchain, rule out the simultaneous account01/B10 `>E/3` heavy slices. Equivalently, handle the surviving **chain-module / corridor-weight** regime rather than trying to make a deleted-chain law uniform.

A particularly direct next step is to take a maximal proper autonomous chain when one exists and combine its uniform external relation pattern with account01/B19's insertion-corridor recurrence. One must prove that the resulting special weights cannot push every width-two balanced pair of the contracted/remainder structure past both balance endpoints, or else force a balanced pair involving the chain itself. If no proper autonomous subset at all remains, the residual is the module-prime connected heavy-slice core and the signed-flux alignment mechanism suggested by account03/B19 becomes the natural next attack.

## 7. Claim status and scope

- Uniform restriction to an autonomous subset: **PROVED** by an explicit bijection.
- No proper autonomous nonchain in a cardinality-minimal POS3 counterexample: **PROVED**, conditional only on choosing a minimal counterexample.
- Incomparable autonomous twin pair is balanced with probability `1/2`: **PROVED**.
- Width-three `1/3–2/3` parent target: **NOT PROVED**.
- Outcome: `ESSENTIAL_STEP_APPLIED`.

No novelty or priority claim is made. No benchmark gold, credentials, scheduler identifiers, machine paths, unrelated private data, email, Drive, paid model/API execution, remote workflow, public release, or production brain mutation was used.
