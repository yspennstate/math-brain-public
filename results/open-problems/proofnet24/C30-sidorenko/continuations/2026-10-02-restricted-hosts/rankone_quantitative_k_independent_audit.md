# Independent audit: quantitative rank-one ML10 inequality

2 October 2026. Verdict: **PASS under the stated nonnegative bounded
rank-one regular-kernel assumptions.** No analytic or code gap was found.
The qualitative rank-one Sidorenko conclusion is already obtainable from
known two-state results. This audit does not claim novelty of the
quantitative surplus, and does not imply the general ML10 conjecture.
The original proof, script, and JSON were not edited.

Audited inputs are `continuation_20261002_rankone_quantitative_proof.md`,
`continuation_20261002_rankone_certificate.py/.json`, and
`continuation_20261002_scope_and_prior_art.md`. A complete certificate
rerun matched its original JSON exactly; see
`restricted_hosts_k_rerun_summary.json`. Independently enumerating subsets
of the conventional C10-plus-five-diameter-chords graph gave the same
degree-pair table; see `restricted_hosts_k_independent_checks.json`.

## 1. Integrability and the cubic subset expansion

Write W=1+lambda f tensor f with E f=0 and E f^2=1. For nonzero lambda,
bounded W ensures bounded f almost everywhere: choose epsilon>0 such
that the set abs(f)>epsilon has positive measure. Fubini's theorem and
abs(lambda f(x)f(y))<=ess-sup(abs(W))+1 then bound abs(f(x)) uniformly for
almost every x. Thus every moment used below exists; the proof's brief
integrability assertion is legitimate. The lambda=0 case can be handled
without using a third moment.

Expanding the fifteen factors gives one contribution per selected edge
subset. A degree-one vertex kills the term. Since the source is cubic,
the only remaining nonzero vertex degrees are two and three, contributing
1 and m=E f^3. Handshaking forces the count n3=2k of degree-three vertices
to be even, and the edge count is n2+3k. The term is therefore
lambda^(n2+3k) m^(2k), exactly as stated.

The bitmask script exhausts all 2^15 subsets, computes their full vertex
degrees, and discards exactly those with degree one. It reproduces every
one of the seventeen listed degree types. My separate enumeration uses
the ten cycle edges and five diameter chords, without the author's
bipartition-index edge list, and matches the complete table. Thus both
the graph identification and the coefficient table have independent
checks. In the nonnegative lambda case all terms are nonnegative and
the five C4 and fifteen C6 subsets yield the stated stronger immediate
bound 1+5lambda^4+15lambda^6.

## 2. Negative lambda and the moment constraint

Put lambda=-z<0 and A=z^(-1/2). Nonnegativity of W implies abs(f)<=A
almost everywhere. If a positive-measure level set had f>A, its product
with itself would violate W>=0; the same reasoning applies to f<-A.
This reasoning is valid on general probability spaces and does not
evaluate a kernel on a null diagonal. E f^2=1 then implies 0<z<=1.

The polynomial (A-f)(f+1/A)^2 is nonnegative. Its expectation is
A-1/A-m, because the first two moments are zero and one. Applying the
same argument to -f gives abs(m)<=A-1/A. Consequently r=z m^2 satisfies
0<=r<=(1-z)^2. The polynomial substitution in the certificate is correct:
lambda^(n2+3k) m^(2k) has sign (-1)^(n2+3k) and equals that sign times
z^(n2+n3) r^k. After factoring z^4 it yields exactly the sixteen
displayed nonconstant monomials of F(z,r), with six negative coefficients.

## 3. Every discarded negative term is controlled

The six bounds, in their displayed order, are valid on 0<=z<=1 and
0<=r<=(1-z)^2:

- 5z^2r<=5z^2 since r<=1;
- 60z^4r<=60z^2[z(1-z)]^2<=(15/4)z^2;
- 95z^6r<=95z^2 z^4(1-z)^2<=(1520/729)z^2<(21/10)z^2;
- 60z^5r^2<=60z^2 z^3(1-z)^4<=(15/16)z^2;
- 75z^6r^3<=75z^2 z^4(1-z)^6<=(75/256)z^2;
- z^6r^5<=z^2 z^4(1-z)^10<=(1/256)z^2.

