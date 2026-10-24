# account01/B01 — credit-augmented Bellman recursion with signed Boolean-dependence transfer

**Run:** `20260922T103250Z-account01-B01-fei-r11`  
**Classification:** `ESSENTIAL_STEP_APPLIED / SIGNED_CREDIT_RECURSION / MONOTONE-CREDIT-SHORTCUT_REFUTED`  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Later owner control and exact target

The current owner programme is `FEI-ALL-TEAM-20260922T095941Z`, control revision `2026-09-22.3`. It supersedes the earlier FOREST assignment for this slot. The active B01 target is the **credit-augmented Bellman supersolution**: retain actual child defects under restriction and explicitly price a source-defined Boolean-dependence credit instead of discarding it.

The preferred newly assigned partner `account02/B01` had no completed compatible FEI result visible at the fresh snapshot; its visible recent work still belonged to the superseded FOREST programme. I therefore did not wait. The named OTHER-account theorem actually consumed is account04/B15's exact I-projection composition-transfer theorem, together with account02/B15's source definition of `K_occ` and account03/B04's fresh near-zero Poincare trichotomy.

Source pins used below:

1. **Selector recursion:** `yspennstate/math-open-problems`, commit `4ccd51ad517f425a529daa52c3352905b86ea69d`, `proofnet24/P03-fei/fleet-2026-09-21/account02/B12/20260922T091546Z-uniform-selector-debit-and-safe-lift/REPORT.md`, Sections 2--4 only. Its historical coefficient `0.337` is refuted and is not used.
2. **Influence I-projection:** same repository, commit `4bd6d05f1eb8325d665f2748f4d74dcee2550a04`, `proofnet24/P03-fei/fleet-2026-09-21/account02/B15/20260922T0829Z-influence-iprojection-kl/REPORT.md`, Sections 2--4.
3. **Named OTHER-account result applied:** same repository, commit `2bf247373576eb406ca91bb3ea5f3ce5e5ab8588`, `proofnet24/P03-fei/fleet-2026-09-21/account04/B15/20260922T091017Z-iprojection-composition-transfer/REPORT.md`, Theorem 2.1 and Sections 3--4. It proves exact superadditivity of `K_occ` under disjoint composition, with the missing hierarchy term retained as an explicit KL credit.
4. **Fresh denominator geometry:** same repository, commit `35ca31a959e9c40d7a5387f913197b6682b5dda6`, `proofnet24/P03-fei/fleet-2026-09-22/account03/B04/20260922T103904Z-nearzero-poincare-trichotomy/REPORT.md`, Sections 2--6.

## 2. Source-defined dependence credit

For a nonconstant Boolean gate `G` at product bias `p`, write

\[
q=\Pr[G=-1],\qquad v=V_q=4q(1-q),
\]

and let `P=w^+` be its biased squared Fourier law conditioned on a nonempty spectral set. Let

\[
r_i=P(i\in S)=\frac{\operatorname{It}_i(G;p)}{v}.
\]

Account02/B15 defines the maximum-entropy nonempty conditional-product law `Q_r` with these coordinate marginals and the exact Boolean-dependence credit

\[
K_{\rm occ}(G;p)=D_{\rm KL,2}(P\Vert Q_r)\ge0.
\]

The exact normalized gate remainder is

\[
R_\Gamma=\frac{D_\Gamma}{v}=B_{\rm inf}^\Gamma+K_{\rm occ}.
\tag{2.1}
\]

It is useful for physical restriction to put the credit back in the same units as the unnormalized gate defect:

\[
\boxed{C(G;p):=v(G;p)K_{\rm occ}(G;p)\ge0.}
\tag{2.2}
\]

Set `C=0` on constant restrictions. For a reserve parameter `lambda>=0`, define the **credit-reserving Bellman defect**

\[
\boxed{A_{\Gamma,\lambda}(G;p):=D_\Gamma(G;p)-\lambda C(G;p).}
\tag{2.3}
\]

If `A_{Gamma,lambda}>=0`, then automatically `D_Gamma>=0`, because `C>=0`. Thus proving nonnegativity of `A` is a stronger statement than the ordinary all-gate condition, not a circular restatement that assumes FEI.

## 3. Exact one-step augmented Bellman identity

Split a physical selector coordinate `j` with bias `s`. Let the Boolean restrictions be `G_0,G_1`; let

\[
q_a=\Pr[G_a=-1],\quad q=(1-s)q_0+s q_1,
\]

and let

\[
d=\Pr[G_0\ne G_1].
\]

