# fleet04/B13 — exact Poincare Bellman margin and a nonreusing exceptional-row tree

**Classification:** `ESSENTIAL_STEP_APPLIED / OWNER_MARGIN_LOCALIZATION / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Novelty/publication priority:** not assessed; no priority claim.

## 0. Live target and the exact change this run

The current owner control, revision `2026-09-22.2`, asks the FEI workers to converge on the all-gate formulation and to compare gates using the owner-normalized margin

\[
 c_G(p)=-\frac{D_\Gamma(G;p)}{P(G;p)},
 \qquad
 P(G;p):=\frac{I(G;p)}4-p_{\rm out}(1-p_{\rm out}),
\]

rather than raw defect. The owner also records that the blind singleton induction `local defect >= 0` is false and explicitly says the child slack has to be retained.

This report identifies the exact currency which retains that slack. For every genuine singleton restriction, the Poincare denominator itself has a nonnegative local increment. Consequently the **global owner margin is an exact convex average of singleton local margins** over any full physical restriction tree. This replaces the false target `local defect >= 0` by the strictly weaker and correctly normalized local target

\[
 \boxed{\mathcal J_{\Gamma,k}+C_*K_k\ge0.}
\]

If this holds for every actual Boolean restriction pair with `C_*` equal to the two-input AND margin, then every gate has owner margin at most the AND margin. This is exactly the child-slack-preserving form of the owner's decomposable/AND-extremality job.

The same Poincare currency also yields a source-exact adaptive elimination theorem: internal rows are paid in actual influence, while near-always-pivotal exceptional rows terminate as near-literals with a variance-weighted error budget. No ambient-dimension factor occurs and no coordinate is reused along a branch.

## 1. Newest compatible other-account result consumed

The named newest compatible peer result consumed substantively is

`proofnet24/P03-fei/fleet-2026-09-21/fleet03/B13/20260922T093915Z-safe-direction-coercivity/REPORT.md`

read from scientific snapshot `3e619ff7cfd0b321b1b43d2ad52f2d5e71bde005`.

It starts from fleet01/B14's universally safe singleton repair

\[
 \eta(p)=2V_p-V_p^2-\varepsilon V_p^3,
 \qquad
 \varepsilon=\frac{113009}{5000000}=0.0226018,
 \qquad V_p=4p(1-p),
\]

and proves the exact singleton recurrence

\[
 M_\eta(G)=qM_\eta(G_0)+tM_\eta(G_1)+L_k,
\]

where, writing `d=|E G_0-E G_1|` and `delta=Pr(G_0 != G_1)`,

\[
 L_k\ge r_0 d\,t(1-t)(2-d)
       +\left(\delta-\frac d2\right)\eta(t),
\]

with the certified continuum constant

\[
 r_0=
 \frac{1999313322941}{16492674416640000000}
 =1.2122432495992445\times10^{-7}.
\]

The peer used this to prove strict positivity of `M_eta` on every nonliteral gate. The present run changes the argument in two exact ways:

1. it identifies the owner's Poincare denominator as an **exact nonreusing singleton currency** `K_k`; and
2. it compares the peer's local repair currency to that owner currency, proving
   \[
   \boxed{L_k\ge4r_0K_k}
   \]
   and hence the global all-row coercivity
   \[
   \boxed{M_\eta(G;p)\ge4r_0P(G;p)}.
   \]

Thus the peer's one-coordinate stability is converted into an all-row, tree-level, owner-margin statement rather than remaining a per-row estimate.

## 2. Exact Poincare singleton recurrence

Fix an actual input coordinate `k` with bias

\[
 t=p_k,\qquad q=1-t.
\]

Let `G_0,G_1` be the two actual Boolean restrictions. Write

\[
 r_b=\Pr(G_b=1),\qquad
 r=qr_0+tr_1,
\]

and set

\[
 s=|r_1-r_0|,
 \qquad
 \delta=\Pr(G_0\ne G_1).
\]

Actual Booleanity gives

\[
 0\le s\le\delta\le1.
\]

Let `I(G;p)=sum_i It_i(G;p)` be the biased spectral influence used in the all-gate formula. For every coordinate `i != k`, pivotality averages exactly over the two physical branches, while the pivot contributes

\[
 It_k(G;p)=V_t\delta=4tq\delta.
\]

Therefore

\[
 I(G;p)=qI(G_0;p_{-k})+tI(G_1;p_{-k})+4tq\delta.
\tag{2.1}
\]

The Bernoulli variance satisfies the exact law of total variance

\[
 r(1-r)=q r_0(1-r_0)+t r_1(1-r_1)+tq(r_1-r_0)^2.
\tag{2.2}
\]

Subtracting (2.2) from one quarter of (2.1) gives the new recurrence.

### Theorem 2.1 — Poincare Bellman currency

For every finite Boolean gate, every interior product bias and every actual pivot,

\[
 \boxed{
 P(G;p)=qP(G_0;p_{-k})+tP(G_1;p_{-k})+K_k,
 }
\tag{2.3}
\]

where

\[
 \boxed{
 K_k=tq\,(\delta-s^2)\ge0.
 }
\tag{2.4}
\]

Moreover

\[
 \boxed{
 K_k\ge tq\,\delta(1-\delta)
       =\frac14\,It_k(G;p)(1-\delta).
 }
\tag{2.5}
\]

because `s<=delta` implies `s^2<=delta^2`.

This is exactly the owner's denominator currency. It is physical, branch-local, and contains no coordinate-count factor.

## 3. Exact owner-margin Bellman principle

Fleet04/B17's source-exact restriction cocycle, already consumed in the preceding B13 work, is

\[
 D_\Gamma(G)
 =qD_\Gamma(G_0)+tD_\Gamma(G_1)+\mathcal J_{\Gamma,k},
\tag{3.1}
\]

where

\[
 \mathcal J_{\Gamma,k}
 =\mathcal R_{\Gamma,k}+\mathcal C_k
\]

and `C_k=H(B|S)+I(S;J)>=0` is the actual Boolean information credit. No credit is discarded here.

Take any finite physical singleton restriction tree which keeps revealing genuinely active original coordinates until each leaf is constant or a literal. Let `pi_v` be the probability of reaching internal node `v`, and let `K_v` and `J_v` be its currencies from (2.4) and (3.1).

Telescoping (2.3) and (3.1) gives

\[
 \boxed{
 P(G)=\sum_v\pi_vK_v,
 \qquad
 D_\Gamma(G)=\sum_v\pi_v\mathcal J_v.
 }
\tag{3.2}
\]

Constants and literals have both `P=0` and `D_Gamma=0`.

There is no hidden zero-denominator local obstruction. If `K_v=0`, then, since `t,q>0`,

\[
 \delta=s^2.
\]

But `s<=delta`. For `0<delta<1`, `s=sqrt(delta)>delta`, impossible. Hence either:

* `delta=0`, in which case the two Boolean children agree pointwise and the pivot is dummy; or
* `delta=1` and `s=1`, in which case the two children are opposite constants and the parent is a literal.

In either case the exact defect cocycle has `J_v=0`.

Therefore every nonzero term admits the local normalized margin

\[
 c_v^{\rm loc}:=-\frac{\mathcal J_v}{K_v}.
\]

### Theorem 3.1 — global margin is a convex average of local margins

Whenever `P(G)>0`,

\[
 \boxed{
 c_G
 =-\frac{D_\Gamma(G)}{P(G)}
 =\sum_{v:K_v>0}
   \frac{\pi_vK_v}{P(G)}\,c_v^{\rm loc}.
 }
\tag{3.3}
\]

The displayed weights are nonnegative and sum to one.

### Consequence for the owner's AND-extremality target

The false blind induction asked for `J_{Gamma,k}>=0` at every pivot. The exact child-slack-preserving target is instead

\[
 \boxed{
 \mathcal J_{\Gamma,k}+C_*K_k\ge0
 \quad\text{for every actual Boolean restriction pair.}
 }
\tag{3.4}
\]

If (3.4) is proved with `C_*` equal to the owner-comparable two-input AND margin for the same base potential, then (3.3) immediately gives

\[
 c_G\le C_*
\]

for every gate of every arity. This is exactly the desired extremality conclusion. Conversely, any global gate with margin above `C_*` forces at least one actual physical pivot in its full restriction tree with local margin above `C_*`.

Thus the full gate search localizes to the source-exact singleton gluing ratio **without dropping the children's accumulated slack**.

## 4. Peer safe direction dominates the owner denominator

Return to the fleet03/B13 peer theorem. In its mean notation

\[
 d=|\mathbb EG_0-\mathbb EG_1|=2s.
\]

Hence its local lower bound becomes

\[
 L_k\ge
 4r_0tq\,s(1-s)+(\delta-s)\eta(t).
\tag{4.1}
\]

The same peer proves

\[
 \eta(t)\ge(1-\varepsilon)V_t
 =4(1-\varepsilon)tq.
\tag{4.2}
\]

Therefore

\[
\begin{aligned}
 L_k
 &\ge4tq\bigl[r_0s(1-s)+(1-\varepsilon)(\delta-s)\bigr]\\
 &\ge4r_0tq\bigl[s(1-s)+(\delta-s)\bigr]\\
 &=4r_0tq(\delta-s^2)\\
 &=\boxed{4r_0K_k},
\end{aligned}
\tag{4.3}
\]

because `r_0<1-epsilon`.

Numerically,

\[
 \boxed{
 4r_0=
 \frac{1999313322941}{4123168604160000000}
 =4.848972998396978\times10^{-7}.
 }
\tag{4.4}
\]

Telescoping the exact recurrences now gives:

### Theorem 4.1 — global owner-denominator coercivity of the safe repair

For every finite Boolean gate and every interior product bias,

\[
 \boxed{
 M_\eta(G;p)\ge4r_0P(G;p).
 }
\tag{4.5}
\]

Thus the safe direction has no merely qualitative positivity: on every genuine owner-margin denominator it supplies a universal positive fraction of that exact denominator. In particular, adding `lambda eta` changes every owner margin by

\[
 c_{\Gamma+\lambda\eta}(G;p)
 =c_\Gamma(G;p)-\lambda\frac{M_\eta(G;p)}{P(G;p)}
 \le c_\Gamma(G;p)-4r_0\lambda.
\tag{4.6}
\]

This does **not** by itself bound the original margins; it says that the peer repair direction is quantitatively nondegenerate in the exact normalization the owner requested.

## 5. Nonreusing adaptive elimination including exceptional rows

The Poincare currency also gives a direct interface-B style theorem with no small-measure-times-dimension term.

Fix `tau in (0,1)`. At a nonconstant restriction state:

1. if some active coordinate `k` has `delta_k>1-tau`, stop at that state and designate `k` as its exceptional near-literal row;
2. otherwise reveal any active original coordinate and recurse.

No coordinate is queried twice on one branch, and the tree terminates in finitely many steps.

At every internal node, `1-delta>=tau`, so (2.5) gives

\[
 \boxed{
 K_v\ge\frac{\tau}{4}\,It_{k_v}(G_v).
 }
\tag{5.1}
\]

Now consider a nonconstant terminal state with designated `k`, child output probabilities `r_0,r_1`, and `s=|r_1-r_0|`. Choose the better of the literal `X_k` and its complement. Its actual product-measure classification error `e_k` is at most

\[
 e_k\le r_{\min}+(1-r_{\max})=1-s.
\tag{5.2}
\]

Since `delta>1-tau`,

\[
 (e_k-\tau)_+
 \le(1-s-\tau)_+
 \le\delta-s.
\tag{5.3}
\]

The terminal state's own Poincare recurrence gives

\[
 P(G_v)\ge K_k
 =tq[(\delta-s)+s(1-s)]
 \ge tq(\delta-s).
\tag{5.4}
\]

Therefore

\[
 \boxed{
 V_t(e_k-\tau)_+\le4P(G_v).
 }
\tag{5.5}
\]

Use the stopped-tree version of (2.3):

\[
 P(G)=\sum_{v\text{ internal}}\pi_vK_v
      +\sum_{\ell\text{ terminal}}\pi_\ell P(G_\ell).
\]

Combining (5.1) and (5.5) gives the all-row budget.

### Theorem 5.1 — adaptive influence-relative exceptional-row elimination

For the policy above,

\[
 \boxed{
 \tau\sum_{v\text{ internal}}\pi_v\,It_{k_v}(G_v)
 +\sum_{\ell\text{ exceptional}}
   \pi_\ell V_{p_{k_\ell}}(e_\ell-\tau)_+
 \le4P(G;p).
 }
\tag{5.6}
\]

The first term pays every nonexceptional revealed row by its **actual biased influence**. The second term pays every exceptional near-always-pivotal row by a **variance-weighted literalization error**. Both are charged once to the exact owner Poincare bank. There is no ambient-dimension factor, no count-of-rows factor, no raw `sum d_i`, and no reuse of the same refund along a branch.

Combining (5.6) with (4.5) also yields the peer-currency form

\[
 \tau\sum_v\pi_v It_{k_v}
 +\sum_\ell\pi_\ell V_{p_{k_\ell}}(e_\ell-\tau)_+
 \le\frac{1}{r_0}M_\eta(G;p),
\tag{5.7}
\]

but (5.6) is the sharper structural statement because `P` is exactly the owner's gate-margin denominator.

## 6. Decisive exact-rational sanity check

The analytic proofs above do not rely on computation. As a falsification check in this invocation, exact rational arithmetic exhausted all Boolean gates through three variables on the product-bias grid

\[
 \{1/3,1/2,2/3\}^n.
\]

Across 7,068 gate/bias configurations it found:

* zero violations of `M_eta >= 4 r_0 P`;
* zero violations of the exact local identity `K=tq(delta-s^2)`;
* zero violations of `L>=4r_0K` across 21,024 coordinate/pivot instances; and
* for the concrete adaptive policy with `tau=1/4`, zero violations of (5.6).

This is a local runtime sanity check only, not a substitute for the analytic proof and not an independently archived executable certificate.

## 7. Relation to fleet04/B18 and the remaining full-FEI implication

Nothing here modifies or weakens fleet04/B18's mixed-curvature conservation

\[
 \kappa_{ik}=\kappa_{ki}=p_{ik}+4o_{ik},
 \qquad
 \sum_{i\ne k}(p_{ik}+4o_{ik})=4d_k,
\]

including the opposite-sign contribution. The exact zero-defect classification as a character-twisted signed one-point defect (irrelevant variables allowed) also remains intact. No step in this report replaces `sum d_k` by `O(J)` or charges a small cube-measure error by ambient dimension.

The newest fleet04/B18 continuation further isolates hidden curvature rather than discarding it; this report is compatible with that split because the present currency is the exact all-gate Poincare slack, not an unsigned second-derivative surrogate.

**What is now proved:**

1. exact nonnegative singleton recurrence for the owner's Poincare denominator;
2. exact convex Bellman decomposition of every global owner margin into actual local singleton margins;
3. the corrected child-slack-preserving local extremality target (3.4);
4. global quantitative coercivity `M_eta>=4r_0P` for the newest universally safe peer direction; and
5. the nonreusing adaptive all-row/exceptional-row budget (5.6).

**What remains open:** prove, for the live base potential and the target AND margin `C_*`,

\[
 \boxed{
 \mathcal J_{\Gamma,k}+C_*\,t(1-t)(\delta-s^2)\ge0
 }
\tag{7.1}
\]

for every actual Boolean restriction pair, or produce a source-valid pair violating it strongly enough to yield a global gate with owner margin above AND. Equation (7.1), not the already-refuted `J>=0`, is the precise local inequality that would close the owner's decomposable/AND-extremality job through Theorem 3.1.

Full uniform-cube FEI remains **OPEN / NOT PROVED**.

Privacy/scope review: this report contains only FEI mathematics, source-relative scientific identifiers, public mathematical constants, and logical account/slot labels. It contains no credentials, scheduler identifiers, machine paths, email/Drive data, benchmark gold, paid/remote compute, workflow dispatch, unrelated private material, permission changes, or public-posting request.
