# Independent geometric Brascamp--Lieb and grouped-Fourier audit

Run: \`20260924T171255Z-fleet04-B04-nine400-bl-audit-r1\`  
Objective: \`QFORM-FIXED-MULTIPLICITY-AUDIT-20260924\`  
Reviewer: fleet04/B04  
Verdict: **PASS for the audited analytic chain; not an end-to-end certification of the entire paper.**

## Source pin

- Repository: \`yspennstate/math-open-problems\`
- Commit: \`eeb752c8943536541b34b42b8bf48e924f4d3d2f\`
- Source: \`proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/interactive/20260924T145418Z-nine-400/paper.tex\`
- Git blob: \`19fb119877426b640b2c0dae19ec2f78a399fe11\`
- SHA-256: \`bf1caf6ae4b4bc33992f501c169b5dc6c795db757b0f6089eff9991391effdf3\`

I independently reconstructed the arguments in source lines 216--527 and their live use in lines 663--856. I also checked the Fourier normalization in lines 87--160 and the no-pivot spectral-to-volume input in lines 663--766 sufficiently to verify the application below. I did not treat this scoped audit as a substitute for the two requested independent end-to-end reviews.

## 1. Geometric rank-one Brascamp--Lieb: PASS

The datum is
\[
 \sum_i c_i u_i u_i^T=I_d,\qquad |u_i|=1,\qquad c_i>0.
\]
For \(f_i(t,\cdot)=g_t*h_i\), \(v_i=\partial_s\log f_i\), and
\[
 F(t,x)=\prod_i f_i(t,u_i\cdot x)^{c_i},
\]
direct differentiation gives
\[
 \partial_tF-\Delta F
 =F\left(\sum_i c_i v_i^2-
 \left|\sum_i c_i u_i v_i\right|^2\right).
\]
Writing \(W=(\sqrt{c_i}u_i)_i\), the frame identity is \(WW^T=I_d\), hence \(\|W\|=1\), and the bracket is nonnegative. Therefore \(\int F(t,x)\,dx\) is nondecreasing.

The two limiting steps are valid:

1. At \(t\to\infty\), \(\sum_i c_i=d\) and
   \[
   \sum_i c_i(u_i\cdot z)^2=|z|^2
   \]
   yield the correct Gaussian limit and constant \(1\).
2. At \(t\downarrow0\), preimages of one-dimensional null sets under nonzero linear functionals are null, so simultaneous Lebesgue-point convergence holds almost everywhere. Fatou gives the desired inequality. Monotone truncation handles general nonnegative integrable inputs.

No hidden rotational-independence assumption occurs.

## 2. Product-projection density: PASS

For an orthonormal \(U\in\mathbb R^{n\times d}\), complete it to \((U,W)\). With
\[
 b_i=|w_i|^2=1-|U^Te_i|^2
\]
and \(v_i=w_i/\sqrt{b_i}\), the exact frame identity is
\[
 \sum_{b_i>0}b_i v_i v_i^T=I_{n-d}.
\]
Applying the preceding Brascamp--Lieb inequality to
\[
 h_i(t)=f_i((Uy)_i+\sqrt{b_i}t)^{1/b_i}
\]
is legitimate because \(0\le f_i\le1\), so
\[
 \int h_i\le b_i^{-1/2}.
\]
Consequently,
\[
 p_{U^TX}(y)\le\prod_{b_i>0}b_i^{-b_i/2}
 \le \exp\!\left(\frac12\sum_i(1-b_i)\right)=e^{d/2}.
\]
This is a deterministic marginal calculation in original product coordinates, not a claim that \(U^TX\) has independent coordinates.

The scalar consequence
\[
 \|p_{a\cdot X}\|_\infty\le\frac{\sqrt e}{|a|}
\]
and the integrated Fourier-power estimate
\[
 \int_{\mathbb R}|\widehat f(t)|^p\,dt
 \le\frac{2\pi\sqrt{2e}}{\sqrt p},\qquad p\ge2,
\]
then follow with the manuscript's Fourier convention. The factors \(2\pi\) and \(\sqrt2\) are correct.

## 3. Regularized crossing determinant: PASS

For
\[
 H=(2\pi e)^2I+(2t)^2M^TM
\]
the coordinate and row vectors used in the proof form an exact rank-one frame. Applying the geometric inequality gives the displayed graph integral. The entropy factor
\[
 \prod_j c_j^{-c_j/2}\le e^{\theta/2}
\]
combines with the scalar Fourier factors to cancel because
\[
 \sqrt{\alpha}=2\pi e,\qquad \alpha=(2\pi e)^2.
\]
After the fourth root from the decoupling inequality, this gives exactly
\[
 |\phi_Q(t)|
 \le\det\!\left(I+\frac{t^2}{\pi^2e^2}M^TM\right)^{-1/8}.
\]
The density caps used here apply to independent difference coordinates in the physical basis. No independence after diagonalizing \(M^TM\) is invoked.

## 4. Grouped mollified-\(L^2\) receiver: PASS

The delicate order is correct.

- The phase-weighted image \(\mu_t\) is dominated in total variation by the ordinary image law; the full-row-rank \(M_J\) image has a bounded density, so \(\mu_t\in L^1\cap L^2\).
- Jensen is applied to \(\|\mu_t*\rho_\delta\|_2^2\), before removing the mollifier.
- Expansion with independent \(X_J,X'_J\) gives the nonnegative kernel
  \[
  K_\delta(M_JD),\qquad D=X_J-X'_J.
  \]
- The pure \(J\)-phase is discarded only after integrating the original independent \(I\)-coordinates, which produces the scalar Fourier factors.
- Weighted Hölder is applied to a finite measure; it does not require that this kernel-weighted measure have total mass one.
- For a selected \(\ell\)-set \(T\), the map
  \[
  D\mapsto\bigl(M_JD,(c_iD)_{i\in T}\bigr)
  \]
  has Gram determinant
  \[
  S^2\det(C_TC_T^T).
  \]
  The product-projection lemma therefore supplies the stated density cap with the correct Jacobian.
- The entropy inequality
  \[
  H(w)+\sum_i\alpha_i\log\alpha_i
  \le\ell\log\ell-\log(\ell!)
  \]
  follows by randomly ordering a sampled subset and applying entropy subadditivity.

The bound is uniform in \(\delta\), and the already established \(L^2\) membership justifies approximate-identity convergence. The resulting constant
\[
 B_{k,\ell}
 =\pi^{(k+\ell)/2}2^{\ell/4}e^{(k+2\ell)/4}
 \left(\frac{\ell^\ell}{\ell!}\right)^{1/4}
 S^{-1/2}Z_\ell^{-1/4}
\]
is consistent with the hub Plancherel factor and the \(\ell\) scalar Fourier integrations.

## 5. Heavy-row promotion: PASS

At every promotion, the chosen row is a literal original coordinate. Gram--Schmidt gives the exact identity
\[
 \text{incident \(q\)-volume}
 =|\text{chosen row}|^2
   \times\text{residual \((q-1)\)-volume}.
\]
After \(k\) heavy promotions, the hub Gram determinant times residual volume exceeds \(Z_q/2^k\). Couplings to unpromoted physical rows remain in \(M_I\); they are not discarded. Thus the row-marginal restriction is removed without rotating the product law.

For \(q=3\), the worst branch is the initial diffuse branch and
\[
 C_3=3\sqrt2\,e\,(9/2)^{1/6}
   =14.818337662843\ldots<15.
\]
For \(q=2\), the conclusion is correctly only the full half-potential estimate
\[
 \sup_a\mathbb E|Q-a|^{-1/2}
 \le C_2 Z_2(M)^{-1/8},
 \qquad C_2=8\sqrt e\,2^{-1/8}<14.
\]

## 6. Application to the live nine-direction branch

This is the concrete theorem-level application of the audited chain.

Assume the normalized no-pivot branch and \(s_9(A)\ge1\). The disjoint-minor interpolation argument gives
\[
 V_3(A)\ge\kappa^3,\qquad \kappa=\frac4{625}.
\]
A fair physical coordinate cut has expected crossing volume \(4^{-3}V_3\), so some original-coordinate cross block \(M\) satisfies
\[
 Z_3(M)\ge4^{-3}\kappa^3.
\]
Therefore
\[
 Z_3(M)^{-1/6}
 \le 4^{1/2}\kappa^{-1/2}
 =\frac{2}{2/25}=25.
\]
Applying the independently checked marginal-free receiver yields
\[
 \boxed{
 \|p_Q\|_\infty
 \le25C_3
 =370.458441571075\ldots
 <375.}
\]
This is the actual no-pivot terminal used in the constant-\(400\) proof.

## 7. Scope and remaining obligations

This audit found no gap in the geometric Brascamp--Lieb, product-projection, determinant, grouped-\(L^2\), or row-promotion chain, and it validates their no-pivot application above.

It does **not** by itself certify:

- every Schur-complement and pivot branch of the paper;
- the new overlap theorem as a route to eight eigenvalues;
- any theorem at eight or three eigenvalues;
- the complete manuscript as independently validated.

A second genuinely independent end-to-end reconstruction remains required before release certification. The current unrestricted three-eigenvalue conjecture also remains open.
