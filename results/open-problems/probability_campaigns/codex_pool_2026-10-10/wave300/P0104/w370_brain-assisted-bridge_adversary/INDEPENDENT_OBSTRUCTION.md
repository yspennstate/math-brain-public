# P0104 independent obstruction (saved before paired proof access)

2026-10-10. No w369 proof has been opened at this checkpoint.

Fix the fluctuation definition first: for positive variances V_n, let
chi_var = lim log(V_n)/(2 log n), if the limit exists. This is a variance
exponent, not automatically a tail, transversal, or convergence exponent.

The BKS upper bound V_n <= C n/log n implies only limsup
log(V_n)/(2 log n) <= 1/2. It gives V_n/n -> 0 but no fixed epsilon > 0
for which V_n = O(n^(1-epsilon)).

An exact countermodel to that inference is X_n = sqrt(n/log n) Z for a
single standard normal Z and integers n >= 3. Its variance equals n/log n
and its chi_var equals 1/2. For every epsilon > 0,
Var(X_n)/n^(1-epsilon) = n^epsilon/log n -> infinity. This is a
counterexample to an implication of inequalities, not an iid lattice FPP
counterexample. It leaves the original FPP problem open.

For any alpha in (0,1/2), X_n = n^alpha Z also obeys the same upper
bound eventually because log n/n^(1-2alpha) -> 0, yet chi_var = alpha.
Thus the upper bound alone cannot select alpha=1/3.

A minimal quantitative bridge for strict subdiffusivity would be a
fixed polynomial saving: for one epsilon > 0 and all sufficiently large
n, Var(T(0,ne_1)) <= C n^(1-epsilon). For chi_var=1/3 one needs
both eventual upper and lower exponent bounds, equivalently
Var(T(0,ne_1)) = n^(2/3+o(1)). Those remain proof obligations.

Local proof status: elementary derivation, independent referee w371 pending.
NEXT: Recover the exact primary-source target and the brain theorem card,
then audit the paired bridge without conflating exponent definitions.