For the third bound the derivative or a direct factorization gives the
maximum 16/729 at z=2/3. For the remaining last three bounds use
z^3(1-z)^4<=[z(1-z)]^3 and
z^4(1-z)^6,z^4(1-z)^10<=[z(1-z)]^4. There is no sign reversal or missing
term. Exact rational addition gives 3867/320, leaving 933/320>2 from
the positive 15z^2 term. Retaining the other scalar positive terms proves

    F(z,r)>=5+(933/320)z^2+30z^4+13z^6,

and hence the asserted 1+5lambda^4+2lambda^6 bound, with slack. All
boundary cases follow from the same nonstrict bounds; z=0 is the separate
constant case. For an even cycle, its only selected subsets without
degree-one vertices are the empty set and the full cycle, proving directly
t(C4,W)=1+lambda^4 and t(C6,W)=1+lambda^6.

## 4. Exact-code assessment

All combinatorial coefficients use integer arithmetic. The mapping from
degree types to the (z,r) coefficient dictionary is injective here and
agrees with the derived exponent formula. The explicit target dictionary
checks all monomials, and the script counts exactly six negative degree
types. Fraction arithmetic checks the rational total and its remaining
coefficient; the analytic maximizations above supply the inequalities
that a Fraction comparison by itself would not prove. The original JSON
is exactly reproduced by a complete rerun. No numerical tolerance,
eigenvalue estimate, or small-parameter assumption enters this proof.

## 5. Known qualitative reduction and limits

The primary 2022 paper by Csikvári, Ruozzi, and Shams, *Markov Random
Fields, Homomorphism Counting, and Sidorenko's Conjecture*, IEEE IT
68(9), 6052-6062, explicitly records the known nonnegative two-state
case; author manuscript:
https://real.mtak.hu/162333/1/Markov_random_fields_Sidorenko.pdf.
The relevant primary theorem is Ruozzi's *The Bethe Partition Function
of Log-supermodular Graphical Models*, NeurIPS 2012, Corollary 4.2,
https://arxiv.org/pdf/1202.6035. Unary factors are permitted. For two
spins, negative determinant is converted to nonnegative determinant by
flipping labels on one source bipartition; the unary factors are flipped
there as well. Nonnegative-determinant two-spin interactions are
log-supermodular. Zeros are handled by continuity.

The addendum's unequal-atom extension is correct. For a regular two-state
kernel K with atom measure mu and degree s>0, use node beliefs mu and
edge beliefs mu_i mu_j K_ij/s. Their marginals are mu. Each edge's energy
plus entropy term equals log(s)-2 sum mu_i log(mu_i). At a degree-d
vertex, the unary energy plus the Bethe vertex correction is
d sum mu_i log(mu_i). The degree sum cancels these terms, so the known
Bethe lower bound is at least s^e. This uses the two-spin theorem; it
does not assume a general Bethe lower bound for all interactions.

For a negative rank-one host, choose a>0 with a-1/a=m and replace f by
a with probability 1/(1+a^2), and -1/a with the complementary probability.
This has first three moments 0,1,m, so the cubic subset expansion gives
the same ML10 density. The moment constraint is equivalent to
sqrt(z)<=a<=1/sqrt(z), ensuring both replacement diagonal kernel entries
are nonnegative; its off-diagonal entry is 1+z. Thus the qualitative
rank-one conclusion follows from existing two-state theory. The explicit
surplus 5lambda^4+2lambda^6 is a more specific conclusion, but a bounded
search not locating it is insufficient to establish novelty.

The proof controls a single third moment. Several centered eigenfunctions
produce mixed third-moment tensors for which no corresponding bound has
been proved here. It yields neither unrestricted regular-host ML10
Sidorenko nor any general pseudo-positive-spectrum theorem. The 2025 EJC
primary introduction independently identifies unrestricted ML10 as open:
https://www.combinatorics.org/ojs/index.php/eljc/article/download/v32i3p38/pdf/.
No general resolution was found in the bounded current primary search.