The exact selector identity is

\[
\operatorname{It}_j(G;p)=V_s d.
\]

Write `B_j+JS_j` for the exact conditional spectral-entropy increment from the selector source. Account02/B12 gives, for an arbitrary symmetric potential `Gamma`,

\[
\begin{aligned}
D_\Gamma(G;p)= {}&(1-s)D_\Gamma(G_0)+sD_\Gamma(G_1)\\
&+(1-s)\Gamma(q_0)+s\Gamma(q_1)-\Gamma(q)\\
&+d\,[\Gamma(s)+h_2(V_s)]-(B_j+JS_j).
\end{aligned}
\tag{3.1}
\]

Define the **signed dependence-credit transfer**

\[
\boxed{
\Xi_j(G;p):=C(G;p)-\bigl[(1-s)C(G_0)+sC(G_1)\bigr].
}
\tag{3.2}
\]

and the local ordinary Bellman term

\[
\boxed{
L_\Gamma(G,j;p):=(1-s)\Gamma(q_0)+s\Gamma(q_1)-\Gamma(q)
+d[\Gamma(s)+h_2(V_s)]-(B_j+JS_j).
}
\tag{3.3}
\]

Subtracting `lambda*C(G)` from (3.1) and adding/subtracting the two child credits gives the exact identity

\[
\boxed{
A_{\Gamma,\lambda}(G;p)
=(1-s)A_{\Gamma,\lambda}(G_0)
+sA_{\Gamma,\lambda}(G_1)
+L_\Gamma(G,j;p)-\lambda\Xi_j(G;p).
}
\tag{3.4}
\]

No child defect and no KL credit has been discarded. This is the requested one-step augmented Bellman state.

### Conditional end-to-end implication

Suppose there exist a finite symmetric nonnegative potential `Gamma`, a finite `lambda>=0`, and a physical-selector policy such that at every nonconstant restriction state

\[
\boxed{L_\Gamma(G,j;p)\ge\lambda\Xi_j(G;p).}
\tag{3.5}
\]

Constants and literals are base cases. Iterating (3.4) gives `A_{Gamma,lambda}>=0`, hence `D_Gamma>=0` for every gate/bias, and the established all-gate equivalence then yields full uniform-cube FEI with finite constant `Gamma(1/2)`.

Thus (3.5) is a genuine sufficient Bellman inequality. The new issue is that `Xi_j` is **signed**. Treating `K_occ` as a monotone bank under physical restriction is false.

## 4. Exact four-bit counterexample to monotone dependence credit

Consider the uniform four-bit Boolean function in little-endian truth-table order

\[
(-1,-1,-1,-1,-1,-1,1,1,-1,1,-1,1,1,-1,-1,1).
\tag{4.1}
\]

Its raw Walsh vector is

\[
(-4,-4,-4,4,-4,-4,4,-4,-4,4,-4,-4,-4,4,4,4).
\tag{4.2}
\]

Every squared Fourier coefficient is therefore `1/16`. The empty coefficient has mass `1/16`, so

\[
v=15/16.
\]

Conditioning on nonempty spectral sets makes `P` uniform on the fifteen nonempty subsets of `[4]`; its four occurrence marginals are all `8/15`. This is **exactly** the I-projection `Q_r`: take independent Bernoulli coordinates of probability `1/2` and condition on nonemptiness. In the account02/B15 parametrization this is

\[
c=15/16,\qquad cr_i=1/2.
\]

Hence

\[
\boxed{K_{\rm occ}(G)=0,\qquad C(G)=0.}
\tag{4.3}
\]

Now restrict the first physical bit at selector bias `s=1/2`.

### Child 0

The child values and raw Walsh vector are

\[
(-1,-1,-1,1,-1,-1,1,-1),
\]

\[
(-4,0,-4,0,0,-4,0,4).
\]

Thus `v_0=3/4`, the conditioned spectral law is uniform on the three masks `010,101,111`, and

\[
r^{(0)}=(2/3,2/3,2/3).
\]

Its I-projection parameter is the positive root

\[
\boxed{c_0=\frac{9-3\sqrt3}{4}.}
\]

The corresponding conditional-product law has positive mass on every nonempty subset, whereas the actual child law has four zero cells. Therefore `P_0 != Q_{r^(0)}` and strictly

\[
K_{\rm occ}(G_0)>0.
\tag{4.4}
\]

Numerically,

\[
K_{\rm occ}(G_0)=1.1074873765924134\ldots,
\qquad
C(G_0)=0.8306155324443101\ldots .
\]

