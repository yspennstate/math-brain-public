SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B03, 2026-09-24T10:11:39Z.
attacking: eliminate the special same-bank normal-form restriction in partner r51 by a determinant-invariant shear: arbitrary 2x2 same-bank curvature plus one zero-corner hyperbolic mode, then compare the leverage-free endpoint with the pinned Fresnel/localized receivers.

# Early calculation: bordered zero-corner determinant compiler

Programme: QFORM-DENSITY-3EIG-20260922. Full unrestricted theorem OPEN.

Let (S,R) have joint density rho with ||rho||_infinity<=M, and let V be independent with density cap N. Fix a,b !=0. The proof of account03/B03 r51 survives the more general form

    Q = a S^2 + 2 ell(R) S + h(R) + 2 b R V

with arbitrary measurable ell,h: for each r, shear s -> u=s+ell(r)/a. This map has Jacobian one, so the joint density cap stays M, and

    Q = a u^2 + H(r) + 2 b r V.

The r51 small-|r| / large-|r| split is uniform in the target translation H(r), hence

    ||p_Q||_(infinity,ess)
      <= 6 M^(2/3) N^(2/3) |a|^(-1/3)|b|^(-2/3).

Invariant 3-mode consequence. Let Y=(Y1,Y2) be two orthonormal projections of one genuine original-coordinate product bank, V a unit projection of a disjoint product bank, and

        B = [ C  g ]
            [g^T 0 ]

with C symmetric 2x2, g !=0, det B !=0. Rotate only the deterministic 2-mode coefficient basis so g=(0,gamma). The resulting projections remain a dependent pair from the same product bank; no probabilistic independence is asserted. Writing C'=[[a,c],[c,d]],

    det B = -a gamma^2.

The product-projection caps used in partner r51 are M<=2 and N<=sqrt(2). Therefore

    ||p_Q||_(infinity,ess) <= 12 |det B|^(-1/3).

For an actual physical triple (Y1,Y2,V)=(X1,X2,X3), M,N<=1 and the sharper bound is

    ||p_Q||_(infinity,ess) <= 6 |det B|^(-1/3).

Strict target test:

    B_* = [[3,1,0],[1,3,3],[0,3,0]],   det B_*=-27.

Its characteristic polynomial is lambda^3-6 lambda^2-lambda+27; sign changes place its roots in (-2,-1),(2,3),(5,6), so all three eigenvalues have modulus >1. Thus for arbitrary independent cap-one X1,X2,X3,

    Q_*=3X1^2+2X1X2+3X2^2+6X2X3

obeys

    ||p_(Q_*)||_(infinity,ess) <= 2.

The corresponding whole-copy estimate from convolution and the positive half-Riesz identity is

    E|Q_*-Q_*'|^(-1/2) <=4,
    int |t|^(-1/2)|phi_(Q_*)(t)|^2 dt <=4 sqrt(2 pi).

Next: write the full proof carefully, apply a completed pinned e5f71d79 theorem to this matrix/family, and record the diffuse embedding showing fixed physical minors may vanish while the bordered determinant remains order one.
