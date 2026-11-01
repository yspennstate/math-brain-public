# P0297 referee attempt — 2026-10-10

## Exact target

For fixed $\gamma\in(0,2)$, determine the almost-sure Hausdorff dimension $d_\gamma$ of the canonical $\gamma$-LQG metric $D_h$ on the plane. Gwynne–Miller, [Problem 7.1](https://arxiv.org/html/1905.00383v3), gives this formulation, with $d_{\sqrt{8/3}}=4$ and $\xi=\gamma/d_\gamma$. Gwynne–Pfeffer, [Corollary 1.7](https://arxiv.org/html/1905.11790v3), identifies the preexisting exponent with metric Hausdorff dimension. A [2025 primary paper](https://arxiv.org/html/2510.26123v1) still says the other values are unknown. I did not complete a 2026 literature audit; current openness is UNKNOWN.

## Brain-assisted proof need and returned-card check

The personal brain query `P0297 Liouville quantum gravity proof mistakes` returned eight unrelated quantum memories and explicitly reported no memory containing P0297. The math-brain CLI first crashed because Python imported the older `math-research-brain` package, whose `NodeKind` lacks `external_reference`, against a store with 177 nodes of that kind. After putting `math-brain-build/src` first on `sys.path`, recall returned the P0297 problem card at rank 1 and its prior attempt at rank 3; none of the top five was the metric KPZ theorem requested by the query. Commands and results are in SOURCE_STATUS.json.

The existing problem card asks for the dimension, and the existing attempt card derives the constant-shift relation $\xi d_\gamma=\gamma$ but does not determine $\xi$. The missing proof input is an evaluated metric/LFPP normalization exponent, equivalently a quantitative limit for a route-sensitive response. The 2018 Ding–Gwynne paper's old expectation that its exponent equals metric Hausdorff dimension is already established by the later Gwynne–Pfeffer paper; that identification is not the remaining gap.

Gwynne–Pfeffer Theorem 1.4 relates Euclidean and $D_h$ dimensions **only** for a deterministic Borel set or a random Borel set independent of $h$. The proof need involves field-dependent thick points or geodesics, so the independence condition fails. I independently checked w526's two obstructions: $T_h^\gamma$ has dimensions $(2-\gamma^2/2,d_\gamma)$ but naive substitution predicts 2; at $\gamma=\sqrt{8/3}$ a geodesic would be assigned Euclidean dimension $3/4$ despite its connected nonconstant image having dimension at least 1. Neither theorem application evaluates $d_\gamma$.

## Finite bridge checked

I rederived w525's soft-min Gaussian identity for finite positive weighted paths and arbitrary PSD covariance:

$$\frac{d}{d\xi}E F_\beta(\xi X)=\xi E[A_\beta(\xi X)-\beta B_\beta(\xi X)].$$

Here $A_\beta$ is the nonnegative within-route covariance term and $B_\beta$ the nonnegative between-route covariance term, as fully defined in w525/ATTEMPT.md. The Hessian of each log path cost is $\operatorname{diag}(r_p)-r_pr_p^T$; differentiating the soft-min weights adds $-\beta\operatorname{Cov}_q(r_p)$. Gaussian integration by parts then gives the identity. The uniform fixed-network error is $\log K/\beta$, so integrate before taking the hard-min limit. A two-route example has $A_\beta=0$ and derivative $-1/\sqrt\pi$; $\beta B_\beta$ survives route ties. Dropping it is wrong.

Gaussian Poincaré gives $\operatorname{Var}(\log D_\xi)\le\xi^2\max_i C_{ii}$, transferring an existing median exponent to a mean exponent when the diagonal variance grows as $O(\log(1/\varepsilon))$. The finite comparison $A_\beta\le\max_i C_{ii}$ recovers the known $\lambda(b)-\lambda(a)\ge-(b^2-a^2)/2$ if the covariance normalization tends to one. These are exact finite/conditional statements, not a value of $d_\gamma$.

w526's C526.5 shows endpoint soft-min bias can survive as the network grows, although that example's bias cancels in a difference. I independently checked C526.6: its two-group Gaussian family makes the **integrated endpoint** hard-min limit 1 and soft-min limit $1-\log2$ even with $\beta_n\to\infty$ and diagonal variance $O(L_n)$. Therefore the condition $\log K_n/(\beta_nL_n)\to0$ (or a proved effective-entropy substitute) is essential to the conditional bridge. The example is abstract, not a planar LFPP discretization.

## Refuted route and status

The old intake attempt D0049-A001 wrote $d_\gamma=2Q/\xi$. At the Brownian parameter, $Q=5/\sqrt6$ and $\xi=1/\sqrt6$, which makes that expression 10 while $d_\gamma=4$. A correction concept and exact edge to the existing P0297 card were submitted as a draft. It is not yet ingested or retrievable.

The single hardest open piece is evaluating the scale-normalized signed response $L_n^{-1}\int_a^b\xi E[A_{n,\beta_n}-\beta_n B_{n,\beta_n}]d\xi$ for the actual planar LFPP crossing model, with its network-to-continuum comparison and uniform smoothing error proved. No exact dimension, new LQG bound, or novelty claim follows from this work.

NEXT: For a specified circle-average planar LFPP crossing discretization, prove a nontrivial bound on the normalized route-switch term over one fixed interval $0<a<b$, with $\log K_n/(\beta_nL_n)\to0$ explicitly controlled.
