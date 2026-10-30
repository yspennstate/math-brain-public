# POS3 fleet03/B10 — actual-law distortion floor and localization of every deletion-balanced pair

**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair whose ordering probability under the uniform law on all linear extensions lies in `[1/3,2/3]`.  
**Parent status after this report:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

This run stays on the exact fleet03/B10 assignment: apply the bounded-width/high-variance inputs to the true width-three target and make the remaining exceptional implication explicit. The main new point is a very simple but previously unused consequence of the exact first-element deletion law: a pair that is balanced under the genuine uniform law of the deletion poset cannot become arbitrarily one-sided after lifting back to the original poset. Its minority probability under the actual projected law is strictly more than `4/9` of its deletion-law minority probability. Combining this with the assigned partner's all-element rank-variance radius theorem localizes **every** deletion-balanced pair to strong-majority distance at most `3786` in a hypothetical counterexample.

No induced law is renamed uniform.

## 1. Exact state consumed

The exact assignment is:

> Apply bounded-width/high-variance results to the exact width-three target and derive the remaining exceptional-case requirement with constants/hypotheses explicit.

The assigned OTHER-account partner is **fleet04/B11**. I consumed its completed report

`proofnet24/collective-POS3/fleet04/B11/20260922T041135Z-B11-pos3-r14/REPORT.md`, commit `3128d0a95d554643fd325a32c86e23b3c60bc903`, blob `b6622b4cdf54821c2086566004a6a4d7a3415d95`.

The partner proves, in every hypothetical POS3 counterexample, that if `x=x_i`, `y=x_j` are incomparable and `i<j` in the transitive strong-majority order, then with `d=j-i`,

`Pr_P(y precedes x) < 2125440/(d+1)^2`.                         (1.1)

It also proves for the exact first-element tilt that the `kappa>=38` contribution to the probability shift of any deletion-balanced pair has absolute value `<15/1216<1/81`, leaving at most `741` shallow initial width-two ideals; this is a front-state localization, not a finite-poset reduction.

I also consumed the newest complete campaign-lead report

`proofnet24/collective-POS3/fleet04/B10/20260922T041420Z-B10-POS3-r13/REPORT.md`, blob `6acb56ae36d1cf3c59af1b9d22cc1b0cb2f70f44`.

It proves that after strict predecessor-corridor span descent is exhausted, the original uniform law always supplies a canonical incomparable pair with minority probability in `(1/6,1/3)`; the remaining lead-level obligation is a global amplification/charge mechanism.

The exact deletion law used below comes from the inherited fleet01/B19 recurrence and the preceding fleet03/B10 report. In the first-element deletion branch, let `c` be the first strong-majority element, `Q=P\{c}`, `nu` the genuine uniform law on `L(Q)`,

`S={z in Q : z || c}`,

and `kappa(tau)` the length of the initial `S`-run of `tau in L(Q)`. Put

`W(tau)=kappa(tau)+1`, `M=E_nu W`.

If `mu` is the restriction/projection of the **uniform law on `L(P)`** to `L(Q)`, then exactly

`d mu/d nu = W/M`.                                              (1.2)

For the full extension let `J=rank_P(c)-1`. The first-block pinned-rank bound gives

`Pr_P(J=0)>4/9`.                                                (1.3)

Exactly one legal lift of every `tau in L(Q)` has `J=0`, so

`Pr_P(J=0)=e(Q)/e(P)=1/M`; hence

`M<9/4`.                                                        (1.4)

The previous fleet03/B10 run used the second moment of `J` to truncate the exact tilt. This run changes the mechanism: instead of another tail estimate, it uses the pointwise likelihood-ratio floor `W>=1`.

## 2. Compact conditional end-to-end route

Assume POS3 is false and work in the inherited cardinality-minimal counterexample branch in which `Q=P\{c}` is a smaller nonchain. By minimality, under `nu` there is at least one incomparable pair `a,b` with

`1/3 <= nu(a<b) <= 2/3`.                                       (2.1)

The unresolved induction problem is that the original-poset probability is not `nu(a<b)` but `mu(a<b)`, where `mu` is the nonuniform tilt (1.2).

The first actual-law question is therefore how badly an arbitrary deletion-balanced pair can be distorted by this exact tilt before any adaptive covariance selection is attempted.

