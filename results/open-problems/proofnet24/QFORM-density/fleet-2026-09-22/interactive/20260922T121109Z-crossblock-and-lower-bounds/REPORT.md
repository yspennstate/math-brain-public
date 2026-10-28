# Quadratic-form density: cross-block smoothing and lower bounds

Programme: QFORM-DENSITY-3EIG-20260922; owner control revision 2026-09-22.5.
Interactive research checkpoint: 20260922T121109Z. This is not a scheduled-worker login.

**Scope:** complete analytic proofs are supplied for the statements below. The full arbitrary-dimension, arbitrary-matrix universal upper bound is NOT PROVED here. No independent end-to-end review or publication-priority claim is asserted. Repository transport is not native brain ingestion; WITHOUT_VERIFIED_BRAIN.

The target assumes independent real X_i with probability densities 0<=f_i<=1 and a symmetric A with at least three eigenvalues of modulus at least 1. All statements below retain arbitrary measurable input densities and require no moments. Additional structural hypotheses are stated explicitly.

## 1. A cross-block theorem without the symmetrization exponent loss

### Theorem QFORM-CROSSBLOCK-RANK-r-FOURIER-v1

Partition the original coordinates into disjoint sets I,J. Suppose the cross block B=A[I,J] has rank r>2 and nonzero singular values s_1,...,s_r. Put Delta=product_j s_j. Then Q=X^TAX, also with arbitrary added linear and constant terms, has a bounded continuous density and

\[
\|p_Q\|_\infty\le {2r\over r-2}\,\Delta^{-1/r}.
\]

In particular, **rank exactly three**, with s_3>=kappa, gives density at most 6/kappa. This is not a bound solely in terms of the top three singular values of a higher-rank cross block: all its nonzero singular values occur in Delta.

#### Published input

Livshyts, Paouris and Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949v2, prove that an r-dimensional orthogonal projection of a product probability density whose one-dimensional factors are at most 1 has density at most 2^(r/2). This is the only non-elementary distributional input used in this section. Plancherel and Fourier inversion use the convention hat h(xi)=integral exp(i xi.z)h(z) dz.

#### Proof

Take a thin singular-value decomposition B=P S R^T, where P and R have orthonormal columns and S=diag(s_1,...,s_r). Define Y=P^T X_I and Z=R^T X_J. These two vectors are independent because I and J are disjoint original-coordinate blocks; their individual coordinates need not be independent. Their densities rho_I,rho_J satisfy

\[
\|\rho_I\|_\infty,\|\rho_J\|_\infty\le 2^{r/2},\qquad
\int\rho_I=\int\rho_J=1.
\]

Write Q=q_I(X_I)+q_J(X_J)+2Y^TSZ+c, absorbing arbitrary linear terms into q_I,q_J. For each real t define complex pushforward measures

\[
\nu_{I,t}(E)=\mathbb E[1_{\{Y\in E\}}e^{itq_I(X_I)}],
\quad
\nu_{J,t}(E)=\mathbb E[1_{\{Z\in E\}}e^{itq_J(X_J)}].
\]

Their total variations are dominated by the laws of Y,Z. Thus they have densities F_t,G_t satisfying |F_t|<=rho_I and |G_t|<=rho_J almost everywhere. In particular,

\[
\|F_t\|_2,\|G_t\|_2\le 2^{r/4}.
\]

Independence of the two original blocks gives the exact identity

\[
|\phi_Q(t)|
=\left|\int F_t(y)\widehat G_t(2tSy)\,dy\right|.
\]

The irrelevant scalar phase exp(itc) has been removed. Cauchy-Schwarz, the invertible change of variables xi=2tSy, and Plancherel imply, for t!=0,

\[
\begin{aligned}
|\phi_Q(t)|
&\le \|F_t\|_2(2|t|)^{-r/2}\Delta^{-1/2}\|\widehat G_t\|_2\\
&=\pi^{r/2}|t|^{-r/2}\Delta^{-1/2}\|F_t\|_2\|G_t\|_2\\
&\le(2\pi)^{r/2}|t|^{-r/2}\Delta^{-1/2}.
\end{aligned}
\]

This estimates phi itself, not |phi|^2. No independence after an eigenvector rotation has been assumed, and all within-block quadratic phases are retained in F_t,G_t.

Let D=(2pi)^(r/2)Delta^(-1/2). Since also |phi_Q|<=1,

\[
\int_{\mathbb R}|\phi_Q(t)|dt
\le {2r\over r-2}D^{2/r}.
\]

