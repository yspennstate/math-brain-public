# Independent proof audit

All logarithms are in bits.  Put

\[
L_{c,\eta}(f)=M(f)+(1+\eta)U(f)-cI(f),\qquad M=G-B.
\]

The audited claim is that, for every genuine Boolean sign \(q\), fresh
uniform signs \(y,z\), \(0<\eta\le1\), and
\(c\ge 3/2+\eta\),

\[
\mathcal T(q)(z,y,x)=
\begin{cases}
1,&z=+1,\\
yq(x),&z=-1
\end{cases}
\quad\Longrightarrow\quad
L_{c,\eta}(\mathcal T(q))\le\frac12L_{c,\eta}(q).
\]

## 1. Independent reconstruction of the balancing step

For \(r(y,x)=yq(x)\),

\[
\widehat r(S\cup\{y\})=\widehat q(S),\qquad
\widehat r(T)=0\quad(y\notin T).
\]

Thus the spectral law is merely relabelled.  Consequently

\[
U(r)=U(q),\quad G(r)=G(q),\quad B(r)=B(q),\quad
M(r)=M(q),\quad I(r)=I(q)+1
\]

and hence

\[
L_{c,\eta}(r)=L_{c,\eta}(q)-c. \tag{1}
\]

The core \(r\) is balanced.  Its only possible singleton coefficient is
\(\widehat r(\{y\})=m:=\mathbb E q\).  This is the exact reason that all
old-coordinate singleton charges disappear; no sign projection is used.

## 2. Substitution in the accepted activation identity

The independently reconstructed fair-activation identity is

\[
L_{c,\eta}(A(r))
=\frac12L_{c,\eta}(r)+D_R(r)+(2+\eta)R(0)-B_z(0)
-\sum_iC_i(0,p_i)-\frac c2. \tag{2}
\]

For the balanced \(r\), \(R(0)=B_z(0)=1\), while the singleton
calculation above gives

\[
D_R(r)=R(0)-\frac{R(m)+R(-m)}2,qquad
\sum_iC_i(0,p_i)=\frac12T(1,m^2).
\]

Defining

\[
d(m)=R(0)-\frac{R(m)+R(-m)}2-\frac12T(1,m^2),
\]

and substituting (1) in (2) yields exactly

\[
L_{c,\eta}(\mathcal T(q))-\frac12L_{c,\eta}(q)
=d(m)+1+\eta-c. \tag{3}
\]

The influence of the fresh balancing character contributes \(-c/2\)
through the inherited child residual in (1); the selector contributes the
other \(-c/2\) in (2).  These are two different physical inputs, so the
total \(-c\) is not double spending.

## 3. Scalar inequality

Direct substitution of the exact \(R\) gives, with natural logarithms,

\[
d(h)=-\frac{h^2}{2}+\frac{3}{8\ln2}A(h)
-\frac{1+h^2}{2\ln2}\ln(1+h^2),
\]

where

\[
A(h)=(1+h)^2\ln(1+h)+(1-h)^2\ln(1-h).
\]

The desired \(d(h)\le h^2/2\) is equivalent to \(F(h)\ge0\), with

\[
F(h)=h^2\ln2-\frac38A(h)+\frac12(1+h^2)\ln(1+h^2).
\]

For \(0\le h\le1\), let

\[
D(h)=(1+h)\ln(1+h)-(1-h)\ln(1-h).
\]

Since \(D(0)=0\) and \(D'(h)=2+\ln(1-h^2)\le2\), one has
\(D(h)\le2h\).  Differentiation gives

\[
F'(h)=h\left(2\ln2+\ln(1+h^2)+\frac14\right)-\frac34D(h)
\ge h\left(2\ln2+\ln(1+h^2)-\frac54\right)>0.
\]

As \(F(0)=0\), the scalar bound follows.  Equation (3) then gives

\[
L_{c,\eta}(\mathcal T(q))-\frac12L_{c,\eta}(q)
\le\frac12+1+\eta-c\le0.
\]

Endpoints use the continuous convention \(0\ln0=0\).

## 4. Closure and GU constants

The spectral laws, caps, restrictions, and hence \(U,G,B,M,I\) tensorize
on disjoint products; therefore \(L\) is additive.  Output sign changes
leave the spectral laws unchanged.  Starting from any base class with
\(L\le0\), disjoint products, output signs, and repeated fresh
applications of \(\mathcal T\) preserve \(L\le0\).

At \(\eta=1/4,c=7/4\),

\[
M+\frac54U\le\frac74I.
\]

Using \(G=M+B\), \(B\le H\), and the source-proved
\(H\le2(I-\operatorname{Var})+2U\),

\[
G\le\frac{15}{4}I+\frac34U-2\operatorname{Var}
\le\frac{15}{4}I+\frac34U.
\]

This is a GU pair only on the generated proper class.

## 5. Adversarial restriction and overlap checks

The physical restrictions are

\[
\mathcal T(q)|_{z=+1}=1,qquad
\mathcal T(q)|_{z=-1}=yq,
\]
\[
\mathcal T(q)|_{y=+1}=A(q),qquad
\mathcal T(q)|_{y=-1}=A(-q),
\]

and restriction of an old coordinate commutes with \(\mathcal T\).
The two middle descendants are precisely the unbalanced activations not
covered by the theorem.  Hence the generated class is not
restriction-closed, and the universal GU-to-\(U\) induction cannot be
applied.  No biased selector, shared coordinate, overlap, or physical
first-owner claim follows.

The theorem inherits only \(L(q)/2\).  Therefore “changing core” means a
different already-admissible child at each node; an unrelated leaf whose
\(L\)-residual has not been paid cannot be inserted circularly.

## Verdict

The claim is **accepted at its declared proper-class scope without
mathematical repair**.  It is not A023 closure, a universal GU pair, or a
proof of FEI.
