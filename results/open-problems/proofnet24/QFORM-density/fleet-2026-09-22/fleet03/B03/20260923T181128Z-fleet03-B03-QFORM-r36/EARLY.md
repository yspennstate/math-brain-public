SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B03, 2026-09-23T18:11:28Z.
attacking: switch from the near-coloop pivot mechanism to the fresh arbitrary-internal-function crossing theorem; derive the exact rank-two crossing of the surviving square-plus-hyperbola packet, its dependence-safe Riesz time integral, and the precise effective-dimension obstruction to one-copy L-infinity.

# Early calculation

In the exact source-valid packet

Q = a^{-1}(H_0 + (beta v + m q).X_R)^2 + 2 sigma (u.X_L)(v.X_R),

write H_0=a r.X_O, where O is the physical complement of R. The vector r has coefficient 1 at the original pivot i, while u is a unit vector supported on L, so ||P_{u^perp}r||>=1. With v,q orthonormal on R,

Q = F(X_R) + 2 X_R^T B X_O + G(X_O),
B = v (beta r + sigma u)^T + q (m r)^T.

Thus B has exact rank two and, because v,q are orthonormal,

(s_1(B)s_2(B))^2
 = det([[beta r+sigma u],[m r]] [[beta r+sigma u],[m r]]^T)
 = m^2 sigma^2 (||r||^2-<r,u>^2)
 >= m^2 sigma^2.

The new projected-crossing source permits arbitrary internal F,G. The two orthogonal physical projections on each side have density cap <=2, so its exact-rank-two crossing theorem gives

|phi_Q(t)| <= min{1, K_2/|t|},
K_2 <= 2 pi (m|sigma|)^(-1/2).

Consequently

int_R |t|^{-1/2}|phi_Q(t)|^2 dt
 <= (16/3) sqrt(K_2)
 <= (16/3)sqrt(2pi)(m|sigma|)^(-1/4),

and

||p_Q||_2^2 <= 4 (m|sigma|)^(-1/2).

The calculation is independent of the heavy-row leverage and the angular cancellation coefficient. It preserves the whole independent-copy difference; no X-X' / X+X' independence is asserted.

Important structural check for the fresh grouped projected-crossing theorem: the light residual is G=a(r.X_O)^2. In any split for which the two-row hub crossing M_J has rank two, its second row is m r_J, hence r_J lies in row(M_J). Therefore the projected light crossing C=(A_G)_{I,J}(I-Pi_row(M_J)) vanishes identically. The natural two-dimensional right-hub grouping has effective dimension d=2, not d>=3. This explains why the fresh theorem supplies the stable L2/half-Riesz endpoint but does not by itself close one-copy L-infinity on this packet.

Full QFORM remains open; continuity is not claimed by this calculation.
