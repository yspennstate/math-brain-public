# Complete signed correction for one fair activation

All logarithms are in bits.  For a Boolean sign `f`, put

\[
 p(S)=\widehat f(S)^2,\qquad
 U(f)=\sum_Sp(S)\log_2\frac{\pi(S)}{p(S)},
\]

and let `G`, `B`, and `M=G-B` be as in the reviewed signed-mismatch
reduction.  Define

\[
 q(t)=t\log_2(1/t)+\frac{2t}{\ln2},\qquad
 \Phi(f)=\sum_iq\bigl(\widehat f(\{i\})^2\bigr).
\]

For a Boolean core `f` with mean `m`, its fresh fair activation is

\[
 A(f)(z,x)=\begin{cases}1,&z=+1,\\f(x),&z=-1.\end{cases}
\]

The selector influence is

\[
 J(m)=\frac{1-m}{2}.
\]

## The theorem

For every finite-dimensional Boolean `f` and every `0<eta<=1`,

\[
\boxed{
 M(Af)+(1+\eta)U(Af)
 \le \frac12\{M(f)+(1+\eta)U(f)\}
       +\Phi(f)+\frac{21}{2}J(m).}
\tag{1}
\]

Equivalently, for

\[
 L_{c,\eta}(f)=M(f)+(1+\eta)U(f)-cI(f),
\]

\[
\boxed{
 L_{c,\eta}(Af)
 \le\frac12L_{c,\eta}(f)+\Phi(f)
       +\left(\frac{21}{2}-c\right)J(m).}
\tag{2}
\]

This is uniform in dimension, bias, and the core.  It keeps the
singleton-logarithmic packet `Phi` intact rather than charging it
pointwise to influence.

## 1. Exact correction

Use the source-reviewed scalar functions

\[
 T(A,p)=(A+p)\log_2(A+p)-A\log_2A-p\log_2p,
\]

\[
 C(m,p)=-\frac12T(m^2,p)
 +\frac14T((1+m)^2,p)+\frac14T((1-m)^2,p),
\]

and the activation remainder `R` characterized by

\[
 U(Af)=\frac12U(f)+R(m).
\]

Writing `a_i=fhat({i})`, the exact reviewed recurrence is

\[
 M(Af)=\frac12M(f)+\sum_i P(m,a_i)+R(m)-B_z(m),
\tag{3}
\]

where

\[
 P(m,a)=R(m)-\frac{R(m-a)+R(m+a)}2-C(m,a^2)
\tag{4}
\]

and

\[
 B_z(m)=\frac{1-m^2}{2}
 +\frac14T((1+m)^2,(1-m)^2)\ge0.
\tag{5}
\]

Thus the whole new correction in (1) is

\[
 \sum_iP(m,a_i)+(2+\eta)R(m)-B_z(m).
\tag{6}
\]

No positive part, selector term, or terminal term has been dropped.

## 2. The signed scalar cancellation

We prove

\[
\boxed{P(m,a)\le q(a^2)}
\quad\text{whenever }-1\le m\le1,
\quad |a|\le1-|m|.
\tag{7}
\]

Put `p=a^2` and

\[
 D_R(m,a)=R(m)-\frac{R(m-a)+R(m+a)}2.
\]

The two signed pieces each consume only half of `q(p)`.

First, on `(-1,1)\{0}` the previously derived exact curvature is

\[
 R''(t)=1+\frac{
 \ln\!\left(\dfrac{t^2}{(1+t)\sqrt{1-t}}\right)+3/4}{\ln2}.
\tag{8}
\]

The factor `(1+t)sqrt(1-t)` is at most

\[
 H_0=\frac{4\sqrt6}{9}<\frac{11}{10}.
\]

The integral form of the symmetric second difference gives

\[
 D_R(m,a)=-\frac12\int_{-a}^a(a-|u|)R''(m+u)\,du.
\tag{9}
\]

