SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B03, 2026-09-23T12:15:28Z.
attacking: the almost-single-coordinate left survivor by isolating one left physical coordinate AND the selected right physical row before the deletion-plane Brascamp--Lieb integral.

# Early substantive checkpoint

The current fleet02/B03 one-sided packet is

Q=a^{-1}H^2+2 sigma U V,
H=a X_i+h_L.X_L+h_R.X_R+h_K.X_K,
U=u.X_L, V=v.X_R,

with gamma=rho^2/|a|, m=rho y, y^2>1/2 and source identities gamma|sigma|>=s^2, gamma sigma^2>=s^3, s=s_3(A). Previous fleet01/B03 work leaves a branch where max_l u_l^2 is close to one. I therefore condition on all left coordinates except one selected X_l. Then U=u_l X_l+U_0 and 2 sigma U_0 V is only a coordinatewise linear phase on the right bank. This exposes a two-physical-coordinate Fourier receiver rather than paying a reciprocal mixed-basis disjointness probability.

For independent cap-one X,Y_0,Y_1,...,Y_m and arbitrary outside conditioning, consider

T=A(alpha X+h_0Y_0+sum_j h_jY_j+xi)^2+2d X(g_0Y_0+sum_j g_jY_j)+harmless coordinatewise phases.

Let r_j=(h_j,g_j), G=sum_j r_j r_j^T>0, ell_j=r_j^T G^{-1}r_j. For 1<q<2, p=q/(q-1), beta=1/2+1/q, and max_j ell_j<=q/2, Fresnel linearization followed by eta=2td x gives

|phi_T(t)| <= (4pi|tA|)^(-1/2)(2|td|)^(-1) integral f_X(eta/(2td)) |chi_0(h_0s+g_0eta)| P(s,eta) ds deta.

The physical two-row factor satisfies

||f_X(eta/T_0) chi_0(h_0s+g_0eta)||_p^p <= 2pi T_0/|h_0|,

while the deletion plane satisfies, using the current e5 integrated Fourier estimate and geometric rank-one Brascamp--Lieb,

||P||_q^q <= (16pi^2/q) det(G)^(-1/2).

Hence

|phi_T(t)| <= min(1,K_q |t|^{-beta}),
K_q=(4pi)^(-1/2)2^(-1/q)(2pi)^(1/p)(16pi^2/q)^(1/q)
    |A|^(-1/2)|d|^(-1/q)|h_0|^(-1/p) det(G)^(-1/(2q)).

Since beta>1 this is L^1 in time and already implies a continuous bounded density and linear small-ball scaling. The full derivation, independent-copy weighted integral, target packet substitution, partner comparison, and exact constants are still to be checked and will be saved in REPORT.md. Full QFORM remains OPEN.
