# POS3 account04/B19 — crossed-singleton fringe funnel and reciprocal-module exclusion

**Run:** `B19-20260922T041629Z-auto11`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has incomparable `x,y` with `1/3 <= Pr(x<y) <= 2/3` under the uniform law on all linear extensions.  
**Parent status:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

This run follows `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`. It performs no brain-installation or benchmark work. The new step is an arbitrary-size structural reduction for the latest crossed-neighborhood branch; the finite computation in Section 7 is regression evidence only.

## 1. Exact source-bound state consumed

The newest complete team-lead report read before the derivation was:

1. **Team lead account04/B10**, `proofnet24/collective-POS3/account04/B10/20260922T034709Z-B10-POS3-r12/REPORT.md`, blob `4759a4ecb5f2963a3d190f66fc6728459bb1a46e`.

   Its crossed-neighborhood theorem says that if `x||y`, `Pred(x) subseteq Pred(y)`, and `Succ(y) subseteq Succ(x)`, then with

   `D=Pred(y)\Pred(x)`, `U=Succ(x)\Succ(y)`,

   and

   `A_D={some d in D is after x in the extension}`,
   `B_U={some u in U is before y in the extension}`,

   one has the exact full-extension identity

   `2 Pr(x<y)-1 = Pr(A_D union B_U)`.                           (1.1)

   In width at most three, only maximal members of `D` and minimal members of `U` are needed, at most two on each side. In the inherited no-internal-descent strict-chain branch the canonical lower distinguisher lies before `x` in the strong-majority order and the canonical upper distinguisher lies after `y`. The lead isolates the singleton two-gap case `D={d}`, `U={u}` as the sharp local obstruction; the 15-point adversary shows the local overlap inequality alone cannot close it.

The required named **OTHER-account partner result** applied here is:

2. **Partner account01/B10**, `proofnet24/collective-POS3/account01/B10/20260922T035049Z-account01-B10-pos3-r11/REPORT.md`, blob `9be1d4000e5d174e7587039ad16140a7308be3b0`.

   In the majority-late strict corridor, if

   `d lessdot a`, `b lessdot z`, `d prec_* b prec_* a prec_* z`,

   `d||b`, `a||z`, and `d<z`, then along any saturated `d-z` chain either an internal chain point gives a strictly smaller strong-majority incomparable span, or there is one cover edge `l lessdot r` crossed heavily by both endpoints:

   `Pr(l<b<r)>1/3` and `Pr(l<a<r)>1/3`.                        (1.2)

The prior B19 structural result used below is:

3. **account04/B19**, `proofnet24/collective-POS3/account04/B19/B19-20260922T001218Z-r44/REPORT.md`, blob `ce30dae79d698103f026d4d871033238489b1fb1`.

   It proves that a cardinality-minimal POS3 counterexample has **no proper autonomous nonchain subset**: restriction of the ambient uniform extension law to an autonomous subset is exactly uniform on the induced subset.

The immediately preceding B19 report is:

4. `proofnet24/collective-POS3/account04/B19/B19-20260922T031150Z-r46/REPORT.md`, blob `9079d05dcdf18d3afdb391d39148ed8c4653768d`.

   It eliminates indefinite clean equal-predecessor fork escalation and supplies TP2 budgets before the resulting lower-distinguisher exit. The present run uses a different mechanism on the newer crossed-neighborhood branch.

## 2. Compact conditional end-to-end route

Assume for contradiction that POS3 is false and choose a cardinality-minimal width-at-most-three counterexample `P`. The inherited reductions give a transitive strong-majority total order `prec_*`, connected incomparability, and no proper autonomous nonchain.

The latest lead reduces one terminal local obstruction to a crossed pair `x||y` with singleton lower and upper discrepancies

`Pred(x) subset Pred(y)`, `Pred(y)\Pred(x)={d}`,                 (2.1)

`Succ(y) subset Succ(x)`, `Succ(x)\Succ(y)={u}`,               (2.2)

and in the no-internal-descent orientation

`d prec_* x prec_* y prec_* u`.                                (2.3)

The first uncovered question is whether this sharp two-gap configuration can remain a self-contained local obstruction. The answer proved below is **no**.

