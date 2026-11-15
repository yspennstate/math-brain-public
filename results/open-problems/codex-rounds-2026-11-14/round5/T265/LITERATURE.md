# Bounded literature check

Search conducted on 15 November 2026, approximately 09:02–09:04
Asia/Tbilisi. Queries combined benign overfitting, two-layer ReLU,
non-orthogonality, n >= d, 2026, and arXiv:2505.16204. No verified
resolution of the whole T265 question was identified. This bounded
search is not an exhaustive literature survey.

Ichiro Hashimoto, *Directional Convergence, Benign Overfitting of
Gradient Descent in leaky ReLU two-layer Neural Networks*,
[arXiv:2505.16204v3](https://arxiv.org/abs/2505.16204v3), revised
10 February 2026. Opened the arXiv page and
[full HTML](https://arxiv.org/html/2505.16204v3), including Assumption
6.1 and Theorem 6.2. The work proves directional convergence and
classification bounds for fixed-width leaky ReLU networks on mixture
data under its sufficient conditions. Assumption 6.1(a) includes
tr(Sigma) >= C n ||Sigma||_F, and 6.1(b) includes
tr(Sigma) >= C n ||Sigma||. For nonzero positive semidefinite covariance
in ambient dimension d, tr(Sigma) <= sqrt(d)||Sigma||_F and
tr(Sigma) <= d||Sigma||. These imply respectively d >= C^2 n^2
and d >= C n. Thus these probabilistic sufficient conditions do not
cover n/d tending to infinity. This dimensional conclusion is a direct
inference from the displayed assumptions, not a restriction asserted
for all its deterministic theorems.

Kedar Karhadkar, Erin George, Michael Murray, Guido Montúfar, Deanna
Needell, *Benign overfitting in leaky ReLU networks with moderate input
dimension*, [arXiv:2403.06903v3](https://arxiv.org/abs/2403.06903v3),
revised 2 October 2024. Opened the arXiv page. Its abstract treats
two-layer leaky ReLU networks trained by GD with hinge loss, and
explicitly states a dimension requirement d=Omega(n). It does not
provide a theorem for n/d tending to infinity or for the ReLU model
in T265.

Secondary search results were used only to locate candidates. No
mathematical claim from an unopened paper is used in this session.
