# B12 FEI — source-valid falsification of AND/decomposable gate extremality

**Status:** `CANDIDATE_REFUTED / ESSENTIAL_STEP_APPLIED`. **Full uniform-cube FEI remains OPEN / NOT PROVED.**

**Execution:** `WITHOUT_VERIFIED_BRAIN`. Authenticated GitHub controls and scientific sources were read directly; no authenticated cognitive-brain retrieval/context was used in the mathematics.

**Model self-report:** GPT-5.6 Sol. Requested effort: maximum actually supported (repository preference requests GPT-6/maximum). Configured/known reasoning effort: `UNKNOWN`; the exposed scheduler inventory has no model/reasoning selector field. Provider reasoning-token and provider-thinking-time counters: not exposed.

## 1. Live owner target and exact outcome

Fresh owner control revision `2026-09-22.2` supersedes the older campaign-B harmonic-row assignment for substantive mathematics in this invocation. The live FEI job is to either prove that two-input AND/decomposable gates are extremal for the source-exact all-gate potential inequality, or falsify that claim by exhibiting a Boolean gate and product bias vector whose required margin exceeds AND's.

This report executes the second job rigorously.

The witness is the already source-certified balanced ten-input Boolean gate `G10` from fleet04/B12, evaluated at the uniform bias vector

\[
p_1=\cdots=p_{10}=\frac12.
\]

For the same base potential used by the certified read-once theorem, `G10` requires quadratic margin coefficient

\[
\boxed{c_{G10}>0.018289126551422924},
\]

whereas the read-once certificate proves that

\[
\boxed{c=0.01}
\]

suffices for **every** two-input AND/OR gate. Hence

\[
\boxed{c_{G10}>1.8289\times 0.01},
\]

so AND/decomposable extremality for that source-exact candidate is false.

A second, stronger source-valid witness comes from the inherited shared-coordinate graft family: its finite balanced gate `F5` requires

\[
\boxed{c_{F5}>0.2682037981828>26.82\times0.01}.
\]

Moreover the previously proved strict increase of the balanced excess ratios along the shared-graft tail turns into strict increase of these uniform-bias gate-margin demands. Thus the failure is not an isolated floating-point accident or a finite-grid anomaly.

## 2. Named completed other-account result consumed

I consume the completed fleet04/B12 report

`proofnet24/P03-fei/fleet-2026-09-21/fleet04/B12/20260922T0254Z-and-atom-stopping/REPORT.md`,

blob `8a35d08850c8bf38a36c58af4ee3dcd670fa0de9`.

It reconstructs the exact balanced ten-input prime witness `G10`, with truth-table SHA-256

`3168d8fb8ac9f5d6d7dca1d79146392aecb5eb55cc76ccb028395a9e6a62bfb4`,

and proves

\[
I(G10)=\frac{257}{128},
\qquad
R(G10):=\frac{H(G10)}{I(G10)-1}
>6.459372281637855731.
\tag{2.1}
\]

The same report proves an exact fixed-order stopping decomposition: all nonaffine terminal continuations are two-input AND/OR atoms, with probability `29/64`, expected terminal Poincare currency `29/1024`, expected terminal entropy `29/32`, and preterminal raw entropy/Poincare margin strictly between `25.057083819433480` and `25.057083819433481`.

**How it is used here:** (2.1) gives a compact finite Boolean gate whose all-gate constraint can be evaluated exactly at one product bias vector. The stopping theorem additionally shows that its obstruction is compatible with ordinary AND/OR terminal continuation rather than being an arbitrary-row artifact.

## 3. Source-exact all-gate margin formula at a balanced uniform gate

The all-gate reformulation asks for one symmetric nonnegative potential `Gamma` satisfying

\[
\Gamma(p_{\rm out})+\widetilde H_G(p)
\le
\sum_i \operatorname{It}_i(G;p)
\frac{\Gamma(p_i)+h(V_{p_i})}{V_{p_i}},
\qquad V_p=4p(1-p).
\tag{G}
\]

