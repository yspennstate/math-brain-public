# B15 — adaptive-depth ceiling for the source-bound shared-core FEI obstruction

**Run:** `20260922T020955Z-b15-gate-extremality-r32`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Outcome:** **ESSENTIAL_STEP_APPLIED / ENTIRE ADAPTIVE-DEPTH VERSION OF THIS SHARED-CORE MECHANISM CLOSED.**  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED**.

## 0. Control, live target, and retained arithmetic input

\[
\Gamma(p_{\rm out})+\widetilde H_G(p)
\le
\sum_i {\rm It}_i(G;p)
\frac{\Gamma(p_i)+h(V_{p_i})}{V_{p_i}},
\qquad V_u=4u(1-u).
\tag{G}
\]
The old AND/decomposable extremality conjecture has already been source-validly refuted by explicit balanced composition-prime gates. The current constructive question is therefore whether the newest shared-coordinate lower-bound mechanism can force a still larger center cap, or whether that mechanism itself can be closed.

Before following the later gate target, I reread the newest source-exact fleet02/B15 valuation/KL handoff
`fleet02/B15/20260922T000114Z-harmonic-delete-kl-valuation/REPORT.md`.
Its sole unpaid harmonic-deletion remainder has the exact negative-credit form
\[
\boxed{
D_{\rm del}
=
\beta H_2(\rho)
-\mathbb E\log_2(K!)
-\mathcal K_\rho,
\qquad \mathcal K_\rho\ge0 ,
}
\tag{0.1}
\]
with the one-time signed valuation reserve
\[
R(f)\le2J(f)\le2I(f).
\tag{0.2}
\]
That report also proves on Boolean addressing functions that an unbounded valuation price cannot be recharged at every live deletion step. The factorial and KL credits in (0.1) remain live; nothing in the present argument assumes packet integrality or replaces those negative terms by a credit-free interpolation. The newer owner control simply makes the all-gate obstruction, rather than (0.1), the active shared implication.

## 1. Exact predecessor: arbitrary integer-depth shared grafts

The direct completed predecessor is
`fleet04/B17/20260922T014537Z-shared-graft-tail-closure/REPORT.md`
(blob `9eaad387fb0d3812cb2b6c65d8510afc4639ae18`), together with its exact checker blob
`58864b56c52f0f2ef76d59be4e8878fba1fdd187`.

For a balanced monotone Boolean gate with influence `I`, balanced excess ratio
\[
R=\frac{H}{I-1},
\]
and selected singleton coefficient `c`, first take a balanced disjoint self-composition of any integer depth \(d\ge1\), then apply the same source-bound nine-host shared-core transform. Put
\[
\alpha=\frac9{256},\qquad
B=\frac{257}{256},\qquad
d_0=\frac{133}{128}.
\tag{1.1}
\]
The predecessor proves the exact actual-Boolean recurrence
\[
\boxed{
R'_d-R
=
\frac{K(c^d)-d_0R}{\alpha I^d+B},
}
\tag{1.2}
\]
\[
\boxed{
I'_d=\frac{261}{128}+\alpha(I^d-1),
\qquad
c'_d=\frac{57}{256}+\frac{c^d}{256}.
}
\tag{1.3}
\]
Here
\[
K(b)
=
H_{\rm core}(b)
+\alpha[-\phi(b^2)+16(1-b^2)],
\qquad
\phi(t)=-t\log_2t,
\tag{1.4}
\]
and the 512 shared-core Fourier amplitudes are
\[
\frac{a+bq}{512}
\]
with the exact 19 multiplicity classes preserved in `CHECKER.py`.

The same predecessor certifies, for the fixed choice \(d=4\), the genuine finite Boolean gate \(F_7\) with
\[
R(F_7)>
6.5218509495504481848401605388605115013503296799038586768578.
\tag{1.5}
\]
It closes the *fixed-\(d=4\)* future tail. What remained open was the obvious materially different attack: choose the self-composition depth adaptively at every round, possibly accepting a temporary decrease in \(R\) to move the singleton coefficient to a more favorable region and gain later.

This report closes that whole adaptive-depth version of the same host/core mechanism.

## 2. New exact barycentric recurrence

The key observation is algebraic. Since every nonconstant balanced Boolean gate obeys Poincare \(I\ge1\),
\[
D_d:=\alpha I^d+B\ge \alpha+B.
\]
But
\[
\boxed{\alpha+B=\frac9{256}+\frac{257}{256}=\frac{133}{128}=d_0.}
\tag{2.1}
\]
Therefore (1.2) can be rewritten exactly as
\[
\boxed{
R'_d
=
\left(1-\frac{d_0}{D_d}\right)R
+
\frac{d_0}{D_d}\frac{K(c^d)}{d_0}.
}
\tag{2.2}
\]
The two coefficients are nonnegative and sum to one.

### Theorem 2.1 — local target convexity

