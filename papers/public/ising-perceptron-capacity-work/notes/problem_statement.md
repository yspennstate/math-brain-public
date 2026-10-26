# The capacity of the Ising perceptron: proof target and literature baseline

Working notes, started 2026-07-07.

## The conjecture

Krauth and Mezard (J. Physique 50, 1989) predicted via the replica method that the
storage capacity M_N/N of the Ising perceptron (x in {-1,+1}^N, M random half-space
constraints <g^a, x>/sqrt(N) >= 0, g^a iid standard gaussian) converges in probability
to an explicit constant alpha_* ~ 0.83307860. This had remained open since 1989. It is the
canonical capacity question for a binary neural network and one of the oldest
outstanding predictions of the replica method.

## Published status before this work (updated 2026-07-13)

- Ding and Sun, *Capacity lower bound for the Ising perceptron*, Probab. Theory
  Relat. Fields 193 (2025), 627--715, DOI 10.1007/s00440-025-01364-x
  (conference version STOC 2019; arXiv:1809.07742): lower bound. For
  alpha < alpha_*, solutions exist with probability bounded away from zero,
  SUBJECT TO their full Condition 1.2: the explicit univariate function
  SE_*(lambda) is < 0 for lambda not in {0,1}, SE_*''(0) < 0, and
  lim_{lambda -> 1-} SE_*'(lambda) > 0. Their sections 8--10 reduce the global
  sign clause to finitely many numerical integrations plus a grid computation,
  but several inputs use nonrigorous numerical integration. The final journal
  version retains the condition as a hypothesis.

- Xu (2021) and Nakajima-Sun (2023): the capacity has a sharp threshold sequence,
  and it is universal in the disorder (subgaussian, includes the original +-1
  Bernoulli disorder of Krauth-Mezard). This upgrades the Ding-Sun positive
  probability lower bound to high probability, unconditionally on their end.

- Huang (FOCS 2024, arXiv:2404.18902; v2 of 2025-04-22): matching upper bound.
  For alpha > alpha_*, no solutions with high probability, SUBJECT TO his
  Condition 1.3 (source label con:2varfn): the explicit two-variable function
  S_*(lambda_1, lambda_2) defined in eq:def-sS-star satisfies S_* <= 0 on all of
  R^2. His v2 appendix verifies, by rigorous interval arithmetic in python-flint,
  every OTHER numerical condition of his general theorem at kappa = 0
  (con:km-well-defd via Ding-Sun Prop 1.3; con:amp-works; con:local-concavity),
  and additionally proves rigorously that the Hessian of the frozen-tilt
  functional at the degenerate maximizer (1,0) is negative definite
  (his Claims clm:numeric-M-estimates / clm:sS-zero-2deriv:
  M_11 <= -0.045408, M_22 <= -0.020490, det M >= 0.0002246).
  Condition 1.3 itself is NOT verified there. Thus, before the present
  certificate, the Krauth-Mezard conjecture was conditional on DS Condition
  1.2 and Huang Condition 1.3.

- Altschuler-Tikhomirov (arXiv:2401.15092): unconditional upper bound 0.847,
  by the Krauth-Mezard outline + spherical perceptron comparison. This is the
  best prior unconditional upper bound; the prior unconditional lower bound is the
  Kim-Roche epsilon. The gap between 0.847 and alpha_* ~ 0.833 is exactly the
  two unverified conditions above.

## The goal

Prove the two outstanding conditions rigorously, i.e. produce a computer-assisted
proof (interval arithmetic with certified quadrature, plus the analytic reductions
needed at the degenerate maximizers and at infinity) of

  (A) Ding-Sun Condition 1.2 / c:G: SE_*(lambda) < 0 for lambda not in {0,1},
      SE_*''(0) < 0, and lim_{lambda -> 1-} SE_*'(lambda) > 0;
  (B) Huang Condition 1.3 / con:2varfn: S_*(lambda_1,lambda_2) <= 0 on R^2,

and audit the assembly (including the rigor of Ding-Sun Proposition 1.3, whose
interval bounds for alpha_*, q_0=q_*(alpha_*), psi_0 are quoted by everything
downstream). Together with the published results this makes the Krauth-Mezard
conjecture an unconditional theorem:

  M_N/N -> alpha_*(0) ~ 0.8330786 in probability, for gaussian and for
  Bernoulli disorder.

## Definitions needed later (transcribed from the sources)

Gaussian density phi(x), upper tail Psi(x) = int_x^infty phi. E(x) = phi(x)/Psi(x).
F_{1-q}(x) = E((kappa - x)/sqrt(1-q)) / sqrt(1-q). At kappa = 0 throughout.

P(psi) = E[tanh(sqrt(psi) Z)^2], R_alpha(q) = alpha E[F_{1-q}(sqrt(q) Z)^2].
(q_0, psi_0) is the fixed point q_0 = P(psi_0), psi_0 = R_alpha*(q_0);
alpha_* is the root of the Gardner free energy

  G(alpha, q, psi) = -(1-q) psi / 2 + E log(2 cosh(sqrt(psi) Z))
                     + alpha E log Psi((kappa - sqrt(q) Z)/sqrt(1-q))

evaluated along the fixed point. Ding-Sun Prop 1.3 intervals:
  alpha_* in [0.833078599, 0.833078600]
  q_0     in [0.56394907949, 0.56394908030]
  psi_0   in [2.5763513100, 2.5763513224]

