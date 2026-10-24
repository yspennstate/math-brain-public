SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B04, 2026-09-23T13:49:02Z.
attacking: replace uniform fourth-volume face deletion by an entropy-biased deletion flow; prove a max-flow dichotomy that either opens the q=4/3 third-volume Fourier gate or forces >2/3 of fourth-volume onto one physical four-row packet, then pay that packet with account02/B04's completed support-defect theorem.

# Early substantive checkpoint

Let M=A[I,J] be an ORIGINAL-coordinate cross block and E4=e4(M^T M)>0. For each physical four-row set R set d_R=det(M_R M_R^T) and pi_R=d_R/E4. For each supported triple S set a_S=det(M_S M_S^T) and tau_S=sum_{j notin S} dist(m_j,span M_S)^2. The previous face identity gives mu0(S)=a_S tau_S/(4E4) when R~pi and one row is deleted uniformly.

NEW mechanism: conditionally on R delete J with an arbitrary kernel kappa_R(j), j in R. Let mu be the resulting triple law and alpha_i=P_mu(i in S). Comparing the joint laws (R,J), then pushing forward to S, gives

D(mu||mu0) <= K(kappa):=sum_R pi_R D(kappa_R||Unif(R)).

Since p(S)=a_S/E3 is the canonical third-row-volume law,

D(mu||p)=D(mu||mu0)+log(E3/(4E4))+E_mu log tau_S.

Therefore the determinant/entropy currency of the lifted 3x3 minor law is EXACTLY

G(mu)=4E4 exp[-D(mu||mu0)] / exp(E_mu log tau_S),

and hence

G(mu) >= 4E4 exp[-K(kappa)]/tau_geo(mu)
       >= E4/||M||_F^2,

because K(kappa)<=log 4 for every deletion kernel.

The remaining issue is to obtain alpha_i<=2/3. Write rho_i=P_pi(i in R), delta_i=P(J=i), so alpha_i=rho_i-delta_i. A deletion kernel with alpha_i<=2/3 exists iff the fractional Hall inequalities

sum_{i in U}(rho_i-2/3)_+ <= P_pi(R intersects U)

hold for every physical row set U. If Hall fails, discard zero-demand indices; then every i in U has rho_i>2/3 and sum_i rho_i=4, so |U|<=5. Pointwise K=|R cap U| shows Hall cannot fail for |U|=1,2,3,5. Thus |U|=4. For such U, failure means

E K -8/3 > P(K>=1).

For K=0,1,2,3,4 the variable K-8/3-1_{K>=1} is at most -2/3 except at K=4, where it is 1/3. Therefore failure forces P(K=4)>2/3. Since both R and U have four elements, this is pi(U)>2/3.

So either:
(A) an entropy-biased deletion kernel has alpha_*<=2/3, hence q=4/3 and the weighted third-volume Fourier theorem gives a C0 density with

||p_Q||inf <= (9 sqrt(3) e/2) (E4/||M||_F^2)^(-1/6),

or
(B) one four-row packet U has d_U>(2/3)E4. For N=M_U,* (rank four), every probability law on its physical row triples has max row marginal >=3/4, so account02/B04 `QFORM-FRACTIONAL-SUPPORT-DEFECT-COMPLETE-EXIT-v1` applies. Also E3(N)>=4 d_U^(3/4) by AM-GM on the four positive squared singular values. Thus

||p_Q||inf <= 6*4^(1/6) E3(N)^(-1/6)
            <= 6 d_U^(-1/8)
            < 6 ((2/3)E4)^(-1/8),

again with a C0 density.

This removes the quantitative near-coloop hole of the previous fourth-volume downshift at the price of matrix-scale E4/Frobenius currency. Full QFORM is still open because the three-large-eigenvalue hypothesis does not yet force an original-coordinate cut with target-scale fourth-volume currency.
