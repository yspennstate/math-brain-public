# T362 Optimal convergence rates of SGD with random reshuffling

Lead: unassigned. Dossier written 2026-10-16 by agent A from the row and the arXiv records below (abstracts read 16 Oct
09:0x, and the 16 Oct 04:47 audit (status PARTLY)).

## STATEMENT
Repaired, following the audit: fresh reshuffling each epoch, constant step chosen knowing (n, K), L-smooth components, mu-
strongly convex average, variance sigma_*^2 at the optimum, LAST iterate, error E[F(x_K) - F*]; regimes K < kappa and K >=
kappa. Separate question: nonconvex L-smooth sums, min over iterates of E||grad F||^2, with a matching lower bound.
Narrowed by the literature: tight-in-kappa bounds are known for weighted-average iterates (Cha, Lee, Yun 2303.07160), and the
(n, K) dependence of the last epoch is matched under a Hessian-Lipschitz assumption (Li 2609.04578, Sept 2026, unreviewed).
What remains: the last iterate tight in kappa as well as (n, K); and the nonconvex lower bound.

## FRONTIER
- Safran, Shamir arXiv:1908.00045: lower bounds for constant-step shuffling, already on quadratics.
- Mishchenko, Khaled, Richtarik arXiv:2006.05988: upper bounds for strongly convex and nonconvex RR.
- Ahn, Yun, Sra arXiv:2006.06946: minimax-optimal rates up to polylog for RR and single shuffle, without component convexity.
- Cha, Lee, Yun arXiv:2303.07160: lower bounds for weighted average iterates tight in kappa; first to close the gap between
  lower and upper bounds for weighted average iterates, strongly convex and convex.
- Liu, Zhou arXiv:2403.07723: first last-iterate function-value rates for shuffling methods without strong convexity; nearly
  matching existing last-iterate lower bounds.
- Li arXiv:2609.04578 (Sept 2026, single author, unreviewed): last-epoch E[F(y_K) - F*] = O~(T^-2 + n^2 T^-3), T = nK, for
  L-smooth components, mu-strongly convex average with Lipschitz Hessian; matches the quadratic lower bound in (n, K).
- Open: last-iterate kappa dependence; nonconvex lower bound for RR.

## ARCHITECTURE
Quadratics give the lower bound (Safran-Shamir); the upper bound tracks the epoch drift: within an epoch the iterate moves by
the partial sums of the permuted gradients at the optimum, whose variance is that of sampling without replacement (a factor
(n - i) i / n smaller than with replacement).

## FAILURE POINT
The kappa factor in the last iterate: the weighted average of 2303.07160 averages out the slow directions; the last iterate
keeps the drift along the direction of curvature mu.

## SHAPE
Days: one-dimensional quadratic epoch recursion, exact last-iterate error as a function of (n, K, kappa) for the
Safran-Shamir instance (the audit's DAYS item); this gives the conjectured kappa exponent. Months: the matching upper bound.

## OBSTRUCTION
Last iterate versus average. Moves: Liu-Zhou's last-iterate technique combined with 2303.07160's kappa-tight instance.

## TARGETS
1. Exact recursion on f_i(x) = (mu/2) x^2 + b_i x with sum b_i = 0 plus one stiff coordinate of curvature L: last-iterate
   error in closed form, minimized over the constant step.
2. Read 2609.04578's constants for their kappa dependence.
