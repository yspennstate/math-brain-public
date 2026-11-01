# fleet03/B04 — boundary Bellman desingularization of the near-zero Poincare quotient

**Outcome:** `ESSENTIAL_STEP_APPLIED / BOUNDARY_QUOTIENT_DESINGULARIZED`  
**Full FEI:** `OPEN_NOT_PROVED`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Programme:** `FEI-ALL-TEAM-20260922T095941Z`, owner revision `2026-09-22.3`.  
**Run:** `20260922T105911Z-fleet03-B04-fei-r11`.

## 1. Target and correction scope

The active B04 task is to classify and control the owner-normalized gate margin
\[
c_G(p)=-\frac{D_\Gamma(G;p)}{W_G(p)},\qquad
W_G(p)=\frac{I(G;p)-V_{p_{\rm out}}}{4},
\]
near the Poincare equality set `W=0`, without ever dividing at `W=0`. The prior B04 run classified the interior collar and showed that a selector bias going to a face is a genuinely different mechanism. Its first unpaid implication was boundary-contraction control.

The current correction bundle retires the old fixed-potential quadratic repairs `0.337` and `0.34`, the raw-U4 shortcut, naive unweighted-L2 payment and fixed-depth KL projection. None is used here. The argument is normalization-exact and potential-agnostic except for the standard source normalization in which constants and literals have zero defect.

### Assigned partner status

The assigned partner is `fleet04/B04`, whose current FEI assignment is the all-bias/face-contraction extension problem. At the fresh source snapshot there was **no completed FEI report or handoff from fleet04/B04** in either its assigned `math-open-problems` FEI root or the shared FEI handoff root. I therefore did not manufacture a partner theorem or wait synchronously.

The compatible completed other-account result consumed is fleet04/B13,

`proofnet24/P03-fei/fleet-2026-09-22/fleet04/B13/20260922T1023Z-poincare-bellman-exception-tree/REPORT.md`,

whose source-reported Theorems 2.1 and 3.1 give the exact singleton Poincare currency and the child-slack-preserving defect cocycle. The present report applies those identities specifically to the B04 boundary-contraction singularity and derives a sharper exact face formula.

The exact selector/disagreement identity from fleet02/B12,

`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B12/20260922T091546Z-uniform-selector-debit-and-safe-lift/REPORT.md`,

is also retained. Only its source-stable Sections 2–4 are used; its obsolete scalar candidate is not used.

## 2. Directional disagreement decomposition

Fix a Boolean gate `G` and one actual selector coordinate of bias `s in (0,1)`. Hold all residual product biases fixed and let `G_0,G_1` be the two Boolean restrictions. Write
\[
q_b=\Pr(G_b=1),\qquad \Delta=q_1-q_0,
\]
\[
a=\Pr(G_0=0,G_1=1),\qquad
b=\Pr(G_0=1,G_1=0),\qquad d=a+b.
\]
Then exactly
\[
\Delta=a-b
\]
and therefore the local Poincare defect is
\[
\boxed{
E:=d-\Delta^2=d(1-d)+4ab.
}
\tag{2.1}
\]
Both terms on the right are nonnegative. In particular
\[
E=0
\]
if and only if either `d=0`, or `d=1` and one of `a,b` is zero. In the latter case the two Boolean restrictions are opposite constants.

Let
\[
W_b=\frac{I(G_b)-V_{q_b}}4.
\]
The exact selector Poincare identity is
\[
\boxed{
W_G(s)=(1-s)W_0+sW_1+s(1-s)E.
}
\tag{2.2}
\]
This is the same currency called `P(G;p)` and `K=s(1-s)E` in the consumed fleet04/B13 theorem.

Equation (2.1) is useful near equality because it separates two different first-order failures: nondeterministic disagreement `d(1-d)` and two-way disagreement `4ab`. A gate can approach a literal only if both disappear.

## 3. Boundary face: exact first nonzero denominator

Assume now that the `s=0` face is a Poincare equality state,
\[
W_0=0.
\tag{3.1}
\]
Under full support on the residual variables, the previously proved equality classification says `G_0` is a constant or a literal/negated literal.

