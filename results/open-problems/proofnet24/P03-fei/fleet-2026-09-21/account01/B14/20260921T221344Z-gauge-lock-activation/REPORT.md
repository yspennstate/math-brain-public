# B14 — high-ratio gauge locking and activation-strengthened crossing tube

**Status:** PARTIAL / proved new selector-potential structure. **Full uniform-cube Friedgut--Kalai Fourier entropy--influence remains OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; no authenticated brain retrieval/context was available or claimed.  
**Model self-report:** GPT-5.6 Sol. Configured/provider reasoning effort: UNKNOWN / NOT_EXPOSED.  
**Route:** APPROACHES 5/6, but with a mechanism change from the previous random-erasure tube: variational control of the folded dimension-cooling gauge, followed by a curvature-refunded block selector.  
**Novelty/publication priority:** UNVERIFIED; no novelty claim.

## 0. Fresh compatible inputs actually consumed

This run used the current joint FEI order and, substantively, the following complete results already on `master`.

1. **account04/B14**, `20260921T201002Z-dimension-cooling-activation/REPORT.md`, proves for
   \[
   P_z^T(f)=\sum_S \widehat f(S)^2\Phi_z(|S\triangle T|),\qquad
   \Phi_z(k)=1+z+\cdots+z^{k-1},
   \]
   the exact block activation kernel
   \[
   \Lambda_{A,z}^T
   =\sum_S\widehat f(S)^2 z^{|(S\triangle T)\setminus A|}
        \Phi_z(|(S\triangle T)\cap A|),
   \]
   and the nonincreasing-scale telescope. Its dimension-cooling choice is
   \(z_d=1-1/d\).

2. **account01/B18**, `20260921T2205Z-folded-cooling-compiler/REPORT.md`, replaces the fixed gauge by the character-invariant folded activation
   \[
   \mathcal A_z(f)=\min_T P_z^T(f),
   \]
   proves \(0\le\mathcal A_z\le\mathcal J\), permits fresh minimization after every physical restriction, and shows the true adaptive drop dominates the parent-minimizer block kernel \(\Lambda_{A,z}^{T_*}\).

3. **account01/B18**, `20260921T1856Z-curvature-refunded-crossing/REPORT.md`, proves for median-centered \(f\)
   \[
   \Delta_A\mathcal F
   \le B_A-\sum_{j\notin A}\mathfrak j'(p_j)c_j(A),
   \qquad \mathcal F=H-\mathcal P,
   \]
   and the exact folded-influence drift
   \[
   D_A=\mathcal J(f)-\mathbb E\mathcal J(f_{A=a})=J_A+C_A,
   \quad J_A=\sum_{i\in A}p_i,
   \quad C_A=\sum_{j\notin A}c_j(A).
   \]

4. **account04/B14**, `20260921T211337Z-posterior-variance-short-circuit/REPORT.md`, proves the Bernoulli-block crossing lower bound and, with its mixed pivotality depth \(M\), the critical-core product obstruction
   \[
   S_\rho\ge (\rho+\kappa(\rho))\frac{J^2}{8M-2J}.
   \]
   The last section below sharpens this exact inequality after adding folded activation.

No settled read-once certificate was rerun. No every-prescribed-coordinate payment is asserted.

## 1. Setup

Median-center the current Boolean function, so its squared Fourier spectral sample \(X\) has coordinate marginals
\[
p_i=\Pr(i\in X)=\operatorname{Inf}_i(f)\le\frac12,
\qquad J=\sum_i p_i=\mathcal J(f).
\]
Let \(d\) be the number of currently unresolved physical coordinates and put
\[
z=z_d=1-\frac1d,
\qquad
a_d:=z_d^{d-1}
\]
for \(d\ge2\); set \(a_1=1\). Then
\[
a_d\ge e^{-1}.
\tag{1.1}
\]
For a character shift \(T\), write
\[
Y=X\triangle T,
\qquad q_i^T=\Pr(i\in Y).
\]
A minimizer of \(P_z^T\) will be denoted \(T_*\).

