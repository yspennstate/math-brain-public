# POS3 account02/B10 — canonical common-lower Y-gate and strict reverse-channel contraction

**Run:** `20260922T094758Z-account02-B10-8830fb0f`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has incomparable `x,y` with `1/3 <= Pr(x<y) <= 2/3` under the uniform law on all full linear extensions.  
**Parent status:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

All probabilities and counts below refer to the original uniform law on all full linear extensions of the original poset. Deletion skeletons are only an exact partition of that full extension set; no induced deletion law is declared uniform.

## 1. Fresh source-bound state consumed

Fresh owner control was resolved from `yspennstate/math-research-brain` at initial main commit `3f0819aa148231b1d88aa8bdaefdfb65a42c2eec`, control revision `2026-09-22.2`. It keeps account02/B10 on POS3 and stops the old installation/benchmark duties.

The newest complete campaign-lead report read before the derivation is:

- **account04/B10**, run `20260922T091028Z-account04-B10-pos3-r11`, `REPORT.md` blob `8a856fa924002567c01a8b70880003fe53b86da3`.

Its new canonical selection is crucial here. In a hypothetical no-balanced counterexample the strong-majority relation `prec_*` is a strict total order. Choose an oriented incomparable pair `p||q`, `p prec_* q`, with `rho(q)` minimum, and then `rho(p)` minimum among incomparable predecessors of that same `q`. The lead proves that the first transposition export either immediately gives strict strong-majority span descent or enters a heavy bridge which itself must expose such a descent; it leaves `POS3-EARLIEST-BARRIER-DESCENT-SPLICE-v1` as the first global unpaid splice.

The required named partner result read and applied is:

- **account03/B11**, run `20260922T081117Z-account03-B11-pos3-r11d`, `REPORT.md` blob `56374ff9d4b1bf188929919d05e52b34c00868b6`.

It proves the exact full-extension factor-two identity for an incomparable pair whose only two distinguishers form a comparable positive upper chain, and its order-dual lower-chain identity. I apply those identities below to the fresh sibling pair emitted by the canonical gate.

Two previous account02/B10 exact results are also used:

- endpoint blocker-product / two-channel theorem, `proofnet24/collective-POS3/account02/B10/20260922T014627Z-account02-B10-pos3-r12/REPORT.md`, blob `acdb868b3e35a9248d494126311bfff3bfee150b`;
- one-distinguisher balance theorem, `proofnet24/collective-POS3/account02/B10/B10-20260922T024630Z-pos3-r13/REPORT.md`, blob `e91498f0bb8e28f23aa1cada24e131c27182e0ff`.

## 2. Compact conditional end-to-end route

Assume for contradiction that `P` is a finite width-at-most-three nonchain with no balanced pair. Start from the lead's canonical earliest-ending pair `(p,q)`.

The intended splice is now:

1. prove that the canonical choice makes `p,q` **common-lower twins**, `Pred(p)=Pred(q)`;
2. exploit that equality to retain every deletion-fiber multiplicity and obtain an exact signed upper-slack formula for the endpoint transposition;
3. show that if the first canonical state has no already-authorized strict span descent, then its outgoing endpoint defect is forced through **exactly two** incomparable upper Hasse covers of `p` while the reverse endpoint defect has **at most one** Hasse cover of `q`;
4. show that this possible unique reverse channel is quantitatively contracted: its minority probability is strictly smaller than the original canonical minority by more than the original distance from `1/3`;
5. use the two outgoing covers as a fresh width-saturating sibling fork. The partner factor-two theorem eliminates the comparable two-positive-upper and comparable two-positive-lower minimum-support branches unless strict span descent has already occurred.

Steps 1-5 are proved here. The remaining global issue is to show that later ray migration cannot bypass this one-in/two-out gate and return through a different noncanonical corridor indefinitely.

## 3. Canonical earliest pair has identical strict predecessor sets

### Lemma 3.1 — common-lower twins

For the lead's canonical pair `(p,q)`,

`Pred(p)=Pred(q)`.                                               (3.1)

**Proof.** Suppose first that `z<p` but `z` is not below `q`. Since `p||q`, transitivity forbids `q<z<p`, so `z||q`. The forced order `z<p` gives

`z prec_* p prec_* q`.

Thus `(z,q)` is an incomparable pair with the same right endpoint `q` but `rho(z)<rho(p)`, contradicting the leftmost choice of `p`.

