# Finite-activity two-port Ward reduction and its unresolved sign

Research continuation, 2 October 2026. This is an exact reformulation and a
record of a failed route to the full weighted forest conjecture. It does not
extend the already proved high-fugacity theorem to all activities.

## 1. Two-port forest connectivity odds

Let H be a finite graph with distinct designated vertices a,b. Write

\[
 X_H=\sum_{F:\,a\leftrightarrow b}\prod_{g\in F}z_g,
 \qquad
 Y_H=\sum_{F:\,a\not\leftrightarrow b}\prod_{g\in F}z_g,
 \qquad r_H=X_H/Y_H.
\]

Both sums are over acyclic edge sets; `Y_H>0` because it includes the empty
forest. If another graph K shares exactly a,b with H and has disjoint edges,
a forest of H and a forest of K have acyclic union exactly when they do not
both connect a to b. Thus

\[
 Z_{H\cup K}=Y_HY_K+X_HY_K+Y_HX_K
           =Y_HY_K(1+r_H+r_K).                         \tag{1}
\]

For a marked e in H and f in K, differentiating exactly gives

\[
 \partial_{ef}\log Z_{H\cup K}
   =-\frac{(\partial_e r_H)(\partial_f r_K)}
              {(1+r_H+r_K)^2},
\]

and hence

\[
 R_{ef}(H\cup K)
   =Y_H^2Y_K^2(\partial_e r_H)(\partial_f r_K).        \tag{2}
\]

This is an exact finite-activity identity, not a leading-coefficient
calculation. Positivity of both local responses would prove the cross-pair
inequality across that two-vertex interface.

However the required local response inequality is already equivalent to the
full conjecture. Add a new edge g=ab of activity w to H, allowing a parallel
edge if one already exists. Its partition is

\[
 Z_{H+g}=X_H+Y_H+wY_H=Y_H(1+w+r_H).
\]

For every original e,

\[
 R_{eg}(H+g)=Y_H^2\partial_e r_H.                    \tag{3}
\]

Conversely every marked pair in every graph is of this form after deleting
one marked edge and using its endpoints as the two designated vertices.
Thus proving `partial_e r_H>=0` for all two-port graphs is precisely another
version of the all-fugacity forest pair conjecture. It is not an available
monotonicity theorem that may be inserted into (2).

## 2. Exact finite-t Ward classification

The two-port reduction can also be recovered from the Grassmann route. In
this section assume H is connected; disconnected factors can be removed
first, and if a,b lie in different components then X_H is zero.
Let all port fields be free and put

\[
 F_{ab}(t)=q(\psi_a-\psi_b)-tq_aq_b,
 \qquad q_i=\bar\psi_i\psi_i.
\]

Integrate the raw local action over all nonport vertices, with vertex factors
`1+t q_i` and deformed edge action `z_xy F_xy(t)`. The result is an even,
charge-balanced polynomial in the four port generators. It is annihilated
by both two-port deformed Ward operators.

The charge-balanced degree-two part has a 2-by-2 coefficient matrix. At t=0
the two ordinary translation Ward equations force its row and column sums
to vanish, so it is a scalar multiple of `q(psi_a-psi_b)`. The only
degree-four balanced monomial is `q_aq_b`; the deformed Ward equation fixes
its coefficient to minus t times that degree-two scalar. Solving these
equations over formal coefficient series therefore gives exactly

\[
 I_H(t)=A_H(t)+B_H(t)F_{ab}(t).                        \tag{4}
\]

There are no further invariant balanced port terms. Also `F_ab(t)^2=0`,
because its quadratic term has rank one and its product with the degree-four
term has degree six in only four generators.

The combinatorial identifications, including powers of t, are

\[
 A_H(t)=\sum_{a\not\leftrightarrow b}z^F t^{k(F)-2},
 \qquad
 B_H(t)=\sum_{a\leftrightarrow b}z^F t^{k(F)-1}.       \tag{5}
\]

