# account02/B01 fixed-multiplicity audit and improvement

Run: 20260924T171028Z-account02-B01-fixedmult-m8-audit
Objective: QFORM-FIXED-MULTIPLICITY-AUDIT-20260924
Lens: theorem quantifiers, scaling, dependency closure; account02 counterexamples.

## Source pins

Active nine-eigenvalue candidate:
commit eeb752c8943536541b34b42b8bf48e924f4d3d2f
paper.tex blob 19fb119877426b640b2c0dae19ec2f78a399fe11
recorded SHA-256 bf1caf6ae4b4bc33992f501c169b5dc6c795db757b0f6089eff9991391effdf3
length 955 lines.

Preserved seventeen-eigenvalue baseline:
commit 7c0d6e60946b19423e6400a12d34b473cf0591e2
manuscript.tex blob 183ccd294763214e6a707e8d4749ff9a8cf7006d
recorded SHA-256 9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69
length 790 lines.

Separate nine-eigenvalue reconstruction required by the fresh owner objective:
retrieved at math-open-problems master 5b116380e01d27aab636d962fec9b60e0fb91121
paper.tex blob 823201f05363fcc60c38cce0feb5abb636f081d7
MANIFEST SHA-256 ea56bc35cff9815db71a9f5a620e0160e3a39cf53ff60c789707294d53240eba.

## Active 955-line audit verdict

Mathematical theorem: PASS.
Support-package source binding: one reproducibility GAP, described below.
Global continuity: not claimed by the theorem and not inferred here.
Multiplicity eight: OPEN.
Multiplicity three: OPEN.

I read all 955 lines of the pinned source and reconstructed every proof rather than using prior PASS files as evidence.

Continuous line coverage:
- lines 1-46, setup and problem quantifiers: PASS. Independent coordinate densities <=K, arbitrary real symmetric A, arbitrary b,c, arbitrary dimension, remaining spectrum and signs all remain quantified.
- 47-75, main theorem, interval form, scaling architecture and parameters: PASS.
- 76-164, Fourier normalization, power envelopes, Gaussian inversion and negative-half Riesz interface: PASS.
- 165-215, singular-value rank perturbation, Schur-count lemma including singular A, diagonal dominance: PASS.
- 216-297, geometric Brascamp-Lieb heat flow, product projection density, scalar integrated Fourier powers: PASS. Zero-weight rows are omitted safely and rough densities are handled by monotone approximation.
- 298-396, decoupling, regularized determinant, Cauchy-Binet and volume envelopes: PASS. The fourth-root exponent and constants are consistent with the stated Fourier normalization.
- 397-527, grouped mollified-L2 argument, entropy bill, heavy-row promotion and free-volume receivers: PASS. Pure-block phases are discarded only after the legitimate decoupling/mollification step; every promoted hub is a literal original coordinate; alpha_i<=1/2 is used exactly where the scalar Fourier-power exponent must be >=2.
- 528-662, scalar square profile, definite pair, indefinite hyperbolic pair and quarter-power/log concentration: PASS. No post-rotation independence is used.
- 663-766, pivot-volume definition, determinant sampling, nonsymmetric completion, global rank <=3r, restricted rank <=r, spectral-to-volume conversion and random cut: PASS. D vanishes on the seed; E has zero diagonal; the diagonal-dominance margins for r=1,2 are positive.
- 767-860, singular kernels, full pair half-potential, five-eigenvalue half-potential and final pivot assembly: PASS. The proof uses the full, not merely truncated, half potential where the scalar square profile requires it.
- 861-934, invertible-seed overlap theorem and s8 corollary: PASS. The exact expectation is only over invertible seeds; singular seeds are not silently included. Frobenius orthogonality of diagonal D and zero-diagonal E is exact.
- 935-955, threshold remarks and bibliography: mathematical threshold/status remarks PASS. External priority/bibliographic exhaustiveness is UNCHECKED in this run and has no theorem dependency.

All proof-map labels were checked against their hypotheses and uses:
thm:main, eq:main, cor:33, eq:parameters, lem:fourier, eq:plancherel, eq:inversion, eq:gaussian-inversion, lem:envelope, eq:envelope, lem:riesz, eq:riesz, eq:riesz-power, lem:rank, eq:rank-perturb, lem:schur, lem:dd, thm:bl, eq:frame, eq:bl, lem:projection, eq:projection, lem:scalar-fourier, eq:scalar-fourier, eq:cross-form, lem:decoupling, eq:decouple2, eq:decouple4, thm:determinant, eq:determinant, eq:graph-bl, eq:Zk, eq:det-expand, cor:vol-fourier, eq:vol-envelope, eq:five-volume, eq:three-volume, lem:grouped, eq:grouped-form, eq:grouped-envelope, eq:grouped-constant, eq:hub-cs, eq:mollified-light, eq:subset-bound, eq:subset-entropy, lem:terminal, eq:terminal, thm:free-volume, eq:free-three, eq:free-two, lem:square, eq:profile, lem:definite, lem:hyperbola, eq:hyperbola, eq:hyper-coarea, lem:quarter, eq:quarter, eq:log-bound, def:pivot-volume, eq:Vr, eq:small-entry, lem:sampling, eq:P, eq:sampling, lem:completion, eq:completion, eq:completion-bounds, prop:volume, eq:volume-lower, lem:cut, eq:cut, cor:no-pivot, eq:no-pivot-five, eq:no-pivot-nine, lem:kernels, eq:J, lem:pair-full, eq:pair-full, prop:five, eq:five-half, eq:scalar-branches, eq:W, thm:overlap, eq:overlap-tail, eq:orthogonal-error, cor:eight-overlap, eq:eight-overlap, eq:eight-explicit. Verdict on each mathematical label: PASS.

