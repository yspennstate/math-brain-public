# A023: singleton-potential amortization for signed rare-defect hierarchies

All logarithms are base two.  For a Boolean sign (f), let

\[
 U(f)=\sum_S\widehat f(S)^2\log_2
 \frac{\sum_{T\supseteq S}\widehat f(T)^2}{\widehat f(S)^2},
 \qquad
 G(f)=\sum_i\left(U(f)-\mathbb E_{x_i}U(f|x_i)\right).
\]

This note proves a dimension-, depth-, rank-, and sign-independent
first-revelation amortization, expressed as a GU' transfer, on an explicit
restriction-closed rare-activation class.  It also repairs the
unpaid step in the preceding positive point-defect tower proof: an additive
bound on (G) cannot be converted to a multiple of (I) by asserting
(I\ge1), because rare positive towers can have arbitrarily small total
influence.

## 1. The class and theorem

Let (Q_r) be the (r)-bit point-defect sign, equal to (+1) except at
one vertex, with (r\ge1).  A **rare-defect product** is any finite product
on disjoint variable blocks of signs (pm Q_r); the empty product is (1).
For a Boolean (q), define the fresh fair half-activation

\[
 A(q)(z,x)=\begin{cases}1,&z=+1,\\q(x),&z=-1.\end{cases}
\]

Let (mathcal C) be a restriction-closed Boolean class for which, for fixed
(a\ge0) and (0\le b<1),

\[
 G(f)\le aI(f)+bU(f)\qquad(f\in\mathcal C).                 \tag{1}
\]

Let (mathcal T(mathcal C)) be the smallest class obtained from
(mathcal C) by repeatedly:

1. multiplying by a rare-defect product on fresh disjoint variables;
2. applying (A) with a fresh selector; and
3. taking arbitrary coordinate restrictions.

Put

\[
 M=\frac2{\ln2},\qquad
 \rho=\frac{1+\ln2}{4}<\frac12,\qquad
 \lambda=\frac4{1-\ln2},\qquad
 C_*=\lambda M=\frac8{\ln2(1-\ln2)}.
\]

Thus (C_*=37.6126911532\ldots).  The main claim is

\[
 \boxed{G(F)\le\bigl(\max\{a,5\}+C_*\bigr)I(F)+bU(F)
 \quad(F\in\mathcal T(mathcal C)).}                       \tag{2}
\]

In particular, starting from constants and signed parities (where
(G=U=0)) gives the explicit restriction-closed class bound

\[
 \boxed{G(F)\le42.6126911533\,I(F).}                       \tag{3}
\]

The class permits arbitrary finite depth, arbitrary changes of sign,
arbitrary point-defect ranks, arbitrary finite products of defects between
selectors, and every coordinate restriction of every such expression.

## 2. A global logarithmic midpoint bound

Use the scalar activation function from the exact identity

\[
 U(A(q))=\frac12U(q)+R(\mathbb E q).                       \tag{4}
\]

For (-1<t<1, t\ne0), direct differentiation gives

\[
 R''(t)=1+\frac{\ln\!\left(
 t^2/((1+t)\sqrt{1-t})\right)+3/4}{\ln2}.                 \tag{5}
\]

The denominator (D(t)=(1+t)\sqrt{1-t}) is at most (2): indeed
(D(t)^2=(1+t)^2(1-t)) has its interior maximum (32/27) at (t=1/3).
Therefore

\[
 -R''(t)\le2\log_2\frac1{|t|}.                            \tag{6}
\]

Define, continuously at zero,

\[
 \phi(h)=2h^2\left(\log_2\frac1h+\frac1{\ln2}\right),
 \qquad 0\le h\le1.                                      \tag{7}
\]

If (x=m-h) and (y=m+h) lie in ([-1,1]), the second-difference
identity and (6) give

