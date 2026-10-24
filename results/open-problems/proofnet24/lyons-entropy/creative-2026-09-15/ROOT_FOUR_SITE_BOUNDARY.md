# A full sixteen-dimensional four-site boundary neighborhood

Coordinator constructive theorem, 15 September 2026. This finishes ROOT_FOUR_SITE_BOUNDARY_LEAD.md under its nonzero endpoint-coordinate hypotheses. A four-site strict-Hall argument also removes the nonzero active-minor restriction from the first version of this proof. General Lyons entropy concavity remains open. No historical novelty or formal verification is asserted.

## 1. Statement

Let [z,w,V] be a unitary four-by-four matrix, with V having two columns. Assume every coordinate of z and w is nonzero. Active-plane row minors may vanish. For a strict two-by-two Hermitian contraction M, put

\[
K_0=ww^*+VMV^*,\qquad
K_{\epsilon,\eta}=\epsilon zz^*+(1-\eta)ww^*+VMV^*.
\]

There is a positive delta such that the **full Hermitian entropy Hessian is negative definite** at K_(epsilon,eta) whenever 0<epsilon,eta<delta. No bound on their ratio is imposed. The assertion is uniform when the frame and M range over a compact set satisfying the displayed strict hypotheses. Allowing these frame and active-matrix parameters to vary gives an ambient open subset of the sixteen-dimensional real space of four-site Hermitian contractions, approaching every boundary point covered by the hypotheses.

Thus every affine segment contained in that open set has strictly concave entropy. No convexity of the entire neighborhood is asserted. The theorem covers vanishing added-plane minors, but not zero endpoint coordinates or arbitrary full-rank four-site kernels.

## 2. The boundary has exactly fourteen positive atoms

Write d=det M and d0=det(I-M). The singleton probabilities are d0 |w_i|^2 and the triple probabilities are d |z_j|^2, where j is the omitted coordinate. These are positive. For a pair U, the active-matrix atom formula from ROOT_DIAMOND_ACTIVE_MATRIX gives

\[
p_U=e_U(M-dI)e_U^*,\qquad
 e_{ij}=(w_iV_{j1}-w_jV_{i1},\ w_iV_{j2}-w_jV_{i2}).
\]

The matrix M-dI is positive definite. If e_(ij)=0, the two rows i,j of [w,V] would be proportional because w_i and w_j are nonzero. But their Gram determinant is the principal two-minor of I-zz*, namely 1-|z_i|^2-|z_j|^2, which is positive because both other coordinates of z are nonzero. Thus every pair probability is positive. Only the empty and full atoms vanish.

## 3. Strictness on the active four-dimensional face

ROOT_DIAMOND_ACTIVE_MATRIX proves concavity for the full active Hermitian matrix M, because the bottom projection has rank one. Its exact Hessian is

\[
T(B)=-\mathrm{FI}(B)+2\det(B)\Lambda,
\]

where Lambda is the expected frozen logarithmic diamond gap. Its definite-direction Fisher bound and Lambda>0 give a strictly negative four-dimensional Hessian. We now prove the required strictness under the present hypotheses.

We strengthen the four-site support conclusion from C033. Write beta=V_1 wedge V_2 and h_(jk)=|beta_(jk)|^2. Its rank-one inclusion transport has pair masses h and triple masses |z_i|^2. For a family A of positive-mass pairs, a zero Hall slack implies iota_w beta_A=0 by C033's exact Hall SOS identity. Since iota_w beta=0, also iota_w beta_(A^c)=0.

If w has no zero coordinate, every vertex incident to the nonzero support of an exterior vector satisfying iota_w beta_A=0 has degree at least two: a degree-one contraction equation would have a single nonzero term. Therefore, if both h(A)>0 and h(A^c)>0, the disjoint edge supports of beta_A and beta_(A^c) would each contain a cycle. The complete graph on four vertices has no two edge-disjoint cycles. Indeed each cycle has length at least three; two triangles on four vertices share an edge, and any larger pair of cycles would require at least seven edges. This contradiction proves strict Hall for every nonempty proper family of positive-mass pairs.

