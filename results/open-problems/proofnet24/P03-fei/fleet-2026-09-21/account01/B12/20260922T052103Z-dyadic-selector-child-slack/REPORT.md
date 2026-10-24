# B12 — child-slack completion of the full dyadic B0 selector spine

**Run:** `20260922T052103Z-b12-fei-r11`  
**Classification:** `ESSENTIAL_STEP_APPLIED / SOURCE-VALID SUBCLASS CLOSED`  
**Live candidate:** `LIMIT-PRIME-GATE-LIFT-v1` with
\[
C_*=6.5218512,\qquad
a_*=0.2682048,\qquad
\Gamma_*(p)=\Gamma_{\rm RO}(p)+a_*p(1-p).
\]
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact source inputs and the live missing implication

The newest compatible campaign-lead state consumed is

`account03/B18/20260922T051809Z-finite-pattern-fourier-dust/REPORT.md`

(report blob `a85d8993f9536d933ec796dcb9356293564c470e`). It keeps the exact live
candidate `LIMIT-PRIME-GATE-LIFT-v1`:
\[
D_{\Gamma_*}(P;p)\ge0
\]
for every finite composition-prime Boolean gate \(P\) and every interior
product-bias vector \(p\). By the already-proved gate composition theorem,
this universal statement would imply FEI with constant \(C_*\). It remains
open.

The named **other-account theorem used substantively** is account03/B16

`account03/B16/20260922T045649Z-b0-dyadic-selector-spine/REPORT.md`

(report blob `8f23ed6e3145e6918f2883e04de0b61250e081db`). It analyzes the genuine
four-input composition-prime gate
\[
B_0^{-1}(1)=\{0,1,2,3,4,5,8,10\}\subset Q_4
\]
when one selector coordinate has bias \(t\) and the other three physical
biases are \(1/2\). If \(q=1-t\), its two restrictions have
\[
r_0=\frac34,\qquad r_1=\frac14,\qquad
\delta=\frac12,
\]
and its **exact conditional Shannon credit** is
\[
\boxed{\mathcal C(t)=h_2(2tq)-\frac14h_2(4tq).}
\tag{1.1}
\]
Consequently the exact local gluing term for any symmetric potential is
\[
\boxed{
L_\Gamma(t)
=
\Gamma(1/4)-\Gamma(1/4+t/2)
+\frac12\Gamma(t)
+\frac14h_2(4tq)-h_2(t).
}
\tag{1.2}
\]
This is the source-exact Shannon increment: no branch/KL credit is dropped.

I also use the exact account04/B17 one-coordinate defect cocycle
`account04/B17/20260922T031352Z-biased-restriction-margin-cocycle/REPORT.md`:
\[
D_\Gamma(G)
=qD_\Gamma(G_0)+tD_\Gamma(G_1)+L_\Gamma(t)
\tag{1.3}
\]
for this selector convention. Thus the children’s already-earned slack must
be retained. Dropping it is precisely the invalid naive arity step flagged by
the owner state.

## 2. The peer's remaining dyadic-tail gap

Let
\[
\Gamma_{\rm cert}(p)=\Gamma_{\rm RO}(p)+c\,p(1-p),
\qquad c=0.01.
\tag{2.1}
\]
This is the proved binary read-once certificate, with center \(6.4573\).

For every dyadic selector
\[
t=2^{-m},\qquad m\ge2,
\tag{2.2}
\]
account03/B16 proves
\[
\boxed{
L_{\Gamma_{\rm cert}}(t)
\ge
B(t)+c\left(\frac{t^2}{2}-\frac1{16}\right),
}
\tag{2.3}
\]
where
\[
\begin{aligned}
(\ln2)B(t)
={}&-(1-2t)^2\ln(1-2t)+(1-t)^2\ln(1-t)+5t^2\ln t\\
&-(2t^2+2t+\tfrac12)\ln(1+2t)
+t(6t+6.4548-2)\ln2.
\end{aligned}
\tag{2.4}
\]
The same report proves analytically, by concavity,
\[
\boxed{B(t)>0\qquad(0<t\le1/4).}
\tag{2.5}
\]

The peer closed \(m=2,\dots,12\) by requiring the **local** remainder itself
to be positive. Its lower certificate becomes negative at \(m=13\) because
the term \(-c/16=-0.000625\) survives as \(t\downarrow0\). The report
correctly identified this as a bridge artifact, not a counterexample.

The missing step is therefore exactly the one demanded by the owner reset:
retain the children’s slack in the same conditional-Shannon recursion.

## 3. Exact child slack

Both restrictions of \(B_0\) on this selector line are a uniform two-input
AND/NAND-type gate. For either child,
\[
I_{\rm child}=1,\qquad
\widetilde H_{\rm child}=2,\qquad
p_{\rm out}\in\{1/4,3/4\}.
\tag{3.1}
\]
The dyadic read-once equality gives
\[
\Gamma_{\rm RO}(1/4)=6.4548-2.
\tag{3.2}
\]
Since
\[
C_*=6.4548+\frac{a_*}{4},
\qquad
\Gamma_*(1/4)=6.4548-2+\frac{3a_*}{16},
\tag{3.3}
\]
the stable-candidate defect of **each** child is exactly
\[
\boxed{
D_{\Gamma_*}(G_0)=D_{\Gamma_*}(G_1)
=C_*-\Gamma_*(1/4)-2
=\frac{a_*}{16}
=0.0167628.
}
\tag{3.4}
\]
This is not a new charge and not an assumed induction reserve; it is the
already-earned exact defect of the two actual restrictions.

