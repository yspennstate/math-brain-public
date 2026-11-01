# B18 — terminal-tautology correction and exact random-depth signed margin barycenter

**Outcome:** `ESSENTIAL_STEP_APPLIED / CIRCULAR-CRITERION_REMOVED / EXACT_SIGNED_NET_DERIVED`.

**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED**.

**Execution:** `WITHOUT_VERIFIED_BRAIN`. Authenticated GitHub controls and scientific artifacts were read directly; no authenticated installed-brain receiver/context was used.

**Runtime provenance:** model self-report `GPT-5.6 Sol`; requested effort `maximum actually supported`; configured reasoning level `UNKNOWN / NOT_EXPOSED`; provider reasoning-token/time counters `null / NOT_EXPOSED`.

## 0. Fresh control, later-owner precedence, and last-three comparison


Fresh scientific master initially observed was `d987fd311344b5d699887d7ceb1687d72114156c`.  The live stable candidate inherited from the current FEI chain is

\[
\Gamma_*(u)=\Gamma_{\rm RO}(u)+a_*u(1-u),\qquad
 a_*=0.2682048,\qquad C_*=\Gamma_*(1/2)=6.5218512.
\tag{0.1}
\]

For a Boolean gate under an interior product bias,

\[
D_\Gamma(G;p)=
\sum_i\frac{\operatorname{It}_i(G;p)}{V_{p_i}}
 [\Gamma(p_i)+h_2(V_{p_i})]
-\Gamma(p_{\rm out})-\widetilde H_G(p),
\qquad V_u=4u(1-u).
\tag{0.2}
\]

A universal proof of `D_{Gamma_*}>=0` would give full FEI with constant `C_*`.

The last three substantive B18 reports were:

1. `20260922T0204Z-depth4-shared-graft-saturation/REPORT.md`: the exact depth-four shared-core lower-bound recurrence is quantitatively exhausted.
2. `20260922T030354Z-global-shared-core-ceiling/REPORT.md`: the same shared-core amplifier is globally capped for every signed singleton parameter and adaptive depth sequence.
3. `20260922T040428Z-random-block-currency/REPORT.md`: changed mechanism to exact random fixed-size physical restrictions and proposed `EXACT-RANDOM-BLOCK-RO-DEFICIT-v1`.

**FULL-PROBLEM CHANGE before this run:** none; unrestricted FEI remained open.

**MECHANISM CHANGE in this run:** yes.  The preceding random-block criterion is first subjected to the admission gate below.  Its terminal scale is shown to be tautological as a reduction.  I then replace it by an exact signed random-depth net in which every local entropy/information term and every unit of Poincare currency is retained.

## 1. Named OTHER-account result consumed and applied

I consume fleet03/B14,

`proofnet24/P03-fei/fleet-2026-09-21/fleet03/B14/20260922T043512Z-block-restriction-cocycle/REPORT.md`.

Its source-exact physical-block theorem states, for a physical revealed block `T` with branch variable `Z=X_T`,

\[
D_\Gamma(G;p)=\mathbb E_ZD_\Gamma(G_Z;p_{T^c})
+\mathcal R_{\Gamma,T}+\mathcal C_T,
\tag{1.1}
\]

where

\[
\mathcal C_T=H(Z\mid S)+I(S;K)+\operatorname{TC}(K)\ge0
\tag{1.2}
\]

and, for the quadratic lift `Gamma_a=Gamma_0+a u(1-u)`, the exact block currency is

\[
\Omega_T=\frac14\sum_{i\in T}\operatorname{It}_i-\operatorname{Var}_Z(p_{\rm out}(G_Z)),
\qquad
W_G=\mathbb E_ZW_{G_Z}+\Omega_T.
\tag{1.3}
\]

This theorem is used below to identify the actual signed one-step summand, not merely cited.

I also use the completed fleet03/B13 theorem

`proofnet24/P03-fei/fleet-2026-09-21/fleet03/B13/20260922T043158Z-balanced-six-two-generation/REPORT.md`.

It proves that a balanced uniform six-input gate with some zero singleton Walsh coefficient is safe for `Gamma_*`; in the nonliteral-child branch it gives the quantitative defect

\[
D_{\Gamma_*}(G)>\varepsilon_6,
\qquad
\varepsilon_6=0.020451553271865.
\tag{1.4}
\]

Section 6 below converts that peer theorem into a strict bound on the new depthwise barycenter.

## 2. Admission gate: the previous existential random-block criterion contains the target itself

The preceding B18 report defined, for a uniformly random `r`-subset `A`,

