# T352: the published convergent bounds for nonconvex noisy SGD do not decrease with n

agent B, 19 Oct 2026. Status: the Chien-Li floor is a CANDIDATE with one audit CONFIRMED (agent A, lam < 1 fix below), second audit pending. The row's question itself is answered by 2401.10371 (section below). Answers the dossier's target 1 and adds the literature it
did not list.

## Setting

Projected full-batch noisy gradient descent on a domain of diameter D, per-example losses K-Lipschitz (or clipped at
K), step eta, Gaussian noise of variance sigma^2, last iterate released. One record changes the averaged gradient by at most
2K/n, so the per-step Renyi cost is alpha (2 eta K/n)^2 / (2 sigma^2). In the convex case the time-uniform plateau is of
order alpha eta K D / (n sigma^2) (Altschuler-Talwar 2205.13710), which decreases like 1/n.

## Result: Chien-Li's limit has an n-free floor

Chien, Li arXiv:2410.01068 v2, Theorem 3.7 (full batch, (L, lam)-Holder gradient), as read on 19 Oct 2026 from
arxiv.org/html/2410.01068v2:
  eps(alpha) <= min alpha/(2 sigma^2) sum_{t=tau}^{T-1} [ (2 eta K/n)^2 / beta_t + a_t^2 / (1 - beta_t) ],
  A_T = 0, A_{t-1} = h(A_t + a_{t-1}), A_tau >= D_tau, h = g^{-1}, g(x) = x + eta L x^lam,
  D_t = min(g(D_{t-1}) + 2 eta K/n, D_{t-1} + 2 eta K, D).

Claim. For every n, lim_{T -> inf} of the right-hand side is at least
  alpha D^2 (2 eta L D^{lam-1} + eta^2 L^2 D^{2 lam - 2}) / (2 sigma^2),
which for lam = 1 is alpha D^2 (2 eta L + eta^2 L^2) / (2 sigma^2).

Proof. Minimising over beta_t gives the per-step cost (c + a_t)^2 >= a_t^2, with c = 2 eta K/n. As T -> inf, any tau with
a finite sum has T - tau finite, so D_tau = D, the cap (D_t grows by at least c per step until it reaches D). For lam = 1,
h(z) = r z with r = 1/(1 + eta L), so A_tau = sum_{j>=1} r^j a_{tau+j-1} >= D, and Cauchy-Schwarz gives
sum a^2 >= D^2 / sum_j r^{2j} > D^2 (1 - r^2)/r^2 = D^2 (2 eta L + eta^2 L^2). For lam < 1, write L' = L D^{lam-1}; then
x^lam >= x D^{lam-1} on [0, D], so g_lam >= g_1' there (g_1' the lam = 1 map with L'). The comparison holds only on [0, D],
so first reduce the path: given a feasible (tau, a), let t' be the last t >= tau with A_t >= D. Dropping the terms before t'
keeps the path feasible and lowers the cost, and lowering a_{t'} until A_{t'} = D lowers it again (all a_t >= 0). On the
reduced path every A_t lies in [0, D]. By induction from A_T = 0 the lam = 1 recursion with L' and the same a's gives
A'_t >= A_t: z = A_t + a_t = g_lam(A_{t-1}) >= g_1'(A_{t-1}), so h_1'(z) >= A_{t-1}, and h_1' is increasing. So every
feasible lam < 1 path is feasible for lam = 1 with L', and the floor follows. QED. (The lam < 1 reduction was supplied by
the audit of agent A, AUDIT_T352_agent_A.md.)

Onset. Each step costs at least c^2, so a window of length T - tau costs at least (T - tau) c^2, and D_t reaches D after
about log(1 + eta L D/c)/(eta L) steps. The floor is n-free in value; it is reached after about log(n)/(eta L) steps.

Numerical check (cl_floor.py, cl_floor.txt; eta 0.01, L = K = D = 1, in units of alpha/(2 sigma^2)). The lam = 1 column solves
the KKT conditions exactly for each window length N; the lam = 1/2 column uses Dijkstra on a 1,500-point grid, which gives an
upper estimate.

    n       lam = 1     lam = 1/2    convex scale 4 c D
    10      2.814e-2    3.481e-2     8.0e-3
    1e3     2.018e-2    2.685e-2     8.0e-5
    1e6     2.0100e-2   2.677e-2     8.0e-8
    floor   2.0100e-2   >= 2.0100e-2

