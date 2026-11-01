# B18 FEI rigidity/adaptive integration — conditional label contraction at the support-balanced reveal

**Run:** `20260921T231012Z-b18-fei-r15`  
**Execution:** **WITHOUT_VERIFIED_BRAIN**  
**Status:** **PARTIAL. Full uniform-cube Fourier entropy--influence remains OPEN / NOT PROVED.**  
**Claim level:** new universal information-theoretic lemma plus a source-exact composition with completed FEI interface-A/B results. No novelty or publication-priority claim.

## 0. What changed

The current interface-B ledger had already made two formerly large objects influence-relative at the same support-balanced Bernoulli reveal:

1. the actual-anchor signed correction `Gamma(A)`;
2. the unresolved robust trigger-incidence load `L_R^surv(A)`.

The branch-character label `T` from the all-row proxy-gauge theorem was still listed as an unpaid Shannon term, through the external mixed-boundary bank `P_ext`. This run proves that **once the support-balanced physical block has already been revealed, only the conditional uncertainty of that label remains, and that conditional uncertainty contracts by exactly the survival factor**.

At the B12 balanced survival probability
\[
s_*=\frac{J}{4M}\le\frac12,
\]
this removes the need for a separate hypothesis `P_ext=O(J)`: the factor `s_*` converts the a priori bound `P_ext<=4M` into an `O(J)` payment.

The resulting simultaneous auxiliary overhead is
\[
\boxed{
\mathbb E\left[
\Gamma(A)+L_R^{\rm surv}(A)+H(T\mid X_A,A)
\right]
\le \frac{299}{112}J.
}
\]
This does **not** pay the Fourier-Shannon/corrected-entropy decrement of the physical reveal itself. Full FEI therefore remains open.

## 1. Exact completed inputs used

All scientific paths below are under `proofnet24/P03-fei/fleet-2026-09-21/`.

1. **fleet01/B18 folded cooling compiler**  
   `fleet01/B18/20260921T2205Z-folded-cooling-compiler/REPORT.md`, report blob `9f2bb40584be20e5e440e7f3913873c34858bc91`.  
   Used for the character-invariant folded activation potential, free descendant re-centering, and the globally nonreused activation telescope. It leaves the local certificate upper bound on corrected entropy as a genuine obligation.

2. **fleet04/B12 posterior-balanced anchor code**  
   `fleet04/B12/20260921T223746Z-posterior-balanced-anchor-code/REPORT.md`.  
   With
   \[
   M=\frac14\sum_{i\ne k}p_{ik},\qquad M\ge\frac J2,
   \]
   and
   \[
   s_*=\frac{J}{4M},\qquad t_*=1-s_*,
   \]
   it proves
   \[
   \mathbb E\Gamma(A_{t_*})
   \le \frac J2-\frac{J^2}{8M},
   \]
   \[
   \mathbb E L_R^{\rm surv}(A_{t_*})
   \le \frac{J^2}{7M},
   \]
   and hence
   \[
   \boxed{
   \mathbb E[\Gamma+L_R^{\rm surv}]
   \le \frac J2+\frac{J^2}{56M}.
   }
   \tag{1.1}
   \]

3. **fleet04/B13 proxy-gauge closure**  
   `fleet04/B13/20260921T2225Z-proxy-gauge-closure/REPORT.md`, report blob `1ec1555932e690e403f7d4320640040628697b96`.  
   After one source-frontier reveal, it constructs the branch character
   \[
   T(z)=\{r:q_r(z)=1\}
   \]
   and proves exact residual influence
   \[
   \mathbb E_z I(\chi_{T(z)}f_{B=z})
   =\sum_{r\in S}e_r
   \le \mathcal D(f).
   \]
   It explicitly leaves the label/reveal Shannon cost unpaid.