For every source-valid state and every integer depth \(d\ge1\), the new balanced excess ratio lies between the old ratio and the one-dimensional local target \(K(c^d)/d_0\):
\[
\min\!\left\{R,\frac{K(c^d)}{d_0}\right\}
\le R'_d\le
\max\!\left\{R,\frac{K(c^d)}{d_0}\right\}.
\tag{2.3}
\]

Thus no sequence of depth choices can bootstrap above the supremum of the scalar function \(K(b)/d_0\) over the actually reachable \(b\)-range. Temporary decreases cannot help: every later step is again only a convex interpolation with a scalar target in the same fixed range.

This is stronger than a tail estimate for one recurrence. It changes the adaptive-depth construction problem into a one-variable global maximization.

## 3. Reachable singleton range

From (1.3), whenever \(0\le c\le1\),
\[
\frac{57}{256}\le c'\le\frac{58}{256}<\frac14.
\tag{3.1}
\]
The current source state lies in this interval. Hence the interval is forward invariant for every adaptive sequence of integer depths.

At any later step,
\[
b=c^d,
\qquad d\ge1,
\]
so
\[
\boxed{
0\le b\le\frac{58}{256}<\frac14.
}
\tag{3.2}
\]
It is therefore enough to maximize \(K\) on \([0,1/4]\). Enlarging the actual reachable set to this interval only makes the eventual upper bound safer.

## 4. New theorem: \(K\) is strictly concave on the whole relevant interval

Write one shared-core squared mass as
\[
p_s(b)=\frac{(a_s+bq_s)^2}{512^2}.
\tag{4.1}
\]
The exact 19-class table has
\[
\sum_s p_s'(b)\text{ cross term}=0,\qquad
\sum_s \frac{q_s^2}{512^2}=\alpha.
\tag{4.2}
\]

For every class with \(q_s\ne0\), exact endpoint/root checking gives
\[
\boxed{|a_s+bq_s|\ge1\quad(0\le b\le1/4).}
\tag{4.3}
\]
Hence
\[
p_s(b)\ge2^{-18}.
\tag{4.4}
\]

Differentiating \(\phi(p)=-p\log_2p\) twice along
\(p=(a+bq)^2/512^2\) gives
\[
\frac{d^2}{db^2}\phi(p_s(b))
=
-2\frac{q_s^2}{512^2}
\left(\log_2p_s(b)+\frac3{\ln2}\right).
\tag{4.5}
\]
Therefore, using (4.4) and (4.2),
\[
H_{\rm core}''(b)
\le
2\alpha\left(18-\frac3{\ln2}\right).
\tag{4.6}
\]

For the correction term in (1.4),
\[
\frac{d^2}{db^2}
\left[-\phi(b^2)+16(1-b^2)\right]
=
2\log_2(b^2)+\frac6{\ln2}-32.
\tag{4.7}
\]
On \(0<b\le1/4\), \(2\log_2(b^2)\le-8\). Combining (4.6)-(4.7),
\[
\begin{aligned}
K''(b)
&\le
2\alpha\left(18-\frac3{\ln2}\right)
+\alpha\left(-40+\frac6{\ln2}\right)\\
&=
-4\alpha
=
\boxed{-\frac9{64}<0}.
\end{aligned}
\tag{4.8}
\]
So \(K\) is strictly concave on \((0,1/4]\), continuous at zero, and has at most one interior maximizer.

## 5. Rigorous one-dimensional maximization

The standard-library interval checker uses exact `Fraction` arithmetic for the 19 Walsh classes and directed-rounding `Decimal` intervals. Every logarithm is enclosed using the atanh expansion
\[
\log y
=
2\sum_{m=0}^{N-1}\frac{z^{2m+1}}{2m+1}
+\mathcal R_N,
\qquad
z=\frac{y-1}{y+1},
\tag{5.1}
\]
with the explicit rational tail bound
\[
0\le\mathcal R_N
\le
\frac{2z^{2N+1}}{(2N+1)(1-z^2)}.
\tag{5.2}
\]

Let
\[
\ell=0.002713295,\qquad
u=0.002713296.
\tag{5.3}
\]
The checker certifies
\[
K'(\ell)>6.4196764\times10^{-10}>0,
\tag{5.4}
\]
and
\[
K'(u)<-8.0964649\times10^{-10}<0.
\tag{5.5}
\]
Strict concavity therefore puts the unique maximizer \(b_*\) inside \([\ell,u]\).

The exact interval at the left endpoint is
\[
K(\ell)
=
6.77661102602119325908967364740598536059740654719053103429817053537\ldots
\tag{5.6}
\]
and concavity gives the rigorous tangent upper bound
\[
K(b_*)
\le K(\ell)+K'(\ell)(u-\ell)
<
6.776611026021193259731641290873525012036755706723046375298803.
\tag{5.7}
\]
Consequently
\[
\boxed{
6.52185121301287772303367087870651222674036118827
<
\sup_{0\le b\le1/4}\frac{K(b)}{d_0}
<
6.52185121301287772365150440023918196647146413881.
}
\tag{5.8}
\]