For the base read-once candidate let

\[
C_0:=\Gamma_0(1/2)=6.4548.
\]

The gate-reformulation report defines the additional quadratic margin by replacing

\[
\Gamma_0(z)\mapsto \Gamma_0(z)+c z(1-z).
\]

If `D_G` denotes right minus left in `(G)` for the base potential, the replacement changes `D_G` by

\[
c\left[\frac{I(G;p)}4-p_{\rm out}(1-p_{\rm out})\right],
\]

and therefore the required coefficient is

\[
c_G=-\frac{D_G}{I/4-p_{\rm out}(1-p_{\rm out})}
\tag{3.1}
\]

whenever the denominator is positive.

Now suppose `G` is balanced under uniform inputs and `I(G)>1`. Then

\[
p_i=p_{\rm out}=\frac12,\qquad V_{p_i}=1,\qquad h(V_{p_i})=0,
\]

and

\[
\sum_i \operatorname{It}_i(G;1/2)=I(G).
\]

Consequently

\[
D_G=C_0 I(G)-C_0-H(G)
=C_0(I(G)-1)-H(G).
\tag{3.2}
\]

The Poincare denominator is

\[
\frac{I(G)}4-\frac14=\frac{I(G)-1}{4}.
\tag{3.3}
\]

Substituting (3.2)--(3.3) into (3.1) gives the exact identity

\[
\boxed{
 c_G(1/2,\ldots,1/2)
 =4\left(\frac{H(G)}{I(G)-1}-C_0\right).
}
\tag{3.4}
\]

This identity uses the actual Boolean gate spectrum and the exact gate potential normalization; no arbitrary-row relaxation, sign-free profile, depth surrogate, rank/l1 bound, or second-moment payment occurs.

There is an even simpler equivalent check for the final certified read-once potential. The read-once theorem adds `0.01 p(1-p)`, so its center is

\[
\widehat\Gamma(1/2)=6.4548+\frac{0.01}{4}=6.4573.
\tag{3.5}
\]

For any balanced uniform gate, `(G)` for this final potential reduces exactly to

\[
\frac{H(G)}{I(G)-1}\le 6.4573.
\tag{3.6}
\]

Thus a single rigorous balanced gate with ratio above `6.4573` directly falsifies universality of the certified read-once potential.

## 4. Compact falsification by `G10`

Apply (3.4) to (2.1). Since the reported lower bound is rigorous,

\[
\begin{aligned}
c_{G10}
&>4(6.459372281637855731-6.4548)\\
&=\frac{4572281637855731}{250000000000000000}\\
&=0.018289126551422924.
\end{aligned}
\tag{4.1}
\]

The certified read-once theorem proves that adding `c=0.01` suffices for all AND/OR constraints. Hence

\[
 c_{G10}>0.018289126551422924>0.01\ge c_{\rm AND}^{\rm required}.
\tag{4.2}
\]

Equivalently, by (3.6),

\[
R(G10)>6.459372281637855731>6.4573,
\]

so the final certified read-once potential itself fails `(G)` at the uniform ten-dimensional product bias.

This is a genuine Boolean counterexample to the **proposed gate-extremality mechanism**, not a counterexample to FEI. It also does not depend on numerical optimization over biases: the bias vector is exactly uniform and the ratio lower bound is inherited from an exact finite Boolean witness.

## 5. Infinite source-valid strengthening from the shared-graft family

The previous fleet02/B12 report

`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B12/20260922T013941Z-shared-graft-tail/REPORT.md`

proved for a recursively generated family of genuine finite balanced monotone Boolean gates `F_t` that

\[
R(F_{t+1})>R(F_t)\qquad(t\ge4),
\tag{5.1}
\]

and certified

\[
R(F_5)>6.5218509495457.
\tag{5.2}
\]

Applying (3.4) pointwise yields immediately

