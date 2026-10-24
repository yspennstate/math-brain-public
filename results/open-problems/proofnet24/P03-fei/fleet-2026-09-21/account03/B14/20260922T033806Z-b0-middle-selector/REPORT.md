# B14 — exact half-currency middle-coordinate selector for the four-bit prime gate B0

**Classification:** `ESSENTIAL_STEP_APPLIED / EXACT_SELECTOR_GEOMETRY`.  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; authenticated repositories were used, but no authenticated installed-brain retrieval/context was used.

## 0. Live candidate, prior gap, and assignment

The live owner target is the all-gate inequality

\[
D_\Gamma(G;p):=
\sum_i \frac{\operatorname{It}_i(G;p)}{V_{p_i}}
       \bigl(\Gamma(p_i)+h_2(V_{p_i})\bigr)
-\Gamma(p_{\rm out})-\widetilde H_G(p)\ge0,
\qquad V_u=4u(1-u),
\tag{0.1}
\]

for one symmetric finite-cap potential and every Boolean gate/product bias.
The stable scalar-lift candidate currently inherited from
`account01/B18/20260922T0222Z-shared-graft-tail/REPORT.md` is

\[
C_*=6.5218512,
\qquad
\Gamma_*(u)=\Gamma_{\rm RO}(u)+a_*u(1-u),
\qquad
a_*=4(C_*-6.4548)=0.2682048.
\tag{0.2}
\]

The remaining universal statement `LIMIT-PRIME-GATE-LIFT-v1` is open.

The immediately preceding B14 run reduced all 1,920 essential five-input
quarter-output equality cases to one literal times a single four-input
composition-prime class

\[
B_0:\quad A=\{0,1,2,3,4,5,8,10\}\subset Q_4.
\tag{0.3}
\]

It handed the all-bias analysis of `B0` to account04/B17.  That peer then
proved the exact restriction-defect cocycle and its Poincare-currency cocycle,
but the all-bias `B0` problem remained open.  The gap was therefore not another
truth-table sweep: it was to find a **realizable selector whose local currency
does not collapse relative to the parent currency**, while leaving controlled
children.

This run proves exactly that selector statement for `B0`.
No affine coordinate change is used anywhere below, so the affine-coordinate
change charge for this policy is identically zero rather than hidden.

### Candidate statement `B0-MIDDLE-CURRENCY-SELECTOR-v1`

For every interior product bias on `B0`, one of its two middle physical
coordinates can be restricted so that

1. both cofactors are binary AND/OR-type read-once gates (with one dummy
   coordinate), and
2. the local Poincare currency of that restriction is at least one half of the
   complete parent Poincare currency.

The factor `1/2` is sharp.

## 1. Required named peer result consumed

This run consumes

`account04/B17/20260922T031352Z-biased-restriction-margin-cocycle/REPORT.md`,
report blob `d32321447c5f30282f243d9a2907ec719d483c92`.

For a pivot `j` with bias `t`, restrictions `G_0,G_1`, output probabilities
`r_0,r_1`, and disagreement probability `delta_j`, that report proves the exact
restriction cocycle

\[
D_\Gamma(G)
=(1-t)D_\Gamma(G_0)+tD_\Gamma(G_1)
+\mathcal R_{\Gamma,j}+\mathcal C_j,
\tag{1.1}
\]

where `C_j>=0` is an exact Boolean information credit.  For a quadratic lift
`Gamma_c=Gamma_0+c u(1-u)` it also proves the local currency

\[
\omega_j
=t(1-t)\bigl(\delta_j-(r_1-r_0)^2\bigr)\ge0
\tag{1.2}
\]

and the exact currency recursion

\[
W_G=(1-t)W_{G_0}+tW_{G_1}+\omega_j,
\qquad
W_G=\frac{I(G;p)}4-r(1-r).
\tag{1.3}
\]

Consequently the required scalar correction is a restriction-tree weighted
average of local gluing margins.  The result below applies this exact theorem,
not a credit-free surrogate.

## 2. The two middle restrictions collapse B0 to binary gates

