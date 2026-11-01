# High-fugacity negative edge correlation on every weighted finite graph

Research checkpoint, 2 October 2026. This is a complete internally audited
extension beyond the previously archived H2/H3 partial results.

## Theorem and precise boundary

For every finite loopless graph G with fixed positive edge conductances c,
there exists a finite threshold lambda_0(G,c) such that all distinct edge
indicators in the unrooted forest measure with activities lambda c are
negatively correlated for every lambda>=lambda_0. A pair on a common cycle
is strictly negatively correlated for sufficiently large lambda. Edges in
different graphic-matroid components are independent at every positive
lambda. Deterministically absent loops can be removed.

Equivalently, the multivariate forest Rayleigh polynomial evaluated at
lambda c has a positive first surviving coefficient, or is identically zero.
The proof does not claim positivity of all its coefficients.

Full proof and all audits are in
[`proofnet24/P14-probability-correlation/continuations/2026-10-02-all-graph-high-fugacity/`](../../../../proofnet24/P14-probability-correlation/continuations/2026-10-02-all-graph-high-fugacity/).
Read `ALL_GRAPH_HIGH_FUGACITY_PROOF.md`, the root audit, K transfer audit,
adversarial arbitrary-order audit, independent local induction audit, and
source/checks records. The assembled draft and the earlier geometric
checkpoint retaining the then-open transfer gap are preserved.

## What closes the higher-order gap

At delayed order ell, each exact local marked score has only field-scalar
coefficients below ell, and a leading positive semidefinite full-contrast
bilinear at ell. The exact free-port Ward identity controls the next
coefficient, including arbitrary-degree translation-invariant remainders.
Successive normalized conditioning advances the leading nonconstant score
by exactly one order. Its matrix is the explicit electrical response Gram;
the Ward correction completes its raw energy to a sum of squares.

The global mixed coefficient at 2ell is a Green trace square; if it vanishes,
the coefficient at 2ell+1 is a shifted response-wedge square. If both vanish,
support absorption preserves every algebraic and geometric invariant. Both
regions strictly enlarge while remaining disjoint and separated. A finite
graph must eventually reach a positive coefficient or exact one-port
factorization. This treats arbitrarily long leading-zero strings and does
not infer the full result from H2, H3, or a collection of examples.

The off-diagonal signs of the response matrix are unrestricted. Higher
marked scores are allowed to contain common-mode quartics and higher-degree
terms. Thus the two previously recorded failed shortcuts are avoided by
proved transfer identities.

## Verification and prior work

Independent full analytic audits pass. Root reran five direct Fraction
exterior-algebra score calculations at delayed orders1,2,2,3,3 and four
complete forest-frontier comparisons through H4/H5/H6, including a
14-vertex asymmetric three-port case. These finite tests support powers and
normalization; the theorem rests on the all-orders analytic induction.

The forest/Grassmann representation and supersymmetry tools are classical.
The current primary arXiv:2610.00549v1, submitted30September2026 and checked
2October2026, supplies the first two coefficients and equality geometry;
the new proof explicitly continues their simultaneous-zero case. Huang's
2023preprint/2024journal theorem supplies older adjacent-edge large-parameter
results. No earlier complete proof of this precise theorem was found in
the bounded primary-source search. Priority and external peer review remain
unverified.

Full Kahn negative correlation at every positive fugacity, the weighted
all-fugacity Rayleigh conjecture, negative association, and the q<1
random-cluster conjecture remain open here. A separate integer-conductance corollary supplies a crude explicit threshold
1+2 product_(g!=e,f)(1+c_g)^2; for an unweighted m-edge graph it is
1+2*4^(m-2). It follows from coefficient integrality and an exact l1 bound,
and was independently audited. No practical or optimal threshold is claimed. Unrestricted Boolean FEI also remains open, while
the deterministic-LTF theorem in derived-04 is established internally.

## Next boundary

Pursue an audited extension to all fugacities, a quantitative threshold or
another major unresolved target. For FEI, examine the proposed strengthened
LTF entropy-versus-influence-deficit inequality and consequent read-once
formula extension; do not treat them as proved before full audits. A
finite-crossing threshold route has a new rare-pivot split obstruction being
developed separately. Preserve its failed approach if completed.
