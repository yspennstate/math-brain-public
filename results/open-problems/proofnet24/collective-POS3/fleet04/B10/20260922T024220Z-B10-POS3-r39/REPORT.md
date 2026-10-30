# POS3 fleet04/B10 — equal-predecessor channel identity and fork escalation

**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair whose ordering probability under the uniform law on all linear extensions lies in `[1/3,2/3]`.  
**Parent status after this report:** **OPEN / NOT PROVED**.  
**Inherited finite frontier:** `n_bal=14` (unchanged).  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

This run continues the exact arbitrary-size width-three target. It does not resume the superseded benchmark or brain-installation work, and it does not replace the target by a finite census or a width-two subclass.

## 1. Exact source-bound state consumed

The newest complete campaign-lead report actually present before this run was

- `proofnet24/collective-POS3/fleet04/B10/20260922T011127Z-fleet04-B10-POS3-r11/REPORT.md`, blob `1e5a9682e4f90f38484a86e7199428de0b0160f8`.

It proves that in a hypothetical width-at-most-three counterexample every element occupies its rank in the common transitive strong-majority order with probability strictly greater than `1/81`, equivalently `81 W_x(g_b(x),g_c(x))>E` in the exact three-chain flux coordinates. The simultaneous one-chain majority-gap marginals remain `>E/3`.

The required named **OTHER-account partner result** consumed and applied is

- **fleet01/B11**, `proofnet24/collective-POS3/fleet01/B11/20260922T021210Z-b11-pos3-exchange-r11/REPORT.md`, blob `5fdf6f70d35fee1011b67c217b9e177fb197e81a`.

For an incomparable endpoint pair `(x,y)` with `Pred(y) subseteq Pred(x)`, that report proves the exact identity

`p_xy = 1 - (Q+R)/(2E)`,

where `Q` is the number of extensions in which `y` precedes every minimal positive successor blocker of `x`, and `R` is the reverse-order nonneutral-blocker remainder. Thus the first endpoint would close if `Q+R>=2E/3`. It also gives a source-valid local example showing that delayed nonautonomy at one endpoint does not by itself force the missing lower bound.

Two further exact compatible inputs are used.

- **fleet03/B11**, `proofnet24/collective-POS3/fleet03/B11/20260922T011439Z-fleet03-B11-pos3-r12/REPORT.md`, blob `3443c6ccc4436b9eaf060884c4eec6fc85dc1792`, proves that at the first strong-majority block boundary `x prec_* y` a hypothetical minimal counterexample has exactly two canonical successor blockers `s_1,s_2`, both Hasse covers of `x`; the blockers are incomparable with each other and with `y`, are nonautonomous, and every element distinguishing them occurs strictly after the whole second majority block.
- **fleet03/B11**, `proofnet24/collective-POS3/fleet03/B11/B11-20260922T021330Z-pos3/REPORT.md`, blob `84167cd7b3a69dc8e4c699fc5ca0e5c9ba5e4a8d`, proves the exact two-gap deletion-fiber formula for an arbitrary incomparable pair and shows that an extreme global pair has a deletion fiber with orientation ratio greater than two. It also proves that the common-neutral set of an incomparable pair is a chain in width three and refutes a fork-plus-earliest-distinguisher local closure.

The inherited I0122 frontier `n_bal=14` is preserved; no finite-frontier movement is claimed.

## 2. Compact conditional end-to-end route

Assume for contradiction that `P` is a cardinality-minimal width-at-most-three POS3 counterexample. The inherited state gives a transitive strong-majority total order `L_*`, width exactly three, connected incomparability graph, no proper autonomous nonchain, and at least five maximal contiguous chain blocks.

At the first block boundary let `x` be the last point of the first block and `y` the first point of the second. The fleet03/B11 endpoint theorem supplies a two-cover Hasse fork

`x lessdot s_1`, `x lessdot s_2`,

with `s_1 || s_2`, `s_i || y`. Since `P` has no balanced pair, after renaming we have

`Pr(s_1 precedes s_2)>2/3`.

The first missing pair-selection/exception implication is what an extreme blocker-sibling pair is forced to do. There are two qualitatively different cases.

1. A lower distinguisher exists, so `Pred(s_1) != Pred(s_2)`. The inherited delayed-distinguisher theorem already turns such a witness into a width-saturating three-antichain branch.
2. No lower distinguisher exists, so `Pred(s_1)=Pred(s_2)`. This was the clean sibling branch left structurally unresolved.

