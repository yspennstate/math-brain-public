# Adjacent terminal edges over a rank-one three-vertex core

2 October 2026. This is a new finite exact polynomial-certificate proof,
pending independent audit. It is separate from the completed matching-vector
negative-association theorem. Historical novelty remains unverified.

## Candidate theorem and its exact scope

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

## 3. Complete exact positive-coefficient certificate

Let R denote the bracket in (4). Substitute the displayed primitive
expressions for B,J,S,L into (2), leaving U and Gamma as independent
nonnegative indeterminates. Expand in the ordered variables

    a,b,c,b_1,b_2,b_3,p,q,r,U,Gamma.

The resulting integer polynomial has exactly 11,063 nonzero monomials,
ALL with positive integer coefficients. The complete sorted coefficient
list is `forest_adjacent_terminal_core3_coefficient_certificate.json`.
It is generated and checked by the independent-of-third-party-algebra
script `forest_adjacent_terminal_core3_coefficient_certificate.py`.
Its coefficient inventory is:

| U degree | Gamma degree | Positive monomials | Minimum coefficient |
|---:|---:|---:|---:|
| 0 | 0 | 4,656 | 1 |
| 1 | 0 | 3,140 | 2 |
| 0 | 1 | 740 | 2 |
| 2 | 0 | 1,528 | 1 |
| 1 | 1 | 335 | 2 |
| 3 | 0 | 477 | 2 |
| 0 | 2 | 41 | 1 |
| 2 | 1 | 61 | 2 |
| 4 | 0 | 85 | 1 |

For reproducibility the script uses only the following elementary exact
rules, with exponent vectors k,l and integer coefficients:

    coefficient_k(P+Q)=coefficient_k(P)+coefficient_k(Q),
    coefficient_k(PQ)=sum_(l+m=k) coefficient_l(P) coefficient_m(Q).

It constructs C by (2), constructs R by the subtraction in (4), collects
all identical exponent vectors, and checks every resulting integer.
Thus this is a finite symbolic sign certificate, rather than testing R
on finitely many numerical inputs. The certificate can be checked without
regenerating any forest on the arbitrarily large background graph.

Every monomial is divisible by `ac`; the monomial `a c b_1^2` has coefficient
one. By symmetry the analogous b_2,b_3 monomials do as well. Therefore R is
nonnegative for all the allowed primitive variables and is strictly
positive when `a,c>0` and some column factor is positive. Equations (1)-(4)
prove the candidate theorem, subject to an independent audit of this exact
polynomial certificate and the reductions above.

## 4. Independent sanity-check route and limitations

The same script separately enumerates the literal forest subsets of four
different other-terminal graphs, contracts their clusters, and propagates
the actual eight choices of each three-spoke star through five frontier
states. It checks all four coefficients against (3) and the Rayleigh
difference against (4). The cases include a cyclic triangle background,
nonuniform rational columns, a zero middle row, a longer background with
extra chords, and small row weights. These checks are recorded in
`forest_adjacent_terminal_core3_exact_results.json`; they are secondary
sanity checks, not the positive-coefficient proof.

The exact proof is substantially larger than the scalar matching-pair
certificate. A shorter positive factorization is still desirable. Full
negative association is not inferred from this pairwise theorem, and
interactions of other terminal edges with the marked three endpoints
remain outside the theorem. Historical novelty, including overlap with
known series-parallel or small-graph SOS results, is unverified.
