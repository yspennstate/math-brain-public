# Iterated tensor-suspension has a finite affine threshold limit

All logarithms are in bits.  Put

\[
L_{c,\eta}(f)=M(f)+(1+\eta)U(f)-cI(f),\qquad M=G-B,
\]

and define the normalized signed-mismatch threshold

\[
c_f(\eta)=\frac{M(f)+(1+\eta)U(f)}{I(f)}.
\]

The source-reviewed reduction says that a universal estimate
\(L_{c,\eta}\le0\), with \(0<\eta\le1\), implies

\[
G(f)\le(c+2)I(f)+(1-\eta)U(f)-2\operatorname{Var}(f),
\]

and hence GU with \((a,b)=(c+2,1-\eta)\).  The theorem below is a
necessary lower bound and a no-unbounded-amplification statement for this
sufficient route.  It does not prove or refute universal GU.

## 1. The tower and exact compressed recurrence

Let \(F_0=A(q)\), where \(q\) is the four-bit mask-56242 witness, and set

\[
F_{k+1}=A(F_k^{\otimes4}). \tag{1}
\]

For a Boolean \(f\), write \(m=\mathbb Ef\),
\(a_i=\widehat f(\{i\})\), and
\(m_{i,\pm}=\mathbb E[f\mid x_i=\pm1]=m\pm a_i\), after orienting the
sign convention.  The fourfold tensor core has mean \(\mu=m^4\), singleton
coefficient \(a_im^3\) on each of four copies of coordinate \(i\), and
restriction means \(m_{i,\pm}m^3\).

Substitution into the reviewed activation identity gives the exact
recurrences

\[
I_{k+1}=2I_k+J(m_k^4),\qquad J(s)=\frac{1-s}{2}, \tag{2}
\]

\[
U_{k+1}=2U_k+R(m_k^4), \tag{3}
\]

\[
M_{k+1}=2M_k+\Theta_k, \tag{4}
\]

where

\[
\begin{aligned}
\Theta_k={}&4\sum_i\left[R(m_k^4)-\frac12R(m_{i,-}m_k^3)
-\frac12R(m_{i,+}m_k^3)\right]\\
&+R(m_k^4)-B_z(m_k^4)
-4\sum_i C(m_k^4,a_i^2m_k^6). \tag{5}
\end{aligned}
\]

No selector, singleton, restriction-mean, or terminal term is omitted.
The mean evolves by

\[
m_{k+1}=\frac{1+m_k^4}{2},\qquad m_0=\frac58. \tag{6}
\]

`CHECK_ITERATED.py` implements (2)--(6) using coordinate types with exact
multiplicities.  The first iterate agrees with the independently checked
21-variable threshold from the preceding run.

## 2. Finite-limit theorem

Let \(\rho\in(0,1)\) be the smaller solution of

\[
2\rho=1+\rho^4.
\]

Equation (6) shows that \(m_k\downarrow\rho\), with
\(\rho=0.543689012692\ldots\).  In particular all means stay in the fixed
compact interval \([\rho,5/8]\).

It remains to control (5).  Under one tower step, every old singleton mass
is multiplied by \(m_k^6/4\) and appears in four tensor copies, while one
new selector mass \((1-m_k^4)^2/4\) is introduced.  Consequently the total
singleton mass obeys

\[
W_{k+1}=m_k^6W_k+\frac{(1-m_k^4)^2}{4}, \tag{7}
\]

and is uniformly bounded.  The same calculation with
\(p(1+\log(1/p))\) shows that the singleton logarithmic moment is uniformly
bounded, because

\[
m_k^6\le(5/8)^6<1. \tag{8}
\]

On the compact range supplied by (6), the symmetric second difference of
\(R\) is bounded by

\[
K d^2(1+|\log d^2|).
\]

Moreover, the combination defining \(C(\mu,p)\) cancels the common
\(p\log(1/p)\) singularity of its three binary-entropy terms, so
\(|C(\mu,p)|\le K'p(1+|\log p|)\) uniformly on this range.  Equations
(7)--(8) therefore imply

\[
\sup_k|\Theta_k|<\infty. \tag{9}
\]

The increments in (2)--(4) are all bounded.  Hence

\[
2^{-k}I_k=I_0+\sum_{j<k}2^{-j-1}J(m_j^4),
\]

and analogous absolutely convergent series hold for \(2^{-k}U_k\) and
\(2^{-k}M_k\).  Their limits \(I_\infty,U_\infty,M_\infty\) exist, with
\(I_\infty>0\).  Thus for every fixed \(\eta\),

\[
c_{F_k}(\eta)\longrightarrow
c_\infty(\eta)=\frac{M_\infty+(1+\eta)U_\infty}{I_\infty}
=\alpha_\infty+\beta_\infty\eta<\infty. \tag{10}
\]

This proves that repeated fourfold tensor-suspension cannot produce an
unbounded SMR lower bound.

## 3. Certified finite lower bound and numerical limit

`CERTIFY_ITERATED.py` keeps every coefficient and recurrence parameter
rational.  At depth four, \(F_4\) has 1365 physical inputs.  The residual
at \(\eta=1/4,c=2.18\) is a 226-term rational linear combination of
base-two logarithms.  Ninety-digit correctly rounded `Decimal.ln` values
are enlarged by one adjacent representable number on each side, and every
division, product, and sum is rounded outward.  This gives

\[
L_{2.18,1/4}(F_4)
\in[0.18867195539361673287,0.18867195539361673288],
\]

so rigorously

\[
\boxed{c_{F_4}(1/4)>2.18.} \tag{11}
\]

This improves the previous certified lower bound \(c>2.1338\).

The compressed recurrence through depth 40 gives the numerical values

\[
\alpha_\infty\approx1.808574256827,qquad
\beta_\infty\approx1.539070793542,
\]

and therefore

\[
c_\infty(1/4)\approx2.193341955212. \tag{12}
\]

Equation (12) is numerical; (10) and (11) are the proved statements.

## 4. Consequence for the GU program

Every universal \(\operatorname{SMR}(c,1/4)\) theorem must now have
\(c>2.18\).  Conversely, this entire amplification mechanism has a finite
limit and cannot disprove all finite \(c\).  After the reused-cone wedge,
one suspension after tensoring, and the present iterated tower, the lower-
bound mechanism has had three substantive attempts.  The next A004 run
must pivot to an upper estimate for \(\Theta\) or to a different signed
aggregate, rather than optimize this tower further.

