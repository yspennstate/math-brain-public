# Independent audit: Klein-four ML10 Schur-convexity certificate

2 October 2026. Verdict: **PASS for the stated restricted-host theorem.**
This is an independent analytic and static-code audit, supplemented by
complete exact reruns. No gap was found. It is not a proof of ML10
Sidorenko for unrestricted hosts, and it is not a historical novelty
certificate. The author proof and original code/JSON were not edited.

Audited inputs:

- `continuation_20261002_klein4_schur_proof.md`;
- `continuation_20261002_klein4_schur.py/.json`;
- `continuation_20261002_klein4_independent_transfer_audit.py/.json`;
- `continuation_20261002_scope_and_prior_art.md`.

The exact reruns, redirected only to new output files, matched the entire
original JSON objects. Their source hashes and output are recorded in
`restricted_hosts_k_rerun_summary.json`. Additional independent checks are
in `restricted_hosts_k_independent_checks.json`.

## 1. Graph, measure, and polynomial normalization

The source has left/right vertices indexed by Z/5Z, with differences
0,1,-1. It has ten vertices and fifteen edges and is the bipartite
ten-vertex Möbius ladder. Rossman's Definition 1.3 uses this same ladder
description. One can also identify it directly with C10 plus its five
diameter chords: label even cycle vertices by left i and odd vertices by
right j. The three differences are 0,-1,2 in those labels; the relabeling
left i to 2i and right j to 2j+1 changes them to 1,-1,0 modulo five.

For a uniform four-element host, W(x,y)=4p_(x+y) has row mean and edge
density s=sum p. Its density is the sum over all 4^10 vertex assignments
times 4^15/4^10. Fixing one vertex to zero removes a factor four because
simultaneous translation preserves every edge color in characteristic
two. Therefore the fixed-label polynomial is multiplied by 4^6=4096,
exactly as in the code. The total fixed-label count is 4^9. All monomials
have degree fifteen and the density coefficient sum is 4^15=1073741824.
Consequently F(s/4,s/4,s/4,s/4)=s^15, including s=0.

The independent root-free transfer also has the correct normalization.
For states (x_i,y_i), the i-th transfer factor contributes the rung
p_(x_i+y_i) and the two neighboring cross edges
p_(x_i+y_(i+1)) p_(x_(i+1)+y_i). A length-five closed walk therefore
contributes each of the fifteen edges exactly once. Its trace sums all
4^10 assignments, so its density factor is 4^5=1024. No root factor is
missing. This route reproduces the full polynomial, not just its value
on selected test points.

## 2. Full S4 symmetry is justified

Translating vertex labels on one source bipartition translates all four
edge colors. Applying GL(2,2) to every vertex label permutes the three
nonzero colors. These transformations generate AGL(2,2), of order 24,
acting faithfully on four colors, hence every permutation of those
colors. Nonnegative p need no extra restrictions for this argument. The
author code also checks the entire coefficient dictionary under all 24
permutations. This symmetry uses both the bipartite source and the special
four-element group.

## 3. The quotient certificate proves the claimed inequality

Let Q=(partial_0 F-partial_1 F)/(p0-p1). The numerator is antisymmetric
under p0,p1, so polynomial divisibility is valid. If an antisymmetric
monomial pair has exponents a>b, its quotient is

    p0^b p1^b (p0^(a-b)-p1^(a-b))/(p0-p1)
      = sum_(j=0)^(a-b-1) p0^(a-1-j) p1^(b+j).

This is precisely the author's loop; its multiplication-back assertion
checks the full numerator. The independent route uses lexicographic
monic polynomial long division and checks the resulting complete Q
dictionary against the certificate. Both are exact integer operations.

The ordered substitution has exponent transformation

    p0^a p1^b p2^c p3^d
      -> binom(a,i) binom(c,j) A^(a+b-i) B^(c+d-j) D^i E^j,

which agrees with both scripts. The full regenerated degree-thirteen
polynomial has 436 nonzero strictly positive coefficients and coefficient
61440 on D^13. The original Q has 434 nonzero coefficients, including
164 negative ones; the raw coefficient shortcut is correctly rejected.

The passage from the ordered region to the whole orthant is valid:
Q is invariant under swapping p0,p1, because both numerator and
denominator change sign, and invariant under swapping p2,p3 by symmetry
of F. Sort each pair separately, so A=min(p0,p1), D=abs(p0-p1),
B=min(p2,p3), E=abs(p2-p3), all nonnegative. Thus

    Q(p) >= 61440 abs(p0-p1)^13.

