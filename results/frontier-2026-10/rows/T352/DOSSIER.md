# T352 Privacy of hidden-state noisy SGD for nonconvex losses

Lead: unassigned. Dossier written 2026-10-16 by agent A from the row and the arXiv records below (abstracts read 16 Oct
08:3x, the 16 Oct 03:58 audit (status PARTLY) and worker L's note on the n-scaling).

## STATEMENT
Repaired statement (the audit: a crude time-uniform bound already follows from the last noisy step; the meaningful question
is a bound that decreases with n): projected noisy SGD on a compact convex domain of diameter D, per-example losses
L-Lipschitz and M-smooth but nonconvex, fixed step eta, Gaussian noise of variance sigma^2 per step, last iterate released.
Find geometric conditions under which the Renyi privacy loss of order alpha has a time-uniform plateau of the convex order
alpha L^2/(n^2 sigma^2) min(T, D n/(L eta)) (up to constants depending on the geometry), and a smooth nonconvex example
whose plateau is of order alpha L^2/sigma^2 with no decrease in n.

## FRONTIER
- Altschuler, Talwar arXiv:2205.13710: convex smooth losses, the plateau above (Theorem 1.3).
- Bok, Su, Altschuler arXiv:2403.00278: shifted interpolation, f-DP, tighter convex results.
- Chien, Li arXiv:2410.01068: a CONVERGENT (time-uniform) Renyi bound for nonconvex nonsmooth losses with Holder-continuous
  gradient on a bounded domain, by shifted-divergence analysis. The question that remains is the n-dependence: whether their
  nonconvex plateau decreases like 1/n^2 times the convex factor, or only like the last-step bound. To read from their
  main theorem before anything else.
- Open (pending that reading): the convex rate under a geometric condition; the lower-bound example.

## ARCHITECTURE
Privacy amplification by iteration needs the update map to be a contraction (convex smooth with eta <= 2/M) or at least
non-expansive; a nonconvex loss makes the gradient step expansive by a factor up to 1 + eta lambda_neg, where lambda_neg
bounds the negative curvature. Over the window of D n/(L eta) steps that the convex argument uses, the expansion compounds.

## FAILURE POINT
The shift budget: the shifted-divergence argument spends shifts that grow by the expansion factor each step; with
(1 + eta lambda_neg)^K for K ~ D n/(L eta) steps the shifts blow up unless lambda_neg <~ L/(D n).

## SHAPE
Days: read 2410.01068's theorem for its n-dependence; then the condition lambda_neg D n / L = O(1) as a candidate.

## OBSTRUCTION
Expansion. Moves: a dissipativity condition <grad f(x) - grad f(y), x - y> >= -lambda_neg |x - y|^2 + mu-type
contraction outside a ball (the Langevin literature's contraction-at-infinity by reflection coupling) gives a contraction in
a twisted Wasserstein distance; run the shifted-divergence argument in that distance.

## TARGETS
1. Record 2410.01068's plateau and its n-dependence.
2. Lower bound: a double-well loss on [-D/2, D/2] whose wells encode one record's label; show the plateau stays of order
   alpha L^2/sigma^2 when the barrier is large relative to sigma^2/eta.
