# fleet04/B18 r5 — bounded-window null-hub edge/cofactor dichotomy

Programme: \`QFORM-DENSITY-3EIG-20260922\`  
Run: \`20260923T221534Z-fleet04-B18-QFORM-r5\`  
Status: \`ESSENTIAL_STEP_APPLIED / LIVE SUBBRANCH PAID / FULL TARGET OPEN\`.

The unrestricted universal-density conjecture remains open. This report proves a source-matched bounded-window exit for the four-coordinate exact-rank-three null-hub geometry. It does not remove the small-edge endpoint, construct the required core from an arbitrary ambient matrix, or close the convex/two-sheet and additional-spectrum branches.

No random variable is rotated. No moment, support, smoothness, iid, conditional-density, arbitrary-joint coarea, or perturbative deletion assumption is used.

## 1. Pinned inputs

The new analytic input is fleet01/B18's theorem \`QFORM-4COORD-NULLHUB-COFACTOR-v1\`:

- scientific report commit \`1d16d620df6233e767d08bff397320d37875429e\`;
- completion/source-pin commit \`bc6e4e35f7e7057b1091d7bda24fcccb3e2627d9\`;
- path \`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B18/20260923T185527Z-fleet01-B18-qform-auto11-r36/REPORT.md\`.

For a symmetric original-coordinate \(4\times4\) principal block \(B\) of exact rank three, with \(B_{00}=0\), nonzero eigenvalues satisfying \(|\mu_j|\ge s\), and
\[
h=\|P_{\operatorname{range}(B)}e_0\|^2>0,
\]
it proves, uniformly in arbitrary affine terms,
\[
\|p_{X^\top BX+b^\top X+c}\|_\infty
\le 576^{1/3}s^{-1}h^{-1/3}. \tag{1.1}
\]
The ambient lift is by conditioning only original coordinates outside the block.

The proof's designated-partner input is fleet02/B18's physical planar-twist theorem at commit \`2d20f8bbcbffd1dfc98d85a976237eebe74e5510\`. Its exact gate is a physical leaf \(i\) with residual twist in the two-dimensional span and
\[
q_i<1.
\]
Fleet01/B18 verifies this gate from a nonzero physical principal cofactor and obtains
\[
\|p\|_\infty\le 192^{1/3}
 \left|\det B_{[4]\setminus\{i\}}\right|^{-1/3}. \tag{1.2}
\]
The adjugate identity then sums the three hub-retaining cofactors to at least \(s^3h\), yielding (1.1).

## 2. Primary-source scope

The marginal theorem used inside the source-valid hub receiver is Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949. Its input is a genuine product density \(\prod_i f_i\) with \(\|f_i\|_\infty\le1\), and it bounds every \(k\)-dimensional orthogonal marginal by \(2^{k/2}\). It does not require moments, iid laws, bounded support, log-concavity, centering, symmetry, or smoothness.

This scope is present after the proof conditions original coordinates. It would not justify declaring spectral coordinates independent.

Herry--Malicet--Poly, arXiv:2303.09488, assumes iid inputs with a sufficiently smooth Gaussian-field representation and additional normalization/spectral hypotheses in its quadratic-form regularity applications. It does not cover the present arbitrary non-iid cap-one laws, so no theorem from that paper is used as a universal substitute.

## 3. New theorem

### \`QFORM-4COORD-NULLHUB-WINDOW-EDGE-DICHOTOMY-v1\`

Let \(B\) be as in Section 1, and assume in addition that its nonzero eigenvalues lie in the spectral window
\[
s\le |\mu_j|\le L,\qquad j=1,2,3. \tag{3.1}
\]
Write
\[
B=\begin{pmatrix}0&g^\top\\ g&C\end{pmatrix},
\qquad g=(B_{01},B_{02},B_{03}).
\]
For every \(a>0\), exactly one of the following exhaustive alternatives supplies the required conclusion:

1. **non-tiny physical edge:** \(\max_i|g_i|\ge a\), and
   \[
   \boxed{\;
   \|p_{X^\top BX+b^\top X+c}\|_\infty
   \le 576^{1/3}\frac{L^{2/3}}{s\,a^{2/3}};
   \;} \tag{3.2}
   \]
2. **tiny-edge endpoint:** every original-coordinate hub edge satisfies
   \[
   |B_{0i}|<a,\qquad i=1,2,3. \tag{3.3}
   \]

The same dichotomy and bound hold for an arbitrary ambient symmetric form containing \(B\) as an original-coordinate principal block, with all outside spectrum and couplings retained.

### Proof

Let \(P=P_{\operatorname{range}(B)}\). Since \(B\) annihilates \(\ker B\),
\[
Be_0=BP e_0.
\]
The upper spectral gate in (3.1) gives
\[
\|g\|_2=\|Be_0\|_2
\le L\|Pe_0\|_2=L\sqrt h. \tag{3.4}
\]
If \(\max_i|g_i|\ge a\), then \(\|g\|_2\ge a\), so
\[
h\ge \frac{a^2}{L^2}. \tag{3.5}
\]
Insert (3.5) into the completed fleet01/B18 inequality (1.1):
\[
\|p\|_\infty
\le576^{1/3}s^{-1}
 \left(\frac{a^2}{L^2}\right)^{-1/3}
=576^{1/3}\frac{L^{2/3}}{s\,a^{2/3}}.
\]
This proves (3.2). If no edge reaches \(a\), (3.3) holds by definition.

For an ambient matrix, condition every original coordinate outside the four-set. The four retained inputs remain independent with cap one; all outside couplings become affine terms, for which (1.1) is uniform. Averaging completes the lift. QED.

## 4. Application to the live \(1/64\) edge gate

The previous fleet04/B18 result \`QFORM-NULLHUB-DIAGONAL-GATED-PAIRLOG-v1\`, commit \`3460488b1a730f54dbac848cddc3e2761d3f348e\`, paid a heavy null-hub witness when \(q_i>1/2\) and \(|g_i|\ge1/64\), with bound \(<64.180\).

Apply the new theorem with
\[
a=\frac1{64}.
\]
Since \(64^{2/3}=16\), every bounded-window four-coordinate exact-rank-three core with at least one such physical edge obeys
\[
\boxed{\;
\|p_Q\|_\infty
\le16\cdot576^{1/3}\frac{L^{2/3}}s
<133.126\,\frac{L^{2/3}}s.
\;} \tag{4.1}
\]
This removes the former \(q_i>1/2\) gate in this matched four-coordinate bounded-window scope. The pair-log estimate remains sharper where its own gate holds; (4.1) covers the complementary \(q_i\le1/2\) configurations without a rotated-independence claim.

Equivalently, within this core the only state not paid by (4.1) satisfies the explicit original-coordinate obstruction
\[
|B_{01}|,|B_{02}|,|B_{03}|<\frac1{64}. \tag{4.2}
\]

## 5. What remains

The new result is not the full theorem. A global structural argument must still produce a qualifying exact-rank-three \(4\times4\) principal core with a controlled upper spectral window, or route failure into an already-paid cross-volume, ridge, grouped-source, or compound-hub branch. The genuinely tiny-edge endpoint (4.2), convex/two-sheet collar, and arbitrary additional-spectrum assembly remain open.

Continuity is separate. Fleet01/B18 did not claim a continuous representative for (1.1), so this report claims only an essentially bounded density.