This report pays the second branch. The key is an exact signed channel identity for **every** incomparable equal-predecessor pair. In a no-balanced width-three candidate it forces either a strictly shorter strong-majority-span incomparable pair or a new two-cover Hasse fork beyond the later sibling. Thus a clean extreme sibling pair cannot remain locally featureless.

## 3. Exact equal-predecessor deletion identity

Let `P` be any finite poset and let `a||b` satisfy

`Pred(a)=Pred(b)`.                                               (3.1)

Put `Q=P\{a,b}`. Fix `tau in L(Q)` and number its external gaps `0,1,...,m`, where gap `g` lies after the first `g` letters of `tau`.

For `v in {a,b}`, let its exact admissible insertion interval be

`I_v(tau)=[ell_v(tau),u_v(tau)]`.

Because the strict predecessor sets are equal, the lower endpoints coincide:

`ell_a(tau)=ell_b(tau)=ell`.                                   (3.2)

Write

`r=u_a-ell+1`, `s=u_b-ell+1`.

Let `A_tau` and `B_tau` be the numbers of lifts of `tau` with `a<b` and `b<a`, respectively. Specializing the exact fleet03/B11 two-gap formula to the common-left-endpoint intervals gives

`A_tau-B_tau = min(r,s)(s-r)`,                                 (3.3)

`A_tau+B_tau = min(r,s)(max(r,s)+1)`.                          (3.4)

Hence the conditional signed bias of this deletion fiber is exactly

`(A_tau-B_tau)/(A_tau+B_tau) = (s-r)/(max(r,s)+1)`.             (3.5)

### Proof

If `s>=r`, the common-left nested intervals have lengths `r,s`. Directly counting pairs of insertion gaps, remembering that equal-gap insertion gives one lift of each relative order, gives

`A_tau = rs-r(r-1)/2`,

`B_tau = r(r+1)/2`.

Subtracting and adding yields (3.3)–(3.4). The case `r>=s` is the same argument with `a,b` interchanged. `square`

The point is that the signed defect is no longer an opaque ratio: it is the short interval length times the **difference of the first-successor positions**.

## 4. Canonical positive channels

Suppose in one deletion fiber that `s>r`. Then `u_a<u_b`. Let `z` be the first successor of `a` appearing in `tau`; equivalently `z` is the letter immediately after gap `u_a`.

### Lemma 4.1 — the first-successor letter is a canonical Hasse blocker

The element `z` satisfies

`a<z`, `z||b`,

and is minimal in

`S_a(b)={w:a<w and w||b}`.

Consequently `a lessdot z`.

### Proof

By definition of `u_a`, `z` is a successor of `a`. Since `u_b>u_a`, no successor of `b` has appeared by the position of `z`, so `b<z` is impossible. The alternative `z<b` would give `a<z<b`, contradicting `a||b`; hence `z||b`.

If some `w in S_a(b)` satisfied `w<z`, then `w` is a successor of `a` and must appear in `tau` before `z`, contradicting the choice of `z` as the first such successor. Thus `z` is minimal in `S_a(b)`. Finally, if `a<w<z`, then the same transitivity argument forces `w||b`, so `w in S_a(b)`, contradicting minimality. Hence `a lessdot z`. `square`

For this fiber, the positive defect in (3.3) is

`r(s-r)`.                                                       (4.1)

It has a literal lift interpretation: choose any of the `r` admissible gaps for `a` and any of the `s-r` extra gaps of `b` strictly beyond `u_a`. Every such lift has

`a < z < b`

in the linear-extension order. Assign this entire quantity to the blocker `z`.

Define `C_{a->b}(z)` to be the sum of `r(s-r)` over all deletion words whose first positive blocker is `z`. Define dually `C_{b->a}(w)` from fibers with `r>s`. Then summing (3.3) gives the exact signed channel identity

`N(a<b)-N(b<a)`
` = sum_z C_{a->b}(z) - sum_w C_{b->a}(w)`.                    (4.2)

Every positive channel counted by `C_{a->b}(z)` is a genuine subset of the event `a<z<b`; there is no induced-law substitution.

The positive blockers are exactly the minimal elements of `S_a(b)`. They form an antichain and are all incomparable with `b`. Therefore, if `width(P)<=3`,