Write the indicator of (0.3) as `g(x0,x1,x2,x3)`.  Relative to the natural
binary encoding used by the source truth table, direct restriction gives

\[
\boxed{
 g\vert_{x_2=0}=1-x_0x_3,
 \qquad
 g\vert_{x_2=1}=(1-x_1)(1-x_3).
}
\tag{2.1}
\]

Thus pivot `x2` has a NAND cofactor and an AND-of-negated-literals cofactor;
each depends on only two variables.  Likewise

\[
\boxed{
 g\vert_{x_3=0}=1-x_1x_2,
 \qquad
 g\vert_{x_3=1}=(1-x_0)(1-x_2).
}
\tag{2.2}
\]

Thus pivot `x3` has the same property.

Equivalently, after complementing the four input literals, `B0` is the monotone
three-edge path gate

\[
y_0y_2\ \vee\ y_2y_3\ \vee\ y_3y_1,
\tag{2.3}
\]

which explains why the two degree-two path vertices are the distinguished
physical pivots.  Importantly, (2.1)--(2.2) are actual coordinate restrictions,
not an affine reparameterization or an unrealizable probability-law split.

## 3. Exact all-bias currency formulas

Put

\[
a=\Pr[x_0=1],\quad b=\Pr[x_1=1],\quad
 t=\Pr[x_2=1],\quad d=\Pr[x_3=1],
\qquad q=1-t.
\tag{3.1}
\]

### Pivot x2

From (2.1),

\[
r_0=1-ad,
\qquad
r_1=(1-b)(1-d).
\tag{3.2}
\]

The second cofactor is pointwise below the first, so its disagreement
probability is exactly the output-probability gap:

\[
\delta_2=r_0-r_1=d(1-a)+(1-d)b.
\tag{3.3}
\]

Hence (1.2) becomes

\[
\boxed{
\omega_2=t(1-t)\,\delta_2(1-\delta_2).
}
\tag{3.4}
\]

For a binary AND/OR gate on input biases `u,v`, direct biased-Fourier
calculation gives

\[
W_{\rm bin}=u(1-u)v(1-v).
\tag{3.5}
\]

Literal complementation leaves this expression unchanged.  Therefore the
product-measure weighted currency left in the two `x2` children is

\[
\boxed{
\beta_2=d(1-d)
\bigl[(1-t)a(1-a)+t b(1-b)\bigr].
}
\tag{3.6}
\]

and the complete parent currency is

\[
W=\omega_2+\beta_2.
\tag{3.7}
\]

### Pivot x3

The same calculation from (2.2) gives

\[
\delta_3=a(1-t)+t(1-b),
\tag{3.8}
\]

\[
\boxed{
\omega_3=d(1-d)\,\delta_3(1-\delta_3),
}
\tag{3.9}
\]

and the child currency

\[
\boxed{
\beta_3=t(1-t)
\bigl[(1-d)b(1-b)+d a(1-a)\bigr].
}
\tag{3.10}
\]

Again

\[
W=\omega_3+\beta_3.
\tag{3.11}
\]

## 4. PROVED: one middle pivot captures at least half of W

Define the nonnegative crossing term

\[
X=t(1-t)d(1-d)(1-a-b)^2.
\tag{4.1}
\]

Apply the elementary Bernoulli mixture-variance identity

\[
[(1-s)u+sv]\,[1-(1-s)u-sv]
=(1-s)u(1-u)+sv(1-v)+s(1-s)(u-v)^2.
\tag{4.2}
\]

First use `(s,u,v)=(t,a,1-b)` in (3.8).  Multiplication by `d(1-d)` gives

\[
\boxed{\omega_3=\beta_2+X.}
\tag{4.3}
\]

Then use `(s,u,v)=(d,1-a,b)` in (3.3).  Multiplication by `t(1-t)` gives

\[
\boxed{\omega_2=\beta_3+X.}
\tag{4.4}
\]

Substituting either identity into (3.7) or (3.11) yields the exact parent
currency decomposition

\[
\boxed{W=\beta_2+\beta_3+X.}
\tag{4.5}
\]

Adding (4.3) and (4.4),

\[
\omega_2+\omega_3=W+X\ge W.
\tag{4.6}
\]