The key new observation is that a minimizer of the nonlinear activation potential cannot arbitrarily disagree with the median character. In the high-ratio regime relevant to FEI it cannot disagree at all.

## 2. PROVED: one-bit variational condition for an activation-minimizing gauge

### Lemma 2.1 — local optimality forces a marginal cap

For every minimizer \(T_*\) of \(P_z^T(f)\) and every coordinate \(i\),
\[
\boxed{q_i^{T_*}\le\frac1{1+a_d}.}
\tag{2.1}
\]

### Proof

Put \(Y=X\triangle T_*\) and \(K=|Y|\). Toggle only the \(i\)-th bit of \(T_*\). If \(i\notin Y\), then \(K\) increases by one and
\[
\Phi_z(K+1)-\Phi_z(K)=z^K.
\]
If \(i\in Y\), then \(K\) decreases by one and
\[
\Phi_z(K-1)-\Phi_z(K)=-z^{K-1}.
\]
Since \(T_*\) minimizes the expectation, the expected cost change is nonnegative:
\[
\mathbb E[1_{\{i\notin Y\}}z^K]
\ge
\mathbb E[1_{\{i\in Y\}}z^{K-1}].
\tag{2.2}
\]
On \(i\in Y\), \(K\le d\), hence
\[
z^{K-1}\ge z^{d-1}=a_d.
\]
The left side of (2.2) is at most \(1-q_i^{T_*}\), while the right side is at least \(a_dq_i^{T_*}\). Therefore
\[
1-q_i^{T_*}\ge a_dq_i^{T_*},
\]
which is (2.1). QED.

This is a genuine variational property of the *minimizing gauge*, not a generic statement about arbitrary character shifts.

## 3. PROVED: high-ratio gauge locking

Define
\[
\theta_d:=\frac{a_d}{1+a_d}.
\tag{3.1}
\]
Since \(a_d\ge e^{-1}\),
\[
\theta_d\ge\theta_\infty:=\frac1{e+1}=0.2689414213\ldots.
\tag{3.2}
\]

### Theorem 3.1 — activation minimizer equals the median gauge below \(\theta_d\)

If every active centered marginal satisfies
\[
p_i<\theta_d,
\tag{3.3}
\]
then the unique minimizer of \(P_{z_d}^T(f)\) is
\[
\boxed{T_*=\varnothing.}
\tag{3.4}
\]

### Proof

Suppose a minimizing \(T_*\) contains \(i\). Since the parent is median-centered,
\[
q_i^{T_*}=1-p_i>1-\theta_d=\frac1{1+a_d},
\]
contradicting Lemma 2.1. Hence no coordinate can belong to \(T_*\). QED.

Thus the character-invariant folded activation introduced by account01/B18 collapses back to the ordinary centered spectral activation whenever the marginals are sufficiently rare.

The threshold is already below the relevant corrected-critical regime. Let
\[
\rho_{\rm lock}:=\frac{h_2(1/(e+1))}{1/(e+1)}
=3.1231393576\ldots.
\tag{3.5}
\]
The function \(h_2(p)/p\) decreases on \((0,1/2]\). Therefore any physical restriction core for which singleton criticality gives
\[
h_2(p_i)\ge\rho p_i\quad\forall i
\]
with \(\rho>\rho_{\rm lock}\) automatically has \(p_i<1/(e+1)\le\theta_d\), so Theorem 3.1 applies.

In particular, the presently relevant corrected lower-bound scale \(\rho\approx3.6364\) is well inside the gauge-locked regime. This removes the residual possibility that the folded activation minimizer is using a different character orientation from the posterior-crossing calculation.

## 4. PROVED: multiplicity-strengthened block activation

The account04 block lower bound used only the event that the shifted spectral sample hits \(A\). The exact kernel actually pays **multiplicity**.

### Theorem 4.1 — block multiplicity bound

For every character shift \(T\) and every physical block \(A\),
\[
\boxed{
\Lambda_{A,z_d}^T
\ge a_d\sum_{i\in A}q_i^T.
}
\tag{4.1}
\]
Consequently, on a gauge-locked centered core,
\[
\boxed{
\Lambda_{A,z_d}^{T_*}
\ge a_d J_A
\ge e^{-1}J_A.
}
\tag{4.2}
\]