4. **fleet01/B13 label-boundary theorem**  
   `fleet01/B13/20260921T223500Z-label-boundary-curvature/REPORT.md`, report blob `7ef3c7b171d03943818ba28cc96f71442b9d30fa`.  
   It proves `H(Y)<=I(Y)` for every finite-valued deterministic label on a uniform cube. Applied to `T`, its reciprocal-component refinement gives, at the live robustness scale `delta=1/16`,
   \[
   I(T)
   \le \frac{17}{8}J+\frac{15}{14}\mathcal P_{\rm ext}.
   \tag{1.2}
   \]
   The displayed report states the entropy consequence; (1.2) is the stronger intermediate inequality in the same proof, before applying `H(T)<=I(T)`.

5. **fleet04/B14 recursive certified peeling**  
   `fleet04/B14/20260921T221102Z-recursive-certified-peeling/REPORT.md`, report blob `253268f70202891aa12c36d2ff4cf76519fa8241`.  
   It recursively pays every currently `q/(16r)`-certifiable maximum row with total physical Shannon decrement at most `12J`, leaving the explicit terminal geometric obstruction.

6. **fleet04/B18 mixed-curvature rigidity and the scalar terminal reduction**  
   `fleet04/B18/20260921T221132Z-support-depth-stalled-core/REPORT.md`, report blob `496b62576a50af809beddde4f0e1901d4358a486`, and  
   `fleet04/B18/20260921T223832Z-defect-adaptive-certificate/REPORT.md`.  
   Used for
   \[
   \kappa_{ik}=p_{ik}+4o_{ik},\qquad
   \sum_{i\ne k}\kappa_{ik}=4d_k,
   \]
   the support/orientation split, the exact zero-defect one-point classification, and the scalar positive-defect floor at a terminal maximum row.

7. **fresh compatible fleet02/B14 asymmetric short-circuit theorem**  
   `fleet02/B14/20260921T230653Z-asymmetric-shortcircuit-ledger/REPORT.md`.  
   It now permits fixed-relative false negatives in a coefficient-12 full-block step and localizes the surviving physical-reveal obstruction to outside false-positive pollution. Its own remaining universal arrow is an upper corrected-entropy estimate for the same realizable short-circuit tree,
   \[
   \Delta_T\mathcal F\le K r q.
   \tag{1.3}
   \]

Known refuted bridges remain excluded: `sum_i d_i=O(J)`, prescribed-coordinate payment, replacing `q/(16r)` by an unconditional `q/16` full-block theorem, ambient-alphabet Fannes continuity, unconditional `R_pref=O(I)`, and deletion of total-correlation/negative-credit terms.

## 2. New universal theorem: independent reveal contracts label entropy by the surviving edge boundary

Let
\[
Y:\{0,1\}^m\to\mathcal Y
\]
be any deterministic finite-valued label. Let
\[
I_k(Y)=\Pr(Y(Z)\ne Y(Z\oplus e_k)),
\qquad
I(Y)=\sum_k I_k(Y),
\]
for uniform `Z`.

Choose a random revealed coordinate set `A` independently of `Z`, leaving coordinate `k` unrevealed with probability `s_k` independently across `k`.

### Theorem 2.1 — weighted conditional-label contraction

\[
\boxed{
\mathbb E_A H(Y\mid Z_A,A)
\le
\sum_{k=1}^m s_k I_k(Y).
}
\tag{2.1}
\]

In particular, if every coordinate survives with the same probability `s`,
\[
\boxed{
\mathbb E_A H(Y\mid Z_A,A)
\le s I(Y).
}
\tag{2.2}
\]

### Proof

Fix one realized set `A` and one revealed value `z_A`. The remaining coordinates form a uniform cube. Apply the already proved partition entropy/edge-boundary inequality to the restricted label:
\[
H(Y\mid Z_A=z_A)
\le
\sum_{k\notin A}
I_k(Y\mid Z_A=z_A).
\tag{2.3}
\]

