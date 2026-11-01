# B14 — terminal two-data-bit restriction for the live MUX hard case

**Classification:** `ESSENTIAL_STEP_APPLIED / EXACT_MUX_DATA_BLOCK_CREDIT`.  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; authenticated repository sources were consumed, but no authenticated installed mathematical-brain retrieval/receiver context entered the derivation.  
**Publication priority:** unverified; no novelty claim.

## 0. Exact candidate version and prior missing implication

The live Campaign-A candidate inherited from the current lead is

\[
C^\dagger=6.521851214,\qquad C_0=6.4548,
\qquad a^\dagger=4(C^\dagger-C_0)=0.268204856,
\]
\[
\Gamma^\dagger(z)=\Gamma_0(z)+a^\dagger z(1-z),
\]

where `Gamma_0` is the committed h96 read-once potential.  For a Boolean gate `G` at product bias `p`, write

\[
D_\Gamma(G;p)=
\sum_i {\operatorname{It}_i(G;p)\over V_{p_i}}
       \bigl(\Gamma(p_i)+h_2(V_{p_i})\bigr)
-\Gamma(p_{\rm out})-\widetilde H_G(p),
\qquad V_z=4z(1-z),
\]

and

\[
W_G={I(G;p)\over4}-p_{\rm out}(1-p_{\rm out})\ge0.
\]

Then

\[
D_{\Gamma^\dagger}=D_{\Gamma_0}+a^\dagger W_G.
\]

Whenever `W_G>0`, the required scalar lift is the owner-requested margin

\[
c_G(p)=-{D_{\Gamma_0}(G;p)\over W_G(p)}.
\]

Thus this candidate succeeds at a point exactly when `c_G(p)<=a^dagger`.

The same explicit hard family used by the current A lead is the one-bit MUX

\[
M(A;D_0,D_1)=D_A,
\qquad \Pr(A=1)=t,
\qquad \Pr(D_j=1)=q_j.
\]

The prior missing implication is the all-bias statement

\[
D_{\Gamma^\dagger}(M;t,q_0,q_1)\ge0
\quad\hbox{for every }(t,q_0,q_1)\in(0,1)^3,
\]

or a genuine violating bias vector.  This is only one prime family; even closing it would not prove the universal prime-gate statement.

## 1. Named other-account result consumed and exact application

This run substantively consumes

`fleet02/B14/20260922T070347Z-scale-free-mux-selector/REPORT.md`,

observed at scientific revision `6c06376d932f8759336a2a5e7d3a207b444d0ae4`, report blob
`7e1272000ca94a3cc9e0d93eebebe380532dd00d`.

It proves for

\[
m=\min\{q_0+q_1,\,2-q_0-q_1\},\qquad
v=q_1-q_0,\qquad s=t-\frac12,
\]

the source-valid physical-address selector tube

\[
|v|\le {m\over224},\qquad |s|\le {1\over464}
\Longrightarrow
D_{\Gamma^\dagger}(M)>{m\over400}>0.
\tag{1.1}
\]

That proof reveals the address bit and uses exact scale cancellations.  I do not rerun it.  The new policy below reveals the *two data bits* instead.  It is applied to the exact complement left by (1.1): any surviving MUX counterexample must now satisfy both the failure of (1.1)'s tube and the new quantitative data-block margin obstruction in Theorem 4 below.

The general block identity used is the preceding fleet03/B14 result

`fleet03/B14/20260922T043512Z-block-restriction-cocycle/REPORT.md`,

committed at `1726124034a382abf00d65eb505cb9ce2e7ec112`, report blob
`d0a5f76b052ebf4fac3ccc969b5d02c2940dad13`.
It proves for a physical block `T`

\[
D_\Gamma(G)=\mathbb E_ZD_\Gamma(G_Z)+\mathcal R_{\Gamma,T}+\mathcal C_T,
\tag{1.2}
\]

\[
\mathcal C_T=H(Z\mid S)+I(S;K)+\operatorname{TC}(K)\ge0,
\tag{1.3}
\]

and for a quadratic lift

\[
W_G=\mathbb E_ZW_{G_Z}+\Omega_T,
\qquad
\Omega_T={1\over4}\sum_{i\in T}\operatorname{It}_i-\operatorname{Var}_Z(r_Z).
\tag{1.4}
\]

No affine coordinate change is used in the result below, so the affine-change charge is exactly zero.

## 2. Distinct realizable policy: reveal both data bits

Take the physical block

\[
T=\{D_0,D_1\}.
\]

The four restrictions are exactly

\[
M\big|_{00}=0,\qquad
M\big|_{01}=A,\qquad
M\big|_{10}=1-A,\qquad
M\big|_{11}=1.
\tag{2.1}
\]

