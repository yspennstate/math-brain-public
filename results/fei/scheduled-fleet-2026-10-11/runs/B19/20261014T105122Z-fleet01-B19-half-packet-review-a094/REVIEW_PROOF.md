# Independent reconstruction and strengthened constant

All logarithms in the Fourier quantities are in base two.  Let

\[
q(t)=t\log_2(1/t)+\frac{2t}{\ln2},\qquad
\Phi(f)=\sum_iq(\widehat f(\{i\})^2),
\]

\[
L_{c,\eta}(f)=M(f)+(1+\eta)U(f)-cI(f),\qquad M=G-B.
\]

The review target is `B05-A023-HALF-PACKET-INVARIANT-v1` at canonical
commit `38fd5ddccc0e53d26f8cf68165fb3080257fe225`.

## 1. Reconstruction of the half-packet lemma

For a Boolean core of mean `m`, put `a=fhat({i})`, `p=a^2`, and

\[
P(m,a)=R(m)-\frac{R(m-a)+R(m+a)}2-C(m,p).
\]

The Boolean condition gives `|a|<=1-|m|`.  The claim is

\[
P(m,a)\le\frac12q(a^2). \tag{1}
\]

For `a!=0`, set `r=m/a`.  From the exact curvature formula and
`(1+t)sqrt(1-t)<=H_0=4sqrt(6)/9`, the triangular second-difference
identity gives

\[
R(m)-\frac{R(m-a)+R(m+a)}2
\le \frac p2\log_2\frac1p
+p\left[-\frac12+
\frac{F(r)+(\ln H_0)/2-3/8}{\ln2}\right], \tag{2}
\]

where

\[
F(r)=\int_{-1}^1(1-|v|)\ln\frac1{|r+v|}\,dv.
\]

Because the other two entropy terms in `C` are nonnegative,

\[
-C(m,p)\le\frac12T(m^2,p)
=\frac{p}{2\ln2}\tau(r), \tag{3}
\]

\[
\tau(r)=(1+r^2)\ln(1+r^2)-r^2\ln r^2.
\]

It remains to show `F+tau/2<=3/2`.  With `Psi=F+tau/2`, direct
differentiation away from `r=1` gives

\[
\Psi''(r)=\ln\frac{1+r^2}{|1-r^2|}-\frac2{1+r^2}. \tag{4}
\]

The function is even and `Psi(0)=3/2`.  On `(0,1)`,

\[
\Psi'''(r)=\frac{2r}{1+r^2}+\frac{2r}{1-r^2}
+\frac{4r}{(1+r^2)^2}>0.
\]

Moreover `Psi'(0)=0` and exact integration of (4) gives
`Psi'(1-)=-ln2`.  Hence `Psi'<=0` on `(0,1)`.  On `(1,infinity)`,
`Psi''>0`; indeed, after setting `x=1/r^2`,
`ln((1+x)/(1-x))>2x>2x/(1+x)`.  Finally,

\[
F'(r)=-\int_{-1}^1\frac{1-|v|}{r+v}\,dv\sim-\frac1r,
\quad
\frac12\tau'(r)=r\ln(1+r^{-2})\sim\frac1r,
\]

so `Psi'(r)->0`.  Therefore `Psi'` remains negative for `r>1`, proving
`Psi(r)<=3/2` for every real `r`.

Substitution into (2)--(3) yields

\[
P(m,a)\le\frac p2\log_2\frac1p+c_0p,
\quad
c_0=-\frac12+\frac{9/8+(\ln H_0)/2}{\ln2}<\frac1{\ln2},
\]

which is (1).  The cases `a=0`, `r=1`, and cube endpoints follow by
continuity.  Thus rare and vanishing-gap limits are included, not inferred
from the numerical grid.

## 2. Producer contraction

The exact activation recurrence and reviewed root estimate imply, for
`0<eta<=1`,

\[
L_{c,\eta}(Af)\le\frac12L_{c,\eta}(f)+\frac12\Phi(f)
+\left(\frac{21}{2}-c\right)J,\qquad J=\frac{1-m}{2}. \tag{5}
\]

The singleton identity is exact:

\[
\Phi(Af)=q(J^2)+\frac14\Phi(f)+\frac12W_1(f),
\quad W_1=\sum_i\widehat f(\{i\})^2. \tag{6}
\]

Equations (5)--(6) give

\[
L_{c,\eta}(Af)+2\Phi(Af)
\le\frac12\{L_{c,\eta}(f)+2\Phi(f)\}
+W_1+2q(J^2)+\left(\frac{21}{2}-c\right)J. \tag{7}
\]

The producer used `W_1<=4J` and `q(J^2)<=2J/ln2`, obtaining
`c=29/2+4/ln2`.  This is correct.

## 3. Reviewer strengthening

Keep the common parameter `J` in both terms.  Since `m=1-2J`,

\[
W_1\le1-m^2=4J(1-J),
\]

and exactly

\[
2q(J^2)=4J^2\log_2(1/J)+\frac{4J^2}{\ln2}.
\]

Thus the last line of (7), divided by `J>0`, is bounded by

\[
h(J)+\frac{21}{2}-c,
\quad
h(J)=4(1-J)+4J\log_2(1/J)+\frac{4J}{\ln2}. \tag{8}
\]

Now

\[
h'(J)=4(\log_2(1/J)-1),
\]

so the unique maximum is at `J=1/2`, with

\[
\max_{0\le J\le1}h(J)=4+\frac2{\ln2}. \tag{9}
\]

Consequently the stronger constant

\[
\boxed{c_\dagger=\frac{29}{2}+\frac2{\ln2}}
\tag{10}
\]

already suffices for

\[
\boxed{L_{c_\dagger,\eta}(Af)+2\Phi(Af)
\le\frac12\{L_{c_\dagger,\eta}(f)+2\Phi(f)\}.} \tag{11}
\]

At `J=0` the extra term in (7) is zero by continuity.  This strengthening
is reviewer-contributed and therefore requires a fresh independent review.

## 4. Products, restrictions, and endpoint

For disjoint products, `U`, `G`, `B`, `M`, and `I` are additive.  A
singleton coefficient of one factor is multiplied by the other factor's
mean.  Since `q` is increasing on `[0,1]`,

\[
\Phi(fg)\le\Phi(f)+\Phi(g). \tag{12}
\]

Hence `L+2Phi<=0` is preserved by disjoint products.  Structural
restriction closure is also valid: restricting a selector returns a
constant or its core, and restricting a data coordinate acts recursively
inside one disjoint factor.  Signed characters and constants satisfy the
base inequality because `c_dagger>4/ln2`.

Taking `eta=1`, the reviewed signed-mismatch reduction therefore gives on
the same fresh/disjoint restriction-closed class

\[
\boxed{G(F)\le\left(\frac{33}{2}+\frac2{\ln2}\right)I(F)
<19.385391I(F),} \tag{13}
\]

and then

\[
\boxed{H(F)\le\left(35+\frac4{\ln2}\right)I(F)
<40.770781I(F).} \tag{14}
\]

No leaf FEI assumption is used.  However, fresh selectors and disjoint
private product blocks remain indispensable.  The result does not cover
shared or reused physical coordinates, so it is not universal GU or full
FEI.

## 5. Verdict

`B05-A023-HALF-PACKET-INVARIANT-v1` is accepted without mathematical
repair at its stated scope.  The word “sharp” should mean “the sufficient
half-packet coefficient,” not proven optimality.  The reviewer strengthening
`B19-A094-HALF-PACKET-CONSTANT-v1` lowers the class constants but requires
fresh A085/A090 review because B19 is its contributor.

