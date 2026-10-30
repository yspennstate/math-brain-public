# Uniform GU' transfer through variable-rank rare-defect balancers

All logarithms are base two. For a Boolean sign `f`, write

\[
U(f)=\sum_S\widehat f(S)^2\log_2
\frac{\sum_{T\supseteq S}\widehat f(T)^2}{\widehat f(S)^2},
\qquad
G(f)=\sum_i\left(U(f)-\mathbb E_{x_i}U(f|x_i)\right).
\]

## 1. The variable-bias tower

Let `Q_r` be the `r`-bit point-defect sign, equal to `+1` except at one
vertex, where it is `-1`. Put

\[
p_r=2^{-r},\qquad \beta_r=\mathbb E Q_r=1-2p_r.
\]

Thus `Q_r` is nonconstant, its bias tends to `+1`, and restricting a physical
coordinate produces either `Q_{r-1}` or the constant `+1`.

For

\[
A(q)(z,x)=\begin{cases}1,&z=+1,\\q(x),&z=-1,\end{cases}
\]

take an arbitrary Boolean base `P`, a fresh fair character `w`, and an
arbitrary finite rank sequence `r_2,...,r_d`, with every `r_k>=2`. On fresh
disjoint variables define

\[
F_1=A(wP),\qquad F_k=A(Q_{r_k}F_{k-1})\quad(k\ge2).
\tag{1}
\]

Then

\[
\boxed{G(F_d)\le2^{-d}G(P)+24.}
\tag{2}
\]

Consequently, for `a>=0` and `0<=b<1`,

\[
G(P)\le aI(P)+bU(P)
\Longrightarrow
\boxed{G(F_d)\le(a+24)I(F_d)+bU(F_d).}
\tag{3}
\]

The coefficient `b` is unchanged, and the added constant is independent of
base dimension, depth, every chosen rank, and the rare probabilities
`p_{r_k}`.

There is also an unconditional endpoint transfer:

\[
U(P)\le5I(P)
\Longrightarrow
\boxed{U(F_d)\le5I(F_d),\qquad H(F_d)\le12I(F_d).}
\tag{4}
\]

## 2. Scalar activation identity

Define

\[
\begin{aligned}
R(t)&=E(t)-\frac12t^2\log_2(1/t^2)+\frac14(1-t^2),\\
E(t)&=\frac{(1+t)^2}{4}\log_2\frac4{(1+t)^2}
+\frac{(1-t)^2}{4}\log_2\frac2{1-t}.
\end{aligned}
\]

The exact cap identity is

\[
U(A(q))=\frac12U(q)+R(\mathbb Eq),
\tag{5}
\]

and hence, if `m=E q` and `m_i^\pm=E(q|x_i=\pm1)`,

\[
G(A(q))=\frac12G(q)+R(m)
+\sum_i\left(R(m)-\frac{R(m_i^+)+R(m_i^-)}2\right).
\tag{6}
\]

We use the global bounds

\[
-\frac12<R(t)<\frac74\qquad(-1\le t\le1),
\tag{7}
\]

already proved in the preceding B01 activation package.

## 3. Uniform positive-side curvature

For `0<t<1`,

