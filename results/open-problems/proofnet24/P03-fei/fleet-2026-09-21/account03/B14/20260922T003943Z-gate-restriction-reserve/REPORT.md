# B14 — exact restriction Poincare reserve after the read-once-Gamma refutation

**Run:** `20260922T003943Z-account03-B14-r11-fei-gate`  
**Outcome:** **CANDIDATE_REFUTED** for the minimal Numaro-scale quadratic repair of the *blind* Shannon/arity induction.  
**Full uniform-cube FEI:** **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.  
**Publication priority:** **UNVERIFIED**; no novelty claim is made.

## 0. Live target and exact candidate change

The live owner target is the all-gate reformulation

\[
\Gamma(p_{\rm out})+H_t(G;p)
\le
\sum_i {\rm It}_i(G;p)
\frac{\Gamma(p_i)+h(V_{p_i})}{V_{p_i}},
\qquad V_u=4u(1-u),
\tag{G}
\]

for one symmetric nonnegative finite-cap potential \(\Gamma\).  The live control asks the FEI fleet to converge on
proving or falsifying the claim that the read-once potential is controlled by decomposable/AND gates.

That specific claim is already falsified by the compatible completed work consumed below.  This run does not redo
that sweep.  Instead it applies the refutation to the restriction/Shannon expansion and derives the exact amount by
which the only natural one-parameter quadratic repair can help a blind arity induction.

The old candidate is the read-once value-iteration potential \(\Gamma_0\) with
\[
C_0=\Gamma_0(1/2)=6.4548.
\]
For \(\phi(u)=u(1-u)\), consider
\[
\Gamma_c=\Gamma_0+c\phi.
\tag{0.1}
\]

The published balanced \(18\)-variable seed forces
\[
C_N=\frac{H(G_{18})}{I(G_{18})-1}
\ge
6.5218457109230465756581439729485784683666622922105\ldots .
\tag{0.2}
\]
Hence the smallest quadratic correction that makes that *uniform balanced gate* tight is
\[
c_N=4(C_N-C_0)
\ge
0.2681828436921863026325758917943138734666491688420\ldots .
\tag{0.3}
\]
This does **not** assert that \(\Gamma_{c_N}\) is universally valid.

## 1. Named peer result consumed

**consumed_peer_artifact:**  
`proofnet24/P03-fei/fleet-2026-09-21/account01/B13/20260922T002604Z-gate-composition-prime/REPORT.md`
at commit `d99ffba1e2cb9dc61f7a6d77f8ba961239694ea3`.

That report proves, for any fixed \(\Gamma\), the exact disjoint-composition laws
\[
D_\Gamma(F)
=
D_\Gamma(H)+
\sum_j\frac{\alpha_j}{V_{q_j}}D_\Gamma(G_j),
\qquad
K(F)
=
K(H)+
\sum_j\frac{\alpha_j}{V_{q_j}}K(G_j),
\tag{1.1}
\]
where
\[
D_\Gamma(G;p)
=
\sum_i {\rm It}_i(G;p)
\frac{\Gamma(p_i)+h(V_{p_i})}{V_{p_i}}
-H_t(G;p)-\Gamma(p_{\rm out})
\tag{1.2}
\]
and
\[
K(G;p)=\frac{I(G;p)}4-\phi(p_{\rm out})\ge0.
\tag{1.3}
\]
Consequently a decomposable gate has required quadratic margin equal to a nonnegative \(K\)-weighted average of
its components' margins, and all-gate validity for a fixed \(\Gamma\) reduces to composition-prime gates
(up to the unary base and the stated zero-\(K\) exceptional possibility).

The same report consumes the source-valid \(n=18\) balanced counterexample and concludes that a
composition-prime violating descendant exists at arity at most \(18\), with required read-once-\(\Gamma_0\) margin
at least
\[
0.2681828436921863026325758917943138734666491688421\ldots
\tag{1.4}
\]
unless a zero-\(K\) component is already a still stronger obstruction.

**applied_to_claim:** the live decomposable/AND-extremality claim is therefore false for \(\Gamma_0\), and any
restriction argument should now be applied to composition-prime interior gates for a replacement potential rather
than trying to prove decomposable extremality of \(\Gamma_0\).

