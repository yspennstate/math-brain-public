# A quantitative cycle surplus for ML10 on Klein-group hosts

2 October 2026. Complete exact finite polynomial proof; historical novelty
unverified. The host family is restricted and the general ML10 Sidorenko
problem is not solved.

## Statement

Let G=(Z/2Z)^2 with uniform measure and let p_0,...,p_3>=0. Define
W(x,y)=4p_(x+y), and put s=sum_i p_i. The integral operator of W has
eigenvalues s,r_1,r_2,r_3, where the three centered eigenvalues are the
three nontrivial Fourier coefficients of p. Then

    t(ML10,W) >= s^15
                 +5 s^11 (r_1^4+r_2^4+r_3^4)
                 +14 s^9 (r_1^6+r_2^6+r_3^6).          (1)

Equivalently, since t(C_(2k),W)=s^(2k)+sum_i r_i^(2k),

    t(ML10,W) >= s^15
                 +5s^11 [t(C4,W)-s^4]
                 +14s^9 [t(C6,W)-s^6].                (2)

The leading fourth-cycle coefficient 5 is sharp. The sixth-cycle
coefficient 15, with that leading coefficient retained, is false even
within this four-state family. The proof certificate actually permits
replacing 14 by 8165/567; this is the largest constant certified by this
particular coefficientwise argument, not a claim about the true optimal
constant in (1).

This covers precisely the equal-measure, equal-diagonal, regular symmetric
four-state hosts. The row-sum proof of this description is in
`continuation_20261002_scope_and_prior_art.md`. It does not cover arbitrary
regular four-state hosts or general graphons.

## 1. Fourier expansion as a cycle-flow polynomial

For each character chi of G, put r_chi=sum_g p_g chi(g); r_0=s. Fourier
inversion gives

    W(x,y)=sum_chi r_chi chi(x)chi(y).

Expanding the fifteen edge factors and integrating the ten vertex labels
selects exactly those character edge labelings with product equal to the
trivial character at every vertex. These are G-valued flows on ML10. Since
G has characteristic two, every coordinate is a binary cycle vector.
ML10 is connected and has cycle rank 15-10+1=6, so it has 64 binary cycle
vectors and 64^2=4096 G-valued flows. Consequently

    t(ML10,W)=sum_(n0+n1+n2+n3=15) N_(n0,n1,n2,n3)
                         s^n0 r1^n1 r2^n2 r3^n3.      (3)

The exact cycle-space enumeration produces 73 nonzero monomials, with
integer coefficients summing to 4096. This is a third generator,
independent of the vertex-assignment generator and the sixteen-state
transfer generator of the earlier Schur-convexity theorem. Its entire
polynomial agrees exactly with the vertex generator after Fourier
inversion and the ordered substitution below.

For compact human inspection, here is (3) grouped under permutations of
the three nontrivial modes. A row means its coefficient times s^n0 times
the sum of distinct monomials with the displayed three exponents.

| n0 | Three mode exponents | Coefficient |
|---:|:---:|---:|
| 15 | (0,0,0) | 1 |
| 11 | (4,0,0) | 5 |
| 9 | (6,0,0) | 15 |
| 8 | (3,3,1) | 10 |
| 7 | (8,0,0) | 30 |
| 7 | (4,4,0) | 10 |
| 7 | (4,2,2) | 20 |
| 6 | (5,3,1) | 40 |
| 6 | (3,3,3) | 60 |
| 5 | (10,0,0) | 13 |
| 5 | (6,4,0) | 5 |
| 5 | (6,2,2) | 70 |
| 5 | (4,4,2) | 90 |
| 4 | (7,3,1) | 30 |
| 4 | (5,5,1) | 40 |
| 4 | (5,3,3) | 210 |
| 3 | (8,2,2) | 30 |
| 3 | (6,4,2) | 110 |
| 3 | (4,4,4) | 390 |
| 2 | (7,3,3) | 40 |
| 2 | (5,5,3) | 200 |
| 1 | (6,4,4) | 50 |
| 0 | (5,5,5) | 36 |

All three nontrivial exponents have the same parity in each monomial.
The first potentially negative term is therefore

    10s^8 r1 r2 r3 (r1^2r2^2+r1^2r3^2+r2^2r3^2).       (4)