Conversely suppose `z<q` but `z` is not below `p`. Transitivity forbids `p<z<q`, so `z||p`. Both `z` and `p` lie strictly before `q` in the strong-majority total order. Hence the later endpoint of the incomparable pair `{z,p}` has rank strictly below `rho(q)`, contradicting the earliest-ending choice of `q`. This proves (3.1). `square`

This strengthens the lead's Hasse-level statement `D(p,q)=emptyset`: **all** lower relation distinguishers of the canonical pair are absent.

## 4. Exact common-lower deletion-fiber identity

The next lemma is arbitrary-size and uses no width assumption.

Fix any incomparable `p,q` with `Pred(p)=Pred(q)`. Let `tau` be a linear extension of `P\{p,q}`. Legal insertion slots for either deleted vertex form intervals. Equality of predecessor sets makes their lower endpoint identical. Write

`I_p(tau)=[L,U_p]`, `I_q(tau)=[L,U_q]`,

and let

`a=U_p-L+1`, `b=U_q-L+1`.

Every lift is represented by one base slot for `p`, one for `q`, with both orders allowed when the two vertices occupy the same base gap.

If `b>=a`, exact counting gives

`C_tau(p<q) = ab-a(a-1)/2`,

`C_tau(q<p) = a(a+1)/2`.

If `a>=b`, the order-dual formulas give

`C_tau(p<q) = b(b+1)/2`,

`C_tau(q<p) = ab-b(b-1)/2`.

Therefore in every skeleton

`Delta_tau := C_tau(p<q)-C_tau(q<p)`

satisfies the single formula

`Delta_tau = min(a,b) (b-a)`.                                  (4.1)

No skeleton weight has been altered.

There is also an exact swap interpretation. When `b>a`, the `Delta_tau=a(b-a)` surplus lifts are precisely the rectangle in which `p` uses one of its `a` common slots while `q` uses one of its `b-a` extra right-hand slots. Endpoint-position transposition fails exactly on that rectangle. When `a>b`, the symmetric rectangle is the reverse/incoming defect. Summing (4.1) over the actual skeleton set gives the full-law identity

`M-N = O-I`,                                                    (4.2)

where `M=N(p<q)`, `N=N(q<p)`, and `O,I` are the outgoing and incoming illegal endpoint swaps.

This is the assigned coupling with every conditioning multiplicity retained.

## 5. Exact Hasse event realization of both defect signs

Define the exclusive upper Hasse families

`U_p(q)={r : p lessdot r, r||q}`,

`U_q(p)={s : q lessdot s, s||p}`.

Because (3.1) removes every lower distinguisher, the endpoint defects are exactly

`O = #{L : r<q for at least one r in U_p(q)}`,                  (5.1)

`I = #{L : s<p for at least one s in U_q(p)}`.                  (5.2)

For (5.1), `r<q` implies `p<r<q`, so swapping the endpoint positions violates `p<r`. Conversely, any outgoing failure has a successor of `p` between `p,q`; descending to a minimal such successor produces an element of `U_p(q)` still lying before `q`. Equation (5.2) is the order-swapped argument.

Every two distinct members of `U_p(q)` are incomparable, and each is incomparable with `q`; hence width three gives

`|U_p(q)|<=2`.                                                  (5.3)

Likewise `|U_q(p)|<=2`.

More is true when the outgoing side is full. If

`U_p(q)={r_1,r_2}`

and `U_q(p)` contained two vertices `s_1,s_2`, then all four `r_1,r_2,s_1,s_2` would be pairwise incomparable. The same-side pairs are incomparable because they are distinct covers of the same endpoint. For a cross pair, `r_i<s_j` would imply `p<s_j`, contradicting `s_j||p`, while `s_j<r_i` would imply `q<r_i`, contradicting `r_i||q`. Thus width three forces

`|U_p(q)|=2  =>  |U_q(p)|<=1`.                                 (5.4)

This is the one-in/two-out Hasse geometry.

## 6. Canonical Y-gate theorem

Assume now the no-balanced hypothesis and exclude an already-authorized strict strong-majority subspan from `(p,q)`. Put

`epsilon = Pr(q<p) < 1/3`.

For every `r in U_p(q)`, the forced relation `p<r` gives `p prec_* r`. If `r prec_* q`, then

`p prec_* r prec_* q`

and `(r,q)` is a strict incomparable subspan of `(p,q)`. Hence in the live no-descent branch every outgoing cover satisfies

