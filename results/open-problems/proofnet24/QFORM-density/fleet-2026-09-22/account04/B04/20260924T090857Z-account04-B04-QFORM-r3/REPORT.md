# account04/B04 r3 — exact capped-Gibbs volume sampling closes the tight rank-two heavy-marginal branch

Programme: \`QFORM-DENSITY-3EIG-20260922\`  
Run: \`20260924T090857Z-account04-B04-QFORM-r3\`  
Status: **ESSENTIAL STEP APPLIED / FULL TARGET OPEN**

The unrestricted QFORM conjecture remains open. Continuity is distinct. This report proves a new exact optimization theorem for admissible volume-sampling weights and applies it to the first uncovered branch of account01/B04's row-matroid compiler. All rows and variables are in original coordinates.

## 1. Sources and live branch

Claude source was refreshed through the later directory commit
\`yspennstate/math-open-problems@b0cbc2233369b6a3f366cf569d425f485f123e1c\`,
starting from the required
\`e5f71d79eff325201dd0274053d20268ce65b837\`
files under
\`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/\`.
The Claude results remain scoped inputs, not a full proof.

The completed account01/B04 theorem used here is
\`yspennstate/math-open-problems@ad493c8b62e0b515fbfd8935d3a9ca063a59154d\`,
\`proofnet24/QFORM-density/fleet-2026-09-22/account01/B04/20260924T064404Z-account01-B04-QFORM-auto11-r31/REPORT.md\`.

Its live tight-rank-two-flat setup is as follows. A literal physical cross block has a rank-two row flat \(F\), exactly two rows \(a,b\) outside \(F\), and
\[
 W=\operatorname{span}\{m_i:i\in F\},\qquad
 h_a=\operatorname{dist}(m_a,W),\quad
 h_b=\operatorname{dist}(m_b,W).
\]
For supported flat pairs \(e=\{i,j\}\), put
\[
 d_e=\det\operatorname{Gram}(m_i,m_j)>0.
\]
A probability law \(q\) on supported pairs is admissible when every flat-row marginal
\[
 \beta_i(q)=\sum_{e\ni i}q_e
\]
is at most \(1/2\). From \(q\), split each pair equally between the two outside rows:
\[
 p_{a,e}=p_{b,e}={q_e\over2}.
\]
The resulting triple law has every physical-row marginal at most \(1/2\), and its determinant-entropy currency is
\[
 G(q)=2h_ah_b
 \exp\left(H(q)+\sum_e q_e\log d_e\right).
 \tag{1}
\]
Account01/B04 r31 proved the result when the unconstrained Gibbs law \(q_e=d_e/\sum_fd_f\) is admissible. Its first uncovered tight-rank-two case was a canonical marginal \(>1/2\).

## 2. Exact optimized admissible weights

### Theorem — \`QFORM-TIGHTFLAT-CAPPED-GIBBS-DUAL-v1\`

Assume the admissible pair polytope is nonempty. Define
\[
 \Phi(d)=
 \max_{\substack{q_e\ge0,\ \sum_eq_e=1\\
                  \beta_i(q)\le1/2\ \forall i}}
 \left\{H(q)+\sum_eq_e\log d_e\right\}.
 \tag{2}
\]
Then
\[
 \boxed{
 \Phi(d)=
 \inf_{\lambda_i\ge0}
 \left[
 {1\over2}\sum_i\lambda_i+
 \log\sum_{\{i,j\}}d_{ij}e^{-\lambda_i-\lambda_j}
 \right].
 }
 \tag{3}
\]
Consequently
\[
 \boxed{
 G^*_{1/2}(M)\ge2h_ah_b e^{\Phi(d)}
 }
 \tag{4}
\]
and the completed product-Fourier receiver gives
\[
 \boxed{
 \|p_Q\|_\infty
 \le6\sqrt e\,[2h_ah_b e^{\Phi(d)}]^{-1/6},
 \qquad p_Q\in C_0(\mathbb R).
 }
 \tag{5}
\]

#### Proof

Introduce multipliers \(\lambda_i\ge0\) for the constraints
\(\beta_i(q)\le1/2\). The Lagrangian is
\[
 H(q)+\sum_eq_e\log d_e
 +\sum_i\lambda_i(1/2-\beta_i(q)).
\]
For fixed \(\lambda\), maximizing over the probability simplex gives
\[
 {1\over2}\sum_i\lambda_i+
 \log\sum_{\{i,j\}}d_{ij}e^{-\lambda_i-\lambda_j}.
\]
Finite-dimensional convex duality yields (3); boundary-feasible cases follow by the same finite entropy variational formula or by a vanishing interior regularization. Equation (4) is (1) evaluated at the optimizer, and (5) is the already-completed half-row-cap product-Fourier theorem. QED.

The optimizer is a genuinely capped Gibbs law:
\[
 q_{ij}={d_{ij}e^{-\lambda_i-\lambda_j}\over
              \sum_{k<\ell}d_{k\ell}e^{-\lambda_k-\lambda_\ell}},
 \tag{6}
\]
with complementary slackness
\[
 \lambda_i>0\Longrightarrow\beta_i(q)=1/2.
 \tag{7}
\]
Thus the admissible weights are optimized on the same physical matrix; no support-only surrogate or rotated independence is introduced.

## 3. A determinant-only lower certificate

The exact dual also has a useful explicit lower bound. Let
\[
 S_{\rm dis}
 =\sum_{\substack{(e,f)\ {\rm ordered}\\e\cap f=\varnothing}}
 d_ed_f.
 \tag{8}
\]
If \(S_{\rm dis}>0\), define a probability law on ordered disjoint pairs by
\[
 \pi(e,f)={d_ed_f\over S_{\rm dis}},
\]
and let \(q\) be its first marginal. Symmetry gives the same second marginal. Since \(e\cap f=\varnothing\),
\[
 \mathbb P(i\in e)+\mathbb P(i\in f)\le1,
\]
so every marginal of \(q\) is at most \(1/2\).

Moreover,
\[
 \log S_{\rm dis}
 =H(\pi)+\mathbb E_\pi\log(d_ed_f)
 \le2H(q)+2\sum_eq_e\log d_e.
\]
Therefore
\[
 e^{\Phi(d)}\ge
 \exp\left(H(q)+\sum_eq_e\log d_e\right)
 \ge\sqrt{S_{\rm dis}},
\]
and
\[
 \boxed{
 G^*_{1/2}(M)\ge2h_ah_b\sqrt{S_{\rm dis}}.
 }
 \tag{9}
\]

For a rank-two row matroid, \(S_{\rm dis}>0\) is equivalent to two disjoint supported pairs. By account01/B04 r31's exact base-packing theorem, this is precisely pair-law feasibility. Hence every feasible tight-rank-two flat is now paid, including all cases where the canonical pair-volume marginal exceeds \(1/2\).

This closes the tight-rank-two heavy-canonical-marginal item left in account01/B04 r31.

## 4. Concrete heavy-marginal family

Take four physical flat rows in \(\mathbb R^3\):
\[
 u_1=(R,0,0),\quad u_2=(0,1,0),\quad
 u_3=(0,1,0),\quad u_4=(1,0,0),
 \qquad R>1,
\]
and two outside rows
\[
 a=b=(0,0,2).
\]
The supported flat-pair graph is \(K_{2,2}\). Its weights are
\[
 d_{12}=d_{13}=R^2,\qquad
 d_{42}=d_{43}=1.
\]
The unconstrained Gibbs marginal at \(u_1\) equals
\[
 {R^2\over R^2+1}>{1\over2},
 \tag{10}
\]
so account01/B04 r31's canonical-marginal hypothesis fails.

For any admissible \(q\), all four vertex marginals must equal \(1/2\). The weight contribution is therefore fixed:
\[
 \sum_eq_e\log d_e=\log R.
\]
Entropy is maximized by \(q_e=1/4\) on the four supported edges, so
\[
 e^{\Phi(d)}=4R.
\]
Since \(h_a=h_b=2\),
\[
 \boxed{G^*_{1/2}(M)\ge32R.}
 \tag{11}
\]
At \(R=4\), the completed Fourier theorem gives the concrete bound
\[
 \boxed{
 \|p_Q\|_\infty
 \le6\sqrt e\,128^{-1/6}
 =4.406530999912367\ldots .
 }
 \tag{12}
\]

This is an actual application of the account01/B04 receiver at the optimized admissible weights, in a case its earlier canonical law did not cover.

## 5. Same-matrix comparison of \(D'\), \(D_5\), and ridge

Right-multiply all six rows by the dense orthogonal Householder matrix
\[
 V={1\over7}
 \begin{pmatrix}
 6&-2&-3\\
 -2&3&-6\\
 -3&-6&-2
 \end{pmatrix}.
\]
All physical crossing entries become nonzero, while row Gram determinants and singular values are unchanged. Form the dense symmetric target matrix
\[
 A_R=
 \begin{pmatrix}
 \epsilon J_6&M_R\\
 M_R^\top&\epsilon J_3
 \end{pmatrix},
 \qquad \epsilon={1\over100}.
\]
Before perturbation,
\[
 M_R^\top M_R
 =V^\top\operatorname{diag}(R^2+1,2,8)V.
\]
Thus all three singular values are at least \(\sqrt2\). Weyl's inequality leaves at least three positive and three negative eigenvalues of \(A_R\) with modulus greater than
\[
 \sqrt2-{6\over100}>1.
\]

On this same matrix:

1. **Optimized \(D'\).** Equation (11) gives \(G^*_{1/2}\ge32R\), hence (12) at \(R=4\), with a continuous \(C_0\) density.

2. **\(D_5\).** The literal cross block has rank three, so every fifth compound vanishes:
\[
 E_5(M_R)=0.
\]
The \(D_5\) certificate is unavailable.

3. **Ridge.** The row-space leverage of \(u_1\) is
\[
 {R^2\over R^2+1}.
\]
At \(R=4\) it is \(16/17\), so every diffuse spectral-window ridge gate with threshold \(1/12\), \(1/32\), or smaller fails strongly.

Therefore the optimized \(D'\) certificate pays a genuinely dense target-valid matrix on which \(D_5\) vanishes and ridge diffuseness fails. This is a same-matrix comparison, not a comparison across incompatible examples.

## 6. Proof-graph update and remaining case

The rank-three row-matroid trichotomy now routes as follows:

- If the half-cap packing number is \(>2\), use the support cap \(3/7\) and the weighted \(D'\) optimization.
- If it equals \(2\) through a tight rank-two flat, Theorem (3) pays every feasible weight configuration, including heavy canonical marginals.
- If it is \(<2\), account01/B04 r31 gives an explicit physical collapse: a rank-two flat plus at most one outside row, a rank-one flat plus at most three outside rows, or at most five nonzero physical rows.

The first remaining implication is therefore no longer the tight-rank-two weight problem. It is
\[
 \text{\`QFORM-COLLAPSED-FLAT-TO-PAID-HUB-v1\`},
\]
together with the tight rank-one/rank-zero faces. One must route those literal low-flat configurations to the existing hub, pair, scalar-pivot, or finite-coordinate receivers without discarding same-bank curvature. The separate shared-bank convex/two-sheet collar also remains.

## 7. Scope discipline

No arbitrary-joint coarea estimate, conditional density cap, pointwise quadratic-phase decay, post-rotation independence, moment assumption, or bounded-support assumption is used. The orthogonal matrix \(V\) is used only to construct and spectrally verify a dense coefficient matrix; the random coordinates are never rotated.

The full universal density theorem remains open.
