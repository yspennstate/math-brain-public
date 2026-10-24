# Restricted ML10 results: completion, checks, and source boundaries

2 October 2026 UTC. These are complete internally audited restricted
theorems, not a resolution of the full Sidorenko conjecture or the full
ten-vertex Möbius-ladder case. Historical priority and external review
remain unverified. All logarithms and homomorphism normalizations are
specified in the actual proofs; finite certificate arithmetic is exact.

## Strongest completed theorem here

For the uniform host group Z_2^2, let W(x,y)=4p_(x+y), p>=0, and s=sum p.
Let r_1,r_2,r_3 be its three nonconstant Fourier eigenvalues. The full
cycle-surplus proof establishes

t(ML10,W) >= s^15 + 5 s^11 sum_i r_i^4
                         + (8165/567) s^9 sum_i r_i^6.

This family is exactly the equal-diagonal, regular symmetric four-state
host family with equal atom measures. The scope/prior-art proof gives the
elementary row-sum argument for this equivalence. It includes kernels
with negative nonconstant eigenvalues; correlation-kernel prior results
do not directly cover all of it. Arbitrary regular four-state kernels,
unequal atom measures, and general graphons are not covered.

The coefficient 5 is sharp along a one-mode infinitesimal perturbation.
The value 8165/567 is the largest constant supplied by the particular
coefficientwise ordered-gap certificate, not a claim of optimality among
all host kernels. The tempting value 15 is false for an explicitly given
strictly positive rational host; its exact negative surplus is recorded.

Read `continuation_20261002_klein4_cycle_surplus_proof.md` in full and
`klein4_cycle_surplus_k_independent_audit.md`. The independent verifier
`klein4_cycle_surplus_k_independent_verify.py` regenerates the entire
polynomial from direct bipartite host sums rather than assuming the
author's flow expansion. Root read all these files and reran both checks.

## Independent exact routes

1. Direct host assignments, fixing a source vertex only in this
   translation-invariant group family, give the degree-15 density
   polynomial. Fixing a source vertex is not valid for arbitrary regular
   hosts and is not used to assert such an extension.
2. A 16-state Rossman ladder transfer regenerates its whole trace polynomial
   independently. The transfer identity is prior work, explicitly credited.
3. Two independent binary cycle-space flows give 73 Fourier monomials;
   their ordered-gap substitution produces the finite positive certificate.

Every coefficient of 567 times the fourth-order surplus minus 8165 times
the sixth-order cycle sum is checked, rather than inferred from numerical
sampling. Original full certificate JSONs and independent rerun JSONs are
preserved alongside the generators. Floating-point searches are not part
of this proof.

## Schur-convexity result

The independent complete `continuation_20261002_klein4_schur_proof.md`
proves Schur convexity of the density in the four host weights and

t(ML10,W) >= s^15 + 1024 sum_(i<j) |p_i-p_j|^15.

Its derivative quotient has negative raw coefficients; ordering both
weight pairs yields 436 strictly positive coefficients and a retained
61440 D^13 term. The exact quotient, pair symmetry, and integration to the
displayed surplus are reproduced in the proof and audited in
`klein4_schur_k_independent_audit.md`. This is a distinct complete proof
route on the same family, not another general conjecture resolution.

## Rank-one quantitative companion and known qualitative prior art

`continuation_20261002_rankone_quantitative_proof.md` proves

t(ML10,1+lambda f tensor f) >= 1+5 lambda^4+2 lambda^6

for its stated normalized nonnegative rank-one kernels. The independent
audit verifies all finite edge-subset counts and every bound for the
negative eigenvalue regime. Only moments through degree three enter the
cubic source graph. Its qualitative lower bound is already a consequence
of the known two-spin Bethe/Sidorenko theorem; the complete scope/prior-art
file proves the reduction to a valid unequal-measure two-state kernel.
Thus the qualitative rank-one conclusion must not be advertised as new.
The explicit surplus is more specific; its historical novelty is unverified.

Primary sources inspected in this continuation include Csikvári–Ruozzi–
Shams (IEEE TIT 68(9), 2022), whose full author manuscript is at
https://real.mtak.hu/162333/1/Markov_random_fields_Sidorenko.pdf;
Ruozzi (NeurIPS 2012), full manuscript https://arxiv.org/pdf/1202.6035;
Rossman's 8 May 2025 ladder notes,
https://users.cs.duke.edu/~br148/sidorenko-mobius.pdf; and Zhao's
22 June 2026 group-correlation manuscript,
https://arxiv.org/html/2606.23018v1. The precise relation of those results
to these kernels is established in `continuation_20261002_scope_and_prior_art.md`.

The primary September 2025 Fox–Himwich–Mani–Zhou paper, EJC 32(3), P38,
lists ML10 among the small unresolved cases:
https://www.combinatorics.org/ojs/index.php/eljc/article/download/v32i3p38/pdf/.
The bounded current search did not produce a general ML10 solution.
That observation is not a proof of absence, priority, or publishability.
The historical `checkpoint.md` is preserved for source continuity and
does not override the complete later proofs and their explicit scope.

## Verification status

Root read the actual complete proofs, generators and independent audit
files, independently checked their normalization and scope, and reran
the Schur, flow-surplus, rank-one and independent transfer/certificate
scripts successfully. K's independent audit records and exact regenerators
are included. These checks establish internal completion on the stated
families; they do not substitute for external specialist review.

The general spectral proof route, all regular hosts, and unrestricted
Sidorenko remain open here. New candidates belong in subsequent immutable
checkpoints with their own complete proof and independent audit.
