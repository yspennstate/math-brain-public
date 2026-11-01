# T348 The exact capacity of dense associative memories

Lead: unassigned. Dossier written 2026-10-16 by agent A from the row and the arXiv records below (abstracts read 16 Oct
08:3x, the 16 Oct 04:33 audit (status PARTLY) and worker L's note that typical and all-pattern thresholds differ).

## STATEMENT
Repaired statement (the audit: the row mixed discrete polynomial and exponential energies with the continuous log-sum-exp model, and
the typical-pattern threshold with all-pattern capacity): the continuous dense associative memory with log-sum-exp energy at fixed
inverse temperature beta, M = exp(alpha N) patterns i.i.d. uniform on the sphere of radius sqrt N (or i.i.d. Gaussian); prove the
all-pattern threshold alpha_c, closing alpha_lower <= alpha_c <= alpha_1 of Lucibello-Mezard, or prove the typical-pattern statement
(fixed point with a basin of stated radius iff alpha < alpha_1) under exact uniformity assumptions. The discrete polynomial and
exponential models (Demircigil et al.) are a separate question.

## FRONTIER
- Ramsauer et al. arXiv:2008.02217: modern Hopfield networks and attention.
- Demircigil, Heusel, Lowe, Upgang, Vermet arXiv:1702.01929: discrete exponential storage with error correction.
- Lucibello, Mezard arXiv:2304.14964: alpha_1 exact (typical pattern), lower bounds on alpha_c via a union bound, basins; Gaussian
  and spherical ensembles differ qualitatively.
- Open: the all-pattern alpha_c; a rigorous typical-pattern basin statement.

## ARCHITECTURE
Retrieval of pattern 1 is a random energy model question: the softmax weight on pattern 1 versus the sum over exp(alpha N) others,
whose overlaps with a point near pattern 1 are i.i.d. with a large-deviation rate I(q). The typical threshold alpha_1 is where the
maximum overlap among the others, at rate I(q) = alpha, competes with the self-overlap; the all-pattern capacity asks the same for the
worst of exp(alpha N) patterns, which adds the pairwise-overlap extremes among patterns.

## FAILURE POINT
The all-pattern problem needs the maximum over patterns of a REM-type quantity, with dependence through shared patterns; a union bound
gives alpha_lower, the second moment fails because of the dependence.

## SHAPE
Days: verify the fixed-state large-deviation computation behind alpha_1 and the union bound behind alpha_lower; identify the missing
uniform-in-neighbourhood step (the audit's DAYS target).

## OBSTRUCTION
Uniformity over the basin and over patterns. Moves: for the spherical ensemble, condition on the pattern Gram matrix's extremes (all
pairwise overlaps at most sqrt(4 alpha) asymptotically by a union bound) and reduce the all-pattern problem to a deterministic
stability condition given those extremes.

## TARGETS
1. Verify alpha_1 and alpha_lower for the spherical ensemble; state the missing uniform step.
2. Upper bound alpha_c <= alpha_1 rigorously (a typical pattern fails above alpha_1, so all-pattern fails).

## 19 Oct (agent A): Targets 1-2, spherical ensemble - the all-pattern threshold equals alpha_1, with an elementary proof and a uniform basin
CORRECTION to the repaired STATEMENT above: for SPHERICAL patterns Lucibello-Mezard do not leave a gap. Their union bound is tight
there: A(alpha, lambda) = +infinity for alpha < alpha_1 and 0 above, so alpha_c^lb = alpha_c = alpha_1 (Sec. III and App. C.2 of
arXiv:2304.14964v4, read 19 Oct in the HTML version). The gap alpha_c^lb < alpha_1 is a GAUSSIAN-ensemble statement (alpha_c^lb
saturates at log(2)/4 for lambda >= 0.70091 while alpha_1 = 1/2). Their argument is a large-deviation computation. What follows
is a short proof at the level of "a fixed point near every pattern, with a basin".

Model (their eq. 1, inverse temperature lambda fixed): E(x) = -(1/lambda) log sum_mu e^{lambda x.xi^mu} + |x|^2/2, update
T(x) = sum_mu a_mu(x) xi^mu with softmax weights a_mu proportional to e^{lambda x.xi^mu}. Patterns xi^1..xi^M are i.i.d. uniform on
the sphere of radius sqrt N, and M = e^{alpha N}.
Re-derived (19 Oct, independently of the paper): with I(t) = -(1/2) log(1 - t^2) the overlap rate on the sphere,
  phi_{alpha,1}(lambda) = sup_{t: I(t) <= alpha} [ t + (alpha - I(t))/lambda ]
                        = alpha/lambda + (s - 1 - log((1+s)/2))/(2 lambda),  s = sqrt(1 + 4 lambda^2)   (uncondensed, lambda < lambda_*)
                        = sqrt(1 - e^{-2 alpha})                                                       (condensed),
  lambda_* = e^{2 alpha} sqrt(1 - e^{-2 alpha})   (their eq. 53),
  alpha_1(lambda) = lambda - (s - 1 - log((1+s)/2))/2   (phi = 1; ~ (1/2) log lambda + 1/2 for large lambda).

THEOREM (spherical ensemble, fixed lambda > 0, alpha > 0). Let Phi_N = max_nu log( sum_{mu != nu} e^{lambda xi^nu . xi^mu} ) / (lambda N).
Then Phi_N -> Phi(alpha, lambda) := max( phi_{alpha,1}(lambda), sqrt(1 - e^{-4 alpha}) ) in probability.
COROLLARY. Since sqrt(1 - e^{-4 alpha}) < 1, Phi < 1 iff alpha < alpha_1(lambda). For alpha < alpha_1 and any rho < (1 - Phi)/2,
with probability -> 1, EVERY pattern nu has a fixed point within distance 2 sqrt(N) e^{-lambda N (1 - Phi - 2 rho - o(1))} of xi^nu,
and every x with |x - xi^nu| <= rho sqrt N lands within that distance after ONE update. For alpha > alpha_1, a typical pattern fails:
at x = xi^nu its own softmax weight is at most e^{-lambda N (phi - 1 - o(1))}, so T(xi^nu) is far from xi^nu. Hence alpha_c = alpha_1 exactly.

Proof sketch.
(1) Max pairwise overlap. P(some pair has overlap > tau) <= M^2 P(t > tau) = e^{N(2 alpha - I(tau)) + o(N)} -> 0 when
I(tau) > 2 alpha, i.e. tau > tau_2 := sqrt(1 - e^{-4 alpha}). A second moment on the pair count (pairs sharing one index are
independent given that index) gives the matching lower bound, so the max overlap -> tau_2.
(2) Cell counts, upper bound. Cut [-1, tau] into cells of width delta. Given xi^nu, the count in cell j is Binomial(M, p_j) with
p_j = e^{-N I(t_j) + o(N)}. Where alpha - I(t_j) > 0, Chernoff gives count <= 2 M p_j outside probability e^{-c e^{N(alpha - I)}}.
Where alpha - I(t_j) <= 0, count >= e^{eta N} has probability <= (e M p_j e^{-eta N})^{e^{eta N}}. Both are super-exponentially
small, so a union over the e^{alpha N} patterns nu and the finitely many cells costs nothing. On the intersection of these events
with (1),
  log Z_nu / (lambda N) <= sup_{t <= tau} [ t + max(alpha - I(t), eta)/lambda ] + delta + o(1)
                        =  max( phi_{alpha,1}(lambda), tau ) + eta/lambda + delta + o(1),
because the region I(t) > alpha contributes at most t <= tau. Let tau -> tau_2 and eta, delta -> 0.
(3) Lower bound. Z_nu >= e^{lambda N max over mu of the overlap} gives tau_2 - o(1) from the pair that attains (1). The cell
near the maximizer of the REM term holds at least M p_j / 2 points (Chernoff), which gives phi - o(1) for every nu.
(4) Fixed point. For |x - xi^nu| <= rho sqrt N: x.xi^nu >= N(1 - rho) and x.xi^mu <= xi^nu.xi^mu + rho N. So the total weight
off nu is at most e^{-lambda N (1 - Phi_N - 2 rho)}, and
  |T(x) - xi^nu| <= 2 sqrt(N) (1 - a_nu) <= 2 sqrt(N) e^{-lambda N (1 - Phi_N - 2 rho)}.
T therefore maps the ball into a tiny ball around xi^nu, and Brouwer gives a fixed point there. The Jacobian lambda Cov_a(xi) has
norm at most 4 lambda N (1 - a_nu), which is tiny, so the fixed point is unique in the ball and the iteration converges.
WHAT IS NOT SHARP: the basin radius rho < (1 - Phi)/2 is crude. Lucibello-Mezard's basin (cos theta_c, App. C.3) is a
typical-pattern computation, and the uniform-over-patterns version of THAT radius is still open. The proof does not transfer to
the Gaussian ensemble: there a pattern of atypically large norm dominates its neighbours' sums (the reason their gap is real).
NOVELTY: the statement is the paper's own physics claim (alpha_c = alpha_1 on the sphere), derived there through an auxiliary REM.
One extended web search on 19 Oct 06:0x found no rigorous proof for this model. arXiv:2604.12811 treats binary patterns with
polynomial energies and loads N^(n-1), and arXiv:2509.06905 a zero-temperature exponential model, so neither covers it. That is
one search, not a full check. The sharp margin formula max(phi, sqrt(1 - e^{-4 alpha})) was not seen in either paper.
NUMERICS (sph_check.py, sph_check_run1.txt). phi_hat_nu = log(sum_{mu != nu} e^{lambda xi^nu.xi^mu})/(lambda N). Memory is
capped before allocation, and the all-pattern max is taken only for M <= 30k (otherwise 2000 sampled nu).
  lambda alpha  phi_{a,1}  Phi(theory)  N: median phi_hat / max phi_hat / failing
  1      0.3    0.677      0.836        20: 0.659/0.801/0   30: 0.666/0.854/0   34: 0.668/0.812/0   40: 0.670/0.745/0 (sampled)
  1      0.5    0.877      0.930        14: 0.877/0.975/0   18: 0.880/0.942/0   20: 0.880/0.931/0   24: 0.880/0.908/0 (sampled)
  1      0.7    1.077      1.077        10: 1.085/1.140/all 12: 1.083/1.120/all 14: 1.083/1.108/all 17: 1.082/1.092/all (sampled)
  3      0.9    0.936      0.986        8: 0.946/1.012/5    10: 0.945/1.011/2   11: 0.944/0.997/0   13: 0.943/0.975/0 (sampled)
The median goes to phi_{alpha,1}. The all-pattern max follows the largest pairwise overlap (0.854 against 0.854 at N = 30): the
worst pattern is the one with the nearest neighbour, which is the mechanism of step (2). Above alpha_1 every pattern fails. Just
below alpha_1, with Phi = 0.986, a few patterns fail at N <= 10 and none from N = 11 on.
STATUS of the TARGETS: 1 done (alpha_1 re-derived and checked; alpha_lower = alpha_1 on the sphere, as the paper states).
2 done for the spherical ensemble in the fixed-point-near-every-pattern sense, with a crude uniform basin. Still open: the sharp
uniform basin, and the Gaussian ensemble's alpha_c in (log(2)/4, 1/2) at large lambda.
RIGOR NOTE (21 Oct, agent C, after the worker W literature review): Lucibello-Mezard describe their results as "obtained through partially non-rigorous arguments" (arXiv:2304.14964v4, Sec. V). The spherical equality above is their physics-level claim; the proof here is the rigorous version on record, with one audit (AUDIT_agent_C.md). A second independent audit of steps (2)-(3) is the next step.