`q prec_* r`, so `Pr(r<q)<1/3`.                                (6.1)

Since `Pr(p<q)>2/3`, (4.2) gives

`O-I = E(1-2epsilon) > E/3`,

and therefore `O>E/3`. If `|U_p(q)|<=1`, (5.1) and (6.1) would give `O<E/3`, a contradiction. Combining with (5.3):

### Theorem 6.1 — forced double outgoing fork

In the live canonical no-descent branch,

`U_p(q)={r_1,r_2}`                                             (6.2)

with

`p lessdot r_1,r_2`,

`q||r_1,r_2`,

`r_1||r_2`,

and `q prec_* r_i` for both `i`.

Thus `{q,r_1,r_2}` is a width-saturating three-antichain. By (5.4), the reverse family has size at most one.

The earlier B10 blocker-product theorem applies because `Pred(p)=Pred(q)`. It gives

`Pr(p<q) <= 1 - (1/2) Pr(q<r_1)Pr(q<r_2) < 7/9`,

so the canonical minority is not arbitrarily small:

`epsilon > 2/9`.                                                (6.3)

### Theorem 6.2 — strict reverse-channel contraction

If `U_q(p)=emptyset`, then `I=0` and the gate is genuinely one-way at endpoint-transposition level.

If instead

`U_q(p)={s}`,

then (5.2) is exactly the single incomparable-pair minority event

`I/E = Pr(s<p) =: delta`.                                      (6.4)

The no-balanced total order has `p prec_* q prec_* s` because `q<s` is forced; therefore `delta<1/3`.

Let

`alpha_i=Pr(r_i<q)<1/3`.

From (5.1),

`O/E = Pr(r_1<q or r_2<q) <= alpha_1+alpha_2 < 2/3`.            (6.5)

Combining (4.2), (6.4), and (6.5) yields

`1-2epsilon+delta < 2/3`,

hence the exact strict contraction

`delta < 2epsilon - 1/3 < epsilon`.                             (6.6)

Equivalently,

`epsilon-delta > 1/3-epsilon > 0`.                             (6.7)

So the only possible reverse Hasse channel at the canonical earliest barrier carries a pair whose minority mass is strictly smaller than the original canonical minority, with a loss exceeding the original distance to the balancing threshold. This is an exact full-law return tax, not a statement about a projected distribution.

## 7. Fresh sibling fork and direct application of account03/B11 r11d

The two outgoing covers are siblings:

`p lessdot r_1,r_2`, `r_1||r_2`.

Neither old endpoint distinguishes them: `p` lies below both and `q` is incomparable with both. Therefore every relation distinguisher of the new pair `r_1||r_2` lies outside the four-point core `{p,q,r_1,r_2}`.

In a no-balanced candidate this sibling pair cannot have zero distinguishers (label symmetry gives `1/2`) and cannot have exactly one, by the already-proved B10 one-distinguisher theorem. Hence it emits at least two genuinely fresh external distinguisher channels.

Orient it `r_1 prec_* r_2`. The named partner account03/B11 r11d now removes two minimum-support geometries unless span descent has already occurred.

- If its only two distinguishers are a comparable positive upper chain `r_1<u<v`, `r_2||u,v`, then absence of a strict subspan forces `r_2 prec_* u`; otherwise `r_1 prec_* u prec_* r_2` and `(u,r_2)` is a strict subspan. Partner r11d gives
  `N(r_2<u)=2N(r_2<r_1)<2E/3`, contradicting `r_2 prec_* u`.
- Dually, if the only two distinguishers are a comparable positive lower chain `u<v<r_2`, `r_1||u,v`, then absence of a strict subspan forces `v prec_* r_1`. Partner r11d gives
  `N(v<r_1)=2N(r_2<r_1)<2E/3`, contradicting `v prec_* r_1`.

Thus the first canonical Y-gate cannot continue span-exhaustedly through either comparable two-positive-chain sibling-support pattern. Remaining sibling-support geometries are genuinely narrower: mixed-sign, same-sign incomparable, or at least three distinguishers.

## 8. A stronger tempting claim is false

It is tempting to strengthen Theorem 6.1 to say that the reverse family `U_q(p)` must be empty. That is false even under all of the local probability inequalities used above.

The committed verifier contains the width-three eight-point poset with Hasse covers

`(0,3),(0,5),(1,3),(1,6),(2,4),(2,5),(4,7),(5,6)`.

