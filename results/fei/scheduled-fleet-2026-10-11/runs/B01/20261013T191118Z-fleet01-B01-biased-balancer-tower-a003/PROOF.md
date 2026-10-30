# Depth-uniform GU' transfer through a biased-balancer tower

All logarithms are base two.  For Boolean signs, let

\[
U(f)=\sum_S\widehat f(S)^2\log_2
\frac{\sum_{T\supseteq S}\widehat f(T)^2}{\widehat f(S)^2},
\qquad
G(f)=\sum_i\left(U(f)-\mathbb E_{x_i}U(f|x_i)\right).
\]

## 1. Tower and theorem

Let

\[
B=(-1,-1,-1,1)
\]

be the two-bit AND sign.  Thus

\[
\mathbb EB=-\frac12,\qquad U(B)=I(B)=1,\qquad G(B)=2.
\]

For a Boolean sign $q$, define its half-activation

\[
A(q)(z,x)=\begin{cases}1,&z=+1,\\q(x),&z=-1.\end{cases}
\]

Let $P$ be arbitrary, let $w$ be a fresh fair character, and set

\[
F_1=A(wP),\qquad F_k=A(B_kF_{k-1})\quad(k\ge2),
\]

where all selectors and all copies $B_k$ use fresh disjoint physical
variables.  Then, for every $d\ge1$,

\[
\boxed{G(F_d)\le2^{-d}G(P)+24.}                       \tag{1}
\]

Consequently, for every $a\ge0$ and $0\le b<1$,

\[
G(P)\le aI(P)+bU(P)
\Longrightarrow
\boxed{G(F_d)\le(a+24)I(F_d)+bU(F_d).}                \tag{2}
\]

The coefficient $b$ is preserved exactly.  The cost is independent of
the base dimension, tower depth, and terminal rarity $2^{-d}$.

If $c\ge72/35$ and $U(P)\le cI(P)$, then also

\[
U(F_d)\le cI(F_d),\qquad
H(F_d)\le(2+2c)I(F_d).                                \tag{3}
\]

In particular, a base with $U(P)\le2I(P)$ gives
$H(F_d)\le(214/35)I(F_d)$ after enlarging $c$ to $72/35$.

## 2. Exact activation identity

Put $m=\mathbb Eq$ and define

\[
\begin{aligned}
R(t)={}&E(t)-\frac12u(t)+\frac14(1-t^2),\\
u(t)={}&t^2\log_2(1/t^2),\\
E(t)={}&\frac{(1+t)^2}{4}\log_2\frac4{(1+t)^2}
+\frac{(1-t)^2}{4}\log_2\frac2{1-t}.
\end{aligned}                                          \tag{4}
\]

The cap calculation from the preceding parity-tower package gives

\[
U(A(q))=\frac12U(q)+R(m).                              \tag{5}
\]

If $m_i^\pm=\mathbb E(q|x_i=\pm1)$, applying (5) to every
restriction gives the exact aggregate identity

\[
G(A(q))=\frac12G(q)+R(m)
+\sum_i\left[R(m)-\frac{R(m_i^+)+R(m_i^-)}2\right].   \tag{6}
\]

No coordinatewise sign assumption is made in (6).

The elementary maxima of $s\log_2(1/s)$ and
$s^2\log_2(1/s)$ imply the global bound

\[
-\frac12<R(t)<\frac74\qquad(-1\le t\le1).             \tag{7}
\]

Hence an unrestricted scalar Jensen term in (6) is at most $9/4$.

## 3. The safe interval and the logarithmic cusp

For $t\ne0$, direct differentiation gives

\[
R''(t)=1+\frac{
\ln\!\left(\dfrac{t^2}{(1+t)\sqrt{1-t}}\right)+3/4}{\ln2}.       \tag{8}
\]

On $[-3/8,-1/8]$,

\[
-4<R''(t)<0.                                           \tag{9}
\]

Indeed,