Average (2.3) over `z_A`. For each fixed `k\notin A`, the restriction event depends only on coordinates other than `k`, so averaging the restricted `k`-edge disagreement over all fibers reconstructs the original edge disagreement:
\[
\mathbb E_{z_A}I_k(Y\mid Z_A=z_A)=I_k(Y).
\tag{2.4}
\]
Hence
\[
H(Y\mid Z_A,A)
\le \sum_{k\notin A}I_k(Y).
\tag{2.5}
\]
Finally average over the independent random set `A`. Coordinate `k` appears on the right with probability `s_k`, giving (2.1). The uniform case gives (2.2). QED.

This theorem is all-dimensional, makes no Boolean-spectrum assumption, and has no alphabet-size or ambient-dimension factor.

## 3. Apply the theorem to the B13 source-frontier character label

Use the B13 source-frontier label
\[
T(z)=\{r:q_r(z)=1\}.
\]

At robustness `delta=1/16`, the fleet01/B13 edge calculation gives
\[
I(T)\le \frac{17}{8}J+\frac{15}{14}\mathcal P_{\rm ext}.
\tag{3.1}
\]

By definition,
\[
\mathcal P_{\rm ext}
=
\sum_{r\in S}\sum_{k\in F_r\setminus C_r}p_{rk}
\le
\sum_{i\ne k}p_{ik}
=4M.
\tag{3.2}
\]

Now reveal each physical coordinate with probability `t_*=1-s_*`, where the B12 support-balanced survival is
\[
s_*=\frac{J}{4M}.
\]
The label depends only on its physical control block; revealing coordinates outside that block is irrelevant to (2.2). Therefore
\[
\begin{aligned}
\mathbb E H(T\mid X_{A_{t_*}},A_{t_*})
&\le s_* I(T)\\
&\le \frac{17}{8}s_*J
+\frac{15}{14}s_*\mathcal P_{\rm ext}\\
&\le \frac{17}{8}s_*J+\frac{15}{14}J.
\end{aligned}
\tag{3.3}
\]

Since `M>=J/2`, `s_*<=1/2`, and thus
\[
\boxed{
\mathbb E H(T\mid X_{A_{t_*}},A_{t_*})
\le \frac{239}{112}J
=2.1339285714\ldots\,J.
}
\tag{3.4}
\]

The conditioning is essential. This theorem does **not** claim that the unconditional label entropy is `O(J)` by itself. It says that after the same physical block used by the support-balanced interface has already been revealed, the **additional unresolved character-label information** is universally linear in `J`.

If a source representative itself is revealed by `A`, its later character bit is no longer needed; retaining it in `T` only overcounts the actual residual label, so (3.3) remains conservative.

## 4. New simultaneous three-channel budget at one physical reveal

Combine (3.3) with the B12 exact same-reveal budget (1.1). Since
\[
\frac{J^2}{56M}
=\frac{s_*}{14}J,
\]
we obtain
\[
\begin{aligned}
&\mathbb E\left[
\Gamma(A_{t_*})
+L_R^{\rm surv}(A_{t_*})
+H(T\mid X_{A_{t_*}},A_{t_*})
\right]\\
&\qquad\le
\left[
\frac12+\frac{15}{14}
+\left(\frac1{14}+\frac{17}{8}\right)s_*
\right]J\\
&\qquad=
\left[
\frac{11}{7}+\frac{123}{56}s_*
\right]J\\
&\qquad\le
\boxed{\frac{299}{112}J}.
\end{aligned}
\tag{4.1}
\]

Thus one and the same support-balanced Bernoulli reveal simultaneously makes all three of these auxiliary channels influence-relative:

- signed actual-anchor correction;
- unresolved robust trigger incidence/address capacity;
- unresolved source-frontier character-label information.

No step assumes `M=O(J)`, `P_ext=O(J)`, `sum d_i=O(J)`, bounded ambient dimension, or a fixed number of components.

Because the left side is nonnegative, averaging also implies the existence of a deterministic realized physical block with auxiliary overhead at most `299J/112`. This existence statement by itself does not certify that block's Fourier-Shannon decrement.

## 5. Compatibility with the adaptive folded-activation budget

