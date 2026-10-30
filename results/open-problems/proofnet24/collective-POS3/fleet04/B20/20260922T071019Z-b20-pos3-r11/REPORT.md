# POS3 fleet04/B20 — incoming transposition cancellations are forced to strict strong-order superintervals

**Run:** `20260922T071019Z-b20-pos3-r11`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has incomparable `x,y` with `1/3 <= Pr(x<y) <= 2/3` under the uniform law on all full linear extensions.  
**Parent status:** **OPEN / NOT PROVED**.  
**Inherited finite frontier:** `n_bal=14`, unchanged.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

Every probability and count below is for the original uniform law on all full linear extensions. No deletion-induced law is treated as uniform.

## 1. Exact collective state consumed

The latest complete team-lead state consumed is

- fleet04/B10 r16, `proofnet24/collective-POS3/fleet04/B10/20260922T064124Z-B10-POS3-r16/REPORT.md`, which proves lossless boundary-anchor recoding of every canonical outgoing heavy-gap defect and, in the low-endpoint branch, two distinct fully outward actual pairs each carrying more than `2E/33` marked extensions. It leaves **OUTWARD-STATE RECYCLING** as the first unpaid global implication.

The required named OTHER-account partner state consumed is the newest complete fleet01/B19 report available before this derivation:

- fleet01/B19 r13, `proofnet24/collective-POS3/fleet01/B19/20260922T054717Z-b19-pos3-r13/REPORT.md`. Its exact four-state selector gives a continuing exact-two corridor pair with minority at least `3E/11`; therefore the exact numerical gap to the balanced threshold is `2E/33`. It also shows that bounded local corridor length cannot replace the global exit argument.

A newer fleet01/B19 directory `20260922T065044Z-b19-pos3-r14` had only a start record at the source snapshot and was not promoted to a completed mathematical input.

Two exact dependencies are also used:

- fleet03/B11, `proofnet24/collective-POS3/fleet03/B11/20260922T061153Z-fleet03-B11-pos3-r11/REPORT.md`, for the two signed swap identities and canonical Hasse realization of outgoing defects;
- fleet03/B10, `proofnet24/collective-POS3/fleet03/B10/b10-20260922t061504z-r11/REPORT.md`, for the fact that the exact-two recurrence reaches the first actual non-exact boundary with zero probability-count defect; the unresolved issue is structural charge conversion, not a missing additive term.

The present run deliberately attacks a different mechanism from the preceding B20 successor-staircase theorem: it analyzes the **negative/incoming terms** in the exact transposition identities and asks whether they can cancel exported charge locally.

## 2. Live heavy-cover setup and exact signed identities

Work in the inherited hypothetical minimal no-balanced branch with the transitive strong-majority order `prec_*`. Let

`x lessdot y`, `a||x,y`, `x prec_* a prec_* y`.

Partition all `E` full linear extensions into

- `A={L:a<x<y}`;
- `H={L:x<a<y}`;
- `C={L:x<y<a}`.

Thus `A+H+C=E`, and because the two endpoint incomparable pairs are strong-majority oriented as displayed,

`A/E<1/3`, `C/E<1/3`.

Use fleet03/B11's signed transposition notation:

- `D_H^-`: middle extensions for which swapping the positions of `x,a` is invalid;
- `D_A^+`: left-end extensions for which the reverse swap of `x,a` is invalid;
- `D_H^+`: middle extensions for which swapping the positions of `a,y` is invalid;
- `D_C^-`: right-end extensions for which the reverse swap of `a,y` is invalid.

The exact full-extension identities are

`|D_H^-|-|D_A^+|=H-A`,                                      (2.1)

`|D_H^+|-|D_C^-|=H-C`.                                      (2.2)

The positive terms were structurally localized by B10 r16. The new point is that the negative terms cannot be a local sink: every incoming defect canonically leaves the old half-interval in the opposite, span-increasing direction.

## 3. Canonical incoming Hasse witnesses

### Theorem 3.1 — every incoming defect has one of four Hasse forms

For every `L in D_A^+`, with displayed order `a<x<y`, there is a vertex `r` strictly between `a` and `x` in `L` of one of the two forms

`I1={r:r lessdot x, r||a}`,                                  (3.1)

`I2={r:a lessdot r, r||x}`.                                  (3.2)

For every `L in D_C^-`, with displayed order `x<y<a`, there is a vertex `r` strictly between `y` and `a` in `L` of one of the two dual forms

`J1={r:y lessdot r, r||a}`,                                  (3.3)

`J2={r:r lessdot a, r||y}`.                                  (3.4)

### Proof

Take `L in A`. Swapping the positions of `a` and `x` moves `x` earlier and `a` later. If the result is invalid, then some vertex strictly between their positions either

