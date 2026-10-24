VERDICT: PASS

Independent audit of D0019, 12 October 2026.

## Claim audited

ATTEMPT.md:5–9 and CLAIMS.jsonl:1–2 claim that for a continuous two-parameter Brownian sheet B with independent R^d-valued coordinates, d in {2,3}, and Z = {(s,t) in (0,infinity)^2 : B(s,t)=0}, there is one event of probability one on which every orthogonal line projection of Z has Hausdorff dimension 2-d/2. Thus even a direction selected using the entire sheet cannot be exceptional. The claimed resolution is a literature result, not an original proof of the probabilistic theorem.

This is the intended Open Problem 4 in Khoshnevisan's source. The answer is no, almost surely. The image dimensions are 1 and 1/2 for d=2 and d=3 respectively.

## Independently fetched evidence

All network access used Python urllib; no built-in web search was used. Downloaded copies and extracted text are in this audit folder, rather than copied from the claimant's evidence.

1. https://arxiv.org/pdf/math/0510518 returned HTTP 200, 468241 bytes, saved as source.pdf and source.txt. PDF page 34, Section 8.3, contains exactly the random orthogonal projection question in the assignment. Page 2 gives covariance min(s,u)min(t,v) delta_ij. Page 3, equation (1.7) and the paragraph following it, singles out d=2,3 for equality between the axis-image dimension and the zero-set dimension. Remarks 1.3 distinguish d=1 and d>=4.
2. https://arxiv.org/pdf/2405.20019v2 returned HTTP 200, 324474 bytes, saved as resolution.pdf and resolution.txt. This is Keming Chen and Guillaume Woessner, Zeros of the Brownian Sheet, arXiv v2 dated 31 May 2024. PDF page 2 states:

   “Theorem 1.2 (Open problem). For N = 2 and d = 2 or 3, almost surely, for any non-zero linear map p : R^2 -> R, dim_H[p(Z)] = dim_H(Z).”

   The preceding sentence explicitly says this answers Open Problem 4. The following paragraph explicitly says that “almost surely” is before the quantification of the linear maps and that the conclusion holds for all maps simultaneously. This removes the central possible quantifier failure. Reference [8], PDF page 22, is the specified Khoshnevisan work.
3. Proposition 1.1 on resolution.pdf page 2 supplies dim_H Z = (N-d/2)^+ almost surely. Definitions on page 1 give the matching independent-coordinate Brownian sheet. Section 2, pages 4–7, is a proof of Theorem 1.2; page 7 expressly addresses simultaneous directions in Step 3. I inspected these pages to establish that the result has a proof section, rather than being an abstract-only announcement.
4. https://api.crossref.org/works/10.1007/s10959-024-01399-1 returned HTTP 200, 9789 bytes, saved as crossref.json. It independently confirms the authors and title, Journal of Theoretical Probability 38 (2025), article 33, publication 6 February 2025. The theorem text checked here is the arXiv version; I did not inspect a journal PDF.
5. A fresh bounded arXiv API search for “Brownian sheet” AND (projection OR Marstrand) returned two records, saved in arxiv_search.xml. One is the exact Chen–Woessner resolver; its abstract explicitly identifies Khoshnevisan's Open Problem 4. The other concerns RKHS projections of additive Wiener fields and does not answer this zero-set question. The result does not depend on treating that unrelated hit as evidence.

## Checks against ATTEMPT.md and possible failure points

- Lines 5 and 9 (dimension and domain): the source's standalone question suppresses these conventions. Its own page 3 supports d=2,3. Positive parameters are essential: retaining the deterministic zero axes would force dimension at least one for some images when d=3. The original source uses nonnegative parameters to define B, but its nontrivial zeros and dimension comparisons concern positive parameters; see (1.3), (1.4), and (1.8). The later paper's notation R_+ is not defined unambiguously on page 1, but its Proposition 1.1 and localization to [a,b]^2 with 0<a<b on page 4 make the interior convention explicit in substance. The claimant correctly states this convention instead of asserting the theorem for the zero axes. No fix is required.
- Line 13 (literature theorem): independently verified the exact N=2, d=2,3 hypotheses and the simultaneous all-maps conclusion on page 2. This is neither a theorem for a different random set nor a fixed-direction result passed off as uniform. Proposition 1.1 gives exactly the required numerical dimension for these parameters.
- Lines 15–17 (scalar versus orthogonal image): re-derived the identification. For a unit vector u spanning L, p_u(x)=<x,u> is nonzero and P_L(x)=u<x,u>. The map J_u(r)=ru satisfies ||J_u(r)-J_u(s)||=|r-s|, so it is an isometry and preserves Hausdorff dimension. This supplies the asserted equality without an extra probabilistic hypothesis. Evaluating 2-d/2 gives 1 and 1/2, both within the dimension bound for a line.
- Line 19 (random projection): on the common probability-one event, the assertion holds pointwise for every L. Substituting L=L(omega) is therefore valid, including directions depending on B and directions chosen with auxiliary randomness. No intersection of uncountably many separately almost-sure events is being taken. The affine-line observation is also valid, since the affine projection differs by a translation along the perpendicular offset.
- Lines 23–28 (referee checks): the cited pages and bibliographic details match the independently fetched sources. In particular, page 7 really is the simultaneous-direction step. The restriction to positive parameters is substantive, not merely stylistic.
- Lines 31 and 35 (scope of verification): no original proof, numerical validation of Brownian-sheet estimates, or formalization is claimed. This audit independently verifies the literature theorem and completely checks its application. It does not certify every estimate in Chen–Woessner's probabilistic proof. For a SOLVED_IN_LITERATURE verdict the assignment asks for a source-matching paper/theorem check; that requirement is met by the full-text theorem, explicit quantifier explanation, and proof section.

## Issues and limits

No defect or required correction was found in the claimant's application. PASS applies to the intended positive-parameter, d=2,3 question. It does not assert that the literal target 2-d/2 is a line-image dimension in every spatial dimension, nor that including the zero axes yields the same theorem. In d=1 the target would be 3/2 and hence impossible for a subset of a line; the claimant already identifies this issue in ATTEMPT.md:9. These are explicit source conventions, not a remaining gap concealed in the claimed result.

What is established is the published literature resolution and the valid deduction excluding any random exceptional line projection almost surely. No new solution or independent proof of the cited probabilistic theorem is asserted.
