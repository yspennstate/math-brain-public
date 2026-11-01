# Independent transfer and global-invariant audit

2 October 2026. This note independently audits [RESPONSE_INDUCTION_INDEPENDENT_AUDIT.md](RESPONSE_INDUCTION_INDEPENDENT_AUDIT.md). The transfer calculation below closes the separate algebraic gap identified in the earlier [RESPONSE_CLOSURE_INDEPENDENT_AUDIT.md](RESPONSE_CLOSURE_INDEPENDENT_AUDIT.md). It does not prove forest negative correlation at every fugacity, and it does not certify historical novelty or external peer review.

## 1. The invariant that must be propagated

At a continuing stage, keep two disjoint marked interiors I,J, with no graph edge between them, and all local ports free before grounding. The original marked edge e belongs to the I local subgraph and f to the J local subgraph. Their original electrical current potentials are zero outside these respective interiors; a marked endpoint may be a zero-potential port. Hence every harmonic extension has equal marked-endpoint values. The local Schur complements, harmonic rows, outer Gaussian law, and their Gaussian normalizers are fixed under the respective marked conductance variations.

Let the exact local marked scores be

\[
 U_e(t)=C_e(t)+t^\ell Q_{B_e}+t^{\ell+1}P_e+O(t^{\ell+2}),\qquad
 U_f(t)=C_f(t)+t^\ell Q_{B_f}+t^{\ell+1}P_f+O(t^{\ell+2}).\tag{1}
\]

Here C_e,C_f are genuine boundary-field scalars, each depends only on its own marked local subgraph, Q_B=\bar\psi B\psi, and B_e,B_f are positive semidefinite with the full contrast range on their respective geometric ports. Their Gram channel weights are positive. The local scores obey both exact deformed odd-translation Ward identities. These assertions hold initially at \ell=1 by the H_2 proof, before any absorption.

The first requirement is more than the vanishing of a few global coefficients: every lower **local** score coefficient must be scalar. This is precisely what the transfer calculation preserves.

## 2. Ward decomposition of the next score coefficient

Use left Grassmann derivatives. Write D_\psi=\sum_i\partial_{\psi_i} and D_{\bar\psi}=\sum_i\partial_{\bar\psi_i} on all free old ports. Exact deformed invariance at the next order gives

\[
 D_\psi P=\sum_i q_i\partial_{\psi_i}Q_B,\qquad
 D_{\bar\psi}P=\sum_i q_i\partial_{\bar\psi_i}Q_B.
\]

For symmetric B with B\mathbf1=0, the explicit particular solution is

\[
 P_B=\sum_{i<j}B_{ij}q_iq_j.
\]

Indeed \partial_{\psi_i}q_i=-\bar\psi_i and \partial_{\bar\psi_i}q_i=\psi_i; the off-diagonal terms give exactly the two displayed right sides, while the diagonal terms there vanish by nilpotence. Consequently

\[
 P=P_B+R,\qquad D_\psi R=D_{\bar\psi}R=0.\tag{2}
\]

There is no \ell multiplier or factorial. R may have arbitrary allowed Grassmann degree; its ordinary translation invariance, rather than a degree assumption, is what is needed.

## 3. Successive conditioning has no extra score term

Assume the cross trace and shifted wedge vanish, and enlarge I by the support of its shifted response potentials a_\rho. Every a_\rho has physical zero-sum charge \rho on the old ports and is zero outside the enlarged region I'. The old-port harmonic rows in the new Dirichlet problem all equal \pi, by the full-contrast source argument in the closure audit.

Successive Gaussian elimination writes the new normalized conditional partition as the outer conditional average of the old partition times the remaining interaction. The outer Gaussian kernel is mark-independent: its Schur block is obtained from the old marked-independent local Schur complement. The determinant normalization satisfies the same factorization. Therefore, exactly,

