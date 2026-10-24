# P0297: independent statement packet

Target: determine d_gamma = dim_H(C,D_h^gamma) almost surely, for gamma in (0,2), where h is a whole-plane GFF with its additive constant fixed and D_h^gamma is the canonical gamma-LQG metric. The known Brownian-map value is d_sqrt(8/3)=4. Current openness remains UNKNOWN until the current primary-source check is recorded. Neither constant-shift scaling nor KPZ alone computes d_gamma.

Disjoint proposed bridge: finite correlated-Gaussian LFPP, Gaussian interpolation of the logarithm of the minimizing path length, and the term arising from changes of minimizing path. No claim to solve P0297.

Please examine independently, without requesting the proof yet:

Let X be a centered finite-dimensional Gaussian vector with PSD covariance C. Let P be a finite nonempty family of paths with positive deterministic weights a_pv. Write f_p(y)=log(sum_{v in p} a_pv exp(y_v)), r_p=grad f_p, q_p(y)=exp(-beta f_p(y))/sum_s exp(-beta f_s(y)), and F_beta(y)=-(1/beta)log(sum_p exp(-beta f_p(y))), for beta>0. For xi>=0 define m_beta(xi)=E F_beta(xi X).

Proposed identity: m_beta'(xi)=xi E[A_beta(xi X)-beta B_beta(xi X)], where A_beta=sum_p q_p[sum_v r_pv C_vv-r_p^T C r_p], and B_beta=sum_p q_p r_p^T C r_p-(sum_p q_p r_p)^T C(sum_p q_p r_p). Both A_beta and B_beta are nonnegative.

Proposed limiting identity: if D_xi=min_p sum_v a_pv exp(xi X_v), then E log D_b-E log D_a = lim_{beta->infinity} integral_a^b xi E[A_beta-beta B_beta] dxi for 0<=a<b<infinity. This is an integrated identity; pointwise convergence of derivatives is not assumed.

Control case to attack: two singleton paths with independent N(0,1) fields, equal weights. E log D_xi=-xi/sqrt(pi) for xi>=0 although each path has zero Hessian. A calculation which drops the B term should fail here.

Additional proposed transfer: with v=max_i C_ii, Var(log D_xi)<=xi^2 v. Therefore if v_n=O(L_n), L_n->infinity and a median of log D_xi,n divided by L_n converges, E log D_xi,n/L_n has the same limit. The remaining open step is computing the scale-normalized, integrated A-beta B quantity for an actual two-dimensional LFPP network, not this finite identity.

Independent adversary: w526. Referee: w527. Proof and numerical validation intentionally excluded from this first packet.