\[
R''(t)=1+\frac{
\ln\!\left(\dfrac{t^2}{(1+t)\sqrt{1-t}}\right)+3/4}{\ln2},
\qquad
R'''(t)=\frac{4-t-t^2}{2\ln2\,t(1-t^2)}>0.
\tag{8}
\]

Thus `R''` is increasing. At `t=1/8`, the inequality `R''(1/8)>-4` is
equivalent to

\[
e^{3/4}>\frac94\sqrt{\frac78}.
\]

Now `sqrt(7/8)<15/16`, while the first five terms of the exponential series
give

\[
e^{3/4}>1+\frac34+\frac9{32}+\frac{27}{384}+\frac{81}{6144}
=\frac{12993}{6144}>\frac{135}{64}.
\]

Therefore

\[
\boxed{R''(t)>-4\qquad(1/8\le t<1).}
\tag{9}
\]

Convexity of `R(t)+2t^2` now implies, for `a,b in [1/8,1]`,

\[
R\!\left(\frac{a+b}{2}\right)-\frac{R(a)+R(b)}2
\le\frac{(a-b)^2}{2}.
\tag{10}
\]

## 4. Exact point-defect budgets

The spectrum of `Q_r` has empty coefficient `beta_r` and every nonempty
coefficient of magnitude `2p_r`. Hence

\[
I(Q_r)=2rp_r,
\qquad
U(Q_r)=\beta_r^2\log_2(1/\beta_r^2)+2rp_r\beta_r.
\tag{11}
\]

Since restricting a coordinate gives `Q_{r-1}` or `1`,

\[
G(Q_r)=r\left(U(Q_r)-\frac12U(Q_{r-1})\right).
\tag{12}
\]

The elementary estimate

\[
-\ln(1-2p)\le\frac{2p}{1-2p}
\]

gives

\[
\beta_r^2\log_2(1/\beta_r^2)\le\frac{4p_r\beta_r}{\ln2}.
\tag{13}
\]

It follows immediately that

\[
\boxed{U(Q_r)\le3I(Q_r).}
\tag{14}
\]

Also `G(Q_2)=2`. For `r=3`, the explicit formula and
`(9/16)log_2(16/9)<1/2` give `G(Q_3)<2`. For `r>=4`, (12)--(13) and
`1/ln2<3/2` give

\[
G(Q_r)\le6rp_r\beta_r
+2rp_r\bigl(1+(2r-4)p_r\bigr).
\tag{15}
\]

Both terms decrease from `r=4` onward, and their value at `r=4` is
`21/16+5/8=31/16`. Therefore

\[
\boxed{G(Q_r)\le2\qquad(r\ge2).}
\tag{16}
\]

For a coordinate of `Q_r`, the three arguments in (6) are

\[
\beta_rm,\qquad (1-4p_r)m,\qquad m,
\]

with the first the midpoint of the latter two. If `r>=3` and `m>=1/2`,
all are at least `1/4`, so (10) bounds the aggregate charge of the `r`
coordinates by

\[
8rp_r^2m^2\le\frac38.
\tag{17}
\]

For `r=2`, the global bound (7) gives the uniform bound `9/2`. Thus at every
rank the full point-defect-coordinate charge is at most `9/2`.

## 5. The cusp is paid only once

Every restricted mean of `F_1=A(wP)` lies in `[0,1]`. Base coordinates have
both restricted means exactly `1/2`; only `w` and the first selector can meet
zero. Their combined charge at the first point-defect step is at most `9/2`
by (7).

After that step, every restricted mean of `F_2` is at least `1/4`:

- inherited means become `(1+beta_r s)/2>=1/2` for `s>=0`;
- point-defect-coordinate means are at least `1/2`; and
- the new selector branches have means `1` and `beta_r E F_1>=1/4`.

The same lower bound is preserved at every later level. Thus, from the third
activation onward, all inherited scalar arguments lie in `[1/8,1]`. If the
two restricted means of coordinate `i` are `m+-delta_i`, (10) charges it by
at most `2 beta_r^2 delta_i^2`. Summing gives

\[
\sum_i\text{inherited charge}_i
\le2\beta_r^2W_1(F_{k-1})\le2.
\tag{18}
\]

This is the parameter-free refund of the rare logarithm. The local curvature
does diverge at zero, but the tower moves all inherited coordinates to the
positive safe interval after one step; only two physical coordinates ever
pay the global fixed price.

## 6. GU' recurrence

Disjoint tensor additivity and (16) give

\[
\frac12G(Q_rF)=\frac12G(F)+\frac12G(Q_r)
\le\frac12G(F)+1.
\]

At the first point-defect step, the remaining terms in (6) are bounded by

\[
\frac74+\frac92+\frac92,
\]

for the root scalar, point-defect coordinates, and the two unsafe inherited
coordinates. Therefore

\[
G(F_2)<\frac12G(F_1)+12.
\]

At every later step, (18) replaces the last `9/2` by `2`, so the same bound
continues to hold:

\[
\boxed{G(F_k)\le\frac12G(F_{k-1})+12\quad(k\ge2).}
\tag{19}
\]

The first balanced activation satisfies

\[
G(F_1)\le\frac12G(P)+\frac{13}{4}.
\tag{20}
\]

Solving (19) proves (2). Since

\[
I(F_d)\ge2^{-d}I(P),\qquad U(F_d)\ge2^{-d}U(P),\qquad I(F_d)\ge1,
\]

the conditional GU' implication (3) follows with `b` preserved exactly.

## 7. Endpoint recurrence

For `0<=t<1`, put `epsilon=1-t`. Dropping the nonpositive term in `R` and
using `-ln(1-x)<=x/(1-x)` gives

\[
R(t)\le\left(\frac1{\ln2}+\frac1{2e\ln2}+\frac12\right)(1-t)
<\frac52(1-t).
\tag{21}
\]

Indeed, the two entropy terms are bounded respectively by
`epsilon/ln2` and `epsilon/(2e ln2)`, and `(1-t^2)/4<=epsilon/2`.

At every point-defect step, `m=E F_{k-1}>=1/2`, so
`t=beta_r m>=1/4`. From (5), (11), (14), and (21),

\[
\begin{aligned}
U(F_k)&=\frac12U(F_{k-1})+\frac12U(Q_r)+R(t),\\
I(F_k)&=\frac12I(F_{k-1})+\frac12I(Q_r)+\frac{1-t}{2},
\end{aligned}
\]

and

\[
\frac12U(Q_r)+R(t)
\le\frac52I(Q_r)+\frac52(1-t)
=5\left(\frac12I(Q_r)+\frac{1-t}{2}\right).
\]

The first balanced activation also preserves `U<=5I`, proving (4). The last
claim follows from the standard `H<=2I+2U` bridge.

## 8. Exact scope

The point-defect balancer family is restriction-closed and its allowed biases
approach `+1`; ranks may vary arbitrarily with depth. The activated tower class
itself is not restriction-closed. The proof still requires fresh disjoint
blocks and fair outer selectors, and it does not cover negative near-constant
balancers, biased selectors, reused variables, or changing overlapping cores.
It is therefore a proper-class transfer theorem, not universal GU' and not
full FEI.