1. is a predecessor of `x`, so moving `x` before it breaks that relation; or
2. is a successor of `a`, so moving `a` after it breaks that relation.

In case 1, follow a saturated chain from that predecessor to `x` and take the final vertex before `x`. It lies between `a` and `x` in `L`, is a lower cover of `x`, and is incomparable with `a`: comparability in either direction would contradict either `a||x` or the displayed linear-extension order. This is `I1`.

In case 2, follow a saturated chain upward from `a` and take the first vertex. It lies between `a` and `x`, is an upper cover of `a`, and is incomparable with `x`, giving `I2`.

The proof for `L in C` is dual. Swapping `y` and `a` moves `y` later and `a` earlier. An obstruction is either a successor of `y` or a predecessor of `a`; following a saturated chain to the relevant endpoint gives `J1` or `J2`. `square`

### Width-three capacity

In width at most three,

`|I1|,|I2|,|J1|,|J2| <= 2`.                                 (3.5)

For example, three distinct lower covers of `x` are pairwise incomparable; since every member of `I1` is also incomparable with `a`, three of them together with `a` would form a four-antichain. The other three bounds are dual.

Moreover the four vertex families are pairwise disjoint. Each possible overlap contradicts one of the defining relation/incomparability conditions; for instance `I1 cap J1` would force `r<x<y<r`, while `I1 cap J2` would require both `r||a` and `r<a`.

Thus every incoming left defect can be assigned canonically to at most four vertices, every incoming right defect to at most four vertices, and the two sides use disjoint canonical vertex families.

## 4. Strict-superinterval theorem

Let `rank_*(v)` be the position of `v` in the inherited transitive strong-majority order, and for an oriented incomparable pair `u prec_* v` write

`span_*(u,v)=rank_*(v)-rank_*(u)`.

### Theorem 4.1 — every incoming defect is already a minority mark on a strict superinterval

A deterministic choice of the Hasse witness in Theorem 3.1 gives the following lossless charge map.

For `L in D_A^+`:

- if its witness `r` is in `I1`, charge `L` to the actual incomparable pair `(r,a)` and the event `{a<r}`;
- if `r` is in `I2`, charge `L` to `(x,r)` and the event `{r<x}`.

For `L in D_C^-`:

- if `r` is in `J1`, charge `L` to `(a,r)` and the event `{r<a}`;
- if `r` is in `J2`, charge `L` to `(r,y)` and the event `{y<r}`.

Every charged orientation is a minority orientation and its strong-order span strictly contains the corresponding old half-interval:

`I1: r prec_* x prec_* a`, so `span_*(r,a)>span_*(x,a)`;       (4.1)

`I2: x prec_* a prec_* r`, so `span_*(x,r)>span_*(x,a)`;       (4.2)

`J1: a prec_* y prec_* r`, so `span_*(a,r)>span_*(a,y)`;       (4.3)

`J2: r prec_* a prec_* y`, so `span_*(r,y)>span_*(a,y)`.       (4.4)

### Proof

For `I1`, the witness relation `r<x` and the inherited strong-majority orientation `x prec_* a` give `r prec_* x prec_* a`. The marked order `a<r<x` is contained in the endpoint-minority event `{a<x}=A`, so `{a<r}` is a minority orientation. The span inequality is strict because `r` lies strictly before `x` in `prec_*`.

For `I2`, `a<r` is a poset relation, so `x prec_* a prec_* r`. The marked order `a<r<x` lies in `{a<x}=A`, making `{r<x}` minority; the charged span strictly extends past `a`.

The two right-side cases are dual. `J1` gives `a prec_* y prec_* r`, and its marked event `r<a` is contained in `{y<a}=C`. `J2` gives `r prec_* a prec_* y`, and its marked event `y<r` is likewise contained in `{y<a}=C`. `square`

The conclusion is stronger than a witness-existence statement: it keeps every incoming defect extension as an actual full-extension mark on a concrete incomparable pair.

## 5. New no-local-return consequence

Define a directed **incoming-cancellation edge** from the old oriented half-interval to the charged oriented incomparable pair in Theorem 4.1. Every such edge strictly increases `span_*` by at least one.

### Corollary 5.1 — the exact reverse-transposition cancellation graph is acyclic

No directed cycle can consist entirely of canonical incoming-cancellation edges. Along any such path, the integer potential `span_*` increases strictly at every step. In an `n`-element poset, a path beginning at span `s` contains at most `n-1-s` further incoming-cancellation steps.

This does **not** prove global recycler termination: a subsequent fork, exact-two, crossed, non-crossed or bridge transition may change mechanism, and the source-valid `R_N` family already rules out a bounded local-corridor argument. What is now excluded is the specific possibility that the negative terms in (2.1)-(2.2) repeatedly cancel the heavy-gap export by returning through the same or a smaller strong-order interval.