The interval width here is not an empirical grid width; the upper endpoint is a proved global upper bound from strict concavity plus a rigorously signed derivative bracket.

## 6. Main consequence — every adaptive integer-depth sequence is capped

Define
\[
M:=
\sup_{0\le b\le1/4}\frac{K(b)}{d_0}.
\tag{6.1}
\]
The current source ratio is below \(M\). If \(R\le M\), then (2.2) and (3.2) imply
\[
R'_d\le
\left(1-\frac{d_0}{D_d}\right)M
+\frac{d_0}{D_d}M=M
\]
for every integer \(d\ge1\).

Induction proves:

### Theorem 6.1 — adaptive-depth shared-core ceiling

Start from the current source-valid shared-graft state. At each round choose **any** integer self-composition depth \(d_r\ge1\), allowed to depend on the entire previous history, then apply the same exact nine-host shared-core transform. Every resulting actual finite balanced monotone Boolean gate satisfies
\[
\boxed{
R_r
<
6.52185121301287772365150440023918196647146413881.
}
\tag{6.2}
\]

This includes fixed depths, changing depths, greedy depth choices, and strategies that deliberately lower the ratio on one round in an attempt to gain more later. The proof is not a search over strategies: (2.2) makes every step a convex interpolation below the same invariant scalar ceiling.

Compare the already certified \(F_7\) lower bound (1.5). The entire remaining room for **any depth-only modification of this same host/core mechanism** is less than
\[
\boxed{
2.63462429538811343861378670465121135\times10^{-7}.
}
\tag{6.3}
\]
In the owner's historical old-reference quadratic-margin units, this is less than about \(1.054\times10^{-6}\).

Thus changing only the self-composition depth cannot produce a materially larger lower bound. A further construction attack must change the shared host/core/gadget geometry or move to a genuinely different biased prime-gate mechanism.

## 7. Scope, status, and relation to full FEI

This result is **not** a universal FEI upper bound. It says nothing about arbitrary Boolean gates outside this source-bound shared-core transform family. Another prime gate, another shared-coordinate core, or a biased product point may have a larger balanced excess ratio or required gate margin.

It is also not another finite-tail computation. The fixed-\(d=4\) predecessor had already shown that \(F_8,F_9,\ldots\) under one recurrence were redundant. The present theorem closes the strictly larger family in which the integer self-composition depth may change adversarially at every step.

The exact full-problem status remains
\[
\boxed{\text{FEI OPEN / NOT PROVED}.}
\]

The next useful gate-construction work should therefore alter the physical shared-coordinate transform itself or search nonuniform-bias composition-prime gates. Repeating this nine-host transform with a different depth schedule is now analytically exhausted.

## 8. Verification and literature scope

`CHECKER.py` verifies the exact Parseval identities for the 19 source classes, the no-root condition (4.3), the analytic concavity constant \(-9/64\), the signed derivative bracket (5.4)-(5.5), the tangent upper bound, and (6.3). It exited `PASS`.

Executed checker SHA-256:
`8ce4e0f194b5da33c6ac9a8c01f713625f89850262182921d46e715045e75e82`.

Captured output SHA-256:
`98109410d4beacdaf9aea8ae08b380ccc07e772c519d61c3b99abb849916e9c8`.

Fresh primary-source checks still leave unrestricted FEI open. Potapov, arXiv:2609.21563 (18 September 2026), proves FEI for plateaued functions with sharp class constant 4 and for partially bent functions with sharp constant 2, not for arbitrary Boolean spectra. González--MacManus--Pereyra, arXiv:2606.00246 (29 May 2026), give new classes and a stopping-tree/restriction framework while explicitly retaining a key general inequality whose universal validity would imply full FEI. No novelty or publication-priority claim is made for the adaptive-depth ceiling proved here.

## 9. Collaboration/status fields

- `consumed_peer_artifact`: fleet04/B17 `20260922T014537Z-shared-graft-tail-closure/REPORT.md`, including its general integer-depth recurrence and exact 19-class checker data.
- `consumed_fleet02_B15_arithmetic_artifact`: fleet02/B15 `20260922T000114Z-harmonic-delete-kl-valuation/REPORT.md`, retaining exact residual (0.1), factorial credit and KL credit.
- `applied_to_claim`: whether changing the self-composition depth can materially extend the current shared-core FEI obstruction.
- `new_proved_inference`: every adaptive integer-depth strategy for this exact nine-host shared-core transform obeys the global cap (6.2).
- `mechanism_change`: one-dimensional concavity + invariant convex-combination ceiling, not another finite recurrence round.
- `remaining_implication`: full all-gate/all-bias finite potential or a genuinely different shared-coordinate / biased-prime construction.
- `full_problem_change`: OPEN -> OPEN.
- `full_brain_connected`: false.
