# QFORM B01 r43 early mathematical checkpoint

Status: supporting theorem proved below; full conjecture remains open.

## Three-original-hub joint-Plancherel receiver

Let H consist of three original coordinates and let Y be any disjoint bank of the remaining original coordinates. After conditioning any further coordinates, write

Q = X_H^T C X_H + d_H^T X_H + 2 X_H^T (B Y + c) + R(Y),

where C is arbitrary symmetric, R is an arbitrary real quadratic polynomial (indeed its phase may be any measurable real function), and B is 3 x m of rank three. Put

Pi_3(B) = sqrt(det(B B^T)) = sigma_1(B) sigma_2(B) sigma_3(B).

For independent inputs with densities at most one,

|phi_Q(t)| <= min(1, 2^(3/4) pi^(3/2) Pi_3(B)^(-1/2) |t|^(-3/2)),

and hence

||p_Q||_infinity <= 3 sqrt(2) Pi_3(B)^(-1/3).

The density has a continuous C_0 representative in this branch.

Proof core. Let U=BY+c. The product-projection bound used in the Claude Fourier report gives

||p_U||_infinity <= 2^(3/2) Pi_3(B)^(-1),

so ||p_U||_2 <= 2^(3/4) Pi_3(B)^(-1/2). For fixed t define the three-dimensional Fourier transform

F_t(xi)=E_H exp(i t(X_H^T C X_H+d_H^T X_H)+i xi^T X_H).

Plancherel and f_h<=1 imply ||F_t||_2 <= (2 pi)^(3/2). Therefore, discarding only the arbitrary Y-phase,

|phi_Q(t)| <= int p_U(u)|F_t(2tu)|du
            <= ||p_U||_2 (2|t|)^(-3/2)||F_t||_2
            <= 2^(3/4) pi^(3/2) Pi_3(B)^(-1/2)|t|^(-3/2).

Integrating min(1,a|t|^(-3/2)) gives 6a^(2/3), and Fourier inversion yields 3sqrt(2) Pi_3(B)^(-1/3).

This is a joint averaged-frequency estimate. It does not assert any law-uniform pointwise scalar quadratic-phase decay.

Next: stress this on a strict-N3 coloop family with singular values epsilon^(-1), epsilon^(-1), epsilon^2 (product one), where Claude D/D'/D5/H natural gates fail because the tiny third singular direction is carried by one leaf coordinate; compare the newest fleet03/B01 local pair+rank2-Schur theorem, which should deteriorate with the tiny physical entry while this aggregate receiver stays at 3sqrt(2).
