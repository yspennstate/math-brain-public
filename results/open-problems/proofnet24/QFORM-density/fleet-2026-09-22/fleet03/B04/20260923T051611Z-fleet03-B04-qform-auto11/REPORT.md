# fleet03/B04 — product-localized 3x3 closure without arbitrary-joint coarea

SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B04, 2026-09-23T05:16:11Z.

attacking: a product-preserving replacement for the invalid arbitrary-joint localized-coarea step, using the rank-two half-Riesz rearrangement endpoint plus the physical-pair logarithmic endpoint.

## Status

Full QFORM remains OPEN. This report proves a supporting theorem with all constants explicit. It applies to a full ambient quadratic form whenever one ORIGINAL-coordinate 3x3 principal block is quantitatively invertible. It uses only original-coordinate product structure and completed product-space estimates; it does not assume Gaussianity, log-concavity, moments, compact support, connected support, or independence after a rotation.

The result establishes absolute continuity and an essential L-infinity bound in its stated scope. It does **not** prove continuity for arbitrary merely measurable cap-one input densities.

## Exact theorem

### QFORM-LOCAL-3BLOCK-PRODUCT-CLOSURE-v1

Let X=(X_1,...,X_n) have independent real coordinates with probability densities f_i satisfying 0<=f_i<=1. Let A be any real symmetric n-by-n matrix. Suppose there is a set I of three ORIGINAL coordinates such that the principal block M=A_{I,I} satisfies

    sigma_min(M) >= s > 0.

Then the full ambient quadratic form Q=X^T A X has an essentially bounded density and

    ||p_Q||_infinity < 102/s.                                      (1)

All coefficients outside I and all couplings between I and I^c are arbitrary.

The theorem is product-specific: after conditioning on X_{I^c}, the three coordinates in I remain independent with their original density caps. No arbitrary three-dimensional joint-density coarea statement is used.

## Dependencies actually used

1. `QFORM-RANK2-AFFINE-HALF-RIESZ-v1`, complete supporting proof at

   `yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`

   `proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`.

   When an invertible symmetric 2x2 quadratic form has arbitrary affine term lying in its range, including every affine term in R^2, the source proves

       sup_t E |Y^T S Y + ell^T Y - t|^(-1/2)
           <= 16 sqrt(30) |det S|^(-1/4).                         (2)

2. `QFORM-RANK3-INDEFINITE-PAIR-PIVOT-v1`, complete supporting proof at

   `yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`

   `proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`.

   For a rank-three ORIGINAL-coordinate block whose three eigenvalue magnitudes are at least one, and an invertible indefinite physical 2x2 principal pair B with

       D=|det B|,   kappa=sigma_min(B),

   the full ambient form, including arbitrary outside couplings and affine terms after conditioning, obeys

       ||p_Q||_infinity <= 8 sqrt(5) (D kappa)^(-1/4).             (3)

Both inputs retain original-coordinate product provenance. The second is logarithmic near the hyperbolic critical value rather than asserting a false uniformly bounded rank-two indefinite density.

The designated partner `fleet04/B04` had current QFORM login/start records but no completed current-QFORM canonical report or shared handoff visible in the fresh direct repository lookup for this run. No partner theorem is fabricated.

## Proof of (1)

By conditioning on X_{I^c}, it is enough to prove a uniform statement for three independent cap-one variables x=(x_1,x_2,x_3) and

    F(x)=x^T M x + ell^T x + c,                                  (4)

where ell and c are arbitrary deterministic quantities depending on the conditioned outside coordinates.

Scale by s. Replacing M by N=M/s and ell by ell/s divides the output by s; hence a density bound C for sigma_min(N)>=1 becomes C/s for the original form. We therefore assume throughout the proof that

    sigma_min(M) >= 1.                                           (5)

Because M is real symmetric, all three eigenvalue magnitudes are at least one, so

    |det M| >= 1,    ||M||_F^2 >= 3.                             (6)

