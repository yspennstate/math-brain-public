# fleet03/B04 — pass 4 measurability / boundary / exact-render audit

Run ID: `20260925T044229Z-fleet03-B04-fiveaudit-r14`
Objective: `QFORM-FIVE-SINGULAR-VALUES-LINE-AUDIT-20260925`
Pass ID: `pass4_measurability_boundary_adversarial`

Pinned source: `yspennstate/math-open-problems@ec211ba2d77a4a9850168c6af1574ea651feaa7c`
TeX blob: `c4f2a997cf336ee974e15409b5bccdd8cca039d8`
PDF SHA-256: `4c1a8eb808b32739625aa475c1aad24dc857a3f35fc960504b371487f2850423`, 484310 bytes, 14 pages.

## Verdict

Fourth complete fleet03/B04 reconstruction. Repaired mathematical theorem: **PASS**. No new fatal/major theorem defect.

Literal source is **not** defect-free:
- C01 FALSE wording: half-open polar chart is not a global diffeomorphism; null-ray chart repairs it.
- C03 GAP: hyperbolic proof omits critical-level no-atom sentence; level is two affine lines, hence null.
- B04-P3-N01 GAP: Lemma 5.1 displayed density formula is undefined at z=v unless a density version is chosen; set p_T(v)=0 since P(T=v)=0.
- C04/C05 are narrative defects.
- C02 mathematical step is PASS: “and averaging over X_{I'}” invokes |E F|^2 <= E|F|^2; explicit display is editorial clarification.
- C06 wording only; C07 literature-open-status remains UNCHECKED.

## Heat flow, lines 177–205, pp.4–5 — PASS

With f_i=g_tau*h_i and F=prod f_i(tau,u_i·x)^c_i,
(∂_tau F-Delta F)/F = sum c_i v_i^2 - |sum c_i v_i u_i|^2 >=0.
The frame matrix with columns sqrt(c_i)u_i is a contraction since WW^T=I.

On compact tau intervals, ∂_y log f_i is the tilted average of -(y-Z)/(2tau), and
∂_y^2 log f_i = -1/(2tau)+Var(Z)/(4tau^2).
Compact support plus the frame identity gives a common integrable polynomial-Gaussian envelope for F, ∂_tau F, grad F, and Hessian F. Thus differentiation under the integral and ∫Delta F=0 are justified.

At tau→∞, x=sqrt(tau)z gives the exact Gaussian limit and a common Ce^{-|z|^2/16} majorant. At tau↓0, approximate-identity convergence holds at Lebesgue points; pullbacks of one-dimensional null sets under nonzero x↦u_i·x are null by orthogonal coordinates/Fubini. Fatou plus monotonicity closes the bounded compact-support case; monotone truncation closes arbitrary nonnegative integrable inputs.

## Projection/Fourier powers, lines 206–241, p.5 — PASS

The orthogonal completion is only a deterministic density-coordinate change; no post-rotation independence is asserted. If beta_i=|w_i|^2=0, then w_i=0 and the actual factor f_i((Uy)_i)<=1 is independent of z, so every such factor may be dropped. This confirms the source line-222 reading.

For positive beta_i, geometric BL and beta log(1/beta)<=1-beta give p_{U^T X}<=e^{d/2}. SVD yields the full-rank linear-map bound. Lemma 3.3 then gives the stated Fourier-power constant via differences, inversion at zero, and the one-dimensional projection bound.

## Preliminaries, lines 83–173, pp.2–4 — PASS

Fourier normalizations, Gaussian identity, Gamma half-potential calculation, conditioning/Radon–Nikodym domination, approximation-number singular-value inequalities, Schur threshold equality including the singular-A epsilon limit, and Gram/Cauchy–Binet identities all check.

## Crossing-volume compiler, lines 245–390, pp.5–8 — PASS

Entropy/Jensen and the squarefree m! count are correct. In Lemma 4.3, hub residualization, difference-coordinate independence, two-copy decoupling, complex-measure domination, scaled Plancherel, mollified L2 convergence, measurability/DCT, zero-weight Holder, determinant factorization, Fourier-power exponents, entropy products and greedy row promotion all check.

For C02, the source phrase “and averaging over X_{I'}” supplies the standard Jensen step |E F|^2<=E|F|^2. The explicit correction display is useful but the mathematical implication is valid.

## Pivot section, lines 395–510, pp.9–11

Lemma 5.1: substantive square change-of-variables and interval bound PASS. Literal displayed density needs a version at z=v; define p_T(v)=0.

Lemma 5.2: statement/repaired proof PASS; literal global-diffeomorphism sentence FALSE. The null-ray chart has the same Jacobian 1/(2sqrt(det B)) and constant pi L/sqrt(det B).

Lemma 5.3: all branch Jacobians, physical-coordinate positive/negative tails, cutoffs and logarithmic envelope PASS; literal proof has C03 GAP at q=v. Adding that the critical level is two affine lines closes absolute continuity.

Lemma 5.4: diagonal/off-diagonal alternatives, random partition, Fourier smoothing, atom exclusion and log layer cake PASS. A rigorous enclosure gives Gamma(1/4)<3.752, 2^{5/4}<2.38 and e^{3/4}<2.12, hence the Gaussian coefficient <18.93<19.

Lemmas 5.5–5.6: kernel antiderivatives/rearrangement and half-moment calculations PASS after carrying the local Lemma 5.2/5.3 repairs.

## Random signs, lines 512–580, pp.11–13 — PASS

No-pivot entry bounds, doubled crossing singular values, the two surviving ordered Rademacher fourth-moment pairings, compression/Weyl indexing, gamma_m constants and E_m lower bound all check.

## Section 7 / main theorem, lines 582–647, pp.13–14

Proposition 7.1 PASS. Literal Proposition 7.2 and literal end-to-end Theorem 1.1 are classified GAP only because they depend on literal C01/C03 defects. After the independently reproduced local repairs:
- no pivot <167;
- pair half-potential <=64;
- three-eigenvalue half-potential <77;
- diagonal main branch sqrt(12)*77<267;
- definite pair 16pi<51;
- indefinite pair <269;
- final K,s scaling is exactly K^2/s.

The global conclusion is an essentially bounded density. Continuity is proved on the integrable-Fourier branch, not globally.

## Exact render audit

The exact uploaded PDF was materialized and SHA-256 remeasured. It was rendered at 160 dpi and all 14 pages were individually inspected. No visible TeX/PDF mismatch or missing formula was found.

## External clauses

BGKS Theorem 2.1 and LPP are substantively consistent with the related-work descriptions. The global claim that the exact three-large-eigenvalue problem is open remains UNCHECKED; a limited search cannot prove absence of all results. These clauses are not analytic dependencies.

## Pass-4 status

Lines: 1–676 accounted. PDF: 1–14 accounted. Complete B04 passes: 4.
First unchecked mathematical proof clause: none.
Literal-source defects: C01, C03, B04-P3-N01; narrative C04/C05.
Repaired theorem: PASS. New fatal/major defects: none.
A favorable pass is not a stop condition.
