# Retained upper-set credit through biased activation towers

All logarithms are base two.  For a Boolean sign (f), write

\[
U(f)=\sum_S\widehat f(S)^2\log_2
\frac{\sum_{T\supseteq S}\widehat f(T)^2}{\widehat f(S)^2},
\qquad I(f)=\sum_S|S|\widehat f(S)^2.
\]

## Theorem

Let (P) be any Boolean sign and let (w) be a fresh fair character.  Put

\[
B=(-1,-1,-1,1),\qquad \mathbb EB=-\frac12,qquad U(B)=I(B)=1,
\]

and define half-activation by

\[
A(q)(z,x)=\begin{cases}1,&z=+1,\\q(x),&z=-1.\end{cases}
\]

On fresh disjoint physical variables set

\[
F_1=A(wP),\qquad F_k=A(B_kF_{k-1})\quad(k\ge2).
\tag{1}
\]

For every (c\ge48/35),

\[
U(P)\le cI(P)\quad\Longrightarrow\quad
\boxed{U(F_d)\le cI(F_d)\quad(d\ge1).}
\tag{2}
\]

Let (h) be an arbitrary Boolean sign on a common disjoint block, and let
(\mathcal T) be any finite adaptive or pruned restriction tree querying
physical variables of (F_d).  If (w_\ell) is the probability of leaf
(\ell), then

\[
\boxed{
U(F_dh)-\sum_\ell w_\ell U((F_d)_\ell h)
\le cI(F_d).
}
\tag{3}
\]

In particular, the dense nullity-two shields from the preceding B05 theorem
satisfy (U(P)\le2I(P)).  For every such shield, every depth, and every tree
above,

\[
U(F_dh)-\sum_\ell w_\ell U((F_d)_\ell h)le2I(F_d),
\qquad H(F_d)\le6I(F_d).
\tag{4}
\]

The constants are independent of the shield dimension and orientation, its
coherent core, tower depth, terminal rarity (2^{-d}), tree policy, reveal
order, pruning, and the common terminal core.

## 1. Exact activation recurrences

For (t\in[-1,1]), define the continuous scalar

\[
\begin{aligned}
R(t)={}&E(t)-\frac12u(t)+\frac14(1-t^2),\\
u(t)={}&t^2\log_2(1/t^2),\\
E(t)={}&\frac{(1+t)^2}{4}\log_2\frac4{(1+t)^2}
+\frac{(1-t)^2}{4}\log_2\frac2{1-t},
\end{aligned}
\tag{5}
\]

with the usual zero convention.  Direct Fourier cap accounting gives

\[
U(A(q))=\frac12U(q)+R(\mathbb Eq).
\tag{6}
\]

For disjoint products, both (U) and (I) add.  Character multiplication
preserves (U) and adds one to (I).  Finally, the selector of (A(q)) has
influence ((1-\mathbb Eq)/2), while every old influence is halved.  Thus,
writing (m_k=\mathbb EF_k),

\[
\begin{aligned}
m_1&=\frac12,&
U(F_1)&=1+\frac12U(P),&
I(F_1)&=1+\frac12I(P),\\
m_k&=\frac12-\frac14m_{k-1},&
U(F_k)&=\frac12U(F_{k-1})+\frac12+R(-m_{k-1}/2),&
I(F_k)&=\frac12I(F_{k-1})+1+\frac14m_{k-1}.
\end{aligned}
\tag{7}
\]

In particular,

\[
\frac38\le m_k\le\frac12.
\tag{8}
\]

## 2. A one-sided scalar lemma

The key improvement over the earlier coarse endpoint estimate is

\[
\boxed{R(t)\le1\qquad(-1\le t\le0).}
\tag{9}
\]

For (t\in(-1,0)), differentiation gives

\[
R''(t)=1+\frac{
\ln\!\left(\dfrac{t^2}{(1+t)\sqrt{1-t}}\right)+3/4}{\ln2}
\tag{10}
\]

and

\[
R'''(t)=\frac{4-t-t^2}{2\ln2\,t(1-t^2)}<0.
\tag{11}
\]

Hence (R'') decreases strictly from (+\infty) to (-\infty), so it has
one zero.  Moreover,

\[
R'(-1+)=\frac{\ln2-1}{2\ln2}<0,
\qquad
R'(0-)=\frac12-\frac1{4\ln2}>0.
\tag{12}
\]

It follows that (R') first increases and then decreases, crosses zero
exactly once, and remains positive at the right endpoint.  Thus (R) first
decreases and then increases on ([-1,0]).  Since

\[
R(-1)=0,\qquad R(0)=1,
\]

(9) follows.

## 3. Endpoint propagation

At the first level, for every (c\ge1),

\[
U(F_1)-cI(F_1)
=\frac12\bigl(U(P)-cI(P)\bigr)+(1-c)\le0.
\tag{13}
\]

For (k\ge2), (7)--(9) give

\[
\begin{aligned}
U(F_k)-cI(F_k)
&\le\frac12\bigl(U(F_{k-1})-cI(F_{k-1})\bigr)
+\frac32-c\left(1+\frac14m_{k-1}\right)\\
&\le\frac12\bigl(U(F_{k-1})-cI(F_{k-1})\bigr)
+\frac32-\frac{35}{32}c.
\end{aligned}
\tag{14}
\]

The last scalar is nonpositive exactly when (c\ge48/35).  Induction proves
(2).  The standard inequality (H\le2I+2U) then gives

\[
H(F_d)\le(2+2c)I(F_d).
\tag{15}
\]

For (c=2), this is the constant six in (4).

## 4. Complete tree payment and terminal core

The complete signed node charge of any finite physical restriction tree
telescopes:

\[
\sum_{v\in\mathcal T^\circ}w_v
\left(U((F_d)_vh)-\frac{U((F_d)_{v,+}h)+U((F_d)_{v,-}h)}2\right)
=U(F_dh)-\sum_\ell w_\ell U((F_d)_\ell h).
\tag{16}
\]

Disjoint tensor additivity gives
(U((F_d)_vh)=U((F_d)_v)+U(h)), so the common terminal packet cancels
exactly once.  Since every leaf (U) is nonnegative,

\[
U(F_dh)-\sum_\ell w_\ell U((F_d)_\ell h)
=U(F_d)-\sum_\ell w_\ell U((F_d)_\ell)
\le U(F_d)\le cI(F_d),
\]

which proves (3).  No nodewise positivity or descendant closure is used.

## 5. Scope and remaining gap

The result is uniform in depth and rare terminal probability, and it permits
an arbitrary base satisfying the stated endpoint.  It therefore applies to
the preceding dense nullity-two shields with arbitrary coherent core and
physical orientation.  It still uses fresh disjoint variables, fair outer
selectors, and the fixed balancer mean (-1/2).  It does not cover biased
outer selectors, reused variables, balancer means approaching (\pm1), or
arbitrary overlapping changes of the coherent core between levels.

The tower family is not restriction-closed.  This theorem is a proper-class
retained-credit result, not a universal (U\le cI) estimate and not full FEI.