Fix the threshold

    delta = 11/20.                                                (7)

We split into two exhaustive physical-coordinate cases.

### Case A: a scalar physical pivot has |M_ii| >= 11/20

Relabel so a=M_11 and |a|>=delta. Write

    M = [ a   b^T ]
        [ b    C  ]

with b in R^2 and C symmetric 2x2. Complete the square in the ORIGINAL coordinate x_1:

    F(x)
      = a (x_1 + a^(-1)b^T y + d)^2
        + y^T S y + eta^T y + c',                               (8)

where y=(x_2,x_3), d,eta,c' are deterministic after the outside conditioning, and

    S = C - a^(-1) b b^T.                                       (9)

Since det M = a det S and det M is nonzero, S is invertible. Conditional on y, the one-variable square pushforward has the elementary density envelope

    p_{a(X_1+m)^2}(u) <= |a|^(-1/2) |u|^(-1/2)                  (10)

on the appropriate half-line; translation of X_1 does not alter the density cap. Therefore, for almost every t,

    p_F(t)
      <= |a|^(-1/2)
         E |t-(Y^T S Y + eta^T Y + c')|^(-1/2).                 (11)

Because S is invertible, eta lies in range(S)=R^2. Applying (2),

    ||p_F||_infinity
      <= 16 sqrt(30) |a|^(-1/2) |det S|^(-1/4)
      = 16 sqrt(30) |a|^(-1/4) |det M|^(-1/4)
      <= 16 sqrt(30) delta^(-1/4).                               (12)

With delta=11/20,

    C_A = 16 sqrt(30) (20/11)^(1/4)
        = 101.7630084433... < 102.                               (13)

The strict inequality can be checked without floating point by taking fourth powers:

    C_A^4 = 16^4 30^2 (20/11)
          = 1,179,648,000/11
          < 102^4 = 108,243,216.                                (14)

### Case B: every physical diagonal satisfies |M_ii| < 11/20

From (6),

    2 sum_{i<j} M_ij^2
       = ||M||_F^2 - sum_i M_ii^2
       > 3 - 3(11/20)^2
       = 837/400.                                                (15)

Hence some off-diagonal entry b=M_ij obeys

    b^2 > 279/800,
    |b| > sqrt(558)/40.                                         (16)

Let the corresponding physical 2x2 principal pair be

    B = [ alpha   b ]
        [ b      beta ],                                        (17)

where |alpha|,|beta|<11/20. Then

    det B = alpha beta - b^2
          < (11/20)^2 - 279/800
          = -37/800.                                            (18)

Thus B is invertible and indefinite, with

    D=|det B| > 37/800.                                         (19)

To lower-bound its smallest singular value, compare with

    B_0 = [0 b; b 0].

The perturbation diag(alpha,beta) has operator norm <11/20 and sigma_min(B_0)=|b|. Weyl's singular-value inequality gives

    kappa=sigma_min(B)
       > sqrt(558)/40 - 11/20
       = (sqrt(558)-22)/40.                                     (20)

Apply the product-preserving pair-log theorem (3). Since the normalized three-coordinate block has all eigenvalue magnitudes at least one,

    ||p_F||_infinity
      < 8 sqrt(5)
        [ (37/800) ((sqrt(558)-22)/40) ]^(-1/4)                 (21)

    = 8 sqrt(5)
      [37(sqrt(558)-22)/32000]^(-1/4)

    = 85.9602676479... < 102.                                  (22)

For a purely rational certificate of the last inequality, note 23.62^2=557.9044<558, hence sqrt(558)-22>1.62. Therefore

    D kappa > 37*1.62/32000 > 0.00187,                           (23)

whereas

    (8 sqrt(5)/102)^4 = 102400/102^4 < 0.000947.                (24)

Thus the fourth power of the right side of (21) is strictly less than 102^4.

Cases A and B are exhaustive, proving the normalized bound <102. Undoing the scaling by s proves (1). Finally, the conditional bound is uniform in the outside coordinates, so averaging the conditional densities proves the same bound for the full ambient Q. QED.

## Why this repairs a previously invalid localized interface

The live programme correction `QFORM-JOINT-DENSITY-COAREA-23-FALSE-v1` shows that an arbitrary bounded 3D joint density can concentrate in a thin quadratic shell and produce arbitrarily large output density. Therefore a proof cannot rotate a product law into a bounded 3D density and then invoke a generic coarea estimate.

The theorem above avoids that failure completely. It conditions only on outside ORIGINAL coordinates, retains independence of the selected three scalar inputs, and then uses two product-specific endpoints. In particular, it provides a rigorous product-law replacement for the informal statement "a uniformly invertible physical 3x3 principal block is localized and therefore harmless."

## A genuinely rotated indefinite family missed by every physical-pair pivot

Consider the 3x3 block

    M_* = [ 1   1   1 ]
          [ 1   1  -1 ]
          [ 1  -1   1 ].                                      (25)

It has exact spectrum

    spec(M_*) = {2,2,-1},                                      (26)

so sigma_min(M_*)=1. It is genuinely non-diagonal and indefinite. Yet every physical 2x2 principal determinant is zero:

    det M_*[{1,2}] = det M_*[{1,3}] = det M_*[{2,3}] = 0.      (27)

Thus a strategy requiring one invertible physical pair fails maximally on this target block.

The scalar-pivot branch closes it. Pivoting coordinate 1 gives

    a=1,
    b=(1,1)^T,
    C=[1 -1; -1 1],

and hence

    S=C-bb^T = [0 -2; -2 0],
    det S=-4.                                                   (28)

Equation (11) together with (2) yields the sharper explicit bound

    ||p_F||_infinity
      <= 16 sqrt(30) * 4^(-1/4)
      = 16 sqrt(15)
      = 61.9677335393... .                                     (29)

This survives arbitrary affine perturbations of the three selected coordinates.

Consequently, for every dimension n>=3 and every real symmetric full matrix A whose principal block on some three ORIGINAL coordinates is M_*, **all remaining entries of A may be arbitrary**, and every admissible product input law satisfies

    ||p_{X^T A X}||_infinity <= 16 sqrt(15).                    (30)

By Cauchy interlacing, such a full A automatically has at least two eigenvalues >=2 and at least one eigenvalue <=-1, so (30) is a genuine target-level family under the three-large-eigenvalue hypothesis. It is not a diagonal or Gaussian control.

Continuity is not asserted by this argument.

## Relation to the current high-leverage / low-tail debt

The preceding B04 run established a spectral-commuting third-volume gate for diffuse/high-tail physical cross blocks. The present theorem changes mechanism and pays the opposite kind of certificate: once any three ORIGINAL coordinates carry a uniformly invertible principal block, there is no need to route through an arbitrary-joint coarea argument or select an invertible physical pair. The scalar-pivot and indefinite-pair branches are exhaustive at the 3x3 block level.

What remains unpaid for full QFORM is structural, not this local analytic endpoint: from the bare condition s_3(A)>=1, either produce such a uniformly conditioned original 3x3 principal block, or show quantitatively that its failure forces one of the already-paid aggregate grouped-star/ridge/volume-tail mechanisms. Known diffuse families show that a uniformly good 3x3 block is not automatic, so this theorem is not a full solution.

## Correction awareness and scope

This proof does not use:

- law-uniform pointwise van-der-Corput decay;
- independence after an orthogonal diagonalization;
- the refuted arbitrary-joint 3D coarea estimate;
- positive moments of conditional projection-density suprema;
- naive fiber-sup integration;
- a claim that one physical pair is always uniformly invertible.

It uses only the exact product-law scopes (2) and (3), both with arbitrary affine terms as required by outside conditioning.

Claim ID: `QFORM-LOCAL-3BLOCK-PRODUCT-CLOSURE-v1`.

Full QFORM status: OPEN.