The fleet01/B18 folded activation potential is character invariant and its adaptive physical drop is nonnegative and globally telescoping:
\[
\sum_u w_u\Lambda_u\le J(f_{\rm root}).
\]

Therefore using the support-balanced reveal does not introduce a new gauge-leakage term. At a realized block `A`,
\[
\Delta_A\mathcal G_\lambda
\le E_A-\lambda\Lambda_A
\le B_A.
\tag{5.1}
\]

The new result pays the three **auxiliary source/label channels** in (4.1), but it does not upper-bound `B_A`, `E_A`, or the corresponding corrected-entropy decrement for this arbitrary balanced block. That distinction prevents a conditional interface from being promoted to unconditional FEI closure.

The fresh fleet02/B14 result sharpens where this unpaid physical term lives. Its asymmetric full-block theorem already pays the branch with
\[
E^-\le q/16,\qquad E^+\le q/[8(r+1)],
\]
while its random-order short-circuit analysis leaves the explicit local target
\[
\Delta_T\mathcal F\le K r q
\]
in the fixed-relative outside-pollution branch. The present label-contraction theorem is compatible with that tree, but does not prove this corrected-entropy estimate.

## 6. Zero-defect endpoint and status ledger

**PROVED / preserved:** if every relevant derivative row has zero normalized depth defect, the completed B18 rigidity theorem classifies the function, after median-character folding and irrelevant-coordinate deletion, as a character-twisted one-point defect. That branch satisfies `H<4J`.

**PROVED / new:** weighted conditional-label contraction (2.1), including the uniform factor-`s` contraction (2.2).

**PROVED / new composition:** the source-frontier character label has residual conditional entropy at most `239J/112` after the support-balanced reveal, with no hypothesis `P_ext=O(J)`.

**PROVED / new composition:** actual-anchor correction + surviving robust trigger load + residual character-label uncertainty are jointly at most `299J/112` in expectation at one and the same reveal.

**OPEN / unpaid:** a universal upper corrected-entropy/Fourier-Shannon payment for that physical reveal or for the fresh asymmetric random-order short-circuit tree in the remaining outside-pollution terminal class.

**OPEN / unpaid:** any positive-defect/off-trigger remainder not already absorbed by the completed source-frontier, factorial, crossing, activation, or asymmetric short-circuit banks.

**REFUTED and not reused:** the bridges listed at the end of Section 1.

Therefore full uniform-cube FEI remains **OPEN / NOT PROVED**.

## 7. Decisive calculation

A checker accompanying this report tests the new general label theorem independently of the FEI algebra.

- Exhaustive binary labels on cubes of dimensions `1,2,3`, at six uniform survival probabilities: `1656` inequalities, zero violations.
- `2000` deterministic pseudorandom finite-valued labels on dimensions `1..4` with independent nonuniform coordinate survival probabilities: zero violations.
- Maximum numerical ratio `LHS/RHS` was `1.0000000000000002`, showing equality/tightness cases are present up to floating roundoff.
- The derived constants are `239/112 = 2.1339285714285716` and `299/112 = 2.6696428571428572`.

These calculations are regression/falsification evidence only. The theorem is proved analytically above.

## 8. Smallest honest next arrow

The label bank is no longer the reason the balanced support reveal fails to close interface A/B. The smallest remaining universal implication is now a **physical corrected-entropy theorem**:

> in the terminal positive-defect/outside-pollution regime, prove that either a realizable physical block/short-circuit tree satisfies a universal upper bound on its corrected entropy decrement in the scale already paid by crossing/activation, or the positive defect forces a complementary already-paid branch.

For the freshest asymmetric short-circuit mechanism, the concrete target is the source-exact estimate
\[
\Delta_T\mathcal F\le K r q
\]
with universal `K`, retaining its false-positive survival ledger and all existing refunds. Proving that arrow would allow the current folded-activation compiler to absorb the remaining physical restriction cost without resurrecting any refuted bridge.
