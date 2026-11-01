# Independent audit: adjacent terminal marks with arbitrary background graph

Date: 2026-10-02. Auditor: independent `antivoter_audit` agent.

**Verdict: PASS for the stated adjacent pair and background scope.** I
read the full `forest_adjacent_terminal_core3_candidate.md`, the entire
coefficient-certificate script, the complete coefficient JSON, and the
exact-results JSON. I independently checked every reduction and
regenerated all 11,063 polynomial coefficients by a different algebraic
construction and encoding. Exact original-graph enumeration also passes.
No mathematical gap was found; no author file or Git state was modified.
This audit does not certify novelty or external peer review.

## 1. Exact weighted star and arbitrary-background contraction

The three-port weighted star transfer is
\(T(x)=(1+Bx)I+x^2P+x^3Q\), with
\(B=\sum b_i\), \(J=\prod b_i\),
\(P^2=2BQ\), and \(PQ=QP=Q^2=0\). These identities are valid also
when some or all column factors vanish; they are polynomial identities,
not an inversion or nonsingularity argument. With
\(\alpha=x^2/(1+Bx)\), \(\gamma=x^3/(1+Bx)^2\), the nilpotent
exponential has precisely the required \(Q\) coefficient
\(\gamma+B\alpha^2=x^3/(1+Bx)\). All denominators remain positive
even at \(B=0\).

For any fixed full forest, its edge subset \(H\) wholly inside the
other-terminal graph is acyclic. Conversely, fixing any acyclic such
\(H\), contracting each tree component preserves acyclicity of the
remaining selected edges. The contracted component has row weight
\(a_C=\sum_{j\in C}a_j\). Its parallel spokes to core vertex \(i\)
aggregate to \(a_Cb_i\): a forest cannot select two of those parallel
spokes, and the single-edge alternatives have exactly that summed
weight. Expanding a selected aggregate edge back to any of its original
alternatives preserves acyclicity because the contracted components
were trees. Thus this is a weight-preserving term-by-term enumeration,
including when the background graph itself contains cycles.

Each acyclic \(H\) consequently contributes
\(w_HD_H\exp(U_HP+\Gamma_HQ)\). Summing these contributions and
normalizing by \(D=\sum_Hw_HD_H>0\) yields raw \(P\) coefficient
\(\mathbb EU_H\) and raw \(Q\) coefficient
\(\mathbb E\Gamma_H+B\mathbb EU_H^2\). Therefore the exact
effective parameters are
\[
 U=\mathbb EU_H,\qquad
 \Gamma=\mathbb E\Gamma_H+B\operatorname{Var}(U_H).
\]
Both are nonnegative. The empty background forest guarantees \(D>0\).
No upper bound on \(\Gamma\) is needed or assumed. This distinction
from the matching-background argument is essential and is correct.
The result applies to every finite background graph, with no bound on
its size; it is not a claim about an infinite-volume forest measure.

## 2. Four adjacent deletion/contraction coefficients

The marked edges form the path \(a-b-c\), with no other terminal
edges incident to those three vertices. Their deletion/contraction
graphs have endpoint-cluster rows respectively
\((a,b,c)\), \((a+b,c)\), \((a,b+c)\), and \((a+b+c)\).
The double contraction is valid since the two marked edges themselves
are acyclic. The background contribution is unchanged in all four
cases, because its terminal vertices are disjoint from the marked path.

Writing \(F=S+LU+J\Gamma+BJ U^2\) and \(M=L+2BJ U\), expansion
of \(\exp(UP+\Gamma Q)\prod T(x_i)\) gives exactly
\[
\begin{aligned}
 C(x_1,\ldots,x_k)={}&F\prod_id(x_i)
 +M\sum_i x_i^2\prod_{j\ne i}d(x_j)\\
 &+J\sum_i x_i^3\prod_{j\ne i}d(x_j)
 +2BJ\sum_{i<j}x_i^2x_j^2\prod_{l\ne i,j}d(x_l).
\end{aligned}
\]
The \(2BJ U\) in \(M\) is the background/one-star cross term;
the pair-star coefficient is \(2BJ\). There are no surviving
three-merger terms. This agrees with the independent raw
\((I,P,Q)\)-basis calculation.

The four coefficients are \(D\) times the four displayed cluster
values, hence the Rayleigh difference is exactly \(D^2R\), where
\[
 R=C(a+b,c)C(a,b+c)-C(a,b,c)C(a+b+c).
\]
Both marked activities cancel by multiaffinity. No equality between the
single-mark coefficients is assumed.