Thus every child is a constant or a literal.  For every symmetric boundary-normalized potential `Gamma`, all four child gate defects vanish exactly.  Their quadratic currencies vanish as well.  Consequently (1.2)--(1.4) give

\[
\boxed{
D_\Gamma(M)=\mathcal R_{\Gamma,D}+\mathcal C_D,
\qquad
\Omega_D=W_M.
}
\tag{2.2}
\]

So this two-step physical policy captures **100 percent of the parent Poincare currency** and terminates immediately.  There is no geometry loss and no child debit.

For later use put

\[
d=q_0+q_1-2q_0q_1,
\qquad
r=(1-t)q_0+tq_1,
\qquad
V_j=4q_j(1-q_j),
\qquad V_t=4t(1-t).
\]

The three biased influences are

\[
\operatorname{It}_A=V_t d,\qquad
\operatorname{It}_0=V_0(1-t),\qquad
\operatorname{It}_1=V_1t.
\tag{2.3}
\]

A direct expansion then gives the exact parent currency

\[
\boxed{
W_M=t(1-t){V_0+V_1\over4}.
}
\tag{2.4}
\]

Because all biases are interior, `W_M>0`.

The exact block remainder from (1.2) is

\[
\boxed{
\begin{aligned}
\mathcal R_{\Gamma,D}={}&d\Gamma(t)-\Gamma(r)\\
&+(1-t)\bigl(\Gamma(q_0)+h_2(V_0)\bigr)
+t\bigl(\Gamma(q_1)+h_2(V_1)\bigr)\\
&-h_2(q_0)-h_2(\operatorname{It}_0)
-h_2(q_1)-h_2(\operatorname{It}_1).
\end{aligned}}
\tag{2.5}
\]

Here `E_Z Gamma(r_Z)=d Gamma(t)` because the off-diagonal data branches yield `A` and `1-A`, while the diagonal branches are constants.

## 3. Exact new information credit and a sharp elementary lower bound

The exact six nonzero biased-Walsh squared masses of the MUX, already supplied by the peer source, are

\[
(1-2r)^2,\quad
V_t(q_1-q_0)^2,\quad
(1-t)^2V_0,\quad
t^2V_1,\quad
t(1-t)V_0,\quad
t(1-t)V_1.
\tag{3.1}
\]

With respect to the data block `T={D0,D1}`, the block-spectrum subset `K` therefore takes only

\[
\varnothing,\qquad \{D_0\},\qquad \{D_1\};
\]

there is **no** atom containing both data coordinates.  Its marginal law is

\[
\Pr(K=\{D_0\})=a:=V_0(1-t),
\qquad
\Pr(K=\{D_1\})=b:=V_1t,
\]
\[
\Pr(K=\varnothing)=1-a-b.
\tag{3.2}
\]

Since `a+b<=(1-t)+t=1`, this is a probability law.  Hence the total-correlation term contained in the exact block credit is

\[
\operatorname{TC}(K)
=h_2(a)+h_2(b)-H_3(1-a-b,a,b).
\tag{3.3}
\]

### Lemma 3.1 — mutual-exclusion credit
For `a,b>=0`, `a+b<=1`,

\[
\boxed{
\operatorname{TC}(K)\ge {ab\over\ln2}.
}
\tag{3.4}
\]

**Proof.** Work first in nats and call the left side `F(a,b)`.  Since `F(a,0)=0`,

\[
{\partial F\over\partial b}
=\ln {1-b\over1-a-b}
=-\ln\left(1-{a\over1-b}\right)
\ge {a\over1-b}\ge a.
\]

Integrating from `0` to `b` gives `F(a,b)>=ab`.  Division by `ln 2` converts to bits.  Boundary cases follow by continuity.  QED.

Because the exact block credit in (1.3) contains `TC(K)` plus two additional nonnegative terms,

\[
\boxed{
\mathcal C_D
\ge {V_0V_1\,t(1-t)\over\ln2}.
}
\tag{3.5}
\]

Combining (2.4) and (3.5) gives the scale-free credit-per-currency bound

\[
\boxed{
{\mathcal C_D\over W_M}
\ge
\kappa(q_0,q_1)
:={4V_0V_1\over\ln2\,(V_0+V_1)}.
}
\tag{3.6}
\]

Notably, the certified lower bound is independent of the address bias `t`.  If both data biases lie in
`[epsilon,1-epsilon]`, then `V_j>=4 epsilon(1-epsilon)` and

\[
\boxed{
{\mathcal C_D\over W_M}
\ge {8\epsilon(1-\epsilon)\over\ln2}.
}
\tag{3.7}
\]

For example, on `q_0,q_1 in [1/4,3/4]`, the guaranteed information credit is at least

\[
{1.5\over\ln2}=2.164042561333445\ldots
\]

units of the quadratic currency.

The exact full block credit itself can also be read directly from the child entropy in (2.1):

