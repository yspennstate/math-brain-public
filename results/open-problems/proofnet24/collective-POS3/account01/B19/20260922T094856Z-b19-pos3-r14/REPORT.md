# POS3 account01/B19 — canonical earliest-endpoint exports collapse to an exact two-cover fork

**Run:** `20260922T094856Z-b19-pos3-r14`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has incomparable `x,y` with `1/3 <= Pr(x<y) <= 2/3` under the uniform law on all full linear extensions.  
**Parent status:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

All counts below refer to the original uniform set of full linear extensions of the original poset. A chain-deletion projection is always retained with its exact multiplicity and is never renamed uniform.

## 1. Exact collective state consumed

Fresh shared controls assign account01/B19 to the chain insertion/deletion part of POS3. The latest complete campaign-lead result consumed is:

- account04/B10 `20260922T091028Z-account04-B10-pos3-r11`, `proofnet24/collective-POS3/account04/B10/20260922T091028Z-account04-B10-pos3-r11/REPORT.md`, blob `8a856fa924002567c01a8b70880003fe53b86da3`.

It works in a hypothetical no-balanced width-at-most-three counterexample, where the inherited strong-majority relation `prec_*` is a strict total order extending the poset order. It chooses the least possible later endpoint `q`, then the leftmost `p||q`, proves `D(p,q)=empty`, and proves that the first positive Hasse export cannot be a span-exhausted heavy bridge.

The newest complete team-integrator result used is:

- account04/B20 `20260922T094004Z-B20-POS3-r11b-auto`, report blob `fc88efaf9bfa7915364bd87469f083d089b99938`.

It proves the **prefix-chain / terminal-block barrier**: every vertex before the earliest endpoint `q` lies in one poset chain; the vertices incomparable with `q` form a terminal block `I=[p,q)`; for every `s in I`, `D(s,q)=empty`; and a `q`-anchored transposition/heavy-bridge re-entry cannot be neutral.

The assigned OTHER-account partner result consumed is:

- account02/B10 `20260922T084851Z-b10-pos3-r12`, canonical report commit `57a563af112063929fae35a4aa28c4fe61aa64cf`, report blob `0d6b6aaf49e848e27daf8bc78d672cb28ed58aa4`.

Its exact-backtrack theorem gives the full-law transposition identity and proves noncentral leakage on both sides of a heavy bridge. In particular, the endpoint transposition of a strong pair has outgoing-minus-incoming defect equal to `2N-E`, with all illegal swaps localized on genuine Hasse channels.

I also apply account04/B19 `B19-20260922T091459Z-r46`, report blob `3ab26879c6f8301fa782a8ee1d2fbd47dca150a7`, which proves one-sided same-cover span resets have exact lexicographic potentials and leaves cover-changing / alternating-side re-entry as the first local splice obstruction.

For the chain-weight formulas I retain account01/B19 `20260922T084614Z-b19-pos3-r11`, report blob `c1442ecaf5ca6f61b5a97fcbf1fc18ca85518aff`: chain deletion is represented by exact interval-profile path counts, and fixed-profile insertion acts by prefix-sum operators.

## 2. Exact chain-deletion recurrence at the earliest endpoint

Let `q` be the least `prec_*`-rank that is the later endpoint of any incomparable pair. By account04/B20, the set

`C={c_1 prec_* ... prec_* c_m : c_j prec_* q}`

is a poset chain in the same order. Let `p=c_a` be the first element of this chain incomparable with `q`. Then

- `c_j<q` for `j<a`;
- `c_j||q` for `j>=a`.

Delete the whole chain `C`, and write `Q=P\C`. For any `x in Q`, let `I_C(x)=[lambda(x),rho(x)]` be the interval of possible numbers of `C`-elements preceding `x` in a full lift. If `tau=(x_1,...,x_n) in L(Q)`, then its exact full-extension multiplicity is

`W_C(tau)=#{z_1<=...<=z_n : z_i in I_C(x_i)}`.                 (2.1)

Equivalently, with

`f_1(t)=1_{t in I_C(x_1)}`

and

`f_i(t)=1_{t in I_C(x_i)} sum_{s<=t} f_(i-1)(s)`,             (2.2)

we have

`W_C(tau)=sum_t f_n(t)`.                                      (2.3)

