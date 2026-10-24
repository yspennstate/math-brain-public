# account02/B01 r33 checkpoint — aggregate two-slope + one-Fresnel route

Programme: QFORM-DENSITY-3EIG-20260922. Full target remains open.

Substantive checkpoint: let I,J be disjoint original-coordinate banks and C=A[I,J] have rank two. Suppose on I,

A_II = lambda v v^T + D,

with lambda!=0, ||v||_2=1 and D diagonal. Let R be an orthonormal basis of range(C), delta=dist(v,range(C)), and require the row leverages of span(v,range(C)) to be <=1/2. Writing C=RB and eta=B X_J, the partner/product-projection estimate gives

||p_eta||_infinity <= e/sqrt(pdet(CC^T)).

Fresnel-linearize only lambda(v^T X_I)^2, average eta before absolute inversion, change y=2t eta, and apply the shifted three-dimensional Fourier–Brascamp–Lieb integral from the newest Claude report to the augmented rows (v_i,R_i). This yields

|phi_Q(t)| <= 8 pi^(5/2) K |lambda|^(-1/2) delta^(-1) |t|^(-5/2),

K=||p_eta||_infinity.

Hence Fourier inversion of min(1,A|t|^(-5/2)) gives the candidate bound

||p_Q||_infinity <= (5/3) 2^(6/5) e^(2/5)
  [ |lambda| delta^2 pdet(CC^T) ]^(-1/5)
<5.713 [ |lambda| delta^2 pdet(CC^T) ]^(-1/5).

All J-self curvature, outside blocks, and affine terms are intended to remain arbitrary. The key audit still to record in the final report is that the Fresnel/BL integral is translation-invariant in all conditioning-generated affine shifts and that the two-dimensional slope density is obtained before any fixed two-column minor is inverted.
