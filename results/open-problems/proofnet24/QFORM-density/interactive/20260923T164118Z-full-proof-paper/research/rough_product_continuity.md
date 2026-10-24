# A full proof of fixed-matrix C0 regularity

Status: proved in paper_work/fleet_gluing.tex, Lemmas
fg:critical-ball through fg:invertible-continuity and Theorem
fg:fixed-matrix-continuity. Independently reviewed without a mathematical
gap. No claim of literature novelty is made.

## Statement

For every fixed real symmetric A of rank at least three, every vector b
and scalar c, and independent real coordinate laws with densities at
most one, Q=X^TAX+b^TX+c has a bounded density in C0(R).
The height may depend on A. This does not solve the universal-height
conjecture, whose quantifier ranges over all dimensions and matrices
with s3(A)>=1.

## Proof improvement recorded during preparation

The source r3 regularity proof divides an invertible physical block
of order3 or4 into a critical neighborhood, the far field, thin tubes
where only one gradient component is large, and the remaining compact
region with two large derivatives.

Instead of relying directly on rough chart continuity, the manuscript
uses that decomposition to prove stability in the uniform output norm.
For product densities F=prod fi and G=prod gi, telescope F-G.
On the region with at least two partial derivatives larger than delta,
the summand containing fi-gi can be integrated in a different coordinate
j. There are at most two quadratic inverse branches, and the inverse
derivative is at most1/delta. All unchanged densities have capone and
massone. The resulting density difference is at most

    2(d-1)/delta * sum_i ||fi-gi||1.

The other three regions have uniformly small density, independently
of the input product law. Thus, for every eta>0 there is delta>0,
depending only on B and eta, such that

    ||p_F-p_G||infty
       <=6eta+2(d-1)/delta * sum_i ||fi-gi||1.

Smooth compact cap-one laws approximate arbitrary admissible inputs
in L1. Their quadratic output densities are C0: ordinary smooth
submersion charts handle the complement of the critical point, while
the critical-ball contribution tends to zero as r^(d-2).
The stability inequality makes the output approximation uniform.

The same proof supplies an explicit uniform height for the fixed block:

    M_B = C_d ||B||^((d-2)/2)|det B|^-1/2
                     + d^(3/2)/s_d(B),
    C3=2pi, C4=4pi.

Completing affine terms only translates original coordinates, preserving
caps and independence. Every symmetric matrix of rank>=3 has an
invertible physical principal block of order3 or4, found by symmetric
one- or two-coordinate elimination. Conditional output densities for
that block are C0 and bounded by the same M_B, regardless of the
induced affine term. Dominated convergence then proves C0 after
averaging over all outside coordinates.

## Preserved sources

The source reports and exact blob hashes are listed in
paper_work/fleet_gluing_provenance.md and in
source_snapshot/additional_claude/ADDITIONAL_CONTINUITY_SOURCES.json.
The complete proof is in the manuscript; this note records the
preparation-time strengthening of the proof presentation.
