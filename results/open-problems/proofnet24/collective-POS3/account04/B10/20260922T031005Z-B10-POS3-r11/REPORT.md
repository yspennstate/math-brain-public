# POS3 account04/B10 — delayed-predecessor funnel and sibling-corridor continuation

**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair whose ordering probability under the uniform law on all linear extensions lies in `[1/3,2/3]`.  
**Parent status after this report:** **OPEN / NOT PROVED**.  
**Inherited finite frontier:** `n_bal=14` (unchanged).  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

This run continues the exact arbitrary-size width-three target under `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`. It performs no new benchmark or brain-installation work and makes no novelty claim.

## 1. Source-bound state consumed

The source target and frozen I0122 frontier are from `operations/claims/I0122.md` at scientific snapshot `2d9669d532d826d4d41aa23b710a19b4566618b0`: the universal 1/3–2/3 conjecture is distinct from the finite frontier `n_bal=14`, which remains partial.

The immediate lead predecessor is

- account04/B10, `proofnet24/collective-POS3/account04/B10/20260922T024220Z-B10-POS3-r39/REPORT.md`, blob `c1b4721b079ea67e9176948c7f5ea4cc179c79f3`.

That report proved the equal-predecessor deletion-channel identity. In a hypothetical no-balanced width-three candidate, an incomparable equal-predecessor pair oriented `a prec_* b` either has a canonical Hasse blocker strictly between it in the strong-majority order, giving strict span descent, or has exactly two positive Hasse blockers after `b`, total positive channel mass `>E/3`, with one channel `>E/6`. Applied to the first-boundary sibling fork this paid the clean `Pred(s_1)=Pred(s_2)` branch but left the lower-distinguisher branch open.

The required named **OTHER-account partner result** applied here is

- account01/B11, `proofnet24/collective-POS3/account01/B11/20260922T021210Z-b11-pos3-exchange-r11/REPORT.md`, blob `5fdf6f70d35fee1011b67c217b9e177fb197e81a`.

For any incomparable `(a,b)` with `Pred(b) subseteq Pred(a)`, it proves the exact endpoint identity

`p_ab = 1 - (Q+R)/(2E)`,

with `Q` the number of extensions in which `b` precedes every minimal successor blocker of `a`, and `R` the reverse-order nonneutral-blocker remainder. It also proves `2I=Q-R`, hence `Q>=R`.

Two further exact completed inputs are used.

- account03/B11, `proofnet24/collective-POS3/account03/B11/20260922T011439Z-account03-B11-pos3-r12/REPORT.md`, blob `3443c6ccc4436b9eaf060884c4eec6fc85dc1792`: at the first strong-majority block boundary `x prec_* y`, a cardinality-minimal hypothetical counterexample has exactly two successor Hasse blockers `s_1,s_2`, with `x lessdot s_i`, and `{y,s_1,s_2}` an antichain. Every element distinguishing `s_1` from `s_2` occurs strictly after the whole second majority block `B_2`.
- account02/B10, source report `proofnet24/collective-POS3/account02/B10/B10-20260922T024630Z-pos3-r13/REPORT.md`, handoff `account02-B10-20260922T0301Z-one-distinguisher-balance.md`: any incomparable pair with exactly one relation-distinguisher is balanced. Therefore every incomparable pair in a hypothetical POS3 counterexample has at least two distinct distinguishers.

## 2. Compact conditional end-to-end route

Assume for contradiction that `P` is a cardinality-minimal width-at-most-three counterexample. Use the inherited transitive strong-majority total order `L_*`, which extends the poset. At the first chain-block boundary let `x` be the last point of `B_1` and `y` the first point of `B_2`. The inherited first-boundary theorem gives

`x lessdot s_1`, `x lessdot s_2`,

with `s_1 || s_2`, `y || s_1`, `y || s_2`, and every distinguisher of the sibling pair strictly after `B_2`.

The predecessor report handled the special case `Pred(s_1)=Pred(s_2)`. The first missing exception implication is whether lower distinguishers can occur on both sides of the sibling pair, which would prevent applying the account01/B11 endpoint theorem with a fixed inclusion direction.

This run proves they cannot. In fact the two full predecessor sets are always nested, the proper predecessor difference is a chain whose top is a new Hasse predecessor, and the account01/B11 exact endpoint identity then forces the strict branch either to **descend to a shorter extreme incomparable pair or to continue through a new canonical successor Hasse blocker**. When the sibling with the larger predecessor set is majority-early, absence of span descent forces exactly two new successor Hasse blockers.

## 3. Delayed-predecessor funnel

### Theorem 3.1 — first-fork sibling predecessor sets are nested

Let `P` have width at most three and let `L_*` be a linear extension of `P`. Suppose `x,y,s_1,s_2` satisfy