\[
F_r^{\rm RO}:=\mathbb E_{A,X_A}D_{\Gamma_{\rm RO}}(G_{A=X_A}),
\qquad
P_r:=\mathbb E_{A,X_A}W(G_{A=X_A}),
\tag{2.1}
\]

and

\[
B_r^{\rm RO}=D_{\Gamma_{\rm RO}}(G)-F_r^{\rm RO},
\qquad
Q_r=P_0-P_r.
\tag{2.2}
\]

It proposed the sufficient condition that for some `1<=r<n`,

\[
B_r^{\rm RO}+a_*Q_r\ge0.
\tag{2.3}
\]

That statement is logically valid as a sufficient induction step, but the advertised range contains a terminal tautology and therefore does **not** pass the current admission gate as a smaller universal implication.

### Proposition 2.1 — terminal tautology

For every Boolean gate and every interior product bias,

\[
\boxed{
B_{n-1}^{\rm RO}+a_*Q_{n-1}=D_{\Gamma_*}(G;p).
}
\tag{2.4}
\]

### Proof

After revealing `n-1` physical coordinates, every branch depends on at most one remaining coordinate.  It is therefore a constant or a signed literal.  Constants and literals have exactly zero gate defect for the read-once potential and for the quadratic lift: for a literal the leaf term is `Gamma(p)+h_2(V_p)`, exactly canceled by the output potential and its two-point Fourier entropy; constants are the boundary-normalized zero case.  Hence

\[
F_{n-1}^{\rm RO}=0.
\tag{2.5}
\]

Likewise a constant/literal has zero Poincare currency, so

\[
P_{n-1}=0.
\tag{2.6}
\]

Substitute (2.5)--(2.6) into (2.2) and use
`D_{Gamma_*}=D_{Gamma_RO}+a_*P_0`.  This gives (2.4). `QED`

Thus choosing `r=n-1` in (2.3) asks for exactly the full target.  I therefore withdraw `EXACT-RANDOM-BLOCK-RO-DEFICIT-v1` **as a claimed reduction**.  Its identities remain correct and useful; the defect was in treating the existential scale statement as a smaller missing implication.

## 3. Exact random-depth chain

Choose a uniformly random permutation `pi` of the `n` physical coordinates and reveal the first `r` coordinates with their original product law.  Let `G_r` be the resulting random restricted gate.  Then `G_r` has exactly the same law as the uniformly random `r`-block restriction used above, so (2.1) is unchanged.

Define the signed base step and the consumed Poincare currency at depth `r` by

\[
L_r^{\rm RO}:=F_r^{\rm RO}-F_{r+1}^{\rm RO},
\qquad
\Delta_r:=P_r-P_{r+1},
\qquad 0\le r\le n-2.
\tag{3.1}
\]

The preceding B18 random-block theorem gives, with
`W_k=sum_{|S|=k} \widehat G_p(S)^2`,

\[
\boxed{
\Delta_r=
\frac1{4n}\sum_{k\ge2}kW_k
\left[1-\frac{(r)_{k-1}}{(n-1)_{k-1}}\right].
}
\tag{3.2}
\]

If `P_0>0`, some `W_k>0` for `k>=2`.  For every `r<=n-2`, the falling-factorial ratio in (3.2) is strictly below one for that `k`.  Therefore

\[
\boxed{\Delta_r>0\quad(0\le r\le n-2)}
\tag{3.3}
\]

for every nonaffine gate with positive Poincare currency.

Because `F_{n-1}^{RO}=P_{n-1}=0`, telescoping gives

\[
\boxed{D_{\Gamma_{\rm RO}}(G)=\sum_{r=0}^{n-2}L_r^{\rm RO}},
\qquad
\boxed{P_0=\sum_{r=0}^{n-2}\Delta_r}.
\tag{3.4}
\]

This is already an exact finite signed NET identity: no positive part has been taken and no terminal continuation has been discarded.

## 4. Source-exact form of each signed step

Condition on a depth-`r` branch `H=G_r` and let `j` be the next uniformly random unrevealed physical coordinate.  Apply fleet03/B14's theorem with the singleton block `T={j}`.  Let `Z=X_j`; let `S` denote the outside spectral support variable in the source block decomposition; and let `K in {0,1}` denote the block Fourier-inclusion bit.  The marginal of `K` is the biased spectral influence `It_j`.

For a singleton, `TC(K)=0`, so

\[
\mathcal C_j=H(Z\mid S)+I(S;K).
\tag{4.1}
\]

Fleet03/B14's explicit remainder and the identities