\[
R'''(t)=\frac1{\ln2}\left(
\frac2t-\frac1{1+t}+\frac1{2(1-t)}\right)<0
\]

there, so it suffices to check the endpoints.  At $-3/8$, use
$\sqrt{8/11}<8/9$ and $e^{3/4}<9/4$; at $-1/8$, use
$\sqrt2>7/5$ and $e^{3/4}>2$.  These inequalities give the two strict
endpoint bounds in (9).

Suppose a coordinate of $f$ has restricted means $m\pm\delta$ lying in
$[1/4,3/4]$.  Since $\mathbb EB=-1/2$, the corresponding three arguments
of $R$ for $Bf$ lie in $[-3/8,-1/8]$.  Taylor's theorem and (9) give

\[
R(-m/2)-\frac{R(-(m+\delta)/2)+R(-(m-\delta)/2)}2
\le\frac{\delta^2}{2}.                                \tag{10}
\]

Summing (10) over such coordinates costs at most
$W_1(f)/2$, where

\[
W_1(f)=\sum_i\widehat f(\{i\})^2.                    \tag{11}
\]

This is the point that removes the repeated-ancestor loss: the dangerous
logarithmic cusp is confined to finitely many exceptional coordinates,
while the inherited safe coordinates are paid by contracting level-one
mass rather than by the full influence.

## 4. Exceptional coordinates and level-one contraction

Write $m_k=\mathbb EF_k$.  Then

\[
m_1=\frac12,\qquad m_k=\frac12-\frac14m_{k-1},
\qquad \frac38\le m_k\le\frac12.                     \tag{12}
\]

In $F_1=A(wP)$, every base coordinate has both restricted means equal to
$1/2$; only $w$ and the top selector can be exceptional.  For $k\ge2$,
every old coordinate becomes safe after one biased activation because

\[
s\in[-1,1]\Longrightarrow \frac{1-s/2}{2}\in[1/4,3/4].
\]

The two new $B_k$ coordinates are handled explicitly, and only the new
top selector can remain exceptional for the next generation.  Therefore
at any biased step there are at most four scalar exceptions: two from
$B_k$ and at most two from $F_{k-1}$.

The level-one mass contracts exactly.  Since
$\mathbb EB=-1/2$ and $W_1(B)=1/2$,

\[
W_1(F_k)=\frac1{16}W_1(F_{k-1})
+\frac18m_{k-1}^2+\frac14(1+m_{k-1}/2)^2.             \tag{13}
\]

Also

\[
W_1(F_1)=\frac{1+(\mathbb EP)^2}{4}\le\frac12.
\]

Using (12) in (13) gives

\[
W_1(F_k)\le\frac1{16}W_1(F_{k-1})+\frac{27}{64}le\frac12.       \tag{14}
\]

## 5. Aggregate $G$ recurrence

Disjoint tensor additivity gives

\[
G(B_kF_{k-1})=G(B_k)+G(F_{k-1})=2+G(F_{k-1}).
\]

Apply (6).  The contributions beyond $G(F_{k-1})/2$ are bounded by:

- $1=G(B)/2$;
- $7/4$ for the outer-selector scalar $R(-m/2)$;
- at most $4(9/4)=9$ for all exceptional coordinates; and
- at most $W_1(F_{k-1})/2\le1/4$ for all safe coordinates.

Thus

\[
\boxed{G(F_k)\le\frac12G(F_{k-1})+12\quad(k\ge2).}    \tag{15}
\]

For the first level, $q=wP$ is balanced.  All base-coordinate terms in
(6) vanish because the fresh character remains after restriction.  The
only nontrivial old-coordinate term is the restriction of $w$.  Therefore
(7) gives directly

\[
G(F_1)\le\frac12G(P)+1+\frac94
=\frac12G(P)+\frac{13}{4}<\frac12G(P)+24.             \tag{16}
\]

Solving (15), the nonseed term is a convex combination of $13/4$ and $24$,
which proves (1).

## 6. Transfer of $I$, $U$, and the coefficient $b$

The first level satisfies

\[
I(F_1)=1+\frac12I(P),\qquad U(F_1)=1+\frac12U(P).      \tag{17}
\]

For every later level, direct pivotal counting and (5) give

\[
\begin{aligned}
I(F_k)&=\frac12I(F_{k-1})+1+\frac14m_{k-1},\\
U(F_k)&=\frac12U(F_{k-1})+\frac12+R(-m_{k-1}/2).
\end{aligned}                                          \tag{18}
\]

By (7), both added terms in (17) are nonnegative.  Hence

\[
I(F_d)\ge2^{-d}I(P),\qquad U(F_d)\ge2^{-d}U(P),
\qquad I(F_d)\ge1.                                    \tag{19}
\]

Combining (1), the base GU' hypothesis, and (19) proves (2).

For the endpoint, (7), (12), and (18) yield

\[
U(F_k)\le\frac12U(F_{k-1})+\frac94,qquad
I(F_k)\ge\frac12I(F_{k-1})+\frac{35}{32}.
\]

Thus $U\le cI$ propagates whenever $c\ge72/35$.  The standard inequality
$H\le2I+2U$ then proves (3).

## 7. Exact scope

This is a proper-class theorem for fresh physical variables.  It removes
exact parity balancing at every positive level and replaces it by a fixed
genuinely biased Boolean balancer of mean $-1/2$.  It is uniform in base
dimension, depth, and terminal rarity.

It does not cover biased outer selectors, variable reuse, arbitrary
balancer bias approaching $\pm1$, or changing coherent cores.  The tower
class is not restriction-closed under arbitrary physical restrictions.
No universal control of the upper-set asymmetry mismatch follows, and
full FEI remains open.
