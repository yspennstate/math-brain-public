SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B12, 2026-09-22T17:46:33Z.
attacking: whether conditioning on arbitrary added spectral directions admits a universal 2/3-moment bound for the conditional three-dimensional spectral-core density cap; explicit product-cube calculation refutes that bridge.

# account03/B12 handoff — conditional spectral-core cap moment is unbounded

Source control at final owner-message refresh: `yspennstate/math-research-brain@b8b58e8f3f112e9a835265bce1ebdb5c24b98411`, OWNER CONTROL revision `2026-09-22.10`.

Canonical proof: `yspennstate/math-open-problems@c8a12f4123a08228db723fe100be2126f6c8c6f5:proofnet24/QFORM-density/fleet-2026-09-22/account03/B12/20260922T174633Z-qform-eigenvalue-r14/REPORT.md`.

## New decisive correction

The owner-message full-rank bridge

`E_Z ||p_{Y|Z}||_infinity^(2/3) <= universal constant`

is false even for product uniforms and a three-dimensional block-constant spectral subspace. For `n=3m`, three independent `m`-coordinate cube blocks, and the block-constant directions `u_1,u_2,u_3`, the exact value is

`M_m = m^2 Gamma(4/3)^3 [Gamma(m)/Gamma(m+1/3)]^3`

and Wendel gives

`M_m >= Gamma(4/3)^3 m = 0.7120729426... m`.

Thus conditioning on the spectral complement and paying rank-three coarea through the conditional `L^infinity` cap cannot be universal.

This remains true for the actual additional-eigenvalue family

`A_{m,tau}=u_1u_1^T+u_2u_2^T-u_3u_3^T+tau(I-P_U)`, `tau>=1`,

whose spectrum is `{1,1,-1,tau,...,tau}`.

## Partner theorem applied

The designated account04/B12 location still has no current QFORM canonical run, so none was invented. The compatible completed account04/B18 theorem `QFORM-SCHUR-PIVOT-SMOOTHING-v1` was applied to the same family. A physical triple inside the first block has

`B_3=tau I_3-((tau-1)/m)J_3`,
`a>=1`, `det B_3>=tau^2`,

hence

`||p_Q||_infinity <= 2sqrt(pi)/sqrt(tau) <=2sqrt(pi)`.

So the conditional-moment divergence is a proof-interface failure, not a QFORM counterexample.

## Replacement obligation

Do not try to close full rank by bounding the conditional three-dimensional density cap moment. The next viable interface must average before taking a fiberwise supremum: an averaged coarea/fractional-trace functional, or an original-coordinate Schur/cross-bank mechanism retaining product provenance. The current rank-two affine half-Riesz theorem is compatible with that replacement.

Full QFORM remains OPEN. Continuity is not proved by this B12 result.
