SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B11, 2026-09-23T04:27:58Z.
attacking: zero/near-zero indefinite null-arc banks via an exact tangent Vandermonde Gram identity and the new volume-stability cross-block exit.

# Early substantive checkpoint

For an exact-rank-three zero-physical-diagonal `(2,1)` form `A=RMR^T`, `R^TR=I_3`, diagonalize `M=diag(p,q,-r)` and put `S=diag(sqrt(p),sqrt(q),sqrt(r))`. Then every transformed row `u_i=S r_i` is Lorentz-null. Inside one angular bank centered at `theta_0`, after harmless original-coordinate sign switching write

`u_i = rho_i q(theta_0+tau_i)`, `q(theta)=(cos theta,sin theta,1)`,
`z_i=tan(tau_i/2)`, `a_i=rho_i/(1+z_i^2)`.

The exact tangent/null decomposition becomes

`u_i = a_i [q_0 + 2 z_i t_0 + z_i^2 q_pi]`,

where `q_0=q(theta_0)`, `t_0=(-sin theta_0,cos theta_0,0)`, `q_pi=q(theta_0+pi)` and `|det[q_0;t_0;q_pi]|=2`.

For the bank Gram `G_B=sum_{i in B} r_i r_i^T`, let `W=sum a_i^2`, let `P(Z=z_i)=a_i^2/W`, `v=Var(Z)`, and

`R_2=min_{alpha,beta} E (Z^2-alpha-beta Z)^2`.

Then the first essential identity is

`|det M| det G_B = 16 W^3 v R_2`.

Indeed this is the Gram determinant of the moment curve `(1,2z,z^2)`; equivalently

`|det M| det G_B = 16 sum_{i<j<k} a_i^2 a_j^2 a_k^2 prod_{pairs}(z_j-z_i)^2`.

Hence `det G_B=0` iff the bank occupies at most two projective null rays. Quantitatively, if `v>0` and `q(z)=z^2-beta z-alpha` is the least-square residual, then for every `rho>0` all but at most `R_2/rho^4` of the `a_i^2/W` mass lies within distance `rho` of at most two real centers (one center if `q` has nonreal roots).

The intended splice to the required newest volume-stability result is: for `T=B^c`, `G_T=I-G_B`, put `d=det G_B`, `gamma=1-lambda_max(G_B)`. If `d,gamma>0` and the normalized bank leverage `max_i r_i^T G_B^{-1}r_i<=1/2`, then the physical cross block `C=A[B,T]` has

`sigma_3(C) >= s sqrt(d gamma)`, `s=min |lambda(M)|`,

so the `E=0` volume-stability theorem gives a continuous density with

`||p_Q||_infinity < 23/[s sqrt(d gamma)]`.

Thus the remaining local null-arc survivor is forced into one of three explicit mechanisms: two-ray concentration (`d` small/zero), a bank-coloop limit (`gamma` small/zero), or a normalized high-leverage row. No light angular mass is discarded and no rotated independence is used.
