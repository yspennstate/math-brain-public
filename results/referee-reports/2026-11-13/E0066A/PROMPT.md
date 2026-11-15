# Open problem E0066: trajectories of bistochastic (doubly stochastic) quadratic stochastic operators

Statement (ledger): a quadratic stochastic operator V on the simplex S^{m-1}, V(x)_k = sum_{i,j} p_{ij,k} x_i x_j with
p_{ij,k} = p_{ji,k} >= 0 and sum_k p_{ij,k} = 1, is bistochastic (doubly stochastic) if V(x) is majorised by x for every x.
"Investigate the behaviour of the trajectories of the bistochastic quadratic operators."
Known: Ganikhodzhaev (Russian Math. Surveys 1993) and Ganikhodzhaev-Shahidi characterised these operators (extreme points,
conditions on the coefficients p_{ij,k}). Abdulghafor-Shahidi-Zeki-Turaev, Open Math. 14 (2016) 509-519, doi
10.1515/math-2016-0045: on the 2-simplex interior trajectories converge when there are no interior periodic points of period
greater than one (Thms 3.3, 3.5, Cor 3.8, Ex 3.9). Higher dimensions are open.

TASK: decide whether every trajectory of a bistochastic QSO converges (or at least is Cesaro/ergodic convergent) for m >= 4,
or produce an operator with a non-convergent trajectory (an attracting or neutral periodic orbit of period >= 2, or a
non-ergodic orbit), verified rigorously.
1. Parametrise the bistochastic class exactly (the coefficient conditions; the polytope of bistochastic p's for m = 3, 4, 5;
   its extreme points). Note the centre c = (1/m,...,1/m) is fixed and majorisation makes sum x_i^2 (and every Schur-convex
   function) non-increasing along orbits: use this Lyapunov structure. Where can omega-limit sets live (level sets of all
   Schur-convex functions; permutation orbits of a point)? A period-2 orbit would have to consist of points that are
   permutations of each other - analyse exactly when V maps x to a permutation of x.
2. Numerical search: random and extreme bistochastic operators for m = 3..6, iterate many starts, detect non-convergence;
   targeted search for V with V(x) = sigma x (sigma a permutation) on an invariant set. Verify any candidate exactly
   (rational arithmetic / interval bounds).
3. Prove what you can: convergence for m = 3 in full (removing the no-periodic-point hypothesis if possible), convergence for
   the extreme operators in every m, or a general theorem; or a counterexample family in every m >= some m_0.
4. Check later literature (Shahidi, Ganikhodzhaev, Mukhamedov, Jamilov, Saburov 2016-2026) before claiming novelty.
Keep peak memory under 4 GB; no worker pools larger than 4 threads.

OUTPUT: REPORT.md whose FIRST LINE is one of PROVED / PARTIAL / COUNTEREXAMPLE / NO_PROGRESS, then the theorem
statement(s), complete proofs written as for a referee, numerical tables with code paths, and what remains open.
Keep a running LOG.md. Save all code and data in this folder. Write like a professional mathematician; no narration of
your process inside the theorem/proof text.
