SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B14, 2026-09-22T20:15:07Z.

# account04/B14 handoff — law-level mixture localization

Status: `SUPPORTING_THEOREM_PROVED / FULL_TARGET_OPEN / CONTINUITY_NOT_TRANSFERRED / WITHOUT_VERIFIED_BRAIN`.

Canonical mathematics: `yspennstate/math-open-problems@321ec7899f4972d125d641408512fe9e5e9dcf4c`, path `proofnet24/QFORM-density/fleet-2026-09-22/account04/B14/20260922T201507Z-account04-B14-mixture-localization-r4/REPORT.md`.

New theorem `QFORM-LAW-LEVEL-FINITE-MIXTURE-LOCALIZATION-v1`: every cap-one probability density is an (L^1) limit of finite convex combinations of indicators (1_E), where every (E) is a compact finite union of intervals of total length one. The proof is constructive after compact replacement: conditional expectation on a mesh (1/M) gives a vector in the hypersimplex ({a\in[0,1]^N:\sum a_j=M}), whose vertices are exactly the (0)-(1) vectors with (M) ones.

Coordinatewise expansion shows every cap-one product law is a total-variation limit of finite mixtures of product-indicator laws. Pushforwards contract total variation. Hence any uniform interval inequality proved for finite-fragment indicators transfers simultaneously to all intervals and all cap-one product inputs with exactly the same constant. This is stronger than choosing a different bathtub extremizer for each interval.

Assigned partner account01/B14 r18 was applied to the genuine diffuse family (A_m=[1]\oplus J_m/m\oplus(-J_m/m)). Its finite-fragment component estimate compiles to
[
\|p_{X_0^2+U_m^2-V_m^2}\|_\infty\le\pi\sqrt2<4.443
]
for arbitrary independent cap-one densities, uniformly in (m), and remains valid with the partner's arbitrary range-aligned outside blocks/couplings.

The theorem transfers essential boundedness, not continuity: total-variation limits of continuous densities need not be continuous. Full QFORM remains open. The first localization-specific obstruction is still kernel leakage (P_{\ker B}C) in the active/outside affine quotient.

Fresh control: OWNER revision `2026-09-22.15`; live correction inbox blob `c7000cf3822ae4935a2faf43b89ac92ea65ac0fe`. No scheduler or notification state was changed.
