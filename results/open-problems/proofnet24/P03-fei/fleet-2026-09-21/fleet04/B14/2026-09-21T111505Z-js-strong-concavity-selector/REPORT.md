# B14 — strong-concavity rebate for recombination and a repaired erasure selector

**Run:** 2026-09-21T11:15:05Z, fleet04/B14  
**Role:** FEI erasure and selector proof  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`  
**Status:** PARTIAL / new proved scalar and selector refinements. **Full uniform-cube FEI remains OPEN / NOT PROVED.**  
**Publication priority:** UNVERIFIED; no novelty claim is made.

This run follows the owner's creative-FEI instruction.  It starts from the current exact
coordinate decomposition
\[
\Delta_iH=B_i+JS_i,\qquad B_i=H(S_i\mid S_{-i}),
\]
and the current singleton prediction-error payment
\[
JS_i\le c_*M_i,\qquad c_*=\frac2{\ln2},
\]
where
\[
M_i=\sum_{T\not\ni i}\min\{p_T,p_{T\cup\{i\}}\},\qquad
p_S=\widehat f(S)^2.
\]
It also uses the current low-influence erasure-selector compiler, which had replaced
the exact recombination term by the tangent bound \(JS_i\le c_*p_i\).  Here
\(p_i=\Pr[i\in S]=\operatorname{Inf}_i(f)\).

The new point is that the binary recombination profile is not merely tangent-bounded:
it is uniformly strongly concave.  Keeping the exact erasure term while Jensenizing
only recombination gives a strictly sharper local payment.  This both repairs a
concrete width-two-tribes obstruction to the fixed-threshold erasure compiler and
produces a weaker remaining existential selector.

## 1. Exact fibre notation

Fix a coordinate \(i\).  For every \(T\subseteq[n]\setminus\{i\}\), put
\[
x_T=p_T,\qquad y_T=p_{T\cup\{i\}},\qquad w_T=x_T+y_T,
\]
and, when \(w_T>0\),
\[
t_T=\frac{y_T}{w_T},\qquad
s_T=\min\{t_T,1-t_T\}\in[0,\tfrac12].
\]
The weights \(w_T\) sum to one.  Define
\[
M_i:=\sum_Tw_Ts_T=\sum_T\min\{x_T,y_T\},
\]
\[
V_i:=\sum_Tw_T(s_T-M_i)^2,
\qquad
Q_i:=\sum_Tw_Ts_T^2=M_i^2+V_i.
\]
The exact fibre formulas are
\[
B_i=\sum_Tw_T h_2(s_T)
\tag{1}
\]
and
\[
JS_i=\sum_Tw_T\,j(s_T),
\qquad
j(s):=1-h_2\!\left(\frac12+\sqrt{s(1-s)}\right).
\tag{2}
\]
Equation (2) follows by writing the two child squared Fourier masses as
\((u_T\pm v_T)^2\), with \(u_T^2=x_T\), \(v_T^2=y_T\).  Conditional on the
erased label \(T\), the restriction-branch posterior has bias
\(|u_Tv_T|/(u_T^2+v_T^2)=\sqrt{s_T(1-s_T)}\).

For \(j_i:=\min\{p_i,1-p_i\}\),
\[
M_i\le j_i.
\tag{3}
\]

## 2. New scalar theorem: recombination is strongly concave

### Theorem 2.1

On \(0\le s\le1/2\), the function
\[
j(s)=1-h_2\!\left(\frac12+\sqrt{s(1-s)}\right)
\]
is increasing and satisfies the uniform strong-concavity bound
\[
\boxed{
j''(s)\le-\frac{4}{3\ln2}.
}
\tag{4}
\]
The constant is sharp at \(s\downarrow0\).

Consequently,
\[
\boxed{
JS_i\le j(M_i)-\frac{2}{3\ln2}V_i
=j(M_i)-\frac{c_*}{3}V_i.
}
\tag{5}
\]
In particular,
\[
\boxed{
JS_i\le j(M_i)\le j(j_i),
}
\tag{6}
\]
and the tangent/second-moment forms
\[
\boxed{
JS_i\le
c_*\!\left(M_i-\frac{Q_i}{3}\right)
\le
c_*\!\left(j_i-\frac{j_i^2}{3}\right).
}
\tag{7}
\]

Thus the existing linear payment \(JS_i\le c_*M_i\) has a universal
quadratic rebate, while (5) is stronger still because it keeps the exact
concave profile and the fibre variance.

### Proof

Work first in natural logarithms.  Set
\[
z=2\sqrt{s(1-s)},\qquad y=1-2s=\sqrt{1-z^2},
\]
and
\[
J(s):=(\ln2)\,j(s)
=\frac{(1+z)\ln(1+z)+(1-z)\ln(1-z)}2.
\]
Let
\[
A(z):=\frac{\operatorname{atanh}z}{z}
=\sum_{k\ge0}\frac{z^{2k}}{2k+1}.
\]
Since \(dz/ds=2y/z\),
\[
J'(s)=2yA(z).
\]
Differentiating once more and expanding \(A\) gives
\[
\frac{J''(s)}4
=
-\frac13-\sum_{m\ge1}\frac{z^{2m}}{2m+3}.
\tag{8}
\]
Indeed, the coefficient of \(z^{2m}\) for \(m\ge1\) is
\[
-\frac1{2m+1}
+\frac{2(m+1)}{2m+3}
-\frac{2m}{2m+1}
=-\frac1{2m+3},
\]
while the constant coefficient is \(-1/3\).  Hence
\[
J''(s)\le-\frac43,
\]
which proves (4) after division by \(\ln2\).  The series also shows equality
of the curvature constant in the limit \(s\downarrow0\).  Monotonicity follows
from \(J'(s)=2yA(z)\ge0\).

For a \(\kappa\)-strongly concave function,
\[
\mathbb E j(S)\le j(\mathbb ES)-\frac\kappa2\operatorname{Var}(S).
\]
Apply this to the probability weights \(w_T\), with
\(\kappa=4/(3\ln2)\), to obtain (5).  Dropping the variance and using
(3) plus monotonicity gives (6).

Finally, strong concavity at the tangent point \(0\), together with
\(j(0)=0\) and
\[
j'(0)=\frac2{\ln2}=c_*,
\]
gives
\[
j(s)\le c_*\left(s-\frac{s^2}{3}\right).
\]
Average this inequality to obtain the first inequality in (7), because
\(\sum_Tw_Ts_T^2=Q_i\).  Jensen gives \(Q_i\ge M_i^2\), and
\(u-u^2/3\) is increasing on \([0,1/2]\), giving the second inequality.
QED.

## 3. Erasure-preserving restriction payment

Combining (1), (2), and Theorem 2.1 yields the new hierarchy
\[
\boxed{
\Delta_iH
\le
B_i+j(M_i)-\frac{c_*}{3}V_i
\le
B_i+j(j_i)
\le
B_i+c_*\left(j_i-\frac{j_i^2}{3}\right).
}
\tag{9}
\]

This is strictly different from applying the known concave cap
\(\Delta_iH\le\Psi(M_i)\): the erasure \(B_i\) is kept **exact**, and only
the recombination term is concavified.  Since \(B_i\le h_2(M_i)\),
(9) is never worse than the corresponding \(\Psi(M_i)\) cap, and it can
be substantially sharper when the exact erasure sits below its Jensen
envelope.

### Corollary 3.1 — refined low-influence erasure selector

Fix a candidate FEI coefficient \(C\ge4\), and let \(\tau(C)\) be the
existing concave-cap threshold satisfying
\[
\Psi(\tau(C))/\tau(C)=C.
\]
Suppose every nonconstant Boolean state whose relevant coordinates all
satisfy \(0<p_i<\tau(C)\) has a relevant coordinate \(i\) with
\[
\boxed{
B_i\le Cp_i-j(p_i).
}
\tag{10}
\]
Then \(H(f)\le CI(f)\) for every Boolean \(f\).

A simpler sufficient condition is
\[
\boxed{
\frac{B_i}{p_i}
\le
C-c_*+\frac{c_*}{3}p_i.
}
\tag{11}
\]

**Proof.**  In the low-influence regime \(p_i<1/2\), so \(j_i=p_i\).
Equation (9) and (10) give \(\Delta_iH\le Cp_i\).  Outside that regime,
the already proved concave restriction cap supplies a coordinate with
the same payment exactly as in the inherited selector compiler.  The
standard physical-restriction induction then gives \(H\le CI\).
Equation (11) implies (10) by the tangent quadratic bound in (7). QED.

Compared with the preceding fixed threshold
\[
B_i/p_i\le C-c_*,
\]
the moving threshold in (11) gives back
\[
\frac{c_*}{3}p_i=\frac{2}{3\ln2}p_i
\]
bits per unit influence.  This correction is asymptotically forced to
vanish as \(p_i\to0\), so it is a refinement rather than a closure of the
general problem.

## 4. Width-two tribes: the old Hod-scale erasure target is false, the new one survives

The previous singleton compiler calibrated the Hod-scale value
\[
C_H=6.4547837,\qquad
C_H-c_*=3.569393618222\ldots,
\]
and proposed the fixed low-influence target
\[
\exists i:\quad B_i/p_i\le3.569393618222\ldots.
\tag{12}
\]

That particular sufficient target is false.

Let \(f_s\) be width-two tribes with \(s\) disjoint tribes:
\(f_s=+1\) when no tribe has both bits equal to one and \(-1\) otherwise.
All \(2s\) coordinates are symmetric, with
\[
p=p_s=\frac12\left(\frac34\right)^{s-1}.
\tag{13}
\]
For a nonempty Fourier label meeting exactly \(m\) tribes, the squared
coefficient is
\[
c_m=\frac{4\,9^{s-m}}{16^s},
\]
whereas the empty squared coefficient is
\[
(1-3p)^2.
\]

Fix one coordinate and classify its erased fibres.

1. If the mate in the same tribe is present, the two squared masses are
   equal.  Their total contribution to \(B_i\) is exactly \(p\).
2. If the mate is absent but at least one other tribe is active, the two
   squared masses are in ratio \(9:1\).  The sum of the larger masses is
   \[
   \frac92p-9p^2.
   \]
3. The empty fibre has squared masses \((1-3p)^2\) and \(p^2\).

Hence, with
\[
F(x,y)=(x+y)h_2\!\left(\frac{y}{x+y}\right),
\qquad
A_B=\frac{10}{9}h_2(1/10),
\]
one gets the exact closed form
\[
\boxed{
B_i=
p+A_B\left(\frac92p-9p^2\right)
+F((1-3p)^2,p^2).
}
\tag{14}
\]

The exact restriction decrement is obtained by replacing \(h_2\) by
\[
\Psi(t)=h_2(t)+j(t):
\]
\[
\boxed{
\Delta_iH=
2p+\frac{10}{9}\Psi(1/10)
\left(\frac92p-9p^2\right)
+((1-3p)^2+p^2)
\Psi\!\left(\frac{p^2}{(1-3p)^2+p^2}\right).
}
\tag{15}
\]

For \(s=8\),
\[
p=\frac{2187}{32768}=0.066741943359375,
\]
which is well below the inherited Hod-scale
\(\tau(C_H)\approx0.1805540\).  Yet
\[
\boxed{
B_i/p=3.606847002096409
>
3.569393618222073.
}
\tag{16}
\]
All coordinates are symmetric, so there is no existential escape:
width-two tribes with \(s=8\) refutes the fixed-threshold target (12).

This is **not** an FEI counterexample.  In fact (15) gives
\[
\boxed{
\Delta_iH/p=6.00374605655909<C_H.
}
\tag{17}
\]
The obstruction is exactly the loss from replacing the true recombination
term by its first-order tangent surcharge.

Indeed,
\[
JS_i/p=2.396899054462681,
\]
far below \(c_*=2.885390081777927\).  The exact new marginal bound gives
\[
j(p)/p=2.817542327818821,
\]
so (10) asks only for
\[
B_i/p\le
C_H-j(p)/p
=
3.637241372181179,
\]
which (16) satisfies with margin
\[
0.030394370084770.
\]
Even the simpler quadratic threshold (11) is
\[
3.633585798691315,
\]
and is satisfied with margin
\[
0.026738796594906.
\]

The stronger fibrewise rebate is larger still.  For this \(s=8\) fibre
law, \(M_i=p\) and
\[
Q_i=0.0196079411133198,
\]
so
\[
B_i/p+
c_*\frac{M_i-Q_i/3}{p}
=
6.209673346766175<C_H.
\]

Thus the same family which kills the old erasure-only Hod target is
comfortably paid after retaining the second-order structure of
recombination.

The attached targeted checker derives (14)--(15), compares them against a
direct Walsh computation for \(s=2,\ldots,8\) (maximum absolute discrepancy
\(4.12\times10^{-13}\)), and evaluates the moving-threshold margins.  The
proofs above do not depend on that finite check.

## 5. New critical-core consequence

Let \(g\) be the inherited maximal-ratio physical-restriction descendant
with
\[
r=H(g)/I(g)
\]
and
\[
\Delta_iH(g)\ge r\,p_i
\]
for every relevant coordinate.  If \(p_i\le1/2\), (9) implies
\[
\boxed{
\frac{B_i(g)}{p_i}
\ge
r-\frac{j(p_i)}{p_i}
\ge
r-c_*+\frac{c_*}{3}p_i.
}
\tag{18}
\]
The fibrewise version is
\[
\boxed{
B_i(g)
\ge
r p_i-j(M_i)+\frac{c_*}{3}V_i.
}
\tag{19}
\]

Therefore a hypothetical Hod-scale critical core must violate the repaired
selector (10) at **every** coordinate, not merely the older constant
threshold.  This is a strictly narrower counterexample geometry.

## 6. What remains

The full FEI conjecture is not closed.  The next erasure/selector target is
now the weaker and more faithful statement:

> On every low-influence Boolean state, find one relevant coordinate with
> \[
> B_i+j(M_i)-\frac{c_*}{3}V_i\le C p_i
> \]
> for some finite universal \(C\), or at the Hod calibration.

A still simpler target is (10).  The key point is that future Booleanity
arguments should not spend the entire sharp tangent \(c_*p_i\) on
recombination before looking at the fibre profile.  Width-two tribes proves
that doing so loses genuine constant-scale room, while Theorem 2.1 shows
that part of that room is universally recoverable.

The compatible current frontiers are:

- use the signed all-shift Boolean convolution identities to force a
  favorable \(M_i,V_i\) / erasure tradeoff on a restriction-critical core;
- combine the pivotal two-face compatibility identities with (19);
- seek a mass-weighted existential selector for the **rebated** charge,
  not an every-prescribed-coordinate payment.

Known counterexamples to every-coordinate payment are untouched.  No
every-coordinate universal selector, no FEI closure, and no publication
priority are claimed.
