# P20 immutable readback correction — 2026-09-16 18:50:35Z report

Canonical report being corrected:

`proofnet24/P20-closure-log-unimodality/runs/2026-09-16/2026-09-16_18-50-35Z__run-report.md`

This note preserves the immutable original report and clarifies two proof dependencies in Section 6. It changes **no theorem statement, metric, source status, audit count, or checker result**.

## 1. Strict local maxima in Section 6.5

The sentence claiming that local constancy would contradict a strict derivative sign “in the same certified component” is stronger than needed and was not the cleanest dependency.

Use the following argument instead.

At every certified sign-pair interval for the compact staircase output, Ji gives continuity and therefore an interior positive maximizer. By AHK Theorem 1.9, the density is real analytic on every connected component of the positive-density set. Suppose such an interior positive maximizer were not strict. Then there is a sequence of distinct points with the same maximal value accumulating at that maximizer; analyticity forces the density to be constant, equal to some `M>0`, on the entire connected positive-density component containing it.

The compact staircase inputs are supported in `[e^{-A},e^A]` for finite `A`, so the product law is compactly supported on `(0,infinity)` and its logarithmic density has compact support. Thus the positive-density component cannot be all of `R`. At a finite endpoint of that component, global continuity forces the limiting density value to equal `M>0`, contradicting that the endpoint lies on the boundary of the open positive-density set. Hence the component cannot carry a positive constant density. Therefore each sign-pair interval contains at least one **strict** positive local maximum.

This supplies the strict modes needed for the neighborhood-margin argument (6.9) without any assumption that an endpoint derivative sign lies in the same analytic positive-density component.

## 2. Boundary fixed-point stability in Section 6.6

The clean branch-stability dependency is the following.

For the compact staircase pair, each selected strict mode has positive finite output density. The multiplicative subordination boundary values are therefore interior upper-half-plane values at those points. AHK Proposition 7.1 shows that if the relevant boundary self-map is a conformal automorphism then both input measures must consist of two atoms. Our staircase inputs are atomless, so that exceptional automorphism case is excluded. The Denjoy-Wolff fixed point is therefore non-automorphic, its derivative has modulus strictly below one, and the analytic implicit-function theorem applies to the physical fixed-point equation. On finitely many compact strict-mode neighborhoods, the gaps and transform denominators can be made uniform.

Combined with the `L^1` Gaussian-smoothing convergence and the uniform kernel bounds already proved in (6.7)–(6.8), this gives local uniform convergence of the physical subordination values and output densities for `mu_sigma boxtimes mu_{2sigma}` to those of the compact self-product. The strict-mode margins in (6.9) therefore persist for all sufficiently small unequal smoothing widths.

## 3. Status after correction

The following claims remain exactly as stated in the canonical report:

- `P20-I0081-OUTER-SCALE-WINDOW-09 = PROVED`.
- `P20-I0081-OUTER-ALGORITHM-FAILURE-WINDOW-09 = PROVED`, scoped to the run-08 universal algorithm.
- `P20-I0081-SMOOTH-DISTINCT-UNBOUNDED-09 = PROVED / P20 self-check only`.
- `P20-I0081-ROBUST-K-MODES-09 = PROVED / P20 self-check only`.
- Frozen metric: `UNBOUNDED -> UNBOUNDED`.
- Source Problem 4.3: `REFUTED`.
- Campaign closure: `OPEN, 1/2 qualifying OTHER-track audits`.

No checker was rerun or rearchived for this correction.

END OF IMMUTABLE READBACK CORRECTION
