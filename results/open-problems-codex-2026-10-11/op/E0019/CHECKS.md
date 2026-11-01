# Verification record, 2026-10-12

## Lean 4

`Algebra.lean` was checked from `~/lean_verify` using

    lake env lean ~/brain_workers/TRIO_1011/op/E0019/Algebra.lean

Final exit code: **0**, no output or warnings. Full result: `lean_result.json`. The subprocess timeout was 3,600 seconds as requested for Lean; actual runtime was about 73 seconds, below ten minutes. Only one Lean invocation ran at a time.

Imports are `Mathlib.Data.Real.Basic`, `Mathlib.Tactic.Ring`, and `Mathlib.Tactic.NormNum`. There is no `sorry`, `native_decide`, or unrestricted `import Mathlib`. The proofs use `ring` and `norm_num` with kernel checking. They establish identities over the reals for the affine drift determinant, bracket coordinates, constant rank determinant, controllability determinant, the source's homogeneous determinant, and the L^p threshold algebra. They do not formalize the analytical arguments in ATTEMPT.md.

The first invocation failed because PowerShell had written a UTF-8 byte-order mark at the beginning of the Lean file. The file was rewritten as UTF-8 without that mark, the polynomial variables were upgraded from rationals to reals, and the final invocation passed. No failed invocation is counted as checked mathematics.

## Symbolic and numerical checks

Run `python -X utf8 checks.py` in this folder. Results are in `numerics.json`.

- SymPy gave `det(F_0,F_1)=2*y`, `Aa=(-1,1)`, `A^2a=(0,-2)`, and `det(Aa,A^2a)=2` exactly.
- All 300 finite-difference comparisons of the fixed-time two-switch endpoint Jacobian passed. Maximum absolute error: about `1.63e-10`; minimum absolute exact determinant among the sampled cases: about `0.01166`.
- The critical-annulus exponent is symbolically exactly zero at `p=2/(2-lambda)`. This supports checking the endpoint in the proof; the proof of divergence uses disjoint annuli, not numerics.
- Generated 30,000 samples of the stationary convolution at `(lambda_0,lambda_1)=(0.5,3)`, with seed 190019 and backward-time cutoff 30. Two-state reversibility justifies using the same jump rates backward. The deterministic tail norm is at most `sqrt(2)*exp(-30)`, about `1.32e-13`.
- Empirical mode-0 masses of balls of radii `0.2, 0.1, 0.05, 0.02, 0.01` were approximately `0.653, 0.510, 0.381, 0.251, 0.179`. All exceed the respective proved lower bounds `0.271, 0.192, 0.136, 0.0857, 0.0606`, using R=2. This is only numerical evidence.
- The numerical job itself took less than a second according to its timer and uses small arrays, well below 1 GB. There are no images, background workers, services or repository changes.

## Hostile-referee review

The analytical proof was rechecked for the following possible failures: incorrectly normalized mode densities; fixed-time versus variable-total-time switch derivatives; an invalid stationary-to-invariant implication; assuming bracket conditions automatically smooth densities; losing the critical L^p endpoint; forgetting the additional time-window factor during singularity propagation; and assigning intrinsic values to a density at individual points. The complete argument in ATTEMPT.md explicitly addresses each issue.

A further endpoint audit strengthened the propagated-curve obstruction: using the L^p norm on the shrinking tube itself, rather than on its fixed neighborhood, shows failure also at p=1/(1-lambda_0). The norm tends to zero by absolute continuity of the Lebesgue integral. At the end of the first attempt there was no matching L^p upper bound or full singularity classification. The follow-up below supplies exact finite-p bounds for the common-matrix affine family and exact C0 boundedness/continuity for the spiral. The full nonlinear and higher-differentiability classification remains unresolved.

## Second-attempt checks, 2026-10-12

Complete analytical proofs and the separate referee checklist are in `FOLLOWUP.md`, Theorems A and B and Corollary C.