1. `x prec_* y`;
2. `x lessdot s_1` and `x lessdot s_2`;
3. `x || y`, `s_1 || s_2`, and `y || s_i` for `i=1,2`;
4. every element distinguishing the poset relations of `s_1,s_2` occurs after `y` in `L_*`.

Then

`Pred(s_1) subseteq Pred(s_2)` or `Pred(s_2) subseteq Pred(s_1)`.

Moreover, whichever proper difference is nonempty is a chain.

The actual first-boundary state satisfies the stronger version of hypothesis 4: every distinguisher occurs after the whole block `B_2`.

### Proof

Take

`d in Pred(s_1) \ Pred(s_2)`.

Then `d<s_1`. Also `d||s_2`: `d<s_2` would put `d` in `Pred(s_2)`, while `s_2<d<s_1` would contradict `s_1||s_2`.

Because `d` distinguishes the siblings, hypothesis 4 puts `d` after `y`, hence after `x`, in `L_*`.

We claim

`d||x` and `d||y`.                                             (3.1)

The relation `d<x` is impossible because `L_*` extends `P` and places `x` before `d`. The relation `x<d` would give `x<d<s_1`, contradicting the Hasse cover `x lessdot s_1`. Thus `d||x`.

Likewise `d<y` is impossible from the `L_*` order. If `y<d`, then `y<d<s_1`, contradicting `y||s_1`. Hence `d||y`. This proves (3.1).

The same reasoning applies to every element of either proper predecessor difference.

Now suppose for contradiction that both differences are nonempty. Choose

`d in Pred(s_1) \ Pred(s_2)`,
`e in Pred(s_2) \ Pred(s_1)`.

By (3.1), both `d,e` are incomparable with both `x,y`. They are also incomparable with one another: if `d<e`, then `e<s_2` gives `d<s_2`, contradiction; if `e<d`, then `d<s_1` gives `e<s_1`, contradiction. Therefore `{x,y,d,e}` is a four-element antichain, contradicting `width(P)<=3`. So at most one proper difference is nonempty, proving the predecessor-set inclusion.

Finally suppose, after relabelling, that

`D=Pred(s_1) \ Pred(s_2)`

is nonempty. For distinct `d,e in D`, both are incomparable with `x,y`. If `d||e`, then again `{x,y,d,e}` is a four-antichain. Hence every two elements of `D` are comparable, so `D` is a chain. `square`

### Theorem 3.2 — the strict branch creates an incoming Hasse fork

Relabel the siblings as `a,b` so that

`Pred(b) subsetneq Pred(a)`,

and put

`D=Pred(a) \ Pred(b)`.

Let `d=max D`, which exists and is unique because Theorem 3.1 makes `D` a finite chain. Then

`d lessdot a`.                                                 (3.2)

Moreover

`d||x`, `d||y`, `d||b`,

so `{x,y,d}` is a three-antichain and `a` has the two incomparable lower Hasse neighbours `x,d`.

### Proof

We already proved `d||x,y,b`; only the cover assertion is new. Suppose `d<c<a`. If `c<b`, then `d<c<b`, contradicting `d||b`. If `b<c`, then `b<c<a`, contradicting `a||b`. If `c||b`, then `c in Pred(a)\Pred(b)=D` and `d<c`, contradicting maximality of `d`. These exhaust the possibilities, so no such `c` exists and `d lessdot a`. `square`

Thus every strict lower-distinguisher branch has a concrete Hasse bow-tie

`d lessdot a greaterdot x lessdot b`,

with `d||x`, `d||b`, `a||b`, and with `y` incomparable with `x,d,a,b` wherever stated above.

### Dual endpoint

Order-duality gives the corresponding statement at the last strong-majority block boundary: the two predecessor-Hasse siblings there have nested successor sets, the proper successor difference is a chain, and its bottom element is a Hasse successor of the sibling carrying the larger successor set.

## 4. Exact account01/B11 endpoint reduction

Relabel the first-boundary siblings as `a,b` so that

`Pred(b) subseteq Pred(a)`.                                    (4.1)

Theorem 3.1 proves that this relabelling is always possible. Therefore the account01/B11 endpoint theorem applies without any equal-predecessor assumption.

Let

`M_a(b) = Min{z : a<z and z||b}`,
`Q = #{L : b precedes every m in M_a(b)}`,

and let `R` be the number of reverse extensions `b ... a` whose open interval contains a nonneutral endpoint blocker. With `E=e(P)`, the partner theorem gives

`p_ab = 1-(Q+R)/(2E)`,                                       (4.2)
`2I=Q-R`, hence `Q>=R`.                                       (4.3)

Since `P` has no balanced pair, exactly one of the following holds.

### Majority-early larger-predecessor sibling

If `a prec_* b`, then `p_ab>2/3`, so