`|Min S_a(b)| <= 2`.                                           (4.3)

This recovers the width-three two-channel geometry directly from the exact deletion fibers.

### Relation to the partner endpoint identity

Under the stronger hypothesis `Pred(a)=Pred(b)`, the fleet01/B11 endpoint quantities become transparent in the channel language. If `M=Min S_a(b)` and

`Q=#{L:b precedes every z in M}`, then

the complement of the `Q` event is exactly the union of the positive first-blocker channels, so

`E-Q = sum_z C_{a->b}(z)`.                                     (4.4)

The reverse nonneutral remainder is the dual negative-channel total,

`R = sum_w C_{b->a}(w)`.                                       (4.5)

Thus (4.2) is the fiberwise refinement of the partner identity

`N(a<b)-N(b<a)=E-Q-R`.

This is the substantive use of the named partner result: its endpoint remainder is now decomposed into exact first-successor channels in the equal-predecessor sibling branch.

## 5. Width-three span-descent / fork-escalation theorem

Now assume `P` has width at most three, has no balanced incomparable pair, and let `L_*` be its transitive strong-majority order. Let `a||b` satisfy

`Pred(a)=Pred(b)`, `a prec_* b`.

Then `Pr(a<b)>2/3`.

### Theorem 5.1 — clean extreme siblings must descend or fork again

Exactly one of the following structural alternatives is available.

**Span descent.** There exists a canonical positive Hasse blocker `z in Min S_a(b)` with

`a prec_* z prec_* b`.

Then `z||b`, so `(z,b)` is another extreme incomparable pair and its `L_*` span is strictly shorter than that of `(a,b)`.

**Fork escalation.** Every canonical positive blocker lies after `b` in `L_*`. Then there are exactly two such blockers, say `z_1,z_2`, both Hasse covers of `a`, and

`{b,z_1,z_2}`

is a three-element antichain. Moreover

`sum_i C_{a->b}(z_i) > E/3`,                                  (5.1)

and for at least one `i`,

`C_{a->b}(z_i) > E/6`.                                        (5.2)

### Proof

Because `Pr(a<b)>2/3`,

`N(a<b)-N(b<a)>E/3`.

By (4.2), the total positive channel mass is therefore strictly greater than `E/3`.

If some positive blocker `z` precedes `b` in `L_*`, then `a<z` in the poset implies `a prec_* z`; since `z||b`, this is the span-descent alternative.

Otherwise every positive blocker lies after `b` in `L_*`. Since every such `z` is incomparable with `b` and the poset has no balanced pair,

`Pr(b<z)>2/3`,

so

`#{L:z<b}<E/3`.

But every lift counted by the `z` channel has `z<b`, hence

`C_{a->b}(z)<E/3`.                                             (5.3)

One positive blocker cannot carry the total `>E/3` mass. Thus there are at least two. Width three gives at most two by (4.3), so there are exactly two. Both are Hasse covers by Lemma 4.1. Pigeonhole applied to (5.1) gives (5.2). `square`

This is an arbitrary-size pair-selection/exception implication. It is not a finite certificate and does not assume a uniform law after deletion.

## 6. Application to the first Hasse fork

Return to the first strong-majority boundary `x prec_* y` and its inherited blockers `s_1,s_2`.

Because every distinguisher of the blocker pair occurs after the entire second majority block, a difference between `Pred(s_1)` and `Pred(s_2)` is already a delayed **lower-distinguisher branch**. In particular, if no lower distinguisher exists then

`Pred(s_1)=Pred(s_2)`.                                         (6.1)

Rename so that `s_1 prec_* s_2`. Theorem 5.1 applies with `a=s_1,b=s_2`.

Therefore the previously clean sibling branch now has a forced dichotomy:

1. **strict span descent:** a Hasse successor `z` of `s_1` lies before `s_2` in `L_*` and is incomparable with `s_2`; or
2. **second fork:** `s_1` has two Hasse-successor blockers `z_1,z_2` lying after `s_2`, with a channel carrying more than `E/6` extensions.

The second case has an additional width-three bridge back to the original boundary. At the first boundary, `y` is incomparable with `s_1,s_2`; because `x prec_* y` are adjacent and `x<s_i`, both siblings lie after `y` in `L_*`. In the fork-escalation case the new blockers lie still later. Since `{s_2,z_1,z_2}` is already a three-antichain, `y` cannot be incomparable with both `z_1,z_2`, or width would be at least four. Hence for at least one `i`, `y` is comparable with `z_i`; because `L_*` extends the poset and `y prec_* z_i`, necessarily

