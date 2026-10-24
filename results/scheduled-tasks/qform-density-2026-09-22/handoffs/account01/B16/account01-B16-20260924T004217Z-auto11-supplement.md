# Source-pinned supplement — account01/B16 `account01-B16-20260924T004217Z-auto11`

- Programme: `QFORM-DENSITY-3EIG-20260922`.
- Full target: **OPEN / NOT PROVED / NOT DISPROVED**.
- Execution: `WITHOUT_VERIFIED_BRAIN`.
- Canonical supplement mathematics: `yspennstate/math-open-problems@70872ade53c0602c70d6313bb4c088be2d8dcc7f`, path `proofnet24/QFORM-density/fleet-2026-09-22/account01/B16/account01-B16-20260924T004217Z-auto11/SUPPLEMENT.md`, read-back blob `1e18e6af4f231fa67d757c0a0c7221f8e9bc4820`.
- Main report from the same run remains `@f09e25a5a88982c08b2d91359a9c6e87e9e7f8a2`.
- Completed designated partner actually used: account02/B16 r37 `@c9c865f02890e5fe7108c49759ee82b84f42ee38`.
- Projection input: `@e5f71d79eff325201dd0274053d20268ce65b837`.

## New theorem

`QFORM-HUBPHASE-TWOBANK-CROSSSQUARE-v1`.

Let a cap-`L_H` fresh hub `H` and two original source banks `A,B` be mutually independent. Suppose the two-dimensional projections `(L_i,V_i)` of bank `i` have joint density caps `M_i`. Allow arbitrary real measurable phases `R_H(H),R_A(X^A),R_B(X^B)`. For

`Q=R_H(H)+2 alpha H(L_A+L_B)+lambda(V_A+V_B)^2+R_A+R_B+affine`,

with `alpha lambda !=0`,

`||p_Q||_infinity <= 3 [L_H^2 M_A M_B/(alpha^2 |lambda|)]^(1/3)`,

and the density is continuous and vanishes at infinity.

Proof currency: phase-weighted bank pushforwards obey `||h_i||_2^2<=M_i`; 2D Plancherel gives `||Phi_i||_2<=2pi sqrt(M_i)`. One Fresnel representation for the aggregate square and the physical change of variables `eta=2 alpha t h` yield

`|phi_Q(t)| <= pi^(3/2)L_H sqrt(M_A M_B)|alpha|^(-1)|lambda|^(-1/2)|t|^(-3/2)`.

This retains dependence inside each projected pair and uses only independence of the original source banks.

For orthonormal pair projections of cap-one product banks, the actual bounded-density projection theorem gives `M_A,M_B<=2`, hence

`||p_Q||_infinity <=3*2^(2/3)|alpha|^(-2/3)|lambda|^(-1/3)`.

## Strict target family

For arbitrary orthonormal projected pairs in two product banks, arbitrary `theta in R`, same-bank perturbations `||E_A||_op,||E_B||_op<=1/4`, and one extra independent cap-one coordinate `W`,

`Q_theta=theta H^2+2H(L_A+L_B)+(V_A+V_B)^2+(X^A)^TE_AX^A+(X^B)^TE_BX^B+W^2`

satisfies

`||p_(Q_theta)||_infinity<=3*2^(2/3)<4.763`.

The normalized carrier has `H,ell` block roots `(theta +/- sqrt(theta^2+8))/2`, aggregate `v` eigenvalue `2`, and exact independent `W` eigenvalue `1`. The large root has modulus at least `sqrt(2)`; the `1/4` perturbation leaves it above one and leaves the `v` eigenvalue above one, while `W` stays exactly one. Hence at least three eigenvalues have modulus at least one for every `theta`.

## Updated B16 debt

The fresh hub square is now harmless on both: (i) the nonzero r37 punctured packet, by the main report's hub-phase lift; and (ii) the exact zero-puncture two-bank cross-square packet, by this supplement. The remaining issue is structural reduction of the generic near-coloop leaf quadratic to one of these source-preserving packets with quantitative transverse currency. No bare dependent joint-density/coarea shortcut is permitted.