All triple masses are positive. There is consequently a transport positive on every inclusion edge from a positive-mass pair: put a sufficiently small common mass on all these finitely many edges first, using the strictly positive Hall slacks and marginal masses, and apply the Hall construction to the residual masses. The full-pair-family equality is preserved by this subtraction. C033's exact marginal identities turn it into a diamond coupling positive for every addition pair {j,k} with h_(jk)>0 and every singleton bottom i outside that pair.

The determinantal log-submodularity inequality, obtained at this boundary by regularization, says

\[
\log\frac{p_{ij}p_{ik}}{p_i p_{ijk}}\ge0.
\]

If Lambda were zero, every supported gap would vanish. Choose two positive h-edges sharing a vertex, say {j,k} and {k,l}, and let i be the fourth site. Such edges exist: a decomposable nonzero two-form supported on one pair would make V a coordinate plane, contradicting the nonzero coordinates of w; if two support edges were disjoint, the four-coordinate Pluecker relation forces an additional edge meeting them. Thus a support with at least two edges always has a pair meeting at a vertex.

Condition on site i being occupied. The resulting three-site DPP has positive empty probability p_i/K_(ii), so its conditional kernel F has I-F>0 and a finite positive-semidefinite odds matrix L=F(I-F)^(-1). Equality of the two selected logarithmic gaps gives

\[
\det L_{jk}=L_{jj}L_{kk},\qquad
\det L_{kl}=L_{kk}L_{ll}.
\]

Hermiticity therefore forces L_(jk)=L_(kl)=0. Its diagonal entry L_(kk)=p_(ik)/p_i is positive, and its remaining two-by-two determinant is det L_(jl)=p_(ijl)/p_i>0. Hence det L=L_(kk) det L_(jl)>0. But the conditional full atom is p_(1234)/K_(ii)=0, forcing det L=0. This contradiction proves Lambda>0, including when some active-plane minors vanish.

In particular, writing C1=8-6 log 2>0, the active theorem supplies the explicit pointwise face gap

\[
T(B)\le-\gamma\|B\|_F^2,\qquad
\gamma=\min\{\Lambda,2C1/(C1+2\Lambda)\}>0.
\]

All fourteen positive atom probabilities and gamma are bounded below uniformly on any compact family satisfying the theorem's hypotheses.

## 4. Exact jets of both singular atoms

Use the spectral splitting z,w,V, and write an arbitrary Hermitian direction as

\[
A=\begin{pmatrix}a&\overline c&x^*\\c&b&y^*\\x&y&B\end{pmatrix}.
\]

Let N=I-M, t=tr(M^(-1)B), and t0=tr(N^(-1)B). The full atom q=det K and empty atom q0=det(I-K) have the following exact directional jets:

\[
q=\epsilon(1-\eta)d,\quad
q'=d[(1-\eta)a+\epsilon b+\epsilon(1-\eta)t],
\]
\[
q''=2d[ab+(1-\eta)at+\epsilon bt-|c|^2
 -(1-\eta)x^*M^{-1}x-\epsilon y^*M^{-1}y]
 +2\epsilon(1-\eta)\det B,
\]
\[
q0=\eta(1-\epsilon)d0,\quad
q0'=-d0[\eta a+(1-\epsilon)b+\eta(1-\epsilon)t0],
\]
\[
q0''=2d0[ab+\eta at0+(1-\epsilon)bt0-|c|^2
 -\eta x^*N^{-1}x-(1-\epsilon)y^*N^{-1}y]
 +2\eta(1-\epsilon)\det B.
\]

These follow by selecting two perturbed rows/columns in the block determinant. They retain the interaction between the two endpoint eigenspaces, as well as both active-plane mixing blocks. Every other atom and its first two derivatives are smooth at the boundary, with a positive probability denominator.

The normalized entropy identity is

