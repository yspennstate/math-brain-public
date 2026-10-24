# Addendum — exact projection-leverage factor and the square curved-bank endpoint

This sharpens Theorem 2.1 of `REPORT.md` without changing any hypotheses or correction scopes.

Let

`L=(BB^T)^(1/2)`, `R=B^T L^(-1)`, `R^T R=I_r`,

and write `ell_j=||R[j,:]||_2^2` for the row leverages of the `r`-dimensional row space of `B`. Define

`Phi(B)=prod_{j: ell_j<1} (1-ell_j)^(-(1-ell_j)/2)`,

with rows of leverage one contributing the factor one. The completed weighted affine-fiber Brascamp--Lieb theorem gives the **sharper** projection cap

`||p_{R^T V}||inf <= Phi(B) <= exp(r/2)`.

Repeating the reciprocal-distance calculation in the main report with this exact cap, rather than replacing it immediately by `exp(r/2)`, gives

`boxed:
 ||p_Q||inf
 <= K_r Phi(B)^(1/r) det(BB^T)^(-1/(2r)),
 K_r=[r/(sqrt(2)(r-1))] omega_r^(1/r).
`

Thus the universal theorem in the report is the corollary `Phi(B)^(1/r)<=sqrt(e)`.

## Square opposite bank: no sqrt(e) loss

If `m=r` and `B` is invertible, then `R` is a square orthogonal matrix. Every row leverage equals one, so

`Phi(B)=1`.

Therefore, with an exact-null original-coordinate `U` bank and **arbitrary quadratic curvature on the opposite `V` bank of the same size**, one has the stronger bound

`boxed:
 ||p_Q||inf <= K_r |det B|^(-1/r).
`

For `r=2`,

`boxed:
 ||p_Q||inf <= sqrt(2 pi) |det B|^(-1/2).
`

This exactly matches the designated partner's sharp constant for a square null **leaf** bank, but here the leaf-side `2 x 2` curvature is completely arbitrary; nullity is on the hub side instead.

For a rectangular two-hub bank, the sharp form is

`||p_Q||inf
 <= sqrt(2pi) Phi(B)^(1/2) e_2(B^T B)^(-1/4)`,

because `det(BB^T)=e_2(B^T B)`. Consequently an actual slab ratio `rho` forces

`e_2(B^T B)
 <=4 pi^2 Phi(B)^2 rho^(-4)
 <=4 pi^2 e^2 rho^(-4)`.

This leverage-sensitive version is sometimes materially stronger than the universal `sqrt(e)` relaxation. It also cleanly separates the source of the only loss in the rectangular dual theorem: it is exactly the product-projection density factor, not the arbitrary same-bank leaf curvature.
