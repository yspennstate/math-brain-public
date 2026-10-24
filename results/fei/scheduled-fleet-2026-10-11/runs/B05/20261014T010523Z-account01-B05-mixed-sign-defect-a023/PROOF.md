# Mixed-sign point-defect towers with a quantitative reserve

All logarithms are base two.  For a Boolean sign (f), write

\[
U(f)=\sum_S\widehat f(S)^2\log_2
\frac{\sum_{T\supseteq S}\widehat f(T)^2}{\widehat f(S)^2},
\qquad I(f)=\sum_S|S|\widehat f(S)^2.
\]

Let (Q_r) equal (+1) except at one vertex of the (r)-cube.  Put
(\beta_r=\mathbb E Q_r=1-2^{1-r}).  Let

\[
A(q)(z,x)=\begin{cases}1,&z=+1,\\q(x),&z=-1.\end{cases}
\]

All blocks below are physically disjoint.

## Theorem

For an arbitrary Boolean base (P), a fresh balanced character (w), any
ranks (r_k\ge2), and any signs (\sigma_k\in\{-1,+1\}), define

\[
F_1=A(wP),\qquad
F_k=A(\sigma_k Q_{r_k}F_{k-1})\quad(k\ge2).
\tag{1}
\]

Then

\[
U(P)\le\frac83I(P)
\quad\Longrightarrow\quad
\boxed{U(F_d)\le\frac83I(F_d)}
\tag{2}
\]

for every finite depth, sign sequence, and rank sequence.  Moreover, for any
finite adaptive/pruned restriction tree on the physical variables of (F_d)
and every one common Boolean terminal factor (h) on a disjoint block,

\[
\boxed{
U(F_dh)-\sum_\ell w_\ell U((F_d)_\ell h)
\le\frac83I(F_d).}
\tag{3}
\]

## Exact recurrence

The accepted half-activation identities are

\[
U(A(q))=\frac12U(q)+R(\mathbb E q),
\qquad
I(A(q))=\frac12I(q)+\frac{1-\mathbb E q}{2}.
\tag{4}

The point-defect spectrum gives

\[
I(Q_r)=2r2^{-r},qquad
U(Q_r)=\beta_r^2\log_2(1/\beta_r^2)+2r2^{-r}\beta_r,
\tag{5}

and the reviewed bound

\[
U(Q_r)\le2I(Q_r)\qquad(r\ge2).
\tag{6}

Negating a Boolean function changes no squared Fourier coefficient, so (5)
and (6) also hold for (-Q_r).

Let (m_k=\mathbb E F_k) and, at level (k\ge2), put

\[
t_k=\sigma_k\beta_{r_k}m_{k-1}.
\]

Since (m_1=1/2) and

\[
m_k=\frac{1+t_k}{2},
\tag{7}

induction gives (0\le m_k\le1), hence (t_k\in[-1,1]).  Disjoint tensor
additivity and (4) give the exact recurrences

\[
\begin{aligned}
U(F_k)&=\frac12U(F_{k-1})+\frac12U(Q_{r_k})+R(t_k),\\
I(F_k)&=\frac12I(F_{k-1})+\frac12I(Q_{r_k})+\frac{1-t_k}{2}.
\end{aligned}
\tag{8}

## One scalar inequality for both signs

The independently reviewed positive-side estimate is

\[
R(t)\le\frac43(1-t)\qquad(0\le t\le1).
\tag{9}

The independently reviewed negative-side estimate is

\[
R(t)\le1\qquad(-1\le t\le0).
\tag{10}

At (c=8/3), (10) yields the strict reserve

\[
\frac c2(1-t)-R(t)
\ge\frac43(1-t)-1\ge\frac13
\qquad(-1\le t\le0).
\tag{11}

Thus sign changes cost nothing: positive nodes use (9), while every negative
node creates at least (1/3) of new endpoint slack.

## Endpoint induction and quantitative reserve

Put (D_k=cI(F_k)-U(F_k)), (c=8/3), and
(\epsilon_k=1_{\{\sigma_k=-1\}}).  The balanced first level gives

\[
D_1=c-1+\frac12(cI(P)-U(P))\ge\frac53.
\tag{12}

From (6), (8), (9), and (11),

\[
D_k\ge\frac12D_{k-1}+\frac13\epsilon_k.
\tag{13}

Consequently

\[
\boxed{
D_d\ge2^{-(d-1)}D_1+rac13
\sum_{k=2}^d2^{-(d-k)}\epsilon_k.}
\tag{14}

In particular (D_d\ge0), proving (2).  Formula (14) records the exact
discounted reserve created by all negative levels rather than discarding it.
The standard bridge (H\le2I+2U) gives

\[
H(F_d)\le\frac{22}{3}I(F_d).
\tag{15}

## Tree loss

For any finite adaptive/pruned physical restriction tree,

\[
\sum_{v\in T^\circ}w_v\left[U((F_d)_vh)-
\frac{U((F_d)_{v,+}h)+U((F_d)_{v,-}h)}2\right]
=U(F_dh)-\sum_\ell w_\ell U((F_d)_\ell h).
\tag{16}

Because the same disjoint (h) appears everywhere, tensor additivity
cancels (U(h)) exactly.  Leaf (U\) is nonnegative, so the loss is at most
(U(F_d)\), proving (3).  In fact the unused tree budget is at least the
right side of (14), plus the nonnegative average leaf (U).

## Scope

This theorem removes sign-homogeneity from the arbitrary-rank point-defect
family.  Its constant is independent of dimension, depth, rank, defect
rarity, sign changes, reveal order, pruning, and the common disjoint terminal
core.  It still assumes fresh disjoint defect blocks, fair outer selectors,
and one common disjoint terminal factor.  The proof is an endpoint signed
telescope, not an ownership proof for the individual
(\mu[\log_2(1/\mu)-D_2(\nu\|q)]) credits.  Changing, overlapping, or
leaf-dependent cores remain open.