Indeed, split each half-line at t_0=D^(2/r), and integrate 1 below t_0 and D t^(-r/2) above it. Fourier inversion now gives

\[
\|p_Q\|_\infty\le{1\over2\pi}{2r\over r-2}D^{2/r}
={2r\over r-2}\Delta^{-1/r}.
\]

The integrable characteristic function gives a continuous density vanishing at infinity. QED.

**Compatibility with the new B09 correction:** a nonsingular 2x2 cross block alone does not force bounded density. At r=2 this proof gives only t^(-1), which is not integrable. It therefore does not contradict QFORM-CROSSMINOR-ALONE-FALSE or its rank-two saddle example. The B09 replacement with a zero pivot-side principal block is a different theorem.

## 2. Dimension-free closure of a delocalized rank-three branch

### Theorem QFORM-DIFFUSE-RANK3-C24-v1

Suppose A=U Lambda U^T has rank exactly three, U^TU=I_3, and all three diagonal entries lambda_j of Lambda have modulus at least 1. Let u_i^T be row i of U. If

\[
\max_i\|u_i\|^2\le 1/12,
\]

then for every permitted input law Q has a bounded continuous density and

\[
\boxed{\|p_Q\|_\infty\le24.}
\]

More generally, if an original-coordinate partition I,J satisfies U_I^TU_I>=alpha I_3 and U_J^TU_J>=alpha I_3, then

\[
\|p_Q\|_\infty\le {6\over\alpha|\lambda_1\lambda_2\lambda_3|^{1/3}}.
\]

#### Proof of the partition criterion

Put Sigma_I=U_I^TU_I and Sigma_J=U_J^TU_J. The cross block is U_I Lambda U_J^T. Factoring U_I=P Sigma_I^(1/2) and U_J=R Sigma_J^(1/2) with P,R isometries shows that its three nonzero singular values are those of Sigma_I^(1/2) Lambda Sigma_J^(1/2). Their product is

\[
\Delta=|\det\Lambda|\sqrt{\det\Sigma_I\det\Sigma_J}
\ge |\det\Lambda|\alpha^3.
\]

The rank-three case of Theorem 1 yields 6 Delta^(-1/3), proving the criterion.

#### Proof that the leverage condition produces a partition

Choose independent auxiliary Bernoulli(1/2) variables epsilon_i and let

\[
D_0=\sum_i(\epsilon_i-1/2)u_i u_i^T.
\]

These auxiliary variables are only a proof of existence of a deterministic partition; they impose no new assumptions on X. Orthogonality of centered independent summands gives

\[
\mathbb E\|D_0\|_F^2
={1\over4}\sum_i\|u_i\|^4
\le {1\over4}\left(\max_i\|u_i\|^2\right)\sum_i\|u_i\|^2
\le {1\over16}.
\]

Here sum_i ||u_i||^2=3. Some realization therefore has ||D_0||op<=||D_0||F<=1/4. For I={i:epsilon_i=1},

\[
\Sigma_I=I_3/2+D_0\ge I_3/4,
\qquad
\Sigma_J=I_3/2-D_0\ge I_3/4.
\]

Use alpha=1/4 in the partition criterion. QED.

This directly addresses a delocalized branch rather than repeating a coordinate-diagonal proof. It includes flat Hadamard three-frames once n>=36 (and hence their Sylvester instances n>=64). It does NOT cover every rank-three frame: a concentrated or mixed-leverage frame may fail this partition criterion. Nor may arbitrary additional eigenvalues be discarded; the theorem assumes rank exactly three. The more general cross-block theorem does allow arbitrary within-block additions while preserving the stipulated cross block.

## 3. A finite six-variable witness disproves C=pi

### Proposition QFORM-SIX-UNIFORMS-2PI-MINUS-7OVER3-v1

Let X_1,...,X_6 be iid Uniform[-1/2,1/2] and

\[
Q={(X_1+X_2)^2\over2}+{(X_3+X_4)^2\over2}-{(X_5+X_6)^2\over2}.
\]

Then A=diag(J_2/2,J_2/2,-J_2/2) has eigenvalues 1,1,-1,0,0,0, and its continuous output density satisfies

\[
\boxed{p_Q(0)=2\pi-7/3>\pi.}
\]

#### Proof

Each independent block average Y=(U+V)/sqrt(2) has density h(y)=sqrt(2)-2|y| for |y|<1/sqrt(2). Its square has density