This is the exact chain-insertion recurrence required by the assignment. It is a recurrence for the true biased projection multiplicity, not for a fictitious uniform law on `L(Q)`.

For the canonical element `q`,

`I_C(q)=[a-1,m]`.                                             (2.4)

Now fix `s=c_k` in the terminal incomparability block and an upper Hasse witness

`r in U(s,q)={r:s lessdot r, r||q}`

lying in the surviving no-immediate-descent branch `q prec_* r`. Because `s lessdot r`, no `c_j` with `j>k` can lie below `r`; because `q prec_*r` while every such `c_j prec_*q`, none can lie above `r`. Therefore

`I_C(r)=[k,m]`.                                               (2.5)

In particular, for the canonical left endpoint `s=p=c_a`, every surviving upper witness has the one-slot profile

`I_C(r)=[a,m] subset [a-1,m]=I_C(q)`.                         (2.6)

Thus the exact chain-insertion bias at the canonical fork is especially simple. For adjacent projected occurrences of `q,r` with all outside insertion states fixed, the nested-profile determinant from the exact recurrence gives

`W(...,q,r,...)-W(...,r,q,...)=U_(a-1) V_[a,m] >= 0`,         (2.7)

where `U_(a-1)` is the exact prefix mass reaching the unique extra state `a-1` and `V_[a,m]` is the exact suffix completion mass from the inner profile. Hence the chain insertion itself contributes a one-sided, rank-one bias in the `q<r` direction; every remaining obstruction is carried by genuine projected/Hasse geometry.

## 3. Main theorem: every undescended earliest-endpoint export is an exact two-cover fork

For `s in I`, orient the strong pair as `s prec_* q` and write

`M_s=N(s<q)`, `E=e(P)`.

Since the candidate has no balanced pair,

`M_s>2E/3`.                                                    (3.1)

Let `O_s` and `J_s` be the outgoing and incoming illegal endpoint-transposition sets. The exact partner/lead identity is

`|O_s|-|J_s|=2M_s-E>E/3`,                                    (3.2)

so

`|O_s|>E/3`.                                                  (3.3)

By the terminal-block theorem,

`D(s,q)=emptyset`.                                            (3.4)

### Lemma 3.1 — exact outgoing-channel union

`O_s` is exactly the union of the upper-Hasse channel events

`O_s = union_(r in U(s,q)) {L : r<q in L}`.                  (3.5)

**Proof.** Every outgoing illegal swap has a Hasse witness in `U(s,q) union D(s,q)`. Equation (3.4) removes the lower family. For `r in U(s,q)`, the poset forces `s<r`; hence in an extension with `s<q`, the witness lies between the endpoint positions exactly when `r<q`. Conversely, if `r<q`, swapping `s` to the old position of `q` places `s` after `r`, violating `s<r`. `square`

### Lemma 3.2 — at most two upper channels

`|U(s,q)|<=2`.                                                (3.6)

**Proof.** Distinct upper covers of one vertex `s` are pairwise incomparable. Every member of `U(s,q)` is also incomparable with `q`. Thus `{q} union U(s,q)` is an antichain. Width at most three gives (3.6). `square`

### Theorem 3.3 — two-cover saturation

Suppose no member `r in U(s,q)` already gives the strict `q`-anchored subspan `s prec_*r prec_*q`. Then

1. `U(s,q)={r_1,r_2}` has **exactly two** vertices;
2. `q prec_* r_i` for both `i`;
3. `{q,r_1,r_2}` is a three-element antichain;
4. with `A_i={L:r_i<q in L}` and `alpha_i=|A_i|`,
   `alpha_i<E/3` for both `i`, while
   `|A_1 union A_2|>E/3`;
5. both exclusive cross cells are nonempty:
   `A_1\A_2 != empty` and `A_2\A_1 != empty`;
   equivalently there are full extensions with
   `r_1<q<r_2` and full extensions with `r_2<q<r_1`;
6. one of the two genuine channel minorities satisfies
   `alpha_i>E/6`;
7. the canonical pair itself satisfies the sharpened strict window
   `2/3 < M_s/E < 5/6`.

**Proof.** If `r prec_*q`, then because `s<r` in the poset we have `s prec_*r prec_*q`, giving the excluded strict subspan. Hence every surviving `r` satisfies `q prec_*r`. Since `q||r` and there is no balanced pair,