Substituting (3.1) into (2.2) gives the exact face formula
\[
\boxed{
W_G(s)=s\,[W_1+(1-s)E]
       =s(W_1+E)-s^2E.
}
\tag{3.2}
\]
Thus the first nonzero denominator coefficient is
\[
\boxed{A=W_1+E.}
\tag{3.3}
\]
There is no hidden higher-order positive-denominator branch. Indeed if `A=0`, then `W_1=E=0`. By (2.1), either `G_1=G_0` pointwise or `G_0,G_1` are opposite constants. In the first case the selector is dummy and the whole gate is the same equality gate; in the second the whole gate is the selector literal. Hence
\[
\boxed{A=0\quad\Longrightarrow\quad W_G(s)=0\ \text{for every }s.}
\tag{3.4}
\]
So **no quotient is defined in this branch**.

If `A>0`, then necessarily `E>0`: if `E=0`, the preceding Boolean classification forces `W_1=0`. Consequently for every `s in (0,1)` the local currency
\[
K_s=s(1-s)E
\tag{3.5}
\]
is strictly positive and `W_G(s)>0`. For `0<s<=1/2`, (3.2) also gives the explicit enclosure
\[
\boxed{
\frac{s}{2}(W_1+E)\le W_G(s)\le s(W_1+E).
}
\tag{3.6}
\]
This is a quantitative boundary neighborhood theorem for the denominator itself.

## 4. Exact desingularization of the gate-margin quotient

Let `D_\Gamma` be the source-normalized all-gate defect for any fixed potential for which constants/literals have zero defect. The consumed fleet04/B13 cocycle gives, at this selector,
\[
D_\Gamma(G;s)=(1-s)D_0+sD_1+\mathcal J_s,
\tag{4.1}
\]
where `J_s` is the exact local gluing defect. Since the `s=0` face is an equality state,
\[
D_0=0.
\tag{4.2}
\]
Therefore
\[
\boxed{D_\Gamma(G;s)=sD_1+\mathcal J_s.}
\tag{4.3}
\]

In the positive-denominator branch `A>0`, define
\[
c_1=-D_1/W_1\quad\text{when }W_1>0,
\]
and define the local gluing margin
\[
\ell_s=-\frac{\mathcal J_s}{K_s}
       =-\frac{\mathcal J_s}{s(1-s)E}.
\tag{4.4}
\]
If `W_1=0`, the child term below is simply omitted. Combining (3.2), (3.5) and (4.3) yields the main identity of this run.

### Theorem 4.1 — exact boundary-margin desingularization

For every actual Boolean split whose `s=0` face has `W_0=D_0=0` and whose parent has `W_G(s)>0`,
\[
\boxed{
c_G(s)
=\frac{W_1c_1+(1-s)E\,\ell_s}
       {W_1+(1-s)E}.}
\tag{4.5}
\]
In particular the vanishing factor `s` cancels **before** any limit is taken. The global gate margin is an exact convex average of the child margin and the local gluing margin.

**Proof.** From the definitions,
\[
-D_1=W_1c_1,
\qquad
-\mathcal J_s=K_s\ell_s=s(1-s)E\ell_s.
\]
Thus (4.3) gives
\[
-D_\Gamma(G;s)=sW_1c_1+s(1-s)E\ell_s.
\]
Divide only in the branch where (3.2) has already proved `W_G(s)>0`, cancel the common positive factor `s`, and obtain (4.5). The weights are nonnegative and sum to one. QED.

This resolves the algebraic singularity left open in the preceding B04 report. A selector bias tending to zero does **not** by itself create an uncontrolled owner margin. Any boundary blow-up must already be present in the normalized local gluing ratio `ell_s` (or in the fixed child, which is not changing with `s`).

## 5. Quantitative consequences

Let
\[
\omega_s=\frac{(1-s)E}{W_1+(1-s)E}.
\]
Then (4.5) can be written
\[
c_G(s)=(1-\omega_s)c_1+\omega_s\ell_s.
\tag{5.1}
\]
For `0<s<=1/2`,
\[
\boxed{
\frac{E}{2(W_1+E)}\le\omega_s\le1.
}
\tag{5.2}
\]
Hence:

1. **Uniform local bound propagates to the boundary.** If, for some finite `C`,
   \[
   D_1+C W_1\ge0
   \quad\text{and}\quad
   \mathcal J_s+C K_s\ge0
   \tag{5.3}
   \]
   for all `0<s<=s_0`, then
   \[
   \boxed{D_\Gamma(G;s)+C W_G(s)\ge0}
   \tag{5.4}
   \]
   for all such `s`. Whenever `W_G(s)>0`, this is exactly `c_G(s)<=C`. At `W_G=0` equation (5.4) remains meaningful and no quotient is formed.

