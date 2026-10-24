SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B06, 2026-09-24T00:06:19Z.
attacking: the newest partner account03/B06 r47 shear-flat heavy-hub / diagonal-plus-rank-one endpoint. First unpaid implication: after a heavy physical shear coordinate is exposed, can one peel that literal coordinate and spend the remaining aggregate two-area currency of its exact Schur complement, rather than take a worst curved-fiber supremum?

# Early checkpoint — scalar peel + aggregate E2 transfer

Programme: QFORM-DENSITY-3EIG-20260922. Full target remains OPEN.

Let Q be a quadratic polynomial in independent cap-one original coordinates. Fix a literal physical coordinate h with diagonal coefficient a=A_hh != 0. Completing the square in that original coordinate gives

    Q = a (X_h + ell(X_-h))^2 + S(X_-h),

where S is the exact Schur-complement quadratic polynomial, including all induced affine/constant terms. The completed square-peel lemma in the pinned e5f71... FOURIER_ROUTE_REPORT gives

    D(Q) := ||p_Q||_infinity <= |a|^(-1/2) H_{1/2}(S).

Now choose any two disjoint original-coordinate banks I,J among the remaining variables and put M=S[I,J],

    Z=e_2(M^T M)>0.

The preceding account02/B06 theorem QFORM-E2-HALFRIESZ-ROW-GATE-FREE-v1 applies to the entire exact S and yields

    H_{1/2}(S) <= 8 e^(1/4) Z^(-1/8).

Therefore

    boxed: D(Q) <= 8 e^(1/4) |a|^(-1/2) Z^(-1/8).        (E1)

No individual minor is selected, no post-rotation independence is used, and arbitrary same-bank curvature and the complete nonzero cross tail survive.

## Exact transfer inside partner r47 shear-flat normal form

The newest designated partner r47 has exact Schur residual

    S = D + E^T T E,

where D is diagonal, E is a 2xm physical shear frame, and T=T^T is 2x2. Let e_h be column h of E and define

    s_h = D_hh + e_h^T T e_h.

If s_h != 0, scalar completion at the literal environment coordinate h gives a second shear-flat residual

    S/h = D_J + E_J^T T_h E_J,
    T_h = T - (T e_h e_h^T T)/s_h,
    J=[m]\{h}.

Two exact determinant identities are

    det T_h = det(T) D_hh/s_h,                              (E2)

and, with W=det(EE^T) and alpha_h=e_h^T(EE^T)^(-1)e_h,

    W_h:=det(E_JE_J^T)=W(1-alpha_h).                        (E3)

Let mu_h be the squared physical pair-area law of E_J and Omega_h=P(P cap Q=empty) for iid P,Q~mu_h. The partner random-cut identity, now on J, gives some cut I|K of J with

    W_I W_K >= W_h^2 Omega_h/16.

For the exact cross block M_h=(S/h)[I,K]=E_I^T T_h E_K,

    e_2(M_h^T M_h)=(det T_h)^2 W_I W_K
                 >= (det T_h)^2 W_h^2 Omega_h/16.          (E4)

Applying (E1) to S at the physical coordinate h and the cut I|K gives

    D(S-polynomial)
      <= 8 sqrt(2) e^(1/4) Omega_h^(-1/8)
         |s_h|^(-1/4)
         [ |det T| |D_hh| W(1-alpha_h) ]^(-1/4),           (E5)

provided every displayed denominator is nonzero. This is a new weighted receiver for the r47 heavy-shear branch: one literal hub is peeled and the remaining singular kernel is averaged against the complement pair-area law instead of maximized fiberwise.

The exact surviving degeneracies are now explicit: s_h=0 (literal pivot cancellation), D_hh=0 (rank of T_h drops after the peel), det T=0 (partner's diagonal-plus-rank-one endpoint), W_h=0 (shear coloop), or Omega_h small (the complement pair-area law is itself physically concentrated). These are finite physical certificates, not hidden dimensional losses.
