# ML10 Sidorenko inequality for every eight-state Boolean convolution host

2 October 2026. Complete exact finite polynomial proof. A separate agent's full analytic
and independent coefficient audit passed. Historical novelty unverified. This is a restricted
host theorem and does not solve unrestricted ML10 Sidorenko.

## Statement and normalization

Let G=(Z/2Z)^3, with uniform probability measure. For arbitrary
p_g>=0, define W(x,y)=8p_(x+y), and let s=sum_g p_g. Let H=ML10 have
left and right vertices indexed by Z/5Z, with edges (i,j) when
j-i is 0,1,or -1. Then

    t(H,W) >= s^15.                                           (1)

The eight Fourier coefficients of p are the integral-operator eigenvalues
of W. They may have either sign. Consequently (1) goes beyond the case
where all the Fourier coefficients are nonnegative. It does not concern
arbitrary regular eight-state hosts, unequal host-atom measures, or
nonconvolution hosts.

The proof has two parts. An elementary binary-coordinate averaging
argument handles all but one affine orbit of strict weight orders. A
positive polynomial multiplier proves (1) on that last order chamber.
All boundary cases follow by continuity.

## 1. Affine invariance and a binary-coordinate averaging lemma

For any bipartite H, its density in a convolution kernel p_(x+y) is
unchanged by replacing p_g by p_(Ag+b), where A is an invertible linear
map of G and b is arbitrary. Relabel both source parts by A; translate
one of the source parts by b. The uniform host measure is preserved.
The same invariance holds for the edge density s.

Suppose coordinates are G=F2 x F2^2, and

    p(t,u)=a(u)+(-1)^t b(u),  a(u)>=0, b(u)>=0.                 (2)

Let pbar(t,u)=a(u), obtained by averaging the first coordinate. Expanding
all edge factors and summing the first coordinate of every source vertex
selects exactly edge subsets S having even degree at every vertex. Thus

    t(H,8p)=sum_(S even-degree) E_(u_v)
                product_(e in S) 8b(u_x+u_y)
                product_(e not in S) 8a(u_x+u_y).              (3)

Each term is nonnegative. The empty subset is t(H,8pbar), so

    t(H,8p)>=t(H,8pbar).                                      (4)

This argument itself needs no bipartiteness; bipartiteness is used for
the affine translations permitting (2). It is a standard character
expansion positivity argument, not claimed as a new general tool.
Writing q_u=2a(u)=p(0,u)+p(1,u), the averaged kernel is exactly the
four-state convolution kernel 4q_(u+v), and sum_u q_u=s.

For completeness, every nonnegative convolution kernel on F2^2 satisfies
Sidorenko for every bipartite source graph. Split F2^2=F2 x F2. In each of
the two pairs, choose the larger weight as the t=0 entry. Either choice
pattern is the value table of an affine function f:F2->F2. The affine
host permutation (t,u)->(t+f(u),u) therefore makes b>=0 in (2). Average
that coordinate by (3). The remaining two-state kernel can be oriented
so its first weight is at least its second by a host translation, then
averaged again. The final kernel is constant s, proving the assertion.
We use this elementary qualitative consequence here; the earlier
quantitative Klein4 cycle-surplus theorem is not required for (1).

## 2. The orientation test on eight weights

Fix nonzero a in F2^3, with pivot bit l=a&(-a). Choose the transversal
plane T_a={x: x&l=0}; the four pairs are {x,x+a}, x in T_a. Define

    epsilon_a(p)=product_(x in T_a) sign(p_x-p_(x+a)).         (5)

For strictly distinct weights, epsilon_a is +1 or -1. Choose a linear
coordinate map identifying a with (1,0,0), and T_a with {(0,u)}.
The choices of which entry in each pair is larger form a four-bit
function f:F2^2->F2. That function is affine precisely when it has even
parity: its quadratic coefficient equals the XOR of its four values.
Therefore epsilon_a=+1 permits an affine pair flip
(t,u)->(t+f(u),u) making every p(0,u)>=p(1,u). Apply (4) and the
four-state conclusion above to prove (1).