## Dependency/scaling closure

Normalized K=s=1 proof closes all cases. Rescaling Y=KX and A/s gives the density scale K^2/s. No branch introduces moments, compact support, log-concavity, identical distributions, rotated-coordinate independence, or a signature restriction.

The no-pivot branch is the only place multiplicity nine is used. Scalar pivot removes one spectral direction and then uses a lower-multiplicity half-potential theorem; pair pivots are paid directly. The overlap section is supporting structure only and is not used to claim multiplicity eight.

## Support package audit

README.md and MANIFEST.json: PASS as provenance records for the pinned paper identity.
proof_map.csv: PASS against the 955-line source.
checks_new.json: PASS only as the recorded finite diagnostic output; it is not universal proof.
AUDIT_NEW.md: UNCHECKED AS INDEPENDENT EVIDENCE; it is the authoring self-audit and was not used for this verdict.
verify_new.py: GAP in reproducibility/source binding only. It does not read or hash paper.tex and does not compare the source with the pinned SHA before running. A changed paper could therefore leave this checker PASS. Repair: add a pinned paper SHA-256 check, as the preserved baseline verify.py does. Downstream mathematical impact: none on this audit, which reconstructs the pinned proof directly.

## Preserved 790-line baseline

The preserved 17-eigenvalue manuscript.tex was also read in full, together with root README.md, SOURCE_MANIFEST.json, AUDIT.md, proof_map.csv, verify.py and checks.json. Its theorem/scaling, Fourier determinant estimate, pivots, sampling/completion, singular-Schur limit and final 17-eigenvalue assembly are PASS. The baseline verify.py is source-bound. This baseline is preserved history, not the current best threshold.

## Comparison with the separate nine-eigenvalue paper

The fresh owner objective also names proofnet24/QFORM-density/nine-eigenvalues-paper-2026-09-24/. I read its README.md, AUDIT.md, MANIFEST.txt and paper.tex in full.

No mathematical disagreement with the pinned 955-line paper was found.

Common core:
- identical theorem quantifiers and K^2/s scaling;
- identical pivot thresholds eta=3/40 and zeta=1/400, kappa=4/625;
- same grouped crossing-volume mechanism, heavy-row promotion and product-projection input;
- same nonsymmetric completion and 4k-3 spectral-to-volume count;
- same full two-coordinate half-potential scale 16 |det B|^(-1/4).

The separate paper uses a stronger one-direction concentration estimate based on the first crossing volume, giving
P(|R-a|<rho) <= 19 sqrt(rho/||S||)
and L0=2+2 log 19<8. This changes constants but not hypotheses. Its four normalized theorem branches are approximately:
no pivot 370.4585; scalar pivot 299.422; definite pair 62.832; indefinite pair 333.598.
Thus that reconstruction actually proves a safe <375 bound, while stating 400. This is compatible with, and stronger numerically than, the active 400 statement.

Its Lean files formalize many finite/algebraic/constants interfaces but not Fourier inversion, Brascamp-Lieb or the full analytic grouped theorem. Those analytic pieces were checked here from the written proof, not accepted from Lean or numerics.

This run is still one account02/B01 review. It does not self-award a two-independent-review release certificate.

## New counterexample-driven improvement

Packet diffusion does not imply coordinate diffusion.

Take coordinates h and seven disjoint pairs (u_i,v_i), set a=1/20 and eps=1/32, put A_hh=a and A_{u_i,v_i}=A_{v_i,u_i}=eps, all other entries zero.

No pivot: a<3/40 and every nonzero principal pair determinant has modulus eps^2=1/1024<1/400.

Exact disjoint volumes:
V2 = 4*C(7,2)*eps^4 = 21/262144 > kappa^2.
V3 = 8*C(7,3)*eps^6 = 35/134217728 < kappa^3.
V3/V2 = 5/1536 < kappa.

Every nonsingular two-seed consumes two matching edges. Every external leaf has zero same-index bordered determinant; h is the unique nonzero overlap anchor and det(border)=a det(seed). Hence there are exactly 84 nonzero overlap packets, all equal weight:
max_p w_p = 1/84 < 1/64,
but anchor incidence alpha_h=1.

Therefore the implication
  diffuse packet weights => all physical-coordinate role marginals <=1/2
is FALSE, even at the active no-pivot V2/V3 numerical scale.

This is not an s8 counterexample: its spectrum is {1/20, +1/32 x7, -1/32 x7}. Precisely the missing spectral provenance is visible:
W/V2=1/400 here,
whereas s8>=1 plus the audited overlap theorem would force
W/V2 >= 2-9(V3/V2) = 1009/512 > 1.97.

So a valid multiplicity-eight proof must keep and spend the strong s8-derived W/V2 energy; the packet entropy bound alone cannot infer the alpha_i<=1/2 hypothesis needed by a direct Hölder receiver. A heavy shared anchor must be promoted explicitly or handled by a new dependence-safe mechanism.

Exact enumeration in this run confirmed 84 nonsingular ordered two-seeds, 84 nonzero overlap packets, every packet anchored at h, and bordered determinant modulus a eps^2=1/20480.

## Lowest supported multiplicity and next obligation

The lowest complete threshold supported by the audited proofs is 9. A complete argument even gives a safe constant <375 K^2/s via the separate reconstruction, while the active source states 400 K^2/s.

Multiplicity 8 is not closed. The next unpaid implication is a product-law-safe heavy-shared-anchor receiver that jointly uses the s8-forced large W/V2 overlap energy, keeps each original shared coordinate present exactly once, and gains enough frequency/small-ball integrability to cross the critical rank-two logarithmic endpoint.

No unrestricted three-eigenvalue theorem is claimed.
