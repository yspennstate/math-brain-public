SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B15, 2026-09-24T05:03:54Z.
attacking: a uniform submass stability estimate on the e5f71d79 ruled one-sheet, with rough-input passage at the interval level and no use of output continuity.

# Early calculation: square-root submass gain on the isotropic ruled sheet

Programme: QFORM-DENSITY-3EIG-20260922. Full conjecture remains OPEN.

Let R be an n x 3 matrix with orthonormal columns and rows r_i in R^3, and put

q(X)=<r_1^*,X>^2+<r_2^*,X>^2-<r_3^*,X>^2,

where equivalently Y=R^T X and q=Y_1^2+Y_2^2-Y_3^2. All original coordinates are independent with probability densities <=1 except a chosen coordinate j, whose factor g satisfies 0<=g<=1 and int g=m<=1. Denote by nu_g^+ the pushforward submeasure restricted to {q>=0}.

The completed ruled theorem at math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837 gives, for smooth inputs and s>=0, the parametrisation

  y=sqrt(s)e_theta+t v_theta,  v_theta=e_theta^perp+e_3,
  delta(q-s)dy=(1/2)dtheta dt.

Hence if rho_g is the 3D projected subdensity,

  r_g^+(s)=(1/2) int_0^{2pi} int_R rho_g(sqrt(s)e_theta+t v_theta) dt dtheta.      (1)

Write vhat_theta=v_theta/sqrt(2), and let U_theta be any 2 x 3 matrix with orthonormal rows spanning vhat_theta^perp. The inner line integral is 1/sqrt(2) times the density h_theta of U_theta Y at the projected point.

Put b_j(theta)=U_theta r_j in R^2. Since sum_i b_i b_i^T=I_2, the remaining-coordinate frame has Gram matrix

  G_theta=I_2-b_j b_j^T,
  det G_theta=1-|b_j|^2=:d_j(theta).

Two independent bounds hold for the projected subdensity h_theta.

(1) Complete g to a cap-one probability density in coordinate j. The 2D product-projection theorem used in the ruled source gives h_theta<=2.

(2) Condition on X_j and use only its mass m. The projection of the remaining probability product has density at most 2/sqrt(det G_theta), by normalising G_theta^{-1/2} and applying the same 2D projection theorem. Therefore

  h_theta <= 2 min(1, m/sqrt(d_j(theta))).                         (2)

Now |b_j|^2=|r_j|^2-(r_j.vhat_theta)^2. If ell=|r_j|<=1 and r_j=(u_1,u_2,c), then

  d_j(theta)=1-ell^2 + ( -u_1 sin theta + u_2 cos theta + c )^2/2.   (3)

Set z(theta)=sqrt(d_j(theta)) and F(t)=Leb{theta in [0,2pi): z(theta)<t}. I claim

  F(t) <= 20 sqrt(t)   for every t>0.                               (4)

For t>1/8 this follows from F<=2pi<20 sqrt(t). For 0<t<=1/8, z<t implies ell^2>1-t^2>=63/64 and

  |-u_1 sin theta+u_2 cos theta+c| < sqrt(2)t.

Let A=sqrt(u_1^2+u_2^2). If A<1/4, then |c|>sqrt(59)/8 and the last display is impossible because |c|-A>sqrt(2)/8. Thus A>=1/4. After a phase shift the condition is

  |cos phi-q|<epsilon,   epsilon=sqrt(2)t/A <=4sqrt(2)t.

The elementary arcsine bound

  Leb{phi: |cos phi-q|<epsilon} <= 8 sqrt(epsilon)

holds uniformly in q. Consequently F(t)<=16*2^(1/4)*sqrt(t)<20sqrt(t), proving (4).

Using

  min(1,m/z)=int_0^1 1_{z<m/u} du,

Tonelli and (4) give

  int_0^{2pi} min(1,m/z(theta)) dtheta
   =int_0^1 F(m/u) du
   <=20 sqrt(m) int_0^1 u^(-1/2)du
   =40 sqrt(m).                                                     (5)

Combining (1),(2),(5),

  ||r_g^+||_infinity <= 20 sqrt(2) sqrt(m).                         (6)

This is a direct essential-height estimate for a positive submeasure; no continuity is used.

If two cap-one probability marginals f_j,g_j differ by delta=||f_j-g_j||_1 while all other marginals are fixed, decompose f_j-g_j=h_+-h_- with int h_+=int h_-=delta/2. Applying (6) to each positive submass yields the uniform majority-sheet stability estimate

  ||r_f^+-r_g^+||_infinity <= 40 sqrt(delta).                       (7)

The fleet03/B15 auto32 sharp example for q=2XY+Z^2 has nonnegative source supports, hence lies entirely on this same majority sheet, and gives

  |p_f(delta)-p_g(delta)|
   =sqrt(delta)[1-log 2-(1/2)log(1+delta/4)].

Thus exponent 1/2 in (7) cannot be improved, even for one fixed owner-target matrix. The new point is the matching uniform upper exponent across all n and all orientations of the isotropic rank-three (+,+,-) spectral frame on the ruled side.

Rough-input bridge to be recorded in the final report: mollify only original-coordinate factors, including g. Cap and mass are preserved, product L1 convergence gives total-variation convergence of the restricted pushforward submeasures, so interval domination (6) passes with the same constant. This avoids pointwise traces of rough densities and keeps continuity downstream.