Changing the linear transversal alters the selected representatives in
an even number of pairs; this follows because the difference of two
linear choices is a linear function on F2^2. Consequently the sign test
is independent of that harmless choice. Translation likewise changes
an even number of pair representatives. The sign test is thus compatible
with affine host changes.

If a pair is tied, its orientation can be chosen freely to adjust parity;
we do not need that observation because continuity below covers all ties.

## 3. Exact coverage: just one exceptional affine order orbit

A strict weight order is represented by ranks p_g in {0,...,7}. The
accompanying exact script `continuation_20261002_cube8_coverage.py`
checks every one of the 8!=40320 permutations. The counts are:

| Number of a with epsilon_a=+1 | Number of strict orders |
|---:|---:|
| 0 | 1344 |
| 1 | 4032 |
| 2 | 6720 |
| 3 | 8064 |
| 4 | 8064 |
| 5 | 6720 |
| 6 | 4032 |
| 7 | 1344 |

Every order except the 1344 orders in the first row is covered by Section2.
The same script generates all 168 invertible 3x3 binary linear maps and
all 8 translations, hence all 1344 affine maps. It checks the exact set
identity that the first-row orders are the affine orbit of

    (rank p0,...,rank p7)=(0,1,2,7,3,6,5,4).                 (6)

All ranks are distinct, so this representative's affine orbit has exactly
1344 members. The enumeration checks orbit equality, not merely equal
cardinalities. The full affine permutation list and coverage counts are
saved in the corresponding JSON certificate. No S8 invariance of the
host-density polynomial is assumed: only AGL(3,2) is used.

It remains to prove (1) when

    p3>=p5>=p6>=p7>=p4>=p2>=p1>=p0.                         (7)

## 4. Exact density polynomial, with two independent generators

Let F(p)=t(H,8p). H is connected, bipartite, and has ten vertices and
fifteen edges. Translation on every host vertex preserves x+y, so one
source label can be fixed at 0. Accordingly

    F(p)=8^6 sum_(rooted labels in G^9) product_(xy in E(H)) p_(x+y).
                                                                    (8)

The C++ script `continuation_20261002_cube8_vertex_polynomial.cpp`
enumerates all 8^9=134217728 rooted assignments exactly. It produces
89168 nonzero host-weight monomials with integer coefficients. Fixing
the root is valid here because convolution hosts are translation
transitive. It was not used for the earlier arbitrary regular
three-state proof, where it would be invalid.

A separate Fourier-flow generator checks the entire polynomial.
Write r_chi=sum_g p_g chi(g), with r_0=s. Character expansion of the
fifteen edge factors keeps exactly the character-valued edge flows
whose sum at each vertex is zero. The binary cycle space of H has
dimension 15-10+1=6 and hence 64 elements. For G=F2^3 there are
64^3=262144 flows. Their enumeration gives 3964 Fourier monomials,
with nonnegative integer coefficients summing to 262144.
`continuation_20261002_cube8_flow_and_smoothing.py` generates them.

The independent C++ Walsh transform
`continuation_20261002_cube8_walsh_audit.cpp` substitutes the complete
8-variable Hadamard transform into (8), then divides by 8^15 from
Fourier inversion. Its entire 3964-term polynomial agrees exactly with
the flow generator. This compares every coefficient, not a sample of
values. The numerical smoothing experiments later in the flow script
are exploratory and have no role in the proof.

## 5. Positive multiplier on the exceptional chamber

For (7), put o=(3,5,6,7,4,2,1,0), and write uniquely

    p_(o_i)=d_i+d_(i+1)+...+d7,  0<=i<=7, d_i>=0.           (9)

Then

    s=d0+2d1+3d2+4d3+5d4+6d5+7d6+8d7.

