# Continuation checkpoint: scalar reduction and full Fourier ratio domain

Model/reasoning setting not independently exposed. PARTIAL; unrestricted Lyons OPEN. Frozen three-site `B_Phi`: UNMEASURED -> UNMEASURED, no movement. Restricted Fourier coverage advances again. Moves 3 (prove a stronger local bound), 12 (use the count mean and variance), and 25 (compare exact atom curvature with count information).

`FOURIER_ONE_SCALAR.md` proves that fixing just one pair mean suffices for concavity in the other three parameters. The positive part R of the full Hessian decomposition has an explicit coercive bound whenever either coupling is nonzero. Thus the full four-variable negative entropy Hessian has three strictly positive eigenvalues, and its remaining sign is equivalent to a single determinant inequality. The decoupled locus is handled separately.

`FOURIER_POSITIVE_IMBALANCE.md` proves a quantitative local count estimate, retaining two fifths of each local Fisher term. Shifting the three atom logarithms makes this prove the full four-variable Hessian sign for every nonnegative-imbalance base, without any restriction on the direction. Applying the same estimate without shifting gives the further sufficient criterion `Var(N) log(P/O)<=8/5`. In particular, every strict Fourier kernel with `O/P>=1/4` is certified in all four parameter directions.

The only Fourier directions still missing are same-sign pair-mean motion at bases with `Var(N) log(P/O)>8/5`. This is still a restricted commuting four-site family; arbitrary Hermitian directions and the unrestricted three-site milestone remain open.

Executed `verify_fourier_scalar.py`: PASS, four coefficientwise rational identities, including a generic symmetric 4-by-4 determinant update. Executed `verify_fourier_positive.py`: PASS, one further polynomial identity, two rational scalar comparisons, and 45 rational curvature cases with exact logarithm enclosures. Across the new Fourier continuation, totals are 69 polynomial identities, 70 exact Fourier projection-channel entries, 102 representative rational curvature cases, and two exact proof-shortcut obstructions. These are self-checks, not independent audits.

No global source resolution or historical-priority claim is made. The existing three prior route-obstruction certificates and earlier kernel searches remain archived unchanged. A separate numerical experiment is examining whether count Fisher information alone can pay the remaining mean interaction; it is an unproved candidate, not part of the new theorem.
