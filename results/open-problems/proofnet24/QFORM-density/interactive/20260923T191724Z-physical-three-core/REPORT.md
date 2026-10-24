# Three original-coordinate principal core: an arbitrary-law receiver

Date: 2026-09-23 19:17 UTC. This is a scoped rigorous result for the QFORM density problem, **not a proof of the unrestricted spectral conjecture**. Independently checked by the spectral/PSD analyst.

## Theorem

Let \(X_1,\ldots,X_n\) be independent real random variables with probability densities at most \(1\). Let \(A=A^\top\) be arbitrary, and suppose there is a set \(S\) of **three original coordinates** for which the \(3\times3\) principal matrix \(M=A_{SS}\) has \(s_3(M)\ge\sigma>0\). Then the law of \(X^\top AX\) has a density satisfying
\[
 \|p_{X^\top AX}\|_\infty
 \le \frac{6(6\pi e)^{1/4}}{\sigma}
 <\frac{17}{\sigma}.
\]
All other matrix entries and the remaining coordinates are arbitrary. The same holds with a deterministic affine term added to the form.

Condition on \(X_{S^c}\). The conditional polynomial in the three independent original coordinates \(z=(X_i)_{i\in S}\) is \(q(z)=z^\top Mz+b^\top z+c\), with arbitrary \(b,c\). It is enough to prove the interval estimate uniformly in \(b,c\).

## Exterior coarea, including arbitrary affine shifts

