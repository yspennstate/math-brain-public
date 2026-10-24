# account04/B18 — balanced-bank Schur-isotropic closure

Run: \`20260923T021454Z-account04-B18-QFORM-r1\`

Status: \`ESSENTIAL_STEP_APPLIED / SUPPORTING_TARGET_BRANCH_PROVED / FULL_TARGET_OPEN\`.

## Target and source pins

The target is the universal density conjecture for independent real original-coordinate inputs with density caps one and a symmetric matrix having at least three eigenvalues of modulus at least one. Continuity is separate.

This report applies account01/B18's completed full-bank LPP--Plancherel theorem at scientific commit \`a9cecd1c7eaa605bd5d4bfd69ae9d9cb721705b7\`. Its primary analytic input is the Livshyts--Paouris--Pivovarov marginal theorem (arXiv:1507.07949; Israel J. Math. 216 (2016), 877--889), used exactly for orthogonal marginals of product measures. The Claude source pin is \`e5f71d79eff325201dd0274053d20268ce65b837\`.

No independence after rotation, conditional projection cap, arbitrary-joint coarea estimate, moment assumption, bounded support assumption, or law-uniform pointwise quadratic-phase estimate is used.

## The balanced-bank theorem

Consider the exact-rank-three Schur-isotropic core

\[
 Q=(Y+uX_0)^T D(Y+uX_0),\qquad Y=V^T X_{\rm res},
\]

where \(X_0\) is an original coordinate independent of the residual original coordinates,
\(V^TV=I_3\), \(D=D^T\) is invertible, and \(u^TDu=0\). Put \(r=\|u\|\) and
\[
 L=[u,V^T],\qquad G=LL^T=I+uu^T.
\]
Assume the residual physical columns admit a partition into two disjoint original-coordinate banks \(I_0,J\) satisfying
\[
 \sum_{i\in I_0}v_iv_i^T=\alpha I_3,\qquad
 \sum_{j\in J}v_jv_j^T=(1-\alpha)I_3
\]
for some \(0<\alpha<1\). Adjoin the special column \(u\) to \(I_0\), producing \(I\).

Then \(Q\) has a continuous density and
\[
\boxed{\;
\|p_Q\|_\infty
\le 6\left[
\frac{\alpha(1-\alpha)^{3/2}\sqrt{\alpha+r^2}}{1+r^2}
\right]^{-1/3}.
\;}
\tag{1}
\]

This statement is valid for arbitrary cap-one laws on every physical coordinate.

### Proof

The two disjoint bank Gram matrices are
\[
G_I=uu^T+\alpha I_3,\qquad G_J=(1-\alpha)I_3.
\]
The matrix determinant lemma gives
\[
\det G_I=\alpha^2(\alpha+r^2),\qquad
\det G_J=(1-\alpha)^3.
\tag{2}
\]
The three nonzero eigenvalues of \(A=L^TDL\) are those of \(G^{1/2}DG^{1/2}\), hence
\[
|\operatorname{pdet}A|=|\det D|\det G=|\det D|(1+r^2).
\tag{3}
\]
Under the target spectral hypothesis, \(|\operatorname{pdet}A|\ge1\), so
\[
|\det D|\ge(1+r^2)^{-1}.
\tag{4}
\]
Account01/B18's full-bank theorem gives, before any local minor is selected,
\[
\|p_Q\|_\infty\le
6\bigl[|\det D|\sqrt{\det G_I\det G_J}\bigr]^{-1/3}.
\tag{5}
\]
Substituting (2) and (4) into (5) proves (1). The same theorem yields continuity. All bank independence is original-coordinate independence.

## Exact optimization

Writing \(R=r^2\), maximize
\[
H_R(\alpha)=\frac{\alpha(1-\alpha)^{3/2}\sqrt{\alpha+R}}{1+R}.
\]
The unique critical point in \((0,1)\) solves
\[
6\alpha^2+(5R-3)\alpha-2R=0,
\]
therefore
\[
\boxed{\;
\alpha_*(R)=
\frac{3-5R+\sqrt{25R^2+18R+9}}{12}.
\;}
\tag{6}
\]
It is the unique maximizer because \(H_R\) vanishes at both endpoints and its logarithmic derivative has exactly one zero.

Consequently
\[
\boxed{\;
\|p_Q\|_\infty\le 6H_{r^2}(\alpha_*(r^2))^{-1/3}.
\;}
\tag{7}
\]

The envelope theorem and the critical-point equation give
\[
 \frac{d}{dR}\log H_R(\alpha_*(R))
 =\frac{1-R-2\alpha_*(R)}{2(\alpha_*(R)+R)(1+R)}.
\]
This derivative is negative for every \(R>0\). Indeed, for \(R\ge1\) this is immediate. For \(0<R<1\), substituting \(\beta=(1-R)/2\) into the critical polynomial
\[
 f_R(\alpha)=6\alpha^2+(5R-3)\alpha-2R
\]
gives \(f_R(\beta)=-R-R^2<0\), while its positive root is \(\alpha_*(R)\); hence \(\alpha_*(R)>\beta\). Therefore the optimized density constant is increasing in \(R=r^2\).

For the live moderate-shear regime \(1/2\le r\le2\), its maximum is consequently attained at \(r=2\), and exact substitution gives
\[
\boxed{\|p_Q\|_\infty<14.041.}
\tag{8}
\]
This removes the earlier rowwise mixed-volume gate \(p_j+q_j\le1\) for every balanced-split residual frame.

For the explicit account01/B18 example \(r=2\), the optimized value is
\[
\alpha_*=(\sqrt{481}-17)/12
\]
and (7) gives \(14.040422\ldots\), slightly sharper than the equal split bound
\[
6(40/3)^{1/3}=14.227573\ldots.
\]

## Honest boundary

As \(r\to\infty\), \(\alpha_*(r^2)\to2/5\) and (7) grows like a constant times \(r^{1/3}\). Thus this theorem does not pay extreme shear uniformly. It also requires an exact balanced Parseval partition; a general mixed physical frame need not have one.

The full conjecture remains open. The first unpaid implication is a quantitative interpolation: for an arbitrary Schur-isotropic frame, either extract two disjoint banks with determinant product at the scale used in (5), or route concentration of volume-sampled bases to an already-paid high-leverage hub/pivot branch. Arbitrary additional spectrum is a separate unresolved interaction.
