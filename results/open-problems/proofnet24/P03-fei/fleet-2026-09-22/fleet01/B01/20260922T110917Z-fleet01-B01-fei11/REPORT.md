# fleet01/B01 — fixed positive Boolean-dependence reserve is impossible

**Run:** `20260922T110917Z-fleet01-B01-fei11`  
**Programme:** `FEI-ALL-TEAM-20260922T095941Z`  
**Assignment:** credit-augmented Bellman supersolution  
**Classification:** `CANDIDATE_REFUTED / FIXED_POSITIVE_CREDIT_RESERVE_NOGO / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

Full uniform-cube Fourier entropy–influence remains **OPEN / NOT PROVED**. This report refutes a stronger Bellman invariant proposed in the preceding fleet01/B01 run. It does **not** refute FEI.

## 1. Fresh state and exact peer inputs

The current owner control is revision `2026-09-22.3`, programme `FEI-ALL-TEAM-20260922T095941Z`; the native task's older FOREST text is superseded. The canonical FEI state remains `FEI-20260922T1000Z-v1`, with the mandatory correction ledger through `FEI-DELTA-20260922-14` consumed and no pending correction in the inbox at the initial coherent snapshot.

The exact sources used are:

1. **Influence I-projection / Boolean-dependence credit:** `yspennstate/math-open-problems@4bd6d05f1eb8325d665f2748f4d74dcee2550a04:proofnet24/P03-fei/fleet-2026-09-21/fleet02/B15/20260922T0829Z-influence-iprojection-kl/REPORT.md`, Theorems 2.1 and 3.1 and Section 4. For the nonempty spectral law `P` with occurrence marginals `r`,
   \[
   K_{\rm occ}=H_{\max}(r)-H(P)\ge0.
   \]
2. **Preceding B01 signed-transfer identity:** `yspennstate/math-open-problems@374c4874e914c7414abc9109fadf77cfc3947298:proofnet24/P03-fei/fleet-2026-09-22/fleet01/B01/20260922T103250Z-fleet01-B01-fei-r11/REPORT.md`. It defined
   \[
   A_{\Gamma,\lambda}=D_\Gamma-\lambda C,\qquad C=vK_{\rm occ},
   \]
   and the exact physical-restriction recursion with signed transfer `Xi_j`.
3. **Named assigned partner result consumed:** `yspennstate/math-open-problems@ed6d63ec14a43ed8d4e595bb3f9cb6ac2d42db72:proofnet24/P03-fei/fleet-2026-09-22/fleet02/B01/20260922T110344Z-fleet02-B01-fei-r18/REPORT.md`. Its exact two-gate Farkas calculation shows the current singleton-safe shaped family is already squeezed to the center scale `6.55844528...`; in particular the current source candidate center is
   \[
   C_*=6.5584452830718243825\ldots<7.
   \]
4. **Boundary desingularization:** `yspennstate/math-open-problems@74e1f1da10b68c92ae3eaf6edf4f5990c8e8f2fc:proofnet24/P03-fei/fleet-2026-09-22/fleet03/B04/20260922T105911Z-boundary-bellman-desingularization/REPORT.md`, Theorem 4.1. It proves that selector-bias faces do not themselves create a `1/s` blow-up after the exact Poincare factor is cancelled.

The new obstruction below is at **uniform input bias** and therefore is orthogonal to the boundary singularity resolved in item 4.

## 2. Why the coefficient `lambda=1` looked attractive

Let
\[
M(G;p):=vH_{\max}(r),\qquad C(G;p)=vK_{\rm occ}=vH_{\max}(r)-vH(P).
\]
Because the full spectral entropy is
\[
\widetilde H=h_2(v)+vH(P),
\]
the signed transfer satisfies the exact algebraic identity
\[
\Xi_j=\Delta M-\Delta\widetilde H+\Delta h_2(v).
\tag{2.1}
\]
Consequently at `lambda=1` the difficult conditional spectral-entropy increment cancels from the local augmented recursion. Writing
\[
F(u)=\Gamma(u)+h_2(V_u),
\]
one obtains
\[
L_\Gamma-\Xi_j
=(1-s)F(q_0)+sF(q_1)-F(q)+dF(s)
-\Big(M(G)-[(1-s)M(G_0)+sM(G_1)]\Big).
\tag{2.2}
\]
Equivalently,
\[
A_{\Gamma,1}=D_\Gamma-C=vB_{\inf}^{\Gamma}.
\tag{2.3}
\]
Thus `lambda=1` removes all higher-order spectral dependence from the state. The theorem below shows that this attractive strengthening is globally impossible, and in fact **every fixed `lambda>0` is impossible**.

## 3. A balanced antipodal two-flip dictator family

For `n>=4`, on the uniform cube `{−1,1}^n`, start with the dictator
\[
f_0(x)=x_1.
\]
Let
\[
z^+=(1,\ldots,1),\qquad z^-=(-1,\ldots,-1),
\]
and flip the values at exactly these two antipodal points:
\[
f_n(z^+)=-1,\qquad f_n(z^-)=+1,
\]
with `f_n=f_0` elsewhere. One `+1` and one `−1` value are exchanged, so `f_n` remains exactly balanced.

Put
\[
\delta=2^{2-n}.
\]
For the standard uniform Walsh characters, the two-point perturbation changes coefficient `S` by
\[
2^{1-n}\bigl((-1)^{|S|}-1\bigr),
\]
so every even coefficient is unchanged, while every odd coefficient receives `-delta`. Therefore
\[
\widehat f_n(\{1\})=1-\delta,
\]
\[
\widehat f_n(S)=-\delta
\quad\text{for every other odd }S,
\]
and all remaining coefficients vanish. Hence the squared spectral law has one atom of mass `(1-delta)^2` and
\[
M_n:=2^{n-1}-1
\]
other atoms, each of mass `delta^2`. Parseval is exact because
\[
(1-\delta)^2+M_n\delta^2=1.
\tag{3.1}
\]

## 4. Exact influence vector

The sum of cardinalities over all odd subsets of `[n]` equals `n2^{n-2}`. Hence
\[
I(f_n)
=(1-\delta)^2+\delta^2\bigl(n2^{n-2}-1\bigr)
=1+(n-2)\delta.
\tag{4.1}
\]
Set
\[
\varepsilon_n:=I(f_n)-1=(n-2)\delta.
\tag{4.2}
\]
Because the function is balanced, `v=1` and the nonempty spectral law is the whole spectral law. Its occurrence marginals are
\[
r_1=1-\delta,
\qquad
r_i=\delta\quad(2\le i\le n).
\tag{4.3}
\]
Indeed the number of odd subsets containing any prescribed coordinate is `2^{n-2}`.

## 5. The maximum-entropy I-projection grows by at least `(n-1) epsilon_n`

Let `c_n` be the I-projection parameter from the source theorem. It is the unique positive solution of
\[
1-c=[1-c(1-\delta)](1-c\delta)^{n-1}.
\tag{5.1}
\]
Define
\[
c_0={n-2\over n-1},\qquad x=(n-2)\delta.
\]
At `c=c_0`, the right side of (5.1) is
\[
{1\over n-1}(1+x)\left(1-{x\over n-1}\right)^{n-1}
\le {1\over n-1}(1+x)e^{-x}
\le {1\over n-1}=1-c_0.
\tag{5.2}
\]
Since the positive solution of (5.1) is unique and the difference changes sign before `c=1`,
\[
\boxed{c_n\ge {n-2\over n-1}.}
\tag{5.3}
\]
For `n>=4`, this implies
\[
c_n(1-\delta)\ge\frac12.
\tag{5.4}
\]
Consequently, using symmetry and monotonicity of binary entropy on `[0,1/2]`,
\[
h_2(c_n(1-\delta))-h_2(c_n)\ge0.
\tag{5.5}
\]
The exact I-projection formula is
\[
H_{\max}(r)
={h_2(c_n(1-\delta))+(n-1)h_2(c_n\delta)-h_2(c_n)\over c_n}.
\tag{5.6}
\]
By (5.5) and `h_2(u)>=u\log_2(1/u)`,
\[
\begin{aligned}
H_{\max}(r)
&\ge {n-1\over c_n}h_2(c_n\delta)\\
&\ge (n-1)\delta\log_2{1\over c_n\delta}\\
&\ge (n-1)\delta\log_2{1\over\delta}\\
&=(n-1)(n-2)\delta.
\end{aligned}
\]
Therefore
\[
\boxed{H_{\max}(r)\ge (n-1)\varepsilon_n.}
\tag{5.7}
\]

## 6. The actual Fourier entropy is only `O(epsilon_n)`

Let
\[
t_n=M_n\delta^2=2\delta-\delta^2.
\]
The actual spectral entropy is exactly
\[
H(f_n)=h_2(t_n)+t_n\log_2 M_n.
\tag{6.1}
\]
For `n>=4`, `t_n<=1/2`, `t_n>=\delta`, `t_n<=2\delta`, and `M_n<2^{n-1}`. Using
\[
h_2(t)\le t\log_2(e/t),
\]
we obtain
\[
H(f_n)
\le2\delta[(n-2)+\log_2 e]+2\delta(n-1)
\le7(n-2)\delta.
\tag{6.2}
\]
Thus
\[
\boxed{H(f_n)\le7\varepsilon_n.}
\tag{6.3}
\]
Combining (5.7) and (6.3),
\[
\boxed{K_{\rm occ}(f_n)=H_{\max}(r)-H(f_n)\ge(n-8)\varepsilon_n.}
\tag{6.4}
\]
The checker numerically shows the true ratio is much larger; for example at `n=20`,
\[
K_{\rm occ}/(I-1)=16.6765466917\ldots
\]
while the analytic lower bound is `12`.

## 7. Main no-go theorem: no fixed positive reserve fraction can be universal

Let `Gamma` be any symmetric finite-cap potential and write
\[
C_0=\Gamma(1/2)<\infty.
\]
On every balanced uniform Boolean function the all-gate defect is exactly
\[
D_\Gamma=C_0(I-1)-H.
\tag{7.1}
\]
For the family above and any fixed `lambda>0`,
\[
A_{\Gamma,\lambda}
=D_\Gamma-\lambda K_{\rm occ}.
\]
Using (6.4) and `H>=0`,
\[
\boxed{
A_{\Gamma,\lambda}(f_n)
\le [C_0-\lambda(n-8)]\varepsilon_n.
}
\tag{7.2}
\]
Therefore, for every finite `C_0` and every fixed `lambda>0`, choosing
\[
n>8+{C_0\over\lambda}
\tag{7.3}
\]
gives
\[
\boxed{A_{\Gamma,\lambda}(f_n)<0.}
\tag{7.4}
\]

### Theorem

> **No symmetric finite-cap potential can satisfy `D_Gamma >= lambda v K_occ` for every Boolean gate and every product bias with one fixed `lambda>0`.**

Equivalently, the stronger invariant `A_{Gamma,lambda}>=0` proposed in the preceding B01 run cannot close FEI for any fixed positive reserve coefficient.

This is a refutation of the **reserve strategy**, not of FEI. In fact the witness family has actual Fourier entropy only `O(I-1)` and is not a hard FEI family; what diverges is the *maximum-entropy dependence reserve* relative to the small excess influence.

## 8. Exact application of the newly completed fleet02/B01 partner result

The fresh partner report gives the current shaped candidate center
\[
C_*=6.5584452830718243825\ldots<7.
\]
Apply (7.2) with `lambda=1` and `n=15`. Since `n-8=7`,
\[
A_{\Gamma_*,1}(f_{15})
\le(C_*-7)\varepsilon_{15}<0.
\tag{8.1}
\]
Thus the current shaped potential—regardless of its extremely tight two-gate scalar tuning—**cannot** support the `lambda=1` dependence-credit reserve invariant. More generally, for any fixed `lambda>0`, the same candidate fails once `n>8+C_*/lambda`.

This directly applies the partner's center calculation to the B01 Bellman state and shows why another `10^{-9}` scalar retuning cannot repair this obstruction. The state mechanism, not the scalar center, must change.

## 9. Interaction with fleet03/B04 boundary desingularization

The fleet03/B04 theorem removes a possible `1/s` selector-boundary singularity by cancelling the exact Poincare factor before taking the face limit. The present family has **all input biases exactly `1/2`**, so the no-go occurs fully inside the bias cube. Hence there are now two distinct facts:

1. selector-face vanishing is not itself an obstruction after the exact local quotient is used;
2. a fixed positive fraction of total `K_occ` cannot be stored globally, because balanced near-dictator spectra can have
   \[
   K_{\rm occ}/(I-1)\to\infty.
   \]

Any corrected Bellman construction must respect both.

## 10. What survives from the preceding B01 run

The **exact signed-transfer identity** remains valid:
\[
A_{\Gamma,\lambda}(G)
=(1-s)A_{\Gamma,\lambda}(G_0)+sA_{\Gamma,\lambda}(G_1)
+L_\Gamma-\lambda\Xi_j.
\]
The four-bit example with `Xi_j<0` remains valid. What is refuted is the proposed global target `A_{Gamma,lambda}>=0` with one fixed `lambda>0`.

In particular, the algebraic cancellation at `lambda=1`, equation (2.2), is exact but too strong as a universal supersolution condition. The `H_max` envelope itself develops an unbounded rare-direction tax near a dictator even while the true Fourier entropy remains controlled.

## 11. First unpaid implication after the correction

A viable credit-augmented Bellman state must **not reserve a fixed positive fraction of total `K_occ` at every node**. Two source-compatible possibilities remain:

- a **state-dependent reserve price** tending to zero as the spectral law approaches the rank-one/dictator boundary (for the present family, any admissible price must be `O(1/n)=O(1/log(1/delta))` along this sequence); or
- use only **local signed credit transfer** as transient Bellman currency, without requiring a positive fixed fraction of the root credit to remain banked globally.

The next precise B01 target is to derive a noncircular one-step inequality for one of these two mechanisms, retaining child defect and the fleet03/B04 local Poincare currency. A constant-`lambda` restart is now mathematically ruled out.

## 12. Verification and scope

`CHECK.py` reconstructs the exact Parseval identity, `I-1=(n-2)delta`, and occurrence marginals with `Fraction`; it then numerically solves the one-dimensional I-projection equation and checks the proved analytic inequalities. `CHECK.out` is the captured output and ends `STATUS=PASS`.

The checker is a sanity certificate for this explicitly defined family. The theorem (7.4) is analytic and does not depend on numerical root finding. No novelty/priority claim is made. Full FEI remains `OPEN_NOT_PROVED`.
