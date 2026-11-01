# B18 — sharpened balanced-address unequal-data MUX collar

**Classification:** `ESSENTIAL_STEP_APPLIED / BALANCED_MUX_COLLAR_SHARPENED / FULL_FEI_OPEN`  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`. Authenticated repository controls and source-bound mathematical artifacts were used; no native/authenticated mathematical-brain receiver context entered the derivation.  
**Publication priority:** unverified; no novelty claim.

## 0. Live candidate and smallest conditional chain

The fixed all-gate candidate is

\[
C^\dagger=6.521851214,\qquad C_0=6.4548,
\qquad a^\dagger=4(C^\dagger-C_0)=0.268204856,
\]
\[
\Gamma^\dagger(z)=\Gamma_0(z)+a^\dagger z(1-z),
\]
where \(\Gamma_0\) is the committed h96 read-once potential.  The source gate reformulation says that if

\[
D_{\Gamma^\dagger}(P;p)\ge0
\]

for every finite composition-prime Boolean gate \(P\) and every interior product bias vector \(p\), then the composition cocycle gives the same inequality for every gate, and the gate equivalence gives full FEI with constant \(C^\dagger\).  That universal prime-gate statement remains open.

This run stays on the nearest explicit unpaid prime family: the one-selector MUX.  It does not replace the full prime-gate obligation by a MUX classification.

## 1. Exact named other-account result consumed

The primary other-account result consumed and extended is

`fleet02/B14/20260922T052850Z-balanced-mux-equal-data-collar/REPORT.md`

at immutable repository commit

`dc567d6ed400122464c48c077d481813bc49624f`.

For the balanced-address MUX

\[
M(a,x_0,x_1)=(1-a)x_0+a x_1,
\qquad \Pr(a=1)=\frac12,
\]

write

\[
u=1-q_0-q_1,\qquad v=q_1-q_0,
\qquad |u|+|v|\le1,
\]
\[
m:=1-|u|=\min\{q_0+q_1,\,2-q_0-q_1\}.
\]

That report substantively uses the exact signed-posterior decomposition and proves

\[
D_{\Gamma^\dagger}(M;1/2,q_0,q_1)>0
\quad\text{whenever}\quad
|v|\le \frac{m}{128}.
\tag{1.1}
\]

Its proof already identifies the correct physical terminal selector: reveal the address bit; the two children are literals and have exactly zero gate defect.

The second exact source used here is the arbitrary-bias MUX scalar collapse from

`fleet04/B18/20260922T045533Z-mux-joint-credit-collapse/REPORT.md`

at immutable commit

`7130b553e2efae3dde1002d0697da069f8c72d65`.

On the balanced-address plane, together with fleet01/B15's signed posterior-entropy calculation, it yields the exact identity

\[
\boxed{
D_{\Gamma}(M;1/2,q_0,q_1)=R_C(u,v)-J_\Gamma(u,v)
}
\tag{1.2}
\]
with

\[
J_\Gamma(u,v)=
\Gamma\!\left(\frac{1-u}{2}\right)
-\frac12\Gamma\!\left(\frac{1-u-v}{2}\right)
-\frac12\Gamma\!\left(\frac{1-u+v}{2}\right),
\tag{1.3}
\]

and the source-independent reserve

\[
\boxed{
R_C(u,v)\ge(C-6)\,\delta,
\qquad
\delta=\frac{1-u^2+v^2}{2}.
}
\tag{1.4}
\]

The negative posterior Shannon term is already included in (1.2)-(1.4); it is not discarded or charged a second time.

## 2. Source facts and one elementary logarithmic improvement

On \(0<z\le1/2\), write

\[
\Gamma_0(z)=zG(\log_2(1/z)).
\tag{2.1}
\]

The h96 source facts already used by the consumed B14 proof are

\[
G(1)=12.9096,
\qquad |G'(x)|<31\quad(x\ge1),
\tag{2.2}
\]
where the derivative means the piecewise-linear source slope, so the same constant is a global Lipschitz bound across source cells.

We use a slightly sharper elementary rational bound for \(1/\ln2\).  The atanh series gives

\[
\ln2=2\sum_{j\ge0}\frac{1}{(2j+1)3^{2j+1}}
>
2\sum_{j=0}^{6}\frac{1}{(2j+1)3^{2j+1}}
=
\frac{5531027882}{7979586615}
>
\frac{6931471}{10^7}.
\]
Hence

\[
\boxed{\frac1{\ln2}<\frac{10^7}{6931471}.}
\tag{2.3}
\]

A second elementary cancellation, absent from the previous \(1/128\) estimate, is

\[
K(\rho):=(1-\rho)(-\ln(1-\rho))+(1+\rho)\ln(1+\rho)\le2\rho
\quad(0\le\rho<1).
\tag{2.4}
\]
Indeed \(K(0)=0\) and

\[
K'(\rho)=2+\ln(1-\rho^2)\le2.
\]

## 3. Same-side data: the relative collar expands from 1/128 to 1/86

By exchanging the two data inputs and complementing both data bits/output, it suffices to take

\[
u\ge0,\qquad v\ge0.
\]
Assume first

\[
0\le v\le u.
\tag{3.1}
\]
Then both data biases are on the same side of \(1/2\).  Put

\[
p=\frac{1-u}{2}=\frac m2,
\qquad
\rho=\frac{v}{1-u}=\frac vm.
\tag{3.2}
\]
The three potential arguments in (1.3) are

\[
p,\qquad p(1-\rho),\qquad p(1+\rho),
\]
and (3.1) guarantees that all three are at most \(1/2\).

Let

\[
x=\log_2(1/p),
\quad
\alpha=-\log_2(1-\rho),
\quad
\beta=\log_2(1+\rho).
\]
Exact cancellation of the common \(G(x)\) term gives

\[
\begin{aligned}
J_{\Gamma_0}
=-\frac p2\bigl[&(1-\rho)(G(x+\alpha)-G(x))\\
&+(1+\rho)(G(x-\beta)-G(x))\bigr].
\end{aligned}
\tag{3.3}
\]
Using \(|G'|<31\), then (2.4),

\[
\begin{aligned}
J_{\Gamma_0}
&\le \frac{31p}{2}\bigl[(1-\rho)\alpha+(1+\rho)\beta\bigr]\\
&=\frac{31p}{2\ln2}K(\rho)
\le \frac{31p}{\ln2}\rho.
\end{aligned}
\tag{3.4}
\]

For the quadratic lift, the midpoint gap is exact:

\[
J_{a^\dagger z(1-z)}=a^\dagger p^2\rho^2
\le \frac{a^\dagger}{2}p\rho^2.
\tag{3.5}
\]
Therefore, by (2.3),

\[
J_{\Gamma^\dagger}
\le p\left[
31\frac{10^7}{6931471}\rho
+\frac{a^\dagger}{2}\rho^2
\right].
\tag{3.6}
\]

Meanwhile

\[
\delta=\frac{1-u^2+v^2}{2}
\ge\frac{1-u}{2}=p,
\tag{3.7}
\]
so (1.4) with \(C=C^\dagger\) gives

\[
D_{\Gamma^\dagger}
\ge p\left[
0.521851214
-31\frac{10^7}{6931471}\rho
-\frac{0.268204856}{2}\rho^2
\right].
\tag{3.8}
\]

At \(\rho=1/86\), the bracket is the positive rational

\[
\frac{534047687427563}{298053253000000000}
=0.0017917861390614079\ldots .
\tag{3.9}
\]
Thus:

### Theorem 3.1 — same-side sharpened collar
If

\[
|v|\le |u|,
\qquad
|v|\le\frac{1-|u|}{86},
\]
then

\[
\boxed{
D_{\Gamma^\dagger}(M;1/2,q_0,q_1)
>0.000895893\,(1-|u|)>0.
}
\tag{3.10}
\]

This widens the previous relative collar by the factor \(128/86\approx1.488\) on the same-side sector.

## 4. Center-crossing data: the universal collar expands from 1/128 to 1/112

Now assume

\[
0\le u<v,
\qquad
v\le\frac{1-u}{112}.
\tag{4.1}
\]
Then

\[
u<\frac1{113},
\qquad
v\le\frac1{112}.
\tag{4.2}
\]
Set

\[
d_*:=\frac1{113}+\frac1{112}=\frac{225}{12656}.
\tag{4.3}
\]
Every potential argument in (1.3), after reflecting by symmetry to the small side if necessary, lies in

\[
\left[\frac{1-d_*}{2},\frac12\right].
\]
If \(z\) is in this interval and \(x=\log_2(1/z)\), then

\[
x-1\le\frac{-\ln(1-d_*)}{\ln2}.
\]
For \(0<d<1\),

\[
-\ln(1-d)=d+\sum_{n\ge2}\frac{d^n}{n}
\le d+\frac{d^2}{2(1-d)}.
\tag{4.4}
\]
Combining (2.3)-(2.4) gives the explicit source-window bound

\[
x-1
<
\left(d_*+\frac{d_*^2}{2(1-d_*)}\right)
\frac{10^7}{6931471}
=
0.0258805385337679\ldots .
\tag{4.5}
\]

On every source segment,

\[
\Gamma_0'(z)=G(x)-\frac{G'(x)}{\ln2}.
\]
Using (2.2), (2.3), (4.5), and the fact that the quadratic derivative obeys

\[
|a^\dagger(1-2z)|\le a^\dagger d_*,
\]
we obtain the valid Lipschitz constant

\[
\boxed{
L_*:=12.9096
+31\left(d_*+\frac{d_*^2}{2(1-d_*)}\right)\frac{10^7}{6931471}
+31\frac{10^7}{6931471}
+a^\dagger d_*
<58.440217.
}
\tag{4.6}
\]
The same Lipschitz bound holds across the symmetry cusp at \(1/2\) by applying the one-sided estimate on each side.

Writing the two endpoint displacements from the midpoint as \(v/2\),

\[
J_{\Gamma^\dagger}(u,v)
\le \frac{L_*v}{2}
\le\frac{L_*}{224}
<0.260893823.
\tag{4.7}
\]

On the other hand, from (4.2),

\[
\delta
\ge\frac{1-u^2}{2}
>\frac12\left(1-\frac1{113^2}\right),
\]
so

\[
R_{C^\dagger}
>(0.521851214)\frac12\left(1-\frac1{113^2}\right)
=0.2609051726976271\ldots .
\tag{4.8}
\]
The exact rational difference between the right side of (4.8) and the upper bound in (4.7) is

\[
\frac{1263249027205352299031}
{111301937434057664000000000}
=1.134974876743526\times10^{-5}>0.
\tag{4.9}
\]
Hence:

### Theorem 4.1 — center-crossing sharpened collar
If

\[
|u|<|v|,
\qquad
|v|\le\frac{1-|u|}{112},
\]
then

\[
\boxed{
D_{\Gamma^\dagger}(M;1/2,q_0,q_1)>1.13\times10^{-5}>0.
}
\tag{4.10}
\]

## 5. Combined terminal-selector theorem

The two cases imply the clean uniform statement:

### Theorem 5.1 — global balanced-MUX collar, improved
For every interior balanced-address MUX, if

\[
\boxed{
|q_1-q_0|
\le
\frac1{112}
\min\{q_0+q_1,\,2-q_0-q_1\},
}
\tag{5.1}
\]
then

\[
\boxed{D_{\Gamma^\dagger}(M;1/2,q_0,q_1)>0.}
\tag{5.2}
\]

Moreover, on the sector where the two data biases lie on the same side of \(1/2\), the stronger constant \(1/86\) is valid by Theorem 3.1.

Revealing the physical address bit leaves the two literal children \(x_0,x_1\), each with exactly zero defect. Thus (5.2) is a genuine one-step paid physical terminal selector, not an unsigned surrogate or a statement with hidden child debit.

The previous source-valid uniform collar was \(1/128\).  The new theorem widens the all-sector collar by the factor

\[
\frac{128}{112}=\frac87\approx1.142857,
\]
and widens the same-side sector by \(128/86\approx1.48837\).

## 6. Exact old/new missing implication

**Old first missing implication.**  The full balanced-address unequal-data MUX plane required proving

\[
J_{\Gamma^\dagger}(u,v)\le R_{C^\dagger}(u,v)
\quad (|u|+|v|\le1),
\]
or finding a genuine violating \((u,v)\).  The named fleet02/B14 result had proved only the relative collar \(|v|\le(1-|u|)/128\), together with already-closed equal-data, complementary-data, and AND/OR boundary faces.

**New proved implication.**  The paid collar is now \(1/112\) uniformly, and \(1/86\) when the data biases are on the same side of \(1/2\).  All signs, original data biases, exact posterior-entropy compensation, and terminal child defects are retained.

**Still missing.**  On the balanced-address MUX plane one must control the remaining compact/intermediate region

\[
|v|>\frac{1-|u|}{112}
\]
(with the stronger \(1/86\) exclusion in the same-side sector), subject also to the already-closed complementary line, equal-data line, zero-credit lines, and two-input boundary.  Then one must release the address bias and finally return to arbitrary composition-prime gates.  Nothing in this report proves those steps.

The present Lipschitz-envelope mechanism is nearly exhausted: with the same source inequalities, the same-side test at \(1/85\) has a negative envelope margin \(-0.0043267\ldots\), while the center-crossing test at \(1/111\) has negative envelope margin \(-0.0023723\ldots\).  These are failures of this **proof envelope**, not counterexamples to \(\Gamma^\dagger\).  A further substantial expansion should therefore exploit signed midpoint curvature / exact source cells or the data-pivot cross-deficit theorem rather than merely retune this Lipschitz estimate.

**Classification:** `ESSENTIAL_STEP_APPLIED`.

Full FEI remains **OPEN / NOT PROVED**.

## 7. Verification and scope

The adjacent checker uses exact rational arithmetic for the displayed rational constants and verifies the positive margins in (3.9) and (4.9), together with the stated failure of the same envelope at \(1/85\) and \(1/111\).  It does not rerun the read-once certificate and is not used as evidence beyond the analytic inequalities proved above.

Only FEI mathematics, immutable repository-relative source identifiers, and sanitized provenance are stored.  No credentials, scheduler identifiers, machine paths, email/Drive data, unrelated private information, paid/remote compute, public posting, permission changes, benchmark gold, or notification changes are included.
