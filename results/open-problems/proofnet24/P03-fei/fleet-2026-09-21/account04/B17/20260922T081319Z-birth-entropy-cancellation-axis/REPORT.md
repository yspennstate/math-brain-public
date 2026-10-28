# B17 — exact birth-entropy cancellation and a wider five-input prime axis tube

**Run:** `20260922T081319Z-b17-fei-r17`  
**Classification:** `ESSENTIAL_STEP_APPLIED / BOOLEAN_ADVERSARY_AND_REPLACEMENT`.  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

## 0. Live target and consumed B15 theorem


\[
C^\dagger=6.521851214,\qquad
\Gamma^\dagger(p)=\Gamma_0(p)+a^\dagger p(1-p),
\qquad a^\dagger=0.268204856,
\]

and the remaining prime-gate obligation

\[
D_{\Gamma^\dagger}(P;p)\ge0
\]

for every finite composition-prime Boolean gate \(P\) and every interior product bias \(p\).

The named newest compatible other-account B15 result consumed and applied is account03/B15

`proofnet24/P03-fei/fleet-2026-09-21/account03/B15/20260922T073015Z-axis-child-slack-kl/REPORT.md`.

It proves, using exact child slack and a retained negative KL transport credit, that every essential composition-prime five-input gate is safe whenever one bias moves along a coordinate axis by at most \(2\cdot10^{-5}\). It also records that its deliberately coarse entropy envelope fails already at \(2.1\cdot10^{-5}\); this is a failure of that proof envelope, not a Boolean counterexample.

The central prime theorem used by that report gives the rigorous reserve

\[
D_{\Gamma^\dagger}(P;1/2^5)\ge\delta_5=0.004906502214.
\]

I use only the weaker exact decimal floor

\[
\delta_0=0.0049065.
\]

The new step below identifies a Boolean cancellation hidden by the previous Fannes-style leakage term. It both supplies an exact adversary showing the cancellation coefficient is sharp and yields a replacement proof with a larger certified axis tube.

## 1. Exact one-axis Fourier transport

Fix a pivot \(k\), keep the other four inputs uniform, and write

\[
t=\frac12+s,\qquad r=2s.
\]

Let \(g_0,g_1\) be the four-bit restrictions at the pivot. For each residual Fourier index \(A\), write their uniform coefficients as \(u_A,v_A\), and set

\[
c_A=\frac{u_A+v_A}{2},\qquad
e_A=\frac{v_A-u_A}{2}.
\]

The normalized biased transform is exactly

\[
\widehat G_t(A)=c_A+r e_A,\qquad
\widehat G_t(A\cup\{k\})=\sqrt{1-r^2}\,e_A.
\tag{1.1}
\]

If

\[
d=\Pr[g_0\ne g_1],
\]

then Parseval gives

\[
\sum_A e_A^2=d,\qquad
\sum_A c_A^2=1-d,\qquad
\sum_A c_Ae_A=0.
\tag{1.2}
\]

Define the exact newborn-support mass

\[
Z=\{A:c_A=0\},\qquad
\beta=\sum_{A\in Z}e_A^2.
\tag{1.3}
\]

Plainly \(0\le\beta\le d\).

## 2. The birth-entropy cancellation

For every \(A\in Z\), the central pair of spectral masses is

\[
(0,e_A^2),
\]

whereas at bias \(t\) it is

\[
(r^2e_A^2,(1-r^2)e_A^2).
\]

Therefore the entropy increase of this pair is **exactly**

\[
e_A^2h_2(r^2).
\]

Summing,

\[
\boxed{\Delta H_{\rm birth}=\beta h_2(r^2).}
\tag{2.1}
\]

But the pivot contribution on the right side of the all-gate inequality is

\[
\frac{\operatorname{It}_k}{V_t}
\bigl(\Gamma^\dagger(t)+h_2(V_t)\bigr)
=d\bigl(\Gamma^\dagger(t)+h_2(r^2)\bigr),
\]