2. **Boundary escape is equivalent to local escape.** If `c_1` is finite and `s_n downarrow 0`, then `c_G(s_n)` is unbounded above if and only if `ell_{s_n}` is unbounded above. The forward implication follows from convexity; the reverse follows from the positive lower weight (5.2).

3. **Finite local limit gives the exact boundary limit.** If
   \[
   \ell_s\to L\in\mathbb R,
   \]
   then
   \[
   \boxed{
   c_G(s)\to
   \frac{W_1c_1+E L}{W_1+E}.}
   \tag{5.5}
   \]
   The same statement holds in the extended-real sense for `L=+infinity` because the limiting local weight is `E/(W_1+E)>0`.

4. **Pure equality-child case.** If `W_1=0` but `E>0`, then
   \[
   \boxed{c_G(s)=\ell_s\quad\text{exactly}.}
   \tag{5.6}
   \]
   The XOR boundary family from the preceding B04 report is exactly of this type. Its apparent global `0/0` boundary issue is therefore nothing more and nothing less than the local gluing quotient.

These conclusions preserve the child defect rather than deleting it. They are precisely the correction demanded by the current state: positive descendant slack is carried with weight `sW_1`, while the new selector charge is carried by the separate physical currency `K_s`.

## 6. First nonzero numerator and denominator terms

The denominator has the exact expansion already given in (3.2):
\[
W_G(s)=s(W_1+E)-s^2E.
\tag{6.1}
\]
The numerator is also exactly decomposed, without assuming differentiability of the entropy terms:
\[
\boxed{
-D_\Gamma(G;s)
=sW_1c_1+s(1-s)E\ell_s.
}
\tag{6.2}
\]
Thus, if `ell_s -> L`, the first nonzero terms are
\[
W_G(s)=s(W_1+E)+o(s),
\]
\[
-D_\Gamma(G;s)=s(W_1c_1+EL)+o(s),
\tag{6.3}
\]
and their ratio is (5.5). No expansion of `h_2` and no illicit cancellation of child slack is required.

The directional identity (2.1) makes the denominator coefficient completely Boolean:
\[
\boxed{
W_1+E
=W_1+d(1-d)+4ab.
}
\tag{6.4}
\]
So the boundary quotient can become singular only if the **local gluing defect** is large relative to the actual physical currency `s(1-s)[d(1-d)+4ab]`; shrinking the selector probability itself is not an additional source of singularity.

## 7. What changed and the next unpaid implication

The preceding B04 report left `FEI-B04-BOUNDARY-QUOTIENT-v1`: control the global quotient when a selector bias tends to a face. The present theorem removes the spurious part of that problem.

**New proved implication:** after contracting to a Poincare-equality face, the exact global margin is the convex combination (4.5). Therefore the boundary problem reduces source-exactly to the local Bellman inequality
\[
\boxed{
\mathcal J_s+C K_s\ge0,
\qquad
K_s=s(1-s)\,[d-(q_1-q_0)^2],
}
\tag{7.1}
\]
together with the already retained child inequality. There is no separate `1/s` loss to pay.

**Next unpaid implication (`FEI-B04-LOCAL-GLUING-BOUND-v1`):** for the current surviving shaped candidate, or another finite-cap potential, prove a uniform upper bound on
\[
\ell_s=-\mathcal J_s/K_s
\]
for every actual Boolean selector pair with `K_s>0`, retaining the source-defined Boolean information credit and child defects; or construct a genuine Boolean split for which `ell_s` exceeds the proposed finite cap. This is the exact quantity recipient `fleet01/B01` can insert into its credit-augmented Bellman supersolution. A proof of (7.1) with one finite `C` would propagate through the boundary automatically by Theorem 4.1.

Assigned partner `fleet04/B04` should, when it has a completed face-contraction result, be compared directly against (4.5): any claimed boundary enclosure only needs to control `ell_s`, not the already-cancelled selector factor.

## 8. Status

This is a rigorous neighborhood/desingularization theorem, not a proof of FEI. It proves the exact first nonzero denominator term and an exact child-slack-preserving numerator decomposition at every Poincare-equality face, and it identifies the only remaining normalized boundary quantity. No retired candidate, raw-U4, unweighted-L2, or fixed-depth-KL route is used. No novelty claim is made. `full_brain_connected=false`.
