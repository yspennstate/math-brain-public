# fleet03 / B05 — five-singular-values line audit, pass 1, run 20260925T003708Z-fleet03-B05-five-sv-audit-r11

## Source and control

- Objective: `QFORM-FIVE-SINGULAR-VALUES-LINE-AUDIT-20260925`.
- Fresh control head at invocation: `yspennstate/math-research-brain@6057334145e5f75c6fe6328524a567f56ad64b46`; OWNER CONTROL revision `2026-09-25.1`.
- Exact immutable source: `yspennstate/math-open-problems@ec211ba2d77a4a9850168c6af1574ea651feaa7c`.
- LaTeX: `proofnet24/QFORM-density/five-eigenvalues-paper-2026-09-25/short/short.tex`, blob `c4f2a997cf336ee974e15409b5bccdd8cca039d8`, 676 physical source lines including trailing blank.
- PDF: `short/short.pdf`, blob `8be3aae36ecad7a9dc9b7c95978aad09499f32d0`, 484310 bytes, SHA-256 `4c1a8eb808b32739625aa475c1aad24dc857a3f35fc960504b371487f2850423`, 14 pages.
- Execution context: `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected:false`.
- Actual objective acknowledgement was created before this substantive audit at commit `29284548f4ffba01a5cab80098a258734e3175b6`.
- The canonical login write was attempted but blocked by the connector safety layer before execution; the path remained absent on readback. No bypass was attempted.

## This run's exact coverage

Initial assigned lens: Lemmas 3.2–3.3, product-projection densities, fibers/exceptional slices, Fourier powers and constants. I audited their complete local dependency Theorem 3.1 as well.

Reviewed source range: **lines 177–241 inclusive**.
- Theorem 3.1 (geometric Brascamp–Lieb): lines 177–206, rendered PDF page 4.
- Lemma 3.2 (product projections): lines 208–229, rendered PDF page 5.
- Lemma 3.3 (Fourier powers and difference densities): lines 231–241, rendered PDF page 5.

The PDF page references were independently recovered from the exact PDF's named destinations: `theorem.3.1 -> page object 144` (the fourth of the fourteen `/Type /Page` objects), while `theorem.3.2` and `theorem.3.3` both target page object 155 (the fifth page). The exact PDF bytes/blob and 14-page object structure were checked. A browser screenshot of this private pinned PDF was not available, so glyph-by-glyph visual render equivalence remains **UNCHECKED**; mathematical clause auditing below is against the exact pinned `short.tex`.

Coverage records: 40; status counts: {"PASS":28,"NOT_MATHEMATICAL":12}. Every physical source line 177–241 appears in at least one coverage record.

## Verdict on Theorem 3.1

**PASS for the audited mathematical clauses.** I reconstructed the heat-flow proof rather than importing the earlier favorable verdict.

The key identity is
[
\frac{\partial_\tau F-\Delta F}{F}
=\sum_i c_i v_i^2-\left|\sum_i c_i v_i u_i\right|^2.
]
Writing (W) with columns (\sqrt{c_i}u_i), the frame identity gives (WW^T=I_d), hence (\|W\|=1), so the right-hand side is nonnegative. The compact-support approximation has enough Gaussian decay to justify differentiation under the integral and (\int\Delta F=0). At large time, the rescaling (x=\sqrt\tau z), together with (\sum c_i=d) and (\sum c_i(u_i\cdot z)^2=|z|^2), gives the exact product (\prod_i\int h_i). At small time, Lebesgue differentiation plus Fatou and monotonicity gives the desired inequality. Monotone truncation handles arbitrary nonnegative integrable (h_i).

No hidden smoothness assumption on the final inputs is retained.

## Verdict on Lemma 3.2

**PASS.** The proof preserves product structure correctly.

For (d<n), complete (U) to the orthogonal matrix ((U,W)). The density of (U^TX) is the deterministic fiber integral
[
p(y)=\int_{\mathbb R^{n-d}}\prod_i f_i((Uy)_i+w_i\cdot z),dz.
]
This is marginalization of the original product density; it does **not** assert that rotated coordinates are independent.

