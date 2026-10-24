SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B10, 2026-09-23T08:58:02Z.
attacking: true near-coloop noncollinear mixed bank: force a quantitative longitudinal-regression residual and a disjoint original-coordinate residual/transverse packet from the partner survivor.

# Early substantive checkpoint

In the exact-rank-three near-coloop survivor of account02/B10 / account03/B10 r24, write the genuinely mixed spectral rows as `r_j=s_j e+w_j`, with `w_j perp e`, `rho_M=sum s_j^2`, `H_M=sum w_j w_j^T`, and use the exact cancellation `sum s_j w_j=0`. Let `v` be a unit top eigenvector of `H_M`, `eta=v^T H_M v`, and `y_j=v dot w_j`. Then

`sum s_j^2=rho_M`, `sum y_j^2=eta`, `sum s_j y_j=0`.

Normalize `u_j=(s_j/sqrt(rho_M), y_j/sqrt(eta))`. The coefficient rows satisfy `sum u_j u_j^T=I_2`; hence, with `a_j=s_j^2/rho_M`, `b_j=y_j^2/eta`, one has `sum a_j=sum b_j=1` and `a_j+b_j<=1`. Therefore

`sum a_j b_j <= (1/4)sum(a_j+b_j)^2 <=1/2`.

Randomly split the ORIGINAL mixed-coordinate indices into disjoint `S,T`, each index going to either side with probability `1/2`. Put `rho_S=sum_(S)s_i^2`, `eta_T=sum_(T)y_j^2`. Then

`E[rho_S eta_T]
=(1/4)sum_(i!=j)s_i^2 y_j^2
=(rho_M eta/4)(1-sum a_j b_j)
>=rho_M eta/8`.

Thus there is a deterministic original-coordinate split with

`boxed: rho_S eta_T >= rho_M eta/8`.

In every still-unpaid partner state `eta>7/8`, so actually

`boxed: rho_S eta_T > 7 rho_M/64`.

The normalized linear forms `U_S=rho_S^(-1/2)sum_(S)s_i X_i` and `V_T=eta_T^(-1/2)sum_(T)y_j X_j` are genuinely independent because their source banks are disjoint. No rotated-coordinate independence is used. The same banks still carry nuisance components, so this is a structural packet, not yet a density proof.

Also `min_a sum_j(s_j-a y_j)^2=rho_M` exactly, because `sum s_jy_j=0`: the positive-leakage survivor is maximally non-graph-like in its top transverse direction.

Full QFORM remains open; continuity is not claimed here.