This explicitly explains why nonnegative raw Fourier coefficients are
insufficient when centered eigenvalues can be negative.

## 2. Ordered nonnegative substitution

As proved in the previous Schur certificate, the density polynomial is
invariant under all permutations of p_0,...,p_3: affine permutations of
G are all of S4, and bipartiteness allows a translation on one source
part. The two cycle surpluses are also S4-invariant. On nontrivial Fourier
modes an affine permutation acts as a mode permutation and sign changes;
even powers remove those sign changes.

We may thus order p0>=p1>=p2>=p3 and uniquely write

    p0=A+B+C+D, p1=A+B+C, p2=A+B, p3=A,
    A,B,C,D>=0.

Then, up to a permutation of the three centered modes,

    s=4A+3B+2C+D,
    r1=B+2C+D, r2=B+D, r3=D-B.                        (5)

Let P(A,B,C,D) be the difference between the two sides of (1), obtained by
substituting (5) into the 73-term exact polynomial (3). Its exact expansion
has 760 nonzero coefficients, all positive integers. Therefore P>=0 on
the nonnegative orthant. Every nonnegative p has an ordered representative,
so this proves (1), including all boundary points and s=0.

The full positive coefficient list is the
`ordered_surplus_coefficients` field in
`continuation_20261002_klein4_cycle_surplus.json`. The accompanying script
reconstructs the binary cycle space, the entire Fourier polynomial, its
ordered expansion, and the positive surplus exactly with Python integers.
It additionally checks exact agreement with the vertex-enumeration
polynomial from the previous checkpoint. No approximation, eigenvalue
solver, or tolerance is used.

For the stronger sixth-cycle constant, define

    P4=F-s^15-5s^11 sum r_i^4,
    V6=s^9 sum r_i^6.

After (5), both have nonnegative coefficients. The least ratio
[monomial]P4 / [monomial]V6, over positive coefficients of V6, is exactly
8165/567, attained at A^6 B^8 D. Monomials absent from V6 have nonnegative
P4 coefficients. Thus coefficientwise subtraction also proves the
claimed stronger version of (1). This least-ratio assertion is checked
with exact Fraction arithmetic in the same script.

## 3. Sharpness of the fourth-cycle coefficient

Take s=1, r1=epsilon, r2=r3=0, with |epsilon|<=1. This corresponds to a
nonnegative two-state blow-up within the four-state family. Equation (3)
reduces to

    F=1+5epsilon^4+15epsilon^6+30epsilon^8+13epsilon^10.

Any fourth-cycle coefficient larger than 5, with any fixed sixth-cycle
coefficient, would contradict this expansion for sufficiently small
nonzero epsilon. Hence the leading 5 is optimal.

## 4. Exact obstruction to sixth-cycle coefficient 15

Set s=1 and r1=r2=r3=-1/100. The host is strictly positive, with

    (p0,p1,p2,p3)=(97/400,101/400,101/400,101/400).

Exact evaluation of (3) gives

    F=250000037511179426349533203741
       /250000000000000000000000000000.

The proposed coefficient-15 threshold is 1+15/100^4+45/100^6. The exact
difference is

    F-threshold15=-70573650466796259
       /250000000000000000000000000000 <0.

Thus retaining the sharp fourth-cycle coefficient and strengthening the
sixth-cycle coefficient to 15 is false. This is an obstruction to that
sharper inequality, not a counterexample to Sidorenko: the true density
is greater than one and obeys the proved coefficient-14 inequality.

## Source and novelty boundary

The earlier rank-one qualitative inequality follows from prior two-spin
Bethe bounds and is not claimed as new. Rossman's 2025 ladder transfer
identity is prior art and is credited in the companion Schur proof.
The exact Fourier flow expansion is the standard character expansion;
the present work applies it to give the explicit polynomial and positive
surplus certificate above. The existence of those general tools is not
claimed as a new theorem. A bounded primary search did not locate this
specific quantitative four-state statement, but historical novelty is
unverified. The unrestricted ten-vertex Möbius-ladder Sidorenko inequality
remains unproved here.
