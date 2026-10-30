# A003 — tensor/activation closure of the singleton-potential GU' invariant

All logarithms are base two.  Write

\[
U(f)=\sum_S\widehat f(S)^2\log_2
\frac{\sum_{T\supseteq S}\widehat f(T)^2}{\widehat f(S)^2},
\qquad
G(f)=\sum_i\left(U(f)-\mathbb E_{x_i}U(f|x_i)\right).
\]

## Theorem

Let `C` be a restriction-closed Boolean class satisfying

\[
G(f)\le aI(f)+bU(f),\qquad a\ge0,\quad0\le b<1.       \tag{1}
\]

Let `TA(C)` be the smallest class containing `C` and closed under:

1. disjoint products `fg` of any two already generated functions;
2. fresh fair half-activation
   \[
   A(q)(z,x)=1\ (z=+1),\qquad A(q)(z,x)=q(x)\ (z=-1);
   \]
3. arbitrary physical-coordinate restrictions.

Put

\[
M=\frac2{\ln2},\quad
\rho=\frac{1+\ln2}{4},\quad
\lambda=\frac4{1-\ln2},\quad
C_*=\lambda M=\frac8{\ln2(1-\ln2)},
\]

and

\[
A_* = \max\left\{a,\frac83\right\}+C_* .               \tag{2}
\]

Then every `F in TA(C)` satisfies

\[
\boxed{G(F)\le A_*I(F)+bU(F).}                          \tag{3}
\]

Because the class is restriction-closed, the standard restriction induction
then gives

\[
\boxed{U(F)\le\frac{A_*}{1-b}I(F)},                     \tag{4}
\]

and the generic bridge `H<=2I+2U` gives

\[
\boxed{H(F)\le\left(2+\frac{2A_*}{1-b}\right)I(F).}     \tag{5}
\]

For the base class of constants and signed characters, take `a=b=0`.  This
produces the explicit expanding restriction-closed class bound

\[
G(F),U(F)\le
\left(\frac83+\frac8{\ln2(1-\ln2)}\right)I(F)
<40.279358 I(F),                                          \tag{6}
\]

and

\[
\boxed{H(F)<82.558716 I(F).}                             \tag{7}
\]

This class allows arbitrary finite **branched** disjoint product/activation
trees, not only one activation spine with point-defect side factors.

## 1. Singleton potential input

Use the independently reviewed potential

\[
\phi(h)=2h^2\left(\log_2(1/h)+1/\ln2\right),\qquad
\Phi(f)=\sum_i\phi(|\widehat f(\{i\})|).                 \tag{8}
\]

The reviewed scalar and activation inequalities are

\[
\Phi(f)\le MI(f),                                        \tag{9}
\]

\[
G(A(q))\le\tfrac12G(q)+R(\mathbb Eq)+\Phi(q),           \tag{10}
\]

\[
\Phi(A(q))\le\rho\Phi(q)+MJ,qquad
J=\frac{1-\mathbb Eq}{2},                                \tag{11}
\]

and

\[
I(A(q))=\tfrac12I(q)+J,qquad
U(A(q))=\tfrac12U(q)+R(\mathbb Eq).                      \tag{12}
\]

The choice of `lambda` gives

\[
1+\lambda\rho-\lambda/2=0.                              \tag{13}
\]

## 2. A sharper all-sign root price

The previously reviewed negative-half lemma gives

\[
R(t)\le1\qquad(-1\le t\le0).                            \tag{14}
\]

Since `J=(1-t)/2>=1/2`, this implies `R(t)<=2J` there.

For `0<t<1`, direct differentiation gives

