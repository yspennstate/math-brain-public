# Keeper: nine-direction candidate and the exact \(s_8\) boundary

## Bottom line

The current strongest source is the 20-page candidate
\[
s_9(A)\ge s
\quad\Longrightarrow\quad
\|p_{X^\top AX+b^\top X+c}\|_\infty\le {400K^2\over s}.
\]
Its overlap/interpolation section has now passed an independent scoped audit.
The entire constant-\(400\) manuscript has not yet received two independent
end-to-end reviews, so it is retained as a candidate rather than promoted to
a fully certified theorem.

The unrestricted three-eigenvalue conjecture remains open.

## Source pin

- Path:
  \`proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/interactive/20260924T145418Z-nine-400/paper.tex\`
- Commit: \`eeb752c8943536541b34b42b8bf48e924f4d3d2f\`
- Blob: \`19fb119877426b640b2c0dae19ec2f78a399fe11\`
- SHA-256: \`bf1caf6ae4b4bc33992f501c169b5dc6c795db757b0f6089eff9991391effdf3\`

## Noncircular proof graph

1. **Scaling.** Reduce cap \(K\) and threshold \(s\) to the normalized case.
   Restore the factor \(K^2/s\) only at the end.

2. **Physical pivot branches.** Use only original-coordinate diagonal or
   cross pivots. The source's half-potential and logarithmic-receiver bounds
   pay the branches satisfying their explicit pivot hypotheses.

3. **Volume branch.** For disjoint \(r\)-seeds, volume sampling and bordered
   minors give
   \[
   W^\times_{r,1}+(r+1)^2V_{r+1}
   \ge V_r\sum_{j>3r}s_j(A)^2.
   \]
   The rank, support, determinant, and expectation steps of this implication
   independently pass.

4. **Nine-direction terminal.** At \(r=2\), the source uses the singular tail
   beyond rank six together with the remaining analytic branches to reach
   its constant \(400\). This full compiler still requires independent
   end-to-end review; earlier reviews of older constants do not certify it.

5. **Attempted eight-direction extension.** If \(s_8(A)\ge1\), the same
   physical two-seed can be chosen so that its Schur residual \(C=D+E\)
   obeys
   \[
   \boxed{
   \|E\|_F^2\le9{V_3\over V_2},\qquad
   \|D\|_F^2\ge2-9{V_3\over V_2}.}
   \]
   In the live chamber \(V_2\ge\kappa^2\), \(V_3<\kappa^3\),
   \(\kappa=4/625\),
   \[
   \boxed{\|E\|_F<6/25,\qquad \|D\|_F^2>1214/625.}
   \]

6. **Why rank counting stops here.** For \(r=1\), the completion
   \[
   R=\begin{pmatrix}a&b&c\\b&e&d\\c&d&cd/b\end{pmatrix}
   \]
   has
   \[
   \det R=-{(ad-bc)(bd-ce)\over b}.
   \]
   The choice \((a,b,c,d,e)=(0,1,1,2,0)\) gives determinant \(2\).
   Thus \(\operatorname{rank}R=3=3r\) can occur, so replacing \(3r\) by
   \(2r\) is false.

7. **Remaining analytic leaf.** The \(s_8\) survivor has a Schur residual
   close to a diagonal matrix with large aggregate diagonal mass, but that
   mass may be diffuse across arbitrarily many coordinates. The Schur
   correction also shares the pivot variables. What remains is a
   dimension-free shared-coordinate receiver; neither post-rotation
   independence nor a worst conditional-density supremum is available.

## New proofs retained

- Scoped overlap audit and exact arithmetic:
  \`fixed-multiplicity-2026-09-24/audits/account04/B02/20260924T161206Z-account04-B02-nine400-overlap-audit-r1/\`
- Same-seed \(s_8\) volume/ridge certificate:
  \`fleet-2026-09-22/account04/B04/20260924T161310Z-account04-B04-volume-seed-r1/\`
- Exact rank-\(3r\) sharpness witness:
  \`fleet-2026-09-22/account04/B10/20260924T161445Z-account04-B10-rank3-sharpness-r1/\`

## Review status

- Overlap/interpolation section: **PASS**.
- Exact \(s_8\) same-seed corollary: **PROVED**.
- Rank-\(3r\) sharpness witness: **PROVED**.
- Full \(s_9\), constant-\(400\) candidate: **awaiting two genuine independent
  end-to-end reviews**.
- \(s_8\) theorem: **open**.
- Original \(s_3\) theorem: **open**.