`Q+R < 2E/3`,                                                  (4.4)

and in particular `Q<2E/3`. Thus `M_a(b)` cannot be empty: if it were empty, the event defining `Q` would be vacuous and `Q=E`.

### Majority-late larger-predecessor sibling

If `b prec_* a`, then `p_ab<1/3`, so

`Q+R > 4E/3`.                                                  (4.5)

Using `R<=Q` from (4.3),

`Q>2E/3`.                                                      (4.6)

Hence, whenever `M_a(b)` is nonempty, each `m in M_a(b)` satisfies

`Pr(b precedes m) >= Q/E > 2/3`.                              (4.7)

The predecessor-inclusion direction therefore has an exact probabilistic polarity: the same endpoint statistic is forced below `2E/3` or above `4E/3` according to the sibling majority orientation.

## 5. Nested-corridor continuation theorem

The preceding ingredients pay more than predecessor nesting: the strict branch itself cannot terminate without either span descent or a new outgoing Hasse obstruction.

For incomparable `u,v`, define their `L_*` span as the number of elements strictly between them in the strong-majority total order.

### Theorem 5.1 — strict nested siblings descend or open a successor corridor

Assume the strict branch `Pred(b) subsetneq Pred(a)` and let `d=max(Pred(a)\Pred(b))` as in Theorem 3.2.

**Case A: `a prec_* b`.** Either there is a strictly shorter extreme incomparable pair inside the `L_*` interval from `a` to `b`, or `M_a(b)` consists of exactly two elements. In the latter case both are Hasse successors of `a`, both are incomparable with `b`, and together with `b` they form a three-antichain.

**Case B: `b prec_* a`.** Either `(b,d)` is a strictly shorter extreme incomparable pair, or there exists at least one minimal successor blocker

`u in Min{z:b<z and z||a}`.

Such a `u` is a Hasse successor of `b`. If the branch has no span descent at all, every such minimal blocker lies after `a` in `L_*`.

### Proof of Case A

By (4.4), `Q<2E/3`, so `M_a(b)` is nonempty. Suppose first that it is a singleton `{m}`. Then

`Q/E = Pr(b<m) < 2/3`.

Because `b||m` and the poset has no balanced pair, actually

`Pr(b<m)<1/3`.

Thus `m prec_* b`. Since `a<m` in the poset, `a prec_* m`, and hence

`a prec_* m prec_* b`.

The pair `m||b` is therefore a strictly shorter extreme incomparable pair. Consequently, if no span descent occurs, `|M_a(b)|>=2`.

On the other hand the elements of `M_a(b)` are an antichain, each incomparable with `b`; width at most three gives `|M_a(b)|<=2`. Hence no descent forces exactly two blockers. Minimality in the successor set gives `a lessdot m` for each blocker by the standard Hasse-blocker compression argument. `square`

### Proof of Case B

If `b prec_* d`, then `d<a` gives

`b prec_* d prec_* a`,

and `b||d`, so `(b,d)` is a strictly shorter extreme incomparable pair.

Assume instead there is no such descent. Since `d||b` and every incomparable pair is strongly oriented, we must have `d prec_* b`; therefore

`Pr(b<d)<1/3`.                                                 (5.1)

The account01/B11 structural description of `R` says that, in a reverse extension `b ... a`, a nonneutral element between the endpoints is either

- a predecessor of `a` incomparable with `b`, or
- a successor of `b` incomparable with `a`.

The first class is exactly the chain `D=Pred(a)\Pred(b)`. Because `d=max D` and every member of `D` precedes `a`, a reverse extension contains **some** `D`-element between `b,a` if and only if `b<d`. Thus, if there were no successor blocker of `b` incomparable with `a`, we would have the exact identity

`R/E = Pr(b<d) < 1/3`.                                        (5.2)

But `p_ab<1/3` and (4.2) imply `Q+R>4E/3`; since always `Q<=E`, this forces

`R>E/3`,                                                       (5.3)

contradicting (5.2). Therefore `{z:b<z and z||a}` is nonempty. Any minimal element `u` of this set satisfies `b lessdot u` by Hasse-blocker compression.

Finally, if such a `u` lay strictly between `b` and `a` in `L_*`, then `u||a` would itself give a shorter extreme pair. Hence in the no-descent subbranch every minimal successor blocker lies after `a`. `square`

### Interpretation

The strict lower-distinguisher branch has therefore been converted into an actual continuation mechanism:

- an incoming two-cover Hasse fork at `a` from `x,d`;
- then either strict span descent;
- or a new outgoing canonical Hasse blocker;
- and in the `a prec_* b` orientation, no descent forces a full **two-blocker successor fork**.

This is the first missing pair-selection/exception implication requested by the lead assignment. It does not yet prove that iteration must terminate in a contradiction.

