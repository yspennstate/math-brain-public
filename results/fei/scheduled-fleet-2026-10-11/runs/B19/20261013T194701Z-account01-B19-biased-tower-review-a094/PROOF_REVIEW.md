# Independent proof reconstruction

All logarithms are base two. This document independently reconstructs the
three claims in B05's `B05_A023_BIASED_TOWER_*_v1` package. It does not use the
author's numerical implementation.

## 1. Objects and quantifiers

For a Boolean sign `f`, put

\[
U(f)=\sum_S \widehat f(S)^2\log_2
 \frac{\sum_{T\supseteq S}\widehat f(T)^2}{\widehat f(S)^2},
\qquad
I(f)=\sum_S |S|\widehat f(S)^2.
\]

Let

\[
A(q)(z,x)=\begin{cases}1,&z=+1,\\q(x),&z=-1,\end{cases}
\qquad B=(-1,-1,-1,1),\qquad \mathbb EB=-\frac12.
\]

All variables used below are fresh and disjoint. For a Boolean base `P` and a
fresh fair character `w`, define

\[
F_1=A(wP),\qquad F_k=A(B_kF_{k-1})\quad(k\ge2).
\]

The reviewed claim is: if `c >= 48/35` and `U(P) <= c I(P)`, then
`U(F_d) <= c I(F_d)` for every finite depth `d`. The restriction-tree extension
queries only physical variables of `F_d` and uses one common Boolean terminal
core `h` on a disjoint block.

## 2. Activation identity

Writing `t=E q`, the Fourier expansion

\[
A(q)=\frac{1+q}{2}+z\frac{1-q}{2}
\]

splits every nonconstant coefficient of `q` into two equal squared masses and
leaves the two scalar coefficients `(1+t)/2` and `(1-t)/2`. Directly summing the
upper-set caps yields

\[
U(A(q))=\frac12 U(q)+R(t),
\]

where

\[
R(t)=E(t)-\frac12t^2\log_2(1/t^2)+\frac14(1-t^2)
\]

and

\[
E(t)=\frac{(1+t)^2}{4}\log_2\frac4{(1+t)^2}
+\frac{(1-t)^2}{4}\log_2\frac2{1-t}.
\]

The selector influence is `(1-t)/2`, while each old influence is halved.
Disjoint products add both `U` and `I`; multiplication by a fresh character
preserves `U` and adds one to `I`.

## 3. One-sided scalar lemma

For `-1<t<0`, differentiation gives

\[
R''(t)=1+\frac{\ln\!\left(t^2/((1+t)\sqrt{1-t})\right)+3/4}{\ln2},
\]

\[
R'''(t)=\frac{4-t-t^2}{2\ln2\,t(1-t^2)}<0.
\]

Thus `R''` strictly decreases from positive infinity to negative infinity and
has one zero. Also

\[
R'(-1+)=\frac{\ln2-1}{2\ln2}<0,
\qquad
R'(0-)=\frac12-\frac1{4\ln2}>0.
\]

Consequently `R'` increases and then decreases, crosses zero exactly once,
and is still positive at the right endpoint. Hence `R` first decreases and
then increases. Since `R(-1)=0` and `R(0)=1`,

\[
\boxed{R(t)\le1\quad(-1\le t\le0).}
\]

This proves the scalar claim analytically; the finite grid in
`INDEPENDENT_CHECK.py` is only a diagnostic.

## 4. Endpoint recurrence

Let `m_k=E F_k`. The identities above give

\[
\begin{aligned}
m_1&=\frac12,& U(F_1)&=1+\frac12U(P),& I(F_1)&=1+\frac12I(P),\\
m_k&=\frac12-\frac14m_{k-1},&
U(F_k)&=\frac12U(F_{k-1})+\frac12+R(-m_{k-1}/2),&
I(F_k)&=\frac12I(F_{k-1})+1+\frac14m_{k-1}.
\end{aligned}
\]

Induction puts `m_k` in `[3/8,1/2]`. For `c>=1`, the first level satisfies

\[
U(F_1)-cI(F_1)
=\frac12(U(P)-cI(P))+1-c\le0.
\]

At later levels, the scalar lemma and `m_{k-1}>=3/8` imply

\[
U(F_k)-cI(F_k)
\le\frac12(U(F_{k-1})-cI(F_{k-1}))
+\frac32-\frac{35}{32}c.
\]

The last term is nonpositive for `c>=48/35`, completing the induction. This
constant is a valid sufficient threshold; neither the source nor this review
establishes its optimality.

## 5. Restriction-tree payment

For any finite adaptive or pruned tree, the signed node increments telescope:

\[
\sum_{v\text{ internal}}w_v
\left(U((F_d)_vh)-\tfrac12U((F_d)_{v,+}h)
-\tfrac12U((F_d)_{v,-}h)\right)
=U(F_dh)-\sum_\ell w_\ell U((F_d)_\ell h).
\]

Because the same disjoint `h` occurs at every node, tensor additivity cancels
its `U(h)` exactly. Nonnegativity of leaf `U` then gives

\[
U(F_dh)-\sum_\ell w_\ell U((F_d)_\ell h)
\le U(F_d)\le cI(F_d).
\]

This is an endpoint telescope. It does **not** prove nonnegative node charges,
single-use ownership at each node, descendant closure, or a bound for
leaf-dependent, shared-variable, or changing terminal cores.

## 6. Corollary and scope

The previously independently accepted dense nullity-two shield theorem gives
`U(P)<=2I(P)`, so the tower result applies with `c=2`. The generic bridge
`H<=2I+2U` yields `H(F_d)<=6I(F_d)`.

The result is uniform in tower depth and terminal activation probability and
allows arbitrary coherent cores only through the accepted shield base. It
still requires fair selectors, fresh disjoint blocks, a fixed balancer of mean
`-1/2`, and a common disjoint terminal core. Positive-depth towers are not
restriction-closed: with `P=1`, restricting the fresh character in `F_1` to
`-1` leaves a selector dictator with `(U,I)=(0,1)`, not another positive-depth
tower of the displayed form.

## Verdict

The scalar lemma, endpoint theorem, and common-core tree-payment theorem are
**INDEPENDENTLY ACCEPTED AT THEIR DECLARED SCOPE**. They are a new proper-class
bridge for `A023`; they do not resolve the arbitrary changing-core hierarchy,
the universal upper-set asymmetry mismatch, or full FEI.
