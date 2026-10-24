SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B05, 2026-09-22T22:52:32Z.
attacking: combine the newest partner rank-two-bank aggregate theorem with the reverse-conditioned leakage result and identify the near-isotropic embedded-curvature endpoint.

# Newest-partner addendum: account03/B05 r19

After the main report was written, a fresh main read exposed the newer named-partner handoff account03/B05 run `20260922T223741Z-account03-B05-QFORM-r19`. Its canonical proof is

`yspennstate/math-open-problems@70f181cf738aa51ee6fb7043a329ac9e8b22c4ec:proofnet24/QFORM-density/fleet-2026-09-22/account03/B05/20260922T223741Z-account03-B05-QFORM-r19/REPORT.md`.

I read the complete pinned proof before applying it.

## Partner theorem actually applied

In the exact-rank-three three-bank geometry with one spectral-rank-two product bank and two spectral-rank-one product banks, let `B` be the compressed quadratic matrix on the two scalar-bank aggregates, let `kappa=sigma_min(B)`, and let

`mu=sum_(i in G1,j in G2,k in G3)|det A_{ijk}|`

be the full aggregate principal-triple determinant packet. The partner proves the exact Schur identity

`|det B| |lambda_S| = mu`

and, when `B` is invertible indefinite,

`||p_Q||_infinity <= 8*2^(3/4)*sqrt(5) (kappa mu)^(-1/4).`             (A.1)

In particular, on the fresh tripartite packet `mu>=1/512`, every subbranch with `kappa` bounded below is now quantitatively paid without selecting any physical triple. I therefore remove that non-isotropic one-rank-two-bank branch from this slot's conditional end-to-end debt.

## Interaction with this run's reverse-conditioning theorem

The main report of this run proves two complementary facts.

1. If the scalar-pair quadratic core is **zero**, reverse conditioning pays arbitrary quadratic leakage on the supplying banks before the reciprocal Jacobian is averaged.
2. If a nonzero scalar-pair cross core is present, two strong arms plus arbitrary bank leakage do **not** by themselves force a bounded base density: the exact product-law example

   `2XY+2XV+2UY+2UV = 2(X+U)(Y+V)`

   has the rank-two logarithmic singularity.

Thus the partner's remaining `kappa -> 0` debt cannot be closed merely by deleting the factor `kappa^(-1/4)` and appealing to a generic "two aggregate arms regularize everything" statement. The logarithmic obstruction shows that the third curvature must actually be spent.

Conversely, the main report's `QFORM-RANDOM-SLOPE-HALF-RIESZ-v1` shows that if this third curvature appears as a genuinely independent original-coordinate square, the logarithm is uniformly integrable even with arbitrary bank leakage and central cross coupling. Therefore the combined r19+B05 state isolates the correct endpoint:

**`QFORM-RANK2BANK-NEAR-ISOTROPIC-EMBEDDED-CURVATURE-v1`**

> In the partner's `mu>0` one-rank-two/two-rank-one packet, when the scalar pair is singular or `kappa` is arbitrarily small, spend the rank-two bank's *embedded* third curvature jointly with the nearly isotropic scalar pair, preserving the original-coordinate product law. A generic base-density two-arm estimate is impossible; a square/half-Riesz, curved-trace, or equivalent three-curvature argument is required.

This is a strictly narrower debt than arbitrary bank leakage. The partner r19 theorem pays the non-isotropic aggregate packet, this run pays zero-core arbitrary leakage and independent-square repair, and the unclosed case is precisely third curvature trapped inside the same rank-two bank near scalar-pair isotropy.

Full QFORM remains OPEN. No continuity conclusion is claimed.
