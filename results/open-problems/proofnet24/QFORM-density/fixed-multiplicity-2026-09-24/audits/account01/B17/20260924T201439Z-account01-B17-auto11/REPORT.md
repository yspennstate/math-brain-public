# account01/B17 r11 — fixed-multiplicity full audit and threshold accounting

Run: `20260924T201439Z-account01-B17-auto11`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Model: GPT-5.6 Sol; effort: UNKNOWN.  
Execution label: `WITHOUT_VERIFIED_BRAIN`.

## Source pins

Preserved 17-eigenvalue baseline:
- commit `7c0d6e60946b19423e6400a12d34b473cf0591e2`
- manuscript blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`
- SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`
- 790 lines.

Latest nine-eigenvalue source audited end-to-end:
- commit `eeb752c8943536541b34b42b8bf48e924f4d3d2f`
- paper blob `19fb119877426b640b2c0dae19ec2f78a399fe11`
- SHA-256 `bf1caf6ae4b4bc33992f501c169b5dc6c795db757b0f6089eff9991391effdf3`
- 955 lines.

Baseline support files on current master were read in full:
`README.md` blob `dba7741744e78be742a5850dad4c2648cbee9360`;
`AUDIT.md` `d1660140ad428e8113ba5590be4d307d0eef75cf`;
`proof_map.csv` `bd52d705490437a1998d78d4d944d13d2186ff97`;
`SOURCE_MANIFEST.json` `72e16a87ecc6d8b865a1861d929c32609f79a545`;
`verify.py` `5755b77201a734080051a8ed7fee705850310466`;
`checks.json` `cd6a55e928d1a91d63fb17f5f6184a4cf0c5a937`.
The support files postdate the baseline commit, exactly as the current README records.

## Verdict

- Preserved 17-eigenvalue candidate: **PASS** in this B17 mathematical recheck; no fatal defect found.
- Latest nine-eigenvalue/constant-400 candidate: **PASS** in this B17 end-to-end mathematical audit; no fatal defect found.
- External priority/bibliographic completeness: **UNCHECKED**; it is not a proof dependency.
- Numerical/Lean/checker artifacts: supporting evidence only, not substituted for analytic proof.
- This audit does not solve the unrestricted three-eigenvalue conjecture and does not by itself assert journal-level/formal verification.

## Exhaustive latest-source line audit

The following disjoint ranges cover every line of the 955-line latest source. “PASS” means every definition, equation, quantifier and proof step in that range was checked against its dependencies.