because \(\operatorname{It}_k=V_t d\) and \(V_t=1-r^2\). Hence the physical pivot payment contains exactly

\[
d\,h_2(r^2),
\]

which pays every newborn atom and leaves the nonnegative surplus

\[
\boxed{(d-\beta)h_2(r^2).}
\tag{2.2}
\]

Thus the singular \(h_2(r^2)\) leakage in the previous generic support-stability envelope is not a real unpaid remainder for Boolean one-axis motion.

## 3. Retain the old-support KL credit exactly

The complement of \(Z\) has the same total spectral mass \(1-\beta\) at the center and off center. Indeed (1.2) gives zero total cross term. Let \(\rho_0,\rho_r\) be the normalized laws on this complement.

At the uniform five-bit center every nonzero Walsh coefficient is a multiple of \(1/16\), so every positive spectral mass is at least \(1/256\). Therefore the score \(\log_2(1/w_0)\) has range at most eight. From (1.1),

\[
\|w_r-w_0\|_{1,Z^c}
\le
2|r|\sqrt{(1-d)(d-\beta)}
+2r^2(d-\beta).
\]

The exact entropy/relative-entropy identity on the fixed support then gives

\[
\boxed{
\begin{aligned}
H_t-H_0\le{}&
\beta h_2(r^2)
+8|r|\sqrt{(1-d)(d-\beta)}
+8r^2(d-\beta)\\
&-(1-\beta)D_{\rm KL,2}(\rho_r\|\rho_0).
\end{aligned}}
\tag{3.1}
\]

No KL credit is discarded in (3.1).

## 4. Replacement defect estimate

For \(j\ne k\), all input biases remain \(1/2\), so their all-gate coefficient is exactly \(C^\dagger\). The other-coordinate influence sum is affine in \(t\), and each four-bit branch has total influence at most four, hence its contribution can decrease by at most

\[
4C^\dagger |s|.
\]

