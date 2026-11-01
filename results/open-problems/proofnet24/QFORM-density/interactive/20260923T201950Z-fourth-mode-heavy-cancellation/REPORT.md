# A fourth spectral mode cancels a robust heavy two-plane

23 September 2026. This report gives an explicit arbitrary-rank obstruction to transferring the exact-rank-three heavy-Gram pivot lemma to a top-three spectral frame with an unrestricted tail. The same family has a uniform density bound, including arbitrary affine terms.

## Matrix family and spectrum

Fix \(m\ge2\). Use two original hub coordinates \(h_1,h_2\) and two disjoint groups of \(m\) original light coordinates. Let \(w_1,w_2\) be the uniform unit vectors on their respective light groups, and let \(0<\delta<1\). Define
\[
A_{m,\delta}
=2(e_{h_1}w_1^\mathsf T+w_1e_{h_1}^\mathsf T)
 +(e_{h_2}w_2^\mathsf T+w_2e_{h_2}^\mathsf T)
 +\delta e_{h_2}e_{h_2}^\mathsf T. \tag{1}
\]
The two nonzero invariant blocks, in bases \((e_{h_1},w_1)\) and \((e_{h_2},w_2)\), are
\[
\begin{pmatrix}0&2\\2&0\end{pmatrix},
\qquad
\begin{pmatrix}\delta&1\\1&0\end{pmatrix}.
\]
Thus the nonzero eigenvalues are exactly
\[
2,\quad -2,\quad
\lambda_+={\delta+\sqrt{\delta^2+4}\over2}>1,\quad
\lambda_-={\delta-\sqrt{\delta^2+4}\over2}\in(-1,0).
\]
In particular \(s_3(A_{m,\delta})=\lambda_+>1\), the unique top-three spectral subspace has residual spectral norm \(|\lambda_-|<s_3(A)\), and this ratio tends to one as \(\delta\downarrow0\).

Let \(U\) be any orthonormal frame for that top-three spectral subspace, and put \(H=\{h_1,h_2\}\). Both first-star eigenvectors are present, so \(e_{h_1}\) lies in the top-three subspace. For the second star, a normalized \(\lambda_+\)-eigenvector has squared hub component
\[
\theta_\delta={\lambda_+^2\over1+\lambda_+^2}>{1\over2}.
\]
The two hubs are orthogonal projections into distinct invariant blocks. Consequently
\[
\operatorname{spec}(U_H^\mathsf TU_H)=\{1,\theta_\delta,0\},
\qquad
\lambda_2(U_H^\mathsf TU_H)>1/2. \tag{2}
\]
Nevertheless the *actual* heavy principal matrix is
\[
(A_{m,\delta})_{HH}=\operatorname{diag}(0,\delta), \tag{3}
\]
and can be arbitrarily small. The negative fourth mode is essential for this cancellation.

## Failure of fixed physical pivots and third crossing volume

A \(c\)-pivot means either an original-coordinate diagonal entry of modulus at least \(c\), or an original principal two-by-two determinant of modulus at least \(c\). The only nonzero diagonal entry of \(A_{m,\delta}\) is \(\delta\). The only nonzero principal-pair determinants are
\[
\det A_{\{h_1,j\}}=-4/m
\quad(j\text{ in the first light group}),\qquad
\det A_{\{h_2,j\}}=-1/m
\quad(j\text{ in the second light group}).
\]
Hence for every fixed \(c>0\), choosing \(0<\delta<c\) and \(m>4/c\) leaves **no \(c\)-pivot anywhere**, despite (2) and \(s_3(A)>1\).

For any cut of the original coordinates into two sets, each hub–light star contributes at most rank one to the crossing block; the hub diagonal contributes nothing. Thus every physical cross block has rank at most two, and all its third singular values and third squared-minor volumes vanish.

For every original principal set \(K\) of cardinality at most \(N\),
\[
\|A_{KK}\|_{\rm op}\le
2\sqrt{N/m}+\delta.
\]
Indeed, the two star restrictions act on disjoint coordinate blocks, each has norm at most its coupling coefficient times the restricted light-vector norm, and the hub diagonal has norm \(\delta\). Hence fixed-size physical three-cores also disappear as \(m\to\infty,\delta\downarrow0\).

The obstruction is quantitative: a fixed relative gap between the third and fourth spectral magnitudes might allow a corrected heavy-Gram implication, but the condition \(\|A_{\rm tail}\|\le s_3(A)\), even with strict inequality, does not provide a universal pivot threshold.

## Uniform density bound for the family

Let all original coordinates be independent with probability densities bounded by one. Write \(H_j=X_{h_j}\) and \(L_j=w_j\cdot X_{\text{light},j}\). An arbitrary original-coordinate affine term splits between the two independent stars. Thus the complete quadratic polynomial is, up to a constant,
\[
Q=Q_1+Q_2,\qquad
Q_1=4H_1L_1+b_1\cdot X_{\text{light},1}+F_1(H_1),
\quad
Q_2=2H_2L_2+b_2\cdot X_{\text{light},2}+F_2(H_2),
\]
where \(F_1,F_2\) may be arbitrary real measurable hub self functions; in the quadratic-affine problem \(F_2(h)=\delta h^2+\beta_2h\).

We use a uniform \(L^2\) lemma. Let \(H\) have density at most one, \(X\) have independent cap-one coordinates, \(|w|=1\), \(c\ne0\), and
\[
Z=F(H)+cH(w\cdot X)+b\cdot X.
\]
Conditional on \(H=h\), the light term is the linear form \((ch\,w+b)\cdot X\), with density cap at most
\[
{\sqrt2\over\|ch\,w+b\|}
\le{\sqrt2\over |c|\,|h-h_0|},
\qquad h_0=-{w\cdot b\over c}, \tag{4}
\]
by the one-dimensional bounded-density projection theorem. The conditional density is merely translated by \(F(h)\). If \(H'\) is an independent copy, the overlap integral of the two conditional probability densities is at most the smaller of their two supremum bounds. Therefore
\[
\|p_Z\|_2^2
\le{\sqrt2\over|c|}
 \mathbb E{1\over\max(|H-h_0|,|H'-h_0|)}. \tag{5}
\]
Since \(\mathbb P(|H-h_0|\le r)\le\min(1,2r)\), layer cake gives
\[
\mathbb E{1\over\max(|H-h_0|,|H'-h_0|)}
\le\int_0^\infty\min(1,2/t)^2\,dt=4.
\]
Thus
\[
\|p_Z\|_2^2\le {4\sqrt2\over|c|}. \tag{6}
\]
This holds without moment or support assumptions, and uniformly in \(b,F\). The exceptional \(h=h_0\) has probability zero; the result follows by Tonelli or truncation of (4).

Apply (6) with \(c=4\) to \(Q_1\), and \(c=2\) to \(Q_2\). Independence and Cauchy–Schwarz for convolution imply
\[
\boxed{\quad
\|p_Q\|_\infty\le
\|p_{Q_1}\|_2\|p_{Q_2}\|_2
\le\sqrt{\,\sqrt2\cdot2\sqrt2\,}=2.
\quad} \tag{7}
\]
The matrix family refutes the indicated *structural* heavy-Gram extension, not the density conjecture.
