# MOC4 handoff — account01/B09 dense anchored-marginal lift refuted

Run: `20260922T035002Z-b09-moc4-r11`  
Outcome: **CANDIDATE_REFUTED** for `MOC4-DENSE-ANCHOR-MARGINAL-LIFT-v1`; parent MOC4 remains **OPEN**.  
Scientific report: `yspennstate/math-open-problems/proofnet24/collective-MOC4/account01/B09/20260922T035002Z-b09-moc4-r11/REPORT.md`, blob `ac3bec22cb51296419870e462aa83e585795088a`. Exact verifier blob `5366b7f0d8304e3992cbee237de9c44ade4267a4`; captured PASS blob `089192060663f66467c707d54183b799d6126f1f`.

## Inputs actually consumed

- Campaign lead account03/B07 `MOC4-V4-PAIR-GAP-CEILING-v1`, blob `28cbce0f0a6213c0760e0777a5baa5b0de12b31a`: every genuine violation satisfies `0<gamma<=(3d-Delta-G/2)/4`; the positive-reserve branch remains.
- Assigned partner account02/B07 `MOC4-ONE-CYCLE-NORMAL-CONE-v1`, blob `0c82b0d30738d20a146e52abb4b7ba8e410f128c`, plus its earlier `MOC4-BIRAYLEIGH-ORBIT-v1` stationarity theorem.
- OTHER-account account04/B09 `MOC4-ZERO-ANCHOR-MARGINAL-LIFT-v1`, blob `1bf0fbe7d01f0fe659df5ecc12bbd9b5d98667b5`, whose 18-state zero-anchor inequality is extended below to all 24 permutations.

## New exact projected-lift theorem and dense violation

For `sigma in S4`, define

`ell = 1[sigma(1)=3]+1[sigma(2)=1]+1[sigma(3)=2]-1[sigma(1)=2]-1[sigma(2)=3]-1[sigma(3)=1]`

and let `c=[[0,2,1],[1,0,2],[2,1,0]]` on indices `1,2,3`. Then every one of all 24 permutations satisfies

`ell(sigma)+sum_ij c_ij 1_{sigma({0,i})={0,j}} >= 0`.

For `sigma(0)!=0` this is the account04/B09 18-state inequality. For `sigma(0)=0`, the six values are `0,3,3,3,6,3`. Hence any `S4` law matching singleton marginals `P_rc` and only nine anchored two-set marginals `Q_ij` must satisfy

`P13+P21+P32-P12-P23-P31 + 2Q12+Q13+Q21+2Q23+2Q31+Q32 >= 0`.

A dense exact rational orthogonal `U` (all 16 entries and all 36 two-by-two minors nonzero) violates this necessary inequality by

`-10349074315776 / 1167289931640625 < 0`.

Thus even this much weaker projected common-permutation coefficient lift fails away from zero-entry and vanishing-minor faces.

## Genuine simple-complex target datum

With the same `U` and spectra

`a=(-4+4i,-i,-3+2i,-4-4i)`,  
`b=(-4-4i,2-i,2-4i,4-i)`,

both normal matrices have simple nonreal spectra. The exact determinant has a strictly positive three-vertex target-hull certificate using `80-240i`, `64+256i`, `-280+120i`; the triangle doubled area is `172800`. Therefore this is **not** an MOC4 counterexample.

Direct use of account02/B07 `MOC4-BIRAYLEIGH-ORBIT-v1`: for `eta=1`, the true column-pair `(0,3)` derivative is exactly

`3697747106152704 / 6939892578125 != 0`.

So this coefficient-lift adversary is not a support maximizer in that direction. It is a clean negative control: universal positive lifting is too strong, while maximizer-local geometry remains viable.

## Remaining obligation

The first target-level gap is still the lead's `MOC4-RESIDUAL-PR-RESERVE-v1`: on positive endpoint reserve, exclude a genuine common-unitary maximizing support gap using `P-R-D` compatibility plus pair-Rayleigh/Cartan/odd-Weyl structure, or construct a true unitary/spectrum counterexample. The present result shows that replacing this by a projected classical matching law cannot work.

Execution: `WITHOUT_VERIFIED_BRAIN`; no benchmark gold, credential, scheduler identifier, machine path, email/Drive action, public posting, paid model/API/Codex, remote workflow, or permission change.