So the bound improves on the last-step bound alpha D^2/(2 sigma^2) by a factor of about 2 eta L, but it never decreases
with n. This is a statement about the bound, not about the true privacy loss.

## The other two published bounds (read 19 Oct 2026)

- Liang, Zhang, He, Wu, Xing arXiv:2502.17772 v4, Thm 3.4 / B.3 (smooth nonconvex, bounded domain):
  eps = O(alpha C^2/(n^2 sigma^2) min{T, (1 + eta L)^2 n^2 D^2/(eta^2 C^2)}), whose limit O(alpha (1/eta + L)^2 D^2/sigma^2)
  is n-free. (The excerpt's eq. 51 has a term 2 alpha C^2/(beta n b sigma^2) that would decay; the final O-form drops it.
  Not resolved.)
- Asoodeh, Diaz arXiv:2305.09903, Thm 2 (no convexity, no smoothness): delta_inf = p theta/(1 - (1-p) theta) with p = b/n and
  theta = theta_eps((D + 2 eta C)/sigma). n enters only through the sampling rate. At full batch (p = 1), delta_inf = theta,
  which is n-free.

So none of these three gives a time-uniform nonconvex bound that decreases with n. That answers dossier target 1.

## The row's question is answered in the literature: Chien, Wang, Chen, Li, Langevin Unlearning (arXiv:2401.10371, NeurIPS 2024)

Read 19 Oct 2026 21:5x from arxiv.org/html/2401.10371v7, section 3.2. Projected noisy GD x_{t+1} = Pi_{C_R}(x_t - eta grad f_D(x_t)
+ sqrt(2 eta sigma^2) W_t) on a ball of radius R, every loss L-smooth and M-Lipschitz, no convexity. Their Theorem 3.3 gives
  eps_0 <= (2 alpha eta S^2 M^2/(sigma^2 n^2)) sum_{t<T} prod_{t'=t}^{T-1} (1 + eta sigma^2/C_{t',1})^{-1},
with the LSI constants capped by C-bar = 6(4(R + eta M)^2 + eta sigma^2) exp(4(R + eta M)^2/(eta sigma^2)) for every t. The
sum is then a geometric series with ratio below 1, so the limit is O(alpha eta M^2/(sigma^2 n^2)) times a T-free constant
(they write 2 alpha eta S^2 M^2/(sigma^2 n^2 c)). That is the 1/n^2 plateau the row asks for, for every smooth Lipschitz loss
on a ball. The constant is exponential in R^2/(eta sigma^2) and does not depend on the dimension. The row's main question
is therefore settled by an existing theorem. The dossier's target 2 (a smooth nonconvex example whose plateau does not
decrease in n) is false for fixed R, eta, sigma, M as n -> infinity. A double well can only keep the loss large while
n stays below about the exponential constant.

Our earlier line "the row's 1/n question is confirmed open" (19 Oct 21:0x) was wrong: the literature search covered the
privacy-amplification papers and missed the unlearning paper, which proves the learning-phase bound on the way to its
main result.

## A short alternative proof without smoothness (candidate, ours): Doeblin on the torus

Torus T = (R/DZ)^d, x_{t+1} = phi_S(x_t) + xi_t mod D, phi_S(x) = x - eta grad F_S(x), xi ~ N(0, s^2 I), and
sup_x |grad F_S(x) - grad F_S'(x)| <= 2K/n (no smoothness, no convexity). Let k be the wrapped Gaussian density, m = min k,
M = max k, gamma = m D^d, delta = 2 eta K/n, beta = delta sqrt(2/pi)/s, beta_inf = delta ||grad k||_inf. Same start mu_0.

  (i)  u_t = ||mu_t - mu'_t||_1 satisfies u_{t+1} <= (1 - gamma) u_t + beta, so u_t <= beta min(t, 1/gamma).
       mu_{t+1} - mu'_{t+1} = (mu_t - mu'_t) P_S + mu'_t (P_S - P_S'); the first term contracts by the Dobrushin coefficient
       1 - gamma (P_S(x, .) >= m Leb = gamma Unif), the second is at most sup_x ||k(. - a) - k(. - b)||_1 with |a - b| <= delta,
       which is at most twice the Gaussian TV, 2(2 Phi(delta/(2s)) - 1) <= beta.
  (ii) w_{t+1} = sup |f_{t+1} - f'_{t+1}| <= (M - m)/2 u_t + beta_inf: the first term is int k(y - phi(x)) d(mu_t - mu'_t)(x),
       a zero-mass measure against a function with values in [m, M].
  (iii) f'_t >= m for t >= 1, so chi2(f_T || f'_T) <= w_T u_T/m, and D_alpha <= (alpha/2)(1 + rho)^{alpha-2} chi2 for alpha >= 2,
       rho = w_T/m (Taylor with remainder, E_{f'}[f/f'] = 1).
