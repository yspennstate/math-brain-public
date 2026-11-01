# Continuation checkpoint: convex cones and exact route obstructions

Model/reasoning setting not independently exposed. PARTIAL; full Lyons OPEN. Global three-site `B_Phi`: UNMEASURED -> UNMEASURED, no movement. Restricted scope expands to the two fixed-diagonal three-coupling convex cones in `FOURIER_NEXT_STEPS.md`. Moves 18, 20, 30.

The previous exact signed-curvature identity proves concavity on each contraction cone `+/-2z >= sqrt(x^2+y^2)` for `a=t+z,b=t-z`. The proof includes convexity of the domain and its boundary extension. This is a complete restricted statement, not unrestricted four-variable concavity.

The configuration law also reduces exactly to the binomially weighted bivariate count law of a sum of two independent two-site DPP vectors. Nine further coefficientwise polynomial identities check this reduction.

Two exact rational certificates explain failures of proposed extensions. The lower bound obtained by dropping the remaining local Fisher terms can be below -1 even when the actual negative entropy curvature exceeds 1700. Mutual information between opposite pairs can have second derivative below -2/5 along a fixed-diagonal line even when actual negative entropy curvature exceeds 68. Neither example is a counterexample to Lyons's conjecture.

`verify_fourier_barriers.py` passes, including all nine count identities and both exact logarithm-enclosure certificates. Across the three new Fourier verifiers there are 64 polynomial identities, 70 exact Fourier projection-channel entries, 57 representative rational curvature cases, and two exact obstruction cases. These are self-checks only; there have been no independent audits.

A sharper bound retains a quantitative local remainder from the original Hillion-Johnson inequality. Three differential-evolution runs, 8080 evaluations each, did not find a negative value of this new sufficient bound. They exhausted their iteration limits without optimizer convergence and approached nearly equal-eigenvalue degeneracies; this is numerical exploration, not a proof of the bound or of the conjecture. Scripts, seeds, and output are retained. Further progress requires the explicit inequality in Section 5 of `FOURIER_NEXT_STEPS.md`.