### Child 1

The second child has values and raw Walsh vector

\[
(-1,-1,-1,1,1,1,-1,1),
\]

\[
(0,-4,0,4,-4,0,-4,0).
\]

Here `v_1=1`, its conditioned spectral law is uniform on masks `001,011,100,110`, and

\[
r^{(1)}=(1/2,1/2,1/2),\qquad
\boxed{c_1=3-\sqrt5.}
\]

Again the I-projection has full support while the actual law has zeros, so

\[
K_{\rm occ}(G_1)>0.
\tag{4.5}
\]

Numerically,

\[
K_{\rm occ}(G_1)=C(G_1)=0.7356047840765432\ldots .
\]

Consequently

\[
\boxed{
\Xi_j
=C(G)-\frac{C(G_0)+C(G_1)}2
<0,
}
\tag{4.6}
\]

with numerical value

\[
\Xi_j=-0.7831101582604266\ldots .
\]

This is an exact source-valid refutation of the shortcut

> `C(parent) >= E[C(children)]` under every physical restriction.

It is not a counterexample to FEI. In fact, a negative `Xi_j` is favorable in (3.4): child-generated dependence credit creates a positive `-lambda Xi_j` contribution. The theorem says that **the sign must be retained**, rather than declaring every parent-to-child transfer a debit.

The standard-library checker in this run reconstructs every displayed Walsh vector and rational marginal, verifies `K_occ(parent)=0`, verifies both child KL values are positive, and asserts `Xi_j<0`.

## 5. Applying the fresh OTHER-account denominator theorem

Account03/B04 proves the exact physical Poincare-gap decomposition

\[
W=(1-s)W_0+sW_1+s(1-s)[d-\Delta^2],
\qquad \Delta=q_1-q_0,
\tag{5.1}
\]

with `d-Delta^2>=d(1-d)` and a separate boundary-collapse regime.

For the four-bit witness above, `s=1/2`. In output-probability coordinates the two child means `-1/2` and `0` give `|Delta|=1/4`, while `d=1/2`. Thus the local Poincare contribution is

\[
\boxed{
\frac14\left(\frac12-\frac1{16}\right)=\frac7{64}>0.
}
\tag{5.2}
\]

So the sign reversal (4.6) is **not** a selector-boundary artifact and does not arise from the Poincare equality set. It occurs at the fully interior selector `s=1/2` with a definite local Poincare gap. This directly changes the B01 design: the credit ledger and the Poincare/safe-direction ledger are complementary currencies, not interchangeable monotone quantities.

This also complements account04/B15. That theorem says `K_occ` is superadditive, with an explicit positive hierarchy credit, under **disjoint composition**. The present example shows that no analogous one-sided monotonicity holds in the direction needed for **physical restriction**. A correct Bellman proof must therefore use the signed transfer `Xi_j` in (3.4), not transplant composition superadditivity into a restriction step.

## 6. What is proved and what remains unpaid

### New proved implication

For every gate, every physical selector and every `lambda>=0`, (3.4) is an exact credit-augmented Bellman identity. If a finite symmetric nonnegative `Gamma` and a selector policy satisfy the local signed inequality (3.5), then full FEI follows.

### Refuted shortcut

The natural simplification `Xi_j>=0` for all physical restrictions is false, even at uniform bias and strictly away from the Poincare equality/boundary regimes. The four-bit source (4.1) has `C(parent)=0` and positive average child credit.

### First essential missing implication

The remaining B01 target is now sharper than “add a KL credit.” One must prove a **signed-transfer local inequality**

\[
L_\Gamma(G,j;p)\ge\lambda\Xi_j(G;p)
\tag{6.1}
\]

for a finite-cap symmetric potential and an admissible physical selector policy, or exhibit a genuine Boolean family making every such proposed pair fail. The account03/B04 trichotomy suggests separating the proof into interior irrelevant, interior near-dictator, and bias-boundary contraction regimes; (4.6) shows that within the interior regimes the sign of `Xi_j` still cannot be guessed from the Poincare gap alone.

A useful next mathematical question is therefore to bound only the **positive part** `Xi_j^+` by the exact local selector/Poincare quantities plus retained child Bellman slack. Negative `Xi_j` should be kept as a bonus. Any bound that replaces `Xi_j` by `|Xi_j|` throws away precisely the child-generated dependence credit demonstrated here.

**Outcome:** `ESSENTIAL_STEP_APPLIED`.  
**Full FEI:** `OPEN_NOT_PROVED`.  
No novelty or publication-priority claim is made.
