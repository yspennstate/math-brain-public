# Half-packet activation and a nonreusing signed-mismatch invariant

All logarithms are in bits.  Put

\[
q(t)=t\log_2(1/t)+\frac{2t}{\ln2},\qquad
\Phi(f)=\sum_iq\bigl(\widehat f(\{i\})^2\bigr),
\]

and

\[
L_{c,\eta}(f)=M(f)+(1+\eta)U(f)-cI(f),\qquad M=G-B.
\]

For the fresh fair activation

\[
A(f)(z,x)=\begin{cases}1,&z=+1,\\ f(x),&z=-1,\end{cases}
\]

write `m=E f` and `J(m)=(1-m)/2`.

## 1. Sharpened scalar packet

The exact signed activation recurrence is

\[
L_{c,\eta}(Af)=\frac12L_{c,\eta}(f)
+\sum_iP(m,a_i)+(2+\eta)R(m)-B_z(m)-cJ(m),
\tag{1}
\]

where `a_i=fhat({i})`, `B_z>=0`, and

\[
P(m,a)=R(m)-\frac{R(m-a)+R(m+a)}2-C(m,a^2).
\tag{2}
\]

The preceding B01 bound was `P(m,a)<=q(a^2)`.  We prove the sharp packet
coefficient needed by the physical half-branch:

\[
\boxed{P(m,a)\le\frac12q(a^2)}
\qquad(|a|\le1-|m|).                         \tag{3}
\]

Let `p=a^2`; the case `a=0` is immediate.  Put `r=m/a` and

\[
F(r)=\int_{-1}^1(1-|v|)\ln\frac1{|r+v|}\,dv,
\]

\[
\tau(r)=(1+r^2)\ln(1+r^2)-r^2\ln(r^2),
\]

with continuous endpoint conventions.  The curvature identity

\[
R''(t)=1+\frac{
\ln\!\left(\dfrac{t^2}{(1+t)\sqrt{1-t}}\right)+3/4}{\ln2}
\]

and `(1+t)sqrt(1-t)<=H_0=4sqrt(6)/9` give, by the integral form of the
symmetric second difference,

\[
R(m)-\frac{R(m-a)+R(m+a)}2
\le \frac p2\log_2\frac1p
+p\left[-\frac12+
\frac{F(r)+(\ln H_0)/2-3/8}{\ln2}\right].       \tag{4}
\]

The entropy function

\[
T(A,p)=(A+p)\log_2(A+p)-A\log_2A-p\log_2p
\]

is nonnegative, and the definition of `C` gives

\[
-C(m,p)\le\frac12T(m^2,p)=\frac{p}{2\ln2}\tau(r). \tag{5}
\]

The two estimates are coupled through the following elementary lemma:

\[
\boxed{F(r)+\frac12\tau(r)\le\frac32\quad(r\in\mathbb R).} \tag{6}
\]

To prove it, let `Psi=F+tau/2`.  It is even and `Psi(0)=3/2`.  For
`r>0`, distributional differentiation of the triangular kernel gives

\[
F''(r)=\ln\frac{r^2}{|r^2-1|},
\]

and therefore

\[
\Psi''(r)=\ln\frac{1+r^2}{|1-r^2|}-\frac2{1+r^2}. \tag{7}
\]

On `(0,1)`, `Psi'''(r)>0`, so `Psi''` has one zero and `Psi'` first
decreases and then increases.  Its endpoint values are
`Psi'(0)=0` and `Psi'(1-)=-ln2`; hence `Psi'<=0`.  On `(1,infinity)`,

\[
\ln\frac{1+r^2}{r^2-1}>\frac{2}{1+r^2},
\]

so `Psi'` increases from `-ln2` to `0` and remains negative.  This proves
(6).

Combining (4)--(6),

\[
P(m,a)\le \frac p2\log_2\frac1p+c_0p,
\qquad
c_0=-\frac12+\frac{9/8+(\ln H_0)/2}{\ln2}.
\]

