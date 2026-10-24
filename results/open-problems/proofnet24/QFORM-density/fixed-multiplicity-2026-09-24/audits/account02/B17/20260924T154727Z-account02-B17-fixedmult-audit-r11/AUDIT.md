# account02/B17 r11 — fixed-multiplicity end-to-end audit

Objective: QFORM-FIXED-MULTIPLICITY-AUDIT-20260924.

Pins:
- baseline: commit 7c0d6e60946b19423e6400a12d34b473cf0591e2, blob 183ccd294763214e6a707e8d4749ff9a8cf7006d, advertised SHA-256 9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69, 790 lines.
- current nine/400 source: commit eeb752c8943536541b34b42b8bf48e924f4d3d2f, blob 19fb119877426b640b2c0dae19ec2f78a399fe11, advertised SHA-256 bf1caf6ae4b4bc33992f501c169b5dc6c795db757b0f6089eff9991391effdf3, 955 lines.

I read the full requested master package: README, SOURCE_MANIFEST, manuscript.tex, AUDIT, proof_map, verify.py, checks.json, plus the complete nine/400 package README, NINE_400_AND_OVERLAP, AUDIT_NEW, MANIFEST, proof_map, verify_new and checks_new, and DELIVERY_STATUS.

Verdict: baseline 17 theorem PASS mathematically. Current standalone s9 <=400 K^2/s theorem PASS mathematically in this independent audit. No mathematical FALSE or unresolved GAP found. Independent raw-byte SHA-256 recomputation, fresh checker execution, and exhaustive bibliographic priority remain UNCHECKED; none is a proof dependency.

Baseline line coverage:
- 1–46 PASS: definitions/conventions/quantifiers.
- 47–80 PASS: theorem, normalization, scaling.
- 81–160 PASS: Fourier/Plancherel/inversion/Riesz constants and rough limits.
- 161–217 PASS: singular-value rank perturbation, singular Schur count, diagonal dominance. In the singular Schur step, s_m(S_eps)>=t-|eps| and continuity gives s_m(S)>=t.
- 218–301 PASS: geometric BL, product projection, scalar Fourier powers; deterministic rotations only.
- 302–400 PASS: independent-copy decoupling, graph determinant/Jacobians, crossing volumes.
- 401–525 PASS: square/definite/hyperbolic pivots and exceptional-slice handling.
- 526–645 PASS: quarter concentration, sampled interpolation, completion; global rank <=3r, restricted LxL rank <=r, D vanishes on the seed, E has zero diagonal.
- 646–724 PASS: spectral-to-volume, random cut, no-pivot and singular kernels.
- 725–790 PASS: full/truncated half potentials, exhaustive 17-direction branch assembly, K^2/s scaling.

Nine/400 line coverage:
- 1–46 PASS: scope and conventions.
- 47–66 PASS: s9 theorem and pivot parameters.
- 67–164 PASS: Fourier/Riesz layer.
- 165–203 PASS: rank and Schur count.
- 204–297 PASS: BL/projection/scalar Fourier powers.
- 298–396 PASS: decoupling, determinant and volume envelopes.
- 397–527 PASS: grouped physical-product compiler. The mollified light-bank L2 step, weighted Holder, subset entropy, literal-row promotion and q=3/q=2 receivers preserve original-coordinate product provenance. C3=3 sqrt(2)e(9/2)^(1/6), C2=8 sqrt(e)2^(-1/8).
- 528–662 PASS: scalar/definite/hyperbolic pivots and quarter concentration.
- 663–766 PASS: sampled interpolation, both rank bounds, s5/s9 volume consequences, fair cut.
- 767–860 PASS: full pair half-potential, five-direction half-potential and normalized s9 branch assembly.
- 861–925 PASS: overlap-tail theorem; only invertible seeds are inverted and the Frobenius/Eckart-Young argument is correct.
- 926–955 PASS mathematically: threshold accounting and limitations correctly do not claim s8 or s3.

Adversarial checks:
- No post-rotation independence was found.
- Nonsymmetric auxiliaries are used only with singular-value inequalities.
- Full and truncated half potentials are not conflated.
- Fourier branches give C0 regularity, but the global theorem claims only essential boundedness.
- Finite checker outputs are treated as diagnostics, not proofs.

Lower-threshold result of this run: the companion improvement file gives a complete s8 replacement proof with safe constant 2371 and an s7 structural router. Thus this run certifies multiplicity 8; multiplicity 7 remains open; unrestricted multiplicity 3 remains open.