Section 3 proves a universal answer: its minority probability can shrink by a factor of **less than `9/4`**, and no more. Section 4 combines that with the partner's rank-variance estimate (1.1), proving that every deletion-balanced pair must already live in a bounded strong-majority window. Section 5 combines this with the partner's shallow-tilt theorem to state the remaining exact adaptive obstruction.

## 3. Exact likelihood-ratio floor for pair events

For an incomparable pair `a,b in Q`, let

`A={tau in L(Q): a precedes b}`, `q=nu(A)`.

### Theorem 3.1 — actual-law distortion floor

Under (1.2)-(1.4),

`mu(A) > (4/9) q`,                                              (3.1)

`mu(A^c) > (4/9)(1-q)`.                                        (3.2)

Consequently, writing

`b_nu(a,b)=min(nu(a<b),nu(b<a))`,
`b_mu(a,b)=min(mu(a<b),mu(b<a))`,

we have

`b_mu(a,b) > (4/9) b_nu(a,b)`.                                 (3.3)

#### Proof

By the exact projected law (1.2),

`mu(A)=E_nu[W 1_A]/M`.

Since `W=kappa+1>=1` pointwise,

`E_nu[W 1_A] >= nu(A)=q`.

By (1.4), `1/M>4/9`, hence

`mu(A) >= q/M > (4/9)q`.

Apply the identical argument to `A^c` to get (3.2). Taking the minimum yields (3.3). `square`

### Corollary 3.2 — every deletion-balanced pair survives at level `4/27`

If `a,b` is balanced under the genuine uniform deletion law `nu`, then

`b_mu(a,b) > 4/27`.                                            (3.4)

In a hypothetical counterexample `P`, where every incomparable pair has minority probability `<1/3`, every such deletion-balanced pair therefore lies in the strict strip

`4/27 < b_mu(a,b) < 1/3`.                                      (3.5)

This is a statement under the actual original-poset law. No tail truncation, surrogate law, or independence assumption is involved.

### Parameterized form

More generally, if `b_nu(a,b)>=beta`, then

`b_mu(a,b)>(4/9)beta`.                                         (3.6)

Thus a deletion pair closer to `1/2` automatically retains a proportionally stronger original-law minority mass. The constant `4/9` here comes only from the currently proved first-block pinned atom; no claim of sharpness is made.

## 4. Every deletion-balanced pair is strongly-majority local

Now assume `P` is a hypothetical counterexample, and index the inherited transitive strong-majority order as

`x_1 prec_* x_2 prec_* ... prec_* x_n`.

Take **any** incomparable pair `a,b in Q` that is balanced under `nu`. Relabel it as `a=x_i`, `b=x_j` with `i<j`, and put `d=j-i`.

Because `P` has no balanced pair, `prec_*` orients the pair strongly, so the minority probability under the original uniform law is exactly

`b_mu(a,b)=Pr_P(x_j precedes x_i)`.                             (4.1)

The assigned partner's theorem (1.1) and Corollary 3.2 give

`4/27 < b_mu(a,b) < 2125440/(d+1)^2`.                          (4.2)

Therefore

`(d+1)^2 < 2125440 * 27/4 = 14346720`.                         (4.3)

The adjacent exact squares are

`3787^2 = 14341369`,
`3788^2 = 14348944`.

Hence

### Theorem 4.1 — universal deletion-balanced radius

Every pair that is balanced under `nu` satisfies

`d <= 3786`.                                                    (4.4)

Equivalently there are at most `3785` strong-majority positions strictly between its endpoints.

This is stronger in scope than the partner's previous `3570`-radius result for the lead's **particular** canonical pair with minority probability `>1/6`: (4.4) applies to **every** pair supplied by minimality in the deletion poset, at the weaker but still universal `4/27` original-law level.

The general parameterized version obtained from (3.6) and (1.1) is

`d+1 < sqrt(4782240/beta)`                                     (4.5)

whenever `b_nu(a,b)>=beta`.

### What this does not claim

The bound (4.4) does not make `P` finite. The `3786`-window can occur arbitrarily far along a long poset and can have arbitrarily large residual continuations attached to it. It is therefore a localization of the adaptive pair-selection problem, not a finite-kernel theorem.

