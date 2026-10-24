# Exact rank-three quadratic density with arbitrary affine terms

**Status:** Rigorous dimension-dependent theorem. This does **not** prove a dimension-uniform bound or the unrestricted rank/signature conjecture.

## Theorem

Let (n\ge3), let (X_1,\ldots,X_n) be independent real random variables whose densities are bounded by one, and let (A\in\mathbb R^{n\times n}) be symmetric of **exact rank three**, with its three nonzero eigenvalues of modulus at least (\sigma>0). For every (b\in\mathbb R^n) and (c\in\mathbb R), the law of
\[
 Q=X^TAX+b^TX+c
\]
has a density satisfying
\[
 \|p_Q\|_\infty
 < \frac{51(n-2)}{\sigma}.
\]
The result permits all signatures and affine coefficients in the null space of (A). It is dimension dependent; it does not settle the full conjecture.

## A uniform physical three-variable lemma

For any independent cap-one (Z=(Z_1,Z_2,Z_3)), any symmetric (3\times3) matrix (M) with (s_{\min}(M)\ge\tau>0), and any affine coefficients,
\[
 \|p_{Z^TMZ+\ell^TZ+c}\|_\infty
 \le \frac{2\sqrt{(3e^{1/2}\sqrt{2\pi})(3\sqrt3)}}{\tau}
 <\frac{17}{\tau}. \tag{1}
\]

Here is a self-contained interval proof. Write (z_0=-M^{-1}\ell/2), fix an output interval (J) of length (h), and split according to (\|Z-z_0\|\le R). On this ball, the product density is bounded by one and
\[
 \mathbf1_{\{\|z-z_0\|\le R\}}
 \le e^{1/2}\exp[-\|z-z_0\|^2/(2R^2)].
\]
A Gaussian with mean (z_0) and covariance (R^2 I_3), pushed forward by the quadratic, has characteristic-function modulus at most
((1+4\tau^2R^4t^2)^{-3/4}).
Fourier inversion and the elementary bound
(\int_{\mathbb R}(1+u^2)^{-3/4}du\le6)
give a density cap (3/(2\pi\tau R^2)) for this Gaussian pushforward. The ball contribution is therefore at most
\[
 \frac{3e^{1/2}\sqrt{2\pi}Rh}{\tau}. \tag{2}
\]
On the complement, (\|\nabla q(z)\|=2\|M(z-z_0)\|\ge2\tau R), so at least one of the three **original coordinate** derivatives has magnitude at least (2\tau R/\sqrt3). For each physical coordinate, condition on the other two. Its derivative is affine in that coordinate; on the set where its magnitude exceeds this threshold it has at most two monotone branches. On each branch the preimage of (J) has length at most (\sqrt3 h/(2\tau R)). The three-coordinate union and the cap-one densities give
\[
 \mathbb P(q(Z)\in J,\|Z-z_0\|>R)
 \le\frac{3\sqrt3h}{\tau R}. \tag{3}
\]
Optimize (2)+(3) over (R>0): (R=\sqrt{\sqrt3/(e^{1/2}\sqrt{2\pi})}\), leading to (1). All the estimates concern intervals and therefore apply without regularity assumptions on the densities.

## Volume sampling identifies an original-coordinate triple

Spectrally decompose (A=U\Lambda U^T), where (U\in\mathbb R^{n\times3}) has orthonormal columns and (\Lambda\) is invertible with (\|\Lambda^{-1}\|\le1/\sigma). For a three-element row set (I), put (G_I=U_I^TU_I) and (w_I=\det G_I\). Cauchy–Binet gives
\[
 \sum_{|I|=3}w_I=\det(U^TU)=1. \tag{4}
\]
For nonsingular (G_I), (w_I\operatorname{tr}(G_I^{-1})=\operatorname{tr}(\operatorname{adj}G_I)). The latter identity remains a nonnegative polynomial for singular (G_I). Expanding each principal two-by-two minor of (G_I) into row minors of (U_I), and observing that every row pair lies in precisely (n-2) triples, gives
\[
 \sum_{|I|=3}\operatorname{tr}(\operatorname{adj}G_I)
 =(n-2)\sum_{1\le a<b\le3}\sum_{|J|=2}\det(U_{J,\{a,b\}})^2
 =3(n-2). \tag{5}
\]
The final equality is Cauchy–Binet applied to each orthonormal pair of columns of (U). Equations (4)–(5) show that some nonsingular (I) satisfies
\[
 \operatorname{tr}(G_I^{-1})\le3(n-2),\qquad
 s_{\min}(U_I)^2=\lambda_{\min}(G_I)\ge[3(n-2)]^{-1}. \tag{6}
\]
Since (A_{II}=U_I\Lambda U_I^T), it is invertible even if the three eigenvalues of (A) have mixed signs. Its inverse factorization gives
\[
 s_{\min}(A_{II})
 \ge \sigma s_{\min}(U_I)^2
 \ge\frac{\sigma}{3(n-2)}. \tag{7}
\]
Finally condition on all independent coordinates (X_{I^c}). The conditional polynomial in the **three physical variables** (X_I) has quadratic matrix (A_{II}), arbitrary affine terms depending on the conditioning, and cap-one independent coordinate laws. Apply (1) and (7), then average the conditional interval estimates, obtaining the theorem.

## Scope and related routes

The proof relies on exact rank three at (7). With additional nonzero spectral directions, (A_{II}\) includes their indefinite contribution, so the same argument cannot infer invertibility or a lower singular-value bound from the top-three row frame. For exact rank three with affine term in the range of (A), a separate spectral-projection localization yields a better dimension-dependent estimate of order (n^{3/4}/\sigma); the affine null component prevents that argument's unconditional projection-density bound from being applied after conditioning. The physical-triple theorem above handles every affine term at the stated order (n/\sigma).