Let P(d)=F(p(d))-s(d)^15 and L=d0+...+d6. Exact expansion of P has
170406 nonzero coefficients, of which 367 are negative. Thus raw
coefficientwise positivity is not asserted. However the exact identity

    L^2 P(d)=sum_alpha c_alpha d^alpha                    (10)

has 345312 nonzero integer coefficients and EVERY c_alpha is positive.
The polynomial is homogeneous of degree17. The smallest nonzero
coefficient is 262143; the largest is 166970267349065400320.
Multiplication by L once leaves 17 negative coefficients; multiplication
by L twice removes all of them.

The full list is the `certificate_coefficients` field of
`continuation_20261002_cube8_last_chamber_polya.json`.
The generator first remaps all exponents in (8) by o. It applies the
seven successive shears p_i->p_i+p_(i+1), for i=0,...,6. These compose to
(9); doing them in this order is essential. It subtracts s(d)^15 using
integer multinomial coefficients, then multiplies by L twice. All
operations are integer additions and multiplications.

A second implementation,
`continuation_20261002_cube8_polya_cpp_audit.cpp`, repeats this algebra
with exact signed 128-bit integers; the fixed arithmetic bounds here
are below 10^30, safely inside that type. It independently reproduces
all 345312 coefficients and checks no coefficient is negative. The
full C++/Python coefficient maps agree exactly.

Since d>=0, (10) is nonnegative. If L>0, division by L^2 proves P>=0.
If L=0, (9) makes all eight weights equal d7, so F=s^15 directly.
This proves (1) on the exceptional chamber. In fact it is strict there
for nonconstant weights: (10) contains the following positive pure
terms, and at least one corresponding d_i is positive when L>0:

| Monomial | Coefficient |
|:---|---:|
| d0^17 | 262143 |
| d1^17 | 134184960 |
| d2^17 | 1134628245 |
| d3^17 | 3221225472 |
| d4^17 | 60175070835 |
| d5^17 | 118091317248 |
| d6^17 | 72749439945 |

Together with Sections1–3 this proves (1) for all strict orders. Every
nonnegative eight-vector is a limit of positive, distinct eight-vectors;
F and s^15 are polynomials. Taking the limit proves (1) including zeros
and ties, and including the zero host.

## Source and novelty boundaries

Fox–Himwich–Mani–Zhou, Electronic Journal of Combinatorics32(3), P38
(September2025), explicitly identify ML10=K5,5 minus C10 as a notorious
small open Sidorenko case:
https://www.combinatorics.org/ojs/index.php/eljc/article/download/v32i3p38/pdf/
Rossman's May2025 primary note supplies the earlier general Möbius-ladder
transfer method, not an unrestricted solution:
https://users.cs.duke.edu/~br148/sidorenko-mobius.pdf

The elementary Fourier-flow identity and nonnegative-character expansion
are standard tools. Nonnegative spectrum alone already yields a
Sidorenko bound; that observation is not new. Zhao's July2025 theorem for
even subdivisions in abelian Cayley hosts does not apply to ML10, whose
vertices all have degree3 and which is not an even subdivision:
https://arxiv.org/abs/2507.15723

A bounded primary search did not locate this exact all-eight-weight
Boolean convolution statement or its exceptional-chamber multiplier.
This is not sufficient to certify historical novelty. The proof is
complete within its stated finite host family, with exact independent
polynomial checks and a separate full analytic audit PASS. The audit is
`cube8_k_independent_audit.md`. It independently regenerated the full
density through a C10-plus-diameters fundamental-cycle basis and inverse
Walsh transform, reproduced every coefficient of the exceptional chamber
and multiplier by a separately coded direct-square algorithm, and checked
coverage using affine ternary law and highest-pivot transversals. The
original pre-audit proof is preserved unchanged alongside this final copy. The unrestricted graphon problem remains open in
this work. In particular this theorem is not inferred to extend to
arbitrary regular hosts or all finite abelian groups.