\[
 U_{I'}(t)=\mathbb E_{\mathrm{outer},t}[U_I(t)].\tag{3}
\]

The expectation is a normalized formal Wick tilt; no positivity of a Grassmann measure is being assumed. Formula (3) includes every product coming from numerator and denominator normalization.

Every scalar coefficient in C(t) is preserved **exactly** by (3). It cannot couple with an interaction tilt to create a field-dependent term. Thus, at order \ell+1, the only possible nonconstant contribution is

\[
 \mathbb E_0[P]+\operatorname{Cov}_0(Q_B,W_1),\tag{4}
\]

where W_1 is the ordinary first tilt coefficient. Higher tilt coefficients first appear at order \ell+2; there is no missing lower-score product term.

## 4. Evaluate the two contributions independently

Write the old fields under the new conditional Gaussian law as

\[
 \psi_s=\chi_s+\pi\psi_{A'},\quad
 \bar\psi_s=\bar\chi_s+\bar\psi_{A'}\pi^T\qquad(s\in A).
\]

Because B\mathbf1=0, Q_B is entirely a fluctuation bilinear. Its mean is scalar. Since R in (2) is invariant under both ordinary uniform odd translations, substituting the common harmonic field leaves it independent of the new boundary. Its mean is also scalar. This statement is valid even if R has degree six or higher.

Let C_{AA} be the outer fluctuation covariance on old ports, extended by zero at any old port that remains a new boundary vertex. Wick contraction of P_B gives the boundary bilinear

\[
 \sum_{i<j} B_{ij}(C_{ii}+C_{jj}-2C_{ij})Q_\pi
       =-\operatorname{tr}(C_{AA}B)Q_\pi.\tag{5}
\]

The fully uncontracted term is Q_\pi^2=0. For a Gram decomposition B=\sum_\rho\mu_\rho\rho^T\rho,

\[
 \operatorname{tr}(C_{AA}B)=\sum_\rho\mu_\rho R_\rho,
 \quad R_\rho=\rho^TC_{AA}\rho
        =\sum_{xy}c_{xy}(a_\rho(x)-a_\rho(y))^2.
\]

The equality remains valid if a source port stays outside I': its potential is zero, and its contribution to \rho^Ta is zero.

A quadratic tilt gives only a scalar covariance in (4). Its boundary quadratic part is deterministic, its mixed one-fluctuation terms have zero Wick covariance with the balanced bilinear Q_B, and its fluctuation quadratic part is scalar after contraction.

The uncontracted quartic part of W_1 is minus the sum of physical edge products c_{xy}q_xq_y, with old interior fields first harmonically represented. Earlier old-interior contractions contribute only quadratic or scalar terms, already covered. A rank-one insertion of Q_\rho changes the outer covariance by

\[
 \delta C_{xy}=-a_\rho(x)a_\rho(y).
\]

For the harmonic boundary parts p_x,p_y, the boundary bilinear in \mathbb E[q_xq_y] is

\[
 C_{xx}Q_{p_y}+C_{yy}Q_{p_x}
  -C_{xy}\bar\psi(p_x)^T p_y\psi
  -C_{yx}\bar\psi(p_y)^T p_x\psi.
\]

Its rank-one variation is -Q_{a_xp_y-a_yp_x}. The minus sign in the quartic tilt therefore makes its covariance contribution positive:

\[
 \sum_{\rho,xy}\mu_\rho c_{xy}
       (a_\rho(x)p_y-a_\rho(y)p_x)^T
       (a_\rho(x)p_y-a_\rho(y)p_x).\tag{6}
\]

This computation also shows directly that no quartic or higher new-boundary term survives at this order: the fully uncontracted quartic does not vary with C.

Combining (5),(6), the next boundary coefficient is a bilinear with matrix

\[
 B'=\sum_{\rho,xy}\mu_\rho c_{xy}\delta_{\rho,xy}^T\delta_{\rho,xy}
        -\sum_\rho\mu_\rho R_\rho\pi^T\pi,
 \quad\delta_{\rho,xy}=a_\rho(x)p_y-a_\rho(y)p_x.\tag{7}
\]

## 5. Electrical subtraction gives exactly the next response Gram

For fixed \rho and new boundary function h, put k=\pi h. The flow

\[
 j_{xy}=c_{xy}(a_xh_y-a_yh_x)
\]

has divergence hLa-aLh=k\rho: h is harmonic where a is nonzero and equals k at every old source port. The electrical flow i_{xy}=c_{xy}(a_x-a_y) has divergence \rho. Discrete integration by parts gives

\[
 \langle j,i\rangle_{\mathrm{energy}}
       =\sum_x a_x\operatorname{div}j_x=kR_\rho.
\]

Hence j-ki is a circulation and

\[
 \|j\|_{\mathrm{energy}}^2-k^2R_\rho
       =\|j-ki\|_{\mathrm{energy}}^2.
\]

Polarization of this identity in h proves

\[
 \boxed{B'=\sum_{\rho,xy}\mu_\rho c_{xy}
    \eta_{\rho,xy}^T\eta_{\rho,xy}},\quad
 \eta_{\rho,xy}=a_xp_y-a_yp_x-(a_x-a_y)\pi.\tag{8}
\]

Thus the transferred coefficient is positive semidefinite. The closure audit proves it has the full new-port contrast range. If there are at least two new ports, it is nonzero, so the first nonconstant local score has advanced by **exactly** one order, from \ell to \ell+1. If there is one port, exact Ward invariance makes the full score scalar at every order, which is an exact forest-block stop.

No M-matrix hypothesis, positive auxiliary-edge representation, or confinement of all higher score coefficients to bilinears has been used.

## 6. Audit of the global cross-score coefficient induction

With both local scores satisfying (1) at the same \ell, and the outer Gaussian kernel fixed under both marks,

\[
 \partial_{ef}\log F(t)
     =\operatorname{Cov}_{\mathrm{boundary},t}(U_e,U_f).
\]

Scalar C_e,C_f terms drop exactly. Therefore the first possible term is t^{2\ell}, with coefficient

\[
 \operatorname{Cov}(Q_{B_e},Q_{B_f})
       =-\operatorname{tr}(TB_eTB_f).
\]

The forest Rayleigh identity is

\[
 \mathcal R_{ef}(\lambda\mathbf c)
 =-\lambda^{2n-4}\tau^2F(1/\lambda)^2
        \partial_{ef}[\log\tau+\log F(1/\lambda)].\tag{9}
\]

The initial transfer-current equality removes the mixed tree derivative. All earlier mixed local-score terms are absent, not merely assumed to cancel. Thus the first possible Rayleigh coefficient is H_{2\ell}=\tau^2\operatorname{tr}(TB_eTB_f), a nonnegative sum of cross-response squares. If it is positive, it determines the large-\lambda sign.

If that trace is zero, PSD implies every cross-response Green product is zero. The order t^{2\ell+1} coefficient in the covariance is exactly

\[
 \operatorname{Cov}(P_e,Q_{B_f})+
 \operatorname{Cov}(Q_{B_e},P_f)+
 \operatorname{Cum}(Q_{B_e},Q_{B_f},W_1).\tag{10}
\]

There is no coefficient depending on \ell in (10). The Ward particular solution (2), rank-one constant-mode contraction, and quartic triple cumulant are the same identities used in the H_3 proof. They give the shifted physical response wedge square for H_{2\ell+1}. The scalar and lower-coefficient products in F(t)^2 in (9) do not alter this coefficient, because every earlier mixed logarithmic coefficient has already vanished.

If both cross trace and wedge vanish, the support separation and finite-growth lemmas apply. Transfer (8) propagates the full invariant (1), with \ell replaced by \ell+1. Local Ward invariance is retained intrinsically with all new port fields free. The original marked currents remain supported in the enlarged regions, so the marked-independent Schur/normalization condition is also retained. No new condition on higher score degrees is introduced.

Both nontrivial sides strictly enlarge, while a connected graph leaves a nonempty separator between them. After finitely many enlargements, a cross trace or wedge is positive, or a singleton-port factorization makes the mixed derivative identically zero. This supplies the finite alternative needed to deduce nonpositive marked covariance for all sufficiently large fugacity on every finite positive-conductance graph.

## 7. Scope and verdict

The transfer identity and the coefficient invariant pass this independent analytic audit. In particular, the earlier specific gap is closed by (2)--(8), rather than by finite examples or an assumption that higher scores remain quadratic.

The resulting statement is a **high-fugacity** forest theorem: for each fixed finite weighted graph and marked pair there is a finite threshold beyond which the covariance is nonpositive. There are finitely many pairs, so one may take the maximum threshold for the graph. It gives neither an explicit useful threshold in general nor negative correlation at every positive fugacity. It does not establish negative association or the q<1 random-cluster conjecture.

The assembled global theorem should include the invariant in Section 1, the intrinsic ungrounded local Ward identities, and the exact scalar stop. Primary source and novelty boundaries remain those documented in the final H_3 note. Independent exact iteration and delayed local-score checks support normalization but are not substituted for the transfer proof.
