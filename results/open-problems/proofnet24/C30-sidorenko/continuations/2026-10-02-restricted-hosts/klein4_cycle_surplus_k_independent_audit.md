# Independent audit: Klein-four ML10 cycle surplus

2 October 2026. Verdict: **PASS for the stated restricted-host inequality,
the stronger certificate constant 8165/567, and the exact obstruction to
coefficient 15.** No mathematical or code gap was found. Neither the
unrestricted ML10 Sidorenko conjecture nor historical novelty is certified.
The author proof, script, and original certificate were not edited.

Inputs audited in full:

- `continuation_20261002_klein4_cycle_surplus_proof.md`;
- `continuation_20261002_klein4_cycle_surplus.py/.json`;
- the earlier full vertex polynomial and its audited host/S4 definition.

The author script was rerun with output redirected to
`continuation_20261002_klein4_cycle_surplus_k_rerun.json`; its entire JSON
matched the original. The distinct independent checker
`klein4_cycle_surplus_k_independent_verify.py/.json` reproduces the
complete Fourier polynomial using a different graph description and
fundamental-cycle basis, expands by closed multinomial formulas, and
checks all 760 surplus coefficients. Additional run records are in
`klein4_cycle_surplus_k_independent_checks.json`.

## 1. Fourier normalization and the exhaustive flow generator

On the uniform Klein group, define r_chi=sum_g p_g chi(g). Fourier
inversion is 4p_g=sum_chi r_chi chi(g), not a formula with an extra
factor four. Since each real character satisfies chi(x+y)=chi(x)chi(y),

    W(x,y)=sum_chi r_chi chi(x)chi(y).

The integral operator consequently has exactly these four eigenvalues,
with the trivial eigenvalue s=sum p. Expanding the source edge factors
and integrating each vertex gives one if its incident characters multiply
to the trivial character, and zero otherwise. Thus there is no missing
normalization factor in the 4096-flow polynomial. As useful checks, the
constant host retains only the trivial flow and gives s^15, whereas
p=(1,0,0,0) gives all four eigenvalues one and density 4096, agreeing with
the previous vertex polynomial.

The source is connected, with E=15 and V=10, so its binary cycle space
has dimension E-V+1=6. A character labeling is a pair of binary cycle
vectors; there are exactly 64^2=4096 choices. The author's all-mask
parity test correctly enumerates the 64 cycles and its edge-color
encoding bit(x)+2bit(y) enumerates every character flow once. It obtains
73 distinct degree-fifteen monomials.

My independent route uses C10 plus five diameter chords. Take the path
0--1--...--9 as spanning tree. The six non-tree fundamental cycles are
the entire C10 and, for each chord i--(i+5), that chord plus its tree
path. Their edge vectors are independent: each has its own non-tree
edge. XOR of their 64 subsets therefore yields the entire cycle space.
The resulting 4096 paired flows match all 73 certificate coefficients,
not merely their sum or selected evaluations. Their 23 permutation
orbits also exactly match every printed table row and coefficient.

Because every binary cycle vector on a bipartite graph has even edge
cardinality, n1+n3 and n2+n3 are even. Thus n1,n2,n3 have the same parity.
The first odd-parity monomials are permutations of (3,3,1), each with
coefficient 10 and trivial exponent eight. Their grouped contribution
is exactly 10s^8 r1r2r3(r1^2r2^2+r1^2r3^2+r2^2r3^2). This sign issue is
real; positivity of the raw coefficient list alone would not prove the
inequality for negative eigenvalues.

## 2. Ordering is legitimate for the whole surplus

The earlier audited proof establishes that affine color transformations
on this four-element group realize S4 and preserve F, using a translation
on one source bipartition when necessary. Under a linear group
automorphism the three nontrivial Fourier modes are permuted. Under a
color translation r_chi is multiplied by chi(a), a sign. Therefore
sum r_chi^4 and sum r_chi^6 are S4-invariant as well; s is invariant.
This justifies sorting p for both sides of the inequality, not only F.

For sorted p0>=p1>=p2>=p3>=0, write

    A=p3, B=p2-p3, C=p1-p2, D=p0-p1.

These are all nonnegative, and their inverse is exactly the four ordered
host forms in the proof. Direct Walsh-transform calculation gives

    s=4A+3B+2C+D,
    r1=B+2C+D, r2=B+D, r3=D-B,

up to an irrelevant mode permutation. In particular the potentially
negative final mode is not accidentally replaced by its absolute value.
These forms agree exactly with the code, including the minus sign.

## 3. Full coefficient identity and the stronger constant

