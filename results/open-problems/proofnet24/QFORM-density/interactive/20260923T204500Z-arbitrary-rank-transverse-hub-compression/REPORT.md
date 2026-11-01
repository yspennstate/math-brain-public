# Arbitrary-rank transverse-light compression from one hub

Let A be any real symmetric n-by-n matrix in a literal original-coordinate hub/light split,

A = [[a, w^T], [w, D]],

where w is nonzero. Write e=w/||w|| and let P=I-ee^T on the light space. Then the **sharp rank-two deletion bound** is

s_3(A) <= max{|a|, ||PDP||_op}.                              (1)

Consequently, if s_3(A)>=sigma and |a|<sigma, then

||PDP||_op >= sigma.                                         (2)

This has no exact-rank hypothesis, no sign assumption, and no bound on any other spectral mode or light dimension. It identifies a full-strength light quadratic mode transverse to the hub cross vector whenever the literal hub diagonal lies below the third-singular-value threshold.

Proof. Put D_perp=PDP and

A_0=A-a e_h e_h^T-[[0,0],[0,D_perp]].

In the orthogonal decomposition into hub h, light direction e, and light space e^perp, A_0 has block form

[[0, ||w||, 0],
 [||w||, d, u^T],
 [0, u, 0]]

for a real d and vector u. Its range lies in the span of the e column and the vector (||w||,d,u), so rank(A_0)<=2. The error A−A_0 is the orthogonal block sum of scalar a on the hub and PDP on e^perp; hence its operator norm is **exactly** max{|a|,||PDP||_op}. Eckart–Young gives (1), then (2).

More generally, for every integer r>=3, let C be the orthogonal block sum of scalar a and PDP. Since A=A_0+C and rank(A_0)<=2, the singular-value rank-perturbation inequality gives

s_r(A) <= s_(r−2)(C).                                         (3)

If |a|<sigma and s_r(A)>=sigma, then PDP has at least r−2 singular values at least sigma. Thus the same literal hub deletion preserves the entire large-singular-value count after discounting at most two hub-coupled modes. This remains a spectral statement only.

The strict gate |a|<sigma is necessary for deducing (2) from (1): if |a|>=sigma, the hub diagonal alone can account for a third singular direction. The conclusion is spectral only. It does not assert that PDP has a physical-coordinate square bank, nor that a product law remains product after projecting onto e^perp. The canonical mixed hub example 2HL+V^2+2epsilon LP has the transverse V mode and still exhibits the unresolved negative-target product-source leakage problem. An arbitrary original-coordinate affine term does not affect (1), but remains part of the analytic density step.
