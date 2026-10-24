SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B07, 2026-09-24T09:39:02Z.
attacking: the r50 rank-54 / H62-rank4 survivor — determinant-weight preserving balanced cuts for diffuse finite-rank physical blocks, with the operator tail retained.

# Early substantive calculation

Let R=U Lambda U^T be a symmetric rank-r matrix on a literal physical coordinate set L, with U^T U=I_r and row leverages ell_i=||U_{i,*}||_2^2. Put delta=max_i ell_i and rho=sqrt(r delta).

For independent Rademacher signs eps_i, S=sum_i eps_i u_i u_i^T satisfies

E ||S||_F^2 = sum_i ||u_i u_i^T||_F^2 = sum_i ell_i^2 <= delta r.

Hence some sign choice has ||S||_op<=||S||_F<=rho. With I={eps_i=+1}, J=L\I,

(1-rho)I_r/2 <= U_I^T U_I, U_J^T U_J <= (1+rho)I_r/2.

Writing a=(1-rho)/2, the physical crossing M0=R[I,J]=U_I Lambda U_J^T obeys

s_k(M0)>=a s_k(R), k<=r.

Its left singular space is col(U_I), so every physical row leverage on the I side is at most ell_i/a<=delta/a. Since the 3-volume marginal formula from the pinned e5f71d79... Theorem D is alpha_i=sum_m p_m q_m(i)^2 with 0<=p_m<=1, each alpha_i is at most this row leverage. Thus delta<=1/(4r) implies rho<=1/2, alpha_i<=4 delta<=1/r<=1/3, so the exact low-rank crossing is inside Theorem D without selecting any individual minor.

For the live operator tail, let M=M0+E with ||E||_op<=eta and mu=s3(M)>0. If P0 projects onto col(M0), h0=max_i (P0)_{ii}, then for any tau in (eta,mu], split the singular modes of M into strong (s_m>=tau) and weak. The strong left singular subspace P_tau satisfies ||(I-P0)P_tau||_op<=eta/tau. For the actual 3-volume weights p_m,

3 e_3(x) = sum_{a<b} x_a x_b sum_{c notin {a,b}} x_c >= x_3 e_2(x),

so every weak mode has p_m<=3 s_m^2/s3(M)^2<=3 tau^2/mu^2. Therefore the ACTUAL volume-sampling row marginals obey

alpha_i <= (sqrt(h0)+eta/tau)^2 + 3(tau/mu)^2.

This is the operator-tail transfer needed for the r50 near-rank-four state: it controls the determinant weights of the actual crossing, rather than replacing the tail by zero. Full constants and the live r50 corollary go in REPORT.md.