`alpha_r=N(r<q)<E/3`.                                        (3.7)

By Lemma 3.2 there are at most two such channels. Equations (3.3), (3.5), and (3.7) rule out zero or one channel, proving exactly two and the three-antichain statement.

Let `o=|A_1 union A_2|`. Since `o>E/3` while `alpha_2<E/3`,

`|A_1\A_2| = o-alpha_2 > E/3-alpha_2 > 0`,                  (3.8)

and symmetrically `|A_2\A_1|>0`. In the first exclusive event, `r_1<q` and not `r_2<q`, hence `r_1<q<r_2`; the other event is the reverse cross order.

Also

`alpha_1+alpha_2 >= o>E/3`,                                  (3.9)

so `max(alpha_1,alpha_2)>E/6`.

Finally, (3.2) and `|J_s|>=0` give

`2M_s-E <= o <= alpha_1+alpha_2 < 2E/3`,                     (3.10)

hence `M_s<5E/6`. Together with (3.1), this proves the stated window. `square`

This theorem is arbitrary-size and uses exact full-extension counts only.

## 4. Cover rigidity: one whole cover-changing reset class disappears

The two-fork geometry also pays part of the cover-changing residual left by account04/B19 r46.

### Theorem 4.1 — any second lower cover of a fork witness is an immediate strict subspan

Keep the hypotheses of Theorem 3.3 and fix `r_i`. If

`c lessdot r_i`, `c != s`,                                   (4.1)

then necessarily

`q prec_* c prec_* r_i`, `c||q`,                             (4.2)

and therefore `(q,c)` is a strict strong-majority subspan of `(q,r_i)`.

**Proof.** Distinct lower covers `c,s` of `r_i` are incomparable. If `c prec_*q`, then both `c` and `s` lie in the prefix strictly before `q`, which account04/B20 proves is a poset chain. That contradicts `c||s`. Thus `q prec_*c`. Since `c<r_i`, the strong order also has `c prec_*r_i`. If `q<c` in the poset, transitivity with `c<r_i` would give `q<r_i`, contrary to `q||r_i`; and `c<q` is impossible because it would force `c prec_*q`. Hence `c||q`, proving (4.2). `square`

### Corollary 4.2 — unique lower cover in a span-descent-exhausted branch

If the continuation has declared all strict strong-majority subspans already terminal/paid, then each surviving fork witness `r_i` has `s` as its **unique lower cover**. Thus a cover-changing re-entry that keeps the same right endpoint `r_i` cannot be neutral: the mere existence of a different lower Hasse endpoint has already exposed the strict subspan `(q,c)`.

At the canonical state `s=p`, the only direct `q`-middle same-left cover switch among incomparable upper covers of `p` is therefore the switch between the two vertices `r_1,r_2` supplied by Theorem 3.3. The generic cover-changing residual has collapsed, at the earliest endpoint, to a width-saturating two-cover fork plus excursions that change the larger envelope altogether.

This directly complements account04/B19 r46: one-sided same-cover resets are well founded by its `Phi_R/Phi_L`; the present theorem removes every same-right **cover change** at the canonical earliest block unless one accepts the already-authorized strict-span exit.

## 5. Source-valid guard: the bare four local probabilities still do not close POS3

The two-cover theorem is structural progress, but it would be incorrect to jump from it to the claim that one of the four pairs

`(p,q), (q,r_1), (q,r_2), (r_1,r_2)`

must already be balanced based only on the fork incidence and those local orientations.

The committed deterministic checker verifies the following width-three seven-element poset. Its Hasse covers are

`p<r_1`, `p<r_2`, `p<a`, `q<a`, `r_1<b`, `r_1<c`, `a<c`.      (5.1)

It has exactly `E=79` linear extensions and width exactly three. The four local ordering counts are

`N(p<q)=54`,

`N(q<r_1)=55`,

`N(q<r_2)=65`,

`N(r_1<r_2)=56`.                                             (5.2)

Every number in (5.2) is strictly larger than `2E/3=158/3`, so all four local pairs are strongly oriented. Nevertheless the poset is not a POS3 counterexample: for example

`N(r_2<a)=37`, so `Pr(r_2<a)=37/79 in [1/3,2/3]`.            (5.3)

Thus the bare two-cover incidence plus the four obvious strong orientations is not enough. The global earliest-endpoint / terminal-block / Hasse-channel constraints must be used in the next step.

