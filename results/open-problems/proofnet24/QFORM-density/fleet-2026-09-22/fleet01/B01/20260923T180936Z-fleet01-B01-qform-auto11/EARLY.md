SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B01, 2026-09-23T18:09:36Z.
attacking: the critical two-original-hub rank-two cross packet at zero hub self-curvature by a direct distribution-function estimate rather than an L1 Fourier bound.

# Early calculation: the critical k=2 crossing is directly bounded when the two hubs have zero quadratic self-block

Let H=(H1,H2) be two ORIGINAL independent coordinates with densities <=1. Let W be a disjoint tuple of ORIGINAL independent coordinates, independent of H. Let L=L(W) in R^2 have a density g with ||g||_infinity<=M, and let R(W) be arbitrary measurable. For

    Q = 2 H . L(W) + R(W),

condition on W. If l!=0, the conditional density k_l of 2(l1 H1+l2 H2) satisfies

    ||k_l||_infinity <= 1/(2 max(|l1|,|l2|)) <= 1/(sqrt(2)|l|).

Therefore

    ||p_Q||_infinity <= (1/sqrt(2)) E |L|^{-1}.

Since g<=M and has mass one,

    E|L|^{-1}
      = integral_0^infinity P(|L|<1/t) dt
      <= integral_0^infinity min(1, pi M/t^2) dt
      = 2 sqrt(pi M).

Hence

    ||p_Q||_infinity <= sqrt(2 pi M).                 (E1)

If L=CW+d for a rank-two 2xm matrix C, the source-valid product projection theorem gives

    M <= 2/[s1(C)s2(C)].

Thus

    ||p_Q||_infinity <= 2 sqrt(pi) [s1(C)s2(C)]^{-1/2}
                     = 2 sqrt(pi) det(CC^T)^(-1/4).    (E2)

This is exactly the Fourier-critical rank-two crossing for which the generic Plancherel estimate only gives |phi(t)|=O(|t|^-1). The direct small-ball/slicing estimate closes it without any third scalar pointwise Fresnel decay and allows arbitrary same-bank remainder R(W).

Regularity: for a.e. l, l1*l2!=0 because L has a 2D density. Then k_l is the convolution of two L1 densities and is C0. The displayed integrable envelope gives dominated convergence, so p_Q is continuous and vanishes at infinity.

Sharp scope warning. One cannot add an arbitrary hub bilinear term to this theorem using only the slope-density cap: with independent Uniform[-1/2,1/2] variables H1,H2,Y1,Y2,

    2 H1 H2 + 2 H1 Y1 + 2 H2 Y2 + 2 Y1 Y2
      = 2(H1+Y2)(H2+Y1)

has a logarithmically unbounded density at zero. Its matrix has rank two (eigenvalues +2,-2), so this is NOT a counterexample to the three-large-eigenvalue conjecture; it identifies the exact rank-two obstruction that the third spectral resource must remove.

Full proof, target stress family, designated-partner application, and refreshed source pins will follow in REPORT.md. Full QFORM remains OPEN.
