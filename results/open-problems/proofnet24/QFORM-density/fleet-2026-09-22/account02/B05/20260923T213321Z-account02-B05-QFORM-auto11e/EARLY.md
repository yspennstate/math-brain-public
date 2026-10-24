SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B05, 2026-09-23T21:33:21Z.
attacking: QFORM-TWOBANK-HUB-PUNCTURED-COUPLING-v1 — replace the previous power loss as b->0 by a logarithmic bridge using the honest one-dimensional L-density cap before maximalisation.

# Early substantive checkpoint

Fresh owner programme: QFORM-DENSITY-3EIG-20260922, revision 2026-09-22.15. Full QFORM remains open. Execution status: WITHOUT_VERIFIED_BRAIN.

Let the two-bank curved-tube theorem supply, on every shell r<=|L|<=2r,

P(Q in I, shell) <= A |I| sqrt(r/|b|),    A := C_T K/4,    b!=0,

for Q=2HL+2bLP+V^2+affine/shear terms, with H independent of the two banks. In the original-coordinate product setting the normalized linear form L has a density cap M_L (in particular M_L<=sqrt(2)); if ||f_H||_infty<=m, then the same shell also obeys the independent-hub estimate

P(Q in I, shell) <= [m |I|/(2r)] P(shell) <= m M_L |I|.

Finally P(Q in I, shell)<=m|I|/(2r) by the hub slope alone. Hence

P(Q in I, shell) <= |I| min{ A sqrt(r/|b|), B, C/r },
B=m M_L, C=m/2.

Take dyadic shells r_k=r_- 2^k with r_-:=|b|(B/A)^2, so the first two terms meet at r_-. Let r_+:=C/B=1/(2M_L). If r_-<r_+, then summing the small-r geometric tail, the B-plateau, and the large-r geometric tail gives

||p_Q||_(infty,ess)
 <= B [ 4+sqrt(2) + log_2^+(r_+/r_-) ]
 = m M_L [4+sqrt(2)+log_2^+( C_T^2 K^2/(32 |b| m^2 M_L^3) )].

If r_- >= r_+, summing min{A sqrt(r/|b|),C/r} at its crossing gives <=(3+sqrt(2))B, so the same displayed bound remains valid. Thus the punctured deterioration is at most logarithmic, not |b|^{-1/3}. The exact b=0 endpoint remains separately paid by the Borel null-hub square theorem; uniformity through b=0 is still unpaid.

This uses the product-projection one-dimensional cap of L and never treats bP as a small random error.
