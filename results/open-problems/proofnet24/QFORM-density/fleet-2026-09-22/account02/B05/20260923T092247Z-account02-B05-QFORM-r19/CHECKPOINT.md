# B05 r19 early substantive checkpoint — pivot-free leave-one-out Fresnel collar

Full QFORM remains OPEN.

Let `A=R Lambda R^T` have exact rank three, `R^T R=I_3`, and all three nonzero eigenvalues satisfy `|lambda_k|>=1`. Fix an original coordinate `i`, write `r_i` for its spectral row, `c=||r_i||^2<1`, and

`H_i = I_3-r_i r_i^T = sum_{j!=i} r_j r_j^T`.

The completed newest-Claude Theorem F at `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837` can be applied with the heavy coordinate placed on the conditioned `J` side, not the Brascamp--Lieb `I` side. Therefore, if

`r_j^T H_i^{-1} r_j <= 1/2` for every `j!=i`,

then, uniformly in arbitrary affine terms,

`||p_Q||_infinity <= 12 [ |det Lambda| det(H_i) ]^(-1/3)
                       = 12 [ |det Lambda| (1-c) ]^(-1/3).`

This does **not** require `A_ii!=0`. In particular it applies at an exact physical null pivot `A_ii=0`, which is precisely where the scalar-Schur route is unavailable.

If a spectral basis is chosen with `r_i=sqrt(c)e_1` and each leaf row is `r_j=s_j e_1+w_j`, `w_j perpendicular e_1`, then

`r_j^T H_i^{-1}r_j = s_j^2/(1-c)+||w_j||^2`,

and these normalized leaf leverages sum to three. Hence failure of the gate can occur at at most five leaves. On the concrete collar `1-c>=1/128`, the paid branch obeys

`||p_Q||_infinity <=12*128^(1/3)<60.477`.

Thus the first unpaid exact-rank-three high-leverage/null-pivot implication has already narrowed to: an ultra-near-coloop `1-c<1/128`, or a finite set of at most five normalized-heavy leaves. The endpoint `c=1` is separately paid by the completed null-coloop scalar/dependent-pair theorem; what is not yet paid is a uniform bridge through `c->1` when the residual longitudinal coordinate overlaps the transverse pair on the same original product coordinates.
