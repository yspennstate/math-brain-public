# ML10 has a cycle surplus on every regular symmetric three-state host

2 October 2026. Complete exact finite polynomial proof, with a separate
root-free nine-state transfer regenerator. Separate-agent review is
requested. Historical novelty is unverified. This does not solve the
unrestricted ML10 Sidorenko problem.

## Statement and precise scope

Let W be a nonnegative symmetric three-by-three kernel on three atoms of
equal measure1/3. Assume its three row sums are equal, and let s be its
edge density. Then

    t(ML10,W) >= s^15
       +5s^11 [t(C4,W)-s^4]
       +(265/18)s^9 [t(C6,W)-s^6].                    (1)

Equivalently, if r1,r2 are the two centered operator eigenvalues,

    t(ML10,W) >= s^15+5s^11(r1^4+r2^4)
                       +(265/18)s^9(r1^6+r2^6).      (2)

This implies Sidorenko, with equality only for the constant kernel. The
fourth-cycle coefficient5 is sharp. The sixth-cycle coefficient15 is
false when that sharp leading coefficient is retained, even for a
strictly positive three-state host. The number265/18 is the largest
sixth-cycle coefficient certified by the particular ordered polynomial
argument below, not a claim about the true optimum.

Unlike the companion four-state theorem, this statement imposes no
equal-diagonal condition. Equal atom measures and regularity remain
essential scope restrictions. Unequal atom measures, arbitrary
nonregular three-state hosts, larger hosts and general graphons are not
covered. Equal-measure graphon blow-ups preserve the result.

## 1. An exact two-cone decomposition of the host domain

Put P=W/3. Its row sum is s. Let its off-diagonal entries be
a=P01,b=P02,c=P12. Then its diagonal entries are

    P00=s-a-b, P11=s-a-c, P22=s-b-c.

Let S01,S02,S12 be the three transposition permutation matrices. Define
alpha=s-a-b-c. Directly,

    P=alpha I+aS01+bS02+cS12.                         (3)

If alpha>=0, all four coefficients are nonnegative: this is cone I.
If alpha<0, put u=-alpha=a+b+c-s>0. Nonnegativity of the three diagonal
entries gives a-u>=0,b-u>=0,c-u>=0. Since

    I+K3=S01+S02+S12,

where K3 is the unweighted loopless complete-graph adjacency matrix,
equation(3) can instead be written

    P=uK3+(a-u)S01+(b-u)S02+(c-u)S12.                 (4)

This is cone T. Thus every nonnegative symmetric regular three-state
host lies in one of two nonnegative four-generator cones. No polytope
classification theorem is needed; equations(3)-(4) prove coverage.

State relabeling permutes the three transpositions arbitrarily and
preserves the homomorphism density and cycle densities. We may order
their three coefficients. The following nonnegative coordinates cover
the cones:

    I: P=D I+(A+B+C)S01+(A+B)S02+A S12;
       A,B,C,D>=0, s=3A+2B+C+D.

    T: P=D K3+2(A+B+C)S01+2(A+B)S02+2A S12;
       A,B,C,D>=0, s=6A+4B+2C+2D.                    (5)

The factor2 in the second parametrization only clears denominators and
does not restrict its coverage. In(4), choose D=u and use half of the
three transposition coefficients in(5).

## 2. Exact full density polynomials and normalization

Let H=ML10, with edges between left i and right j when
j-i in{0,1,-1} mod5. It has ten vertices and fifteen edges. Since
W=3P and atom measures are1/3,

    F=t(H,W)=3^5 hom(H,P).                            (6)

Every one of the3^10=59049 vertex assignments is enumerated. Counting the
six possible unordered endpoint-state types produces a finite histogram.
Substitution of the entries of P from(5), followed by exact integer
binomial expansion, gives each entire degree-fifteen density polynomial.
The two row-sum fifteenth powers are subtracted exactly. In each cone
the unrefined gap F-s^15 has790 nonzero positive coefficients.

All root labels are included. An earlier invalid scratch calculation
fixed one root label and multiplied by3, which regularity does not
justify. That abandoned calculation and the analytic check that caught
it are explicitly preserved in
`continuation_20261002_regular3_exploratory_erratum.md` and its historical
reproducer. No assertion here uses those invalid files. The valid
regenerator is `continuation_20261002_regular3_full_enumeration.py` and
its separate full-enumeration JSON.

## 3. Cycle excesses in the cone coordinates

On the two-dimensional centered subspace a transposition is a reflection,
the three reflections sum to zero, and K3 acts as minus the identity.
For coefficients beta,gamma,delta the reflection sum has squared
eigenvalue

    r^2=beta^2+gamma^2+delta^2-beta gamma-beta delta-gamma delta.

