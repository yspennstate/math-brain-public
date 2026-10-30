# T348 spherical theorem (DOSSIER.md, 19 Oct section), audit 1 (agent C, 20 Oct 2026 02:04)

Object: the THEOREM, COROLLARY and proof sketch (1)-(4) of agent A's 19 Oct section, and its numerics table.

Verdict: CONFIRMED, with one step to fill in (the failure above alpha_1, below). No error found.

## Checked line by line

- Overlap law. Given xi^nu, the overlap t of an independent uniform point on the sphere of radius sqrt N has density
  proportional to (1-t^2)^{(N-3)/2}, so the rate is I(t) = -(1/2) log(1 - t^2). Correct.
- phi_{alpha,1}. The stationary point of t + (alpha - I(t))/lambda solves t/(1-t^2) = lambda, so t* = (s-1)/(2 lambda) and
  1 - t*^2 = t*/lambda = 2/(1+s), using s^2 - 1 = 4 lambda^2. The value is alpha/lambda + (s - 1 - log((1+s)/2))/(2 lambda).
  I(t*) <= alpha iff (1+s)/2 <= e^{2 alpha}, which is iff lambda <= e^{2 alpha} sqrt(1 - e^{-2 alpha}) = lambda_*. Beyond that the
  sup sits at I(t) = alpha, which gives sqrt(1 - e^{-2 alpha}). alpha_1 solves phi = 1 in the uncondensed branch. The condensed
  value is below 1 for every alpha, so the crossing is always uncondensed. All re-derived.
  Brute-force sup on a 2e6-point grid against the closed forms at 49 (lambda, alpha) pairs, lambda 0.2 to 10, both branches:
  max difference 6.0e-7, the grid's resolution (audit_C/phi_closed_form_check.py, phi_closed_form_check.txt).
- (1) Max pairwise overlap -> tau_2 = sqrt(1 - e^{-4 alpha}). The first moment is right. For the second moment: the overlaps
  of (1,2) and (1,3) are independent, because given xi^1 each is a function of an independent uniform point, and the law of
  t_12 does not depend on xi^1. Pairs sharing an index are therefore independent, Var(count) <= E(count), and Chebyshev
  closes it. Correct.
- (2) Cell counts. Where alpha > I, the lower and upper Chernoff tails are exp(-c e^{N(alpha - I)}). Where alpha <= I,
  P(count >= k) <= C(M,k) p^k <= (e M p / k)^k with k = e^{eta N}. Both are super-exponentially small, so the union over the
  e^{alpha N} choices of nu is free. A cell straddling I = alpha must be put in the class its endpoint rates allow; this
  is bookkeeping only. The bound sup_{t <= tau}[t + max(alpha - I, eta)/lambda] <= max(phi, tau) + eta/lambda holds. The
  dossier writes "=", but only "<=" is needed. Correct.
- (3) The lower bound uses the Chernoff lower tail in the cell at the maximiser. In the condensed case, take a cell just
  inside I < alpha. The union over nu again costs nothing, so the bound holds for every nu, not only the max. Correct.
- (4) x.xi^nu >= N(1-rho), and x.xi^mu <= xi^nu.xi^mu + rho N, so 1 - a_nu <= e^{-lambda N (1 - Phi_N - 2 rho)} and
  |T(x) - xi^nu| <= 2 sqrt N (1 - a_nu). Brouwer then applies on the closed ball. The Jacobian constant is exact: DT = lambda
  Cov_a(xi), and Cov_a = (1/2) sum a_mu a_mu' (xi^mu - xi^mu')(.)^T has norm <= 2N (1 - sum a^2) <= 2N (1 - a_nu^2) <= 4N (1 - a_nu).
  So ||DT|| <= 4 lambda N (1 - a_nu), as written. The ball is convex, so T is a contraction there, the fixed point is unique
  and the iteration converges. Correct.

## The step to fill in: no fixed point near a pattern above alpha_1

The sketch only shows T(xi^nu) is far from xi^nu. On its own, that does not rule out a fixed point at distance eps sqrt N.
The complete argument: take alpha > alpha_1, so by (3) every nu has phi_nu := log Z_nu/(lambda N) >= phi - o(1) > 1, and fix
eps < min((phi - 1)/2, (1 - tau_2)/2). For |x - xi^nu| <= eps sqrt N,
  a_nu <= e^{lambda N (1 + eps)} / (e^{-lambda eps N} Z_nu) = e^{-lambda N (phi_nu - 1 - 2 eps)} -> 0,
  T(x).xi^nu / N = a_nu + sum_{mu != nu} a_mu t_{nu mu} <= a_nu + tau_2 + o(1) < 1 - eps <= x.xi^nu / N.
So T(x) != x anywhere in that ball, for EVERY pattern (not only a typical one). This matches the numerics' "all" rows. With
this step the corollary's "alpha_c = alpha_1 exactly" holds in the sense: (fixed point within eps sqrt N of every
pattern) iff alpha < alpha_1.

## Numerics table

phi and Phi re-computed from the closed forms at (1, 0.3), (1, 0.5), (1, 0.7) and (3, 0.9): 0.677/0.836, 0.877/0.930,
1.077/1.077 and 0.936/0.986. Those are the dossier's values. lambda_*(0.3) = 1.224 > 1 and lambda_*(0.9) = 5.527 > 3, so
the uncondensed branch is the right one for each. I did not re-run sph_check.py. The table's trend (the median goes to phi,
and the worst pattern follows the nearest neighbour) is what (1)-(3) predict.

## Not covered

The novelty claim (one extended search, as the dossier says), the sharp uniform basin, and the Gaussian ensemble. A second
independent audit is still needed before the memory moves to verified.