Therefore

\[
\boxed{
\max\{\omega_2,\omega_3\}\ge\frac{W}{2}.
}
\tag{4.7}
\]

This proves `B0-MIDDLE-CURRENCY-SELECTOR-v1`.

The restriction policy is explicit and adaptive:

\[
 j(p)=\arg\max_{j\in\{2,3\}}\omega_j(p).
\tag{4.8}
\]

It uses one real physical coordinate, incurs no affine-coordinate change, sends
both children directly into the binary read-once class, and loses at most a
factor two in the relevant quadratic currency.

### Sharpness

At the uniform point `a=b=t=d=1/2`,

\[
X=0,\qquad
\omega_2=\omega_3=\beta_2=\beta_3=\frac1{16},
\qquad W=\frac18.
\tag{4.9}
\]

Hence equality holds in (4.7).  Any attempted universal strengthening to
`max(omega_2,omega_3) >= (1/2+epsilon)W` with `epsilon>0` is **REFUTED** by the
actual Boolean gate `B0` at uniform bias.  Thus the half-currency loss is not a
checker artifact; it is the sharp geometry of this two-pivot policy.

## 5. Application to the stable scalar-lift candidate

Let

\[
\Lambda_j^*(p)
:=\mathcal R_{\Gamma_{\rm RO},j}+\mathcal C_j+a_*\omega_j,
\qquad a_*=0.2682048.
\tag{5.1}
\]

The peer cocycle gives, for either middle pivot,

\[
D_{\Gamma_*}(B_0;p)
=(1-p_j)D_{\Gamma_*}(G_0)+p_jD_{\Gamma_*}(G_1)
+\Lambda_j^*(p).
\tag{5.2}
\]

The two children in (2.1)--(2.2) are binary AND/OR-type gates.  The inherited
read-once certificate already controls those gates after the much smaller
quadratic correction `c=0.01`; since `a_*>0.01` and binary Poincare currency is
nonnegative, both child defects in (5.2) are nonnegative for `Gamma_*`.
Therefore the following **single local statement is sufficient** to close the
all-bias `B0` case:

\[
\boxed{
\Lambda_{j(p)}^*(p)\ge0
\quad\text{for all }p\in(0,1)^4,
\qquad j(p)\text{ given by (4.8)}.
}
\tag{5.3}
\]

Unlike a generic local selector, (4.7) guarantees

\[
\omega_{j(p)}\ge W/2,
\tag{5.4}
\]

so the denominator of the corresponding local margin cannot disappear while
the parent gap stays macroscopic.  This is the exact geometry-loss repair
needed for an interval or analytic attack on this hard prime class.

An equivalent credit-retaining form, avoiding any attempt to estimate the two
credits separately, is

\[
\begin{aligned}
\Lambda_j^*={}&
(1-p_j)\Gamma_{\rm RO}(r_0)+p_j\Gamma_{\rm RO}(r_1)
-\Gamma_{\rm RO}(r)\\
&+\delta_j\bigl(\Gamma_{\rm RO}(p_j)+h_2(V_{p_j})\bigr)
-\bigl[\widetilde H_{B_0}-(1-p_j)\widetilde H_{G_0}-p_j\widetilde H_{G_1}\bigr]
+a_*\omega_j.
\end{aligned}
\tag{5.5}
\]

All laws in (5.5) are realized by the actual Boolean restrictions (2.1) or
(2.2).

## 6. Exact uniform anchor

At the uniform point, the inherited dyadic fixed-point identity is

\[
\Gamma_{\rm RO}(1/4)=C_0-2,
\qquad C_0=6.4548.
\tag{6.1}
\]

For either middle pivot, account04/B17's exact formula gives the base local
contribution

\[
\Gamma_{\rm RO}(1/4)-\frac12C_0-1
=\frac12C_0-3=0.2274.
\tag{6.2}
\]

Since `omega_j=1/16`, the stable correction adds exactly

\[
\frac{a_*}{16}=0.0167628,
\]

so

\[
\boxed{\Lambda_j^*=0.2441628>0.}
\tag{6.3}
\]