One way to verify (5) is to set both port fields to zero. The all-minors
rooted-forest expansion requires distinct roots a,b. Every component without
a port contributes its Euler feature count one; a one-port component has
no free root choice. This gives the separated-forest sum A. Next ground b,
multiply the remaining port measure by `1+t q_a`, and integrate a. The
result is `t A+B`, which is the full forest sum with weight
`z^F t^(k(F)-1)`. Subtracting the separated contribution identifies B.
At t=1, (4) is therefore exactly

\[
 I_H(1)=Y_H+X_HF_{ab}(1).                             \tag{6}
\]

For an arbitrary marked edge e, the raw marked logarithmic score is

\[
 \partial_e\log I_H(t)
 =\partial_e\log A_H(t)
   +\partial_e\!\left(B_H(t)/A_H(t)\right)F_{ab}(t). \tag{7}
\]

If the original electrical current of e is compactly supported in the local
interior, its Schur derivative is zero, so the normalized local score differs
from (7) only by a boundary-independent determinant derivative. In that
setting (7) is the exact finite-t continuation of the delayed leading
response used in the high-fugacity proof.

The missing sign is now completely explicit: the coefficient of `F_ab(1)`
is `partial_e(X_H/Y_H)`. Ward symmetry classifies the score but does not
establish its nonnegative sign. At more than two ports, further invariant
terms survive, so the two-port classification does not automatically extend
to the arbitrary separator appearing in the high-fugacity induction.

## 3. A positive diagonal-root determinant representation is impossible

A tempting way to replace the formal Grassmann tilt by a positive integral
would be to find a fixed positive measure mu on vertex root weights s such
that, for K4 and all its edge activities,

\[
 Z_{K_4}(z)=\int \det(L_{K_4}(z)+\operatorname{diag}s)\,d\mu(s).
                                                               \tag{8}
\]

The matrix-forest expansion would give each unrooted forest F coefficient
`integral product_(components C) sum_(i in C) s_i dmu`. Since each coefficient
of Z is one, this representation is impossible even without requiring mu
to be a probability measure or invariant under vertex permutations.

Indeed set `M_ij=integral s_i s_j dmu`. A two-edge tree on three vertices,
plus its isolated fourth vertex l, requires

\[
 \sum_{j\ne l}M_{lj}=1\quad(l=1,2,3,4).
\]

Summing gives `sum_(i<j) M_ij=2`. A forest consisting of two disjoint edges
requires the cross-block sum to equal one for each of the three 2+2
partitions. Summing those three equalities counts every M_ij twice and gives
`sum_(i<j) M_ij=3/2`, a contradiction.

Positivity ensures that all these moments are well-defined and finite once
the required finite coefficient sums are imposed. This rules out (8) for
any positive root-weight measure independent of the edge activities. It does
not rule out other positive field representations, or measures depending on
the activities; the latter would require control of their marked derivatives
and would not yield a Rayleigh proof simply by averaging determinants.

## 4. Frontier and prior-art boundary

Equations (1)--(3) expose the exact finite-activity scalar response needed
for the two-port route. Equations (4)--(7) establish that the Ward route gives
the same response, rather than a new unproved positivity principle. The
determinant-mixture contradiction rules out one natural attempt to supply
such a principle. No all-fugacity sign theorem has been obtained from this
route.

Two-sum preservation of the forest I-Rayleigh property and all-fugacity
series-parallel results are established prior work, so these identities and
their restricted applications must not be represented as new resolutions.
Primary sources checked in this continuation:

* David G. Wagner, *Negatively correlated random variables and Mason's
  conjecture*, https://arxiv.org/abs/math/0602648 (2006).
* Alejandro Erickson, *Sums of squares and negative correlation for spanning
  forests of series parallel graphs*,
  https://arxiv.org/html/1008.3660v3 (2011 revision; published 2012).

The strongest completed statement here is the exact reformulation and the
specified positive-integral obstruction. The full conjecture remains open
in this continuation.
