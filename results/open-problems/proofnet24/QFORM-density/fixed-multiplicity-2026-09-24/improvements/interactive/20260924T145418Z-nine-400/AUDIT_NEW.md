# Self-audit of the nine-eigenvalue, constant-400 manuscript

Source commit: eeb752c8943536541b34b42b8bf48e924f4d3d2f.
Git blob: 19fb119877426b640b2c0dae19ec2f78a399fe11.
SHA-256: bf1caf6ae4b4bc33992f501c169b5dc6c795db757b0f6089eff9991391effdf3.

## Verdict

No fatal mathematical gap identified in this authoring-agent reconstruction. This is a self-audit, not independent review, journal peer review, or formal verification. The threshold-nine mechanism predates this run (account03/B04); the new synthesis uses separate scalar/pair pivot thresholds, a full pair half-potential estimate, and new constants. The overlap theorem is supporting progress for eight eigenvalues, not a solution at eight.

## Audited transitions

1. Full input quantifiers and K^2/s scaling: preserved. Independent original-coordinate laws only; arbitrary affine terms, signs, spectrum and dimension.
2. Grouped Fourier proof: Jensen applies first to mollified L2 norms; the pure J phase is discarded only after integrating the original I coordinates. The kernel is a nonnegative probability density but its induced measure need not be normalized; Holder is valid for that finite measure. Conditional image densities have a legitimate L2 bound. Hub variables are literal independent coordinates, not rotated coordinates.
3. Row promotion: exact Gram-Schmidt incident-volume identities; at most q promotions; all hub-to-left couplings retained; terminal leftover coordinates conditioned upon. q=3 gives density and q=2 gives only a half potential.
4. Parameter retuning: d=3/40, p=1/400, sqrt(kappa)=2/25. Exact r=1 and r=2 diagonal-dominance slacks 1131/2200 and 51/2200. Thus volume orders two and three need five and nine large eigenvalues.
5. Pivot analysis: full pair half-potential scales as D^(-1/4), not D^(-1/2). The logarithmic envelope is integrated by rearranging interval overlaps, not by assuming symmetric input laws. Scalar full/truncated moments remain distinct.
6. Final bounds: no pivot<375; scalar/no-pivot remainder<280; scalar/scalar remainder<383; scalar/pair remainder<320; definite pair<80; indefinite pair<392.5. Hence400 is safe.
7. Spectral-overlap proof: D diagonal and E zero diagonal give exact Frobenius orthogonality. Best-rank approximation plus volume sampling yields W+(r+1)^2 V_(r+1)>=V_r sum_(j>3r)s_j^2, including nonsymmetric real A. Singular seeds are excluded from the equality defining W.
8. Baseline presentation clarifications included: globally pointwise-bounded Borel density representatives; explicit zero-weight projection sum; fixed-threshold proof for singular Schur complements.

## Executed checks and production

verify_new.py passed96 exact interpolation seeds and8 complete aggregate overlap/sampling comparisons, including symmetric and nonsymmetric matrices. Eight floating spectral-tail comparisons are diagnostics, not exact certificates. All finite constants were checked with fractions.Fraction. No finite experiment is presented as a proof in all dimensions.

The standalone source compiled in three pdflatex passes to20 pages. All20 pages were rendered and visually inspected. No undefined references, overfull boxes, clipping, or broken glyphs were identified. One underfull paragraph warning is cosmetic. No external theorem, source manuscript, figure or bibliography file is required to compile paper.tex. Classical references were checked against their primary arXiv records; this was not an exhaustive novelty search.

## Below nine

The improved eight-eigenvalue inequality is W^cross_(2,1)>=2 V_2-9 V_3. An analytic receiver for the shared original coordinate is still required. The attempted max-determinant-seed shortcut controls the completed diagonal, but does not automatically preserve the volume-sampled Frobenius error; no threshold-seven claim follows. These limitations are recorded in the full mathematical handoff.
