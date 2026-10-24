# T421 Adaptive edge of stability: the preconditioned sharpness

Lead: unassigned. Dossier written 2026-10-16 by claude-99aebc7f from the row and the arXiv records below (abstracts read 16 Oct
10:0x-10:1x; items marked 'recalled' were not re-read).

## STATEMENT
Repaired (per the audit of 2026-10-16T05:19, statement_ok NO): for a randomly initialized rank-one or diagonal quadratic or a deep
linear model, full-batch Adam (or RMSProp) with stated betas, bias correction and epsilon = epsilon(eta) -> 0 at a stated rate, prove
that after a burn-in the preconditioned sharpness, or the curvature along the active direction, rises to and stays within o(1/eta) of
the threshold (38/eta for Adam with beta1 = 0.9) while the loss decreases non-monotonically; characterize when the active-direction
curvature rather than the top sharpness tracks the threshold. A fixed epsilon caps the preconditioned sharpness at |H|/epsilon, so
epsilon must shrink with eta.
Narrowed by the literature: Adam's second-moment adaptation is identified as a negative-feedback mechanism driving the dynamics to the
stability boundary, characterized through the active curvature (preconditioned curvature along the preconditioned gradient), with
rigorous results on rank-one quadratics with momentum, diagonal quadratics (where the active curvature separates from the sharpness)
and general objectives; it predicts gradient reversal near the edge.

## FRONTIER
- Cohen, Ghorbani, Krishnan, Agarwal, Medapati, Badura et al. arXiv:2207.14484: empirically, the top eigenvalue of the preconditioned
  Hessian equilibrates at the stability threshold, 38/eta for Adam with beta1 = 0.9; similar in minibatch training at large batch.
- Fong, Yang arXiv:2608.20638: second-moment adaptation as negative feedback toward the stability boundary; active curvature;
  rigorous characterizations in rank-one quadratics with momentum, diagonal quadratics (active curvature separates from sharpness) and
  general objectives; gradient reversal predicted and observed across architectures; iterate averaging smooths the loss.

## ARCHITECTURE
On a quadratic, the Adam step is eta m_t / (sqrt(v_t) + epsilon); near the edge the gradient oscillates in sign along the active
direction, v_t tracks the squared oscillation amplitude, and the effective preconditioned curvature along that direction is pushed
toward the value at which the linearized momentum recursion has a root at -1 (the 38/eta threshold for beta1 = 0.9 with Adam's
normalization). The feedback: amplitude up -> v up -> preconditioned curvature down, and conversely.

## FAILURE POINT
The epsilon(eta) scaling and the 'within o(1/eta)' precision: the read abstract states characterizations in these models but not
the quantitative tracking with epsilon -> 0, which is what the row asks; the diagonal case's statement of WHICH curvature tracks the
threshold is where the abstract stops.

## SHAPE
Days: read 2608.20638 in full and record which of the row's quantified statements it proves; then the diagonal quadratic with two
eigenvalues and epsilon = eta^p: the averaged dynamics of v_t over the oscillation period, giving the equilibrium active curvature
and its deviation from 38/eta.

## OBSTRUCTION
Averaging over the fast oscillation when the oscillation amplitude itself is slowly varying and bias correction is still active.

## TARGETS
1. Diagonal quadratic, two eigenvalues, Adam with beta1 = 0.9, beta2 = 0.999, epsilon = eta^p: the long-run active curvature times
   eta, as a function of p, compared with 38.
2. The condition (in terms of the two eigenvalues and the gradient's alignment) under which the top preconditioned sharpness stays
   above the threshold while the active curvature equals it.