Huang's first-moment functional. dbH ~ N(0, psi_0), hbH ~ N(0, q_0) on separate
spaces; M = tanh(dbH); N = F_{1-q_0}(hbH). For measurable Lam: R -> [-1,1]:

  ent(Lam) = E H2((1 + Lam(dbH))/2),   H2 = binary entropy (nats)
  a_1(Lam) = E[dbH Lam(dbH)],  a_2(Lam) = E[M Lam(dbH)]

  S_*(Lam, s) = s^2 psi_0 / 2 + ent(Lam)
              + alpha_* E log Psi{ (kappa - (a_2/q_0) hbH - (a_1/psi_0) N)
                                   / sqrt(1 - a_2^2/q_0)  + s N }

  S_*(Lam) = inf_{s >= 0} S_*(Lam, s);  Lam_{l1,l2}(x) = tanh(l1 x + l2 tanh(x));
  S_*(l1, l2) = S_*(Lam_{l1,l2}).

Condition 1.3: S_*(l1,l2) <= 0 for all (l1,l2) in R^2. Known analytically
(Huang Lemma lem:sS-zero, unconditional): S_*(1,0) = 0 with optimal tilt
s(1,0) = sqrt(1-q_0); gradient of S_* vanishes at (1,0); and
nabla^2 S_* (1,0) <= nabla^2 osS_*(1,0) = M where osS_* is the frozen-tilt
function S_*(l1, l2, sqrt(1-q_0)) and M is the negative definite matrix above.

Useful exact identities at the fixed point (used to eliminate delicate integrals):
  p_2(psi_0) := E[tanh^2] = q_0
  r_2(gamma_0) := E[E(sqrt(gamma_0) Z)^2] = (1-q_0) psi_0 / alpha_*,
                  gamma_0 = q_0/(1-q_0)
  d_0 = alpha_* E[F'_{1-q_0}(sqrt(q_0) Z)] = -(1-q_0) psi_0
  alpha_* E[N^2] = psi_0,  alpha_* E[N hbH] = -q_0 (1-q_0) psi_0
  E' (x) = E(x)(E(x) - x) in (0,1);  F'_{1-q}(x) = -F(x)(F(x) - x/(1-q)) at kappa=0.

## Verification architecture

For (B), three regimes:

1. Local: extend Huang's point-Hessian negativity to an explicit ball
   B((1,0), rho): interval-evaluate the general-(l1,l2) Hessian entries of the
   frozen-tilt osS_* over the box, certify nabla^2 osS_* <= -c I there; then
   Taylor from the exact center values S_*(1,0)=0, grad=0 gives
   S_* <= osS_* <= -(c/2)|lambda - (1,0)|^2 on the ball. Margins are thin
   (smaller Hessian eigenvalue is about -0.004 at center), so rho and the
   quadrature tightness need tuning; derive the general-lambda Hessian of
   osS_* by hand and check with symbolic differentiation.

2. Middle: cover {rho <= |lambda - (1,0)|, |lambda| <= R} by 2D interval boxes,
   each with a frozen tilt s_B (chosen by nonrigorous optimization, then fixed
   as an exact rational); certify S_*(box, s_B) < 0 by certified quadrature.
   All integrals are one-dimensional gaussian integrals; integrands built from
   tanh, log(2cosh), E, log Psi. Two quadrature options: interval Riemann sums
   with mean-value refinement (no analyticity needed), or arb's rigorous
   integration; start with the former.

3. Tail |lambda| > R: analytic. ent(Lam_{l1,l2}) -> 0 with explicit rate
   (the field f(x) = l1 x + l2 tanh x has only x=0 as a possible degenerate
   root, since sinh(2x)/2 = x only at 0; worst case is the l1 + l2 = 0
   direction where f ~ -l2 x^3 / 3, giving a cube-root rate). The constraint
   term is <= -c_0 uniformly: a_1, a_2 range over an explicit compact set with
   1 - a_2^2/q_0 bounded below (a_2 <= E|M| < sqrt(q_0)), and a window argument
   on hbH gives E log Psi <= -c_0 < 0 with c_0 an explicit interval number.
   Choose R so the entropy bound beats alpha_* c_0. Then S_*(lambda) <=
   S_*(lambda, 0) <= ent - alpha_* c_0 < 0.

For (A), follow Ding-Sun's own outline (their sections 8-10), replacing every
"numerical integration package" step with certified quadrature, and re-prove
their grid Proposition p:grid.result rigorously. Their analytic reductions
(monotonicity lemmas, second derivative at 0, behavior near 1) appear to be
complete proofs modulo those numerical inputs; audit while transcribing.

Also audit: rigor of DS Prop 1.3 (source of the parameter intervals). If their
proof of Prop 1.3 relies on nonrigorous integration, re-derive the intervals
rigorously (sign changes + contraction of q -> P(R_alpha(q)) + monotonicity of
G_*; all 1D certified integrals).

## Assembly (target theorem)

DS Thm 1.1 (under A) + Xu/Nakajima-Sun sharp threshold + universality
+ Huang Thm 1.1 (under B) => for the Ising perceptron with gaussian or
subgaussian disorder, M_N/N -> alpha_* in probability. Write the manuscript
with the two verifications as the main content, the assembly as a short
section, and the verification code as ancillary material.