Supporting files in this run directory:

- `verify_canonical_two_fork.py`;
- `verify_canonical_two_fork.out`, ending `POS3_CANONICAL_TWO_FORK_GUARD_PASS`.

The checker is evidence only for the explicit seven-element guard; Theorems 3.3 and 4.1 are symbolic arbitrary-size proofs.

## 6. Compact conditional end-to-end route after this run

Assume a finite width-at-most-three counterexample with no balanced pair.

1. The inherited total strong-majority order supplies the earliest later endpoint `q`.
2. account04/B20 makes the entire prefix before `q` a chain and the `q`-incomparables a terminal block; every state `(s,q)` in that block has `D(s,q)=empty` and cannot absorb a Hasse export neutrally.
3. The exact chain recurrence (2.1)-(2.3) retains every deletion multiplicity. At the canonical left boundary its witness profiles are the one-slot pair `[a-1,m]` versus `[a,m]`, so the deletion bias itself is explicit rather than hidden.
4. Theorem 3.3 says that every still-undescended `q`-anchored export is not a generic four-channel object: it is **exactly a two-upper-cover, width-saturating fork**, with both cross cells nonempty and a real channel of mass `>E/6`.
5. Theorem 4.1 rules out any neutral same-right cover change: a second lower cover immediately produces a strict subspan. account04/B19 r46 already rules out indefinite one-sided same-cover reset.
6. Therefore a surviving mixed excursion must either switch between the two canonical upper covers, leave the canonical envelope entirely, or take an already-authorized descent/balance/reduction.

The first essential missing implication is now:

> **`POS3-CANONICAL-TWO-FORK-SWITCH-CHARGE-v1`.** In the exact two-cover fork of Theorem 3.3, prove that an excursion which alternates between the two sibling covers `s lessdot r_1,r_2` or leaves and later re-enters that fork cannot recycle the two exclusive cross packets `r_1<q<r_2` and `r_2<q<r_1` indefinitely. It must either (i) produce a balanced pair, (ii) produce a strict smaller strong-majority span, (iii) produce a proper autonomous/ordinal reduction, or (iv) charge a genuinely new disjoint full-extension/Hasse packet under a well-founded envelope statistic.

This is strictly narrower than a generic cover-changing/backtrack residual: at the earliest endpoint the outbound degree is exactly two, both cross directions occur in the full law, every surviving witness is after `q`, and any second lower cover is already a descent.

A proof of this two-fork switch-charge lemma, together with the inherited terminal-block barrier and the existing same-cover potentials, would close the earliest-endpoint recycling mechanism. A further global induction must then show that taking the forced descent cannot generate a later incomparable-endpoint cycle outside the improved envelope; that final splice is not claimed here.

## 7. Honest status

- Parent POS3: **OPEN / NOT PROVED**.
- Inherited finite frontier `n_bal=14`: **UNCHANGED**.
- Latest lead account04/B10 earliest-endpoint theorem: **CONSUMED/APPLIED**.
- account04/B20 terminal-block barrier: **CONSUMED/APPLIED**.
- assigned partner account02/B10 exact-backtrack/Hasse leakage: **CONSUMED/APPLIED**.
- account04/B19 one-sided same-cover potentials: **CONSUMED/APPLIED**.
- exact chain-deletion multiplicity recurrence: **RETAINED AND SPECIALIZED TO THE EARLIEST PREFIX CHAIN**.
- two-cover saturation at every undescended terminal-block state: **PROVED**.
- both cross cells nonempty; one channel `>E/6`; endpoint probability `<5/6`: **PROVED**.
- second lower cover of a surviving witness forces strict subspan: **PROVED**.
- bare local-fork closure shortcut: **REFUTED by an exact width-three seven-element example**.
- canonical two-fork switch-charge lemma: **OPEN**.
- run classification: **`ESSENTIAL_STEP_APPLIED`**.

Scoped integrity review: only the named private mathematical repositories, source-bound peer reports, sanitized logical run labels, exact mathematical formulas, and a deterministic standard-library checker were used. No benchmark gold or sealed answers, credentials, scheduler identifiers, machine paths, unrelated private data/transcripts, email/Drive data, public posting, paid model/API/Codex execution, remote workflow, permission bypass, or production-brain mutation was used or claimed.
