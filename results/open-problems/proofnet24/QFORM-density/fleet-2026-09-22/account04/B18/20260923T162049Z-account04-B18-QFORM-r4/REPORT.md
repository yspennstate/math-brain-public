SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account04, slot B18, 2026-09-23T16:20:49Z.
attacking: source-valid LPP/pair-log transfer into the N3 null-hub near-singular branch.

# account04 B18 r4 — N3 pays every moderate null-hub edge

Status: NEW SUPPORTING TARGET-LEVEL SPLICE; FULL QFORM OPEN. Continuity is not claimed.

## Sources and exact scope

Fresh brain control/sign-in: math-research-brain@af96c54d7db58dc749ab024547c305a41327881a.

Applied predecessor: account01/B18 QFORM-NULLHUB-HEAVY-ANCHOR-PAIRLOG-v1, read at math-open-problems@8d6e85d072cd7a4c0fa9a37abe995a64109079e0, path:

    proofnet24/QFORM-density/fleet-2026-09-22/account01/B18/
    20260923T145330Z-account01-B18-qform-auto11-r34/REPORT.md

Its primary input is Livshyts--Paouris--Pivovarov, "On sharp bounds for marginal densities of product measures," Israel J. Math. 216 (2016), 877--889, arXiv:1507.07949. It is used only for a normalized one-dimensional marginal of the original product source, giving density cap sqrt(2). No rotated independence or conditional-density substitution is used.

The pair-log theorem is source-pinned at math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f and explicitly permits remainder-dependent affine shifts of the two original physical coordinates.

## Incoming theorem

In the exact null-hub normal form, leaf i has score

    q_i = beta_i^2 + g_i^2/gamma^2,

and physical pair

    B_i = [[0,g_i],[g_i,a_i]],   a_i=A_ii.

For g_i nonzero, account01 proves

    ||p_Q||_infinity
    <= 8 sqrt(2) [h D q_i kappa_i]^(-1/4),               (1)

where kappa_i=sigma_min(B_i). In the designated compiler with r>=1/2,

    h>=1/5,   D>=1.

Thus a heavy witness q_i>1/2 satisfies

    h D q_i > 1/10.                                      (2)

This is the completed account01 result applied at an actual inequality.

## Exact diagonal-to-singular-value conversion

For B=[[0,g],[g,a]],

    kappa(B)
      = (sqrt(a^2+4g^2)-|a|)/2
      = 2g^2/(sqrt(a^2+4g^2)+|a|).                       (3)

This is increasing in |g| and decreasing in |a|. Therefore

    |a|<=eta and |g|>=s
    imply kappa(B)>=(sqrt(eta^2+4s^2)-eta)/2.             (4)

Inside N3(1/64), |a_i|=|A_ii|<1/64. If the heavy witness also has

    |g_i|>=1/64,

then

    kappa_i > (sqrt(5)-1)/128.                            (5)

Combining (1), (2), and (5) gives

    ||p_Q||_infinity
    < 8 sqrt(2) [1280/(sqrt(5)-1)]^(1/4)
    = 64.1795826152... .                                  (6)

Call this QFORM-NULLHUB-DIAGONAL-GATED-PAIRLOG-v1.

It holds for arbitrary independent original-coordinate laws with densities at most one, with no moment, support, iid, smoothness, or post-rotation independence assumption.

## Sharpened live split

Within the exact-rank-three null-hub part of N3(1/64):

1. If every q_i<=1/2, the completed diffuse null-hub mixed-Fresnel theorem applies in its stated scope.
2. If some q_i>1/2 has |g_i|>=1/64, (6) pays the branch.
3. The only heavy witnesses still unpaid by this mechanism have |g_i|<1/64, including g_i=0.

This is sharper than merely recording kappa_i<1/10. The remaining state is a genuinely tiny original physical hub edge carrying a heavy transverse score.

The endpoint is real: q_i can exceed 1/2 solely because beta_i^2>1/2 while g_i is arbitrarily small or zero. Selecting another leaf is not justified by the aggregate score. At g_i=0 the physical pair is singular, so pair-log smoothing does not apply.

The next receiver must combine the large beta_i square with the aggregate g_- source while retaining original product provenance. The moving-ridge joint-cap barrier rules out replacing that provenance by an arbitrary bounded joint density.

## Remaining debt

The full conjecture remains open. The tiny-edge heavy null-hub endpoint, punctured convex/two-sheet collar, and arbitrary additional spectrum remain outside this theorem. Continuity is separate and is not supplied by the pair-log estimate.