## 4. New theorem — the entire infinite dyadic selector tail is safe

Because
\[
\Gamma_*=\Gamma_{\rm cert}+(a_*-c)p(1-p),
\]
and account03/B16 computes the exact local quadratic currency
\[
\mathcal W(t)=\frac{tq}{4},
\]
we have
\[
\boxed{
L_{\Gamma_*}(t)
=
L_{\Gamma_{\rm cert}}(t)
+(a_*-c)\frac{tq}{4}.
}
\tag{4.1}
\]

Insert (2.3) and (3.4) into the exact cocycle (1.3). Since the two child
defects coincide,
\[
\begin{aligned}
D_{\Gamma_*}(B_0;t)
&=q\frac{a_*}{16}+t\frac{a_*}{16}+L_{\Gamma_*}(t)\\
&\ge
\frac{a_*}{16}
+B(t)
+c\left(\frac{t^2}{2}-\frac1{16}\right)
+(a_*-c)\frac{tq}{4}\\
&=
\boxed{
\frac{a_*-c}{16}
+B(t)
+\frac c2\,t^2
+(a_*-c)\frac{tq}{4}.
}
\tag{4.2}
\end{aligned}
\]
Every term after the first is nonnegative for \(0<t\le1/4\), and \(B(t)\)
is strictly positive there. Therefore:

### Theorem 4.1
For every integer \(m\ge2\),
\[
\boxed{
D_{\Gamma_*}\!\left(B_0;\frac12,\frac12,2^{-m},\frac12\right)
>
\frac{0.2682048-0.01}{16}
=
0.0161378
>0.
}
\tag{4.3}
\]

Thus **all** dyadic selector points \(t=2^{-m}\), including the previously
unclosed infinite tail \(m\ge13\), satisfy the live all-gate inequality with
a uniform positive reserve. The prior B12 uniform-anchor calculation already
closes \(m=1\), so together the entire inverse-power-of-two selector spine is
safe.

The key point is conceptual as well as numerical: the local bridge loses at
most the fixed \(0.000625\) certificate term, while the exact binary children
carry \(0.0167628\) of stable-candidate defect. The negative local certificate
therefore never threatens the parent. Requiring \(L_{\Gamma_*}(t)\ge0\) was
strictly stronger than necessary.

## 5. Decisive numerical cross-check

A direct evaluation of the analytic lower bound (4.2) gives, for example,
\[
\begin{array}{c|c|c}
m&t&\text{lower bound for }D_{\Gamma_*}(B_0;t)\\ \hline
2&1/4&0.2507122433443495\ldots\\
12&2^{-12}&0.01723729011227957\ldots\\
13&2^{-13}&0.01668843732627846\ldots\\
20&2^{-20}&0.01614210989377867\ldots
\end{array}
\]
and the lower bound tends along the far tail to \(0.0161378\) from above.
These numerics only check the algebra; Theorem 4.1 is the analytic consequence
of (2.3), (2.5), the exact child defect, and the exact cocycle.

## 6. Exact old/new missing implications

**Old missing implication.** On the \(B_0\) selector line, account03/B16 had
a rigorous local certificate only through \(m=12\); its black-box bridge went
negative at \(m=13\), leaving the infinite dyadic tail unresolved unless one
retained additional slack.

**New proved implication.** The exact children contribute \(a_*/16\) at
every selector bias. Keeping this term in the source-exact Shannon/defect
cocycle yields the uniform lower bound (4.3), closing every dyadic selector
bias \(2^{-m}\), \(m\ge2\), and together with the already-closed uniform
anchor, the full inverse-power-of-two spine.

**Still missing.** This does not prove the continuous all-bias \(B_0\)
inequality, and it does not prove `LIMIT-PRIME-GATE-LIFT-v1` for arbitrary
composition-prime gates. The next sharp \(B_0\) step is to replace the
dyadic-chain equality used in (2.3) by a no-loss interpolation valid for
every \(t\in(0,1/4]\), while continuing to retain the same child slack.
Beyond \(B_0\), the universal prime-gate statement remains open.

The latest sparse-defect result from account03/B18 independently closes every
fixed finite balanced point-defect pattern under dummy dilution at slope \(4\).
Thus this run does not reopen addressing/majority/tribes/tensor/sparse-dust
mechanisms already screened in the current state; it attacks the live biased
prime-gate tail directly.

## 7. Scope and verification label

Classification is `ESSENTIAL_STEP_APPLIED / SOURCE-VALID SUBCLASS CLOSED`.
No claim of a universal FEI proof is made. No arbitrary spectral law,
unsigned replacement, uncharged coordinate label, coverage hypothesis, or
circular potential is used. The only inherited inequalities are the exact
named peer results above, applied with their stated hypotheses.

Scoped privacy review: this file contains only FEI mathematics, logical
account/slot labels, repository-relative source identifiers, nonsecret Git
blobs, and sanitized run metadata. No credentials, scheduler IDs, machine
paths, unrelated private material, email/Drive content, workflow dispatch,
paid/remote compute, public posting, or permission change appears.
