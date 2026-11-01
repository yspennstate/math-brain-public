# QFORM-AFFINE-CURVED-TWO-STAR-L2-v1

Supporting theorem only; four eigenvalues remain open.

Let U have density at most 1. Let V have independent coordinates with densities at most 1, independent of U. Let w be nonzero, d arbitrary, and h any measurable real function. For
Z = h(U) + (2 U w + d) dot V,
the law of Z has an L2 density with norm at most 2 e^(1/4) / sqrt(||w||).

Proof: condition on U=u. Except at at most one u, c(u)=2uw+d is nonzero. The product-projection bound gives the conditional density of c(u) dot V supremum at most sqrt(e)/||c(u)||, hence L2 norm at most e^(1/4)||c(u)||^(-1/2). Minkowski gives the integral of this bound against f_U. Writing d=alpha w+d_perp with d_perp orthogonal to w yields ||2uw+d|| >= ||w|| |2u+alpha|. The rearrangement bound for a probability density f<=1 gives integral f(u)|2u+alpha|^(-1/2) du <= 2. This proves the claim.

For two independent systems Z_1,Z_2 of this form,
||p_(Z_1+Z_2)||_infinity <= 4 sqrt(e) / sqrt(||w_1|| ||w_2||),
and the convolution density is continuous.

Therefore the exact two-star carrier in Remark 8.2, with both star norms equal to 1, keeps the same 4 sqrt(e) bound after arbitrary affine terms on all physical coordinates and arbitrary hub self-quadratic curvature. The remaining four-eigenvalue obstruction is the structural reduction from a general no-pivot matrix to such a product-preserving hub/star receiver.
