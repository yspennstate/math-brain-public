SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B09, 2026-09-23T02:43:31Z.
attacking: mixed-hub smoothing on a source-coordinate star with dense same-side couplings; seek a quantitative star-vs-curvature routing certificate and direct linear small-ball bound without square-root decoupling.

# Early mathematical checkpoint: two zero-core source hubs absorb arbitrary complement curvature

Programme: QFORM-DENSITY-3EIG-20260922. Full conjecture remains OPEN.

Let h,s be two ORIGINAL coordinates and K their complement. Assume the physical two-hub core is exactly zero:

A_hh=A_ss=A_hs=0.

Write u=A[K,h], v=A[K,s] and

Delta=||u||_2^2 ||v||_2^2-<u,v>^2.

If Delta>0, then for arbitrary A_KK and arbitrary affine terms,

||p_Q||_infinity <= 2 sqrt(2) Delta^(-1/4),

hence P{Q in L} <= 2 sqrt(2) Delta^(-1/4)|L| for every interval L. No restriction at all is placed on the quadratic curvature in K.

Proof skeleton. Absorb affine hub coefficients into constants and write

Q=2 X_h U+2 X_s V+H(X_K),
U=<u,X_K>+alpha, V=<v,X_K>+beta,

where H is an arbitrary quadratic-affine function of X_K. Since u,v are linearly independent, the two-dimensional linear image (U,V) has density cap

M <= 2/sqrt(Delta)

by the sharp two-dimensional marginal bound for an orthogonal projection of a cap-one product source, followed by the determinant change of variables. Conditional on X_K, the two source coordinates X_h,X_s remain independent. The conditional convolution therefore has density supremum

<= min{1/(2|U|),1/(2|V|)}=1/[2 max(|U|,|V|)]

outside a null set. If R=max(|U|,|V|), then the joint-density cap gives

P(R<=r)<=min(1,4Mr^2),

so layer cake yields

E R^(-1) <= integral_0^infinity min(1,4M/t^2)dt=4 sqrt(M).

Averaging the conditional density gives

||p_Q||_infinity <=2 sqrt(M)<=2sqrt(2)Delta^(-1/4).

This is direct conditional linear anti-concentration; no resampling/probability squaring and no square-root small-ball exponent loss occurs. The argument retains H exactly, so dense same-side curvature is not conditioned into a spectral-density supremum.

Target-valid diffuse test. On a size-m Walsh leaf bank choose orthonormal flat c,d,w and set

Q_m=2 X_h<c,Y>+2 X_s<d,Y>+<w,Y>^2.

The compressed spectrum is {1,-1,1,-1,1}, every star coefficient is O(m^-1/2), the same-side square is dense with O(m^-1) entries, Delta=1, and the theorem gives ||p_Qm||_infinity<=2sqrt(2), uniformly in m and in every admissible product law.

Related completed result. Fleet01/B09's current two-hub physical-star theorem gives 4 W^(-1/4) when the remaining leaf self-block is diagonal and the mixed rows have leverage <=1/2. The present endpoint instead assumes the exact zero two-hub core but removes both of those leaf restrictions: A_KK is arbitrary and there is no row-leverage hypothesis.

Required e5f source application queued for the final report: Theorem H applied to 2 X_h<c,Y>+<v1,Y>^2+<v2,Y>^2 with a flat orthonormal three-frame gives |phi(t)|<=8 pi^2 |t|^-2 and hence ||p||_infinity<=4sqrt(2), a target-valid dense same-side rank-two star family.