- If `d<u`, the exact hypotheses automatically produce the partner's majority-late Hasse corridor, so one gets span descent or a doubly crossed cover edge.
- If `d||u`, the outer pair `(d,u)` inherits crossed predecessor/successor nesting and is quantitatively amplified to `Pr(d<u)>5/6`. Moreover, if its only two distinguishers were the original inner pair `x,y`, the four elements would form a proper autonomous `2+2`, forbidden in a minimal counterexample. Hence the outer pair must acquire at least one **additional** distinguisher.

Thus the singleton crossed obstruction cannot close on four elements. It must export either to the partner's common-cover transport object or to a genuinely higher-distinguisher, very strongly biased outer pair.

## 3. Crossed-singleton geometry

### Lemma 3.1 — the two singleton discrepancies are Hasse edges

Under (2.1)-(2.2),

`d lessdot y`,                                                   (3.1)

`x lessdot u`,                                                   (3.2)

and `u<d` is impossible. Consequently exactly one of `d<u` or `d||u` holds.

### Proof

First `d<y` by definition of `D`. If there were `d<z<y`, then `z in Pred(y)` and `z != d`. By (2.1), every predecessor of `y` other than `d` is a predecessor of `x`, so `z<x`. Then `d<z<x`, contradicting `d notin Pred(x)`. Hence `d lessdot y`.

Dually, `x<u`. If `x<z<u`, then `z in Succ(x)` and `z != u`. By (2.2), `z in Succ(y)`, so `y<z<u`, contradicting `u notin Succ(y)`. Hence `x lessdot u`.

Finally, `u<d` would give `x<u<d<y`, hence `x<y` in `P`, contradicting `x||y`. `square`

This Hasse conclusion uses only the exact singleton neighborhood equalities; no probability estimate enters.

## 4. Comparable fringe endpoints: direct import of the partner funnel

### Theorem 4.1 — the `d<u` singleton case is already a common-cover transport case

Assume (2.1)-(2.3) and `d<u`. Then, after the relabeling

`a=y`, `b=x`, `z=u`,                                             (4.1)

the hypotheses of account01/B10's common-cover theorem are satisfied:

`d lessdot a`, `b lessdot z`,

`d prec_* b prec_* a prec_* z`,

`d||b`, `a||z`, and `d<z`.

Therefore either

1. some point of a saturated `d-u` chain yields a strictly smaller strong-majority incomparable span than `(x,y)`, or
2. there exists a cover edge `l lessdot r` with

   `Pr(l<x<r)>1/3` and `Pr(l<y<r)>1/3`.                         (4.2)

### Proof

The Hasse relations are Lemma 3.1. The strong-order relation is (2.3). Since `d in Pred(y)\Pred(x)`, one has `d||x`; otherwise `d<x` would put `d` in `Pred(x)`, while `x<d<y` would contradict `x||y`. Similarly `u in Succ(x)\Succ(y)` implies `u||y`. Thus every hypothesis of the partner theorem holds with (4.1), and its dichotomy gives the conclusion. `square`

This is a substantive integration of the named other-account result: the latest lead's sharp singleton two-gap branch with comparable fringe endpoints is not a new unrelated obstruction.

## 5. Incomparable fringe endpoints: outer nesting and `5/6` amplification

Now assume `d||u`.

### Lemma 5.1 — the outer pair is crossed and contains the inner pair as distinguishers

One has

`Pred(d) subseteq Pred(u)`,                                     (5.1)

`Succ(u) subseteq Succ(d)`,                                     (5.2)

and

`x in Pred(u)\Pred(d)`,                                        (5.3)

`y in Succ(d)\Succ(u)`.                                        (5.4)

### Proof

If `t<d`, then `t<y`. Since `t != d`, (2.1) gives `t<x`, and `x<u` gives `t<u`. This proves (5.1).

If `u<t`, then `x<u<t`, so `t in Succ(x)`. Since `t != u`, (2.2) gives `y<t`; with `d<y` this gives `d<t`. This proves (5.2).

Equation (5.3) follows from `x<u` and `x||d`; (5.4) follows from `d<y` and `y||u`. `square`

### Theorem 5.2 — strong-bias amplification

Under (2.1)-(2.3) and `d||u`,

`Pr(d<u) > 5/6`.                                                (5.5)

### Proof

Apply the lead's exact crossed-neighborhood identity (1.1) to the outer incomparable pair `(d,u)`. Lemma 5.1 gives the required nesting.