The source-valid B15 regularity bound \(|(\Gamma^\dagger)'|<85\) applies throughout the present interval. Also

\[
|q(t)-q(1/2)|\le d|s|,
\]

because the branch output measures can differ only on the disagreement set. Combining these two potential movements with (2.2) and (3.1) yields

\[
\boxed{
\begin{aligned}
D_{\Gamma^\dagger}(G;t)\ge{}&
D_{\Gamma^\dagger}(G;1/2)
-\bigl[4C^\dagger+170d
+16\sqrt{(1-d)(d-\beta)}\bigr]|s|\\
&-32(d-\beta)s^2
+(d-\beta)h_2(4s^2)
+(1-\beta)D_{\rm KL,2}(\rho_r\|\rho_0).
\end{aligned}}
\tag{4.1}
\]

This is the replacement for the failed \(2.1\cdot10^{-5}\) envelope. It retains both nonnegative information credits instead of charging a generic newborn-support entropy.

## 5. Certified radius \(2.59\cdot10^{-5}\)

For an essential composition-prime five-input gate, \(d=j/16\) for an integer \(1\le j\le15\). The case \(d=0\) makes the pivot irrelevant. The case \(d=1\) has \(g_1=-g_0\), so the gate is a disjoint XOR/XNOR composition of the pivot with \(g_0\), hence is not composition-prime.

Dropping the two positive credits in (4.1), and using \(\beta\ge0\), gives a uniform loss envelope. For \(j\le14\),

\[
170d+16\sqrt{d(1-d)}
\le 170\frac{14}{16}+8=156.75.
\]

For \(j=15\) the same quantity is

\[
159.375+\sqrt{15},
\]

which is larger. Since \(\sqrt{15}<3.873\),

\[
4C^\dagger+170d+16\sqrt{d(1-d)}
<189.335404856.
\]

Also \(32(d-\beta)\le30\). At

\[
\varepsilon=|s|=2.59\times10^{-5},
\]

the total negative loss is therefore strictly below

\[
189.335404856\,\varepsilon+30\varepsilon^2
=0.0049038071100704.
\]

Subtracting from \(\delta_0\) leaves

\[
\boxed{
D_{\Gamma^\dagger}(P;p)
\ge 0.0000026928899296>0
}
\tag{5.1}
\]

whenever exactly one input bias differs from \(1/2\) and

\[
\boxed{|p_k-1/2|\le2.59\times10^{-5}.}
\tag{5.2}
\]

This improves the newest B15 axis radius \(2.00\times10^{-5}\) by \(29.5\%\).

In the owner's requested margin units, when the Poincare denominator \(M_P>0\),

\[
c_P=a^\dagger-\frac{D_{\Gamma^\dagger}}{M_P}.
\]

Since \(M_P\le I(P;p)/4\le5/4\), (5.1) gives the explicit bound

\[
\boxed{c_P(p)\le0.26820270168805632}
\tag{5.3}
\]

throughout the certified axis tube. When \(M_P=0\), the margin quotient is undefined but the positive defect already makes the point harmless.

The derivative-range hypothesis remains valid: even the smallest nonconstant central output mass satisfies \(1/32-\varepsilon>1/64\).

## 6. Exact Boolean adversary: the cancellation coefficient is sharp

The cancellation cannot be improved to \(\beta\le\theta d\) for any universal \(\theta<1\), even after restricting to essential composition-prime five-input gates.

Take the two four-bit branch truth tables

\[
g_0=0x{\rm C7C5},\qquad g_1=0x{\rm 3A38},
\]

and the five-bit table

\[
\boxed{G=0x{\rm 3A38C7C5}.}
\]

The exact Walsh vectors are

\[
u=\frac18(-1,-3,3,1,-1,-3,-5,1,1,-1,1,-1,1,-1,1,-1),
\]

\[
v=\frac18(1,3,-3,-1,1,3,5,-1,1,-1,1,-1,1,-1,1,-1).
\]

Thus \(v=-u\) on the first eight Fourier coordinates and \(v=u\) on the last eight. Consequently

\[
\boxed{d=\beta=\frac78.}
\tag{6.1}
\]

So the newborn entropy is exactly

\[
\frac78 h_2(r^2),
\]

and the pivot's \(h(V_t)\) payment is exactly the same amount: the surplus in (2.2) is zero.

The checker verifies every one of the five variables is relevant and exhausts every proper variable block \(A\) with \(2\le|A|\le4\). For a disjoint functional decomposition through a Boolean child on \(A\), all nonconstant \(A\)-slices would have to be one pattern or its complement. No proper block has this property. Hence this gate is composition-prime under the standard disjoint functional-composition notion used by the prime-gate reduction.

This gate is an adversary to a stronger proof lemma, **not** a counterexample to the live \(\Gamma^\dagger\) inequality.

## 7. Verification, scope and next implication

`CHECKER.py` uses only the standard library. It verifies the exact rational Walsh vectors, \(d=\beta=7/8\), all five relevant variables, absence of every nontrivial decomposition block, the universal prime-axis arithmetic envelope, the derivative interval, and the final positive gap. Its captured output is `PASS`.

No benchmark gold, mocks, paid/remote compute, workflow dispatch, email, Drive, notification changes, unrelated private data, or weakened proof/source gate was used.

**Full-problem change:** `OPEN -> OPEN`.  
**Mechanism change:** generic newborn-support/Fannes charge -> exact Boolean birth payment plus retained old-support KL.  
**Next implication:** use the same birth-payment decomposition when two or more biases move simultaneously. The obstruction is then not atom birth itself but interference between different moving-coordinate pairings; a successful multi-axis analogue would enlarge the current \(4.4\cdot10^{-6}\) full box without sacrificing the exact KL credit.

**Final status:** essential five-input prime axis tube widened and the singular leakage mechanism isolated sharply; unrestricted FEI remains **OPEN / NOT PROVED**.
