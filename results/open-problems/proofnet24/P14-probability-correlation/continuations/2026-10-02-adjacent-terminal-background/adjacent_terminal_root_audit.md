# Root audit of adjacent terminal correlation

2 October 2026 UTC. **PASS for the exact written scope.** I read the
complete large-certificate and shorter Bernstein proofs, both author
implementations, the separate ant audits and both independent checkers.
I reran the author primitive certificate, author seven-polynomial
identity, independent raw-operator certificate/original-graph checker and
independent Bernstein interpolation; every run exited zero.

The result permits a finite three-vertex weighted core with nonnegative
activities, rank-one spokes, and an arbitrary graph on other terminals.
It marks only the two adjacent edges a-b and b-c. No other terminal edge
may be incident to a,b,c. It proves pairwise negative correlation for
that pair. Full forest negative association and arbitrary incidence
patterns remain unproved.

## Exact arbitrary-background reduction

Fixing a forest inside the other-terminal graph and contracting its tree
components preserves acyclicity. Its aggregated spoke row is the sum of
the original row factors. A selected parallel spoke represents a sum of
alternative original edges; selecting two such edges would form a cycle.
The correspondence is weighted term by term. Cyclic background subsets
are excluded, not assigned a transfer value.

For core-frontier operators P^2=2BQ, PQ=QP=Q^2=0, the transfer of row x is
(1+Bx)exp[alpha(x)P+gamma(x)Q]. Expanding the mixture gives the exact
effective U=EU_H, Gamma=EG_H+B Var(U_H). Its variance term cannot be
dropped. Both are nonnegative; no upper bound on Gamma is needed.

The four marked deletion/contraction coefficients have the SAME scalar
background factor D, and rows (a,b,c), (a+b,c), (a,b+c), (a+b+c).
The Rayleigh difference is D^2 times the stated cluster polynomial
difference. Positive marked activities then give
Pr(e)Pr(f)-Pr(e,f)=z_e z_f D^2 R/Z^2 with the claimed sign.

## Short scalar lemma and independent exact identity

Primitive core quantities obey BL>=9J and B^2S-2L>0 when B>0, by
the displayed AMGM expansion and sum-of-squares constant term. Therefore
F=S+LU+J Gamma+BJ U^2 and M=L+2BJ U satisfy BM>=9J,
B^2F-2M>0. Normalize x=Ba,y=Bb,z=Bc, u=2M/(B^2F),v=9J/(BM).
The normalized cluster coefficients are u/2 and uv/18. If M=0 then
J=0 and choosing u=v=0 is valid.

I verified the seven complete positive numerator polynomials and the
degree-two tensor Bernstein identity. The independent checker derives
all nine Bernstein entries from exact evaluations at 0,1/2,1, then
eliminates symmetric x,z polynomials into s=x+z,t=xz,y. It reproduces
every term of the declared lists, independently of the author's UV
expansion. All coefficients are positive. The i=0 entries are
1+s+t, so R>=F^2 xz(1-u)^2(1+s+t)>0 whenever a,c>0 and B>0.
No positivity of b is required.

The separate 11,063-term certificate regenerates the entire primitive
polynomial by raw I,P,Q multiplication and an independent base-32
encoding. Every coefficient is positive, every term contains ac, and
each ac*b_i^2 coefficient is exactly one. Original full-graph enumeration
agrees on a cyclic triangle background and a zero-column/zero-middle-row
case. Their respective exact forest counts are 327,376 and 6,354.

When B=0, the marked path is a separate tree; when an outer row vanishes,
its sole marked edge is a bridge. These cases have independent indicators
and equality. The algebra handles zero core activities and column factors
by direct polynomial identities or the explicitly separated B=0 case.

Both certificate routes prove the inequality for backgrounds of arbitrary
finite size; numerical graph checks are corroboration. Known small-graph
or series-parallel special cases are prior work. Historical priority of
this restricted unbounded-family theorem remains unverified; these are
internal audits rather than external peer review.
