# account01/B11 independent audit — nine-eigenvalue constant-400 source

Objective: QFORM-FIXED-MULTIPLICITY-AUDIT-20260924
Run: 20260924T161242Z-account01-B11-fixedmult-auto11
Pinned source commit: eeb752c8943536541b34b42b8bf48e924f4d3d2f
Pinned paper blob: 19fb119877426b640b2c0dae19ec2f78a399fe11
Pinned SHA-256: bf1caf6ae4b4bc33992f501c169b5dc6c795db757b0f6089eff9991391effdf3
Package-completion commit used for support files: af592913ccfc4a87dfbf7c3a49bf2c5d4bbae359

## Verdict

PASS for the written theorem: if the ninth singular value of the arbitrary real symmetric quadratic matrix is at least s>0, then for arbitrary independent real coordinate densities bounded by K and arbitrary affine b,c,
||p_Q||_infinity <= 400 K^2/s.

I read all 955 source lines and the complete textual audit/check package. I found no fatal mathematical gap and no hidden Gaussian, moment, support, log-concavity, iid, exact-rank, or rotated-independence assumption. This is one independent worker reconstruction of this exact revision; it is not formal verification, journal peer review, or by itself the two-review release gate. Eight and three eigenvalues remain unproved.

## Complete source audit

- Lines 1–46, setup/conventions/abstract: PASS. Scope agrees with the proof; pointwise-bounded Borel density representatives are chosen explicitly.
- Lines 47–86, theorem/scaling/parameters: PASS. Quantifiers are complete and d=3/40, p=1/400, h=2/25, kappa=4/625 are used consistently.
- Lines 87–117, Fourier/Plancherel/Gaussian inversion: PASS. Normalizations and approximate-identity passage are correct.
- Lines 118–127, power envelope: PASS. The envelope integral gives the stated density constant.
- Lines 128–164, negative half moments: PASS. Tonelli is applied to nonnegative majorants; the Fourier coefficient and weighted integral are correct.
- Lines 165–178, singular-value perturbation/rank shift: PASS, including nonsymmetric auxiliaries.
- Lines 179–203, principal Schur spectral count: PASS. Strict inverse thresholds, non-strict original thresholds and singular-A approximation are all handled correctly; detailed reconstruction below.
- Lines 204–215, strict diagonal dominance: PASS.
- Lines 216–252, geometric rank-one Brascamp–Lieb: PASS. Heat-flow sign, integration by parts, large-time limit and rough-input approximation check.
- Lines 253–278, product projection density: PASS. Only original independent coordinates are integrated; deterministic rotations do not assert new independence.
- Lines 279–297, scalar Fourier powers: PASS.
- Lines 298–320, decoupling: PASS. Independent copy and Jensen are in the correct order.
- Lines 321–370, regularized determinant: PASS. Frame weights, Jacobians, integrated Fourier powers and exponent -1/8 check.
- Lines 371–396, crossing volumes: PASS.
- Lines 397–477, grouped product-Fourier lemma: PASS. The phase-weighted image is L1∩L2; Jensen is first applied to mollified L2; weighted Holder is valid on the finite kernel measure; the Gram determinant is S^2 det(C_T C_T^T); entropy and delta-to-zero passages are valid.
- Lines 478–488, terminal literal-hub receiver: PASS.
- Lines 489–527, marginal-free crossing estimates: PASS. Heavy-row promotion retains literal coordinates and all couplings. C3=14.818337...<15 and C2=12.095073...<14. Only the q=3 branch claims continuity.
- Lines 528–548, scalar square profile: PASS as a conditional measure-domination statement, not an independence statement.
- Lines 549–562, definite pair: PASS.
- Lines 563–610, indefinite hyperbolic pair: PASS. Hyperbolic Jacobian, tail monotonicity, rearrangement and Lambda >=2/sqrt(D) all check.
- Lines 611–662, quarter-power concentration/log potential: PASS.
- Lines 663–678, pivots and disjoint volumes: PASS.
- Lines 679–699, volume-sampled interpolation: PASS. Singular deleted seeds are correctly allowed to have nonsingular extensions, so the count is an inequality.
- Lines 700–715, completion A=D+R+E: PASS. D vanishes on the seed, E has zero diagonal, global rank(R)<=3r and restricted rank(R_LL)<=r.
- Lines 716–742, no-pivot spectral-to-volume proposition: PASS. The ratio-drop/first-zero case is exhaustive; for r=1,2 the diagonal-dominance margins are exactly 1131/2200 and 51/2200.
- Lines 743–753, random coordinate cut: PASS.
- Lines 754–766, no-pivot analytic consequences: PASS.
- Lines 767–789, scalar convolution kernel: PASS.
- Lines 790–811, full pair half-potential: PASS. Correct scaling is D^(-1/4); at delta=1/64 the bound is 12+5 log 2<16.
- Lines 812–828, five-eigenvalue half-potential: PASS.
- Lines 829–860, proof of main theorem: PASS. Branch caps are <375,<280,<320,<383,<80,<392.5; scaling yields exactly 400 K^2/s. Absolute continuity is proved in all branches; global continuity is not claimed.
- Lines 861–907, overlap spectral-tail theorem: PASS. Frobenius orthogonality and best rank-3r approximation are valid for the nonsymmetric completion.
- Lines 908–921, eight-eigenvalue overlap corollary: PASS.
- Lines 922–955, threshold accounting/limitations: PASS mathematically. Bibliographic priority is UNCHECKED because no exhaustive novelty search was performed and the references are not proof dependencies.

## Detailed B11 lens: Schur count

Write A in block form with invertible k-by-k principal block B and Schur complement S=D-C^T B^{-1} C. If A is invertible, the complementary principal block of A^{-1} is S^{-1}. Principal-compression eigenvalue interlacing applied separately to A^{-1} and -A^{-1} gives
#{|lambda(S^{-1})|>1/t} <= #{|lambda(A^{-1})|>1/t}.
The strict inverse threshold is exactly complementary to |lambda(A)|>=t, so the right side is n-N_A(t), while the left side is (n-k)-N_S(t). Hence N_S(t)>=N_A(t)-k.

For singular A, fix delta in (0,t), choose epsilon_m->0 avoiding the finitely many forbidden shifts so A+epsilon_m I is invertible, and keep B+epsilon_m I invertible. For |epsilon_m|<delta/2,
N_{A+epsilon_m I}(t-delta)>=N_A(t).
The associated Schur complements converge to S. Continuity of ordered eigenvalue moduli gives the count at t-delta, and in finite dimension N_S(t-delta) decreases to N_S(t) as delta decreases to zero. Equality at the threshold is therefore preserved correctly.

## Audit package

README.md: PASS.
NINE_400_AND_OVERLAP.md: PASS as a derivation/limitations document.
AUDIT_NEW.md: PASS only as self-audit metadata, not independent validation.
MANIFEST.json: PASS.
proof_map.csv: PASS against the 955-line source.
verify_new.py: PASS as a code audit of its finite checks.
checks_new.json: PASS as the supplied execution record, not universal proof.
Independent re-execution of verify_new.py: UNCHECKED in this connector-only run.
Independent PDF compilation/visual inspection: UNCHECKED in this run.

## Review gate

This is one independent end-to-end reconstruction of the exact nine-eigenvalue/400 source. I did not identify a second genuinely separate end-to-end review of this exact post-14:54 revision in the B16/B19 audit folders inspected in this run; the account02/B19 15:09 report that I read audits the historical 17-eigenvalue baseline. Therefore I do not mark the nine-400 candidate independently validated.

The threshold-eight frontier is treated in the companion improvement artifact.