\[
H''=-\sum_S(p'_S)^2/p_S-\sum_Sp''_S\log p_S.
\]

It is essential to retain both singular atoms in this formula.

## 5. Independent-scale normal form and absorption

Put Le=log(1/epsilon), Lh=log(1/eta), and rescale the direction by

\[
a=\sqrt\epsilon\,\alpha,\quad b=\sqrt\eta\,\beta,\quad
c=\chi/\sqrt{Le+Lh},\quad
x=\xi/\sqrt{Le},\quad y=\upsilon/\sqrt{Lh},
\]

leaving B unscaled. Substitution of the exact jets gives, in quadratic-form operator norm,

\[
\begin{aligned}
H''[A,A]={}&-d\alpha^2-d0\beta^2
 -2d\xi^*M^{-1}\xi-2d0\upsilon^*N^{-1}\upsilon\\
&-2\frac{dLe+d0Lh}{Le+Lh}|\chi|^2+T(B)+o(1).
\end{aligned}
\]

The error tends to zero uniformly as epsilon and eta tend independently to zero, on the compact families above. To justify independence of the scales explicitly, the regular fourteen-atom quadratic form differs from its boundary value by O(epsilon+eta). Its bounded mixed terms with the rescaled transverse variables vanish at least as the largest of sqrt(epsilon), sqrt(eta), Le^(-1/2), Lh^(-1/2). In the two singular jets, normal-active mixed terms have sizes at most a constant times sqrt(epsilon)Le or sqrt(eta)Lh. The endpoint-normal mixed terms obey

\[
\sqrt{\epsilon\eta}(Le+Lh)
\le\sqrt\epsilon Le+\sqrt\eta Lh.
\]

The other mixed terms have additional powers of epsilon or eta. Active-block terms omitted from T(B) are bounded by a constant times epsilon(1+Le)+eta(1+Lh). The cross mixing coefficients have only additional factors epsilon Le/Lh or eta Lh/Le, which tend to zero because both logarithms are eventually at least one. Thus the total operator error is bounded by a compact-family constant times

\[
\sqrt\epsilon(1+Le)+\sqrt\eta(1+Lh)+Le^{-1/2}+Lh^{-1/2},
\]

which tends to zero with no ratio restriction.

The displayed principal quadratic form has a uniform strictly negative gap: d,d0 and the two active inverse matrices are uniformly positive, the coefficient (dLe+d0Lh)/(Le+Lh) is at least min(d,d0), and T has the gap gamma. Choosing delta so that the operator error is less than half this gap proves negative definiteness. The rescaling is invertible for each positive epsilon,eta, so it controls all sixteen real Hermitian directions: two normal, two endpoint mixing, eight endpoint-to-active mixing, and four active directions.

The spectral eigenspaces near 0 and 1 are simple and separated from the two surviving interior eigenvalues. Their projections vary continuously. The strict endpoint-coordinate and active-contraction restrictions are open. Taking their union with sufficiently small positive endpoint gaps therefore gives the asserted ambient open neighborhood. This argument proves neither a global convex region nor the remaining four-site interior.

## 6. Reproduction

ROOT_FOUR_SITE_BOUNDARY_check.py checks both singular-atom jet formulas against direct determinant differentiation, then forms all sixteen rescaled Hessian modes at twelve points with equal and widely separated endpoint scales. The maximum jet discrepancy was 7.11e-15; the chosen active face had maximum Hessian eigenvalue -1.79836. All twelve full scaled Hessians were negative. ROOT_FOUR_SITE_BOUNDARY_results.json records the values and convergence errors. These floating-point diagnostics support the formula implementation; the uniform neighborhood and independent-scale conclusions follow from the analytic argument above.


## 7. A zero-minor example covered by the extended theorem

Take w=(1,1,1,1)/2, z=(1,1,-1,-1)/2, V_1=(1,-1,0,0)/sqrt(2), V_2=(0,0,1,-1)/sqrt(2), and M=I_2/2. The active-plane minors on pairs 12 and 34 vanish; the other four squared minors equal 1/4. All endpoint coordinate probabilities equal 1/4.

Every singleton and triple atom equals 1/16. Pair atoms 12 and 34 equal 1/8, and the other four pairs equal 1/16. Giving mass 1/8 to each of the eight inclusions from a positive active pair to a containing triple gives the exact diamond transport. Every supported logarithmic diamond gap equals log 2, so Lambda=log 2>0. The theorem therefore gives a full interior Hessian neighborhood despite these two exactly vanishing active minors, including arbitrarily unequal small endpoint gaps. These fractions verify normalization and every stated marginal directly.
