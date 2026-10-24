# account04/B19 — corrected global proof graph with finite-hub and bank-grid endpoints

Run: \`20260924T121506Z-account04-B19-QFORM-r6\`

Status: **ESSENTIAL_STEP_APPLIED / NONCIRCULAR PROOF GRAPH / FULL QFORM OPEN**

Let \(X_1,\ldots,X_n\) be independent real variables with probability densities bounded by one, and let \(A=A^T\) have at least three eigenvalues of modulus at least one. The desired dimension-free bound for \(X^TAX\) remains open. Continuity remains a separate question.

No step below rotates the product law, deletes nonzero coefficient tails, assumes moments or support regularity, or replaces a scoped one-sided estimate by a full solution.

## 1. Source pins

The Claude inputs are the files
\[
\texttt{RESULTS.md},\quad
\texttt{FOURIER_ROUTE_REPORT.md},\quad
\texttt{COUNTEREXAMPLE_SEARCH.md}
\]
in
\`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/\`,
rooted at required commit
\`e5f71d79eff325201dd0274053d20268ce65b837\`,
with the later Claude-review corrections retained.

The completed account01/B19 theorem applied below is
\`yspennstate/math-open-problems@de21053f13cdf4e81634fa3bde3a6246b90a9a6d\`.
The new physical bank-grid reduction used below is
\`yspennstate/math-open-problems@386b201c7236ed77017e14c1d3afb17587edbf1c\`.

## 2. Actual application of account01/B19 r57

The corrected retained-tail branch has an exact original-coordinate decomposition
\[
A_{\rm light}=D+K_r+F,
\]
where \(D\) is physical diagonal, \(\operatorname{rank}K_r\le r\), and either
\[
r\le12,\qquad \|F\|_{\rm op}<\delta_{12}
=\frac{12289}{65536},
\]
or
\[
r\le11,\qquad \|F\|_{\rm op}<\delta_{11}
=\frac{1537}{8192}.
\]

Account01/B19 r57 proves that if at least \(r+3\) physical coordinates satisfy \(|D_{ii}|\ge a>\delta\), then conditioning outside those \(r+3\) original coordinates gives
\[
\boxed{
\|p_Q\|_\infty
\le
\frac{250(r+3)\,[8+\log(r+3)]}{a-\delta}.}
\tag{1}
\]

Apply (1) at \(a=1/2\). In the rank-12 branch,
\[
a-\delta_{12}=\frac{20479}{65536},
\]
so fifteen such diagonal coordinates imply
\[
\boxed{\|p_Q\|_\infty<128503.}
\tag{2}
\]
In the rank-11 branch,
\[
a-\delta_{11}=\frac{2559}{8192},
\]
so fourteen such coordinates imply
\[
\boxed{\|p_Q\|_\infty<119205.}
\tag{3}
\]

Therefore every unpaid retained-tail state has a finite physical hub
\[
H=\{i:|D_{ii}|\ge1/2\}
\]
with
\[
\boxed{|H|\le14\quad(r\le12),\qquad |H|\le13\quad(r\le11).}
\tag{4}
\]

This removes unbounded diagonal complexity from the first unproved implication. It does not remove \(F\).

The same source then gives the exact finite-hub router. If the hub-light coupling \(C=A[H,H^c]\) satisfies \(\|C\|_{\rm op}\ge1/4\), some literal hub star obeys
\[
\boxed{\|A[i,H^c]\|_2\ge\frac1{4\sqrt{14}}
=0.066815310478\ldots .}
\tag{5}
\]
If \(\|C\|_{\rm op}<1/4\), the light block retains \(3-m_H\) finite-latent directions at scale at least
\[
\boxed{\frac14-\delta_{12}=\frac{4095}{65536}}
\quad\text{or}\quad
\boxed{\frac14-\delta_{11}=\frac{511}{8192}},
\tag{6}
\]
where \(m_H\le2\) counts the hub singular values at least \(3/4\).

At the exact diffuse aligned endpoint
\[
A_{LL}=D_L+WH_0W^T,\qquad W^TW=I,\qquad \max_i\|W_i\|^2\le\frac12,
\]
the completed latent pseudodeterminant theorem gives
\[
\boxed{
\|p_Q\|_\infty
\le \frac{4k}{k-2}\,|\operatorname{pdet}H_0|^{-1/k}.}
\tag{7}
\]
In exact rank three, \(s_3(H_0)\ge1/4\), so
\[
\boxed{\|p_Q\|_\infty\le48.}
\tag{8}
\]
The unpaid aligned endpoint is therefore only the nonzero near-rank-drop collar, not exact rank drop.

## 3. Compact noncircular proof graph

The current graph is:

1. **Physical pivot exits.** Scalar pivots, definite pairs, eligible indefinite pairs, and fixed physical principal cores pay their precise branches. Schur complements are used only with the proved spectral-retention hypotheses.
2. **Fourier-volume exits.** Claude's \(D'\) theorem pays a physical cross block when its volume-sampling row marginals satisfy the corrected gate; \(D_5\) pays fixed fifth cross-volume without a marginal gate. Endpoint entropy factors are retained.
3. **Fresnel/ridge exits.** Low-leverage diagonal-plus-finite-rank blocks are paid by the sharp Hausdorff-Young/Fresnel theorem. Mixed-hub theorems apply only to their exact source block forms.
4. **Ruled-side exit.** Claude's physical ruling identity pays the one-sheet side of an indefinite rank-three range-contained affine form. It does not pay the convex/two-sheet side or affine components outside the range.
5. **Diffuse carrier exit.** The account01/B08 bilateral carrier theorem either produces an inductive five-eigenvalue escape, a genuine third-compound payment, or a rank-two carrier with three physical banks on each side.
6. **New bank-grid localization.** On that last carrier, the literal crossing \(D\) has
   \[
   s_2(D)\ge \sigma L,\qquad
   \sigma=\frac12\sqrt{\frac{67}{800}},
   \]
   and there are two disjoint row-column bank cells satisfying
   \[
   \boxed{
   \|D[H_{i_r},K_{j_r}]\|_F
   \ge\frac{\sigma}{16}L
   =0.0090436225803\ldots\,L,\quad r=1,2.}
   \tag{9}
   \]
   The same matrix has the exact order-two volume certificate
   \[
   \boxed{e_2(D^TD)^{1/4}\ge\sigma L.}
   \tag{10}
   \]
7. **Retained-tail exit.** Robust purification reaches \(D+K_r+F\) with \(F\ne0\) retained. Equations (1)--(8) pay large diagonal cores and the exact diffuse aligned endpoint, leaving only a finite hub plus a transverse or nonzero near-rank-drop light tail.

There is no back-edge in this graph: the inductive five-eigenvalue branch reduces dimension; the finite-core branch conditions only outside a literal coordinate set; the Fourier and Fresnel branches pay the full ambient law; and the ruled theorem is not reused on its unproved convex side.

## 4. First remaining implications

The proof is not complete. The principal leaves are now:

- **Bank-grid plus curvature:** upgrade (9)--(10), together with retained same-bank curvature, to a fixed third compound or a physical finite-carrier receiver. Two large disjoint Frobenius cells alone do not prevent determinant cancellation.
- **Finite-hub transverse tail:** spend the star in (5), or a genuinely transverse part of \(F_{LL}\), without deleting \(F\).
- **Aligned nonzero near-rank-drop:** prove a bound uniform as the smallest nonzero latent singular value tends to zero, or route it to another physical receiver.
- **Shared-bank convex/two-sheet endpoint:** exploit the nonzero modulation. Claude's ruled estimate is one-sided and ordinary projection-density caps are dimensionally false.

These leaves are compatible and noncircular; none is silently declared solved.

## 5. Review status

There is no full candidate proof in this run, so two end-to-end review receipts are neither requested nor fabricated. If the four implications above are closed and assembled into a full candidate, two independent end-to-end reviews are mandatory before any completion claim.

Full universal density theorem: **OPEN**.  
Valid counterexample: **none**.  
Full continuity: **OPEN**.