The symmetric decreasing rearrangement of `ln(1/|x|)` against the
triangular kernel yields

\[
 \int_{-a}^a(a-|u|)\ln\frac1{|m+u|}\,du
 \le a^2\left(\ln\frac1{|a|}+\frac32\right).
\tag{10}
\]

Substituting the lower bound from (8) into (9) gives

\[
 D_R(m,a)
 \le \frac p2\log_2\frac1p+c_Dp,
\qquad
 c_D=-\frac12+\frac{9/8+(\ln H_0)/2}{\ln2}.
\tag{11}
\]

Since `H_0<11/10`, `ln(11/10)<1/10`, and `ln2>2/3`, one has
`c_D<1/ln2`.  Hence

\[
 D_R(m,a)\le\frac12q(p).
\tag{12}
\]

The integrable singularities at zero and the endpoints follow by
monotone limiting; (9)--(12) remain valid there.

Second, `T(A,p)>=0`, so the two positive terms in `C` imply

\[
 -C(m,p)\le\frac12T(m^2,p).
\tag{13}
\]

For `0<=A,p<=1`,

\[
\begin{aligned}
 T(A,p)
 &=A\log_2(1+p/A)+p\log_2(1+A/p)\\
 &\le \frac p{\ln2}
 +p\log_2\frac1p+\frac p{\ln2}
 =q(p).
\end{aligned}
\tag{14}
\]

Here `ln(1+x)<=x`, `A<=1`, and `ln(1+p)<=p<=1` were used; zero
endpoints are by continuity.  Equations (13)--(14) give

\[
 -C(m,p)\le\frac12q(p).
\tag{15}
\]

Adding (12) and (15) proves (7).  This is the key cancellation: neither
the midpoint term nor the entropy correction is discarded.

## 3. Root payment

The reviewed bounds are

\[
 R(m)\le\frac43(1-m)\quad(0\le m\le1),
 \qquad R(m)<\frac74\quad(-1\le m\le1).
\tag{16}
\]

Because `B_z>=0` and `2+eta<=3`, if `m>=0` then

\[
 (2+\eta)R(m)-B_z(m)\le8J(m).
\]

If `m<0`, the same expression is at most `21/4`, while `J(m)>1/2`.
Therefore, throughout the full interval,

\[
\boxed{(2+\eta)R(m)-B_z(m)\le\frac{21}{2}J(m).}
\tag{17}
\]

Summing (7) over the physical coordinates and combining (6) with (17)
proves (1).  Finally,

\[
 I(Af)=\frac12I(f)+J(m)
\]

converts (1) into (2).

## 4. Exact implication and remaining leaf

The earlier signed-mismatch reduction says that a universal
`L_{c,eta}<=0` implies

\[
 G\le(c+2)I+(1-\eta)U
\]

and hence

\[
 H\le\left(2+\frac{2(c+2)}\eta\right)I.
\]

Equation (2) proves that one fair activation creates no unpaid object
except the single packet `Phi(f)` and the explicit selector reserve.  In
particular, for `c>=21/2`, the selector term is nonpositive.  The strictly
smaller remaining assembly inequality is therefore:

> **ACTIVATION-PACKET-OWNERSHIP.**  In a complete changing-core activation
> assembly, charge every weighted occurrence of `Phi(core)` once to the
> signed physical-orbit reveal ledger, without discarding its opening
> refunds or terminal reserve.

The accepted B05 signed-orbit theorem supplies an exact telescope for a
single physical restriction tree, including changing blocks and coordinate
re-entry.  What is not yet proved is that all activation-core packets can
be embedded in one such tree without duplicating a packet at different
activation ancestors.  This is narrower than bounding the original
`sum_i(B_i-Gamma_i+K_i)` directly: the full activation correction has now
been reduced to a named, nonnegative singleton packet plus an already paid
selector term.

This theorem does not prove a universal pair `(a,b)`, universal GU, or
FEI.