\[
R'''(t)=\frac{4-t-t^2}{2\ln2\,t(1-t^2)}>0.              \tag{15}
\]

Thus `R'` is convex.  At `t=1/2`,

\[
R'(1/2)=-\frac14-\frac32\log_2\frac32-\frac1{8\ln2},   \tag{16}
\]

\[
R''(1/2)=\frac32+\frac{3/4-\ln6}{\ln2}.                \tag{17}
\]

The elementary certified intervals

\[
.69<\ln2<.70,quad .405<\ln(3/2)<.406,quad
1.79<\ln6<1.80                                           \tag{18}
\]

give `R'(1/2)>-1.314` and `|R''(1/2)|<1/40`.  The tangent
lower bound for the convex function `R'` therefore yields, for every
`0<=t<=1`,

\[
R'(t)\ge R'(1/2)+R''(1/2)(t-1/2)>-\frac43.              \tag{19}
\]

Because `R(1)=0`, integration gives

\[
R(t)\le\frac43(1-t)=\frac83J.                           \tag{20}
\]

Together with (14),

\[
\boxed{(1-b)R(t)\le\frac83J\qquad(-1\le t\le1).}       \tag{21}
\]

The logarithm intervals in (18) follow, for example, by the positive atanh
series after rational range reduction; their margins are much wider than the
truncation error needed here.

## 3. Disjoint products of arbitrary generated factors

If `f` and `g` use disjoint variables, the upper-set law factors, so

\[
G(fg)=G(f)+G(g),\quad U(fg)=U(f)+U(g),\quad
I(fg)=I(f)+I(g).                                         \tag{22}
\]

For a coordinate of `f`, its singleton coefficient in `fg` is
`(Eg) fhat({i})`, and symmetrically for `g`.  Since `phi` is increasing on
`[0,1]`,

\[
\boxed{\Phi(fg)\le\Phi(f)+\Phi(g).}                      \tag{23}
\]

This is the class extension: (23) needs no point-defect spectrum and no
one-spine hypothesis.

## 4. Propagation of the invariant

We prove

\[
G(f)+\lambda\Phi(f)\le A_*I(f)+bU(f).                   \tag{24}
\]

For a seed in `C`, (1) and (9) prove (24), because
`A_*>=a+lambda M`.  If (24) holds for two disjoint factors, (22)--(23) prove
it for their product.

If it holds for `q`, then (10)--(13) and (21) give

\[
\begin{aligned}
G(A(q))+\lambda\Phi(A(q))
&\le \tfrac12 A_*I(q)+\tfrac b2U(q)
 +(1-b)R(\mathbb Eq)+\lambda MJ\\
&\le \tfrac12 A_*I(q)+(8/3+\lambda M)J
 +b\bigl(\tfrac12U(q)+R(\mathbb Eq)\bigr)\\
&\le A_*I(A(q))+bU(A(q)),
\end{aligned}                                             \tag{25}
\]

because `A_*>=8/3+lambda M`.  Restrictions preserve the grammar: they act
inside one tensor factor, and an activation selector restriction returns
either `1` or its child.  Thus (24), hence (3), holds throughout `TA(C)`.

## 5. GU' to U and FEI

Let `K=A_*/(1-b)` and induct on the ambient dimension.  All restrictions stay
in the class.  Using the induction hypothesis on every child and the exact
influence identity

\[
\sum_i\mathbb E I(f|x_i)=(n-1)I(f),                     \tag{26}
\]

we obtain

\[
\begin{aligned}
nU(f)
&=G(f)+\sum_i\mathbb E U(f|x_i)\\
&\le A_*I(f)+bU(f)+K(n-1)I(f).
\end{aligned}
\]

Since `A_*=K(1-b)`, this is `(n-b)U(f)<=K(n-b)I(f)`, proving
(4).  Equation (5) follows from `H<=2I+2U`.

## Exact remaining gap

The theorem covers arbitrary finite branching, all sign patterns, dimensions,
depths, dyadic terminal rarities, and physical restrictions, but it still
requires fresh disjoint variable blocks and fair selectors.  It does not
control biased outer selectors, shared/reused variables, or the aggregate
upper-set asymmetry mismatch in a genuinely overlapping hierarchy.  Those
are precisely the hypotheses that must be removed for universal GU' and full
FEI.