Its lower discrepancy `Pred(u)\Pred(d)` contains `x`. Therefore the lead's lower fringe union contains the event `{d<x}`. By (2.3), `d prec_* x`; since `d||x` and the poset has no balanced pair,

`Pr(d<x)>2/3`.                                                  (5.6)

Hence the outer fringe union in (1.1) has probability strictly larger than `2/3`. Thus

`2 Pr(d<u)-1 > 2/3`,

which rearranges to (5.5). `square`

The same conclusion also follows using the upper fringe event `{y<u}`, which has probability `>2/3` by (2.3). The point is that the lead's exact union identity turns either inherited inner strong edge into a strictly stronger outer bias.

## 6. Reciprocal singleton exclusion: otherwise an autonomous `2+2`

The remaining possibility would be that the outer crossed pair has **no distinguishers beyond the inner pair**, i.e.

`Pred(u)\Pred(d)={x}`,                                          (6.1)

`Succ(d)\Succ(u)={y}`.                                         (6.2)

This cannot occur in a minimal counterexample.

### Theorem 6.1 — reciprocal singleton neighborhoods force an autonomous `2+2`

Assume (2.1)-(2.2), `d||u`, and (6.1)-(6.2). Then

`M={d,x,y,u}`                                                   (6.3)

is an autonomous subset of `P`, and the induced order on `M` is exactly the disjoint union of two 2-chains

`d<y`, `x<u`.                                                   (6.4)

### Proof

The only internal comparabilities are those in (6.4): `d||x` and `y||u` were noted above, `x||y` is the original pair, and `d||u` is the present branch. Any additional cross-comparability would force `x<y` or contradict one of the displayed Hasse directions.

It remains to prove autonomy. Let `t` lie outside `M`.

Suppose first that `t` is below one member of `M`.

- If `t<d`, then `t<y`; because `t!=d`, (2.1) gives `t<x`, and then `t<u`.
- If `t<x`, then `t<u`; because `t!=x`, (6.1) gives `t<d`, hence by the previous bullet `t` is below all four.
- If `t<y`, then `t!=d`, so (2.1) gives `t<x`, and again `t` is below all four.
- If `t<u`, then `t!=x`, so (6.1) gives `t<d`, and again `t` is below all four.

Thus an outside element below any member is below every member.

The dual argument uses (2.2) and (6.2). If `t` is above any one of `d,x,y,u`, it is above all four. Explicitly, `x<t` with `t!=u` gives `y<t` by (2.2), then `d<t`, and (6.2) gives `u<t`; the other starting points reduce to this one symmetrically.

If neither of these cases occurs, `t` is incomparable with every member of `M`. Hence every outside element is uniformly below, uniformly above, or uniformly incomparable with `M`, proving autonomy. `square`

### Corollary 6.2 — the incomparable-fringe branch must gain a third distinguisher

In a cardinality-minimal POS3 counterexample satisfying (2.1)-(2.3) and `d||u`, at least one of

`Pred(u)\Pred(d)` or `Succ(d)\Succ(u)`

contains an element beyond `x` or `y`, respectively. Equivalently the outer pair `(d,u)` has at least **three** distinguishers in total.

### Proof

If not, Theorem 6.1 gives the autonomous nonchain `M`. If `M` is proper, this contradicts the prior B19 autonomous-module reduction. If `M=P`, then `P` is the `2+2` poset; its two minimal elements `d,x` are exchanged by an automorphism, so `Pr(d<x)=1/2`, giving a balanced pair directly. Thus `M` cannot occur in a counterexample. `square`

Combining with Theorem 5.2, the new outer pair is not merely a multi-distinguisher pair: it is an incomparable crossed pair with

`Pr(d<u)>5/6`                                                   (6.5)

and at least one additional distinguisher beyond the original inner pair.

## 7. Exact finite regression

The standard-library checker

`proofnet24/collective-POS3/account04/B19/B19-20260922T041629Z-auto11/verify_singleton_fringe_funnel.py`

has Git blob `d4b31033ca3a31adfd00fc67e85311045ff5a72a`. It exhausts every transitively closed naturally labelled poset through `n=6`, tests every ordered quadruple satisfying the exact singleton crossed-neighborhood hypotheses, verifies Lemmas 3.1 and 5.1, verifies autonomy in every reciprocal-singleton case, and then exactly enumerates linear extensions for the instances satisfying the strong-order inequalities used in Theorem 5.2.