\[
k(s)={\sqrt2\over\sqrt s}-2,\qquad0<s<1/2.
\]

For 0<s<1/2 the two-square convolution is

\[
(k*k)(s)=2\pi-8\sqrt{2s}+4s.
\]

This follows by expanding the integrand on 0<u<s and using the beta integral integral_0^s du/sqrt(u(s-u))=pi. Consequently

\[
p_Q(0)=\int_0^{1/2}(2\pi-8\sqrt{2s}+4s)
\left({\sqrt2\over\sqrt s}-2\right)ds=2\pi-7/3.
\]

To justify an essential-supremum lower bound rather than just a value of a chosen representative: k*k is bounded by 2pi, because k(s)<=sqrt(2)/sqrt(s). Convolution with the reflected L1 density k is uniformly continuous, by translation continuity in L1. Thus p_Q has a continuous representative and its essential supremum is at least p_Q(0). QED.

The value is approximately 3.949851973846253. This disproves a proposed universal constant pi, not the existence of a larger universal constant. It does not invalidate the pi theorem for forms diagonal in the original independent variables.

## 4. Every universal constant must be at least 3sqrt(2)

### Proposition QFORM-BLOCK-CLT-LOWER-3SQRT2-v1

The supremum of the target density norms is at least 3sqrt(2), approximately 4.242640687119285.

#### Proof

Take n=3m iid uniform variables on [-1/2,1/2], split them into three blocks, and set

\[
S_{j,m}=m^{-1/2}\sum_{i\text{ in block }j}X_i,
\qquad Q_m=S_{1,m}^2+S_{2,m}^2-S_{3,m}^2.
\]

The matrix diag(J_m/m,J_m/m,-J_m/m) has exactly three nonzero eigenvalues 1,1,-1. The three block sums are independent. Their characteristic functions satisfy

\[
\left[{\sin(t/(2\sqrt m))\over t/(2\sqrt m)}\right]^m
\longrightarrow e^{-t^2/24}.
\]

Therefore the block vector converges in law to three independent Gaussians G_j of variance 1/12, and Q_m converges in law to T=G_1^2+G_2^2-G_3^2.

The positive sum G_1^2+G_2^2 has density 6exp(-6u) for u>0. Hence for t>=0,

\[
p_T(t)=6e^{-6t}\mathbb E e^{-6G_3^2}
=3\sqrt2 e^{-6t}.
\]

If a finite C bounds all target density norms, then P(Q_m in [0,h])<=Ch for every h>0. The limiting law has no atoms at the interval endpoints, so weak convergence implies

\[
Ch\ge\Pr(T\in[0,h])={1-e^{-6h}\over\sqrt2}.
\]

Letting h decrease to zero gives C>=3sqrt(2). Equivalently the supremum of the target norms is at least that value, whether or not the supremum is finite. No convergence of density values has been assumed. QED.

## 5. Qualitative boundedness for each fixed A of rank at least three

The following result separates a law-uniform bound for each fixed matrix from the still-missing matrix- and dimension-uniform bound.

### Proposition QFORM-FIXED-MATRIX-BOUNDED-v1

For every fixed real symmetric A of rank at least three, there is a finite C(A) such that ||p_{X^TAX}||infinity<=C(A) for all permitted input laws. It is enough to take C(A)=(2pi+3sqrt(3))/kappa for a nonsingular principal 3x3 block of least singular value kappa; if instead the block obtained below is 4x4, take C(A)=(pi^2+8)/kappa.

#### Existence of a principal block of size three or four

Start with an empty index set S. Whenever |S|<3 and A_SS is nonsingular, form the symmetric Schur complement H. Its rank is rank(A)-|S|>0. If H has a nonzero diagonal entry, append that one index. Otherwise it has a nonzero off-diagonal entry h_ij, and its principal 2x2 block [[0,h_ij],[h_ij,0]] is nonsingular; append those two indices. The block determinant formula preserves nonsingularity of A_SS. The process first reaches size three or four, proving the claim. For S empty the Schur complement simply means A.

#### Three- and four-dimensional interval bounds

For a nonsingular symmetric dxd block B, d=3 or 4, complete the square to absorb all linear terms. Divide B and the output by kappa=min|lambda_j(B)|, so that |B|>=I. Write F(x)=product_i f_i(x_i)<=1. For an interval J of length eta split at |Bx|<=1.

In this near region put z=|B|^(1/2)x. The Jacobian is at most 1, |Bx|^2=z^T|B|z>=|z|^2, and x^TBx=z^T sign(B)z. Thus the contribution is bounded by the volume of a canonical signed quadratic shell inside the unit d-ball.