| Lines | Verdict | Check |
|---|---|---|
| 1–46 | PASS | Preamble, abstract, scope and metadata internally consistent. |
| 47–65 | PASS | Main theorem/corollary and full-scope quantifiers; scaling target is dimensionally correct. |
| 66–86 | PASS | Parameters, pivot definitions in prose, threshold architecture and continuity separation. |
| 87–117 | PASS | Plancherel, inversion and Gaussian identity; approximate-identity and weak-limit arguments are valid. |
| 118–127 | PASS | Power-envelope integration constant. |
| 128–164 | PASS | Negative-half-moment Fourier representation; Gamma substitution and constants. |
| 165–178 | PASS | Singular-value perturbation/rank inequality for nonsymmetric auxiliaries. |
| 179–203 | PASS | Schur spectral count including singular approximation. |
| 204–215 | PASS | Strict diagonal dominance and transition. |
| 216–252 | PASS | Geometric rank-one Brascamp–Lieb heat-flow proof and limiting steps. |
| 253–278 | PASS | Product projection density bound; zero-leverage convention included. |
| 279–297 | PASS | Integrated scalar Fourier powers and difference-density cap. |
| 298–304 | PASS | Cross-block setup; affine/internal terms retained. |
| 305–320 | PASS | Two/four-power decoupling; no moment use. |
| 321–370 | PASS | Regularized crossing determinant; graph weights, BL scaling and determinant exponent all re-derived. |
| 371–380 | PASS | Cauchy–Binet crossing-volume expansion. |
| 381–396 | PASS | Volume envelopes and k=5/k=3 analytic consequences. |
| 397–399 | PASS | Grouped-section setup. |
| 400–477 | PASS | Grouped product-Fourier lemma: complex pushforward L2 control, mollification, weighted Hölder, entropy and limit. |
| 478–488 | PASS | Terminal literal-hub block and conditioning. |
| 489–527 | PASS | Heavy-row promotion and marginal-free E3 density / E2 half-potential constants. |
| 528–548 | PASS | Scalar square profile and conditional domination. |
| 549–562 | PASS | Definite two-coordinate Jacobian without rotated independence. |
| 563–610 | PASS | Indefinite hyperbolic pair: branches, Jacobian, tail integration and logarithmic envelope. |
| 611–662 | PASS | Quarter-power concentration and logarithmic potential. |
| 663–678 | PASS | Pivot/minor definitions and no-pivot entry bound. |
| 679–699 | PASS | Volume-sampled interpolation; singular seeds correctly give an inequality, not equality. |
| 700–715 | PASS | Diagonal/interpolation completion; global rank 3r and complement rank r. |
| 716–742 | PASS | Spectral-to-volume proposition; threshold count and r=1,2 diagonal-dominance margins. |
| 743–753 | PASS | Random physical-coordinate cut factor 4^{-k}. |
| 754–769 | PASS | No-pivot E2/E3 consequences and constants. |
| 770–789 | PASS | Singular convolution kernel. |
| 790–811 | PASS | Full two-coordinate half potential, including D^{-1/4} scaling. |
| 812–833 | PASS | Five-eigenvalue full half-potential proposition; all three pivot alternatives exhaustive. |
| 834–860 | PASS | Main theorem case split, constants, Tonelli/absolute-continuity handling and K,s scaling. |
| 861–874 | PASS | Overlap-one volume definitions and spectral-tail setup. |
| 875–907 | PASS | Spectral-tail/overlap theorem; Frobenius orthogonality, rank approximation and seed averaging. |
| 908–924 | PASS | Eight-eigenvalue overlap corollary and exact constant. |
| 925–944 | PASS | Threshold accounting/limitations accurately describe what the paper itself proves. |
| 945–955 | UNCHECKED | Acknowledgment and bibliographic/priority metadata only; not used as a mathematical premise. |

No range received GAP or FALSE.

## Sensitive dependencies independently re-derived

1. In the grouped lemma the phase-weighted pushforward is L2 because its total variation is dominated by a convolution containing the full-rank product projection through M_J. The delta-mollifier limit is therefore an L2 approximate-identity limit, not a weak-compactness shortcut.
2. Weighted Hölder is applied to a finite nonnegative measure; it does not require that measure to have mass one. The scalar exponents are >=2 exactly because all residual row marginals are <=1/2.
3. Heavy-row promotion uses literal original coordinates. It never rotates the product law.
4. The interpolation correction can be nonsymmetric; only singular values/ranks are used. The forced large diagonal entries lie in the seed complement, where the sharper rank-r bound applies.
5. Pair and scalar pivots are conditional domination statements. No completed square is claimed independent of its remainder.
6. The overlap theorem is genuine shared-coordinate information and is not silently promoted to a disjoint E3 packet.

## Cross-check against the separately written nine-eigenvalue reconstruction

The separately written source at
`proofnet24/QFORM-density/nine-eigenvalues-paper-2026-09-24/`
was also read. Its README blob is
`e4e6c88ee6635940e5c96ae9c434182cf9aaf12c`, its audit blob is
`af65f076e2c6c63a493c4f87f1d070b5f974a98a`, and its manifest blob is
`c88b39fbbcebbbfaa299a1c2e1fdbfd9a77b4d73`.
It reaches the same multiplicity nine by a separately written grouped-Fourier argument, with all normalized branches below 375. I found no contradiction between the two reconstructions. Its Lean checks formalize finite algebra/constants, not the full analytic Fourier/BL theorem, exactly as its audit states.

## Threshold update

A separate improvement in this run gives a complete multiplicity-eight candidate with the same constant 400. See the sibling file
`EIGHT_EIGENVALUE_400.md`.
The unrestricted multiplicity-three conjecture remains open.