Captured output has Git blob `d031b569a861e2ca16dd21e00e462c9a4023e380`:

```text
n 4 singleton 11 d_lt_u 5 d_parallel_u 6 reciprocal_singleton 6 strong_outer_cases 0 amplification_failures 0 min_Pr_d_before_u NA
n 5 singleton 198 d_lt_u 98 d_parallel_u 100 reciprocal_singleton 42 strong_outer_cases 0 amplification_failures 0 min_Pr_d_before_u NA
n 6 singleton 3742 d_lt_u 1967 d_parallel_u 1775 reciprocal_singleton 342 strong_outer_cases 14 amplification_failures 0 min_Pr_d_before_u 13/14
POS3_SINGLETON_FRINGE_FUNNEL_CHECK_PASS
```

The observed minimum `13/14` is regression data only and is **not** claimed as a universal strengthening of `5/6`.

## 8. What this changes in the global induction

The latest lead report left the singleton crossed two-gap branch as the arithmetically sharp local obstruction. The present theorem shows that this branch cannot remain local.

For a cardinality-minimal counterexample in the terminal orientation (2.3), the singleton branch now exits in one of the following source-valid ways:

1. **Comparable fringe endpoints `d<u`:** by Theorem 4.1, either strict strong-majority span descent occurs or account01/B10's doubly crossed cover edge appears.
2. **Incomparable fringe endpoints `d||u`:** by Theorem 5.2 and Corollary 6.2, the outer pair has probability `>5/6` and at least three distinguishers.

There is no third order relation between `d,u`, and the reciprocal two-distinguisher outer case is excluded by the autonomous `2+2` argument.

So the lead's next global charge can discard a persistent four-element singleton obstruction. It only needs to handle:

- the partner's **double-crossed-cover transport** object;
- a **three-or-more-distinguisher outer crossed pair with bias `>5/6`**;
- the lead's already non-singleton canonical-fringe cases; and
- the separately acknowledged non-crossed-successor branch.

This is a genuine arbitrary-size narrowing. It does not count a local constant or finite census as closure.

## 9. First remaining implication

The next precise implication on this route is now:

> **Amplified outer-fringe charge.** Let `d||u` be the outer pair produced by Theorem 5.2 in a minimal width-three counterexample. Use width-three canonical fringe compression plus the full three-chain TP2/heavy-slice constraints to show that the required third distinguisher of `(d,u)`, together with `Pr(d<u)>5/6`, forces either a balanced pair, strong-majority span descent, or the partner's double-crossed-cover state with a strictly improved global potential.

This is strictly stronger input than the preceding lower-distinguisher obligation: the outer pair has a certified `>5/6` bias and cannot have only the two reciprocal inner distinguishers.

The parent POS3 target remains open. No full-proof claim is made.

## 10. Claim status and scope

- Singleton discrepancies imply `d lessdot y`, `x lessdot u`, and exclude `u<d`: **PROVED**.
- Comparable singleton fringe endpoints feed the named account01/B10 common-cover theorem: **PROVED / PARTNER APPLIED**.
- Incomparable fringe endpoints inherit crossed nesting: **PROVED**.
- Outer bias `Pr(d<u)>5/6` in the terminal strong-order orientation: **PROVED** from the lead's exact union identity.
- Reciprocal singleton outer neighborhoods force an autonomous induced `2+2`: **PROVED**.
- Such a reciprocal `2+2` is impossible in a cardinality-minimal counterexample: **PROVED** using the prior B19 autonomous-module theorem (or direct balance if it is all of `P`).
- Full width-three `1/3-2/3` target: **OPEN / NOT PROVED**.
- Outcome: `ESSENTIAL_STEP_APPLIED`.

Scoped provenance/privacy review: the committed scientific files contain mathematical statements, repository-relative source references, Git object identifiers, deterministic standard-library verifier code/output, and nonsecret run labels only. They contain no benchmark gold, credentials, scheduler identifiers, machine paths, unrelated private data/transcripts, email or Drive material, paid-model/API/Codex calls, remote-workflow instructions, public-posting actions, or permission changes.