\[
\boxed{
\mathcal C_D
=d\,h_2(V_t)+h_2(q_0)+h_2(a)+h_2(q_1)+h_2(b)-\widetilde H_M.
}
\tag{3.8}
\]

Equation (3.8) is an identity, while (3.5) is the robust lower bound used below.

## 4. New exact margin filter for the live candidate

Define the **credit-free data-block margin request**

\[
\bar c_D(t,q_0,q_1)
:=-{\mathcal R_{\Gamma_0,D}\over W_M}.
\tag{4.1}
\]

The actual gate margin is, by (2.2),

\[
c_M
=-{D_{\Gamma_0}(M)\over W_M}
=\bar c_D-{\mathcal C_D\over W_M}.
\tag{4.2}
\]

Therefore Theorem 3.1 immediately gives

\[
\boxed{
 c_M(t,q_0,q_1)
\le
\bar c_D(t,q_0,q_1)
-{4V_0V_1\over\ln2\,(V_0+V_1)}.
}
\tag{4.3}
\]

This is the exact selector/potential decrement obtained in this run.  It is a margin statement, not a comparison of raw defects across arities.

For the live lift `a^dagger=0.268204856`, a genuine MUX counterexample must satisfy the strict necessary condition

\[
\boxed{
\bar c_D(t,q_0,q_1)
>
0.268204856
+{4V_0V_1\over\ln2\,(V_0+V_1)}.
}
\tag{4.4}
\]

Combined with the consumed peer theorem (1.1), any remaining negative point must satisfy **both**

\[
|q_1-q_0|>{m\over224}
\quad\hbox{or}\quad
\left|t-{1\over2}\right|>{1\over464},
\tag{4.5}
\]

and (4.4).  This is a source-valid reduction of the exact realizable MUX gap.  In the central data square `[1/4,3/4]^2`, (4.4) strengthens numerically to

\[
\boxed{
\bar c_D>2.432247417333445\ldots .
}
\tag{4.6}
\]

No fixed-relative near-subcube shortcut is used anywhere.

## 5. What this does and does not prove

**New proved inference.**  The live MUX hard case has a second, distinct, entirely physical terminal policy: reveal `D0,D1`.  It captures all quadratic currency, incurs zero affine-coordinate cost, retains every block information credit, and forces the exact margin bound (4.3).  The mutual-exclusion component alone pays the explicit scale-free amount (3.6).

**Attempted refutation / dead subroute.**  The term (3.6) can collapse when one data variance tends to zero.  Therefore the *TC-only estimate* cannot by itself close the entire MUX cube.  The other two exact block credits `H(Z|S)` and `I(S;K)`, or sharper source-specific control of `R`, remain necessary near a data boundary.  This is a limitation of the lower bound, not a Boolean obstruction to FEI and not a claim that the full block credit itself vanishes there.

**Full-problem change.**  None.  Full FEI remains OPEN.  Even a complete MUX proof would leave the universal composition-prime gate statement open.

**Replacement obligation.**  On the residual MUX region outside the peer-certified tubes, prove

\[
\bar c_D(t,q_0,q_1)
\le
0.268204856+\kappa(q_0,q_1)
\]

using the actual h96 source segments and, near data boundaries, the two additional exact credits in (1.3); or exhibit a genuine bias vector violating the actual margin inequality.  Do not replace this by a credit-free remainder bound.

**Next recipient:** `fleet01/B18` (Campaign-A lead).  The precise handoff is (4.3)--(4.5): intersect its current MUX residual with the new data-block necessary condition and attack the source remainder there.  `fleet02/B14` can also reuse the same block policy when extending its MUX selector tubes.

## 6. Independent regression calculation

`CHECK_MUX_DATA_BLOCK.py` was executed in this invocation on 200,000 deterministic pseudorandom interior triples using a generic symmetric boundary-normalized test potential.  It checks the six masses, the block defect cocycle, the closed currency formula (2.4), `C_D>=TC(K)`, and the bound (3.4).  The observed maxima/minima were

```
max_weight_sum_error = 5.551e-16
max_defect_cocycle_error = 1.332e-15
max_W_closed_error = 1.665e-16
min_C_minus_TC = 7.766009381562e-03
min_TC_minus_ab_over_ln2 = 3.206452577562e-10
PASS
```

The checker is only a regression test; the universal statements above are proved algebraically.  SHA-256 of the executed checker text is
`9c2ad63492041f96b0db1df60b501b546e4d460db4b3f9e3e259291e0d364477`; SHA-256 of the saved output is
`b4b36e5fa534ee725690eeb6ffdf9b7fd042eb5d4b7c2233f04440f0eb3463a6`.

The changed files contain only FEI mathematics and nonsecret verification metadata; no credentials, account secrets, scheduler identifiers, machine paths, private transcripts, or held-out benchmark material are present.