So chi2 <= (beta/m) min(T, 1/gamma) [(M - m)/2 beta min(T-1, 1/gamma) + delta ||grad k||_inf] = O(eta^2 K^2/(n^2 s^2)) with a
T-free constant: the 1/n^2 plateau, with the min(T, .) shape of the convex result. Against 2401.10371: no smoothness is used
and, against their ball of radius D/2 with s^2 = 2 eta sigma^2, the exponent is milder when d < 16 (gamma ~ exp(-d D^2/(8 s^2)) on the torus; on a projected box the same argument with the two
boundary atoms counted in the reference measure gives exp(-d D^2/(2 s^2))), but the constant is exponential in the dimension d,
where theirs is dimension-free. A modest variant, not a new answer.

Numerical check (doeblin_torus_check.py, circle, A cos(2 pi x/D) loss, neighbour flips one record, Nystrom on 800 points,
D 1, s 0.3, eta 0.1, A 0.5, x0 = 0): n^2 D_2 = 1.1e-4, 8.0e-3, 9.42e-3, 9.56e-3 at n = 10, 1e2, 1e3, 1e4 (plateau from t = 10,
unchanged to t = 2000), so D_2 ~ 9.6e-3/n^2; the chi2 bound holds with a factor of about 10^3-10^4 to spare. The small-noise run
(doeblin_torus_meta.txt: s 0.12, eta 0.05, 1,000 points, gamma 1.13e-3, to t = 40,000): n^2 D_2 = 0.818, 0.523, 0.497, 0.494 at
n = 10, 1e2, 1e3, 1e4, flat from t = 100, so again D_2 ~ 0.49/n^2. The bound is valid but loose by about 10^9 there, as the
one-step Doeblin constant predicts.

## Earlier route notes (kept as written; superseded by the two sections above)

## Why the dossier's target 2 (an n-free plateau) looks false, and a route

1. Gibbs heuristic. For small eta the chain is close to Langevin at temperature sigma^2/(2 eta), with stationary density
   proportional to exp(-2 eta F/sigma^2). One record moves F by at most 2KD/n in oscillation, so the stationary laws'
   log-ratio is at most 4 eta K D/(n sigma^2), which decreases like 1/n.
2. An exact unstable example. Take F = -(L/2) x^2 with no projection and a record tilt +-K x/n, started at 0. The iterate is
   Gaussian with mean (eta K/n)(c^k - 1)/(c - 1) and variance sigma^2 (c^{2k} - 1)/(c^2 - 1), c = 1 + eta L, so the Renyi
   divergence 2 alpha m^2/v tends to 2 alpha eta K^2 (2 + eta L)/(n^2 L sigma^2) ~ 4 alpha eta K^2/(n^2 L sigma^2).
   Expansion amplifies the signal and the noise equally, and the result decays like 1/n^2. (The example has no projection,
   so it sits outside the compact setting; it shows that expansion alone does not remove the n-decay.)
3. Route: Doeblin. On a torus of side D (compact, no boundary), the law of x_{k+1} = phi(x_k) + xi is (phi_# mu) * the
   wrapped Gaussian. After one step its density lies between the kernel's min m and max M, for ANY loss and any data. This
   is a Doeblin minorisation with constant gamma = m D^d, so the kernel contracts every f-divergence by at most 1 - gamma.
   Combining that contraction with the per-step sensitivity 2 eta K/n is the missing step. Asoodeh-Diaz combine the
   contraction with a worst-case step, which is why their full-batch limit is n-free. Expected answer: a plateau of order
   alpha (eta K/n)^2/(sigma^2 gamma), decreasing like 1/n^2, with a constant exponential in D^2/sigma^2.
   Next: the hockey-stick or Renyi recursion delta_{t+1} <= (1 - gamma) delta_t + (step term at sensitivity 2 eta K/n), with
   eps budgets split geometrically, and then the projected interval, where the projection puts atoms on the boundary.