Write \(z_0=-M^{-1}b/2\), set \(y=z-z_0\), and absorb a constant so \(q(z)=y^\top My+c'\). Translation preserves independence and the cap-one density of all three variables. On \(|y|\ge R\), the gradient satisfies \(|\nabla q(y)|=2|My|\ge2\sigma R\). Thus at least one original-coordinate derivative has magnitude \(|\partial_i q|\ge 2\sigma R/\sqrt3\).

For each \(i\), fix the other two coordinates and restrict to \(|\partial_i q|\ge 2\sigma R/\sqrt3\). Since \(\partial_i q\) is affine in \(y_i\), this set has at most two monotone branches of the quadratic \(q\); if \(M_{ii}=0\), the polynomial is affine in \(y_i\) and has at most one branch. For an interval \(I\) of length \(h\), the total Lebesgue measure of the preimage on these branches is at most \(\sqrt3 h/(\sigma R)\). Integrating the independent cap-one \(i\)-th density and the other two probability densities, and summing over \(i=1,2,3\), gives
\[
 \Pr\{q\in I,\ |y|\ge R\}\le \frac{3\sqrt3}{\sigma R}h.
\]
The derivative event alone suffices for the upper bound; there is no conditional product-law assumption after an orthogonal rotation.

## Interior Gaussian volume

The joint density of \(y\) is bounded by \(1\) pointwise. On \(|y|\le R\),
\(\mathbf1_{\{|y|\le R\}}\le e^{1/2}\exp(-|y|^2/(2R^2))\).
For \(G\sim N(0,R^2 I_3)\), diagonalize \(M\) solely to compute the Gaussian integral. Since every \(|\lambda_j(M)|\ge\sigma\),
\[
 |\mathbb E e^{itG^\top MG}|
 =\prod_{j=1}^3(1+4t^2R^4\lambda_j^2)^{-1/4}
 \le(1+4t^2R^4\sigma^2)^{-3/4}.
\]
The elementary integral \(\int_{\mathbb R}(1+u^2)^{-3/4}\,du\le6\) follows by splitting at \(|u|=1\) and bounding the tail by \(|u|^{-3/2}\). Fourier inversion yields \(\|p_{G^\top MG}\|_\infty\le3/(2\pi\sigma R^2)\). Hence
\[
 \Pr\{q\in I,\ |y|\le R\}
 \le e^{1/2}(2\pi)^{3/2}R^3\frac{3h}{2\pi\sigma R^2}
 = \frac{3e^{1/2}\sqrt{2\pi}R}{\sigma}h.
\]
Optimize at \(R=\sqrt{\sqrt3/(e^{1/2}\sqrt{2\pi})}\). The sum is then \(6(6\pi e)^{1/4}h/\sigma<17h/\sigma\). Average over \(X_{S^c}\). Uniform interval bounds imply a density with the claimed essential supremum.


### Consequence for exact rank three in each fixed dimension

If \(\operatorname{rank}A=3\) and \(s_3(A)>0\), write \(A=U\Lambda U^\top\), \(U^\top U=I_3\). Cauchy–Binet gives \(\sum_{|S|=3}\det(U_S)^2=1\), so some original-coordinate triple has \(\det(U_S)^2\ge\binom n3^{-1}\). Every eigenvalue of \(U_S^\top U_S\) is at most \(1\); therefore its smallest eigenvalue is at least its determinant, at least \(\binom n3^{-1}\). The singular-value product inequality now gives
\[
 s_3(A_{SS})=s_3(U_S\Lambda U_S^\top)
 \ge s_3(A)\,s_3(U_S)^2
 \ge s_3(A)/\binom n3.
\]
The theorem proves the dimension-dependent arbitrary-law bound
\[
 \|p_{X^\top AX}\|_\infty
 <\frac{17\binom n3}{s_3(A)}
 \qquad(\operatorname{rank}A=3).
\]
This finite-dimensional bound is not uniform as \(n\to\infty\); the unresolved conjecture requires a dimension-free constant and arbitrary extra eigenvalues.


### Sharper dimension-dependent bound for homogeneous exact rank three

There is a stronger bound that uses the full projected law, still growing with dimension:
\[
 \|p_{X^\top AX}\|_\infty<\frac{12\,n^{3/4}}{s_3(A)}
 \qquad(\operatorname{rank}A=3).
\]
The same proof permits a deterministic affine coefficient \(b\in\operatorname{range}A\); it makes no claim for an affine component in \(\ker A\). This result was independently checked by two analysts.

Indeed, let \(A=U\Lambda U^\top\), \(U^\top U=I_3\), \(\sigma=s_3(A)\), and \(Y=U^\top X\). The projection density theorem for independent cap-one original coordinates gives \(\|p_Y\|_\infty\le2^{3/2}\). An affine \(b\in\operatorname{range}A\) only translates the center \(Y_0\) of the nondegenerate quadratic in \(Y\).

On \(|Y-Y_0|\le R\), use the three-dimensional Gaussian volume computation above with density cap \(2^{3/2}\). Its shell cost is at most
\[
 \frac{12e^{1/2}\sqrt{\pi}\,R}{\sigma}\,h .
\]
On the exterior, \(\|\nabla_X Q\|=2\|U\Lambda(Y-Y_0)\|\ge2\sigma R\). Some ORIGINAL partial derivative has size at least \(2\sigma R/\sqrt n\). The two-branch one-coordinate coarea argument, followed by a union bound over \(n\) original coordinates, gives cost at most \(n^{3/2}h/(\sigma R)\). Optimize \(R=n^{3/4}/\sqrt{12e^{1/2}\sqrt\pi}\). The sum is \(2\sqrt{12e^{1/2}\sqrt\pi}\,n^{3/4}h/\sigma<12n^{3/4}h/\sigma\). No conditional independence is asserted for the projected coordinates; their joint density cap is used only in the bounded interior region.

The polynomial growth in \(n\) means this does **not** settle the dimension-free conjecture even for exact rank three. The exact near-coloop with diffuse leakage remains the principal rank-three obstacle.

## Scope and connection

The theorem pays any sufficiently strong physical principal triple, with arbitrary cross interactions to all remaining variables. It can be combined with the [marginal-free physical three-crossing theorem](https://github.com/yspennstate/math-open-problems/commit/df738b7f0821d9af56dfd992cab10ecc6704e3fb) as a structural case split. The spectral hypothesis \(s_3(A)\ge1\) **does not by itself provide** a uniform \(\sigma\) for a physical principal triple: for example three diffuse disjoint rank-one blocks have each fixed \(3\times3\) physical principal block of size \(O(1/m)\). Their crossing must be treated separately. The low-crossing near-coloop and overlapping-leakage case remains open in the full conjecture.
