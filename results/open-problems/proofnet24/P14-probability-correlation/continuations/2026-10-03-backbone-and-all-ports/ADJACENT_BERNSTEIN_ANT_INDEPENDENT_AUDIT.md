# Independent audit of the shorter adjacent-terminal Bernstein proof

2 October 2026. Auditor: `/root/antivoter_audit`.

**PASS.** I read the complete
`forest_adjacent_terminal_core3_bernstein_proof.md`, its exact verifier and
saved report. This is a fresh audit of the shorter analytic argument,
independent of my earlier 11,063-term certificate audit. The theorem's
scope is two adjacent marked terminal edges over a weighted three-vertex
core with rank-one spokes, with an arbitrary graph on the OTHER terminals
and no other terminal edges incident to the marked endpoints. It proves
pairwise negative correlation in this scope, not full forest negative
association or the unrestricted conjecture. Historical novelty remains
unverified.

## Core and arbitrary-background reduction

The partition-frontier operators have
\(P^2=2BQ\), \(PQ=QP=Q^2=0\), \(vQ1=J\).
Consequently
\(T(x)=(1+Bx)\exp[\alpha(x)P+\gamma(x)Q]\)
with the stated \(\alpha,\gamma\). Contracting each acyclic terminal
background component sums its spoke-row weights exactly. Cyclic terminal
subsets cannot appear in a forest; after contraction, permitted spoke/core
subsets correspond exactly to permitted original forests. Parallel-spoke
aggregation is valid because two parallel choices would create a cycle.

The mixture has scalar normalizer \(D>0\) and exact parameters
\(U=EU_H\), \(\Gamma=EG_H+B\operatorname{Var}(U_H)\).
The variance term follows from the \(P^2/2=BQ\) coefficient and is
necessary. No upper bound on \(\Gamma\) is used. Multiplying the marked
cluster transfers gives formula (2), with pair coefficient \(2BJ\), and
deletion/contraction gives all four coefficients (3) with the same factor
\(D\). The Rayleigh difference therefore has the stated factor \(D^2\).
The common marked endpoint does not itself create a cycle.

## Scalar bounds and normalization

The inequality \(BL\ge9J\) follows from
\(B\sum_{i<j}b_ib_j=3J+\sum_{i\ne j}b_i^2b_j\) and AMGM, including
zero columns by a direct nonnegative limit. The primitive expansion
of \(B^2S-2L\) in (5) is exact. Its constant term
\(\sum b_i^2\) is strictly positive when \(B>0\).

For \(U,\Gamma\ge0\),
\[
B^2F-2M=(B^2S-2L)+B(BL-4J)U+B^2J\Gamma+B^3JU^2>0.
\]
Here \(BL-4J\ge5J\ge0\), and \(BM\ge BL\ge9J\).
Since \(F>0\), the normalized \(u=2M/(B^2F)\) is in \([0,1)\),
and if \(M>0\), \(v=9J/(BM)\) is in \([0,1]\). After replacing rows
by \(x=Ba,y=Bb,z=Bc\), the normalized transfer coefficients are
\(M/(B^2F)=u/2\), \(J/(B^3F)=uv/18\), and the pair coefficient is
\(2J/(B^3F)\). The scalar \(F^2\) in (8) is correct; there is no
missing power of \(B\).

## Independent derivation of all Bernstein coefficients

The new script `adjacent_bernstein_ant_independent_check.py` does not
import or execute author code. It uses exact Fraction arithmetic and
base-32 polynomial encoding in \(x,y,z\). It evaluates the normalized
Rayleigh polynomial at all nine \((u,v)\) points in
\(\{0,1/2,1\}^2\), divides its exact common factor \(xz\), then recovers
its tensor Bernstein coefficients by
\[
b_0=f(0),\qquad b_2=f(1),\qquad
b_1=2f(1/2)-(f(0)+f(1))/2.
\]
This is sufficient because the polynomial has degree at most two in each
parameter: each C factor is affine in \(u\) and \(uv\).

Each reconstructed coefficient is symmetric in \(x,z\). An independent
elimination algorithm expresses it uniquely in \(s=x+z,t=xz,y\):
subtract the largest remaining \(x^az^c y^b\) term using
\(s^{a-c}t^cy^b\). This yielded exactly the seven displayed polynomials,
with respectively 3, 7, 13, 13, 11, 20 and 31 positive terms, and the
three i=0 polynomials are identical. Only after deriving them did the
checker read the author's declared numerator data for an exact comparison.
All coefficients agree and are positive. The complete independently
derived lists are in `adjacent_bernstein_ant_independent_checks.json`.

Thus (8) is a full exact polynomial identity, and nonnegativity follows
from the nonnegative Bernstein basis and the explicit positive Q
coefficients, without finite-input testing or numerical extrapolation.

## Strictness and endpoints

In the forest application, \(u<1\). Summing the i=0 terms over v gives
the strictly positive contribution
\(F^2xz(1-u)^2(1+s+t)\) when the two outer rows are positive and
\(B>0\), regardless of the middle row. If \(M=0\), the scalar condition
forces \(J=0\); choosing \(u=v=0\) is valid and the independently
derived Rayleigh polynomial is exactly \(F^2xz(1+s+t)\).

When \(B=0\), all spokes vanish and the marked two-edge path is a
separate tree with independent edge indicators. If an outer row is zero,
that terminal has no spokes and, by the theorem's incidence restriction,
its sole marked edge is a bridge. Its indicator is independent of the
remaining forest. These equality cases are correctly separated from the
normalization that divides by \(B\).

The proof closes analytically for arbitrarily many other terminals and
an arbitrary finite graph among them. No unstated \(\Gamma\le U/B\)
assumption is used. It does not justify incidence patterns involving
additional edges at the three marked endpoints or any stronger
association property. No remaining mathematical gap was found.