As `H_0<11/10`, `ln(11/10)<1/10`, and `ln2>2/3`, one has
`c_0<1/ln2`.  Equation (3) follows.

## 2. Exact augmented-potential contraction

For `0<eta<=1`, the reviewed root estimate is

\[
(2+\eta)R(m)-B_z(m)\le\frac{21}{2}J(m).            \tag{8}
\]

Equations (1), (3), and (8) imply

\[
L_{c,\eta}(Af)
\le\frac12L_{c,\eta}(f)+\frac12\Phi(f)
+\left(\frac{21}{2}-c\right)J(m).                  \tag{9}
\]

The activated singleton potential is exact.  If
`W_1(f)=sum_i fhat({i})^2`, then

\[
\Phi(Af)=q(J(m)^2)+\frac14\Phi(f)+\frac12W_1(f),  \tag{10}
\]

because `q(p/4)=q(p)/4+p/2`.  Hence

\[
\begin{aligned}
L_{c,\eta}(Af)+2\Phi(Af)
\le{}&\frac12\{L_{c,\eta}(f)+2\Phi(f)\}\\
&+W_1(f)+2q(J(m)^2)
+\left(\frac{21}{2}-c\right)J(m).                 \tag{11}
\end{aligned}
\]

Parseval and the scalar bound for `q` give

\[
W_1(f)\le1-m^2\le4J(m),
\qquad q(J(m)^2)\le\frac{2J(m)}{\ln2}.             \tag{12}
\]

Therefore, with

\[
\boxed{c_*=\frac{29}{2}+\frac4{\ln2}},             \tag{13}
\]

every Boolean core satisfies the contraction

\[
\boxed{
L_{c_*,\eta}(Af)+2\Phi(Af)
\le\frac12\{L_{c_*,\eta}(f)+2\Phi(f)\}.}          \tag{14}
\]

The coefficient `1/2` in (3) is exactly the probability of entering the
core branch.  Thus (14) stores the packet once in the child potential and
does not recharge it at later activation ancestors.

## 3. Restriction-closed generated class

Let `C` be any restriction-closed Boolean base class satisfying

\[
L_{c_*,\eta}(f)+2\Phi(f)\le0                       \tag{15}
\]

for every `f` in `C`.  Close `C` under:

1. fresh fair activations;
2. products on disjoint physical variable blocks; and
3. physical restrictions.

Equation (14) preserves (15) under activation.  For disjoint products,
`L` is exactly additive and

\[
\Phi(fg)\le\Phi(f)+\Phi(g),                         \tag{16}
\]

because each singleton coefficient acquires the other factor's mean, of
absolute value at most one, and `q` is increasing.  Thus (15) is also
preserved under products.  Restrictions remain inside the generated class
by structural induction: a selector restriction returns either a constant
or its core, while a data restriction acts recursively on one factor.

Consequently the whole generated class satisfies

\[
L_{c_*,\eta}(F)\le-2\Phi(F)\le0.                   \tag{17}
\]

Taking signed characters and constants as the base is valid because
`c_*>4/ln2`.  Choosing `eta=1`, (17) and the reviewed signed-mismatch
reduction give

\[
\boxed{G(F)\le\left(\frac{33}{2}+\frac4{\ln2}\right)I(F)}
\tag{18}
\]

and

\[
\boxed{H(F)\le\left(35+\frac8{\ln2}\right)I(F).}  \tag{19}
\]

Numerically these constants are `22.270780163...` and
`46.541560327...`.

This improves the previous `G/I<42.6127` bound on the fresh fair
activation/disjoint-product closure and permits arbitrary finite branched
construction trees.  It still requires fresh selectors and disjoint
private product blocks.  Shared/reused physical coordinates are not
covered; the next unpaid step is to replace (10) by an orbit version under
one reused coordinate while retaining the terminal `Theta` reserve.

Universal GU and full FEI remain open.

