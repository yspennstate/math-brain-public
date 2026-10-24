# B12 — exact Shannon child-slack and gate-margin conservation

**Status:** PARTIAL / STRUCTURAL. Full uniform-cube FEI remains **OPEN / NOT PROVED**. The current read-once fixed-point `Gamma` as a universal all-gate candidate is independently refuted by the freshly landed account03/B15 n=18 balanced-gate calculation; this report localizes that failure in the Shannon recursion rather than opening another route.

**Execution:** `WITHOUT_VERIFIED_BRAIN`. Authenticated repository sources were used; no authenticated mathematical/cognitive brain retrieval entered the proof context.

## 1. Live owner target and fresh peer result

The current owner target is the all-gate inequality
\[
\Gamma(p_{\rm out})+H_t(G;p)
\le \sum_i \operatorname{It}_i(G;p)
\frac{\Gamma(p_i)+h(V_{p_i})}{V_{p_i}},
\qquad V_p=4p(1-p),
\tag{G}
\]
with gate defect
\[
D_G=\sum_i \operatorname{It}_i(G;p)
\frac{\Gamma(p_i)+h(V_{p_i})}{V_{p_i}}
-H_t(G;p)-\Gamma(p_{\rm out}),
\]
Poincare-defect currency
\[
P_G=\frac{I(G;p)}4-p_{\rm out}(1-p_{\rm out})\ge0,
\]
and requested margin \(c_G=-D_G/P_G\) when \(P_G>0\).

A decisive compatible peer result landed during this run:

`account03/B15/20260922T002607Z-readonce-gamma-counterexample`.

It consumes the source-certified account01/B15 exact n=18 balanced seed with
\[
I=\frac{261}{128},\qquad
H\in[
6.776605309005978082519790221891882314787235038,\,
6.776605309005978082519790221891882314787235039].
\]
For every symmetric potential with \(\Gamma(1/2)=C_0\), a balanced gate at uniform bias has
\[
c_G=4\left(\frac{H}{I-1}-C_0\right).
\]
At the current read-once candidate cap \(C_0=6.4548\), this gives
\[
c_G\in[
0.2681828436921863026325758917943138734666491688421,\,
0.2681828436921863026325758917943138734666491726918],
\]
more than \(60.9864\) times the current two-input-AND floor
\(0.0043974201\). Thus the read-once `Gamma` is not a universal all-gate potential. This is a refutation of that candidate, not of the gate reformulation and not of FEI.

I independently re-ran the exact decimal arithmetic from the certified \(H,I\) interval in the checker shipped below.

A second fresh account02 input was read:
`account02/B13/20260922T001208Z-affine-critical-exchange`.
Its exact implication relevant here is that for any fixed finite \(C\), if ordinary FEI fails then a minimum-dimensional counterexample can be chosen simultaneously in a globally minimum affine gauge, tensor-primitive, and restriction-critical. This legitimizes restriction slack as a structural resource in the minimal-counterexample program. I do **not** identify that uniform folded slack with the biased gate potential slack below; no unsupported bridge is used.

## 2. Exact one-step child-slack identity

Fix an input \(k\), write its bias as \(t\), and let \(G_0,G_1\) be the two restrictions. Put
\[
p_b=\Pr(G_b=1),\qquad
d=\Pr(G_0\ne G_1),
\]
under the remaining product biases. Let
\[
\mu_b(S)=\widehat G_b(S)^2,\qquad
m=(1-t)\mu_0+t\mu_1.
\]
For the biased Fourier coefficients of the parent, for every
\(S\subseteq[k-1]\),
\[
a_S=(1-t)\widehat G_0(S)+t\widehat G_1(S),
\]
\[
b_S=\sqrt{t(1-t)}
\bigl(\widehat G_0(S)-\widehat G_1(S)\bigr),
\]
and therefore
\[
a_S^2+b_S^2=(1-t)\mu_0(S)+t\mu_1(S)=m(S).
\tag{2.1}
\]
Consequently
\[
\operatorname{It}_j(G)
=(1-t)\operatorname{It}_j(G_0)
+t\operatorname{It}_j(G_1),\qquad j<k,
\tag{2.2}
\]
\[
\operatorname{It}_k(G)=4t(1-t)d,
\tag{2.3}
\]
and
\[
H_t(G)=(1-t)H_t(G_0)+tH_t(G_1)+JS_t(\mu_0,\mu_1)+B_k,
\tag{2.4}
\]
where
\[
B_k=H(S_k\mid S_{-k})
\]
is exactly the conditional spectral-bit entropy created by the split.

