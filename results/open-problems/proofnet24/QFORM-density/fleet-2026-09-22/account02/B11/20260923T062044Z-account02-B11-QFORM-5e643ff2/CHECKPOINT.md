SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B11, 2026-09-23T06:20:44Z.
attacking: overlapping third-direction half-Riesz bridge for genuinely rotated (+,+,-)/(+,-,-) signatures via sign-specific Schur and ruled geometry.

# Early mathematical checkpoint — a two-sheet transverse-curvature identity

Programme: `QFORM-DENSITY-3EIG-20260922`. Full target remains OPEN.

I use only one genuinely independent scalar versus a possibly dependent two-dimensional pair. Let X have a probability density f, let Y=(Y1,Y2) be independent of X with joint density g satisfying ||g||_infinity<=M, and consider a translated quadratic form with symmetric matrix H of inertia (2,1). Assume the scalar pivot a>0 is a majority-sign pivot and the 2x2 pair compression C is positive definite. Orthogonally rotate the pair so the scalar cross vector is (beta,0), then use the determinant-one pair shear d=Y2+(delta/gamma)Y1. This preserves the pair density cap and puts

    Q = a x^2 + 2 beta x c + alpha0 c^2 + gamma d^2,

with alpha0>0, gamma>0. Since det H=gamma(a alpha0-beta^2)<0, put b=sqrt(beta^2-a alpha0)>0 and, after c -> -c if necessary, beta>b. Choose

    h=(beta-b)/a,   k=h/(2b)>0,   L=1+k a,

and make only the algebraic shear x=z-hc (no independence claim after the shear). Then

    Q = a z^2 + 2 b z c + gamma d^2.

For a two-sheet target t<0, solving for c gives

    c=(t-a z^2-gamma d^2)/(2 b z)

and therefore

    p_Q(t) <= M/(2b) * I_t,
    I_t = integral integral f(L z + k|t|/z + k gamma d^2/z) dd dz / |z|.

Set d=z y. The |z| Jacobian cancels the hyperbolic 1/|z| factor:

    I_t = integral_R integral_R f(A(y) z + H0/z) dz dy,
    A(y)=L+k gamma y^2,   H0=k|t|.

The exact pushforward density of z -> A z+H0/z is

    w_{A,H0}(u)=|u|/[A sqrt(u^2-4 A H0)] * 1_{|u|>=2 sqrt(AH0)}

(for H0=0 it is 1/A). Direct integration in y gives the identity

    integral_R w_{A(y),H0}(u) dy = pi/sqrt(L k gamma)

whenever the left side is nonzero, and the same value for H0=0. Hence, since integral f=1,

    I_t <= pi/sqrt(L k gamma).

Finally

    k L = alpha0/(4b^2),

so

    2 b sqrt(L k gamma)=sqrt(alpha0 gamma)=sqrt(det C).

Thus the new candidate theorem is

    p_Q(t) <= pi M / sqrt(det C),        t<critical value,

uniformly in the scalar pivot a>0 and in the scalar/pair cross coefficient. This is a genuinely two-sheet bound: if the third curvature gamma is deleted, the y-integral diverges, recovering the rank-two logarithmic endpoint rather than hiding it.

Source applications planned for the completed report: (i) Claude `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837` Theorem C pays the one-sheet side for an exact rank-three product projection by <=pi sqrt(2); (ii) account03/B11 `17813858a272da501b3902b59f53f1e15a366bf2` pays the complementary minority-scalar branch; (iii) account02/B16 `5bf3d5e6765ecd1dd091fc7d862f6f04211c530f` pays the exact-null coloop endpoint. The remaining debt after this checkpoint is the majority near-null branch with nearly singular pair compression det C -> 0, plus arbitrary higher-rank tails.