\[
\begin{aligned}
 R(m)-\frac{R(x)+R(y)}2
 &=-\frac12\int_{-h}^{h}(h-|u|)R''(m+u)\,du\\
 &\le h\int_{m-h}^{m+h}\log_2\frac1{|v|}\,dv\\
 &\le2h^2\left(\log_2\frac1h+\frac1{\ln2}\right)=\phi(h). \tag{8}
\end{aligned}
\]

The last line uses the fact that, among intervals of length (2h), the
integral of the symmetric decreasing function (log_2(1/|v|)) is largest
when the interval is centered at zero.  Approximation handles intervals
containing zero and the endpoints.

Two elementary consequences of (7) are

\[
 \phi(h)\le Mh,
 \qquad
 \phi(h/2)\le\rho\phi(h).                                \tag{9}
\]

For the first, differentiate
(h(\log_2(1/h)+1/\ln2)); it is increasing on ([0,1]).
For the second, write (A=\log_2(1/h)+1/\ln2\ge1/\ln2) and observe

\[
 \frac{\phi(h/2)}{\phi(h)}
 =\frac14\frac{A+1}{A}\le\frac{1+\ln2}{4}=\rho.          \tag{10}
\]

## 3. The singleton potential

Define

\[
 \Phi(f)=\sum_i\phi\bigl(|\widehat f(\{i\})|\bigr).       \tag{11}
\]

For Boolean (f), the physical derivative identity gives

\[
 |\widehat f(\{i\})|\le\operatorname{Inf}_i(f).
\]

Together with (9),

\[
 \boxed{0\le\Phi(f)\le M I(f).}                          \tag{12}
\]

If (m=\mathbb E q) and (m_i^pm=\mathbb E(q|x_i=\pm1)), then
((m_i^+-m_i^-)/2=\widehat q(\{i\})).  Hence the exact activation identity
for (G) and (8) imply

\[
 G(A(q))\le\frac12G(q)+R(m)+\Phi(q).                     \tag{13}
\]

The singleton coefficients of (A(q)) are half those of (q), except
for the new selector coefficient (J=(1-m)/2).  Thus (9) gives the strict
potential contraction

\[
 \boxed{\Phi(A(q))\le\rho\Phi(q)+M J.}                   \tag{14}
\]

Also

\[
 I(A(q))=\frac12I(q)+J.                                  \tag{15}
\]

The coefficient (lambda) was chosen so that

\[
 1+\lambda\rho-\frac\lambda2=0.                         \tag{16}
\]

This is the single-use accounting: the entire logarithmic midpoint charge
(Phi(q)) in (13) is exactly paid by the drop in the stored potential.

## 4. Product and root budgets

For (Q_r), put (p=2^{-r}), (eta=1-2p).  The exact formulas are

\[
 I(Q_r)=2rp,
 \quad
 U(Q_r)=\beta^2\log_2(1/\beta^2)+2rp\beta,
 \quad
 G(Q_r)=r\left(U(Q_r)-\frac12U(Q_{r-1})\right),          \tag{17}
\]

with (Q_1) a character.  The earlier point-defect estimate gives, for
(r\ge4),

\[
 G(Q_r)\le6rp\beta+2rp\bigl(1+(2r-4)p\bigr).
\]

Dividing by (I(Q_r)) gives at most
(3\beta+1+(2r-4)p<5).  The cases (r=1,2,3) follow directly from (17).
Consequently every rare-defect product (B), by exact disjoint-product
additivity, satisfies

\[
 \boxed{G(B)\le5I(B).}                                   \tag{18}
\]

If (q=Bh) on disjoint variables, with (gamma=\mathbb EB) and
(s=\mathbb Eh), then its singleton coefficients are
(gamma\widehat h(\{i\})) and (s\widehat B(\{j\})).  Since (phi)
is increasing and (12) applies to (B),

\[
 \Phi(Bh)\le\Phi(h)+MI(B).                               \tag{19}
\]

We also use the already proved scalar bounds

\[
 R(t)\le\frac52(1-t)\quad(0\le t\le1),
 \qquad R(t)<\frac74\quad(-1\le t\le1).                 \tag{20}
\]

For (J=(1-t)/2) and (0\le b<1), these imply uniformly

