SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B13, 2026-09-23T23:37:51Z.
attacking: mu-weighted cancellation to a finite physical center or a genuinely diffuse transverse bank in the exact-rank-two survivor.

# Early substantive calculation

Work in the diffuse exact-rank-two chamber

`A = D + U Lambda U^T`, `U^T U=I_2`, `max_i ||u_i||^2<=1/3`, `s_3(A)>=1`.

Use the fleet04/B13 slab dichotomy and the previous fleet03/B13 r36 intrinsic pair law. For the partner-selected physical `k`, let `c=||u_k||^2>0`, rotate only the latent two-dimensional coefficient basis so `u_k=(sqrt(c),0)`, and write `u_i=(x_i,y_i)`. Put

`s_i=y_i^2=q_ki/c`, so exactly `sum_{i!=k}s_i=1`.

Let `mu_k({r,s})=q_rs Delta_{krs}/W_k`, where `W_k>=1/1152`, and let `tau_{krs}` be the transverse three-leaf invariant from r36. In the non-rank-one branch of fleet04/B13,

`E_mu |tau| < M0 rho^-1`, `M0=437400000/(1536 e^2)=38538.83651542604...`.

For arbitrary `theta in (0,1)`, define the physical heavy center

`H_theta={i!=k:s_i>=theta}` and `L_theta=H_theta^c`.

Then `|H_theta|<=theta^-1`.

Let `m_theta=mu{E:E intersects H_theta}`.

* If `m_theta>=1/2`, then some physical `h in H_theta` has intrinsic star mass

  `mu{E:h in E}>=theta/2`.

  Hence the star-conditional transverse cancellation satisfies

  `E(|tau_E| | h in E) <= 2 M0 theta^-1 rho^-1`.

* If `m_theta<1/2`, then

  `sum_{E subset L_theta} q_E Delta_E > W_k/2 >=1/2304`.

  Since `0<=Delta_E<=1`, Cauchy-Binet gives the genuine rank-two physical-bank volume floor

  `det(U_L^T U_L)=sum_{E subset L_theta}q_E >=1/2304`,

  so `sqrt(det(U_L^T U_L))>=1/48`.

  In the chosen coefficient basis the transverse energy is

  `S_L=sum_{i in L_theta} y_i^2=sum_{i in L_theta}s_i`.

  Since `det(U_L^T U_L)<=S_L`, one gets `S_L>=1/2304`. Therefore each physical row obeys

  `s_i/S_L < 2304 theta`.

  Also

  `E(|tau_E| | E subset L_theta) < 2 M0 rho^-1`.

Choosing `theta=1/4608` produces the concrete dichotomy:

1. a finite center of at most `4608` physical rows contains a row whose intrinsic mu-star mass is at least `1/9216`; or
2. a complementary physical bank has coefficient rank-two area at least `1/48`, and its transverse coefficient direction has normalized physical row marginals at most `1/2`.

This is the first needed bridge from the r36 `mu_k`-average cancellation to a product-preserving finite-center/diffuse-bank geometry; it requires no lower bound on one physical minor and no support assumptions on the input laws. Full QFORM remains open.