## 3. Independent full polynomial-certificate regeneration

New files are `adjacent_terminal_ant_independent_check.py` and
`adjacent_terminal_ant_independent_checks.json`. The independent script
uses base-32 integer encodings of exponent vectors, instead of the
author's eleven-coordinate tuple keys. It builds \(C\) by multiplying
raw operator triples, starting from
\((1,U,\Gamma+BU^2)\), then applying
\[
 (v_0,v_P,v_Q)(w_0,w_P,w_Q)
 =(v_0w_0,v_0w_P+v_Pw_0,
   v_0w_Q+v_Qw_0+2Bv_Pw_P).
\]
It finally applies the initial core row \((S,L,J)\). Thus its
construction differs from the author's explicit cluster-polynomial
expansion. The total degree of each Rayleigh product is at most 20,
so exponent encoding in base 32 has no carries or aliasing. All
arithmetic is exact integer arithmetic; no third-party symbolic algebra
or floating-point sign test is used.

After primitive substitution for \(B,J,S,L\), every coefficient
agrees exactly with the complete author JSON, and all 11,063 collected
coefficients are positive integers. The independently obtained slice
inventory is:

| \(U\) degree | \(\Gamma\) degree | Terms | Minimum coefficient |
|---:|---:|---:|---:|
| 0 | 0 | 4656 | 1 |
| 1 | 0 | 3140 | 2 |
| 0 | 1 | 740 | 2 |
| 2 | 0 | 1528 | 1 |
| 1 | 1 | 335 | 2 |
| 3 | 0 | 477 | 2 |
| 0 | 2 | 41 | 1 |
| 2 | 1 | 61 | 2 |
| 4 | 0 | 85 | 1 |

Every monomial contains \(ac\). Each of the three monomials
\(acb_i^2\) has coefficient exactly one. Therefore the formal
polynomial is nonnegative on the entire allowed primitive orthant,
independently of any relation between \(U\) and \(\Gamma\), and
is strictly positive when \(a,c>0\) and at least one column factor
is positive. This establishes the symbolic sign for arbitrary
background size, rather than extrapolating from a parameter grid.

## 4. Independent original-graph checks and boundary cases

The new checker literally enumerates every acyclic subset of the core,
spoke, and background edges, then actually inserts the two adjacent
marks successively. It does not contract background components or use
the frontier transfer to calculate those original-graph coefficients.

A six-terminal graph with a cyclic triangle background enumerates
327,376 forests and gives
\[
 (A,B_e,B_f,C_{ef})=
 (2304977317224,311616917616,181980750480,19935541560),
\]
with Rayleigh difference \(10757309427647656626240>0\). These exact
values agree with the author's separate frontier calculation.

A second cyclic-background graph has a zero marked middle row, a zero
column factor, and a missing core edge. Its 6,354 forests give
\((4097004,4097004,4097004,1483836)\), with Rayleigh difference
\(10706159748672>0\). An independently coded raw-background sum
agrees with both graphs' four coefficients and with \(D^2R\).

Additional exact checks give a strict Rayleigh difference of four with
rows \((1,0,1)\), columns \((1,0,0)\), and empty core/background.
They give zero when all columns vanish, when \(a=0\), or when
\(c=0\). These are consistent with the certificate and its exact
strictness condition. In particular, a zero middle row is allowed and
does not force equality.

The author sanity-check code was read in full. It correctly excludes
cyclic background subsets, contracts acyclic components, propagates the
eight actual spoke choices, and checks all four marked coefficients.
Its four reported cases and coefficient inventory are consistent with
the independent calculations. Those finite checks support, rather than
replace, the formal certificate proof.

## 5. Scope and probability statement

For positive marked activities,
\(\Pr(e)\Pr(f)-\Pr(e,f)=z_ez_fD^2R/Z^2\ge0\), with the
stated strictness. Thus the covariance has the claimed nonpositive
sign. The theorem allows an arbitrary finite weighted graph on the
other terminals, including cycles and chords, nonnegative row/column
factors and core activities, and a zero middle row. It requires rank-one
spokes and forbids every other terminal edge incident to the marked
three endpoints.

It does not prove negative association, arbitrary terminal-pair
correlations, arbitrary spoke weights, or the full forest conjecture.
It is separate from the matching-vector negative-association theorem.
A shorter factorization might improve presentation, but the existing
finite exact polynomial certificate and its graph reductions are already
mathematically complete. Historical priority and external review remain
unverified.
