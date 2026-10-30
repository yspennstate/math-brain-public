# Uniform retained credit for positive point-defect towers

All logarithms are base two.  For a Boolean sign `f`, write

\[
U(f)=\sum_S\widehat f(S)^2\log_2
\frac{\sum_{T\supseteq S}\widehat f(T)^2}{\widehat f(S)^2},
\qquad I(f)=\sum_S|S|\widehat f(S)^2.
\]

## 1. Statement

Let `Q_r` be `+1` except at one vertex of the `r`-cube and let

\[
A(q)(z,x)=\begin{cases}1,&z=+1,\\q(x),&z=-1.\end{cases}
\]

For an arbitrary Boolean base `P`, a fresh fair character `w`, and any finite
sequence `r_k>=2`, use pairwise disjoint physical blocks and set

\[
F_1=A(wP),\qquad F_k=A(Q_{r_k}F_{k-1})\quad(k\ge2). \tag{1}
\]

Then

\[
U(P)\le\frac83 I(P)
\Longrightarrow
\boxed{U(F_d)\le\frac83I(F_d)\quad(d\ge1).} \tag{2}
\]

If `h` is a Boolean sign on a common disjoint block and `T` is any finite
adaptive or pruned restriction tree querying physical variables of `F_d`,
then

\[
\boxed{
U(F_dh)-\sum_\ell w_\ell U((F_d)_\ell h)
\le\frac83I(F_d).} \tag{3}
\]

## 2. Exact scalar and recurrences

Define

\[
\begin{aligned}
R(t)&=E(t)-\frac12t^2\log_2(1/t^2)+\frac14(1-t^2),\\
E(t)&=\frac{(1+t)^2}{4}\log_2\frac4{(1+t)^2}
+\frac{(1-t)^2}{4}\log_2\frac2{1-t}.
\end{aligned} \tag{4}
\]

The exact half-activation identity is

\[
U(A(q))=\frac12U(q)+R(\mathbb E q). \tag{5}
\]

For `p=2^{-r}` and `beta=1-2p`, the spectrum of `Q_r` has empty
coefficient `beta` and every nonempty coefficient of magnitude `2p`.  Hence

\[
I(Q_r)=2rp,\qquad
U(Q_r)=\beta^2\log_2(1/\beta^2)+2rp\beta. \tag{6}
\]

Writing `m=E F_{k-1}` and `t=beta m`, disjoint tensor additivity, (5), and
the exact selector influence give

\[
\begin{aligned}
U(F_k)&=\frac12U(F_{k-1})+\frac12U(Q_r)+R(t),\\
I(F_k)&=\frac12I(F_{k-1})+\frac12I(Q_r)+\frac{1-t}{2}.
\end{aligned} \tag{7}
\]

## 3. Point-defect block bound

For `r>=3`, the elementary inequality

\[
-\ln(1-2p)\le\frac{2p}{1-2p}
\]

implies

\[
\beta^2\log_2(1/\beta^2)\le\frac{4p\beta}{\ln2}.
\]

After division by `I(Q_r)=2rp`,

\[
\frac{U(Q_r)}{I(Q_r)}
\le\beta+\frac{2\beta}{r\ln2}<2, \tag{8}
\]

using `1/ln2<3/2`.  At `r=2`, (6) gives `U(Q_2)=I(Q_2)=1` exactly.
Therefore

\[
\boxed{U(Q_r)\le2I(Q_r)\quad(r\ge2).} \tag{9}
\]

## 4. Sharp-enough positive scalar bound

For `0<t<1`, direct differentiation gives

