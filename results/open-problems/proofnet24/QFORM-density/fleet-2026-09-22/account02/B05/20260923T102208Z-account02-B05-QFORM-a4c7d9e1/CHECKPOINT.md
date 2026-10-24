SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B05, 2026-09-23T10:22:08.593825Z.
attacking: the residual-diffuse heavy-null two-sheet branch; quantify the longitudinal leakage left after the two transverse product banks and pay both the nonzero cross-volume collar and the exact zero endpoint without a curved-fiber supremum.

# Early substantive checkpoint — two-bank longitudinal innovation is the missing factor

Full QFORM remains OPEN.

Work in the exact-rank-three heavy-null survivor after the completed nested-heavy exit. In a deterministic spectral coefficient basis,

`r_i=sqrt(c)e_1`, `c>1/2`,

`M=[[0,b,0],[b,alpha,delta],[0,delta,gamma]]`,

with `sigma_min(M)>=1`, hence `|b|>=1`, `|gamma|>=1`. For each residual original coordinate write the spectral row as `(u_j,v_j,w_j)`. The surviving transverse rows `z_j=(v_j,w_j)` satisfy

`sum z_j z_j^T=I_2`, `||z_j||^2<=1/2`.

Apply the completed two-bank partition theorem `QFORM-DIFFUSE-2D-TWO-BANK-PARTITION-v1`: there is a partition of the residual original coordinates into disjoint banks `J,K` for which

`S_G=sum_(j in G) z_j z_j^T`, `lambda_min(S_G)>=1/640`, `G=J,K`.

For each bank put `u_G=(u_j)_(j in G)`, let `Z_G` be the coefficient matrix with columns `(v_G,w_G)`, and define the longitudinal innovation

`tau_G^2 := ||u_G||_2^2-(Z_G^T u_G)^T S_G^(-1)(Z_G^T u_G)`.

This is exactly the squared distance from the longitudinal coefficient row `u_G` to the transverse coefficient span `span(v_G,w_G)` inside the ORIGINAL bank.

The full three-column bank Gram matrix is

`G_G=[[||u_G||^2,(Z_G^T u_G)^T],[Z_G^T u_G,S_G]]`,

so Schur complement gives the exact identity

`det G_G = det(S_G) tau_G^2`.                                              (C1)

For the physical cross block `A[J,K]=R_J M R_K^T`, if `tau_J tau_K>0`, its exact rank is three and the product `Gamma` of its three nonzero singular values obeys

`Gamma^2=det(G_J) det(M)^2 det(G_K)`
`       =det(S_J)det(S_K)|det M|^2 tau_J^2 tau_K^2`,

hence, in the target normalization,

`Gamma >= tau_J tau_K/640`.                                                (C2)

The completed exact-rank-three cross-block Fourier theorem therefore gives the real target inequality

`||p_Q||_infinity <=6 Gamma^(-1/3)`
`                  <=6*640^(1/3)(tau_J tau_K)^(-1/3)`
`                  <51.707 (tau_J tau_K)^(-1/3).`                          (C3)

Thus every branch with `tau_J tau_K` bounded below is paid without any unrestricted curved-fiber supremum.

At the exact endpoint `tau_J=0`, one has coefficientwise `u_J=a v_J+d w_J`. Conditioning on the other bank `K` leaves the independent scalar `X_i` and the dependent two-dimensional product projection `(V_J,W_J)`. Its joint density cap is at most `e/sqrt(det S_J)<=e sqrt(640)`. The homogeneous conditional matrix in `(X_i,V_J,W_J)` is

`H_J=[[0,b sqrt(c),0],[b sqrt(c),alpha+2ba,delta+bd],[0,delta+bd,gamma]]`,

and

`det H_J=-c b^2 gamma`, so `|det H_J|>=c>1/2`. The completed dependence-safe null-scalar theorem therefore gives

`||p_Q||_infinity`
` <=3*2^(2/3)(e sqrt(640))^(2/3)c^(-1/3)`
` <6 e^(2/3)640^(1/3)`
` <100.711.`                                                               (C4)

The same applies with `J,K` reversed. Hence the exact zero-innovation endpoint is also paid.

The first unpaid implication is now genuinely punctured:

`QFORM-NULLROW-PUNCTURED-INNOVATION-BRIDGE-v1` — obtain a bound uniform as `0<min(tau_J,tau_K)->0`, retaining the same-bank dependence between the innovation projection and the transverse pair. Small coefficient norm cannot be treated as a small random perturbation under arbitrary unbounded supports. The latest account03/B05 sigma-free packet theorem does not directly erase this `tau`: its two scalar pair variables must come from genuinely disjoint scalar banks, whereas each B19 bank here carries a dependent two-dimensional transverse product projection. That exact interface, rather than missing matrix curvature, is the current obstacle.