Full S4 symmetry gives the same inequality for every pair i,j, including
equal coordinates via its polynomial extension. Multiplication by the
square of the coordinate difference gives

    (pi-pj)(partial_i F-partial_j F)
      >= 61440 abs(pi-pj)^15.

The standard symmetric differentiable gradient criterion gives
Schur-convexity in the interior of the orthant and continuity extends it
to the boundary. Alternatively its pairwise averaging proof follows by
integrating this gradient inequality along each fixed-sum two-coordinate
segment.

## 4. The quantitative radial constant is correct

For u=(sum p)/4 and p(t)=u1+t(p-u1), the elementary identity

    sum_i (xi-mean x) gi
      = (1/4) sum_(i<j) (xi-xj)(gi-gj)

gives, for t>0,

    dF(p(t))/dt
      = (1/(4t)) sum_(i<j) (pi(t)-pj(t))
                              (partial_i F-partial_j F)(p(t)).

Since pi(t)-pj(t)=t(pi-pj), the lower bound is
15360 t^14 sum abs(pi-pj)^15. Integrating yields
61440/(4*15)=1024. The integrand is polynomial and continuous at t=0;
the intermediate 1/t identity poses no convergence issue. Hence

    F(p) >= (sum p)^15 + 1024 sum_(i<j) abs(pi-pj)^15.

Nonuniform p has a strictly positive displayed surplus, so equality in
the Sidorenko bound within this family requires the constant kernel.

## 5. Exact static-code and regeneration verdict

The host-label enumeration has exactly 4^9 iterations; integer XOR is
the correct Klein-four group operation. All coefficient additions,
derivatives, divisions, binomial expansions, and dictionary comparisons
use Python integers, without finite precision or optimization. Counter
entries that cancel to zero are correctly filtered in equality checks.
The independent transfer's dynamic program computes exact closed walks;
its long-division subtraction has the correct sign for divisor p0-p1.
Both complete reruns passed and their JSON objects match the originals
exactly. The additional audit checks all polynomial degrees, coefficient
sums, term counts, and positivity claims. These are exhaustive finite
algebraic certificates, not a sampling argument.

## 6. Scope and primary-source comparison

The equal-diagonal, equal-row-sum characterization in the addendum is
correct. For a symmetric matrix with off-diagonal rows
(a,b,c), (a,e,f), (b,e,g), (c,f,g), equality of row sums implies
b+c=e+f, a+c=e+g, a+b=f+g. Adding the first two minus the third gives
c=e, then b=f and a=g. Thus every equal-measure, equal-diagonal regular
symmetric four-state host has exactly the claimed Klein-four form.
Unequal atom measures, unequal diagonal entries, larger finite hosts, and
general graphons are outside the proof. Regularity alone is insufficient
to apply this theorem to a general four-state matrix.

Primary sources independently inspected in this audit:

1. Benjamin Rossman, *On Sidorenko's Conjecture for Bipartite Möbius Ladders*,
   author manuscript dated 8 May 2025,
   https://users.cs.duke.edu/~br148/sidorenko-mobius.pdf.
   The local author PDF/text supplies the ladder definition and prior
   transfer trace identity. The identity is properly credited as prior.
2. Jacob Fox, Zoe Himwich, Nitya Mani, Yunkun Zhou, *A note on directed
   analogues of the Sidorenko and forcing conjectures*, EJC 32(3) (2025),
   P3.38, https://www.combinatorics.org/ojs/index.php/eljc/article/download/v32i3p38/pdf/.
   Its introduction identifies ML10 as an unresolved small case.
3. Yuqi Zhao, *Sidorenko Inequalities for Two-Sided Group Correlation
   Kernels*, arXiv:2606.23018, https://arxiv.org/pdf/2606.23018.
   Its Theorem 1.1 applies to two-sided correlation kernels; its
   product-Cayley formulation is for directed one-subdivisions.

On the Klein group a real correlation c(h)=E_z f(z)f(z+h) has Fourier
coefficients hat(f)(chi)^2, all nonnegative. Arbitrary nonnegative p do
not have this property: p=(0,1,1,1) has all three nontrivial Fourier
coefficients negative. Translating colors multiplies those three signs
by a sign vector of product positive, so this example cannot become a
nonnegative-Fourier correlation by the available color translations;
GL(2,2) merely permutes them. Consequently the cited correlation theorem
does not automatically cover this entire host family, let alone its
Schur-convexity assertion. This nonimplication is an inference from its
scope, not a claim that every individual example was previously unknown.

The bounded current primary-source search located no general ML10
resolution and no earlier exact Schur bound with this constant. Search
absence does not establish priority. The certified conclusion is the
restricted theorem above, with historical novelty unverified.