The author uses exact dictionary polynomial multiplication and cached
linear-form powers. Each flow monomial is replaced by its correct product
of powers of the four linear forms. The comparison with the old vertex
polynomial substitutes its host variables by the same ordered p. The
ordered host transformation is invertible, so agreement of these entire
coefficient dictionaries is a full polynomial identity, rather than a
test at ordered numerical samples.

After subtracting s^15+5s^11 sum r_i^4+14s^9 sum r_i^6, the regenerated
degree-fifteen surplus has exactly 760 nonzero coefficients, all strictly
positive integers. This proves nonnegativity on A,B,C,D>=0; symmetry
then proves the statement for every original nonnegative p. Boundary
points require no limiting or positive-entry assumption.

The independent verifier constructs powers by the closed formula

    [A^a B^b C^c D^d](uA+vB+wC+zD)^n
      = n!/(a!b!c!d!) u^a v^b w^c z^d,

with a+b+c+d=n, rather than the author's repeated linear multiplication.
Its full 760-term dictionary matches the original surplus certificate.

For P4=F-s^15-5s^11 sum r_i^4 and V6=s^9 sum r_i^6, the ordered
coefficient lists are both nonnegative. The minimum exact ratio P4/V6
over monomials with positive V6 coefficient is 8165/567, at exponents
(6,8,0,1), i.e. A^6 B^8 D. Monomials absent from V6 also have nonnegative
P4 coefficients. Both the author's Fraction calculation and the distinct
verifier establish the same minimum; the latter additionally checks
every coefficient of 567P4-8165V6 directly. This proves the stronger
constant as asserted. It is only the largest coefficientwise constant
for this ordered substitution, not the globally optimal pointwise
sixth-cycle constant.

For an even cycle, the operator trace equals s^(2k)+sum r_i^(2k), by the
displayed four-character diagonalization. Consequently the stated cycle
density formulation has the correct powers s^11 and s^9 and is homogeneous
of degree fifteen. If s=0, nonnegative p is zero and all terms vanish.

## 4. Fourth-order sharpness and the sixth-order obstruction

Set s=1, r1=epsilon, r2=r3=0. Fourier inversion yields two host weights
(1+epsilon)/4 and two (1-epsilon)/4, so this is a valid host whenever
abs(epsilon)<=1. The flow table reduces exactly to

    F=1+5epsilon^4+15epsilon^6+30epsilon^8+13epsilon^10.

Increasing the fourth-order constant above five while retaining any fixed
finite sixth-order constant gives a negative leading epsilon^4 difference
for sufficiently small nonzero epsilon. This proves the claimed
sharpness in its precise stated sense.

For the coefficient-15 witness, Fourier inversion of eigenvalues
(1,-1/100,-1/100,-1/100) gives
(p0,p1,p2,p3)=(97,101,101,101)/400. All four weights are strictly positive
and have sum one. Direct exact evaluation of the earlier 476-term vertex
polynomial, independently of the new flow evaluation, gives

    F=250000037511179426349533203741
        /250000000000000000000000000000,

and subtracting 1+5sum r_i^4+15sum r_i^6 gives

    -70573650466796259
        /250000000000000000000000000000 < 0.

Thus coefficient 15 fails, even near the constant positive host. This
does not contradict either the coefficient-14 theorem or Sidorenko:
the density remains greater than one. Analytically, setting all three
modes to -epsilon makes the first mixed contribution -30epsilon^7 after
the retained fourth/sixth terms, explaining the failure mechanism.

## 5. Static-code assessment and source boundary

All main-certificate arithmetic is integer or Fraction arithmetic.
The all-mask parity test uses XOR correctly; no orientation is required
over characteristic two. Counter cancellation is filtered when comparing
polynomials, and nonnegative-coefficient assertions inspect signed
values before encoding. The ratio uses only strictly positive V6
coefficients and the proof correctly handles the others separately.
The rational witness uses the total exponent on the three equal modes,
with no dropped mixed terms. No tolerance, fitted coefficient, numerical
optimization, or eigenvalue solver enters either certificate.

The new result uses the same exact restricted host class as the already
audited Schur theorem: equal-measure, equal-diagonal regular symmetric
four-state hosts. It does not include general regular four-state kernels,
unequal measures, or arbitrary graphons. The cycle-space character
expansion and ladder transfer are standard prior tools, properly credited.
The qualitative rank-one result is already implied by known two-spin
Bethe results, as detailed in the separate rank-one audit. The primary
2025 EJC paper and the inspected 2026 correlation-kernel paper do not
supply an unrestricted ML10 resolution; the primary comparison is in
`klein4_schur_k_independent_audit.md`. No earlier exact cycle-surplus
statement was located in the bounded search, which does not establish
novelty. The conclusion here is the fully certified restricted
quantitative inequality and the valid obstruction to its proposed
coefficient-15 strengthening.
