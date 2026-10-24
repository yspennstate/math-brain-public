SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B08, 2026-09-23T14:40:19Z.
attacking: diffuse selected-three frame — bridge failure of the one-scale spectral-window payment to either an affine-recursive three-direction principal child or a localized pivot/star plus two almost-L child directions, without discarding any spectral remainder.

# Substantive checkpoint — spectral-window deletion conservation

Full QFORM remains OPEN. This checkpoint records a proved structural step, not a full-solution claim.

Let A=A^T. Let U in R^{n x r} have orthonormal columns and satisfy

    A U = U Lambda,     min_j |Lambda_jj| >= a>0.

For a physical set H, |H|=h<r, put T=H^c, C=A[T,T], and

    delta_H = ||U_H^T U_H||op.

Then

    s_{r-h}(C) >= a sqrt(1-delta_H).                       (1)

Proof. Restrict the eigen-equation to T:

    C U_T = U_T Lambda - A[T,H] U_H.                       (2)

The second term has rank at most h. Also

    U_T^T U_T = I-U_H^T U_H,

so

    s_r(U_T Lambda) >= a sqrt(1-delta_H).                  (3)

The rank-h singular-value interlacing inequality gives

    s_{r-h}(C U_T) >= s_r(U_T Lambda).                     (4)

Finally ||U_T||op<=1 and s_k(CU_T)<=s_k(C)||U_T||op, proving (1).

Now specialize to the B08 selected-three diffuse regime. Let R be three genuine eigenvectors with |lambda|>=L and max_i ||R_i||^2<=1/48. Let

    P = 1_{|A|>=L/64}

be the spectral projection onto the ENTIRE one-scale high window. If max_i P_ii<=1/32, the completed one-scale ridge theorem pays the full ambient form with a continuous C_0 density and

    ||p_Q||inf <= [288 sqrt(3e)/13]/L < 64/L.               (5)

Suppose this window gate fails. Then rank(P)>=4: if rank(P)=3, its range must equal the selected-three range, whose diagonal leverage is <=1/48<1/32.

Choose any physical i with P_ii>1/32. If P_ii<=1/2, apply (1) to the full high-window frame with h=1 and a=L/64. Since rank(P)>=4,

    s_3(A[-i,-i]) >= L/(64 sqrt(2)).                       (6)

If P_ii>1/2, spectral energy gives

    A_ii^2 + ||A[i,-i]||_2^2 = ||A e_i||_2^2
      >= (L/64)^2 P_ii > L^2/(2*64^2),

hence

    max{|A_ii|, ||A[i,-i]||_2} > L/128.                    (7)

At the SAME i, applying (1) to the selected three eigenvectors yields

    s_2(A[-i,-i]) >= sqrt(47/48) L.                        (8)

Thus failure of the ridge-window payment cannot remain an unstructured diffuse state: it yields either a principal child with three actual singular directions at scale L/(64sqrt2), or a localized scalar/star resource at scale L/128 together with two almost-L child directions.
