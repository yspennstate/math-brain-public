# P0177: third check (claude-322bc92e, 11 Oct 2026 23:1x)

Verdict: PASS. Novelty not verified; this is a modest result. The problem (Hasebe-Ueda, ALEA 15 (2018), Problem 4.6) asks for estimates of the mode location, and the attempt supplies explicit O(1/t) bounds in the source's own parameters (epsilon, alpha) together with two-term expansions:
  M_c(t) = m - mu3/(2t) + (mu5 - 6 mu2 mu3)/(8t^2) + O(t^-3)
  M_f(t) = m - 3 mu3/t + (5 mu5 - 22 mu2 mu3)/t^2 + O(t^-3)

Independent checks:
- By hand: the classical first-order term follows from the stationarity condition E[(x - X) exp(-(x - X)^2/(2t))] = 0, expanded at x = m + delta.
- Numerically, on my own code: a three-point law (x = -1, 0.5, 3; p = 0.5, 0.35, 0.15), with m = 0.125, mu2 = 1.921875, mu3 = 2.871094, mu5 = 28.564819. The classical mode is the maximum of the Gaussian mixture. The free mode is psi_t(u*) with u* the maximizer of eta_t(u), where R = eta^2 solves E[1/(R + (u - X)^2)] = 1/t (Biane). Over t = 50, 100, 200, 400, the error times t^3 stays bounded: classical 3.4, 3.3, 2.4, 4.3 (the last limited by optimizer precision); free 412, 446, 462, 443, and the free error falls by about 8 each time t doubles. Both two-term expansions are therefore right, including the second-order coefficients.
- Algebra: (1 - 3z)/(1 + z)^3 - (1 - 6z) = z^2(15 + 17z + 6z^2)/(1 + z)^3 holds. The free global-maximizer argument (concavity of F(., R*) on [-B, B] once t > 7A) reads correctly.

Not checked: the explicit-constant section beyond reading it; the Lean file.
