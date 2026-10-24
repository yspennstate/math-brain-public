# B13 — exact all-block gate critical core and common-potential G10 stopping payment

**Outcome:** `ESSENTIAL_STEP_APPLIED / FULL_FEI_OPEN`.  
**Full uniform-cube FEI:** **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`. Authenticated repository controls and mathematical source artifacts were read directly; no installed/native cognitive-brain receiver context was consumed.

**Model self-report:** GPT-5.6 Sol.  
**Reasoning requested:** maximum actually supported.  
**Configured/known reasoning level:** UNKNOWN / scheduler selector not exposed.  
**Provider reasoning-token or thinking-time usage:** NOT_EXPOSED.

## 0. Version/change summary and the exact live implication

The later OWNER CONTROL revision `2026-09-22.2` keeps B12--B18 on FEI and supersedes older route-specific duties with the all-gate formulation. For a Boolean gate `G` at independent product biases `p=(p_1,...,p_n)`, let

\[
V_u=4u(1-u),\qquad
A_\Gamma(u)=\Gamma(u)+h_2(V_u),
\]

\[
\lambda_i(G;p)=\frac{\operatorname{It}_i(G;p)}{V_{p_i}},
\]

and write the all-gate slack (RHS minus LHS) as

\[
D_\Gamma(G;p)
=
\sum_i \lambda_i A_\Gamma(p_i)
-
\Gamma(q)-\widetilde H_G(p),
\qquad q=\Pr[G=-1].
\tag{0.1}
\]

The gate reformulation proves that one symmetric nonnegative `Gamma` with finite `Gamma(1/2)` and `D_Gamma>=0` for every finite gate/product bias gives full FEI with the same center constant.

The newest compatible lead result read in this run is account01/B18

`proofnet24/P03-fei/fleet-2026-09-21/account01/B18/20260922T0222Z-shared-graft-tail/REPORT.md`.

Together with account02/B17's exact gate-composition cocycle, it leaves the universal obstruction on composition-prime gates. Subsequent cross-account work has pushed the source-bound shared-core scalar ceiling to

\[
M<6.52185121301287772365150440023918196647146413881
\tag{0.2}
\]
(account04/B15, cited below). To avoid freezing a center below this proved mechanism ceiling, this report uses the explicit safe decimal

\[
\boxed{C^\dagger=6.521852,}
\qquad
\boxed{a^\dagger=4(C^\dagger-6.4548)=0.268208,}
\tag{0.3}
\]

and the candidate

\[
\Gamma^\dagger(u)=\Gamma_{\rm RO}(u)+a^\dagger u(1-u).
\tag{0.4}
\]

Here `Gamma_RO` is the inherited read-once fixed-point potential with `Gamma_RO(1/2)=6.4548`. The positive quadratic lift changes every gate slack by `a^dagger M(G;p)>=0`, so it never destroys a gate inequality already paid by `Gamma_RO`. No claim is made that (0.4) is universal.

The **first missing implication after this report** is the following source-exact physical selector:

> **BLOCK-PRIME-SELECTOR-v1.** Every composition-prime Boolean gate of essential arity at least two, at every interior product bias, has a nonempty proper physical block `A` whose block remainder `R_{Gamma^dagger,A}` defined in (2.2) is nonnegative.

Section 3 proves that this one statement would imply full FEI with constant `6.521852`. It is not proved here.

## 1. Named OTHER-account results actually consumed

The principal required other-account input is account04/B12

`proofnet24/P03-fei/fleet-2026-09-21/account04/B12/20260922T0254Z-and-atom-stopping/REPORT.md`,
report blob `8a35d08850c8bf38a36c58af4ee3dcd670fa0de9`.

For the exact ten-input balanced composition-prime gate `G10`, along the physical reveal order `0,1,...,9` and stopping at the first affine or two-essential-input AND/OR child, it proves exactly

\[
\Pr(\text{AND/OR terminal})=\frac{29}{64},
\qquad
\mathbb E P(G_\sigma)=\frac{29}{1024},
\]

\[
Q_{\rm block}=P(G_{10})-\mathbb E P(G_\sigma)=\frac{229}{1024},
\tag{1.1}
\]

with every nonaffine terminal having output bias `1/4` or `3/4`, `I=1`, `P=1/16`, `H=2`, and

\[
25.057083819433480
<
\frac{H(G_{10})-29/32}{229/1024}
<
25.057083819433481.
\tag{1.2}
\]

That report leaves the **common-Gamma terminal-atom subtraction problem** open. Section 5 below closes that exact calculation for `Gamma^dagger`.

A second OTHER-account input is account04/B15

`proofnet24/P03-fei/fleet-2026-09-21/account04/B15/20260922T020955Z-adaptive-depth-shared-core-ceiling/REPORT.md`,
which proves (0.2) for the entire adaptive integer-depth version of the source-bound shared-core mechanism. This is why the conservative center (0.3) is used.

A third source identity comes from account03/B17

`proofnet24/P03-fei/fleet-2026-09-21/account03/B17/20260922T003133Z-gate5-dyadic-unbalanced/REPORT.md`,
which records the read-once fixed-point identity

\[
\Gamma_{\rm RO}(1/4)=\Gamma_{\rm RO}(1/2)-2=6.4548-2.
\tag{1.3}
\]

Finally, the same-account account02/B17 report

`proofnet24/P03-fei/fleet-2026-09-21/account02/B17/20260922T004442Z-gate-composition-cocycle/REPORT.md`
proves the exact composition cocycle for `D_Gamma` and for the Poincare currency. It is used in Section 3 to make tensor/composition primitivity simultaneous with restriction criticality.

## 2. New universal theorem: exact physical block-slack decomposition

Let `A` be a nonempty physical input block. Draw `z` from the **actual product marginal** on the coordinates in `A`, and let `G_z` be the restricted child on `A^c` with the inherited product biases. Define

\[
\Delta_A\widetilde H
=
\widetilde H_G(p)-\mathbb E_z\widetilde H_{G_z}(p_{A^c}).
\tag{2.1}
\]

### Theorem 2.1 — exact block decomposition

For every Boolean gate, every interior product bias, every symmetric potential `Gamma`, and every physical block `A`,

\[
\boxed{
D_\Gamma(G;p)
=
\mathbb E_z D_\Gamma(G_z;p_{A^c})
+
R_{\Gamma,A}(G;p),
}
\tag{2.2}
\]

where

\[
\boxed{
R_{\Gamma,A}
=
\sum_{i\in A}\lambda_i A_\Gamma(p_i)
+
\mathbb E_z\Gamma(q_z)-\Gamma(q)
-
\Delta_A\widetilde H,
}
\tag{2.3}
\]

and `q_z=Pr[G_z=-1]`.

This preserves the source geometry exactly: the restriction is physical, branch weights are the actual product probabilities, all coordinate prices are in the original biased-influence normalization, and no affine rebasing or sign-free relaxation appears.

### Proof

For every unrevealed coordinate `j notin A`, the biased Fourier influence satisfies

\[
\operatorname{It}_j(G;p)
=V_{p_j}\Pr[G(X)\ne G(X^{\oplus j})].
\]

Conditioning on `X_A=z` and averaging gives

\[
\mathbb E_z\operatorname{It}_j(G_z;p_{A^c})
=
\operatorname{It}_j(G;p),
\tag{2.4}
\]

because `V_{p_j}` is unchanged. Hence the averaged child RHS in (0.1) contains exactly the parent input terms for `j notin A`. Subtract the averaged child slack from the parent slack. The surviving input terms are precisely those in `A`; the output-potential terms give `E Gamma(q_z)-Gamma(q)`; and the entropy terms give `-Delta_A Htilde`. This is (2.2)--(2.3). QED.

The adjacent checker independently evaluates (2.2) for all nonconstant Boolean gates through arity three at fixed interior rational biases and every nonempty proper physical block: **1,552 checks**, maximum absolute floating implementation discrepancy `8.882e-16`.

## 3. Exact minimum-essential-arity critical core

Fix any candidate `Gamma` with the constant/unary boundary cases paid. Suppose some gate violates the all-gate inequality, and choose a violating pair `(G,p)` of **minimum essential arity** `n`. Dummy variables are deleted; boundary biases are deleted as deterministic inputs, so all remaining biases are interior.

Write

\[
D_\Gamma(G;p)=-\varepsilon,
\qquad \varepsilon>0.
\tag{3.1}
\]

Every proper physical restriction has smaller essential arity after deleting dummies. Minimality therefore gives

\[
D_\Gamma(G_z;p_{A^c})\ge0
\]

for every branch of every nonempty proper block `A`. Inserting this into (2.2) yields the simultaneous **all-block overshoot identity**

\[
\boxed{
\Delta_A\widetilde H
=
\sum_{i\in A}\lambda_i A_\Gamma(p_i)
+
\mathbb E_z\Gamma(q_z)-\Gamma(q)
+
\varepsilon
+
\mathbb E_zD_\Gamma(G_z;p_{A^c}).
}
\tag{3.2}
\]

In particular, for every nonempty proper block,

\[
\boxed{R_{\Gamma,A}\le-\varepsilon<0.}
\tag{3.3}
\]

This is the exact critical-core property needed by a physical restriction proof. It is stronger than saying that some child has a lower ratio: **every** physical block overspends the candidate local budget by at least the same parent defect, and the complete descendant slack appears as a positive refund on the right of (3.2).

### Composition/tensor quantifier

The account02/B17 cocycle says that for a disjoint gate composition

\[
D_\Gamma(K)=D_\Gamma(F)+\sum_j b_jD_\Gamma(G_j),
\qquad b_j\ge0.
\tag{3.4}
\]

Therefore a minimum-essential-arity counterexample cannot have a nontrivial disjoint composition: otherwise one strictly smaller factor has negative slack. It is composition-prime. Disjoint tensor powers and recursive disjoint compositions are special cases, so they cannot be the minimum critical core either.

Thus one violating gate may be chosen **simultaneously**:

1. essential and interior-bias;
2. composition-prime/tensor-primitive in the gate sense; and
3. strict all-block physical-restriction critical in the quantitative form (3.2).

This is a true minimum-dimensional/arity reduction for the current gate candidate; it does not assume FEI.

### Conditional transfer to full FEI

If `BLOCK-PRIME-SELECTOR-v1` holds for `Gamma^dagger`, then a minimum counterexample is impossible: the selector gives a proper block with `R>=0`, contradicting (3.3). Hence `D_{Gamma^dagger}>=0` for every composition-prime gate. The composition cocycle gives it for every gate. The all-gate reformulation then gives

\[
\boxed{H(f)\le6.521852\,I(f)}
\]

for every uniform-cube Boolean `f`.

This is the complete transfer back to original entropy/influence. The only unproved arrow is the named selector itself.

## 4. Gauge quantifiers: exact NPN symmetry, but no free affine/character gauge

The minimal critical core may be normalized by the genuine symmetries of the product-biased gate problem:

- permuting inputs and their biases;
- negating input `i` while replacing `p_i` by `1-p_i`;
- negating the output, replacing `q` by `1-q`.

Because `Gamma`, `V_u`, and `h_2(V_u)` are symmetric under `u -> 1-u`, these NPN operations preserve `D_Gamma` exactly.

The older B13 affine/character minimization **cannot** be imported for free. Even at uniform bias it changes the gate slack. Take `Gamma(u)=4u(1-u)`. The two-bit parity character has `H=0`, `I=2`, balanced output and

\[
D_\Gamma(\text{parity})=1.
\]

An invertible `GL(2,2)` change sends its nonzero Fourier character to a dictator, for which

\[
D_\Gamma(\text{dictator})=0.
\]

Likewise multiplying a balanced dictator by an independent input character turns it into parity and changes the slack from `0` to `1`. The checker reproduces both values exactly at displayed precision.

So the current critical core is NPN-normalizable, **not** freely affine/character-normalizable. At nonuniform bias a general linear rebasing additionally destroys the product-coordinate geometry. Any affine change used later must be charged as a new physical gate, not silently inherited from the parent.

This resolves the tensor/gauge quantifier requested of B13 for the current candidate.

## 5. Apply the theorem to the OTHER-account G10 stopping block

The account04/B12 stopping theorem left one precise question: after subtracting the terminal AND/OR continuation, does the **same candidate potential** pay the preterminal block?

For the read-once fixed point, (1.3) and the terminal data `I=1,H=2,q=1/4 or 3/4` give exactly

\[
D_{\Gamma_{\rm RO}}(\text{terminal})
=6.4548-(6.4548-2)-2=0.
\tag{5.1}
\]

Under the quadratic lift (0.4), each terminal gains exactly

\[
D_{\Gamma^\dagger}(\text{terminal})
=
\frac{a^\dagger}{16}
=
\boxed{0.016763},
\tag{5.2}
\]

because its Poincare currency is `1/16`. Hence the expected terminal slack is

\[
\boxed{
\mathbb E D_{\Gamma^\dagger}(G_\sigma)
=a^\dagger\frac{29}{1024}
=0.007595734375.
}
\tag{5.3}
\]

From the rigorous account04/B12 interval (1.2),

\[
6.5098361275881512890625
< H(G_{10}) <
6.5098361275881515126953125.
\tag{5.4}
\]

The root is balanced and `I-1=129/128`, so

\[
\boxed{
0.0629678411618484873046875
<
D_{\Gamma^\dagger}(G_{10})
<
0.0629678411618487109375.
}
\tag{5.5}
\]

Subtracting the terminal continuation gives the aggregate preterminal common-potential slack

\[
\boxed{
0.0553721067868484873046875
<
D_{\Gamma^\dagger}(G_{10})
-
\mathbb E D_{\Gamma^\dagger}(G_\sigma)
<
0.0553721067868487109375.
}
\tag{5.6}
\]

It is strictly positive by a large margin. Equivalently, using account04/B12's exact `Q_block=229/1024`,

\[
D_{\Gamma^\dagger}(G_{10})-
\mathbb E D_{\Gamma^\dagger}(G_\sigma)
=
D_{\Gamma_{\rm RO}}(G_{10})
+a^\dagger\frac{229}{1024}.
\tag{5.7}
\]

Thus the **specific terminal-atom subtraction problem for G10 is closed** for the safe lifted candidate: the preterminal physical corridor has positive aggregate slack and every nonaffine terminal has positive slack. This does not prove that each individual preterminal node has nonnegative local remainder, and it does not prove the universal prime-gate selector.

## 6. Interaction with the newest account01/B14 physical selector

A newest compatible OTHER-account result, account01/B14

`proofnet24/P03-fei/fleet-2026-09-21/account01/B14/20260922T031346Z-signed-nine-core-selector/REPORT.md`,

proves a source-valid nine-coordinate physical block price `<6.528` for the entire signed nine-host shared-core transform, including nonmonotone source coordinates. This is genuine progress on physical selection.

The exact compatibility statement is now transparent from (2.3). That theorem controls its entropy drop `L_X` by a Poincare block currency, but a common-potential proof still needs the sign of

\[
\sum_{i\in X}\lambda_iA_{\Gamma^\dagger}(p_i)
+
\mathbb E\Gamma^\dagger(q_z)-\Gamma^\dagger(q)-L_X.
\tag{6.1}
\]

The account01/B14 `6.528` raw block-price inequality does not by itself determine (6.1). So it is compatible with, but does not yet prove, `BLOCK-PRIME-SELECTOR-v1`. The missing correction is now an explicit common-potential term rather than an unnamed restriction debt.

## 7. Last three B13 reports: target-level versus mechanism-level change

The last three completed substantive account02/B13 reports before this run were:

1. `20260921T232801Z-critical-core-tensor-tax`: fixed-`C` minimum-dimensional `H-CJ` critical core plus a folded-cooling tensor tax;
2. `20260922T001208Z-affine-critical-exchange`: simultaneous affine-minimum restriction criticality/tensor primitivity and all-parity basis exchange;
3. `20260922T014831Z-g10-affine-restriction-atom`: every proper physical restriction of `G10`, even after balancing character and arbitrary affine rebasing, lies below the old read-once center obstruction.

**FULL-PROBLEM CHANGE.** Before: full FEI was open and the current gate programme lacked an exact statement of what a minimum all-gate counterexample must do under *every* physical block. After: full FEI is still open, but any violation of a fixed candidate has been reduced exactly to one composition-prime, tensor-primitive, NPN-normalized gate satisfying the quantitative all-block overshoot identity (3.2). For `Gamma^dagger`, proving `BLOCK-PRIME-SELECTOR-v1` would now close FEI at the explicit constant `6.521852`. Separately, the concrete G10 terminal-atom subtraction debt from account04/B12 is paid with positive common-potential slack (5.6).

**MECHANISM CHANGE.** The preceding B13 mechanism was affine/character vector-matroid minimization on balanced descendants. This run replaces it by the product-biased all-gate slack, an exact physical block restriction decomposition, and a common-potential stopping ledger. It also proves that the older affine/character gauge is *not* a symmetry of this live target and therefore cannot be reused for free.

## 8. Verification and exact scope

The adjacent standard-library checker:

- tests Theorem 2.1 on all nonconstant Boolean gates through arity three at fixed interior rational biases and every nonempty proper block: `1552` checks, maximum absolute discrepancy `8.882e-16`;
- reproduces the uniform parity/dictator affine-gauge witness `D=1` versus `D=0`;
- checks the decimal/rational G10 arithmetic in (5.2)--(5.7), including `C^dagger` lying strictly above the account04/B15 shared-core ceiling.

Checker SHA-256: `4ff143e81804f6fcf74b5105a9ab05143720d0343ca7d51cec7afbd6bc51ce9f`.  
Output SHA-256: `11ab9f84002893d65251b5aa62fc473fffd1ee0fbfc5bdf1cef0472f4fa6cf92`.

The checker is a self-check. The universal theorem is proved analytically above; the finite census does not establish the selector. No novelty or publication-priority claim is made.
