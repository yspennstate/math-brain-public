# Adjacent terminal edges over a rank-one three-vertex core

2 October 2026. Complete analytic proof using seven explicit positive
polynomials. It is separate from the completed matching-vector negative-
association theorem. The preceding larger integer coefficient certificate
and its independent audit are retained as independent verification. This
shorter proof has its own exact identity verifier and is awaiting its
separate audit record. Historical novelty remains unverified.

## Theorem and its exact scope

Let the core have three vertices, with edge activities `p,q,r>=0`. Attach
terminals with rank-one spoke activities `a_j b_i`, where `a_j>=0` and
`b_i>=0`. Choose three terminals with row weights `a,b,c`, and add marked
edges `e=(a,b)` and `f=(b,c)` of arbitrary positive activities. On the
OTHER terminals one may add an arbitrary weighted graph, with arbitrary
nonnegative activities. There are no other terminal edges incident to the
three marked endpoints. Then e and f are negatively correlated under the
weighted forest measure. The inequality is strict if `a,c>0` and at least
one column factor is positive. No positivity assumption is needed for b.

The other-terminal graph can be unbounded and can have cycles, so this
scope is larger than a matching background. It does not cover arbitrary
terminal edges incident to marked endpoints, non-rank-one spokes, all
terminal-pair types, all forest indicators, or the full graph conjecture.

## 1. Exact core transfer and arbitrary background reduction

Use the five set partitions of the three core vertices as frontier states.
Adding one terminal of row x has exact transfer

    T(x)=d(x) I+x^2 P+x^3 Q,
    d(x)=1+Bx,
    B=b_1+b_2+b_3,

where P joins two distinct core blocks with coefficients `b_i b_j`, and Q
joins all three distinct core blocks with coefficient `b_1 b_2 b_3`. If
the initial core row is v, write

    J=b_1 b_2 b_3,
    S=v1=1+p+q+r+pq+pr+qr,
    L=vP1=b_1 b_2+b_1 b_3+b_2 b_3
       +p b_3(b_1+b_2)+q b_2(b_1+b_3)+r b_1(b_2+b_3).

Directly composing two joins gives

    P^2=2B Q,  PQ=QP=Q^2=0,  vQ1=J.

Thus, with

    alpha(x)=x^2/d(x),  gamma(x)=x^3/d(x)^2,

one has `T(x)=d(x) exp[alpha(x)P+gamma(x)Q]`. This is an identity of
polynomial operators; the exponential truncates after degree two.

Fix a forest H in the graph on the other terminals. Contract its tree
components. Parallel spokes sum exactly, so a contracted component C has
row weight `a_C=sum_(j in C)a_j`. Let

    D_H=product_C d(a_C),
    U_H=sum_C alpha(a_C),
    G_H=sum_C gamma(a_C).

The contribution of H, including its terminal-edge activity product w_H,
is the commuting operator

    w_H D_H exp[U_H P+G_H Q].

Only acyclic H occur: a terminal cycle would already be a cycle in the
full forest. Conversely, after contracting an acyclic H, the transfer
counts exactly the remaining allowed spoke/core forests. This gives a
term-by-term equality, not a comparison of two different forest models.

Set `D=sum_H w_H D_H>0`, and normalize these positive weights to a law nu.
Define

    U=E_nu U_H,
    Gamma=E_nu G_H+B Var_nu(U_H).

Expanding the truncated exponentials shows EXACTLY

    sum_H w_H D_H exp[U_H P+G_H Q]
       =D exp[U P+Gamma Q].                         (1)

Both U and Gamma are nonnegative. The variance term is retained. No upper
bound such as `Gamma<=U/B` is asserted or required here. Equation (1) is
valid for an arbitrary finite graph on arbitrarily many other terminals.

## 2. Four exact marked-edge coefficients

After absorbing the normalized background, put

    F=S+L U+J Gamma+BJ U^2,
    M=L+2BJ U.

For a list of cluster row weights x_1,...,x_k, define the polynomial

    C(x_1,...,x_k)
       =F product_i d(x_i)
        +M sum_i x_i^2 product_(j!=i)d(x_j)
        +J sum_i x_i^3 product_(j!=i)d(x_j)
        +2BJ sum_(i<j) x_i^2 x_j^2 product_(l!=i,j)d(x_l).
                                                               (2)

This is the expansion of `v exp[UP+Gamma Q] product_i T(x_i) 1`.
Deletion/contraction of the marked edges gives the four coefficients
of their multi-affine partition polynomial:

    A   =D C(a,b,c),
    B_e =D C(a+b,c),
    B_f =D C(a,b+c),
    C_ef=D C(a+b+c).                                  (3)

The common-endpoint edge pair does not create a terminal cycle, and
contraction sums the corresponding row weights exactly. Therefore its
Rayleigh difference is

    B_e B_f-A C_ef
       =D^2 [C(a+b,c) C(a,b+c)-C(a,b,c) C(a+b+c)].      (4)

It remains to prove the sign of ONE fixed polynomial, independent of the
number, topology, or activities of the other-terminal graph.

## 3. Two scalar bounds

Suppose B>0. The primitive core quantities satisfy

    BL>=9J,
    B^2 S-2L>0.                                      (5)

For the first, `L>=b_1b_2+b_1b_3+b_2b_3`, and expanding
`B(b_1b_2+b_1b_3+b_2b_3)` gives `3J` plus the six symmetric monomials
`b_i^2 b_j`. Their sum is at least `6J` by AMGM. This also holds when
some column factors are zero by continuity.

