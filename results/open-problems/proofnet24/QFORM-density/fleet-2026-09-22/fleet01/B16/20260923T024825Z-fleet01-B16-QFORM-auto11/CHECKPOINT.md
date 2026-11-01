SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B16, 2026-09-23T02:48:25Z.
attacking: a null-hub plus dependent three-dimensional product-projection kernel, using definite planar curvature before any conditional projection-height normalization.

# Early substantive checkpoint — null hub + dependent projected triple

Programme: QFORM-DENSITY-3EIG-20260922. Full conjecture remains OPEN. This checkpoint is a supporting calculation, not a full solution.


Newest Claude source actually used: yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837:proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/COUNTEREXAMPLE_SEARCH.md. Its Theorem 5 / definite planar curved geometry is used below in the set-valued form |{y:y^T C y in E}| <= pi |E|/sqrt(det|C|) for definite 2x2 C.

Designated partner source actually used: fleet02/B16, yspennstate/math-open-problems@80f21f0a650baffd62c8b9e4d21babd30ade95f0:proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B16/20260923T012820Z-fleet02-B16-QFORM-r22/REPORT.md. Its definite-receiver theorem is the point-level version of the same area identity and confirms that dependence inside a planar projected pair is allowed; no projected-coordinate independence is introduced.

## Candidate theorem (proof below)

Let X be a real random variable with density f<=1. Let Z=(S,Y) in R x R^2 be independent of X and have an arbitrary joint probability density g with ||g||_infinity<=M. Let beta!=0 and let C be a definite symmetric 2x2 matrix. Put d=det|C|>0 and

    Q = 2 beta X S + Y^T C Y.

Then Q has an essentially bounded density and

    ||p_Q||_infinity <= 2 sqrt( pi M / (|beta| sqrt(d)) ).       (1)

The scaling is the rank-four determinant scale: for the 4x4 core matrix diag([[0,beta],[beta,0]],C), |det B|=beta^2 d, so (1) is 2 sqrt(pi M) |det B|^(-1/4).

The statement is invariant under translations of X,S,Y and under the determinant-one shear S -> S + h^T Y. Consequently it also permits arbitrary affine terms and arbitrary hub-to-Y linear cross terms after these changes of variables, while preserving independence between X and the entire dependent triple Z and preserving the joint density cap M.

## Proof calculation

After the harmless sign reflection of C, assume C is positive definite. Fix t. For s!=0, conditioning on Z=(s,y), the map x -> 2 beta s x + y^T C y is affine, hence the conditional density kernel is

    K_t(s,y) = [1/(2|beta s|)]
               f( [t-y^T C y]/[2 beta s] ).                    (2)

Thus p_Q(t)=int g(s,y) K_t(s,y) ds dy.

Fix u>0. If K_t(s,y)>u, put m=2|beta|u|s|. Since f<=1, necessarily m<1, hence

    |s| < 1/(2|beta|u).                                        (3)

Let E_m={x:f(x)>m}. Probability normalization gives |E_m|<=1/m. From (2), K_t>u also implies

    y^T C y in t - 2 beta s E_m.                               (4)

The value set on the right has one-dimensional Lebesgue measure at most

    2|beta s| |E_m| <= 1/u.                                    (5)

For every measurable E subset R, definite planar quadratic geometry gives

    |{y in R^2 : y^T C y in E}|
      <= pi |E| / sqrt(d).                                     (6)

Indeed w=C^(1/2)y reduces this to polar coordinates, where area{|w|^2 in E}=pi |E cap [0,infinity)|. Equation (6) is exactly the geometric ingredient behind the completed fleet02/B16 definite receiver theorem and the newest-Claude rank-two PSD estimate, now applied to the moving value set in (4).

Combining (3),(5),(6),

    |{(s,y): K_t(s,y)>u}|
       <= [1/(|beta|u)] [pi/(u sqrt(d))]
       = A u^(-2),

    A = pi/(|beta| sqrt(d)).                                   (7)

Use both ||g||_infinity<=M and int g=1. Layer cake yields

    p_Q(t)
      = int_0^infinity int_{K_t>u} g dz du
      <= int_0^infinity min(1, M A u^(-2)) du
      = 2 sqrt(MA),                                             (8)

which is exactly (1), uniformly in t. Tonelli applied to the conditional density formula gives absolute continuity.

## Product-projection corollary

If Z=(S,Y) is a genuine three-dimensional orthogonal projection of an independent cap-one product source on coordinates disjoint from X, any source-valid dimension-free 3D projection-density cap M_3 can be inserted in (1). Using the conservative weighted product-projection cap exp(3/2) already recorded in the fleet gives

    ||p_Q||_infinity <= 2 sqrt(pi) e^(3/4)
                        |beta|^(-1/2) d^(-1/4).                 (9)

No independence among S,Y_1,Y_2 is assumed.

## Why this is not a refuted cap-only indefinite step

The bounded joint projection density is not pushed through an indefinite 3D quadratic. The hub X is kept genuinely independent and integrated first; the remaining nonlinear payment is the finite-area PREIMAGE of a measurable VALUE SET under a definite 2D quadratic. This is exactly where dimension two matters. If C is indefinite, (6) fails because hyperbolic level strips have infinite area, matching the live two-sheet/X-ray correction.

## Remaining implication

This proves the exact null-hub rank-four kernel with one transverse linear projected direction and a definite planar receiver. It does not handle a nonzero hub quadratic coefficient a X^2 in the opposite-sign/indefinite Schur regime, nor arbitrary additional leaf curvature. The next target is a source-valid near-null interpolation that retains product provenance rather than treating a X^2 as a small random perturbation.