\[
 \boxed{(1-b)R(t)\le5J.}                                \tag{21}
\]

Indeed (20) gives the claim for (t\ge0).  For (t<0), it is automatic
when (R(t)<0), while otherwise (J\ge1/2) and (R(t)<7/4<5J).

## 5. The invariant

Set

\[
 A_*=\max\{a,5\}+\lambda M.
\]

We prove throughout the generated class the stronger inequality

\[
 \boxed{G(f)+\lambda\Phi(f)\le A_*I(f)+bU(f).}            \tag{22}
\]

For a seed (f\in\mathcal C), (1) and (12) establish (22).

Suppose (22) holds for (h), and let (q=Bh) for a rare-defect product
(B) on fresh variables.  Disjoint product additivity, (18), and (19)
give

\[
\begin{aligned}
 G(q)+\lambda\Phi(q)
 &\le A_*I(h)+bU(h)+(5+\lambda M)I(B)\\
 &\le A_*I(q)+bU(q),
\end{aligned}                                             \tag{23}
\]

because (A_*\ge5+\lambda M) and (U(B)\ge0).

Now suppose (22) holds for an arbitrary (q), and put (F=A(q)),
(t=\mathbb Eq), (J=(1-t)/2).  Using (4), (13)--(16), and (21),

\[
\begin{aligned}
 G(F)+\lambda\Phi(F)
 &\le\frac12G(q)+R(t)+\Phi(q)
      +\lambda\rho\Phi(q)+\lambda MJ\\
 &\le\frac{A_*}{2}I(q)+\frac b2U(q)
      +(1-b)R(t)+\lambda MJ\\
 &\le\frac{A_*}{2}I(q)+(5+\lambda M)J
      +b\left(\frac12U(q)+R(t)\right)\\
 &\le A_*I(F)+bU(F).                                     \tag{24}
\end{aligned}
\]

This proves (22), hence (2), under both generating operations.

## 6. Restriction closure

A restriction of a point defect is either a lower-rank point defect or a
constant.  Restricting a disjoint product preserves the same product form.
For an activation (A(q)), restricting its selector gives either (1) or
(q), while restricting any other coordinate gives (A(q|x_i=\pm1)).
Thus the generated class is genuinely restriction-closed, and the induction
above applies to every restricted descendant without adding a hypothesis or
changing the constant.

Taking (mathcal C) to be constants and signed parities gives (3), since
all restrictions remain constants or parities and (G=U=0).

## 7. Correction to the preceding tower transfer

The positive point-defect tower report proved the useful additive recurrence
(G(F_d)\le2^{-d}G(P)+24), but its conversion to
(G(F_d)\le(a+24)I(F_d)+bU(F_d)) used the displayed assertion
(I(F_d)\ge1).  That assertion is false for rare positive activations.
For example, with constant seed, the first balanced cap has (I(F_1)=1),
and a subsequent positive (Q_r) step has exactly

\[
 I(F_2)=\frac34+\frac{r+1/2}{2^r}<1\qquad(r\ge6).         \tag{25}
\]

Long positive high-rank runs make the influence arbitrarily small.  The
additive (G) recurrence and the separately proved endpoint recurrence are
not refuted by (25), but the old GU' implication requires replacement.  The
potential invariant (22) supplies that replacement and also permits arbitrary
sign changes and restriction closure.

## 8. Exact scope and remaining gap

The theorem covers a new all-parameter restriction-closed class and removes
depth, activation probability, point-defect rank, sign pattern, and the
number of disjoint rare-defect factors between selectors.  It also transfers
any already proved base GU' inequality without increasing (b).

It does **not** prove universal GU' or FEI.  Its hierarchy is still generated
by fresh fair selectors and disjoint point-defect products.  It does not cover
reused variables, biased selectors, arbitrary coherent balancers, or changing
overlapping cores.  Extending (19)--(24) to an overlapping product/composition
requires a replacement for exact (G,U,I) additivity and is the next unpaid
step.  Full FEI remains open.