For the second, put `H=b_1^2+b_2^2+b_3^2>0`. Exact expansion gives

    B^2S-2L
      =H+p(H+2b_1b_2)+q(H+2b_1b_3)+r(H+2b_2b_3)
        +B^2(pq+pr+qr)>0.

Since U,Gamma are nonnegative, (5) implies

    BM>=9J,
    B^2F-2M
      =(B^2S-2L)+B(BL-4J)U+B^2J Gamma+B^3J U^2>0.    (6)

Thus all dependence on the arbitrary background has been reduced to two
scalar inequalities. No finite-size restriction or upper bound on Gamma
is used.

## 4. Seven positive polynomials give the adjacent Rayleigh inequality

This section proves a general scalar lemma: the expression in brackets
in (4), with C given by (2), is nonnegative whenever `F>0,B>0,M,J>=0`,
`B^2F>=2M`, and `BM>=9J`.

Normalize the rows and parameters by

    x=Ba, y=Bb, z=Bc,
    u=2M/(B^2F),  v=9J/(BM),
    s=x+z, t=xz.                                      (7)

When M=0, the second hypothesis forces J=0; set u=v=0. Otherwise both
u and v belong to [0,1]. Define the degree-two Bernstein basis

    beta_0(w)=(1-w)^2,
    beta_1(w)=2w(1-w),
    beta_2(w)=w^2.

Let R denote the bracket in (4). The exact polynomial identity is

    R=F^2 xz sum_(i,j=0)^2 beta_i(u) beta_j(v) Q_ij(s,t,y).   (8)

Here the nine Q polynomials have only seven distinct values. The following
is the complete list, grouped by powers of y. Every displayed coefficient
is nonnegative:

    Q_00=Q_01=Q_02=1+s+t.

    4 Q_10
      =2+3s+2s^2+2st
       +2y(1+s+t).

    72 Q_11
      =36+51s+34s^2+30st+2s^3+2s^2t
       +y(30+34s+4s^2+30t+4st)
       +2y^2(s+t).

    18 Q_12
      =9+12s+8s^2+6st+s^3+s^2t
       +y(6+8s+2s^2+6t+2st)
       +y^2(s+t).

    4 Q_20
      =2s+2s^2+s^3+s^2t
       +y(4+4s+2s^2+2st)
       +y^2(2+s+t).

    72 Q_21
      =30s+32s^2+17s^3+2s^4+12s^2t+2s^3t
       +y(60+68s+38s^2+6s^3+24st+6s^2t)
       +y^2(36+25s+6s^2+12t+6st)
       +y^3(4+2s+2t).

    324 Q_22
      =108s+126s^2+72s^3+15s^4+s^5+36s^2t+12s^3t+s^4t
       +y(216+288s+180s^2+48s^3+4s^4+72st+36s^2t+4s^3t)
       +y^2(162+144s+54s^2+6s^3+36t+36st+6s^2t)
       +y^3(36+24s+4s^2+12t+4st)
       +y^4(3+s+t).

For an elementary check of (8), divide each C expression by F and replace
`B a,B b,B c` by x,y,z. Each factor d becomes `1+x`, the normalized M
coefficient becomes `u/2`, and the normalized J coefficient becomes
`uv/18`. Form the four C expressions in (4) and expand their two products.
Since the result has degree at most two in each of u,v, its tensor-product
Bernstein coefficients are determined by these products. They are exactly
the seven displayed Q polynomials after the substitutions `s=x+z,t=xz`.
This is an identity of polynomials, with no inequality or numerical
approximation in the calculation.

All beta and Q factors on the right of (8) are nonnegative, proving the
scalar lemma. In the forest application (6) gives u<1. Since
`sum_j beta_j(v)=1`, the i=0 terms alone contribute

    F^2 xz (1-u)^2 (1+s+t).

This is strictly positive when a,c>0. If B=0, all spokes vanish, the marked
two-edge path is a separate acyclic component, and its two edge indicators
are independent. If either outer row vanishes, its marked edge is a bridge
and independent; the inequality is again equality. Equations (1)-(8)
prove the theorem for all allowed cases.

## 5. Exact checks and limitations

`forest_adjacent_terminal_core3_bernstein_exact.py` checks (8) as an exact
Fraction polynomial identity in x,y,z,u,v, using the seven integer
numerator lists above. Its report is
`forest_adjacent_terminal_core3_bernstein_exact_results.json`. It is a
finite identity verification, not checking numerical inputs.

The earlier independent route is the full 11,063-term positive integer
expansion in primitive column/core variables, recorded in
`forest_adjacent_terminal_core3_coefficient_certificate.json` and generated
by `forest_adjacent_terminal_core3_coefficient_certificate.py`. Its complete
coefficient-list identity and positivity have already received an
independent adversarial PASS. That larger certificate is not needed to
read or use the seven-polynomial proof above.

The same script separately enumerates the literal forest subsets of four
different other-terminal graphs, contracts their clusters, and propagates
the actual eight choices of each three-spoke star through five frontier
states. It checks all four coefficients against (3) and the Rayleigh
difference against (4). The cases include a cyclic triangle background,
nonuniform rational columns, a zero middle row, a longer background with
extra chords, and small row weights. These checks are recorded in
`forest_adjacent_terminal_core3_exact_results.json`; they are secondary
sanity checks, not the positive-coefficient proof.

Full negative association is not inferred from this pairwise theorem, and
interactions of other terminal edges with the marked three endpoints
remain outside the theorem. Historical novelty, including overlap with
known series-parallel or small-graph SOS results, is unverified.