Define the one-step residual
\[
R_k=
d[\Gamma(t)+h(V_t)]
+(1-t)\Gamma(p_0)+t\Gamma(p_1)
-\Gamma((1-t)p_0+tp_1)
-JS_t(\mu_0,\mu_1)-B_k.
\tag{2.5}
\]
Then, with no inequality and for any symmetric \(\Gamma\),
\[
\boxed{
D_G=(1-t)D_{G_0}+tD_{G_1}+R_k.
}
\tag{2.6}
\]

This is the exact quantity discarded by the already-refuted naive arity induction. That induction demanded \(R_k\ge0\); the correct recursion retains the two child defects.

## 3. Exact Poincare-currency decomposition

Let
\[
P_G=\frac{I(G)}4-p_{\rm out}(1-p_{\rm out}).
\]
Because
\[
I(G)=(1-t)I(G_0)+tI(G_1)+4t(1-t)d
\]
and
\[
p_{\rm out}(1-p_{\rm out})
=(1-t)p_0(1-p_0)+tp_1(1-p_1)
+t(1-t)(p_1-p_0)^2,
\]
we get
\[
\boxed{
P_G=(1-t)P_{G_0}+tP_{G_1}+Q_k,
}
\tag{3.1}
\]
with
\[
\boxed{
Q_k=t(1-t)\left[d-(p_1-p_0)^2\right]\ge0.
}
\tag{3.2}
\]
The nonnegativity is elementary:
\[
|p_1-p_0|\le d\le1
\quad\Longrightarrow\quad
(p_1-p_0)^2\le d^2\le d.
\]

For \(0<t<1\), equality \(Q_k=0\) is completely degenerate: either
\(d=0\), so \(G_0=G_1\) on the full-support product measure, or
\(d=1\) and \(|p_1-p_0|=1\), so the two children are opposite constants and \(G\) is just the split variable up to negation. Thus every genuine Shannon split has \(Q_k>0\).

## 4. Adding a margin: the exact missing child-slack recursion

Replace
\[
\Gamma(p)\mapsto \Gamma_c(p)=\Gamma(p)+c\,p(1-p).
\]
Then exactly
\[
D_G(\Gamma_c)=D_G(\Gamma)+cP_G,
\tag{4.1}
\]
and the one-step residual changes by exactly
\[
R_k(\Gamma_c)=R_k(\Gamma)+cQ_k.
\tag{4.2}
\]

Define the margin-\(c\) slack
\[
S_c(G):=D_G+cP_G.
\]
Combining (2.6), (3.1), and (4.2),
\[
\boxed{
S_c(G)
=(1-t)S_c(G_0)+tS_c(G_1)+R_k+cQ_k.
}
\tag{4.3}
\]

This is the exact corrected arity induction. The false sufficient condition was to discard the first two terms and require the local residual to be nonnegative. The real proof obligation at a candidate margin \(c_*\) is
\[
R_k+c_*Q_k
\ge
-\bigl[(1-t)S_{c_*}(G_0)+tS_{c_*}(G_1)\bigr].
\tag{4.4}
\]
So a negative local Shannon residual is allowed precisely to the extent that already-proved child slack pays for it.

Equivalently, whenever all denominators are positive, define
\[
c_b=-D_{G_b}/P_{G_b},\qquad
c_R=-R_k/Q_k.
\]
Then
\[
\boxed{
c_G=
\frac{(1-t)P_{G_0}c_0+tP_{G_1}c_1+Q_k c_R}
{(1-t)P_{G_0}+tP_{G_1}+Q_k}.
}
\tag{4.5}
\]
Thus the parent margin is literally a barycenter of the two child margins and the one-step residual margin, in the correct Poincare-defect currency.

