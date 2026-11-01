# P0220: third check (claude-322bc92e, 11 Oct 2026 23:2x)

Verdict: PASS on the cases I could test independently. The general proof was not re-derived. Novelty and priority are not verified.

Claim: every joint survival probability of the stationary ordered particles of Aldous's drift-jump process (dX/dt = X, rate-one space-time Poisson points pull the nearest particle on the right to the point) equals exp(-T) det M. M is a finite block matrix of Bessel-type entries E_u(a,b) = u^((b-a)/2) I_{a-b}(2 sqrt u), of size at most k(k-1) for the first k particles. That gives an explicit joint law, evaluating the 1993 patience-sorting representation with classical RSK and Eynard-Mehta tools.

Independent checks:
- One particle, exact. The leftmost particle is Markov on its own: it drifts as x' = x and jumps at rate x to a uniform point of [0, x]. Its adjoint equation -(x pi)' - x pi + integral_x^inf pi = 0 is solved by pi = e^-x, so P(X1 > T) = e^-T, the formula's d = 0 case.
- Two particles, from the recipe (I worked the 2x2 block by hand): P(X2 > T) = e^-T I0(2 sqrt T) and P(X1 > t1, X2 > T) = e^-T I0(2 sqrt(T - t1)).
- Monte Carlo of the process itself (my own code; simulation on [0, 18] is exact for particles inside the window; 80k samples at spacing 0.5):
  - P(X2 > T) for T = 0.5, 1, 2: 0.9498, 0.8401, 0.5794 against 0.9499, 0.8386, 0.5755;
  - joint survival at (0.5, 1.5), (1, 2.5), (0.3, 3): 0.5117, 0.2641, 0.3112 against 0.5086, 0.2598, 0.3073;
  - X1 marginal 0.6093, 0.3721, 0.1402 against 0.6065, 0.3679, 0.1353.
  All within about 0.005, one shared upward fluctuation of roughly 1-2 sigma at the effective sample size.
- The solver's own checks are strong and independent of the derivation: exact Taylor coefficients through degree 7 against exhaustive permutation counts, 55-digit positive-growth numerics, Lean block-sign check.

Not done: a line-by-line check of the general determinant proof (sections 3-7 of the continuation), or a literature search for priority.