\[
c_{F_{t+1}}(1/2,\ldots,1/2)
>c_{F_t}(1/2,\ldots,1/2)
\qquad(t\ge4),
\tag{5.3}
\]

and from (5.2),

\[
\begin{aligned}
c_{F_5}
&>4(6.5218509495457-6.4548)\\
&=\frac{670509495457}{2500000000000}\\
&=0.2682037981828.
\end{aligned}
\tag{5.4}
\]

Thus the certified AND payment `0.01` is beaten by a factor greater than

\[
26.82037981828.
\tag{5.5}
\]

The monotonicity in (5.3) is structurally useful: a universal proof cannot freeze the base potential at any finite member of this shared-coordinate family and then invoke decomposable-gate extremality. Later genuine Boolean gates in the same construction demand strictly more center/margin at uniform bias.

## 6. What this resolves and what it does not

The owner target for this invocation offered two alternatives: prove decomposable/AND extremality, or falsify it with a gate/bias vector whose source-exact demand is higher. Equations (4.1)--(4.2) execute the second alternative.

This does **not** refute the all-gate reformulation itself. It refutes the specific hope that the read-once/AND candidate potential is already universal, and more generally refutes the claim that the corresponding all-gate margin is maximized by AND/decomposable gates.

The surviving full-FEI problem is therefore:

> Construct some other symmetric nonnegative potential `Gamma` with finite center, necessarily at least the best balanced-gate lower floor, that satisfies `(G)` for every Boolean gate and every product bias; or replace the scalar-measure potential mechanism by another complete universal proof.

The present report supplies no finite universal upper bound on that new center.

## 7. Last-three comparison and movement fields

The last three own substantive B12 reports before this run were:

1. `20260922T013941Z-shared-graft-tail`: source-valid infinite-tail lower-bound theorem.
2. `20260921T232119Z-harmonic-root-marked-spectrum`: one-source harmonic first-mark code, global continuation entropy unpaid.
3. `20260921T211150Z-component-factorial-harmonic-capacity`: factorial reciprocal-component routing, exceptional address entropy unpaid.

The first of these had already moved away from the harmonic residual because the newer owner message changed the active mechanism. This run does not reopen the killed row-local implication; it translates the source-valid Boolean witnesses directly into the exact all-gate margin coordinates and resolves the owner's falsification fork.

**FULL-PROBLEM CHANGE:** `NO FEI UPPER-BOUND CHANGE`. Full FEI remains open. The rigorous lower-floor information is inherited rather than newly improved here. However, the current owner subproblem changes from `AND/decomposable extremality unresolved` to `REFUTED by an exact Boolean gate at an exact bias vector`.

**MECHANISM CHANGE:** `YES`. Before: balanced-gate ratios were used mainly as center lower bounds. After: the exact identity (3.4) converts them into source-exact all-gate margin demands; this produces both a compact ten-input falsifier and an infinite strictly increasing family of margin demands.

**Quantified remaining implication:** any replacement scalar potential must survive at least `G10` with center/routing sufficient for `R>6.459372281637855731`, and the shared-graft family forces the center above `6.5218509495457`; satisfying AND constraints alone is insufficient.

## 8. Verification and method notes

The exact-arithmetic checker `check_gate_margin.py` represents all quoted certified decimal lower bounds as Python `Fraction`s. It verifies:

- `G10` beats the final read-once center `6.4573`;
- `c_G10 > 0.01`;
- `c_F5 > 0.01`;
- `c_F5 > c_G10`;
- the exact rational forms in (4.1) and (5.4).

Executed output is archived in `check_gate_margin.out` and reports `PASS`.

The three fresh FLEET_RULES moves used were **#2 attack the negation first** (falsify extremality rather than prove it), **#18 say it in another language** (balanced excess ratio -> exact all-gate margin), and **#24 find the extremal object** (the shared-graft family supplies a monotone sequence of harder gates, disproving a frozen AND extremizer).

No claim of publication novelty is made. No finite scan is promoted to FEI closure.
