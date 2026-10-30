# Fourfold tensor suspension strengthens the SMR lower bound

All logarithms are in bits.  Put

\[
L_{c,\eta}(f)=M(f)+(1+\eta)U(f)-cI(f),\qquad M=G-B.
\]

The source-checked reduction says that a universal estimate
\(L_{c,\eta}\le0\), with \(0<\eta\le1\), would imply

\[
G\le(c+2)I+(1-\eta)U-2\operatorname{Var}
\]

and therefore GU with \((a,b)=(c+2,1-\eta)\).  The present theorem is a
necessary lower bound on this sufficient route, not a proof or disproof of
universal GU.

## 1. Exact tensor identities

For Boolean signs on disjoint physical blocks, their spectral laws and
upper caps factor.  Hence

\[
U(fg)=U(f)+U(g),\quad I(fg)=I(f)+I(g).
\]

Restriction of a coordinate in one factor leaves the other factor intact,
so \(G\) is additive.  The coordinate-pair entropy defining \(B\) is also
additive.  Therefore \(M=G-B\) and \(L_{c,\eta}\) are additive.  In
particular, tensoring alone never amplifies the normalized threshold

\[
c_f(\eta)=\frac{M(f)+(1+\eta)U(f)}{I(f)}.
\tag{1}
\]

This disposes of the first proposed amplification mechanism exactly.

## 2. One suspension after tensoring

For a Boolean core \(h\), mean \(m\), singleton masses
\(p_i=\widehat h(\{i\})^2\), and fresh fair activation \(A(h)\), the
independently reconstructed recurrence is

\[
L_{c,\eta}(A(h))=\frac12L_{c,\eta}(h)+D_R(h)
+(2+\eta)R(m)-B_z(m)-\sum_iC_i(m,p_i)-cJ(m).
\tag{2}
\]

No terminal, selector, singleton-orbit, or pivotal term is omitted.

Let \(q\) be the four-bit sign with LSB-first +1 mask 56242 and let
\(F=A(q)\).  This is the independently reconstructed B05 activation
witness.  It has

\[
\mathbb EF=\frac58,\qquad I(F)=\frac{11}{8}.
\]

Set \(Q=F^{\otimes4}\) and \(W=A(Q)\).  Tensorization and (2) reduce all
statistics of the 21-variable Boolean sign \(W\) to the five-variable
truth table of \(F\).  Its exact influence is

\[
I(W)=\frac{25999}{8192}.
\]

Writing

\[
c_W(\eta)=\frac{M(W)+(1+\eta)U(W)}{I(W)}
=\alpha_4+\beta_4\eta,
\]

the certified values are

\[
\alpha_4=1.770873264041823\ldots,qquad
\beta_4=1.451867015896827\ldots.
\tag{3}
\]

For the seed \(F\), subtracting its affine threshold gives

\[
c_W(\eta)-c_F(\eta)=D_0+D_1\eta,
\]

where exact rational-log intervals certify

\[
D_0\in[0.037915828805916769,0.037915828805916769],
\]

\[
D_1\in[0.11506096192931070,0.11506096192931070].
\]

Thus \(c_W(\eta)>c_F(\eta)\) for every \(\eta\ge0\).  At the principal
value \(\eta=1/4\),

\[
\boxed{c_W(1/4)=2.133840018016030\ldots>2.1338.}
\tag{4}
\]

Consequently every universal \(\operatorname{SMR}(c,1/4)\) theorem must
have \(c>2.1338\).  More generally, it must have
\(c\ge\alpha_4+\beta_4\eta\).

## 3. Exact certification

`CHECK_EXACT_T4.py` represents each entropy as a rational linear
combination of logarithms of positive integers.  It encloses every
logarithm using the exact atanh series

\[
\log y=2\sum_{j=0}^{N-1}\frac{z^{2j+1}}{2j+1}+E_N,
\quad z=\frac{y-1}{y+1},
\]

with the rational remainder bound

\[
0\le E_N\le
\frac{2z^{2N+1}}{(2N+1)(1-z^2)}.
\]

The script uses \(N=120\); every reported sign interval has a strictly
positive rational lower endpoint.  `CHECK_TENSOR_SUSPENSION.py`
independently reconstructs the base truth table, verifies all five tensor
additivities directly on \(F^{\otimes2}\), and checks the activation
recurrence against the direct 11-variable truth table.

## 4. What does not amplify

For general \(t\), put \(W_t=A(F^{\otimes t})\).  Since
\(|\mathbb EF|=5/8<1\), every restriction mean and singleton mass entering
the nonterminal terms of (2) decays exponentially after tensoring.  Hence

\[
c_{W_t}(\eta)=c_F(\eta)+
\frac{2+2\eta-c_F(\eta)}{tI(F)}+o(t^{-1}).
\tag{5}
\]

The coefficient is positive here, but the excess tends to zero.  Therefore
tensor-plus-one-suspension produces a genuine finite strengthening (4), not
an unbounded lower bound.  It neither disproves SMR for some larger finite
\(c\) nor refutes GU or FEI.

