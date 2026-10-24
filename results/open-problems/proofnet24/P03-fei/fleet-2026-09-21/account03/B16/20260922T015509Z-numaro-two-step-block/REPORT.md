# account03/B16 — exact two-step signed block refund on the 18-input Numaro gate

**Outcome:** `AUXILIARY_ONLY` (the named finite obstruction is resolved); **full uniform-cube FEI remains OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`. Authenticated repository sources were read through the GitHub connector, but no authenticated mathematical-brain retrieval/receiver context was used.  
**Owner-control revision:** `2026-09-22.2`. The live natural-language owner message supersedes the older Campaign-C assignment and directs all FEI workers to converge on the all-gate reformulation.  
**Novelty/publication:** not assessed. The 18-input gate is inherited external/source-bound material; no priority claim is made.

## 1. Version, old missing implication, and peer artifact consumed

The live gate reformulation is

\[
\Gamma(p_{\rm out})+H_t(G;p)
\le
\sum_i \operatorname{It}_i(G;p)
\frac{\Gamma(p_i)+h(V_{p_i})}{V_{p_i}},
\qquad
V_p=4p(1-p).
\tag{1.1}
\]

The old read-once-potential claim that the maximal required gate margin is attained by a decomposable/AND gate is already **REFUTED** by compatible completed workers. In particular, the source-bound balanced 18-input Numaro gate has
\[
I=\frac{261}{128},
\qquad
\frac{H}{I-1}=6.521845710923046575\ldots,
\]
which at the old base \(C_0=6.4548\) asks for
\[
c_G=4\!\left(\frac{H}{I-1}-C_0\right)
\ge 0.2681828436921863\ldots.
\]
Thus this invocation does not repeat the dead AND-extremality search.

The named cross-account result actually consumed is

`account02/B16/20260922T010120Z-gate-margin-restriction-martingale/REPORT.md`

(blob `335d6ffa58cae84c7b47e742a250a20d2e2bddd4`).

Its exact theorem says that for any adaptive restriction policy,
\[
P(G)c_G=\mathbb E\sum_{r<\tau}Q_r c_r,
\qquad
P(G)=\mathbb E\sum_{r<\tau}Q_r,
\tag{1.2}
\]
where \(P=I/4-p_{\rm out}(1-p_{\rm out})\), \(Q_r\) is the Poincare-currency decrement at step \(r\), and \(c_r\) is the local signed restriction margin. In the balanced-excess specialization \(\Gamma_0=0\), uniform biases,
\[
L_r=H_t(G_r)-\mathbb E[H_t(G_{r+1})\mid G_r],
\qquad
\rho_r=\frac{L_r}{4Q_r},
\tag{1.3}
\]
and
\[
\frac{H(g)}{I(g)-1}
=
\frac{\mathbb E\sum_r Q_r\rho_r}{\mathbb E\sum_r Q_r}.
\tag{1.4}
\]

That peer report named the immediate exact test: compute a depth-two adaptive block margin on the composition-prime 18-input obstruction and determine whether descendant continuation actually refunds the bad one-step margin. This report executes that test source-exactly.

## 2. Source-exact gate and checker

The checker reconstructs the same 18-variable parent used by the existing arity-10 certificate, with truth-table SHA-256

`f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839`.

It recomputes the integer Walsh transform and proves
\[
p_{\rm out}=\frac12,\qquad
I=\frac{261}{128},\qquad
P=\frac{I-1}{4}=\frac{133}{512},
\tag{2.1}
\]
and, by rational atanh-series logarithm enclosures,
\[
6.776605309005978082
< H <
6.776605309005978083.
\tag{2.2}
\]

Coordinates \(0,\ldots,8\) are the nine core coordinates of the inherited construction and \(9,\ldots,17\) are its nine host-selector coordinates. No symmetry assumption is used for the final inequalities: the checker evaluates every listed coordinate and every branch of the explicit adaptive policies.

## 3. Core coordinates: one step is already cheap

For every core coordinate \(i\in\{0,\ldots,8\}\), the exact first-step currency is
\[
Q_i=\frac{11343}{262144},
\tag{3.1}
\]
while the entropy decrement is
\[
1.013601295074620283
< L_i <
1.013601295074620284.
\tag{3.2}
\]
Therefore
\[
\boxed{
5.856243892621909096
<\frac{L_i}{4Q_i}<
5.856243892621909097.
}
\tag{3.3}
\]
So a depth-one block already lies below \(5.857\) on all nine core coordinates.

## 4. Host coordinates: the bad one-step margin is a continuation artifact

For every host-selector coordinate \(i\in\{9,\ldots,17\}\), the first step is genuinely bad:
\[
Q_i=\frac{255}{262144},
\tag{4.1}
\]
\[
0.032776311895838726
< L_i <
0.032776311895838727,
\tag{4.2}
\]
hence
\[
\boxed{
8.423640691787006960
<\frac{L_i}{4Q_i}<
8.423640691787006961.
}
\tag{4.3}
\]
Thus any proof demanding a pointwise first-split ratio below the FEI scale fails even on this source gate.

However, retain the child continuation exactly as (1.2) requires. The following branch-adaptive second splits are certified:

\[
\begin{array}{c|cc}
\text{first host }i & j\text{ after }x_i=0 & j\text{ after }x_i=1\\ \hline
9&4&1\\
10&1&0\\
11&0&2\\
12&0&1\\
13&3&0\\
14&0&1\\
15&0&2\\
16&3&0\\
17&1&0
\end{array}
\tag{4.4}
\]

For every one of these nine adaptive depth-two blocks, the total consumed currency is exactly
\[
Q_\sigma=\frac{11739}{262144},
\tag{4.5}
\]
and the total entropy decrement satisfies
\[
1.054724011361257967
< L_\sigma <
1.054724011361257968.
\tag{4.6}
\]
Consequently
\[
\boxed{
5.888269257055234872
<\rho_\sigma:=\frac{L_\sigma}{4Q_\sigma}<
5.888269257055234873
<5.889.
}
\tag{4.7}
\]

For example, for \(i=9\), after branch \(x_9=0\) split \(j=4\), and after branch \(x_9=1\) split \(j=1\). Each second-step conditional branch spends
\[
Q_{\rm second}=\frac{2871}{65536}
\tag{4.8}
\]
and has
\[
5.831971824465840769
<\frac{L_{\rm second}}{4Q_{\rm second}}<
5.831971824465840770.
\tag{4.9}
\]
The large one-step value \(8.4236\ldots\) is therefore not a persistent obstruction; it is exactly compensated once the descendant term that the blind arity induction discards is retained.

## 5. Proved finite statement and attempted refutation

### PROVED, source-exact finite statement

For the inherited balanced 18-input Numaro gate, **every possible first coordinate has an explicit adaptive restriction block of depth at most two whose balanced-excess block margin is \(<5.889\)**.

For core coordinates the block stops after one reveal; for host coordinates use (4.4).

This applies the peer's exact signed/Poincare-currency theorem to the explicit gate that refuted the old read-once potential. It shows that the obstruction to AND extremality is **not** itself an obstruction to the signed finite-block mechanism.

### Attempted refutation

The natural falsifier was the host-selector layer because its one-step local ratio is \(8.42364069\ldots\), already above both \(6.4573\) and the Numaro balanced-excess ratio. The exact two-step calculation refutes that attempted obstruction: all nine host coordinates fall below \(5.889\) once a single source-valid child split is included.

No averaging over signs, no non-Boolean relaxation, and no positive-part replacement is used.

## 6. What remains universal

This calculation does **not** prove that every Boolean gate admits a bounded-depth block with margin below a universal constant. It proves only that the first major composition-prime gate falsifier survives the proposed repair.

The next universal obligation is:

> Prove a dimension-independent finite-block theorem: for every non-affine Boolean gate there exists an explicit adaptive restriction block with bounded signed block margin while preserving all descendant continuation credits; or produce a Boolean family for which every bounded/admissible block remains above every fixed constant.

The next decisive finite test is the newer 162-input shared-graft obstruction named by the peer. If the same core/host refund pattern survives there, the next proof attempt should isolate the structural reason one core reveal pays a bad selector reveal rather than add another broad gate sweep.

**replacement_obligation:** derive a universal structural finite-block selector/refund lemma, or refute it on the 162-input/iterated shared-graft family.  
**consumed_peer_artifact:** `account02/B16/20260922T010120Z-gate-margin-restriction-martingale/REPORT.md`, blob `335d6ffa58cae84c7b47e742a250a20d2e2bddd4`.  
**applied_to_claim:** the peer's named immediate depth-two test on the exact 18-input composition-prime obstruction.  
**remaining_implication:** universal dimension-independent existence of a paid adaptive finite block.  
**next_recipient:** `account02/B16` and `account03/B18`; the next construction target is the 162-input shared-graft obstruction.  
**full-FEI implication:** none yet; full FEI remains OPEN / NOT PROVED.

## 7. Reproducibility and scope

`check_numaro_two_step_block.py` reconstructs the parent source, verifies the source hash, computes exact integer Walsh restrictions, computes all Poincare currencies as rational numbers, encloses every logarithm by a rational atanh series, checks all 18 first coordinates and all nine explicit adaptive depth-two policies, and exits `PASS`.

`check_output.txt` records the numerical/rational certificate. The check is finite evidence for the theorem in sections 3–5, not a finite certificate for FEI.
