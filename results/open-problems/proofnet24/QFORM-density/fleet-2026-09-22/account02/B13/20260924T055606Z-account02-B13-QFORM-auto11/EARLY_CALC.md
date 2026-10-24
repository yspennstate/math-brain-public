SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B13, 2026-09-24T05:56:06Z.
attacking: the partner r44 near-rank-one survivor; first self-improve the second carrier mode from O(rho^-1) to O(rho^-13/6), then test whether that faster tail can be retained product-safely rather than deleted.

# Early calculation: r44 forces a rho^(-13/6) second carrier mode

Work in the completed diffuse exact-rank-two chamber

A = D + U Lambda U^T,   U^T U = I_2,   max_i ||u_i||^2 <= 1/3,   s_3(A) >= 1,

and write the two eigenvalues of the symmetric 2x2 Lambda as lambda_1, lambda_2 with |lambda_1| >= |lambda_2|.
Let rho be a slab ratio.

The completed account03/B13 r44 theorem gives a physical k with |d_k|>=1 and

||p_Q||_infty <= C_sq (1 + |det Lambda|^(-6/13))

for one universal finite C_sq, uniformly in affine terms and arbitrary cap-one product laws.
Therefore, if rho > 2 C_sq,

rho <= C_sq(1+|det Lambda|^(-6/13))
     <= rho/2 + C_sq |det Lambda|^(-6/13),

so

|det Lambda| <= (2 C_sq / rho)^(13/6).                    (E1)

This is strictly stronger, for an unbounded-ratio sequence, than the preceding O(rho^-2) determinant obstruction.

Now use the completed account04/B13 fifth-diagonal sparsification from r44. If S contains the four largest |d_i|, then

||D_{S^c}||_op <= C_D/rho,   C_D = 2 sqrt(30 pi) = 19.416259125557...

Suppose |lambda_1| < 1/8 and rho >= 8 C_D. Then

||A-D_S||_op <= |lambda_1| + C_D/rho < 1/4.

Weyl and s_3(A)>=1 imply s_3(D_S)>3/4, hence three physical coordinates T subset S have |d_i|>3/4. On that same physical triple,

sigma_min(A[T,T]) >= 3/4 - ||(U Lambda U^T)[T,T]||_op > 5/8.

The pinned physical 3x3 theorem (Theorem A in COUNTEREXAMPLE_SEARCH.md) then gives

||p_Q||_infty <= 6 sqrt(pi)/(5/8) = 48 sqrt(pi)/5 < 17.02.

Consequently every sufficiently high-ratio survivor has |lambda_1|>=1/8. Combining with (E1),

|lambda_2| <= 8 (2 C_sq)^(13/6) rho^(-13/6).              (E2)

Thus the genuine remaining exact-rank-two obstruction is not merely rank-one plus an O(rho^-1) second mode: the second carrier eigenvalue is forced to be O(rho^-13/6). The diagonal tail is still only O(rho^-1), and neither tail may be deleted on fragmented/unbounded inputs.

First unpaid implication after this calculation:
QFORM-RANK1-4DIAG-DIAGTAIL-SUPERSMALL-MODE-RECEIVER-v1 — retain the O(rho^-13/6) second rank-one mode and the O(rho^-1) distributed diagonal tail in a product-preserving receiver, or give a genuine finite-union product-indicator counterexample in this exact normal form.