This also follows by directly computing the trace and determinant of the
centered two-dimensional restriction. Set R=B^2+BC+C^2. In cone I the
centered eigenvalues are D plus/minus sqrt(R), and in cone T they are
-D plus/minus2sqrt(R). Thus, with q=R in cone I and q=4R in cone T,

    E4=t(C4,W)-s^4=2D^4+12D^2 q+2q^2,
    E6=t(C6,W)-s^6=2D^6+30D^4 q+30D^2 q^2+2q^3.       (7)

The sign of the common termD in the two eigenvalues is immaterial for
these even moments. Both expressions have nonnegative integer
coefficients. The transfer audit independently verifies them by direct
three-by-three polynomial matrix powers, without this eigenvalue
derivation.

## 4. The quantitative positive-coefficient certificate

Form the homogeneous polynomial

    L=18(F-s^15)-90s^11 E4-265s^9 E6.                 (8)

After(5) and(7), every coefficient of L is a nonnegative integer. Cone I
has744 nonzero positive coefficients; cone T has741. Since A,B,C,D>=0,
L>=0 in both cones. Equations(3)-(5) cover the complete stated domain,
so(8) proves(1), including all boundary points and the zero kernel.

The full coefficient lists are the `integer_scaled_surplus_coefficients`
fields in `continuation_20261002_regular3_cycle_surplus.json`. The
reproducer constructs both E4 and E6 exactly, subtracts(8), and checks
each coefficient without tolerances or floating-point arithmetic.

The ratio description gives an additional check: in each cone all
coefficients of F-s^15-5s^11 E4 are nonnegative. Among monomials with a
positive coefficient in s^9E6, the smallest ratio is exactly265/18. In
cone I it occurs at A^7B^6CD; in cone T at A^7CD^7. Monomials absent
from s^9E6 have nonnegative remaining coefficients. The exact Fraction
ratio check and the integer certificate(8) agree.

Since E4=r1^4+r2^4>=0, and it vanishes only when the centered operator is
zero, equation(1) is strict for every nonconstant host with s>0. If s=0,
nonnegativity forces W=0. This proves the equality statement.

## 5. Independent complete polynomial regeneration

`continuation_20261002_regular3_transfer_audit.py` uses the root-free
nine-state polynomial transfer

    T_(i,j),(k,l)=Pij Pil Pkj.

Exact dictionary matrix multiplication computes trace(T^5) separately in
each cone. Multiplication by3^5 gives the entire density polynomial in
(6), agreeing coefficient by coefficient with full vertex enumeration.
It then computes trace(P^4)-s^4 and trace(P^6)-s^6 directly and checks
the cycle formulas(7). This is a distinct mathematical generator:
it enumerates no ten-vertex assignment or edge-type histogram.

The root-free transfer identity is Rossman's prior ladder identity in a
similarity-equivalent form, not claimed as new. Python's unbounded
integers are used throughout these polynomial checks. No spectral solver
or optimizer is part of the proof.

## 6. Sharpness and an exact stronger-bound obstruction

The leading fourth-cycle coefficient is5 because H has five four-cycles.
For a regular perturbation W=1+epsilon U, all terms whose selected edge
subgraph has a degree-one vertex vanish. At order4 only the five
four-cycles survive, so

    t(H,W)=1+5epsilon^4 t(C4,U)+O(epsilon^6).

Take U to be a nonzero regular centered three-state kernel, for example
the identity direction. Any coefficient larger than5 in(1), with any
fixed sixth-cycle coefficient, fails for sufficiently small epsilon.
Thus5 is optimal.

For sixth-cycle coefficient15, take the strictly positive regular host

    Wii=49/50, Wij=101/100 for i!=j.

Here s=1 and both centered eigenvalues equal-1/100. Exact evaluation
gives

    F=500000050014954450821054849999
       /500000000000000000000000000000.

Its difference from the proposed coefficient15 threshold
1+10/100^4+30/100^6 is

    -45549178945150001/500000000000000000000000000000 <0.

The example obstructs that stronger quantitative inequality only. It
obeys the proved265/18 bound and is not a Sidorenko counterexample.

## Historical and source boundary

General two-state Sidorenko follows from prior Ruozzi/Bethe results;
the companion scope audit explains why qualitative rank-one statements
are rederivations. The present three-state statement permits two
arbitrary centered eigenvalues and arbitrary diagonal entries in its
regular equal-measure domain. A bounded primary search has not located
the exact quantitative statement, but this is insufficient to establish
historical novelty. The transfer and character tools are credited as
prior art. The famous unrestricted ten-vertex Möbius-ladder conjecture
remains unresolved by this work.