## 2. Exact child-slack identity for a Shannon restriction

Let the last input of \(G\) have bias \(t\in(0,1)\).  Write \(G_0,G_1\) for the two cofactors, with output
probabilities
\[
q_b=\Pr[G_b=1],\qquad
q=(1-t)q_0+tq_1,
\]
and let
\[
d=\Pr[G_0\ne G_1].
\]
The gate report gives the exact spectral restriction increment
\[
H_t(G)-(1-t)H_t(G_0)-tH_t(G_1)
=
JS_t(\mu_0,\mu_1)+B_k.
\tag{2.1}
\]
For each old input \(j<k\), biased influence averages across the two cofactors:
\[
{\rm It}_j(G)=(1-t){\rm It}_j(G_0)+t{\rm It}_j(G_1),
\tag{2.2}
\]
while
\[
{\rm It}_k(G)=V_t d.
\tag{2.3}
\]

Substitution into (1.2) gives the **exact**, not merely sufficient, defect decomposition
\[
\boxed{
D_\Gamma(G)
=
(1-t)D_\Gamma(G_0)+tD_\Gamma(G_1)+R_\Gamma,
}
\tag{2.4}
\]
with
\[
\boxed{
R_\Gamma
=
d\bigl(\Gamma(t)+h(V_t)\bigr)
-\Bigl(JS_t+B_k+\Lambda_\Gamma\Bigr),
}
\tag{2.5}
\]
where the concavity deficit is
\[
\Lambda_\Gamma
=
\Gamma(q)-(1-t)\Gamma(q_0)-t\Gamma(q_1).
\tag{2.6}
\]

Thus the already-refuted blind arity step is exactly the demand \(R_\Gamma\ge0\).  The correct induction may have
\(R_\Gamma<0\), provided the weighted child slack in (2.4) pays \(-R_\Gamma\).

## 3. New exact formula: the quadratic repair pays a restriction Poincare reserve

For \(\Gamma_c=\Gamma+c\phi\), subtract (2.5) for \(\Gamma\) from that for \(\Gamma_c\).
Since \(\phi(t)=t(1-t)\) and
\[
\phi(q)
=
(1-t)\phi(q_0)+t\phi(q_1)+t(1-t)(q_1-q_0)^2,
\tag{3.1}
\]
we obtain

\[
\boxed{
R_{\Gamma_c}-R_\Gamma
=
c\,t(1-t)\Bigl[d-(q_1-q_0)^2\Bigr].
}
\tag{3.2}
\]

The same quantity is exactly the restriction decrement of the Poincare slack:
\[
\boxed{
K(G)-(1-t)K(G_0)-tK(G_1)
=
t(1-t)\Bigl[d-(q_1-q_0)^2\Bigr].
}
\tag{3.3}
\]

This is always nonnegative.  To see its geometry, let
\[
a=\Pr[G_0=0,G_1=1],\qquad
b=\Pr[G_0=1,G_1=0].
\]
Then
\[
d=a+b,\qquad q_1-q_0=a-b,
\]
so
\[
\boxed{
d-(q_1-q_0)^2
=
d(1-d)+4ab.
}
\tag{3.4}
\]
The first term is a disagreement-variance reserve; the second is a genuine bidirectional-crossing bonus.  In
particular
\[
t(1-t)d(1-d)
\le
K(G)-(1-t)K(G_0)-tK(G_1)
\le
\frac14.
\tag{3.5}
\]

This makes precise how a quadratic cap correction interacts with the older posterior-crossing/restriction
mechanism: it does not merely alter the endpoint cap; it contributes a local reserve, and the reserve has an exact
crossing term \(4ab\).

## 4. Decisive calculation: the Numaro-scale repair cannot rescue blind arity induction

The live owner message records that the blind sufficient condition for \(\Gamma_0\) fails on the \(n=3\) cofactor
search at \(t=1/2\): the printed maximum is \(7.0237\) against the available \(6.4548\), i.e. a printed deficit
\[
\delta_{\rm blind}\approx 0.5689.
\tag{4.1}
\]

