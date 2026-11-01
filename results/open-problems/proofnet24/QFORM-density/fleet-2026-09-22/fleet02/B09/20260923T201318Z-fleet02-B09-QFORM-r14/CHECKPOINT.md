SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B09, 2026-09-23T20:13:18Z.
attacking: unify the one-index-overlap kernel-curvature and kernel-shear branches by an integrated quadratic-fiber L4 estimate that spends the full physical invariant ||w|| ||P w|| before any reciprocal minor selection.

# Early substantive checkpoint

Let L,R be disjoint original-coordinate sets with |L|=3, |R|=2. Put P=A[L,L], C=A[L,R], assume rank(C)=2, write the columns of C as c1,c2, w=c1 x c2, Delta=||w||>0, n=w/Delta, and a=P n. I claim the exact-shear condition n^T P n=0 in fleet03/B09 r41 is unnecessary whenever a!=0.

Choose an orthonormal 3x2 frame E spanning n^perp, C0=E^T C, and r=C^T y. Then |det C0|=Delta and the transformed left density

g(x,r)=Delta^(-1) F_Y(n x+E C0^(-T)r)

has cap Delta^(-1), mass one, and r-marginal m(r)<=2/Delta. The x-dependent phase, including an arbitrary affine term beta x, is

q_r(x)=d x^2+xi(r)x,  d=n^T P n,
xi(r)=2 p^T C0^(-T)r+beta,
p=(I-nn^T)Pn.

Its derivative satisfies the source-coordinate identity

q_r'(x)=2d x+xi(r)=2(Pn)^T Y+beta=2 a^T Y+beta.

For h(x)=g(x,r), let F_r(t)=int h(x)e^{it q_r(x)}dx. Since q_r has at most two inverse branches, coarea plus (u+v)^(4/3)<=2^(1/3)(u^(4/3)+v^(4/3)) and Hausdorff--Young give

||F_r||_4^2 <= (4 pi)^(1/2) I(r)^(3/2),
I(r)=int h(x)^(4/3)|q_r'(x)|^(-1/3)dx.

Using h<=Delta^(-1), Jensen on the normalized x-fiber, and m(r)<=2/Delta,

int I(r)^(3/2)dr
 <= sqrt(2) Delta^(-1) E |2a^T Y+beta|^(-1/2).

The scalar on the right is a genuine original-product linear projection. The one-dimensional projection density cap sqrt(2), followed by scaling by 2||a||, gives density cap 1/(sqrt(2)||a||). Hence the elementary cap-to-half-potential bound E|T|^(-1/2)<=4 sqrt(||p_T||_infinity) yields

E |2a^T Y+beta|^(-1/2) <=4*2^(-1/4)||a||^(-1/2).

Thus, for A0(t)^2=int |F_r(t)|^2dr,

||A0||_4 <=2^(13/8) pi^(1/4) Delta^(-1/2)||a||^(-1/4).

The right physical pair has arbitrary same-side quadratic phase but L2 norm at most one. Two-dimensional bilinear Plancherel therefore gives

|phi_Q(t)|<=pi |t|^(-1) A0(t).

Splitting at T and applying Holder on |t|>T,

int |phi_Q(t)|dt <=2T+pi*6^(3/4)T^(-1/4)||A0||_4.

Optimizing and applying Fourier inversion gives

||p_Q||_infinity
 <= [5*6^(3/5)/2^(11/10)] Delta^(-2/5)||a||^(-1/5)
 = 6.834830666196632 (||w|| ||P w||)^(-1/5).

This simultaneously covers d!=0 (kernel curvature plus shear) and d=0,p!=0 (exact shear). No pointwise oscillatory decay, probability squaring, post-rotation independence, moment assumption, or small-coefficient deletion is used. The full proof, target-valid interpolation example, required pinned e5f mixed-hub application, and exact remaining aggregate V1 gap follow in REPORT.md.
