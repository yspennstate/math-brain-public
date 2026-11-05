# T390 The statistical efficiency of score matching

Lead: unassigned. Dossier written 2026-10-16 by agent A from the row and the arXiv records below (abstracts read 16 Oct
09:4x-10:2x).

## STATEMENT
As in the list row: the sample complexity of learning a mixture of k well-separated Gaussians in R^d by (denoising) score
matching at a small noise level against maximum likelihood, and whether annealing over noise levels closes the gap
polynomially.
Narrowed by the literature: for a finite mixture with a SHARED covariance, annealed (Gaussian-convolution) score matching
already has sample complexity polynomial in d, the diameter of the means and the extreme covariance eigenvalues (Qin and
Risteski). What stays open is a sharp comparison: the exact exponent of the single-noise-level loss on a k-mixture, a
matching lower bound for the annealed loss, and mixtures with unequal covariances.

## FRONTIER
- Koehler, Heckett, Risteski arXiv:2210.00726: the statistical efficiency of score matching against maximum likelihood is
  tied to the isoperimetry of the target (Poincare, log-Sobolev and isoperimetric constants); for poorly mixing targets score
  matching is much less efficient.
- Qin, Risteski arXiv:2306.09332: a generalized score-matching loss built from a fast-mixing Markov process; lifting with a
  temperature gives a Gaussian-convolution annealed loss (as in Song and Ermon), and for a finite Gaussian mixture with
  shared covariance its sample complexity is polynomial in d, the diameter of the means and the smallest and largest
  covariance eigenvalues, which removes the Poincare-constant lower bound of the basic loss.
- Pabbaraju et al. arXiv:2306.01993: exponentials of fixed-degree polynomials, a family where score matching is
  computationally efficient with statistical efficiency comparable to ML while the ML loss is hard for gradient methods.
- Shah, Chen, Klivans arXiv:2307.01178: gradient descent on the DDPM objective recovers the parameters of a mixture of two
  spherical Gaussians with 1/poly(d)-separated centers from random initialization, and of K spherical Gaussians with
  Omega(sqrt(log min(K,d)))-separated centers from a warm start.
- Chen, Kontonis, Shah arXiv:2404.18893: d^poly(k/eps) samples and sample-polynomial time give a sampler eps-close in TV to a
  general k-mixture (bounded condition number, means and covariances in a ball), with no separation assumption.
- Tyurin arXiv:2606.19876: the reverse Fisher divergence gives better gradient-descent behaviour than the forward one on
  Gaussian mixtures.

## ARCHITECTURE
Score matching's variance is controlled by the target's Poincare constant, which for k well-separated components grows like
exp(separation^2); maximum likelihood pays no such price. Annealing adds a noise level at which the components overlap and
the convolved target mixes fast, and the losses at the different levels are chained.

## FAILURE POINT
The polynomial bound for the annealed loss is proved for a shared covariance; with unequal covariances the convolved target at
intermediate noise levels is not a translate family, and the chaining argument through the temperature-lifted chain was not
stated for that case in the abstract.

## SHAPE
Weeks: the two-component one-dimensional mixture at separation m: compute the asymptotic variance of the single-level score
matching estimator of the means against the Fisher information (exact in m), and the same for the annealed loss with a fixed
number of levels.

## OBSTRUCTION
A lower bound for the annealed loss that shows its polynomial is necessary (or a sharper upper bound), and an extension of the
annealed analysis beyond a shared covariance.

## TARGETS
1. One dimension, two components at separation m, small noise sigma: the asymptotic relative efficiency of denoising score
   matching to maximum likelihood as an explicit function of m and sigma.
2. Read 2306.09332's mixture theorem for the exact polynomial and whether it covers k growing with d.

## RESULTS

2026-10-18 (agent A), are_dsm.py and are_dsm_weight.py: for 1/2 N(-m,1) + 1/2 N(m,1) the asymptotic relative efficiency
of plain score matching to maximum likelihood stays near 1 for the means (0.89 at worst, at m = 1.5) but decays like
e^(-m^2/2) for the weight (7.2e-3 at m = 3, 5.9e-9 at m = 6); with denoising at the best of the listed noise levels, which
grow with m, the weight's efficiency is back above 0.9 for every m up to 6.

2026-10-31 (agent B), T390_weight_are_asymptotic.md: the closed form for the weight.

2026-11-04 (agent C), audit (AUDIT_agent_C.md). With eps = 1/m^2 and the substitution y = m x,

    ARE(m) = sqrt(2 pi) e^(-m^2/2)/m (1 - c/m^2 + d/m^4 + O(m^-6)),
    c = 4/3 + pi^2/8 = 2.56703...,   d = 58/9 - pi^2/2 + 5 pi^4/128 = 5.31468...

c follows from int y^2 sech^3 = pi^3/8 - pi and int y^2 sech^5 = 3 pi^3/32 - 5 pi/6; d was found by PSLQ and holds to 40
digits, with the remainder checked to be O(m^-6). The source's "about 2.5" was read at m <= 8, where the d term still pulls
the estimate down. The denoising table matches an independent quadrature to every printed digit; the lower bound
H^2/(V_s I) is valid, loose by about 3 at sigma = m and by 4.6-6.8 elsewhere. The M-estimator hypotheses hold on a compact
parameter set. Open: k components and the comparison with arXiv:2210.00726 and Chen-Kontonis-Shah.
