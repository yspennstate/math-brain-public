from pathlib import Path
s=r'''

## 5. Upper-count conditioning: an actual replica theorem for the local surrogate

The source's phi_K conditions the INITIAL OCCUPIED COUNT, whereas Theorems A/B were first proved under product bits. Conditioning cannot simply preserve a dependency graph. We can nevertheless handle it by a joint Gaussian limit, instead of making that false independence assumption.

**Corollary C.** Keep Theorem B's assumptions, and fix K>=0 and a real a. Let M be the INITIAL VACANT count, and put

  U_n={M<nq_n-K sqrt(n)},
  T_n=(H_t-n h_t(q_n))/sqrt(n sigma_t(q_n)^2).

Then Q_G=P(T_n<=a | G,U_n) concentrates in graph probability around a deterministic sequence c_n(a). In particular Var_G Q_G->0, so for two independent initial sets sampled conditionally on G and U_n,

  P(T_n<=a,T'_n<=a)-P(T_n<=a)^2 -> 0.                  (D1)

This is the same conditional-count replica structure as the missing criterion, but with a LOCAL VACANCY COUNT CDF in place of FINAL SUCCESS. It does not prove the missing criterion for F.

Proof. Differentiation of a finite Bernoulli expectation gives the exact identity

  Cov(H_t,M|G)=q_n(1-q_n) d/dq E_q(H_t|G) at q=q_n.      (D2)

To see it, differentiation multiplies each configuration weight by [M-nq]/[q(1-q)], so the derivative is Cov(H_t,M)/[q(1-q)]. A local survival indicator is increasing in at most S_t bits, so its derivative lies between 0 and S_t. At vertices with tree balls that derivative is h'_t(q); other vertices change the derivative by at most 2S_t. Thus

  |d/dq E_q(H_t|G)-n h'_t(q)|<=2S_t B_t.               (D3)

For any finite t,q, the limit of conditional Cauchy-Schwarz on the typical graphs of Theorem A shows

  0<=rho_t(q):=sqrt(q(1-q)) h'_t(q)/sigma_t(q)<=1.       (D4)

This yields a valid deterministic Gaussian covariance parameter for every t, including the subsequently chosen t_n. There is no assumption of its convergence as t grows.

Apply the dependency-graph moment argument to fixed linear combinations of the two local variables (Y_v-EY_v)/sigma_t(q_n) and (Z_v-q_n)/sqrt(q_n(1-q_n)). Their per-vertex magnitudes are n^{o(1)} under (C1), and the dependency degree is still D=n^{o(1)}. The moment-counting errors gain at most n^{o(1)} factors, so after sqrt(n) normalization still vanish: odd orders have error n^{-1/2+o(1)}, and even non-pair terms n^{-1+o(1)}. By (C5), (D2), and (D3), the limiting covariance matrix along any subsequence on which rho_t(q_n)->rho is [[1,rho],[rho,1]]. A linear combination with limiting variance zero tends to zero by Chebyshev; combinations with positive limiting variance have the Gaussian moment limit. Cramer-Wold therefore gives the conditional joint Gaussian limit of

  (T_n, (M-nq_n)/sqrt(nq_n(1-q_n)))

along every such subsequence. Its centering errors vanish as in (C5). If q_n does not converge, additionally pass to a compactness subsequence q_n->q; all prior bounds were uniform on [c,1-c].

Let b_n=-K/sqrt(q_n(1-q_n)), and let (N_1,N_2) be standard Gaussians of correlation rho_t(q_n). Define

  c_n(a)=P(N_1<=a,N_2<b_n)/Phi(b_n).                   (D5)

The denominator is bounded away from zero uniformly in n. The actual denominator P(U_n|G) is deterministic in G, since M is binomial, and converges to Phi(b) on each compactness subsequence by the binomial CLT. Gaussian marginal distributions have no atoms, even if rho=1 and the joint distribution is degenerate; thus the rectangle boundary at T=a or M=b has probability zero. The joint conditional CLT gives Q_G-c_n(a)->0 in graph probability along every subsequence, hence for the full sequence (otherwise extract a contradicting compactness subsequence in q_n and rho_t(q_n)). The Gaussian rectangle probabilities in (D5) are continuous in q and rho, including rho=1, by representing N_1=rho N_2+sqrt(1-rho^2)N_0 and using the zero boundary probabilities.

Since Q_G,c_n(a) lie in [0,1], convergence in probability of their difference implies convergence in L2, and Var_G Q_G<=E[(Q_G-c_n(a))^2]->0. Conditional independence of the two U-conditioned seed sets gives (D1) by the same exact variance identity as ATTEMPT.md equation (5). End proof.

This proof explicitly conditions via a two-dimensional limit; it never treats the U-conditioned vertex bits as independent. At occupied density p_n=1-q_n, U_n is exactly the source's upper-count event |A|>np_n+K sqrt(n). The finite-time completion event H_t=0 still has probability tending to zero under this conditioning: divide its unconditioned probability by the binomial tail probability, which is bounded away from zero. At the critical density, final conditional success may instead be close to one for large K. The local surrogate's conditional replica concentration therefore cannot be substituted for concentration of final occupation.
'''
p=Path('SECOND_ATTEMPT.md');p.write_text(p.read_text(encoding='utf8')+s,encoding='utf8')
