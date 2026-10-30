SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B10, 2026-09-23T11:17:55Z.
attacking: near-null nonzero coloop interpolation; apply the completed scalar/dependent-pair kernel and close its remaining small-transverse-coefficient branch by an inverse-cofactor identity.

# Early substantive checkpoint — exact coloop curvature cannot disappear

Fresh owner direction assigns B10 to the near-null nonzero coloop interpolation. The completed fleet02/B05 theorem `QFORM-NEARNULL-SCALAR-DEPENDENT-PAIR-v1` gives, for an independent scalar X and an arbitrary dependent pair (C,D) of joint density cap M,

    Q=a X^2+2 beta X C+alpha C^2+2 delta C D+gamma D^2,
    B=[[a,beta,0],[beta,alpha,delta],[0,delta,gamma]],

    ||p_Q||_infinity <= 31 M^(2/3) |beta^2 gamma det B|^(-1/6).

Its source is `yspennstate/math-open-problems@5bf3d5e6765ecd1dd091fc7d862f6f04211c530f` for the exact-null endpoint and the completed near-null interpolation report currently at
`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B05/20260923T035943Z-fleet02-B05-QFORM-r21/REPORT.md`.

The B05 report left `|gamma|<1/2` as a mixed-transverse branch. In the exact coloop geometry this branch is actually impossible as an obstruction.

Assume B is real symmetric and `sigma_min(B)>=1`; in the target exact-rank-three state this follows from the three nonzero eigenvalues having modulus at least one. Then `||B^{-1}||op<=1`. Since

    (B^{-1})_11=(alpha gamma-delta^2)/det B,

we have

    |alpha gamma-delta^2| <= |det B|.                         (1)

Expanding the determinant along the first row,

    det B = a(alpha gamma-delta^2)-beta^2 gamma.              (2)

Hence for every `|a|<1`,

    |beta^2 gamma|
      >= |det B|-|a| |alpha gamma-delta^2|
      >= (1-|a|)|det B|.                                      (3)

In particular `gamma` cannot vanish in the near-null regime, and

    |beta^2 gamma det B| >= (1-|a|)|det B|^2 >= 1-|a|.        (4)

For an exact leverage-one physical coloop, the remaining two spectral coordinates are a two-dimensional orthogonal projection of the remaining independent ORIGINAL coordinates. The weighted product-projection theorem gives their joint density cap `M<=e`. Therefore B05's completed theorem plus (4) yields

    ||p_Q||_infinity <= 31 e^(2/3)(1-|a|)^(-1/6),             (5)

uniformly for every `|a|<1`. At `|a|<=9/10`, this is <88.626.

For `|a|>=9/10`, the completed scalar-pivot/rank-two half-Riesz estimate gives

    ||p_Q||_infinity <=16 sqrt(30)|a det B|^(-1/4)
                      <=16 sqrt(30)(10/9)^(1/4)
                      <89.975.                                (6)

Thus every exact leverage-one coloop in the exact-rank-three target is paid by a universal essential-density bound <90. The exact-null case is included (and has the sharper previously proved bound <9.276).

This closes the near-null nonzero coloop endpoint without treating `aX^2` as a small random perturbation and without assuming C,D independent.

Designated-partner use retained at a real inequality: fleet04/B10's `QFORM-REGRESSION-THREEBANK-CURVATURE-SPLIT-v1` applied to the preceding non-coloop mixed-row state gives

    rho_S M(G_Y,G_Z) >= (2/81) rho det G.

In the r23 normalization `G=I_2`, hence `rho_S M(G_Y,G_Z)>=2rho/81`. The new coloop theorem pays the boundary `rho=0`; the first remaining interpolation issue is therefore a product-safe receiver for arbitrarily small positive rho, not the exact coloop itself.

Status: new equation-level closure of the exact coloop near-null branch; full exact-rank-three theorem and full QFORM remain open. Continuity is not claimed by this argument beyond scopes of cited inputs.
