# Independent derivation of the proposed H3 identity

2 October 2026. Root analytic audit of the local Ward identity and response
completion, before final comparison with the assembled general theorem.
This note concerns H0=H1=H2=0 only; it proves no all-orders assertion.

Use the already audited general H2 notation. The full, ungrounded response
matrix has kernel exactly the functions constant on its port set A (or C
for f). If both matrices are nonzero, each port set has at least two vertices.
H2=0 implies their contrast spaces are orthogonal in the grounded Green
metric, so |A intersect C|<=1. Choose the grounded vertex r in A minus C.

For each e-response row eta_g and f-response row theta_h let

\[
 u_g(x)=p_xT\eta_g^{\mathsf T},\qquad
 z_h(x)=p_xT\theta_h^{\mathsf T}.
\]

All sources here are extended by their balancing coordinate at r. Their
full Laplacian sources satisfy Lu_g=eta_g on A and Lz_h=theta_h on C.
Orthogonality and the response-space lemma imply z_h=0 on A, while u_g is
constant k_g on C. Write R_h=theta_h T theta_h^T=sum_edges c(dz_h)^2.

The candidate identity, with the Rayleigh coefficients normalized as in the
H2 theorem, is

\[
 H_3=\tau^2\sum_{g,h,j}c_gc_hc_j
 \left[(u_g(x_j)-k_g)z_h(y_j)
       -(u_g(y_j)-k_g)z_h(x_j)\right]^2.
\tag{1}
\]

The following independently checks its algebraic ingredients.

## Ward sign and normalization

Use positive Gaussian exponent +bar(psi)L psi, with q_i=bar(psi_i)psi_i.
The forest perturbation is tV, V=sum_i q_i-sum_edges c_ij q_iq_j.
It can be written using vertex factors (1+tq_i) and invariant bonds

\[
 f_{ij}^{(t)}=(\bar\psi_i-\bar\psi_j)(\psi_i-\psi_j)-tq_iq_j.
\]

With left odd derivatives, both Q_t=sum_i(1-tq_i)partial_psi_i and its
barred counterpart annihilate each bond. The divergence with respect to the
vertex factor is zero because (1+tq_i)(1-tq_i)=1. Interior Berezin
integration by parts thus passes invariance to the unnormalized conditional
factor. Its Schur quadratic form is independent of the marked conductance:
the harmonic exit rows at the two marked endpoints agree. Consequently the
marked logarithmic score inherits invariance, even though the normalized
conditional factor itself has a noninvariant Schur factor.

On the f side all ports C are ungrounded. Expand its score as
U_f=tU_f1+t^2U_f2+..., with U_f1=constant+bar(psi)B_f psi.
The order-two Ward equations imply

\[
 D_{\mathbf1_C}U_{f2}=-\bar\psi B_f\psi.
\tag{2}
\]

Here D_a denotes the covariance lowering derivative in direction aa^T.
For verification, P=sum_{i<j}(B_f)_{ij}q_iq_j has the same first odd
derivatives as U_f2. Their difference is translation invariant in both odd
directions. The contraction of P is -bar(psi)B_f psi, using the zero row
sums of the full response matrix. No sign restriction on its off-diagonal
entries is used.

## Coefficient extraction

The harmonic extensions, boundary covariance T, and cross derivative of
log(tau) are independent of perturbations of the marked conductances in
this equality geometry. Conditional E and F interiors factor. Hence the
mixed logarithmic derivative is the boundary covariance of the two local
marked scores. Its order-three coefficient is

\[
 \operatorname{Cov}_0(U_{e2},U_{f1})+
 \operatorname{Cov}_0(U_{e1},U_{f2})+
 \kappa_0(U_{e1},U_{f1},V).
\tag{3}
\]

The last expectation can use the full Gaussian field, because the first two
arguments depend only on boundary fields. For a rank-one bilinear with
response potential a, its covariance with a polynomial P is
-E[D_a P]. The first covariance in (3) is zero: every z_h vanishes on A,
where U_e2 depends. Equation (2) and u_g=k_g on C give the second covariance
as sum_{g,h}c_gc_h k_g^2 R_h.

The linear terms sum_i q_i in V contribute zero to the mixed third cumulant:
every contraction joining the two response bilinears contains the vanishing
inner product eta_g T theta_h^T. For a quartic q_xq_y, the third cumulant
equals (u_g(x)z_h(y)-u_g(y)z_h(x))^2. One way to check its coefficient is
to perturb the Gaussian quadratic form by the two rank-one bilinears. Under
their zero cross inner product, the covariance is exactly
K-alpha u_g u_g^T-beta z_h z_h^T up to terms depending on only one parameter;
the alpha beta coefficient in its two-by-two principal determinant is the
displayed square. Since the quartic in V has coefficient -c_xy, the last
term in (3) is minus the corresponding edge energy.

Finally R=-Z^2 partial_e partial_f log Z. All earlier mixed coefficients
vanish, so H3 is -tau^2 times (3); lower terms of Z^2 do not contribute.
Thus H3/tau^2 is the unshifted wedge energy minus sum c_gc_h k_g^2R_h.

## Completion for arbitrary multiport currents

This last step requires no two-terminal or positive-edge representation.
For v=u_g, w=z_h, k=k_g define

\[
 J=\sum_{xy}c_{xy}(v_xw_y-v_yw_x)(w_y-w_x).
\]

Direct expansion and discrete integration by parts give

\[
 J=\sum_x v_xw_x(Lw)_x-\sum_xw_x^2(Lv)_x=kR_h.
\]

The last equality uses w=0 on A, Lv supported on A, v=k on C, and Lw
supported on C. Therefore

\[
 \sum_{xy}c_{xy}(v_xw_y-v_yw_x)^2-
 \sum_{xy}c_{xy}((v_x-k)w_y-(v_y-k)w_x)^2=k^2R_h.
\]

Substitution yields (1). This identity is valid with arbitrary signed
multiport currents; it relies only on the support and constant-potential
properties. Ground edges are included in this energy calculation.

If a response matrix is zero, its support has a single interface port. The
marked subgraph then attaches to the rest at a cut vertex and the weighted
forest polynomial factors; the distinct marked edges lie in different
factors. Their entire Rayleigh difference is zero. This case should be
stated explicitly in the final theorem.

This derivation establishes the displayed identity conditional on the
already proved H2 response setup and local Ward construction. The final
assembled proof still needs comparison for definitions, powers and factors;
finite checks support an identity but cannot replace these analytic steps.
