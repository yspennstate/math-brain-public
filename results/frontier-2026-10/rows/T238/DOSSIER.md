# T238 The transition between the lazy and the rich regime

Lead: unassigned. Dossier written 2026-10-16 by agent A from the row and the arXiv records below (titles and dates
checked 16 Oct 06:4x; contents as recalled from the abstracts, to be read before a route is chosen).

## STATEMENT
Kept as listed: single-index teacher y = g(v . x); student alpha m^(-1) sum_j a_j relu(w_j . x) minus its initial value;
gradient flow to time T; m -> infinity first, then n, d -> infinity with n/d^k fixed. Determine the window of alpha (in d
and n) across which the trained predictor's distance from the linearized predictor goes from o(1) to order 1, and the test
error across it.
Comment: with m -> infinity first, alpha m^(-1) sum is the mean-field parametrization scaled by alpha, and alpha -> infinity
is lazy (Chizat-Oyallon-Bach). The window must be stated jointly with T: at fixed alpha the dynamics leave the lazy regime
at a time of order alpha^c, so "the window of alpha" is really a curve in the (alpha, T) plane, and the row should fix T (to
convergence, or to a stated power of d). The diagonal-linear answer (Woodworth et al.) is the template: there the
transition is governed by a single scale (initialization size against the target norm).

## FRONTIER
- Chizat, Oyallon, Bach arXiv:1812.07956: lazy training as the scale alpha -> infinity, with quantitative bounds.
- Geiger, Spigler, Jacot, Wyart arXiv:1906.08034: the crossover between feature and lazy training in deep networks; the
  crossover scale against width, measured.
- Woodworth, Gunasekar, Lee, Moroshko, Savarese, Golan, Soudry, Srebro arXiv:2002.09277: kernel and rich regimes for
  diagonal linear networks; the implicit regularizer interpolates between l_2 and l_1 with the initialization scale.
- Ba, Erdogdu, Suzuki, Wang, Wu, Yang arXiv:2205.01445: one large gradient step (step of order sqrt d against order one)
  separates kernel-like from feature-learning predictors in the proportional regime; a sharp threshold in the step.
- Bordelon, Pehlevan arXiv:2205.09653: dynamical field theory with a parameter gamma interpolating lazy and rich training
  at infinite width; kernel evolution as a function of gamma.
- Open: the window in alpha for a single-index teacher at n of order d^k, with the test error, rigorously.

## ARCHITECTURE
At infinite width the dynamics are the mean-field PDE with the output scaled by alpha (equivalently the gamma = 1/alpha
field theory). The predictor's distance from its linearization is driven by the second-order term in the parameter
motion, of order (movement)^2 times the curvature; for the single-index teacher, the movement needed to fit the projection
of g on the low-degree spherical harmonics is of order 1/alpha in the lazy regime, while fitting degree k needs the
kernel's degree-k eigenvalue, of order d^(-k). The transition occurs where the movement needed by the kernel solution for
the target's relevant degree stops being small, which suggests a window alpha ~ d^(c k) at n ~ d^k.

## FAILURE POINT
A rigorous description of the mean-field dynamics at alpha in the intermediate window, in high dimension: neither the
linearization (alpha large) nor the order-one mean-field limit with a dimension-free PDE applies, and the PDE's dependence
on d is not controlled.

## SHAPE
Weeks to months. Days for a heuristic window from the gamma field theory of 2205.09653 applied to the single-index
teacher, which fixes the exponent to aim for.

## OBSTRUCTION
A crossover, not a phase: its location depends on which degree of g the samples can resolve, so the answer is a family of
windows indexed by k. Moves: the k = 1 case (linear part of g, n ~ d); the quadratic activation where the mean-field
dynamics close on a matrix ODE; the one-step version (2205.01445) as the T -> 0 end of the curve.

## TARGETS
1. Restate the row with T fixed (convergence or T = d^s) and the window as a curve.
2. Quadratic activation, g of degree 2, n ~ d^2: compute the alpha window from the matrix ODE.
3. Derive the heuristic window from 2205.09653 for g with information exponent 1 and 2.
4. Experiment: m = 2000, d = 32, n = 4 d, g = He_2, alpha from 1 to 1000, distance to the linearized predictor and test
   error at convergence.

## RESULTS

2026-10-31 (agent B), target 2 for a quadratic student (NOTE_quadratic_window.md). With +- pairs sharing their initial
weights, the infinite-width student is x^T (P - Q) x with P' = -(GP + PG), Q' = GQ + QG, P(0) = Q(0) = c I and c
proportional to alpha/d: matrix sensing grown multiplicatively from a scaled identity. When the G(t) commute the implicit
regularizer is the spectral hypentropy at scale c, between the minimum-Frobenius (lazy) and minimum-nuclear (rich)
solutions. window.py trains this flow to convergence at n = d^2/4 for c from 1e-3 to 0.1.

2026-11-04 (agent C), audit with seed spread (AUDIT_agent_C.md, 34 runs). Share of the lazy gap left at c, mean over seeds:

| c | d = 8 | d = 12 | d = 16 | d = 24 | d = 32 |
|---|---|---|---|---|---|
| 1e-3 | 0.59 | 0.76 | 0.83 | 0.88 | 0.91 |
| 1e-2 | 0.31 | 0.43 | 0.47 | 0.51 | 0.60 |
| 0.1 | 0.03 | 0.06 | 0.04 | 0.04 | 0.06 |

The lazy edge is fixed at c of order 0.1 for every d. At fixed small c the run ends nearer the rich solution as d grows
(slope +0.11 per doubling of d at c = 1e-3 with d = 8 left out, 3.1 standard errors), so the rich edge drifts to larger c.
At d = 8 (n = 2d) three of eight seeds do not reach the teacher at c = 1e-3, which confounds that column. Nine runs stop at
the step cap with train loss between 1e-10 and 5e-9.

Open: the bridge from the quadratic flow to the row's two-layer ReLU student (degree-2 Hermite part, the He1 term of the
teacher, finite width, the stopping rule, the map between c and alpha). The row stays open.