## 5. Full decision-tree conservation law

Assume the natural endpoint normalization
\(\Gamma(0)=\Gamma(1)=0\), satisfied by the read-once potential. Expand a gate all the way to constants along any variable order. At every internal restriction node \(v\), let \(w_v\) be the product probability of reaching that restriction, and let \(R_v,Q_v\) be the quantities above for the chosen next split.

Repeated application of (2.6) and (3.1) gives the order-independent identities
\[
\boxed{
-D_G=\sum_{v\ {\rm internal}} w_v(-R_v),
\qquad
P_G=\sum_{v\ {\rm internal}} w_v Q_v.
}
\tag{5.1}
\]
Nodes with \(Q_v=0\) are degenerate and also have \(R_v=0\). Therefore, for every nondegenerate gate,
\[
\boxed{
c_G=
\frac{\sum_v w_v Q_v c_{R,v}}
{\sum_v w_v Q_v}.
}
\tag{5.2}
\]

This is a Shannon-margin conservation law: the global gate margin is the \(Q\)-weighted average of the local one-bit residual margins, for **every** full Shannon decision tree. The local residual margins themselves depend on the split order, but their weighted mean does not.

### Consequence for the freshly found n=18 obstruction

For the certified balanced n=18 gate under the current read-once potential,
\[
c_G\ge
0.2681828436921863026325758917943138734666491688421.
\]
Hence **every full variable ordering** contains at least one genuine restriction node with
\[
\boxed{
c_{R,v}\ge
0.2681828436921863026325758917943138734666491688421.
}
\tag{5.3}
\]
In particular the failure is not merely a global high-arity averaging artifact: every complete Shannon expansion must expose a local one-bit residual whose required margin is at least \(60.9864\) times the current AND floor.

This also shows why retaining child slack is necessary but cannot rescue the *current* read-once potential globally: after all child slacks telescope to constants, the conserved average is still the n=18 gate's much larger margin.

## 6. What this changes

The owner's falsification job for the current read-once `Gamma` is already fulfilled by account03/B15's source-valid n=18 gate. The present result gives the exact local mechanism behind that falsification and replaces the false blind induction by a conserved child-slack recursion.

The live universal target is now:

> construct a new finite-cap symmetric nonnegative \(\Gamma\) for which the decision-tree average in (5.2) is uniformly bounded, or prove no such finite-cap \(\Gamma\) exists.

A pointwise bound on every \(c_{R,v}\) would be sufficient but is stronger than necessary. The exact conserved quantity suggests a more flexible route: choose/adapt the split order and prove a weighted-average residual bound, allowing some local spikes provided they are compensated by low-margin nodes in the same \(Q\)-budget.

Full FEI remains OPEN.

## 7. Finite verification

`check_child_slack_decomposition.py` is standard-library only. It checks the algebra with an arbitrary smooth symmetric test potential (the identities are potential-independent), then separately performs exact-decimal arithmetic for the certified n=18 margin interval.

Native run:

- 21,216 exhaustive n=2 / randomized n=3 child-pair cases;
- 14,499 nondegenerate barycentric-margin checks;
- 675 interior \(Q=0\) degeneracy checks;
- 1,536 complete n=3 decision-tree/order conservation checks;
- 160 boundary-continuity gate-pair checks;
- exact-decimal reproduction of the n=18 interval and \(>60.9864\) factor over the current AND floor;
- zero assertion failures.

The arbitrary test potential produced large individual residual margins (maximum absolute value about 32.30), illustrating why pointwise residual control is much stronger than the conserved-average statement; that diagnostic is not a claim about the current read-once `Gamma`.

Checker SHA-256: `223ae0bcef1f81d22027f6ff7a2b90729325379cc44fbecf88e7424ef579a35e`.
Output SHA-256: `83028923fdaee5c71e0e59b53902105764b298f6a7a2f63826c631132f3dabaf`.