### Proof

For one spectral realization put
\[
k=|Y|,\qquad r=|Y\cap A|.
\]
If \(r=0\), both sides of the desired pointwise inequality vanish. If \(r\ge1\), then
\[
z^{k-r}\Phi_z(r)
=\sum_{\ell=0}^{r-1}z^{k-r+\ell}
\ge r z^{k-1}
\ge r z^{d-1}
=a_dr.
\tag{4.3}
\]
Average over \(Y=X\triangle T\). Since
\[
\mathbb E|Y\cap A|=\sum_{i\in A}q_i^T,
\]
(4.1) follows. Under Theorem 3.1, \(T_*=\varnothing\) and \(q_i^{T_*}=p_i\), giving (4.2). QED.

This is stronger than the earlier hit-probability lower bound
\(\Lambda_A\ge e^{-1}\Pr(Y\cap A\ne\varnothing)\): repeated spectral occupancy inside the queried block is retained rather than discarded.

## 5. PROVED: activation-strengthened curvature-refunded critical tube

Fix \(\lambda\ge0\) and use account01/B18's adaptive potential
\[
\mathcal G_\lambda(f)
:=\mathcal F(f)-\lambda\mathcal A_{z_d}(f).
\tag{5.1}
\]
Choose a nonconstant physical descendant maximizing \(\mathcal G_\lambda/\mathcal J\), and write
\[
\rho=\frac{\mathcal G_\lambda}{\mathcal J}.
\]
Assume \(\rho>\rho_{\rm lock}\), so Theorem 3.1 locks the activation gauge to the median-centered gauge.

