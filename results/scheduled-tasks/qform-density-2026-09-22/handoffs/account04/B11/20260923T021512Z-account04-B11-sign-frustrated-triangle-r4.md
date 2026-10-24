# account04/B11 handoff — 20260923T021512Z

Status: `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN / WITHOUT_VERIFIED_BRAIN`

Source pins:

- required Claude package: `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`
- current source blobs: `RESULTS.md@62e20ee976ddeb3f42d3ee5befd6ed49edc917a5`, `FOURIER_ROUTE_REPORT.md@9da148eed6cd43b1046a6f91d0f9329e12921cb4`, `COUNTEREXAMPLE_SEARCH.md@ee721b237e206f31298b1871979faaab37a1bac2`
- account01/B11 Schur source: `REPORT.md@f696979d58d0e6fcc39a7a519405c1591a34b53a`
- newest account01/B11 Lorentz source: `REPORT.md@d08cde8957cf615c877b28a70ad069848dc47cdb`
- brain controls consumed: owner revision `2026-09-22.15`; request blob `165c570...`; corrections blob `c700...`; memory protocol blob `0d902...`

New theorem: if an actual physical triple has positive diagonals `a_i`, normalized off-diagonals within `eta<1/2` of signs whose triangle product is `-1`, then its smallest singular value is at least

`sigma=min_i a_i (1-2 eta)`.

Conditioning all outside original coordinates preserves the product fibre. On its moving one-sheet side, the ruled theorem gives `pi sqrt(2)/sigma`. The convex/two-sheet side is paid separately by account01/B11 majority-sign Schur smoothing:

`4 C_bin^(3/4)(a_i |det H|)^(-1/4)`.

The full target-level bound is the minimum of the best Schur bound and `6 sqrt(pi)/sigma`.

Exact endpoint: if every physical `2x2` principal determinant is zero and `rank A>=3`, some active triangle is sign-frustrated. For that triple the normalized eigenvalues are `{2,2,-1}` and `|det H|=4a_1a_2a_3`. This closes the exact all-pairs-null chamber at fixed diagonal scale, with arbitrary outside spectrum/couplings.

First unpaid implication: aggregate the balanced-sign near-rank-one chamber. Large dimension can accumulate many small normalized edge defects into two additional spectral directions while every single physical triangle stays weak. Route this collective defect to cross volume, disjoint innovations, or a quantitative pivot; do not delete it as a small quadratic error under unbounded inputs.

Canonical report path:

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B11/20260923T021512Z-account04-B11-sign-frustrated-triangle-r4/REPORT.md`

