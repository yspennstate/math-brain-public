SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B11, 2026-09-23T14:15:42Z.
attacking: the finite-shared-spike null-sum chamber via a four-row L2 matching estimate that removes the leverage<=1/2 gate.

# Early substantive checkpoint

Partner input actually used: fleet02/B11 r31, commit `15189fa11c0c752c1d9022c60e253a9e8d457df8`, reduces the exact null-sum endpoint to

`Q = beta U^2 + 2 alpha V H + R_T(X_T) + sum_i q_i(X_i)`

with disjoint ORIGINAL-coordinate banks S,T, `U=a.X_S`, `H=h.X_S`, `V=c.X_T`, and gives the Fresnel reduction

`|phi_Q(t)| <= (4 pi |beta t|)^(-1/2) * (sqrt(2)/(2|alpha t| C)) * integral_R2 prod_i |hat g_i(a_i xi+h_i y)| dxi dy`,

where `C=||c||_2` and `|g_i|<=f_i<=1`.

New mechanism: choose four distinct rows `i,j,k,l` and pair them into two nonparallel pairs. Put `v_r=(a_r,h_r)` and `Delta_1=|det(v_i,v_j)|`, `Delta_2=|det(v_k,v_l)|`. Dropping all other Fourier factors and applying Cauchy-Schwarz gives

`I <= [int |F_i(v_i.z)F_j(v_j.z)|^2 dz]^(1/2) [int |F_k(v_k.z)F_l(v_l.z)|^2 dz]^(1/2)`

`<= (2 pi)^2 (Delta_1 Delta_2)^(-1/2)`

by the exact 2x2 changes of variables and Plancherel, since `int f_r^2<=int f_r=1`.

Therefore

`|phi_Q(t)| <= min(1, K |t|^(-3/2))`,
`K = sqrt(2) pi^(3/2) |beta|^(-1/2)(|alpha|C)^(-1)(Delta_1 Delta_2)^(-1/2)`.

Fourier inversion then gives the candidate supporting bound

`||p_Q||_inf <= 3*2^(1/3) |beta|^(-1/3)(|alpha|C)^(-2/3)(Delta_1 Delta_2)^(-1/3)`.

This avoids the fleet02/B11 leverage gate entirely in any chamber containing two vertex-disjoint nondegenerate left-plane wedge pairs. Next: check constants, apply to the partner six-coordinate target family, and state the remaining matching-number-one/star obstruction exactly.
