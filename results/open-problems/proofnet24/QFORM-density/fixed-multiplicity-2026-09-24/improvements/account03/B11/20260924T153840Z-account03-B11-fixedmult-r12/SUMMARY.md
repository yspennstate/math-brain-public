# B11 result summary

The current nine-eigenvalue paper (source commit eeb752c8943536541b34b42b8bf48e924f4d3d2f, 955 lines) was read end to end. Verdict: PASS for the written bound 400 K^2/s; no theorem-breaking gap was found in this review.

New theorem: sign-resolved Schur spectral counts, including singular ambient matrices, and the following target-level branch. If s_3(A)>=s and a physical indefinite 2-by-2 principal pivot has determinant magnitude at least s^2/400, then the density is bounded by 392.5 K^2/s. Essential boundedness only; continuity is not proved.

Authoritative proof: INDEFINITE_PAIR_TARGET_BRANCH_CORRECTED.md. The earlier sibling file without CORRECTED is a failed transport copy with escape-character corruption.

The completed account04/B11 Schur-sharpness family was applied to a strict target matrix with spectrum {1.1,-1.1,1,0,0}; the resulting concrete inequality is density <392.5 for every cap-one product input.

Still open: general s_8 endpoint, unrestricted three-eigenvalue theorem, and global continuity.