The certified seed interval also gives
\[
c_N
\le
0.2681828436921863026325758917943138734666491726916\ldots .
\]
Therefore the **largest possible** improvement from this Numaro-scale quadratic correction at any one Shannon
step is, by (3.2) and (3.5),
\[
\frac{c_N}{4}
\le
0.0670457109230465756581439729485784683666622931729\ldots .
\tag{4.2}
\]

Hence even granting the maximal possible local Poincare reserve, the printed witness retains approximately
\[
0.5689-0.0670457109230465756581
=
\boxed{0.5018542890769534243419}
\tag{4.3}
\]
of unpaid local deficit.  Even allowing one unit in the last printed decimal on each side of (4.1), a conservative
lower bound from the printed data is still \(>0.50175\).

Therefore the candidate

> “repair \(\Gamma_0\) only by the minimal quadratic shift forced by the \(n=18\) seed, and then close arity
> induction by requiring each restriction residual \(R_{\Gamma_{c_N}}\ge0\)”

is **REFUTED**.

This is not a refutation of \(\Gamma_{c_N}\) itself as an all-gate potential: the child slacks in (2.4) may still
rescue a negative local residual.  It is specifically a refutation of the *blind* induction that discards them.

## 5. Exact replacement obligation

By (2.4), an arity induction for any candidate \(\Gamma\) needs only the following quantitative child-slack
inequality at steps where the local residual is negative:
\[
\boxed{
(1-t)D_\Gamma(G_0)+tD_\Gamma(G_1)
\ge
\Bigl[
JS_t+B_k+\Lambda_\Gamma
-d(\Gamma(t)+h(V_t))
\Bigr]_+.
}
\tag{5.1}
\]

For \(\Gamma_{c_N}\), (3.2)-(3.4) identify exactly how much of the right side is already paid by the quadratic
correction.  The remaining burden is genuinely **stability of lower-arity slack**, not another endpoint margin and
not an every-coordinate erasure estimate.

Combining this with the account01/B13 prime-gate reduction gives a narrower universal target:

1. prove lower arities;
2. restrict attention to composition-prime gates at interior biases;
3. when \(R_{\Gamma_{c_N}}<0\), prove that the two cofactors carry at least \(-R_{\Gamma_{c_N}}\) weighted slack.

A successful inequality of this form for one finite-cap symmetric \(\Gamma\) would close (G) by induction.  No such
universal stability inequality is proved here.

## 6. Status ledger and handoff

- **PROVED:** exact child-slack decomposition (2.4)-(2.6).
- **PROVED:** exact quadratic restriction/Poincare reserve (3.2)-(3.4).
- **PROVED:** the reserve is at most \(c/4\) per Shannon step.
- **CONSUMED / APPLIED:** account01/B13's exact composition-prime reduction and its application of the
  source-valid \(n=18\) obstruction.
- **REFUTED:** decomposable/AND extremality for the read-once \(\Gamma_0\) (peer result).
- **REFUTED:** minimal Numaro-scale quadratic repair + blind \(R\ge0\) arity induction (this report).
- **OPEN:** universal child-slack stability (5.1) for a finite-cap replacement \(\Gamma\).
- **OPEN:** full uniform-cube FEI.

`prior_missing_implication`: read-once \(\Gamma_0\) is controlled by decomposable/AND gates.  
`new_proved_inference`: composition-prime reduction plus exact restriction Poincare reserve shows why the
quadratic correction cannot by itself close the blind step and isolates the child-slack quantity that must pay it.  
`replacement_obligation`: prove (5.1), or find a composition-prime gate violating the proposed replacement
potential.  
`consumed_peer_artifact`: account01/B13 `20260922T002604Z-gate-composition-prime/REPORT.md`,
commit `d99ffba1e2cb9dc61f7a6d77f8ba961239694ea3`.  
`next_recipient`: `account03/B18` and `account04/B18`.  
`remaining_implication`: quantitative lower bound on weighted cofactor slack sufficient to pay every negative
restriction residual for one finite-cap \(\Gamma\).  
`full_problem_change`: one live extremality hypothesis and one natural blind-repair induction are eliminated;
full FEI remains OPEN.
