# account01/B03 reverse-order audit

Run ID: `20260925T014938Z-account01-B03-five270-audit-r12`

Objective: `QFORM-FIVE-SINGULAR-VALUES-LINE-AUDIT-20260925`.

Source: `yspennstate/math-open-problems@ec211ba2d77a4a9850168c6af1574ea651feaa7c`, `short/short.tex` blob `c4f2a997cf336ee974e15409b5bccdd8cca039d8`; exact 14-page PDF SHA-256 `4c1a8eb808b32739625aa475c1aad24dc857a3f35fc960504b371487f2850423`.

Fresh controls were reread before publication. This invocation reconstructed the proof in reverse dependency order, beginning with Section 7 and Theorem 1.1 and working back through Sections 6, 5, 4, 3 and the preliminary lemmas.

## Verdict

No new fatal theorem defect was found. The exact source is not literally gap-free:

- line 222: **FALSE_LOCAL / theorem unaffected**. “Factors with beta_i=0 are at most one” is false. Example: in R^3 with d=2, U=(e1,e2), W=e3 gives two zero rows. Minimal repair: delete “are at most one”; every zero-beta factor is integration-variable independent and <=1.
- Lemma 4.3 lines 319-321: **GAP_LOCAL**. The passage described as “averaging over X_{I'}” needs the explicit Jensen inequality |E F|^2 <= E|F|^2. No constant changes.
- Lemma 5.2 line 412: **FALSE_LOCAL** chart wording. Remove the angular seam/null ray before calling the elliptic polar map a diffeomorphism. Jacobian and density bound are unchanged.
- Lemma 5.3: **GAP_LOCAL** at the critical level. Add that {q=v} is the union of two affine lines and hence has probability zero under the joint density. The positive and negative hyperbolic tails correctly use separate original coordinates.
- Abstract and outline contain the already identified no-pivot/singularity wording defects; they do not alter the theorem proof.
- current literature/open-status and bibliography claims remain **UNCHECKED**.

## B03 dependence audit

Lemma 2.4 is PASS: only the original random elements U,V are assumed independent, Tonelli gives measure domination, and no conditional density recap or rotated-coordinate independence is used.

Lemma 4.3 is PASS after the explicit Jensen line and line-222 repair. The copied object is the entire literal J-bank, D=X_J-X'_J. Its physical coordinates are independent and each difference density is bounded by one. No sum/difference independence is asserted. For retained hubs, the complex image measure has total variation dominated by the projected image law, hence an L2 density. Mollification occurs after that L2 fact, Young contraction supplies domination, and the mollified square expands with a genuine independent J-copy. Step 4 uses Lemma 3.2 only as a joint projected-density bound, never as independence of image coordinates.

The determinant and Fourier powers recheck as
[
\det(BB^T)=\Theta(H)\theta(T'),\qquad
\int |\psi_i(2t(z+\lambda_i\cdot y))|^{1/\alpha_i}dz
\le \pi\sqrt{2e\alpha_i}/|t|.
]
The entropy step therefore yields |phi_Q(t)|^2 proportional to |t|^{-ell}; ell=3 gives the integrable |t|^{-3/2} envelope after taking the square root.

## Reverse theorem reconstruction

Proposition 7.1 correctly converts the no-pivot random-sign result into E3/E2 crossing volume lower bounds. Proposition 7.2 correctly loses one spectral direction at a diagonal Schur complement and uses the log-moment concentration estimate. In Theorem 1.1, a diagonal pivot from s5 leaves at least four large Schur eigenvalues, while a pair pivot leaves at least three. The final scaling Y=KX is exact and gives K^2/s.

Independent numerical diagnostics agree with the analytic chain:
C3=14.818337662843, C2=12.095072570796486, gamma2=0.23736246421253723, gamma3=0.09004855146533981, C3/gamma3=164.55942290805933, C2/sqrt(gamma2)=24.82575456311178, sqrt(12)*77=266.7358243656071, and the final indefinite-pair expression is 266.95134633033405.

After deriving these points, I compared with the separate account02/B19 complete audit. Its report found no fatal defect, but its line-222 PASS conflicts with the explicit zero-row counterexample above; that disagreement is preserved.

## Remaining unchecked

Direct rendered-PDF versus TeX formula equivalence is **UNCHECKED** because the authorized private source interface exposed the pinned binary identity but not a renderable PDF to the inspection tool in this invocation. External literature/priority claims are also **UNCHECKED**.

Strict owner-format complete pass count for this invocation: 0, because those PDF/external obligations remain open.

`full_brain_connected:false`; repository transport is not claimed as native learned-memory ingestion.