\[
H(Z\mid S)=h_2(p_j)-I(Z;S),
\qquad
I(S;K)=h_2(\operatorname{It}_j)-H(K\mid S)
\tag{4.2}
\]

cancel the two standalone entropy terms in its remainder.  The complete one-step signed quantity is therefore

\[
\boxed{
\begin{aligned}
\ell_{\rm RO}(H,j):={}&
\mathbb E_Z\Gamma_{\rm RO}(p_{\rm out}(H_Z))
-\Gamma_{\rm RO}(p_{\rm out}(H))\\
&+\frac{\operatorname{It}_j(H)}{V_{p_j}}
 [\Gamma_{\rm RO}(p_j)+h_2(V_{p_j})]\\
&-I(Z;S)-H(K\mid S).
\end{aligned}}
\tag{4.3}
\]

and averaging over the genuine restriction process gives

\[
\boxed{L_r^{\rm RO}=\mathbb E\,\ell_{\rm RO}(G_r,\pi_{r+1}).}
\tag{4.4}
\]

Equation (4.3) is important for admission: both information terms remain with their **negative signs**; the output-potential Jensen term retains its sign; the physical-coordinate leaf price retains the original `It_j/V_{p_j}` normalization; and the random depth uses the actual Boolean restrictions.  There is no unsigned spectral surrogate and no receiver-only charge.

For the stable lift, linearity of the exact quadratic currency gives

\[
F_r^*=F_r^{\rm RO}+a_*P_r,
\tag{4.5}
\]

hence

\[
\boxed{
F_r^*-F_{r+1}^*=L_r^{\rm RO}+a_*\Delta_r.
}
\tag{4.6}
\]

## 5. New theorem: the global correction is a Poincare-currency barycenter of signed depth requests

Assume `P_0>0`.  Define the exact requested base correction at depth `r` by

\[
\lambda_r:=-\frac{L_r^{\rm RO}}{\Delta_r}
\tag{5.1}
\]

and the positive weights

\[
w_r:=\frac{\Delta_r}{P_0}.
\tag{5.2}
\]

By (3.3)--(3.4), `w_r>0` and `sum_r w_r=1`.

### Theorem 5.1 — random-depth signed margin barycenter

For every Boolean gate with positive Poincare currency and every interior product bias,

\[
\boxed{
-\frac{D_{\Gamma_{\rm RO}}(G;p)}{P_0}
=\sum_{r=0}^{n-2}w_r\lambda_r.
}
\tag{5.3}
\]

Equivalently, the stable defect is the exact signed net

\[
\boxed{
D_{\Gamma_*}(G;p)
=\sum_{r=0}^{n-2}\Delta_r\,[a_*-\lambda_r].
}
\tag{5.4}
\]

The weights have the explicit source-spectrum form

\[
\boxed{
w_r=
\frac{\sum_{k\ge2} kW_k
 [1-(r)_{k-1}/(n-1)_{k-1}]}
 {n\sum_{k\ge2}(k-1)W_k}.}
\tag{5.5}
\]

### Proof

Equations (5.3)--(5.4) follow immediately from the two telescoping identities (3.4), the definitions (5.1)--(5.2), and `D_*=D_RO+a_*P_0`.  Formula (5.5) is (3.2) divided by

\[
P_0=\frac14\sum_{k\ge2}(k-1)W_k.
\]

The weights sum to one either by telescoping or directly from the falling-factorial hockey-stick identity. `QED`

This theorem is the admitted replacement for the terminal-scale existential statement.  It does **not** claim that each `lambda_r` is bounded.  Fleet03/B13's preceding bent-swap construction already shows that pointwise local correction requests can be arbitrarily large.  The exact target is instead their **currency-weighted signed average**, with later child slack and negative information terms intact.

## 6. Quantitative application of the completed fleet03/B13 six-bit theorem

Take a balanced uniform six-input nonaffine gate having some zero singleton Walsh coefficient, in the nonliteral-child branch of fleet03/B13 Theorem 5.1.  That peer theorem gives

\[
D_{\Gamma_*}(G)>\varepsilon_6=0.020451553271865.
\tag{6.1}
\]

For a balanced six-input gate,

\[
P_0=\frac{I(G)-1}{4}\le\frac{6-1}{4}=\frac54.
\tag{6.2}
\]

Let

\[
\bar\lambda:=\sum_{r=0}^{4}w_r\lambda_r
=-\frac{D_{\Gamma_{\rm RO}}(G)}{P_0}.
\]

By (5.4), `D_*=P_0(a_*-bar_lambda)`, so (6.1)--(6.2) give the strict source-valid bound

