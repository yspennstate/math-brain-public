# B18 — curvature-lift envelope and a Q-currency good-split reduction

**Status:** PARTIAL / PROVED REDUCTION. Full uniform-cube Fourier entropy--influence remains **OPEN / NOT PROVED**.

**Execution:** **WITHOUT_VERIFIED_BRAIN**. Authenticated source artifacts were read directly; no authenticated cognitive-brain retrieval entered the proof.

## 1. Fresh source state consumed

The live owner target is the all-gate inequality
\[
\Gamma(p_{out})+H_t(G;p)\le \sum_i \operatorname{It}_i(G;p)\frac{\Gamma(p_i)+h(V_{p_i})}{V_{p_i}}. \tag{G}
\]
I use the exact gate reformulation, account04/B12's Shannon child-slack/Poincare-currency recursion, account02/B17's constant-for-constant balanced equivalence, and the fresh 162-input balanced obstruction recorded by account03/B13. The latter proves that the old read-once-scale universal candidate is already refuted on the balanced-uniform slice. I do **not** reuse the refuted AND-extremality claim.

The previous account04/B18 exact zero-depth classification and mixed-curvature identities remain valid historical inputs, but are not promoted into an unconditional FEI closure here.

## 2. PROVED: scalar curvature-lift envelope

Fix any symmetric nonnegative reference potential \(\Gamma_0\), with endpoint normalization \(\Gamma_0(0)=\Gamma_0(1)=0\), and put
\[
v(p)=p(1-p),\qquad \Gamma_\lambda(p)=\Gamma_0(p)+\lambda v(p),\quad \lambda\ge0.
\]
For a gate/bias instance write its defect under \(\Gamma_0\) as \(D_0(G;p)\), and define
\[
P_G:=\frac{I(G;p)}4-p_{out}(1-p_{out})\ge0.
\]
Then exactly
\[
\boxed{D_{\lambda}(G;p)=D_0(G;p)+\lambda P_G.} \tag{2.1}
\]
This follows because \(v(p_i)/V_{p_i}=1/4\) for every input and the output contributes \(-v(p_{out})\).

For \(P_G>0\), define
\[
c_G^{(0)}(p):=-\frac{D_0(G;p)}{P_G}.
\]
Hence, within this one-parameter family,
\[
\boxed{(G)\text{ for }(G,p)\iff \lambda\ge c_G^{(0)}(p).} \tag{2.2}
\]
Consequently, if all zero-currency instances have \(D_0\ge0\) and
\[
\lambda_*:=\sup_{G,p:P_G>0}c_G^{(0)}(p)<\infty,
\]
then \(\Gamma_{\lambda_*}\) is a universal gate potential and FEI follows with
\[
\boxed{C=\Gamma_0(1/2)+\lambda_*/4.} \tag{2.3}
\]
Conversely no smaller \(\lambda\) can work inside this scalar-lift family. This is a reduction, not a proof that \(\lambda_*<\infty\).

## 3. PROVED: the B12 split currency is exactly higher-order biased Fourier mass

Fix an input \(i\) of bias \(t\). Let \(G_0,G_1\) be the restrictions, let
\[
d_i=\Pr(G_0\ne G_1),\qquad \Delta p_i=p_1-p_0,
\]
and use B12's exact currency
\[
Q_i=t(1-t)\bigl[d_i-(\Delta p_i)^2\bigr]. \tag{3.1}
\]
Let \(w_S=\widehat G_p(S)^2\) be the squared biased Fourier coefficients in the orthonormal product basis. Then
\[
\operatorname{It}_i=4t(1-t)d_i=\sum_{S\ni i}w_S,
\]
while the singleton coefficient satisfies
\[
w_{\{i\}}=4t(1-t)(\Delta p_i)^2.
\]
Subtracting gives the exact identity
\[
\boxed{4Q_i=\sum_{S\ni i,\ |S|\ge2}w_S.} \tag{3.2}
\]
Also Parseval gives
\[
4P_G=I(G;p)-4p_{out}(1-p_{out})
=\sum_{|S|\ge2}(|S|-1)w_S. \tag{3.3}
\]
Therefore
\[
\boxed{P_G\le\sum_iQ_i\le2P_G,} \tag{3.4}
\]
because
\[
4\sum_iQ_i=\sum_{|S|\ge2}|S|w_S
\]
and \(1\le |S|/(|S|-1)\le2\) for \(|S|\ge2\).

