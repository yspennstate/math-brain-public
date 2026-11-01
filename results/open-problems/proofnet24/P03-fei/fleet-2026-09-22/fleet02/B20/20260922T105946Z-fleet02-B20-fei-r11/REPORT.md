# fleet02/B20 — diffuse-selector entropy lower bound and exact posterior-refund necessity

**Programme:** `FEI-ALL-TEAM-20260922T095941Z`  
**Assignment:** `FEI-20260922-fleet02-B20` / Path C / Adaptive block entropy cost  
**Run:** `20260922T105946Z-fleet02-B20-fei-r11`  
**Classification:** `ESSENTIAL_STEP_APPLIED / SELECTOR_COST_SHARPENED / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Model self-report:** GPT-5.6 Sol. Maximum useful reasoning requested; configured effort and provider reasoning counters were not exposed.

## 0. Current scope and corrections

The direct owner control `2026-09-22.3` puts all active workers on uniform-cube FEI. Older BT4, installation and benchmark assignments are suspended and are not premises here. Full FEI remains open.

This report uses the candidate-independent Path-C quantities

\[
\mathcal F=H-\mathcal P,\qquad \mathcal J=\sum_i q_i,
\]

and the physical-block quantities from the all-block terminal theorem. For a nonempty physical block `A`,

\[
D_A(f)=\mathcal J(f)-\mathbb E_z\mathcal J(f_z),
\qquad
U_A(f)=\sum_{i\in A}h_2(q_i)-W_A(f),
\]

with

\[
\boxed{\Delta_A\mathcal F(f)\le U_A(f).}\tag{0.1}
\]

Entropy is in bits throughout. The refuted raw-`U4=O(J)`, unweighted-`L2`, fixed-depth-KL and old fixed-quadratic-potential claims are not used. The current correction inbox was empty at the publication preflight.

## 1. Exact source pins

The mathematical premises actually consumed are:

1. **TERMINAL_CORE.** `yspennstate/math-open-problems@85ffa60db26997421d980b1f86c03d82259504ca`, `proofnet24/P03-fei/fleet-2026-09-21/fleet02/B13/20260922T075416Z-all-block-terminal-core/REPORT.md`, especially `D_A=I_A+C_A`, (0.1), and exact telescoping of `D_A` in `J`.
2. **SELECTOR_LEDGER, previous fleet02/B20 run.** `yspennstate/math-open-problems@4a1748352ae7e31c4941f91c3f6a81a5a6928421`, `proofnet24/P03-fei/fleet-2026-09-22/fleet02/B20/20260922T103102Z-fleet02-B20-fei-r17/REPORT.md`: if a selector is source-realizable from a latent source `Theta` and decoded history, then the selector entropy is part of the posterior-information decrement and the refunds telescope.
3. **Newest compatible named-partner result, fleet03/B20.** `yspennstate/math-open-problems@7d31b66c5517b7b491693642c503d29352d8ffb4`, `proofnet24/P03-fei/fleet-2026-09-22/fleet03/B20/20260922T104610Z-terminal-lowJ-diffusion/REPORT.md`. For every centered minimum-dimensional all-block ratio-critical core with `0<J<1`,

\[
\boxed{\max_i\frac{q_i}{J}\le \frac{c_0}{\log_2(1/J)},\qquad c_0:=\frac2{\ln2}.}\tag{1.1}
\]

The same source supplies the genuine one-point-defect calibration

\[
q=2^{1-d},\qquad J=d2^{1-d},\qquad \frac qJ=\frac1d,
\tag{1.2}
\]

and `F/J -> 4-2/ln2 < 2`.

This invocation uses (1.1) quantitatively rather than merely citing the partner report.

## 2. Prior selector theorem, stated at the exact ledger level

At a reached node `v`, let `H_v` be the already decoded physical branch history, `A_v` the next physical block, `Z_v` its uniformly distributed physical assignment, and `w_v` the reach probability. Let a latent source `Theta` be allowed only under the explicit source-realizability condition

\[
H_2(A_v\mid \Theta,H_v)=0.\tag{2.1}
\]

Put

\[
R_v:=H_2(\Theta\mid H_v)
\]

and

\[
\operatorname{ref}_v:=R_v-\mathbb E[R_{\rm child}\mid v]
=I_2(\Theta;A_v,Z_v\mid H_v).\tag{2.2}
\]

Then the exact chain rule gives

\[
\boxed{
\operatorname{ref}_v
=H_2(A_v\mid H_v)+I_2(\Theta;Z_v\mid A_v,H_v)
\ge H_2(A_v\mid H_v).}
\tag{2.3}
\]

Moreover

\[
\boxed{
\sum_v w_v\operatorname{ref}_v
=H_2(\Theta)-\mathbb E H_2(\Theta\mid H_L).}
\tag{2.4}
\]

Thus source information cannot be spent repeatedly. If the block is a deterministic function of the decoded state, then its conditional address entropy is exactly zero; if a hidden/random choice is used, its actual information must appear in (2.3) or as a separate debit.

The new question is quantitative: how large can that debit be in the newly isolated low-`J` diffuse branch?

## 3. New theorem: normalized-influence randomization has a logarithmic-in-log selector bill

Fix a centered minimum-dimensional all-block ratio-critical core satisfying the hypotheses of fleet03/B20 and let

\[
L:=\log_2(1/J)>0,
\qquad
p_i:=\frac{q_i}{J}.
\tag{3.1}
\]

Thus `p=(p_i)` is a probability law on the essential coordinates. Consider the source-realizable or explicitly randomized **influence-proportional index selector**

\[
\Pr[I=i\mid H]=p_i.\tag{3.2}
\]

The exact selection information before any coarsening into blocks is

\[
\boxed{
H_2(I\mid H)=\sum_i\frac{q_i}{J}\log_2\frac{J}{q_i}.}
\tag{3.3}
\]

This is the exact partner expression applied in this run.

Let the physical block queried after selecting `i` be

\[
A=\Phi_H(i),\tag{3.4}
\]

where `Phi_H` is a deterministic map from the selected index and decoded history to a nonempty remaining physical block. Define its label multiplicity

\[
m(H):=\max_a\#\{i:\Phi_H(i)=a\}.\tag{3.5}
\]

### Theorem 3.1 — diffuse-selector entropy lower bound

At every state satisfying the partner hypothesis,

\[
\boxed{
H_2(I\mid H)
\ge
\log_2\!\left(\frac{L}{c_0}\right)
}
\tag{3.6}
\]

whenever `L>c0`, and more generally

\[
\boxed{
H_2(A\mid H)
\ge
\left[\log_2\!\left(\frac{L}{m(H)c_0}\right)\right]_+ .}
\tag{3.7}
\]

Here `[x]_+=max{x,0}`.

#### Proof

By the partner theorem (1.1),

\[
p_i\le \frac{c_0}{L}\quad\text{for every }i.\tag{3.8}
\]

Shannon entropy dominates min-entropy, so

\[
H_2(I\mid H)\ge -\log_2\max_i p_i
\ge \log_2\frac{L}{c_0},
\]

which is (3.6) when its right side is positive.

For a block label `a`,

\[
\Pr[A=a\mid H]
=\sum_{i:\Phi_H(i)=a}p_i
\le m(H)\max_i p_i
\le \frac{m(H)c_0}{L}.\tag{3.9}
\]

Again using Shannon entropy >= min-entropy and truncating the vacuous negative bound at zero proves (3.7). QED.

### Interpretation

In the low-`J` critical branch, `L=log_2(1/J)` diverges. Therefore an influence-proportional selector whose labels have uniformly bounded multiplicity has an address entropy at least

\[
\log_2\log_2(1/J)-O(1).\tag{3.10}
\]

This is an **absolute number of bits**, not an `O(J)` debit. Variable-sized blocks are therefore not intrinsically cheap merely because every normalized influence is small. Diffuseness makes randomized identification more expensive.

Conversely, if one insists on keeping the selector entropy below `b` bits at such a node, (3.7) forces

\[
\boxed{
m(H)\ge \frac{L}{c_0 2^b}.}\tag{3.11}
\]

So a low-information randomized scheme must coalesce at least order `log(1/J)` index choices into the same physical block label, or become deterministic from decoded state.

## 4. Posterior-refund corollary: the required hidden-source consumption is quantitatively large

Assume now that the selector in Theorem 3.1 is source-realizable in the exact sense (2.1). Combining (2.3) with (3.7) yields

\[
\boxed{
\operatorname{ref}_v
\ge
\left[\log_2\!\left(\frac{\log_2(1/J_v)}{m_vc_0}\right)\right]_+}
\tag{4.1}
\]

at every reached node `v` for which the partner's low-`J` critical-core hypothesis is valid.

If a finite restriction tree has a set `V_diff` of such nodes, then the posterior telescope (2.4) gives the exact global constraint

\[
\boxed{
\sum_{v\in V_{\rm diff}} w_v
\left[\log_2\!\left(\frac{\log_2(1/J_v)}{m_vc_0}\right)\right]_+
\le
H_2(\Theta)-\mathbb E H_2(\Theta\mid H_L)
\le H_2(\Theta).}
\tag{4.2}
\]

This is a genuine **nonreuse theorem** for diffuse adaptive choices. It says that repeated randomized low-`J` selections cannot be justified by repeatedly citing the same hidden source: each such choice consumes posterior information, and their reach-probability-weighted bills are bounded by the one root reserve.

Equation (4.2) is conditional only on the nodes to which (1.1) legitimately applies. It does not assert that arbitrary descendants of a critical core remain ratio-critical.

## 5. Exact insertion into the original `F/J` budget

For a finite physical restriction tree, the source block theorem gives, after conditioning on the actual block label,

\[
\mathcal F(f_v)-\mathbb E[\mathcal F(f_{\rm child})\mid H_v]
\le \bar U_v,
\qquad
\bar U_v:=\mathbb E[U_{A_v}(f_v)\mid H_v],\tag{5.1}
\]

and

\[
\bar D_v:=\mathbb E[D_{A_v}(f_v)\mid H_v]
\]

telescopes exactly in folded influence. Hence the already-proved expected-cost theorem remains

\[
\boxed{
\bar U_v+H_2(A_v\mid H_v)-\operatorname{ref}_v
\le K\bar D_v\quad\forall v
}
\tag{5.2}
\]

implies

\[
\boxed{
\mathcal F(f)-\mathbb E\mathcal F(f_L)
+\sum_v w_v\bigl(H_2(A_v\mid H_v)-\operatorname{ref}_v\bigr)
\le K\bigl(\mathcal J(f)-\mathbb E\mathcal J(f_L)\bigr).}
\tag{5.3}
\]

The new contribution is that (4.1) identifies the minimum posterior consumption required by a natural randomized selector in the diffuse critical branch. If `Theta` is an **already admitted** reserve, (2.3) makes the bracket in (5.3) nonpositive and no extra FEI constant is introduced. If `Theta` is an external random seed or otherwise absent from the proof ledger, then its entropy cannot be declared a Path-C credit: the positive address term must stay in (5.2).

For the canonical deterministic rule—choose the first admissible block according to one fixed total order computed from the current restricted Boolean truth table—

\[
H_2(A_v\mid H_v)=0,\qquad \operatorname{ref}_v=0.\tag{5.4}
\]

Thus variable block **size** itself still has zero address cost under the canonical rule. The new theorem does not contradict that fact; it quantifies exactly why hidden/random selection is different.

The physical-coordinate ledger is separate from the address ledger. Querying `A_v` physically fixes `|A_v|` coordinates, but the dimension-independent stopping budget is the actual folded-influence decrement `D_{A_v}`, not raw cardinality or depth. Along each branch no coordinate is physically queried twice, while in expectation the exact quantity paid is the telescope on the right side of (5.3).

## 6. Genuine Boolean calibration: one-point defects refute a free randomized singleton-choice lemma

The partner's one-point-defect family makes the necessity of the selector debit exact rather than asymptotic bookkeeping.

Let `f_d` be `+1` on the `d`-cube except at one point, where it is `-1`. Then every active coordinate has

\[
q=2^{1-d},\qquad J=dq.\tag{6.1}
\]

Choose a singleton block by first taking `I` uniformly from the `d` active coordinates and setting

\[
A=\{I\}.\tag{6.2}
\]

Then

\[
\boxed{H_2(A)=H_2(I)=\log_2 d.}\tag{6.3}
\]

The physical restriction has two branches, each with probability `1/2`. On the branch that misses the exceptional point, the child is constant and has `J=0`. On the branch containing the exceptional point, the child is the `(d-1)`-dimensional one-point defect and has

\[
J_{d-1}=(d-1)2^{2-d}.\tag{6.4}
\]

Therefore, for every singleton coordinate,

\[
\begin{aligned}
D_{\{i\}}
&=d2^{1-d}-\frac12(d-1)2^{2-d}\\
&=2^{1-d}=q.
\end{aligned}\tag{6.5}
\]

Since `I_A=q`, the exact identity `D_A=I_A+C_A` gives

\[
C_{\{i\}}=0,\qquad W_{\{i\}}=0,\qquad
\boxed{U_{\{i\}}=h_2(q).}\tag{6.6}
\]

Hence a proposed no-refund local payment for this randomized singleton step would require

\[
h_2(2^{1-d})+\log_2 d
\le K2^{1-d}.\tag{6.7}
\]

For every fixed finite `K`, (6.7) fails for all sufficiently large `d`; indeed the left side is at least `log_2 d` while the right side tends to zero. In particular, even the weaker universal claim

\[
H_2(A)\le K D_A\tag{6.8}
\]

is false on this genuine Boolean family.

This is **not an FEI counterexample**. The same partner report shows `F/J -> 4-2/ln2 <2` for this family. It is a counterexample only to a claimed free/random block-choice step.

The refund ledger is exact here. If a latent selector source `Theta=I` is admitted, then `A` determines `I`, while the physical branch bit is uniform once the chosen coordinate is known. Thus

\[
\operatorname{ref}=I_2(I;A,Z)=H_2(I)=\log_2d,\tag{6.9}
\]

so the selector debit in (6.3) is canceled **exactly once**. What remains is the genuine block-affordability issue `h_2(q)` versus `Kq`; the refund does not fake a good block. This cleanly separates the two Path-C obligations.

## 7. What changed and what remains unpaid

### Before

The previous B20 run proved the exact posterior-refunded selector theorem and showed that a canonical deterministic variable-block rule has zero address entropy. It did not have the newly completed fleet03/B20 low-`J` result, so it did not quantify the entropy of natural randomized selectors in the diffuse terminal branch.

### After

The named partner theorem now yields the exact normalized-influence entropy expression (3.3), the critical-core lower bounds (3.6)--(3.7), and the global nonreuse inequality (4.2). A genuine Boolean one-point-defect family gives an exact falsifier (6.7) to any attempt to charge randomized singleton identity for free or solely by a fixed multiple of the same physical `D_A` decrement. Posterior refund cancels the address entropy exactly but does not solve block affordability.

Thus the variable-sized selector issue is now resolved at a sharper scope:

* **decoded-state deterministic selection:** exact address cost `0`;
* **hidden source-realizable selection:** exact entropy debit, covered only by the corresponding posterior decrease, with no reuse;
* **external/unadmitted randomization:** not free, and can cost `log d` bits while physical `D_A` tends to zero;
* **low-`J` diffuse influence-proportional selection:** costs at least `log log(1/J)-O(1)` bits unless many indices coalesce to the same block label.

### First unpaid implication

The remaining Path-C obstruction is not block-label entropy. It is the mathematical existence/nonreuse of **affordable physical blocks** or direct control of every all-block terminal ratio-critical core. In the low-`J` branch isolated by fleet03/B20, the one-point-defect calibration also shows why singleton `h_2(q)` costs may be much larger than `q`: the next mechanism must exploit nonlocal Boolean structure, multiscale grouping, or a pre-existing information reserve without repeated spending.

A useful next target for recipient `fleet04/B19` is therefore:

> On a minimum-dimensional all-block ratio-critical core satisfying the low-`J` diffusion bound, construct a deterministic decoded-state block selector (hence zero address entropy) whose block charge obeys `U_A <= K D_A`, or prove a direct terminal inequality `F<=KJ`; randomized influence-proportional row choice cannot be used as a free substitute.

**Full uniform-cube FEI remains OPEN / NOT PROVED.**
