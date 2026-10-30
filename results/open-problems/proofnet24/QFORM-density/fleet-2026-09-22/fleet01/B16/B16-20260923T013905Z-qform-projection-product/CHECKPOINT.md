SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B16, 2026-09-23T01:39:05Z.
attacking: projection-product interaction: absorb the scalar Schur-aligned square inside a mixed Fresnel linearization without losing the original product source.

# Early substantive checkpoint: aligned-square mixed Fresnel

Status: SUPPORTING LEMMA DERIVED; full QFORM remains OPEN. This is the required early mathematical checkpoint, not a proof-status promotion.

Pinned inputs actually used:
- Claude mixed-Fresnel proof: yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837, proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md, especially the twisted L^p lemma and Theorem MF;
- designated partner fleet02/B16 r21: yspennstate/math-open-problems@45bff099504543528c3c7c78fba03f1b8cafeb16, proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B16/20260923T003232Z-fleet02-B16-QFORM-r21/REPORT.md.

## Lemma candidate, with complete core calculation

Let X_0,X_1,...,X_m be independent with densities at most one. Let a != 0, c in R^m, let U be an m x 2 matrix with orthonormal columns, and let M be an invertible symmetric 2 x 2 matrix. Let D be diagonal. Consider

Q = a (X_0 + a^{-1} c^T X)^2 + X^T(D+UMU^T)X + affine terms.

Equivalently the physical scalar-leaf cross vector is c and the leaf block is D+UMU^T+cc^T/a. Put W=[c,U] and Gamma=W^T W. Assume Gamma is invertible and every normalized row leverage

    l_j = w_j^T Gamma^{-1} w_j

is at most 1/2. Then the same regularized-Fresnel/BL mechanism as Theorem MF gives

    |phi_Q(t)| <= (4 pi)^(3/2) |a|^(1/2)
                  |det M|^(-1/2) det(Gamma)^(-1/2) |t|^(-3/2).      (C1)

The point is that the apparent singular Schur factor 1/a is exactly canceled before taking absolute values. To see it, diagonalize M orthogonally inside the two-dimensional U-space and Fresnel-linearize the two U-squares and also the aligned square (c^T X)^2/a. If eta is the auxiliary variable for the aligned square, its oscillatory factor is

    exp[- i a eta^2/(4t) + i eta c^T X].

The original scalar-leaf interaction contributes exp[2it X_0 c^T X] and the scalar square contributes exp[it a X_0^2]. Make the auxiliary change

    zeta = eta + 2t X_0.

Then exactly

    - i a( zeta-2tX_0 )^2/(4t) + it a X_0^2
      = - i a zeta^2/(4t) + i a zeta X_0.                     (C2)

With the usual epsilon>0 Fresnel regularization an extra factor exp[-epsilon(zeta-2tX_0)^2] has modulus at most one, so after integrating X_0 against its probability density the whole scalar factor has modulus at most one. Thus the leaf variables again factor coordinatewise into the twisted transforms from the source theorem, now at the three-dimensional row vectors (c_j,U_{j1},U_{j2}). Geometric BL after normalizing by Gamma gives the integral bound (4 pi)^3 det(Gamma)^(-1/2). The Fresnel prefactors are

    (|a|/(4 pi |t|))^(1/2) (4 pi |t|)^(-1) |det M|^(-1/2),

which proves (C1). Linear terms only translate Fourier arguments, and diagonal leaf terms are the already-valid twists. Passing epsilon down to zero uses the same domination/limiting argument as Theorem F/MF.

Combining (C1) with |phi|<=1 and

    integral_R min(1,K |t|^(-3/2)) dt = 6 K^(2/3)

gives a bounded continuous density with

    ||p_Q||_infinity <= 12 [ |a|/(|det M| det Gamma) ]^(1/3).  (C3)

## Exact-rank-three invariant

Suppose now the whole quadratic matrix has exact rank three and a is the chosen nonzero physical scalar pivot. Its Schur complement is S=UMU^T. Write c=c_E+c_perp with E=range(U), q=||c_perp||. Then

    det Gamma = q^2.                                           (C4)

The rank-three factorization

    A = a v v^T + Ubar M Ubar^T,
    v=(1,c/a),

has Gram determinant 1+q^2/a^2. Hence, for D3 equal to the absolute product of the three nonzero eigenvalues,

    D3 = |det M| (a^2+q^2)/|a|.                               (C5)

Define the transverse fraction

    eta_perp = q^2/(a^2+q^2).

Then (C4)-(C5) give the exact identity

    |det M| det Gamma / |a| = D3 eta_perp.                    (C6)

Therefore the new branch is

    ||p_Q||_infinity <= 12 (D3 eta_perp)^(-1/3) <= 12 eta_perp^(-1/3),  (C7)

because the target hypothesis gives D3>=1 in exact rank three.

This is pivot-uniform: there is no negative power of |a|. It is complementary to the earlier scalar-Schur half-Riesz estimates, whose constants deteriorate as a->0.

## Target-valid near-null test paid uniformly

Let g,u,v be orthonormal diffuse vectors on a leaf bank with max_j(g_j^2+u_j^2+v_j^2)<=1/2. For 0<delta<1 set

    a=delta,
    c=sqrt(delta(1-delta)) g,
    S=uu^T-vv^T.

Then

    A = [[delta,c^T],[c,S+cc^T/delta]]

has, on span(e_0,g,u,v), the 2x2 block

    [[delta,sqrt(delta(1-delta))],
     [sqrt(delta(1-delta)),1-delta]]

plus eigenvalues +1,-1. The 2x2 block is a rank-one projection, so the full nonzero spectrum is exactly {1,1,-1}; this is a genuine target instance for every delta. Here D3=1 and eta_perp=1-delta, hence

    ||p_Q||_infinity <= 12(1-delta)^(-1/3).

In particular for 0<delta<=1/2 the bound is at most 12*2^(1/3)<15.12 uniformly through the near-null limit. This branch is not paid by a naive square-peel certificate, which carries a negative power of delta.

## Designated partner applied and exact complementary degeneracy

For fleet02/B16 r21,

    Q_{m,delta}=delta X_0^2+2 sqrt(1+|delta|) X_0 Y+Z^2,

with Y=a_vec.X and Z=b_vec.X on the same leaf bank. For delta!=0 its Schur complement is

    S = b_vec b_vec^T - [(1+|delta|)/delta] a_vec a_vec^T,

while c=sqrt(1+|delta|) a_vec lies inside range(S). Thus q=0, det Gamma=0, and the new transverse theorem correctly does not apply. The designated partner's original-block mixed-Fresnel decomposition instead uses augmented rows (sqrt(1+|delta|) a_j,b_j), has Gamma=diag(1+|delta|,1), and proves

    ||p_Q||_infinity <= 3*2^(4/3)(1+|delta|)^(-1/3) <= 7.5595263.

So the partner result pays the exact same-bank endpoint where the Schur-transverse currency vanishes. This is an actual complementary application, not an independence claim about (Y,Z).

First remaining bridge after this checkpoint: in an exact-rank-three/high-leverage N3 survivor with 0<eta_perp<<1, either obtain a quantitatively admissible original-block augmented Gram packet (as in the partner family), or route to the already-paid volume/determinant/grouped-bank exits. The new lemma removes the near-null pivot itself from the transverse branch; only the small-angle/product-routing issue remains.