Thus the one-step B12 currencies across the root coordinates already cover the entire global Poincare-defect currency with overlap at most two. This is the direct interface between the Shannon recursion and a coordinate selector; no ambient dimension enters.

## 4. PROVED: good-split / aggregate-selector induction

B12 proves for every split input \(i\)
\[
D_0(G)=(1-t)D_0(G_0)+tD_0(G_1)+R_i^{(0)},
\]
and after the scalar lift
\[
\boxed{D_\lambda(G)=(1-t)D_\lambda(G_0)+tD_\lambda(G_1)
+R_i^{(0)}+\lambda Q_i.} \tag{4.1}
\]
Hence an arity induction does **not** need every local residual to be nonnegative. It is enough that, after the two child gates are already known, there exists one input with
\[
\boxed{R_i^{(0)}+\lambda Q_i\ge0.} \tag{4.2}
\]

A sufficient all-gate selector statement is therefore
\[
\boxed{\sum_i\bigl(R_i^{(0)}+\lambda Q_i\bigr)\ge0} \tag{4.3}
\]
for every non-affine gate/bias instance: (4.3) forces at least one good split, and (4.1) closes the induction. Equivalently, writing \(c_{R,i}^{(0)}=-R_i^{(0)}/Q_i\) on \(Q_i>0\),
\[
\frac{\sum_iQ_i c_{R,i}^{(0)}}{\sum_iQ_i}\le\lambda. \tag{4.4}
\]
By (3.4), the still stronger but very concrete bank inequality
\[
\boxed{\sum_i(-R_i^{(0)})\le\lambda P_G} \tag{4.5}
\]
also suffices.

This is the smallest honest replacement I obtain for the refuted blind arity induction: prove one **aggregate one-step residual bank**, then select a split. It is compatible with the existing adaptive/crossing machinery, which may be used to prove (4.3)/(4.5); those conditional inputs are not themselves treated as closure.

## 5. Sharp current calibration from the balanced obstruction

Take as \(\Gamma_0\) the rigorously certified read-once potential whose proved cap is
\[
C_0=\Gamma_0(1/2)=6.4573.
\]
The fresh 162-input balanced source certifies
\[
6.521850083658612443633672199029299526203969333669
\le R_{162}:=\frac{H(F)}{I(F)-1}
\le
6.521850083658612443633672199029299526203969334600.
\]
For a balanced gate at uniform bias, any reference potential satisfies
\[
c_G^{(0)}=4\left(\frac{H(G)}{I(G)-1}-C_0\right).
\]
Therefore every scalar lift of this certified reference must have
\[
\boxed{\lambda_*\ge
0.258200334634449774534688796117198104815877334676.} \tag{5.1}
\]
The corresponding upper endpoint is
\[
0.258200334634449774534688796117198104815877338400.
\]

Thus one exact remaining target is now:

> prove (4.3), or the stronger (4.5), for the certified reference potential with \(\lambda\) equal to the upper endpoint above.

If that universal selector inequality is proved, (2.3) gives an all-gate potential with cap at most the certified upper endpoint of \(R_{162}\), while the balanced recursive-composition theorem supplies the matching lower endpoint. That would close FEI to the width of the existing source-certified entropy interval. **This selector inequality is not proved here.**

## 6. Decisive finite check of the new algebra

A standard-library exact-rational checker independently tested (3.1)--(3.4) on every Boolean gate through arity three and every product-bias vector with coordinates in \(\{1/3,1/2,2/3\}\): **7,068 gate/bias instances**, zero failures. It checked Parseval, the split formula for every coordinate, the singleton subtraction, and both inequalities in (3.4). These checks support the implementation only; the theorem above is analytic.

## 7. Preserved exclusions and exact remaining arrow

Preserved as refuted or insufficient: universal AND/decomposable extremality at the read-once-scale cap; the blind requirement that every Shannon split have nonnegative local residual; the per-coordinate erasure bound; \(\sum d_i=O(J)\); prescribed-coordinate payment; fixed-relative near-subcube payment; dropping total-correlation or negative-credit terms.

Preserved as proved but not used as closure: account04/B18 mixed-curvature symmetry and exact zero-depth classification; account01/B18 folded-cooling/curvature refunds; account04/B13-B14 asymmetric stability and physical boundary-cover steps.

**Remaining universal implication:** prove the aggregate selector bank (4.3), preferably by charging its negative residuals to the higher-order currency (3.2) using the existing curvature/crossing refunds without reuse. Full FEI remains OPEN.
