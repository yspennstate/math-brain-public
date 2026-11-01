# Hostile self-review

This review supports only the partial verdict.

1. **Does the source really state this?** Yes, Conjecture 5.7, p.23, including
   optimality. The subsection's sofic context is preserved as a caveat; neither
   the broader intake nor the restricted reading is solved here.
2. **Is a matching later theorem verified?** No. The successful searches found
   related work, not a matching solution. OpenAlex and Semantic Scholar 429
   errors block a complete source citation check. No absence-of-literature
   theorem is claimed. An unverified diagnostic OpenAlex ID is explicitly
   excluded from evidence in LITERATURE.md.
3. **Does cardinality determine the law?** Only under exchangeability. The
   permutation coupling in Section 3 uses this hypothesis explicitly, and is
   not applied to arbitrary regular equivariant kernels.
4. **Does smoothing actually converge?** Yes. Each step preserves the log sum
   and decreases its variance by half the squared range; the range bounds the
   variance by a factor n. The resulting uniform contraction gives convergence.
   Zero eigenvalues are handled separately, with trivial lower comparator.
5. **Could endpoint or complement signs be wrong?** Complementing reverses
   stochastic order and turns Q into I-Q. The upper density is 1-FK(I-Q), not
   FK(I-Q). Finite endpoint couplings are limits in a compact simplex.
6. **Is the conditional quantity odds or probability?** Schur complement s
   is odds. Probability is s/(1+s), yielding HM. The two-site exact example
   exposes the obstruction to the full-rest conditional route.
7. **Does the averaging counterexample refute the DPP conjecture?** No. It
   refutes only a universal heterogeneous-product lemma. Its rational gap is
   exact, its event is increasing and translation invariant, and its probability
   vector is not claimed attainable as equivariant-Q pivots.
8. **Are the sampled matrices genuinely equivariant?** Their initial entries
   depend on g^(-1)h. Hermitian symmetrization and affine spectral functional
   calculus preserve left equivariance, and all eigenvalues are in (0,1).
9. **Does the LP test every increasing event?** Yes, in exact arithmetic:
   every feasible fractional increasing function is an integral of upper-set
   indicators. The solver is floating point, so the observed absence of
   violations is evidence only. Trivial upper sets explain a zero optimum.
10. **Could atom probabilities be wrong?** Boolean Mobius inversion was
   independently checked against det(I-Q)det(J_S) on 15 additional kernels;
   all 190 records also passed normalization and atom nonnegativity checks.
11. **Does compressed log prove all event inequalities?** No. It proves only
   inclusion/absence cylinders. Its operator integral is justified by the
   strict lower spectral bound, with general kernels obtained by regularization.
12. **What is Lean checking?** Only the scalar two-parameter smoothing algebra,
   not the DPP generating identity, smoothing convergence, coupling, or full
   conjecture. No checked proof may contain sorry or native_decide. Initial
   import Mathlib.Tactic.Nlinarith failed because that module is absent; the
   corrected file imports Mathlib.Tactic.Linarith. Final check status is recorded
   below after the shared slot finishes.

Numerical and exact rational verification: `python -X utf8 verify_results.py`
completed with `ALL_CHECKS_PASS` on 2026-10-12 local time. The first verification
run found a script namespace error in the independent cross-check; it was fixed
by providing __file__ to exec, then the entire script was rerun successfully.

Endpoint checks also passed: 80 all-event comparisons for 40 exchangeable
kernels with spectral endpoints, and 600 direct-convolution cardinality
comparisons. The worst count-tail discrepancy was -1.44e-15 (roundoff).
The second Lean run found that real-number notation and instances needed an
explicit Mathlib.Data.Real.Basic import; that import was added before rerunning.

Final Lean check: **PASS (exit code 0)**. `PairBalancing.lean` contains no sorry
or native_decide and imports only Mathlib.Tactic.Linarith and Mathlib.Data.Real.Basic.
Both algebra declarations are kernel checked. One unused-hypothesis linter warning
remains; it does not affect proof acceptance. See LEAN_CHECK.txt for command,
failed-import corrections and the limited scope of the formalization.

Final assessment: **PARTIAL**, with complete written proofs of the claimed
partial results and an exact obstruction to one proposed route. Neither a full
proof, a counterexample to the source conjecture, nor a matching published solution
has been obtained.