Each child has `H=2`, `I=1`, output bias `1/4` or `3/4`, and its exact stable
candidate defect is

\[
\boxed{D_{\Gamma_*}(G_b)=0.0167628.}
\tag{6.4}
\]

The parent defect reconstructed from (5.2) is therefore

\[
0.2441628+0.0167628=0.2609256,
\tag{6.5}
\]

which agrees exactly with the direct calculation

\[
\frac32C_*-3-C_*=\frac12C_*-3=0.2609256.
\tag{6.6}
\]

This is an exact arithmetic anchor, not a floating sign decision.

## 7. Attempted refutation and what died

The direct way to falsify (4.7) is to find product biases for which both middle
restriction currencies are less than half of the parent currency.  Algebra
(4.3)--(4.6) rules this out universally.

The adjacent standard-library checker additionally evaluates all
`6^4=1296` interior rational grid points with coordinates in
`{1/7,...,6/7}` using exact `Fraction` arithmetic.  It finds minimum
`max(omega_2,omega_3)/W = 1/2`, with exact equality examples, and reproduces the
uniform candidate numbers (6.3)--(6.6).  The finite grid is a regression check;
the proof of (4.7) is the algebra above.

**REFUTED stronger claim:** a universal selector factor strictly larger than
`1/2` using only these two middle physical pivots.

**Dead route:** broad four-dimensional search for a noncollapsing physical
pivot on `B0`.  The exact selector (4.8) already solves that geometric part and
is sharp.  Future work should spend effort on the local corrected defect
(5.3), not rediscover the pivot.

## 8. Movement of the proof gap

**Exact candidate version:** `B0-MIDDLE-CURRENCY-SELECTOR-v1`, equations
(2.1)--(4.8), applied to `LIMIT-PRIME-GATE-LIFT-v1` via (5.2).

**Prior missing implication:** account04/B17 had reduced arbitrary gate margins
to exact local restriction gluing, but the fresh `B0` all-bias handoff still
lacked a realizable pivot with nonvanishing local currency and controlled
cofactors.

**New proved inference:** every product-biased `B0` instance has a physical
middle-coordinate pivot whose local currency is at least half the parent
currency, and both resulting cofactors are binary read-once gates.  The factor
`1/2` is exact and sharp.

**Replacement obligation:** prove (5.3) for the selected nested
NAND/AND cofactor family, or produce a genuine product-bias vector for which
(5.3) is negative.  Because of (5.4), such a counterexample cannot be dismissed
as a vanishing-denominator artifact.

**Consumed peer artifact:** account04/B17
`20260922T031352Z-biased-restriction-margin-cocycle/REPORT.md`, blob
`d32321447c5f30282f243d9a2907ec719d483c92`; the stable scalar centre (0.2) is
from account01/B18 `20260922T0222Z-shared-graft-tail/REPORT.md`.

**Applied to claim:** the peer's exact defect/currency cocycle is specialized
to `B0`, turning its generic local margin into the sharp adaptive selector
(4.8) and the sufficient local inequality (5.3).

**Next recipient:** `account04/B17`, which already owns the exact local-cocycle
machinery and can now interval-certify only the selected four-parameter gluing
family (5.3), with the guaranteed denominator bound (5.4), rather than the full
unstructured four-bit gate.

**Implication to full FEI:** proving (5.3) closes the all-bias `B0` prime class;
combined with the preceding B14 factorization and the gate-composition margin
cocycle, it also removes the entire 1,920-member lifted quarter-equality family
as a new higher-arity obstruction.  It does **not** prove
`LIMIT-PRIME-GATE-LIFT-v1` for every prime gate, so full FEI remains open.

## 9. Verification scope

`CHECK_B0_MIDDLE_SELECTOR.py` is standard-library only.  It verifies the exact
truth-table restrictions, the currency cross-identities on 1,296 exact rational
bias tuples, the sharp `1/2` selector inequality, and the exact stable-candidate
uniform anchor.  It exits `PASS`.

No paid/remote compute, workflow dispatch, email/Drive action, scheduler
mutation, public posting, credentials, machine paths, or unrelated private
material were used or recorded.