### Lean

`lake env lean ~/brain_workers/TRIO_1011/op/E0019/FollowupAlgebra.lean` ran from `~/lean_verify`, with a 3,600-second timeout, one invocation at a time. The final invocation returned **exit code 0** in about 42 seconds. Its only warnings concern an unreachable, redundant `ring` tactic after `field_simp` had already solved a goal. No failed invocation is counted as checked mathematics.

Imports are only `Mathlib.Data.Real.Basic`, `Mathlib.Tactic.FieldSimp`, `Mathlib.Tactic.Ring`, and `Mathlib.Tactic.Linarith`. There is no `sorry`, `native_decide` or unrestricted Mathlib import. It checks the exact equivalence between the shell exponent being nonnegative and the rate being at or below D(1-1/p), for real variables with p>0, together with the source's threshold simplification and the linear relation used in the three-pulse implicit-function argument. It does not formalize the submersion theorem, Neumann-series measure argument, or support/positivity proof. Final raw result: `followup_lean_result.json`.

Initial Lean invocations failed because `Mathlib.Tactic.Nlinarith` was not an available compiled module, and because ASCII `!=` denotes a Boolean expression rather than the intended proposition; a Unicode replacement was then mangled by PowerShell stdin encoding. The final source uses the explicit proposition `Not (p = 0)` with the available `Linarith` module. No dependency was built or written outside the problem folder.

### Reproducible numerical and symbolic diagnostics

Run `python -X utf8 followup_checks.py`; raw results are in `followup_numerics.json`. The job itself took about 2.3 seconds and used small matrices and arrays, far below 1 GB.

- **240 fixed-time switch Jacobians**, 60 each for a scalar model, the source spiral, a stable nonnormal Jordan model, and a three-dimensional diagonal model: all passed. The largest finite-difference absolute error was about 2.47e-10. Controllability determinants were respectively 1, 1, -2 and 2, and every tested switch-map determinant was nonzero.
- **Four remainder-contraction examples:** exact finite-count killed-CTMC matrix exponentials were below the proved Poisson low-switch-count bounds. With a stated extra cutoff-loss budget, the resulting Lp remainder norm bounds were about 0.358, 0.255, 0.250002 and 0.250035, all strictly below 1. This numerically checks the order of parameter choices and the volume/probability balance; the existence of smooth cutoffs is proved analytically.
- **Three positive pulses:** the numerical implicit-equation solution had lengths approximately 0.0005933, 0.0049330 and 0.0402715, residual norm 4.46e-17, and first-two-column derivative determinant 0.141829. All pulse lengths were positive and shorter than pi/3. The scaled 120-degree linear relation had residual 8.98e-14. The initial tolerance of 1e-14 was too strict for the matrix-exponential floating-point evaluation and was changed to 1e-11; the proof uses the exact rotation identity, not this tolerance or numerical root.
- **Boundary-case symbolic test:** for A=-1 and rates (1,2), the explicit invariant component masses are 2/3 and 1/3, the stationary flux residual is exactly zero, and the total density is 2-2x on (0,1). It is bounded at m=D. This checks that the spiral's critical L-infinity conclusion is not silently generalized to all A.
- **One-dimensional finite-p exponent:** SymPy verifies exactly that p(lambda/alpha-1)+1=(p/alpha)[lambda-alpha(1-1/p)], matching the theorem and the explicitly known beta-density boundary exponents.

### Remaining analytical limitations

The finite-p and spiral C0 classifications are complete within their stated model classes. The local positive density lower bound is proved by a positive smooth subkernel, not inferred from support membership. Critical divergence is a logarithmic lower bound, not an exact asymptotic. Higher differentiability at every rate pair, matching local bounds at all propagated curves, and arbitrary nonlinear or state-dependent-rate regularity remain unresolved. There is no claim of publication novelty from the narrow additional literature search.