## 5. Combination with the partner's exact shallow-tilt theorem

For a deletion-balanced event `A`, the assigned partner writes

`mu(A)-q = T_G(A)+R_D(A)`,                                     (5.1)

where

`G={kappa<=37}`,
`T_G(A)=(1/M) E_nu[(1_A-q) kappa 1_G]`,                        (5.2)

and

`|R_D(A)| < 15/1216 < 1/81`.                                  (5.3)

The shallow score (5.2) is indexed by at most `741` initial ideals of the width-at-most-two ideal `S`, although each residual continuation can still be arbitrarily large.

The new Theorem 4.1 shows that **all** `nu`-balanced pairs to which (5.1) can be applied already have endpoint distance at most `3786` in the original strong-majority order. Thus a hypothetical counterexample must simultaneously satisfy the following for every deletion-balanced pair:

1. its actual original-law minority probability lies in `(4/27,1/3)`;
2. its strong-majority endpoint distance is at most `3786`;
3. all but `<1/81` of its tilt transfer is represented by the same at-most-`741` shallow first-hit states;
4. despite (1)-(3), its shallow plus deep transfer still pushes it strictly outside `[1/3,2/3]`.

This is a genuinely smaller exceptional regime than the earlier unbounded-weight WICSL statement: both the pair span and the relevant front-state depth are now universally bounded, while the residual continuation remains arbitrary-size.

## 6. Refined first missing implication

A sufficient next statement can be phrased without pretending the deletion law is the original law.

> **BR3786-SH741 adaptive transfer lemma.** In the first-element deletion branch of a cardinality-minimal hypothetical width-three counterexample, let `nu` be uniform on `L(Q)` and let `mu` be the exact `(kappa+1)`-tilt (1.2). Among the `nu`-balanced incomparable pairs — which Theorem 4.1 shows all have strong-majority distance at most `3786` — select one for which the shallow score `T_G` in (5.2), together with the rigorously bounded remainder (5.3), leaves the actual probability in `[1/3,2/3]`.

Equivalently, if the target is false then every `nu`-balanced pair in that bounded span must exhibit a coherent same-sign shallow Simpson displacement large enough to escape the balanced interval. The next mathematical mechanism should exploit overlap/flux between these bounded-span pair windows and the lead's canonical `(1/6,1/3)` fork/bridge selector, rather than improve the constants `3786`, `741`, or `1/81` in isolation.

This is still an adaptive correlation problem, not a finite census.

## 7. Relation to the lead's current selector

The campaign lead now guarantees, after strict-corridor descent is exhausted, an original-law canonical pair with minority in `(1/6,1/3)`. The deletion induction guarantees at least one `nu`-balanced pair, and Theorem 3.1 places every such pair in `(4/27,1/3)` under the original law if `P` is a counterexample.

Thus the two surviving mechanisms are now quantitatively close in the same actual-law scale:

- corridor selector: minority in `(1/6,1/3)`;
- deletion-balanced selector: minority in `(4/27,1/3)` and strong-majority distance `<=3786`.

The missing global step is to force one of these one-sided masses across `1/3` by a common overlap/charge argument. No claim that this amplification is already proved is made here.

## 8. Status

- POS3: **OPEN / NOT PROVED**.
- Exact actual-law distortion floor (3.3): **PROVED**.
- Every `nu`-balanced pair has actual minority `>4/27`: **PROVED**.
- Every `nu`-balanced pair has strong-majority distance `<=3786`: **PROVED**, conditional only on the inherited hypothetical-counterexample rank-variance theorem and exact deletion setup.
- BR3786-SH741 adaptive transfer lemma: **OPEN**.
- No finite-kernel, finite-census, fixed-pair balance transfer, or target-level closure is claimed.

No computation beyond exact integer arithmetic was used. No induced law was relabelled uniform. No benchmark gold, FEI proof material, credentials, scheduler identifiers, machine paths, unrelated private data/transcripts, email, Drive data, paid model/API/Codex execution, remote workflow, public release, permission change, or production-brain mutation was used. No authenticated brain retrieval/context use occurred, so the run remains `WITHOUT_VERIFIED_BRAIN`.
