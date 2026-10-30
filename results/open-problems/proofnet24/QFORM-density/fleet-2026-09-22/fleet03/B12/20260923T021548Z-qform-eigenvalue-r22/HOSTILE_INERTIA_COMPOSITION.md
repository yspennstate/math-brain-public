# Addendum: compose the new pivot chain with B12's preceding hostile-inertia theorem

The immediately preceding B12 run, `20260923T014701Z-qform-eigenvalue-r22`, was restored from its worker-owned memory after the first r22 bundle was written. Its canonical report is

`yspennstate/math-open-problems@2b9f9ccd93e8df4a7bb6b6f4bd3ec351c286976c:proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B12/20260923T014701Z-qform-eigenvalue-r22/REPORT.md`.

That run proved the cofinite one-sided spectrum theorem: if an `n x n` terminal matrix `H` has, for one sign,

`d=min{n-N_+(H;L), n-N_-(H;L)} <= n-3`,                         (A.1)

then every cap-one product input gives

`||p_(X^T H X)||inf <= C_d/L`,
`C_d=2 sqrt(6 pi (d+3)).`                                       (A.2)

It also proved the hostile-inertia perturbation rule: if `H=H0+E`, `N_+(H0;L)>=n-k` and `nu_-(E)<=r` (or the sign-reversed analogue), then (A.1) holds with `d=k+r`. Magnitudes and orientations of the added eigenvalues are unrestricted; same-sign additions are free.

Combining (A.2) with the scalar-pivot chain theorem of the present run gives a strictly stronger additional-spectrum statement.

## Theorem A — pivot chain followed by a hostile-inertia terminal

Suppose `k_chain` original-coordinate scalar Schur eliminations satisfy

`|a_j|>=tau L`

and the terminal Schur matrix `H` satisfies (A.1). Then the original form has density cap

`boxed:
 ||p_Q||inf <= L^(-1) max{2 sqrt(6 pi(d+3)),16/tau}.
}`                                                                  (A.3)

If instead the terminal matrix is represented as `H=H0+E` with a positive threshold packet satisfying

`N_+(H0;L)>=n-k0,   nu_-(E)<=r,   k0+r<=n-3`,                    (A.4)

then

`boxed:
 ||p_Q||inf <= L^(-1) max{2 sqrt(6 pi(k0+r+3)),16/tau}.
}`                                                                  (A.5)

The negative-sign version is identical.

### Proof

The preceding run gives the terminal cap (A.2), or (A.2) with `d=k0+r` by its hostile-inertia theorem. The present run's recurrence

`T_tau(B)=4 sqrt(B/tau)=sqrt((16/tau)B)`

propagates any terminal normalized cap `B` backward through an arbitrary chain length with final normalized cap at most `max(B,16/tau)`. Insert `B=C_d`. QED.

At `tau=1`, the first few constants are

- `d=0`: `max(2sqrt(18pi),16)=16`;
- `d=1`: `17.366430109398422...`;
- `d=2`: `19.41625912555699...`;
- `d=3`: `21.269446210866192...`.

The point is not the numerical constants but the currencies: **chain length is free after the fixed point is reached, helpful-sign added inertia is free, and only the terminal hostile one-sided deficiency is charged.** This applies even if the added eigendirections are dense in the physical coordinates and do not commute with the baseline.

Consequently the high-rank no-pivot terminal identified in the main report is already paid whenever one one-sided threshold deficiency is bounded. The genuinely unpaid high-rank terminal must have **both** one-sided deficiencies large and also fail the current diffuse/collective-tail exits. That is a sharper remaining obstruction than the main report stated before restoring the immediately preceding B12 memory.

Continuity is not asserted by this composition; it is an essential-L-infinity bound.