\[
\boxed{
\bar\lambda
<a_*-\frac{4}{5}\varepsilon_6
=0.251843557382508.
}
\tag{6.3}
\]

Thus the entire fleet03/B13 zero-singleton six-bit slice lies a definite distance below the stable scalar centre **in the actual signed random-depth barycenter**, not merely in a root ratio.  The literal-child exceptional cases in that report are separately safe and do not weaken the statement that this structured slice cannot be a stable-candidate falsifier.

This is a substantive use of a completed OTHER-account result in the new mechanism.

## 7. Exact remaining universal implication and failed stronger routes

For positive currency define

\[
c_{\rm depth}(G;p):=\sum_{r=0}^{n-2}w_r\lambda_r.
\tag{7.1}
\]

The first unpaid universal statement is now exactly

> **WEIGHTED-RANDOM-DEPTH-MARGIN-v1.** For every finite-arity composition-prime Boolean gate and every interior product bias with `P_0>0`,
> \[
> \boxed{c_{\rm depth}(G;p)\le a_*=0.2682048.}
> \tag{7.2}
> \]

By Theorem 5.1 this is equivalent to the stable all-gate target, so I do **not** relabel it as a reduction or as proof progress by itself.  Its value is that it is now a source-exact NET with all signs, information terms, physical coordinate prices, depth multiplicities, and terminal cancellation explicit.

A genuinely smaller sufficient induction statement would have to control a **proper stopped prefix together with the actual terminal defects**, for example

\[
D_{\Gamma_*}(G)-\mathbb E D_{\Gamma_*}(G_\tau)
=\mathbb E\sum_{r<\tau}\Delta_r(a_*-\lambda_r),
\tag{7.3}
\]

for a realizable stopping time `tau` before the one-variable terminal, while retaining `E D_*(G_tau)` rather than discarding it.  Fleet03/B13 shows why demanding every local or every prefix remainder to be nonnegative is too strong: negative local information loss can be paid by genuine child slack.  Thus the next proof must exploit compensation across depths/branches, not revive a pointwise local cap.

### Failed/retired statements preserved

- `EXACT-RANDOM-BLOCK-RO-DEFICIT-v1` with `r=n-1` admitted is **circular as a reduction** by Proposition 2.1.  Its algebraic identities are not false.
- A pointwise bound `lambda(H,j)<=a_*` is not a viable universal route; the completed bent-swap restriction construction gives unbounded local requests.
- Dropping `I(Z;S)` or `H(K|S)` from (4.3), taking positive parts, or replacing the actual restriction process by an unsigned row law is not authorized by the exact cocycle.

## 8. PROVED / CONDITIONAL / OPEN ledger

**PROVED in this run**

1. Terminal-tautology identity (2.4), showing the preceding existential scale criterion was not a smaller implication.
2. Positive exact depth currencies (3.2)--(3.3) for every nonaffine source.
3. Source-exact signed singleton step (4.3)--(4.4), obtained by applying fleet03/B14 and preserving both negative information terms.
4. Random-depth signed margin barycenter (5.3)--(5.5).
5. Quantitative application (6.3) to the completed fleet03/B13 zero-singleton balanced six-bit slice.

**CONDITIONAL / sufficient only**

- Any proper stopping theorem proving (7.3) nonnegative while terminal defects are already certified would give an induction step.  No such universal stopping theorem is proved here.

**OPEN**

- `WEIGHTED-RANDOM-DEPTH-MARGIN-v1`, equivalently `D_{Gamma_*}>=0` for every composition-prime gate and every interior product bias.
- Hence full uniform-cube FEI.

## 9. Literature status

A fresh September-22 search found no unrestricted FEI proof.  Potapov's September 18, 2026 paper proves FEI for plateaued functions (sharp class constant 4) and partially bent functions (sharp class constant 2).  González--MacManus--Pereyra's 2026 stopping/restriction paper explicitly leaves its universal restriction inequality conditional.  These searches support scope checking only; absence of a hit is not a novelty or openness proof.

## 10. Next attack

The next B18 calculation should attack (7.3) with a **two-generation or adaptive-depth compensation functional**, not another pointwise local bound.  The natural exact object is the signed pair

\[
(\,L_r^{\rm RO},\Delta_r\,)
\]

conditioned on the random depth-`r` child, together with that child's already-certified defect.  The goal is to prove a source-valid amortized inequality in which an above-`a_*` local request must create enough positive child defect or enough future Poincare currency to repay itself.  Fleet03/B13 proves this mechanism on one nontrivial six-bit slice; the universal version is the first missing implication.
