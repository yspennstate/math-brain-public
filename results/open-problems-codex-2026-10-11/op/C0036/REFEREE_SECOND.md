# Hostile self-review of the additional attempt

The additional theorem is a finite scalar-neighborhood special case. It does
not solve the all-kernel or all-group conjecture. Proof: SECOND_ATTEMPT.md.

1. **Russo applies to a product law, not a DPP.** The proof first expresses both
   expectations with the same multilinear coefficients. Only the iid polynomial
   F is differentiated by the pivotal formula. The DPP term is differentiated
   independently by the determinant's permutation expansion.
2. **Could equivariance be replaced just by equal diagonal?** No. The quadratic
   edge redistribution needs constant row energy of the perturbation. Transitive
   equivariance supplies it, and extracting within/cross blocks preserves it.
   The new theorem does not assert a neighborhood for arbitrary equal-diagonal
   kernels lacking a transitive symmetry.
3. **Could an odd complex cycle alter the leading coefficient?** Odd cycles
   contribute at order >=3. Transpositions give -|H_ij|², even for complex H.
   The exact symbolic test uses a genuinely complex Hermitian circulant H.
4. **Is nonnegative quadratic variation enough?** No. This was the main danger.
   The proof classifies zero coefficients by minimal accepted subsets, proves
   exact equality on the entire associated block-diagonal subspace, and proves
   that first cross derivatives vanish at every point on that subspace.
5. **Is the zero classification exact?** Yes. A pivotal configuration with j
   absent gives a minimal set containing i but not j, and such a minimal set
   gives a pivotal configuration. Strictly positive product weights are essential;
   this is why t is in (0,1). The equivalence relation uses membership in all
   minimal sets, not just the support graph of one chosen perturbation.
6. **Are the blocks invariant and equally sized?** Invariance of U permutes its
   minimal sets. It therefore preserves their membership equivalence relation.
   Transitivity on sites then maps any class onto any other class. No normality
   assumption about a subgroup is used.
7. **Does block diagonal imply equality for the whole event?** For the event's
   inseparability partition, yes: every minimal accepted set is a union of full
   blocks. The event is determined by block-full indicators. Independent blocks
   with identical determinants give the same indicator law for the DPP and its
   homogeneous FK iid comparator. An arbitrary block partition would not suffice.
8. **Could a nearly zero direction spoil a nonuniform Taylor estimate?** The
   integral Taylor expansion is in B with A fixed, and both the value and first
   derivative at B=0 vanish exactly. Its error scales with ||B||_F², rather than
   an uncontrolled O(||A+B||³). The scalar cross Hessian is uniformly positive
   on the whole cross-block linear space. This addresses varying directions too.
9. **Does Hessian continuity prove a common event radius?** Yes: there are finitely
   many invariant upper sets. The stronger quantitative argument bounds the third
   derivative uniformly over all Boolean events, bypassing their enumeration.
10. **Check the explicit constant.** The indicator coefficient sum is bounded
    by 3^n. Mixed determinant derivatives select distinct columns, bounded by
    Hadamard. For p=exp((log det Q)/n), all inverse/trace derivative estimates
    use eigenvalues >=c and Frobenius norms. The third chain-rule bound is
    L=3^n[n^3+(n^3+6n^2+6n)/c^3]. One pivotal configuration gives gamma_*
    >=a^(n-2)/(2T). Radius (7) makes Hessian variation <gamma_*/2, and covers
    both t and 1-t. It is a sufficient, highly conservative radius.
11. **Does the invariant-event argument give every increasing event?** Average
    its indicator over the finite group, decompose that finite-valued invariant
    function by upper-level events, and use invariance of both measures. This
    is a full event comparison, not just cardinality comparison.
12. **Is optimality proved?** Yes, using the all-present and all-absent events
    on the finite set. For the subgroup-supported infinite family, the same
    necessity test uses a single finite coset; finite Strassen couplings are
    independently multiplied over the countably many cosets.
13. **Does this close the original gap?** Only locally for finite groups, and
    for the displayed subgroup-supported infinite family. The explicit radius
    decays with n. Neither a global continuation along a kernel path nor a
    uniform finite-to-infinite approximation has been proved.

Checks completed so far:

- `pivotal_checks.py`: all 168 increasing events on four sites passed exact
  determinant-coefficient/pivotal comparisons and zero-coefficient classification.
  All eight C4-invariant events also passed equal-block determinant, exact
  block-diagonal equality and vanishing cross-derivative checks.
- `near_flat_checks.py`: 144 spatial event comparisons on D4 at 80 digits passed,
  using C4 and nonnormal C2 coset partitions, multiple internal strengths and
  signed cross strengths from 10^-2 down to 10^-7. Minimum gap/cross-strength²
  was about 0.94159. These sampled strengths are not asserted inside radius (7).
- `certified_radius_checks.py`: passed 1008 all-event comparisons at 80 digits inside the explicit radius.
- `PivotalIdentity.lean`: the initial direct nlinarith proof did not substitute
  a defining equality before multiplying it by t. It was replaced by explicit
  rewriting and ring normalization; final check passed with exit code 0. No failed
  run is called checked, and no sorry/native_decide is used.

An additional hostile test disproves a tempting weakening of the theorem:
constant row energy plus equal diagonal is not enough. The triangle-plus-pair
five-site family in SECOND_ATTEMPT.md has nonnegative quadratic variation but
a negative cubic gap for the two-site full-occupancy event. Its component sizes
are unequal, so step 4's equal normalized block determinants cannot hold.
This confirms why the transitive symmetry hypothesis and exact equality
subspace are essential. The auxiliary counterexample is not equivariant under
a transitive action and does not refute C0036.

The certified-radius script completed successfully: 1,008 all-event comparisons
at 80 digits, with rigorous norm bounds strictly inside radius (7). Equality
roundoff was of order 10^-82, while every nontrivial non-top gap was positive.
The explicit radius therefore was tested as stated, rather than only at sampled
perturbation strengths whose inclusion in the analytic neighborhood was unknown.

The exact auxiliary boundary script also passed. At t=1/2,epsilon=1/100 its
strict power-comparison margin d3²-d2³ is 61489/125000000000>0. This is an
exact counterexample only to the row-energy weakening. The mathematical
self-review supports the finite-neighborhood theorem and subgroup-supported
corollary, with the original global conjecture still unresolved.

Final Lean check **PASS, exit code 0**, with no compiler output. All three
declarations in PivotalIdentity.lean are kernel checked, without sorry or
native_decide. LEAN_SECOND_CHECK.txt records the command, corrected tactic
failure, and the limited scope. The full neighborhood theorem is a written
analytic proof, not a Lean formalization.

Final assessment: **DONE / PARTIAL**. The additional attempt establishes a
stronger special case, with an explicit uniform finite-group scalar radius;
no full proof, C0036 counterexample or matching published solution was found.
