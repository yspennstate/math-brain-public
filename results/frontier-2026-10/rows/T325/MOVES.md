# T325 moves on the obstruction

- 2026-10-16, literature (agent A): Abstracts read 16 Oct 10:3x: 2306.09927, 2306.00297, 2307.03576, 2410.08292, 2402.14951, 2501.16265, 2402.19442, 2503.12734, 2512.11784, 2402.14180, 2407.10005, 2504.12916, 2610.10761. Weight-shared multi-layer convergence is proved (2410.08292); untied layers and multi-layer softmax are open. Reduction: scalar steps g_l give risk int prod(1-g_l s)^2 dMP_q.
- 2026-10-16, narrowed (agent A): scalar-step landscape measured: noiseless floor 1/sum_k q^-k reached from 200/200 starts at L<=6; with noise the floor needs complex roots at L>=4, real-step GD ends at coincident steps, several end values at L=6
- 2026-10-16, bound (agent A): gap to ridge over polynomials: noiseless R*_L = (1-q)q^L/(1-q^(L+1)) proved via MP Jacobi parameters; with noise the gap ratio per layer is rho^-2 (Bernstein ellipse of the ridge pole -sigma^2 q), measured to 5 digits L=12..16
- 2026-10-16, special (agent A): with noise, L=6, real scalar steps: three strict local minima per q (Hessian PD, |grad|<1e-9), steps in even groups; global basin 60%/32% of starts; Target 1 'almost every start' false there
- 2026-10-16, special (agent A): quadratic-factor (complex-pair) parametrization also has strict local minima with noise (identical-factor symmetric points); risk convex in coefficients, not in any factorisation tried
- 2026-10-16, special (agent A): full 4x4 preconditioners, L=4, noise: the real-step minimum is a strict local min in full matrix space (Hessian PD), 10/10 random small inits end there, none reach the polynomial floor
