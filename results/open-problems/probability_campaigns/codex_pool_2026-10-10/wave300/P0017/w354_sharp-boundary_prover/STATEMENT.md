# Independent statement packet: P0017, w354

For every integer d>=1 and every log-concave probability mu on R^d with mean zero and Cov(mu)=I_d, seek an absolute C<infinity such that every locally Lipschitz f in L^2(mu) with finite gradient energy satisfies Var_mu(f)<=C integral |grad f|^2 dmu. Equivalently, in full-dimensional nonisotropic coordinates, C_P(mu)<=C ||Cov(mu)||_op. The covariance operator norm is also a lower bound, by linear test functions.

Cheeger convention: h(mu)=inf_A mu^+(A)/min(mu(A),1-mu(A)), where mu^+ is outer Euclidean Minkowski perimeter. The corresponding target is a positive universal lower bound for h in isotropic position. Numerical constants between Poincare and Cheeger formulations need not match.

Primary target recovery: Bizeul, Klartag and Lehec, arXiv:2610.05474v1 (4 Oct 2026), Theorem 1.1 and equations (5)-(6), https://arxiv.org/html/2610.05474v1. Original geometric source: Kannan, Lovasz and Simonovits (1995), https://www.renyi.hu/~miki/KannanLovSimIso.pdf.

Current-status caution: the October primary literature explicitly claims a proof of the full target. This packet does not audit that proof or assert current openness. The September ranking is stale evidence for that question.

Boundary claim reserved for this lane, stated without its proof: there is an explicit isotropic uniform d-simplex, d>=2, and an edge-parallel unit direction v for which ess sup_z C_P(Law(<v,Y>|Proj_{v-perp}Y=z))=2(d+1)(d+2)/pi^2, even though the average conditional constant is 12/pi^2. Test the proposed uniform conditional bound independently. This is an obstruction to an auxiliary bridge, not to KLS.

Independent adversary: w355. Referee: w356. Full proof follows separately.