For every physical block \(A\), ratio maximality gives
\[
\rho D_A\le\Delta_A\mathcal G_\lambda.
\tag{5.2}
\]
The true adaptive activation drop dominates \(\Lambda_{A,z_d}^{T_*}\), and the curvature-refunded theorem gives
\[
\Delta_A\mathcal G_\lambda
\le
B_A-\sum_{j\notin A}\mathfrak j'(p_j)c_j(A)
-\lambda\Lambda_{A,z_d}^{T_*}.
\tag{5.3}
\]
Use
\[
D_A=J_A+C_A,
\qquad C_A=\sum_{j\notin A}c_j(A),
\]
and Theorem 4.1. Rearranging yields the new all-block necessary condition
\[
\boxed{
B_A
\ge
(\rho+\lambda a_d)J_A
+
\sum_{j\notin A}(\rho+\mathfrak j'(p_j))c_j(A).
}
\tag{5.4}
\]
Since
\[
B_A=H(X_A\mid X_{A^c})\le H(X_A)\le\sum_{i\in A}h_2(p_i),
\]
we obtain the **activation-strengthened crossing tube**
\[
\boxed{
\sum_{i\in A}\bigl[h_2(p_i)-(\rho+\lambda a_d)p_i\bigr]
\ge
\sum_{j\notin A}(\rho+\mathfrak j'(p_j))c_j(A)
\quad\text{for every }A.
}
\tag{5.5}
\]

This is strictly stronger than the inherited \(\lambda=0\) critical inequality whenever \(\lambda>0\). It uses the activation bank and the curvature-crossing refund **simultaneously**, rather than treating them as two alternative certificates.

A singleton consequence, after gauge locking, is
\[
\boxed{
h_2(p_i)\ge(\rho+\lambda a_d)p_i.}
\tag{5.6}
\]
So the activation penalty bootstraps the rarity threshold after the first gauge-lock step.

Crucially, (5.5) is only a necessary condition on a ratio-maximal descendant. It does not claim a cheap prescribed coordinate and therefore preserves the known addressing counterexamples to every-coordinate payment.

## 6. PROVED: strengthened mixed-depth product obstruction

This section substantively consumes account04/B14's newest posterior-variance selector.

Let
\[
r_\lambda:=\rho+\lambda a_d,
\qquad
S_{r_\lambda}:=\sum_i[h_2(p_i)-r_\lambda p_i].
\tag{6.1}
\]
By (5.6), all summands are nonnegative. Let \(M\) be account04/B14's total pivotality Fourier depth. Their Bernoulli selector uses
\[
t_*=1-\frac{J}{4M}
\]
and proves
\[
\mathbb E C_{A_{t_*}}\ge\frac{J^2}{8M}.
\tag{6.2}
\]

Because \(h_2(p_i)/p_i\ge r_\lambda\), every active \(p_i\) lies below the scalar threshold \(\sigma(r_\lambda)\). Concavity of \(\mathfrak j\) therefore gives
\[
\mathfrak j'(p_i)\ge\kappa(r_\lambda)
:=\mathfrak j'(\sigma(r_\lambda)).
\tag{6.3}
\]
Average (5.5) over \(A_{t_*}\). The left side is \(t_*S_{r_\lambda}\); the right side is at least
\[
(\rho+\kappa(r_\lambda))\mathbb E C_{A_{t_*}}.
\]
Using (6.2) and dividing by \(t_*=(4M-J)/(4M)\) gives
\[
\boxed{
S_{r_\lambda}
\ge
(\rho+\kappa(r_\lambda))
\frac{J^2}{8M-2J}.
}
\tag{6.4}
\]
Equivalently, since
\[
S_{r_\lambda}=S_\rho-\lambda a_dJ,
\]
we have the double-charge form
\[
\boxed{
S_\rho
\ge
\lambda a_dJ
+
(\rho+\kappa(\rho+\lambda a_d))
\frac{J^2}{8M-2J}.
}
\tag{6.5}
\]

The inherited product obstruction charged only posterior crossing. Equation (6.5) says that the same critical core must simultaneously finance the explicit activation shift \(\lambda a_dJ\) **and** the posterior-crossing/mixed-depth term out of one scalar Shannon-slack bank.

This does not yet close FEI because no dimension-free upper bound on \(S_\rho/J\) is proved, and the large-\(M/J\) branch remains possible. But it narrows the remaining interface: any candidate high core that survives a positive activation penalty must have enough scalar slack to pay (6.5), while account04's high-\(M\) branch is already tied to the Palm/prefix programme.

## 7. Numerical thresholds from the analytic formulas

These are evaluations of the proved scalar thresholds, not finite evidence for FEI.

\[
\begin{array}{c|c|c|c}
 d&a_d&\theta_d&a\text{-locking ratio }h_2(\theta_d)/\theta_d\\\hline
2&0.5&0.3333333333&2.7548875022\\
3&0.4444444444&0.3076923077&2.8940978307\\
4&0.421875&0.2967032967&2.9565685074\\
10&0.3874204890&0.2792379758&3.0597930592\\
\infty&e^{-1}&1/(e+1)&3.1231393577
\end{array}
\]

Thus the universal gauge-lock threshold is substantially below the corrected ratios already reached by the currently relevant hard FEI branch.

## 8. What changed and the next exact arrow

### Proved this run

1. A one-bit variational inequality for every folded-activation minimizing character.
2. A universal **high-ratio gauge-lock theorem**: once the critical ratio exceeds \(3.1231393576\ldots\), the dimension-cooling activation minimizer is exactly the median character gauge.
3. A multiplicity-strengthened block activation lower bound \(\Lambda_A\ge a_dJ_A\) on that core.
4. The activation-strengthened curvature-refunded all-block inequality (5.5).
5. Combining (5.5) with account04/B14's posterior-variance selector gives the sharpened product obstruction (6.4)--(6.5).

### Still open

Full FEI remains OPEN. The sharp remaining route is now:

> control the same-core pair \((S_\rho,M)\) strongly enough that (6.5) fails for some fixed \(\lambda>0\), or use the large-\(M/J\) branch to trigger a separately paid Palm/prefix restriction.

A particularly concrete target is a dichotomy of the form
\[
S_\rho\le C_1J+C_2\frac{J^2}{M}
\]
with constants strong enough to contradict (6.5) after optimizing \(\lambda\), or an equivalent realizable block selector. No such bound is proved here.

This run therefore changes the mechanism and strengthens the universal critical-core constraints, but does **not** claim a solution of FEI.
