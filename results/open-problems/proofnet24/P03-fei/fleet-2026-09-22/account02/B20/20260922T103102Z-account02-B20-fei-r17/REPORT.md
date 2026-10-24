# account02/B20 — adaptive block entropy cost and posterior-refunded selector theorem

**Programme:** `FEI-ALL-TEAM-20260922T095941Z`  
**Assignment:** `FEI-20260922-account02-B20` / Path C / Adaptive block entropy cost  
**Run:** `20260922T103102Z-account02-B20-fei-r17`  
**Classification:** `ESSENTIAL_STEP_APPLIED / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  

## 0. Owner correction and scope

The later direct owner control `2026-09-22.3` supersedes this worker's preceding BT4 assignment. No new BT4 work is used here. Full uniform-cube FEI remains open. I use the current Path-C objects

\[
\mathcal F=H-\mathcal P,\qquad \mathcal J=\sum_iq_i,
\]

and the source-valid block quantities of the terminal-core theorem. For a nonempty physical block `A` at a centered Boolean state `f`,

\[
D_A(f)=\mathcal J(f)-\mathbb E_z\mathcal J(f_z),
\]
\[
U_A(f)=\sum_{i\in A}h_2(q_i)-W_A(f),
\]

with the proved local inequality

\[
\Delta_A\mathcal F(f):=\mathcal F(f)-\mathbb E_z\mathcal F(f_z)\le U_A(f). \tag{0.1}
\]

The physical child `z` is uniform on the queried coordinates. The current source also proves that if a stopping tree always queries a block with `U_A<KD_A`, then the `D_A` charges telescope exactly in `J`; no raw-depth or ambient-dimension charge may be inserted.

The all-team correction bundle was consumed through state revision `FEI-20260922T1000Z-v1`. In particular the old coefficient `0.337`, the `0.34` quadratic repair, raw `U4=O(J)`, full unweighted-convolution `L2`, and fixed/low-depth KL extraction are not premises. The arbitrary global safe-cone selector floor is `NEEDS_REVALIDATION`, so no local nonnegativity is inferred by deleting child slack.

## 1. Source pins and partner status

The exact premises used are:

1. **TERMINAL_CORE**, `yspennstate/math-open-problems@85ffa60db26997421d980b1f86c03d82259504ca`, `proofnet24/P03-fei/fleet-2026-09-21/account02/B13/20260922T075416Z-all-block-terminal-core/REPORT.md`, especially (2.6) and Theorem 3.1: (0.1) and the exact `J` telescope.
2. **SELECTOR_DEBIT**, `@4ccd51ad517f425a529daa52c3352905b86ea69d`, `proofnet24/P03-fei/fleet-2026-09-21/account02/B12/20260922T091546Z-uniform-selector-debit-and-safe-lift/REPORT.md`, Sections 2--4 only: the source-exact conditional Shannon debit and preservation of child defects. Its Section 5 candidate `c=0.337` is refuted and not used.
3. **ROBUST_ROW**, `@fdbfbcc1beed0db4cb6d13c8d61fd92db53a8113`, `proofnet24/P03-fei/fleet-2026-09-21/account04/B12/20260922T081051Z-terminal-trigger-surplus/REPORT.md`: actual trigger blocks carry influence-relative surplus, but their shared-use payment remains open.
4. **Compatible completed other-account block result:** account03/B18, `yspennstate/math-open-problems@730731281a24e70b01b4021a90ff758575414db1`, `proofnet24/P03-fei/fleet-2026-09-21/account03/B18/20260921T100020Z-block-selector-compiler/REPORT.md`. I use its exact lifetime identity
   \[
   \sum_vw_v I_{A_v}(f_v)=I(f)-\mathbb E I(f_L) \tag{1.1}
   \]
   and the fact that an adaptive proper-block tree incurs no additional *influence* lifetime term once each local block is paid.

The named partner is account03/B20. At the fresh all-team snapshot its current card is `FEI-20260922-account03-B20`, “Terminal exceptional branch removal”. No completed all-team account03/B20 handoff was available in the shared handoff location when checked. The newest completed account03/B20 result found before this reallocation is an MOC4 report and is mathematically incompatible with FEI block selection (complex-normal determinant/permanent geometry, no Boolean restriction/F/J quantity). I therefore did not import it. Work continues asynchronously from the compatible completed account03/B18 block theorem above, as the memory protocol permits when a named partner has not yet delivered a compatible completed snapshot.

## 2. The precise unpaid selector issue

The all-block compiler proves an expected `F/J` telescope once a block has been chosen, but an implementation can accidentally introduce a new random variable: the **identity/size of the chosen block**. A statement such as “choose whichever trigger block is best” is not automatically a free code. If the block label is randomized or depends on hidden source information unavailable to the decoder, its Shannon information must be either

* zero because the block is reconstructible from the already known branch state; or
* explicitly paid; or
* charged to an already-accounted posterior information reserve, with the corresponding posterior refund retained.

The theorem below gives the exact ledger. It is deliberately abstract enough to cover variable block sizes, but its application to the Path-C stopping tree is source-exact and uses only physical restrictions.

## 3. Adaptive selector ledger

Consider a finite physical restriction tree. At a reached internal node `v` let `\mathscr H_v` denote the entire already decoded branch history. The current Boolean function `f_v` is deterministic from the root truth table and `\mathscr H_v`. Before revealing the next physical block assignment, a selector chooses a nonempty remaining block `A_v`; then the uniform physical assignment on `A_v` is revealed and the process moves to a child. Let `w_v` be the reach probability.

Allow first a hidden source variable `Theta` used by the selector. The admissible **source-realizable** hypothesis is

\[
H_2(A_v\mid \Theta,\mathscr H_v)=0. \tag{3.1}
\]

Thus there is no external randomness in the choice once the source and branch history are known. Put

\[
R_v:=H_2(\Theta\mid\mathscr H_v), \tag{3.2}
\]

and, writing `Z_v` for the physical child assignment,

\[
\operatorname{ref}_v
:=R_v-\mathbb E[R_{\mathrm{child}}\mid v]
=I_2(\Theta;A_v,Z_v\mid\mathscr H_v). \tag{3.3}
\]

This is a genuine posterior-information decrement; it may be spent only when `R` is an already admitted source reserve in the proof ledger. It is not manufactured credit.

### Lemma 3.1 — exact selector debit is covered by its posterior refund

Under (3.1),

\[
\boxed{H_2(A_v\mid\mathscr H_v)\le \operatorname{ref}_v.} \tag{3.4}
\]

More exactly,

\[
\operatorname{ref}_v
=H_2(A_v\mid\mathscr H_v)
 + I_2(\Theta;Z_v\mid A_v,\mathscr H_v). \tag{3.5}
\]

**Proof.** By the mutual-information chain rule,

\[
I(\Theta;A_v,Z_v\mid\mathscr H_v)
=I(\Theta;A_v\mid\mathscr H_v)
 +I(\Theta;Z_v\mid A_v,\mathscr H_v).
\]

Because `A_v` is a deterministic function of `(Theta,mathscr H_v)`,

\[
I(\Theta;A_v\mid\mathscr H_v)
=H(A_v\mid\mathscr H_v)-H(A_v\mid\Theta,\mathscr H_v)
=H(A_v\mid\mathscr H_v).
\]

This proves (3.5), hence (3.4). QED.

The point is that selection information is not “free”; it is exactly visible as a part of a source posterior decrement. If that reserve is already present in the proof state, retaining the refund prevents double payment.

### Lemma 3.2 — posterior refunds telescope exactly

For any finite tree satisfying the posterior interpretation in (3.2),

\[
\boxed{
\sum_{v\text{ internal}}w_v\operatorname{ref}_v
=H_2(\Theta)-\mathbb E H_2(\Theta\mid\mathscr H_L).
} \tag{3.6}
\]

**Proof.** Multiply `R_v-E R_child` by `w_v` and sum. Each internal child posterior appears once with positive weight as its own `R_v` and once with negative weight from its parent. Only the root and leaves remain. QED.

Thus a source reserve cannot be reused at many block choices: its refund bank has an exact one-time telescope.

## 4. Main theorem — expected cost of variable-sized physical blocks

At node `v`, condition on the history and possibly on a random source-realizable block choice. Let

\[
\bar U_v:=\mathbb E[U_{A_v}(f_v)\mid\mathscr H_v],\qquad
\bar D_v:=\mathbb E[D_{A_v}(f_v)\mid\mathscr H_v]. \tag{4.1}
\]

### Theorem 4.1 — adaptive block cost with selection debit and posterior refund

Suppose every reached internal node obeys

\[
\boxed{
\bar U_v
+H_2(A_v\mid\mathscr H_v)
-\operatorname{ref}_v
\le K\bar D_v.
} \tag{4.2}
\]

Then

\[
\boxed{
\mathcal F(f)-\mathbb E\mathcal F(f_L)
+\sum_vw_v\bigl[H_2(A_v\mid\mathscr H_v)-\operatorname{ref}_v\bigr]
\le
K\bigl(\mathcal J(f)-\mathbb E\mathcal J(f_L)\bigr).
} \tag{4.3}
\]

In particular, if the choice is source-realizable and the posterior reserve `R` in (3.2) is an already admitted proof reserve, (3.4) makes the bracket nonpositive. No additional selector entropy beyond the original `F/J` payment is required.

**Proof.** Conditional on `A_v=A`, the source block inequality (0.1) gives

\[
\mathcal F(f_v)-\mathbb E[\mathcal F(f_{v,Z})\mid A_v=A,\mathscr H_v]\le U_A(f_v).
\]

Average over `A_v` and add the local selector debit minus refund. By (4.2),

\[
\mathcal F(f_v)-\mathbb E[\mathcal F(f_{child})\mid v]
+H(A_v\mid\mathscr H_v)-\operatorname{ref}_v
\le K\bar D_v. \tag{4.4}
\]

Multiply by `w_v` and sum. The `F` terms telescope on the restriction tree. Since `D_A=J(f_v)-E_zJ(f_{v,z})` for every physical block, the random-block average also telescopes exactly:

\[
\sum_vw_v\bar D_v=J(f)-EJ(f_L). \tag{4.5}
\]

Substitution gives (4.3). QED.

### Corollary 4.2 — canonical variable-sized selector has exactly zero address cost

At any node for which at least one block satisfies `U_A<KD_A`, fix once and for all a deterministic total order on finite coordinate subsets and choose

\[
A^*(f_v)=\text{the first block minimizing }(U_A-KD_A,|A|,\text{coordinate mask})
\]

among blocks with negative slack. Because `f_v` is completely determined by the root function and the previously revealed physical branch history,

\[
\boxed{H_2(A^*(f_v)\mid\mathscr H_v)=0.} \tag{4.6}
\]

Taking a trivial `Theta` gives `ref_v=0`. Therefore variable block size and block identity add **no address entropy at all**, and

\[
\boxed{
\mathcal F(f)-\mathbb E\mathcal F(f_L)
<K\bigl(\mathcal J(f)-\mathbb E\mathcal J(f_L)\bigr)\le K\mathcal J(f).
} \tag{4.7}
\]

This is not an informal “the decoder can probably infer the block” claim: (4.6) is the exact conditional-entropy statement. The block is a deterministic branch-state function.

### Corollary 4.3 — randomized trigger-row selection is not free unless its information source is in the ledger

Suppose a robust-row routine first chooses an index `I_v`, then queries the actual trigger block `F_{I_v}`. If `I_v` is the deterministic first qualifying row computed from `f_v`, then `H(F_{I_v}|mathscr H_v)=0` even though `|F_{I_v}|` varies. If instead `I_v` is randomized from information not contained in the decoded branch state, the local cost includes

\[
H_2(F_{I_v}\mid\mathscr H_v)\le H_2(I_v\mid\mathscr H_v). \tag{4.8}
\]

It may be removed only by identifying a source variable `Theta` satisfying (3.1) and retaining its posterior refund (3.3), or by separately proving a direct `J` payment for (4.8). External random seed entropy is not a Path-C credit.

This gives a clean interface to ROBUST_ROW: its trigger-surplus theorem can determine *which blocks are admissible*, while the present theorem says how the adaptive block label itself is accounted for without introducing a raw `|F_i|`, `log n`, or depth charge.

## 5. Application of the compatible account03 block theorem

The account03/B18 theorem proves both an exact physical influence telescope (1.1) and the selector compiler based on a local inequality `B_A<=K I_A`. The same address accounting applies verbatim to that older `H/I` compiler:

* choose the first proper block minimizing `(B_A-KI_A,|A|,mask)` among admissible blocks;
* then the block label has conditional entropy zero;
* account03/B18's exact identity (1.1) pays the accumulated physical influence once;
* no `log(number of admissible blocks)` term and no variable-size penalty appears.

This is the exact expression from a completed other-account result used here: the right side of the adaptive lifetime bill is `I(f)-E I(f_L)`, not raw depth or the sum of block cardinalities. The present Path-C theorem is its `F/J` analogue with the additional posterior-refund ledger for source-dependent choices.

## 6. Why this is not circular and what remains unpaid

The result does **not** prove that every nonterminal Boolean state possesses a block with `U_A<KD_A`. The terminal-core theorem says that a minimum-dimensional ratio obstruction can instead be terminal for every block. Nor does this report prove `F<=KJ` on that terminal class. Those are the genuine Path-C mathematical obstacles.

What is removed is a separate bookkeeping objection:

> once a realizable good block exists, allowing its size and identity to depend adaptively on the already decoded physical branch does not require a new dimension-dependent entropy payment.

A block selector based on hidden information is also permitted, but its exact selection information must be debited and its posterior source decrease retained. Equations (3.5), (3.6), and (4.3) prevent both free hidden choices and repeated spending of the same information.

This distinction matters for the robust-row route. ROBUST_ROW shows that actual trigger blocks carry enough terminal surplus locally but leaves a global reuse issue. The present theorem says one should not add a second, artificial “which trigger block?” entropy loss when a canonical rule is used. The remaining obstruction is therefore genuinely the nonreuse/availability of the *surplus itself*, not the variable block address.

## 7. Conditional end-to-end Path-C argument after this step

A complete Path-C proof would now be:

1. use the all-block stopping inequality `Delta_A F<=U_A` and the exact `D_A` influence loss;
2. prove that every nonterminal source state has a physical block satisfying the local paid inequality, or else show every all-block-terminal ratio-critical core obeys `F<=KJ` for one finite `K`;
3. choose blocks canonically as in Corollary 4.2 (or use Theorem 4.1 with a genuinely source-backed posterior reserve), so variable block identity/size introduces no unpaid entropy;
4. telescope `F` and `J`, and apply the source phase cap to recover a finite FEI constant.

Step 3 is now discharged under explicit selector hypotheses. Step 2 remains the first essential universal gap.

## 8. Outcome and next derivation

**Outcome:** `ESSENTIAL_STEP_APPLIED`. Full FEI is still **OPEN / NOT PROVED**.

**Target-level movement:** none; no universal constant for all Boolean functions is proved.

**Mechanism movement:** the variable-block selector ledger is closed under an explicit, checkable hypothesis. A canonical branch-state selector has exactly zero conditional address entropy. More generally, a source-realizable hidden selector has selection cost exactly embedded in a posterior mutual-information decrement, and those refunds telescope without reuse.

**First unpaid implication:** turn the robust-row/critical-core structural information into existence of an affordable physical block or a terminal-class bound `F<=KJ`; specifically, prevent shared trigger-surplus from being requested by many robust rows without either a paid canonical block or a compensating source reserve. A productive next attack is to combine the surplus-weighted depth bank from ROBUST_ROW with a canonical first-row/first-scale selector and test whether its source-visible posterior polarization gives an actual `D_A`-relative payment. If not, construct an explicit ratio-critical Boolean family demonstrating the missing nonreuse hypothesis.