\[
R''(t)=1+\frac{
\ln\!\left(\dfrac{t^2}{(1+t)\sqrt{1-t}}\right)+3/4}{\ln2},
\qquad
R'''(t)=\frac{4-t-t^2}{2\ln2\,t(1-t^2)}>0. \tag{10}
\]

Thus `R''` is strictly increasing and `R'` has one global minimum, at the
unique zero `tau` of `R''`.

We now locate and bound that minimum with elementary exact estimates.  Put

\[
a(t)=\frac{t^2}{(1+t)\sqrt{1-t}}.
\]

The exponential series gives

\[
e^{3/4}<\frac{17}{8},\qquad e^{3/4}>1+\frac34+\frac9{32}+\frac{27}{384}.
\tag{11}
\]

For the upper bound, sum through degree four and dominate the tail beginning
at degree five by a geometric series of ratio `1/8`; the resulting rational
number is strictly below `17/8`.

At `t=49/100`, `sqrt(51)>71/10`, so `a(t)<23/100`; (11) yields
`e^{3/4}a(t)<1/2` and hence `R''(49/100)<0`.  At `t=51/100`,

\[
a(t)=\frac{2601}{10570},
\]

and the lower bound in (11) gives `e^{3/4}a(t)>1/2` (cross-multiplication is
an exact integer comparison), so
`R''(51/100)>0`.  Therefore

\[
\frac{49}{100}<\tau<\frac{51}{100}. \tag{12}
\]

The same estimates give `e^{3/4}a(49/100)>1/4` (use
`sqrt(51)<36/5` and `e^{3/4}>7/4`) and
`e^{3/4}a(51/100)<1`.  Thus, by monotonicity,

\[
|R''(t)|<1\qquad(49/100\le t\le51/100). \tag{13}
\]

An exact evaluation gives

\[
R'(1/2)=\frac34\log_2\frac{16}{9}-\frac74-\frac1{8\ln2}. \tag{14}
\]

Now `log_2(16/9)>33/40`, because it is equivalent to

\[
2^{127}>3^{80}
\]

and the two integers are respectively
`170141183460469231731687303715884105728` and
`147808829414345923316083210206383297601`.  Also the positive-term
atanh series gives

\[
\ln2=2\sum_{j\ge0}\frac{(1/3)^{2j+1}}{2j+1}>rac{56}{81}.
\]

Consequently

\[
R'(1/2)>\frac{99}{160}-\frac74-\frac{81}{448}. \tag{15}
\]

Combining (12)--(15) with the mean value theorem,

\[
R'(\tau)>\frac{99}{160}-\frac74-\frac{81}{448}-\frac1{100}
=-\frac{14807}{11200}>-\frac43. \tag{16}
\]

Since `tau` is the global minimizer of `R'`, (16) holds for every
`t in (0,1)`.  Finally `R(1)=0`, so integration gives

\[
\boxed{R(t)\le\frac43(1-t)\qquad(0\le t\le1).} \tag{17}
\]

## 5. Endpoint propagation

At the first balanced level,

\[
U(F_1)=1+\frac12U(P),\qquad I(F_1)=1+\frac12I(P),
\]

so every constant `c>=1` propagates from `P` to `F_1`.  For later levels,
assume `U(F_{k-1})<=cI(F_{k-1})` with `c=8/3`.  From (7), (9), and (17),

\[
\begin{aligned}
U(F_k)
&\le \frac c2I(F_{k-1})+I(Q_r)+\frac43(1-t)\\
&\le \frac c2I(F_{k-1})+\frac c2I(Q_r)+\frac c2(1-t)
=cI(F_k).
\end{aligned}
\]

This proves (2).  The standard bridge `H<=2I+2U` gives

\[
H(F_d)\le\frac{22}{3}I(F_d). \tag{18}
\]

## 6. Complete tree payment

For any finite adaptive/pruned physical restriction tree,

\[
\sum_{v\in T^\circ}w_v\left(
U((F_d)_vh)-\frac{U((F_d)_{v,+}h)+U((F_d)_{v,-}h)}2\right)
=U(F_dh)-\sum_\ell w_\ell U((F_d)_\ell h). \tag{19}
\]

Disjoint tensor additivity makes every term `U((F_d)_v h)` equal
`U((F_d)_v)+U(h)`, so the common terminal contribution cancels exactly once.
Since leaf `U` is nonnegative, (2) gives

\[
U(F_d)-\sum_\ell w_\ell U((F_d)_\ell)
\le U(F_d)\le\frac83I(F_d),
\]

proving (3).  This is a single-use signed telescope; it does not assert a
positive nodewise charge.

## 7. Scope

Ranks, depth, base dimension, tree policy, reveal order, pruning, and terminal
core complexity are uniform.  Activation probabilities may tend to zero.
The proof still requires fresh disjoint point-defect blocks and fair outer
selectors.  It does not cover negative near-constant bias, biased selectors,
variable reuse, or changing overlapping coherent cores.  Thus it is not a
universal `U<=KI` estimate and does not prove full FEI.
