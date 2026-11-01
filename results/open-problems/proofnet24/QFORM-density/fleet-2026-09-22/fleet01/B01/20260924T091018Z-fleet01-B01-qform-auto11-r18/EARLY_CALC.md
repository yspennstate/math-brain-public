SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B01, 2026-09-24T09:10:18Z.
attacking: a decoupled mixed-frequency replacement for the false scalar pointwise quadratic-phase decay, with the conditional-density blowup absorbed before inversion.

# Early calculation: an unconditional sum-difference mixed-norm bound

Let X,X' be iid with probability density f satisfying 0<=f<=1. Put U=X-X' and V=X+X'. Their joint density is

h(u,v) = (1/2) f((v+u)/2) f((v-u)/2).

Define the UNNORMALIZED conditional Fourier kernel

Psi_f(u,s) := int_R exp(i s v) h(u,v) dv.

This is preferable to the normalized conditional characteristic function because no reciprocal of the difference density is introduced.

Let r(u)=int h(u,v)dv=int f(x)f(x-u)dx. Then 0<=r<=1 and int r=1. For r(u)>0, k_u(v)=h(u,v)/r(u) is the density of V conditioned on U=u. For p>=2 and q=p/(p-1),

int k_u(v)^q dv
 = 2^(1-q) r(u)^(-q) int [f(x)f(x-u)]^q dx
 <= 2^(1-q) r(u)^(1-q),

because 0<=f<=1 implies f^q<=f. With the Fourier convention hat g(s)=int exp(i s v)g(v)dv, Hausdorff-Young in the form ||hat g||_p <= (2*pi)^(1/p)||g||_q gives

||hat k_u||_p^p <= pi/r(u).

Since Psi_f(u,s)=r(u) hat k_u(s),

int_R |Psi_f(u,s)|^p ds <= pi r(u)^(p-1).

Integrating u and using r<=1, p>=2,

BOX: int_R int_R |Psi_f(u,s)|^p ds du <= pi.          (E1)

This is uniform over every cap-one f and every p>=2. It remains valid when r(u)=0 by defining k_u arbitrarily there.

Scaled version: for every measurable a(u) with a(u)!=0 a.e.,

int_R int_R |a(u)| |Psi_f(u,t a(u))|^p dt du <= pi.   (E2)

Indeed s=t a(u) for each fixed u.

Exact quadratic decoupling identity: for independent coordinates X_j with cap-one densities, an independent copy X', U=X-X', V=X+X', and symmetric A,

|phi_Q(t)|^2
 = int_{R^n} product_j Psi_{f_j}(u_j, t(Au)_j) du.      (E3)

The equality follows from Q(X)-Q(X')=U^T A V and the fact that, before conditioning, the pairs (U_j,V_j) are independent across j. Hence

|phi_Q(t)|^2 <= int product_j |Psi_{f_j}(u_j,t(Au)_j)|du.       (E4)

(E1)-(E4) are a genuine averaged-frequency replacement for the false law-uniform pointwise estimate for E exp(i t X^2): the normalized conditional density of V|U=u may have cap 1/(2r(u)), but the dangerous r(u)^(-1) cancels exactly against the unnormalized kernel before integration.

The remaining full-target problem is now geometric/analytic: combine three copies of (E1)/(E2) along the coupled coefficient maps u -> (Au)_j without introducing inverse conditional caps or a uniformly good single minor. I will next test this on the designated partner's two-hub rank-one arrowhead and on the projected-crossing receiver.
