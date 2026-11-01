# Balanced-preconditioned fair activation: exact signed-refund transfer

All logarithms are base two.  Let

\[
L_{c,\eta}(f)=M(f)+(1+\eta)U(f)-cI(f),
\qquad M(f)=G(f)-B(f)=\sum_i(K_i-\Gamma_i).
\]

The result below keeps the complete signed mismatch.  It does not replace
`M` by an unsigned KL or singleton surrogate.

## 1. Scalar cancellation lemma

For nonnegative `a,b`, put

\[
T(a,b)=a\log_2\frac{a+b}{a}+b\log_2\frac{a+b}{b},
\]

with zero terms omitted.  Let `R` be the exact fair-activation scalar from

\[
U(A(q))=\frac12U(q)+R(\mathbb E q).
\]

For `|h|<=1`, define

\[
d(h)=R(0)-\frac{R(h)+R(-h)}2-\frac12T(1,h^2). \tag{1}
\]

Then

\[
\boxed{d(h)\le\frac{h^2}{2}.} \tag{2}
\]

It suffices to take `0<=h<=1`, since `d` is even.  Direct substitution of
the formula for `R` gives, with natural logarithms,

\[
d(h)=-\frac{h^2}{2}
+\frac{3}{8\ln2}A(h)
-\frac{1+h^2}{2\ln2}\ln(1+h^2), \tag{3}
\]

where

\[
A(h)=(1+h)^2\ln(1+h)+(1-h)^2\ln(1-h).
\]

Thus (2) is equivalent to `F(h)>=0`, where

\[
F(h)=h^2\ln2-\frac38A(h)
+\frac12(1+h^2)\ln(1+h^2). \tag{4}
\]

Write

\[
D(h)=(1+h)\ln(1+h)-(1-h)\ln(1-h).
\]

Since `D(0)=0` and

\[
D'(h)=2+\ln(1-h^2)\le2,
\]

we have `D(h)<=2h`.  Differentiating (4),

\[
F'(h)=h\left(2\ln2+\ln(1+h^2)+\frac14\right)
-\frac34D(h).
\]

Therefore

\[
F'(h)\ge h\left(2\ln2+\ln(1+h^2)-\frac54\right)>0
\quad(0<h\le1),
\]

using `2 ln 2>5/4`.  Since `F(0)=0`, (2) follows.  Endpoint values use the
continuous convention `0 ln 0=0`.

## 2. Exact balancing identities

For a fresh sign `y`, set

\[
r(y,x)=yq(x).
\]

Fourier support is relabelled by `S -> S union {y}`.  Hence

\[
U(r)=U(q),\quad G(r)=G(q),\quad B(r)=B(q),\quad
M(r)=M(q),\quad I(r)=I(q)+1. \tag{5}
\]

In particular,

\[
L_{c,\eta}(r)=L_{c,\eta}(q)-c. \tag{6}
\]

The core `r` is balanced.  Its only possibly nonzero singleton coefficient
is

\[
\widehat r(\{y\})=\mathbb E q=:m; \tag{7}
\]

all old-coordinate singleton coefficients vanish.

## 3. The transfer theorem

Let `z` be another fresh sign and define

\[
\mathcal T(q)(z,y,x)=A(r)(z,y,x)
=\begin{cases}1,&z=+1,\\yq(x),&z=-1.\end{cases} \tag{8}
\]

The exact activation recurrence is

\[
L_{c,\eta}(A(r))=\frac12L_{c,\eta}(r)
+D_R(r)+(2+\eta)R(0)-B_z(0)
-\sum_iC_i(0,p_i)-\frac c2. \tag{9}
\]

Here `R(0)=1`, `B_z(0)=1`, and (7) gives

\[
D_R(r)=R(0)-\frac{R(m)+R(-m)}2,
\qquad
\sum_iC_i(0,p_i)=\frac12T(1,m^2). \tag{10}
\]

Combining (1), (6), and (9)--(10) yields the exact identity

\[
\boxed{
L_{c,\eta}(\mathcal T(q))-rac12L_{c,\eta}(q)
=d(m)+1+\eta-c.
} \tag{11}
\]

By (2) and `m^2<=1`, for every genuine Boolean `q`,

\[
\boxed{
c\ge\frac32+\eta
\quad\Longrightarrow\quad
L_{c,\eta}(\mathcal T(q))\le\frac12L_{c,\eta}(q).
} \tag{12}
\]

This is uniform in the dimension, bias, Fourier support, and internal
structure of the changing core `q`.  Every selector and balancing character
is fresh; no shared-variable or biased-selector claim is made.

## 4. A concrete growing GU class

For fixed `eta` and `c` as in (12), let `C` be any family satisfying
`L_{c,eta}(q)<=0`.  Close it under output sign, disjoint Boolean products,
and the operation `T` in (8), always using fresh inputs.  The residual is
sign-invariant and additive under disjoint products, while (12) handles
every `T` node.  Thus every function in the generated class satisfies

\[
M+(1+\eta)U\le cI. \tag{13}
\]

Taking constants and characters as the base, `eta=1/4`, and `c=7/4`
produces an unbounded-depth, changing-core class with

\[
M+\frac54U\le\frac74I. \tag{14}
\]

Using `G=B+M`, `B<=H`, and
`H<=2(I-Var)+2U`, equation (14) gives the pointwise GU bound

\[
\boxed{G\le\frac{15}{4}I+\frac34U-2\operatorname{Var}
\le\frac{15}{4}I+\frac34U.} \tag{15}
\]

This is a proper-class GU theorem.  The generated endpoint class is not
restriction-closed: restricting the balancing input `y` in (8) produces
`A(q)` or `A(-q)`, precisely the unbalanced activation not covered by (12).
Therefore the universal GU-to-`U` induction cannot be applied to this class,
and no class FEI constant is claimed from (15).

## 5. Relation to the certified falsifier

The independently certified five-bit witness refutes
`L_{2,1/4}(A(q))<=0` for an unbalanced core of mean `1/4`.  It does not
contradict (12), which first replaces `q` by the balanced core `yq` and then
uses two fresh inputs.  Conversely, (12) does not repair arbitrary
unbalanced activation, physical-variable reuse, or overlap.