For d=3 that shell volume is at most 2pi eta: for a definite form the radial volume density is 2pi sqrt(t)<=2pi; for a mixed signature fix the coordinate of the minority sign, apply the planar annulus area pi eta, and integrate over an interval of length 2.

For d=4 the shell volume is at most pi^2 eta. In the definite case the radial density is pi^2 t<=pi^2. In signature (3,1), fix the minority coordinate s: the three-dimensional radial density is at most 2pi sqrt(1-s^2), whose integral over [-1,1] is pi^2. Signature (1,3) is its reflection. In signature (2,2), set a=z_1^2+z_2^2 and b=z_3^2+z_4^2; the volume measure is pi^2 da db on a,b>=0,a+b<=1. The pushforward under a-b has density pi^2(1-|t|)/2 on [-1,1], so it obeys the same bound.

In the far region some original coordinate has |(Bx)_i|>1/sqrt(d). Condition on all other original coordinates. The scalar polynomial has derivative of absolute value greater than 2/sqrt(d), on at most two monotone branches. The preimage of J there has length at most sqrt(d)eta. Its conditional probability is no greater, since f_i<=1. Summing over i gives d sqrt(d)eta.

The complete interval bound is therefore (2pi+3sqrt(3))eta in d=3 and (pi^2+8)eta in d=4. Interval domination implies an essentially bounded density. Restore the output scaling kappa. Finally condition on all original coordinates outside the selected block. All outside couplings become linear and constant terms, already allowed above, and averaging preserves the bound. QED.

The d=3 argument is the completed account02/B15 source result listed below; the 4D shell calculation and principal-pivot extension are supplied here. Continuity for all these fixed-matrix cases is not established by this interval proof.

## 6. What is still missing

Neither local-block conditioning nor the new cross-block theorem covers every matrix in the target with a uniform constant. For example, for A=diag(J_m/m,J_m/m,-J_m/m), every nonsingular principal 3x3 block has least singular value 1/m, so a fixed-coordinate triple estimate loses dimension. The diffuse-frame theorem now treats this family for large m by a different mechanism, but it is not a universal dichotomy theorem.

The remaining task is to cover arbitrary mixed-leverage frames and arbitrary higher-rank matrices, without discarding dependent spectral remainders. In the cross-block estimate it is invalid to replace the product of all nonzero singular values by the product of only three without a new proof. In particular, this report does not supply the requested full arbitrary-n universal upper bound.

## 7. Source pins, computations, and delivery scope

- Fresh owner README: yspennstate/math-research-brain, revision 2026-09-22.5, blob 433b2d57345823967480245b59a7c47d51019c37.
- Completed three-dimensional source: yspennstate/math-open-problems, proofnet24/QFORM-density/fleet-2026-09-22/account02/B15/20260922T110507Z-account02-B15-qform-pivot-r1/REPORT.md, blob 1da4167bbf6b2785659bd50007cab5f04b9c3084, present at archive snapshot 0605c987ff531ccc2fd5554c48df29e65b3eaaa8.
- External theorem actually applied: Livshyts--Paouris--Pivovarov, arXiv:1507.07949v2, orthogonal marginal density bound 2^(r/2). Other researched Gaussian and smooth-input theorems were not used as if they covered arbitrary bounded densities.
- Exact symbolic checks executed: the six-variable matrix eigenvalue multiplicities; mass integral of k; p_Q(0)=2pi-7/3; a 36-coordinate rank-three frame of leverage 1/12 with both partition Gram matrices I_3/2. These calculations support only these identities, not the universal conjecture.
- Reproducible density integral: in SymPy, with s>0, integrate((2*pi-8*sqrt(2*s)+4*s)*(sqrt(2)/sqrt(s)-2),(s,0,Rational(1,2))) returns -7/3+2*pi.
- Checker SHA-256: f4c2e081652d13bcf7c611d3d294f163b76e7125f442ab6f3aaf045ccd41267f. Output SHA-256: f1482261b380cd50b910aa187b6fac0e560d2812d639c25a3bf1fd1a44cfc07c. The analytic proofs, not these finite checks, support the quantified scoped statements.
- Explicit private mathematical write only; no credentials, account identifiers, scheduler IDs, emails, unrelated data, production-population changes, or public release. The content was manually reviewed on this narrow allowlist; a repository-wide scanner was not executed in this interactive runtime.