With (\beta_i=|w_i|^2), each (0\le\beta_i\le1),
[
\sum_i\beta_i=n-d,qquad
\sum_{\beta_i>0}\beta_i v_iv_i^T=I_{n-d}.
]
After dropping only the (\beta_i=0) factors (permitted because (f_i\le1)), the Brascamp–Lieb substitution gives
[
p(y)\le\prod_i\beta_i^{-\beta_i/2}.
]
Then
[
\log p(y)
\le\frac12\sum_i\beta_i\log(1/\beta_i)
\le\frac12\sum_i(1-\beta_i)
=\frac d2.
]
The (\beta_i=0) convention is valid by continuity and the second inequality contributes (0\le1) for such indices. Thus (\|p_{U^TX}\|_\infty\le e^{d/2}).

The SVD step in part (b) has the correct Jacobian:
[
\det\Sigma=\sqrt{\det(BB^T)}.
]
Hence
[
\|p_{BX}\|_\infty\le e^{d/2}\det(BB^T)^{-1/2}.
]

## Verdict on Lemma 3.3

**PASS.** All Fourier powers and constants were recomputed.

For a cap-one density (f), (f\in L^2) since (f^2\le f). The difference (Y-Y') has density
[
g(x)=\int f(x+y)f(y),dy\le1.
]
For real (p\ge2), let (m=\lfloor p/2\rfloor). Then (m\ge p/4) and, because (|\widehat f|\le1),
[
|\widehat f|^p\le|\widehat f|^{2m}.
]
The latter is the characteristic function of
[
Z=\sum_{j=1}^m(Y_j-Y_j').
]
It is (L^1), because
[
\int|\widehat f|^{2m}
\le\int|\widehat f|^2
=2\pi\|f\|_2^2\le2\pi.
]
Fourier inversion therefore gives a continuous density with
[
p_Z(0)=\frac1{2\pi}\int|\widehat f|^{2m}.
]
Applying Lemma 3.2 to the (2m) original independent copies with coefficient vector of norm (\sqrt{2m}) gives (p_Z\le\sqrt e/\sqrt{2m}) a.e.; continuity upgrades this ceiling to every point, including zero. Thus
[
\int|\widehat f(t)|^pdt
\le\frac{2\pi\sqrt e}{\sqrt{2m}}
\le\frac{2\pi\sqrt{2e}}{\sqrt p}.
]
No moment, support, continuity or connected-support hypothesis entered.

The source notation (\mathbf1\cdot(Y_1,\ldots,-Y_m')) is harmless: equivalently use coefficients (+1) and (-1) on (Y_j,Y_j'); reflection preserves both independence and the density cap.

## Correction-note comparison

None of C01–C07 supplies a repair to Theorem 3.1 or Lemmas 3.2–3.3. I did not use the prior review's PASS as a premise. The current clauses pass independently.

The most relevant scope caution is respected: projection bounds control a projected **joint density** but do not create independence in a rotated basis. Every independence use above is on original coordinates or independent copies.

## Open issues and downstream impact

No GAP or FALSE mathematical clause was found in lines 177–241. Consequently the following downstream inputs survive this run's audit:
1. projected-density ceiling (e^{d/2}\det(BB^T)^{-1/2});
2. scalar ceiling (\sqrt e/|a|);
3. cap-one density for coordinate differences;
4. Fourier power bound (2\pi\sqrt{2e}/\sqrt p).

This does **not** certify any downstream theorem that has not yet been audited in this pass.

## Coverage cursor / incompleteness

This is **not a complete manuscript pass**. Complete passes finished by fleet03/B05 on this source: **0**.

Checked in pass 1: lines **177–241**.

Still UNCHECKED in this worker's pass 1:
- lines **1–176**;
- lines **242–676**.

The numerically first unchecked source line is **1**. For efficient continuation from the assigned starting lens, the next forward cursor is **line 242**; after reaching the end I will wrap to lines 1–176 before calling pass 1 complete.

Render/source glyph equivalence on PDF pages 4–5 remains UNCHECKED beyond exact-blob verification, page-object count, and named-destination/page mapping because the private PDF could not be opened in the screenshot browser.

No other research, threshold reduction or constant optimization was performed.