Thus B10 r16's outward positive defect flow and the present negative defect flow have complementary directions:

- outgoing canonical marks are boundary-anchored on fully outward pairs;
- incoming reverse-swap marks live on strict strong-order superintervals.

Immediate signed transposition cancellation therefore has no local directed cycle.

## 6. Quantitative consequence at the partner's `2/33` gap scale

Let

`I_L=|D_A^+|`, `I_R=|D_C^-|`.

Since each side has at most four canonical incoming pair channels, Theorem 4.1 gives

- if `I_L >= 8E/33`, then some strict-superinterval actual incomparable pair has at least `2E/33` marked minority extensions;
- if `I_R >= 8E/33`, the analogous statement holds on the right.

The threshold `2E/33` is exactly the numerical gap between fleet01/B19's `3E/11` selector and `E/3`.

In the low-endpoint branch of B10 r16, `A,C<3E/11`, the signed identities also give the strict **net** inequalities

`|D_H^-|-I_L = H-A = E-2A-C > 2E/11`,                       (6.1)

`|D_H^+|-I_R = H-C = E-A-2C > 2E/11`.                       (6.2)

So reverse defects cannot erase the positive heavy-gap current. If a reverse term is large, it itself produces a gap-scale packet on a strict superinterval; if it is small, the signed outward current remains quantitatively positive. This is a structural conversion of the exact signed terms, not an addition of probabilities from different pairs.

## 7. Deterministic regression

`verify_incoming_superinterval.py` exhausts every naturally labelled transitively closed poset through six vertices, keeps only width-at-most-three posets, enumerates all covers `x lessdot y` and all `a||x,y`, and checks:

1. every invalid reverse `A -> H` transposition has a between-position Hasse witness in `I1 union I2`;
2. every invalid reverse `C -> H` transposition has a between-position Hasse witness in `J1 union J2`;
3. each of the four Hasse families has size at most two;
4. the four canonical incoming families are pairwise disjoint;
5. the charged event of each family is structurally contained in the corresponding endpoint-minority event `A` or `C`.

Captured output:

```text
natural_transitive_closures_n3 7
natural_transitive_closures_n4 40
natural_transitive_closures_n5 357
natural_transitive_closures_n6 4824
width_at_most_three_posets 3699
cover_incomparable_triples 24996
left_incoming_defects 63296
right_incoming_defects 63296
maximum_incoming_family_size 2
failures 0
POS3_INCOMING_SUPERINTERVAL_CHECK_PASS
```

This computation is regression evidence only. The arbitrary-size statements are the symbolic proofs above.

## 8. First still-unpaid implication

The local signed transposition return has now been eliminated. The remaining target-level problem is narrower:

> **MIXED-MECHANISM OUTWARD RECYCLING.** Starting from B10 r16's two boundary-anchored outward `>2E/33` packets, prove that a sequence which alternates among fork/exact-two/crossed/non-crossed/bridge mechanisms cannot evade balance by repeatedly changing mechanism. Any use of an incoming reverse-transposition cancellation must strictly increase strong-order span by Theorem 4.1; therefore a genuine cycle must contain another transition type. Show that width three, the conserved exact-two `K`, and the already-proved non-crossed staircase charge force such a mixed-mechanism cycle to terminate in a balanced pair, strict span descent, a proper autonomous/ordinal reduction, a four-antichain contradiction, or a controlled charge-preserving exit.

This is strictly more specific than the previous generic OUTWARD-STATE RECYCLING obligation: the negative terms of the exact swap identities are no longer an unclassified return channel.

## 9. Status and integrity

- newest complete lead fleet04/B10 r16: **CONSUMED/APPLIED**;
- newest complete designated OTHER-account partner fleet01/B19 r13: **CONSUMED/APPLIED**;
- canonical incoming Hasse realization: **PROVED**;
- width-three incoming capacity `2+2` per side and pairwise disjointness: **PROVED**;
- lossless strict-superinterval minority charge for every incoming defect: **PROVED**;
- acyclicity of pure incoming-cancellation chains: **PROVED**;
- `2/33` quantitative large-incoming dichotomy: **PROVED**;
- mixed-mechanism global recycling termination: **OPEN**;
- parent POS3 theorem: **OPEN / NOT PROVED**;
- run classification: `ESSENTIAL_STEP_APPLIED`.

No novelty or priority claim is made. No benchmark material, credentials, scheduler identifiers, machine paths, unrelated private data/transcripts, email/Drive data, paid model/API/Codex call, remote workflow, permission change, public posting or native brain activation is used or claimed. The current connector did not expose the repository's local privacy scanner; before publishing this scoped report I performed a narrow content review for credentials, account identifiers beyond logical fleet labels, absolute machine paths, emails, signed URLs and unrelated private material, and found none. This fallback scan does not replace a repository-native scanner.