`y<z_i`.                                                       (6.2)

Thus a clean first-fork sibling pair either yields a shorter extreme pair or forces a second two-cover fork together with a genuine poset relation from the original endpoint `y` into the new fork. This is precisely the kind of nonlocal propagation that the fleet01/B11 and fleet03/B11 local counterexamples showed was missing.

## 7. What is paid and what remains unpaid

**Paid in this run.** The first missing exception implication for the no-lower-distinguisher sibling branch is now exact. Equal-predecessor extreme pairs admit a signed deletion-fiber channel decomposition, and in width three a no-balanced candidate cannot support such a pair without either strict strong-majority span descent or another two-cover Hasse fork. The second fork has a quantitative channel `>E/6`, and in the inherited first-boundary setting at least one new blocker is forced above the original endpoint `y` in the poset.

**Still unpaid.** This does not yet prove that iterating span descent / fork escalation terminates in a balanced pair or an autonomous nonchain. The lower-distinguisher branch also remains. The next global obligation is to couple the two branches with the existing cumulative three-chain heavy-slice constraints and the delayed-distinguisher span: prove that repeated escalation cannot continue through all majority blocks without creating either

- a balanced pair,
- a four-element antichain,
- a proper autonomous nonchain, or
- a violation of the `>E/3` heavy-slice / `>E/81` central-cell conditions.

No unsupported finite-kernel or compactness reduction is substituted for this obligation. POS3 remains open.

## 8. Exact verification

A deterministic standard-library checker is archived as

`verify_equal_predecessor_channel.py`, Git blob `ef91a9ed51b2d6291f6c2bb49db48af613f71fa7`.

The captured output is

`verify_equal_predecessor_channel.out`, Git blob `5ecc2c075448d0b3dd228b01bdeca376716bc4d5`.

The verifier enumerates every transitively closed relation contained in the natural order on `n<=6`; every finite `n`-element poset has an isomorphic topologically labelled representative in this family. It retains only width-at-most-three cases and checks every ordered incomparable equal-predecessor pair. It verifies the common lower insertion endpoint, formulas (3.3)–(3.4), exact global channel identity (4.2), canonical-blocker membership, Hasse-cover property, the width-three two-blocker bound, and the quantitative fork-escalation conclusions whenever `Pr(a<b)>2/3` and every positive blocker is strongly after `b`.

Captured output:

```text
POS3_EQUAL_PREDECESSOR_CHANNEL_CHECK_PASS
n=2 closures=2 width_le_3=2 equal_pred_pairs=2 p_gt_2_3=0 fork_escalation=0
n=3 closures=7 width_le_3=7 equal_pred_pairs=16 p_gt_2_3=0 fork_escalation=0
n=4 closures=40 width_le_3=39 equal_pred_pairs=134 p_gt_2_3=8 fork_escalation=0
n=5 closures=357 width_le_3=314 equal_pred_pairs=1334 p_gt_2_3=144 fork_escalation=10
n=6 closures=4824 width_le_3=3339 equal_pred_pairs=15914 p_gt_2_3=1985 fork_escalation=218
TOTAL closures=5230 width_le_3=3701 equal_pred_pairs=17400 p_gt_2_3=2137 fork_escalation=228
```

The symbolic proofs above are the mathematical justification; the finite execution is regression evidence only and is not used as arbitrary-size closure.

## 9. Status and provenance

- Equal-predecessor common-left insertion reduction: **PROVED**.
- Exact signed channel identity: **PROVED**.
- Canonical first-successor blockers are Hasse covers: **PROVED**.
- Width-three span-descent / fork-escalation theorem: **PROVED**, conditional only on the stated no-balanced strong-majority setting.
- First-fork clean-sibling application and forced relation (6.2): **PROVED**, conditional on the inherited first-boundary Hasse-fork theorem.
- Parent width-three `1/3–2/3` conjecture: **OPEN / NOT PROVED**.
- Inherited finite frontier: `n_bal=14`, unchanged.

No novelty or priority claim is made. No benchmark gold or keys, credentials, scheduler identifiers, machine paths, unrelated private data/transcripts, email, Drive, paid model/API/Codex execution, remote workflow, public posting, permission change, or production-brain mutation was used.