## 6. Combining with the one-distinguisher theorem

Let `D=Pred(a)\Pred(b)` after (4.1). The account02/B10 one-distinguisher theorem gives an exhaustive refinement.

- If `D=empty`, every relation-distinguisher of `a,b` is a successor distinguisher, and there are at least two. This is the clean equal-predecessor branch to which the previous B10 channel theorem applies.
- If `|D|=1`, at least one successor distinguisher is also forced; otherwise the sibling pair would have exactly one distinguisher and would already be balanced.
- If there is no successor distinguisher, then `|D|>=2`; all lower distinguishers lie in the same delayed chain `D`.

The Hasse bow-tie also creates further forced witness obligations. For the strict branch, `x||d` has the known distinguisher `b` (`x<b`, `d||b`); `y||d` has the known distinguisher `a`; and `y||b` has the known distinguisher `x`. Since no incomparable pair may have exactly one distinguisher, each of these three pairs has at least one additional relation-distinguisher. These additional witnesses need not be distinct, so this observation is not counted as a contradiction.

## 7. A stronger shortcut is false

Predecessor nesting alone does **not** make the sibling pair balanced. For example, take the six-element width-two poset with elements

`x,d_1,d_2,d_3,a,b`

and relations

`x<a`, `x<b`, `d_1<d_2<d_3<a`,

with no further cross-relations. Then `x lessdot a`, `x lessdot b`,

`Pred(b)={x} subset Pred(a)={x,d_1,d_2,d_3}`,

and the proper difference is a chain. There are exactly `14` linear extensions and exactly `4` have `a` before `b`, so

`Pr(a<b)=4/14=2/7<1/3`.

The poset is not a POS3 counterexample: it has other balanced pairs. This example only rules out the invalid local shortcut “nested predecessors imply the sibling pair itself is balanced.” The global endpoint statistic and subsequent boundary constraints remain essential.

## 8. Finite regression of the structural theorem

The v2 standard-library verifier in this run folder enumerates every transitively closed relation compatible with a chosen ambient linear extension through six labelled elements. Any finite poset together with a chosen linear extension can be relabelled in this form.

For each width-at-most-three closure it scans adjacent incomparable `x,y`, incomparable Hasse successors `a,b` of `x` both incomparable with `y`, and the delayed-predecessor condition that every predecessor distinguisher occurs after `y`. It asserts:

1. nested predecessor sets;
2. a chain proper difference; and
3. when the difference is strict, its unique top element is a Hasse predecessor of the sibling carrying the larger predecessor set.

Exact recorded output:

```text
POS3_PREDECESSOR_FUNNEL_V2_REGRESSION_PASS
unique_transitive_closures 5230
width_le_3 3701
delayed_two_cover_forks 456
strict_predecessor_difference_cases 110
```

This is regression evidence only. The arbitrary-size results are the proofs above.

## 9. What is paid and what remains unpaid

**Paid in this run.** The previously open lower-distinguisher exception at the inherited first Hasse fork now has an exact arbitrary-size structure. Opposite-side lower distinguishers are impossible in width three; the sibling predecessor sets are nested; their proper difference is a delayed chain with a canonical top Hasse blocker; the account01/B11 endpoint exchange applies to every first-fork sibling pair; and the strict branch either descends to a shorter extreme pair or opens a new canonical successor Hasse corridor. In the majority-early orientation, absence of descent forces exactly two successor Hasse blockers.

**Still unpaid.** POS3 is not proved. The remaining global obligation is to show that repeated span descent / Hasse-corridor continuation cannot propagate through all majority blocks. The next step should couple

1. the incoming bow-tie `d lessdot a greaterdot x lessdot b`,
2. the outgoing blocker(s) from Theorem 5.1,
3. the at-least-two-distinguisher constraints,
4. the next adjacent strong-majority boundary, and
5. the inherited heavy-slice / pinned-rank inequalities,

to force a balanced pair, a four-antichain, a proper autonomous nonchain, or an exact flux contradiction.

The correct next lead object is therefore the **strict nested corridor**, not the already-solved equal-predecessor fiber and not an unsupported claim that nesting by itself balances the siblings.

## 10. Source and integrity notes

Primary target references remain those recorded in the collective `TARGETS.md`, especially Chan–Pak, *Linear extensions of finite posets* (EMS Surveys 2025; arXiv:2311.02743v2, Section 13), and the bounded-width progress of Aires–Kahn (arXiv:2510.26134). The inherited `n_bal=14` frontier is preserved exactly from I0122; no finite-frontier movement is claimed.

No benchmark gold, credentials, scheduler identifiers, machine paths, unrelated private data, email, Drive, paid model/API/Codex execution, remote workflow, public release, or permission bypass was used. The verifier is finite regression only and is not cited as proof of the arbitrary-size theorems.