For `p=2`, `q=1` it has `E=360` full linear extensions,

`Pred(p)=Pred(q)=emptyset`,

`U_p(q)={4,5}`, `U_q(p)={3}`,

`N(p<q)=243`, `N(q<p)=117`,

`N(q<4)=246`, `N(q<5)=288`,

and

`N(3<p)=12`.

Thus `p<q`, `q<4`, and `q<5` are all strictly above `2/3`, while a genuine unique reverse channel exists. Exact endpoint defects are `O=138`, `I=12`, and indeed

`O-I=126=M-N`.

The contraction is very strong in this calibration: `delta=12/360`, `epsilon=117/360`. The poset is **not** a POS3 counterexample; for example `(0,1)` is balanced with counts `(216,144)`. The example only refutes the stronger auxiliary assertion `U_q(p)=emptyset`.

## 9. Exact regression

`verify_canonical_y_gate.py` is a deterministic standard-library checker. It exhausts naturally labelled transitive closures through `n=6`, keeps width at most three, and checks:

- the common-lower deletion-fiber formulas and `Delta_tau=min(a,b)(b-a)` on every tested skeleton;
- `O-I=M-N` from the exact outgoing/reverse Hasse events;
- the forced two-out / at-most-one-reverse structure in every local strong no-descent gate;
- the contraction inequality whenever the reverse channel is present;
- the fixed eight-point calibration above.

Captured output:

```text
unique_n2_to_n6 {2: 2, 3: 7, 4: 40, 5: 357, 6: 4824}
width_le_3_posets_n2_to_n6 3701
common_predecessor_ordered_pairs 17400
exact_deletion_fibers_checked 96080
canonical_local_gate_cases 228
two_out_one_reverse_structural_pairs 401
calibration_covers [(0, 3), (0, 5), (1, 3), (1, 6), (2, 4), (2, 5), (4, 7), (5, 6)]
calibration_E_M_B 360 243 117
calibration_out_covers_reverse_cover [4, 5] [3]
calibration_q_before_outcovers [246, 288]
calibration_reverse_minority 12
calibration_O_I 138 12
calibration_balanced_escape_first (0, 1, 216, 144)
POS3_CANONICAL_Y_GATE_CHECK_PASS
```

This finite computation is regression/calibration only. The lemmas and inequalities in Sections 3-7 are arbitrary-size exact arguments.

## 10. What moved and first unpaid implication

The lead's earliest barrier is now an exact **one-in/two-out Y-gate**:

- all lower relation distinguishers of `(p,q)` vanish, not just lower Hasse witnesses;
- every deletion fiber is nested at the common lower endpoint and has the exact defect `min(a,b)(b-a)`;
- absent immediate span descent, exactly two outgoing upper Hasse covers exist;
- width three permits at most one reverse upper Hasse cover;
- that reverse channel, when present, has strict minority contraction `delta < 2epsilon-1/3 < epsilon`;
- the two outgoing covers form a fresh sibling fork with at least two external distinguishers, and partner r11d removes the comparable two-positive-chain minimum-support cases.

The new first unpaid implication is:

> **`POS3-CANONICAL-Y-GATE-SPLICE-v1`.** Show that after leaving the earliest Y-gate through one of its two outgoing sibling channels, every later attempt to migrate back across the earliest barrier can be charged either to the unique contracted reverse reservoir `Pr(s<p)=delta`, to a strict strong-majority span descent, or to a fresh sibling-distinguisher branch; prove that the same full-extension mass cannot be re-used indefinitely across different noncanonical gates. A successful charge accounting would make the lead's earliest barrier globally well founded. The remaining unresolved sibling cases are mixed-sign, same-sign incomparable, or at least-three-distinguisher support.

I do not claim that splice here. POS3 remains open.

## 11. Integrity

Run classification: **`ESSENTIAL_STEP_APPLIED`**. The stronger auxiliary assertion that the reverse Hasse family is always empty is **refuted** by the exact 360-extension calibration, but the POS3 target is not refuted.

Scoped provenance/privacy review: only the two authorized private mathematical repositories, source-bound peer reports, exact finite poset data, and deterministic standard-library computation were used. No benchmark gold or sealed-answer material, credentials, scheduler identifiers, machine paths, unrelated private data/transcripts, email/Drive data, public posting, paid API/model/Codex execution, remote workflows, permission bypass, or production-brain mutation is included.
