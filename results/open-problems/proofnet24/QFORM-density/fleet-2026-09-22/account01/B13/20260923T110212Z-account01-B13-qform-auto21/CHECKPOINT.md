# Early substantive checkpoint — dual rectangular null-bank aggregation

Run `20260923T110212Z-account01-B13-qform-auto21`. Full QFORM remains OPEN.

## New mechanism under proof

Let `r>=2`. Let `U in R^r`, `V in R^m` be disjoint original-coordinate banks with independent scalar densities bounded by one, and let `Z` be the remaining independent coordinates. Assume the `U`-bank is exactly null in the quadratic form, so after conditioning on `Z`

`Q = G(V,Z) + (2 B V + c(Z))^T U`,

where `B` is an `r x m` full-row-rank matrix and `G` is completely arbitrary. Unlike the partner account02/B13 theorem, **no nullity or other restriction is imposed on the `V`-bank curvature**.

Conditioning on `(V,Z)` and using the sharp weighted Rogozin/Ball scalar linear-form cap gives

`||p_{Q|V,Z}||inf <= sqrt(2) / ||2 B V + c(Z)||_2`.

Factor `B = L R^T`, with `L=(B B^T)^(1/2)` and `R=B^T L^(-1)`, so `R^T R=I_r`. The completed product-projection theorem `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1` gives

`||p_{R^T V}||inf <= exp(r/2)`.

Hence, for fixed `Z=z`, `Y=2 B V+c(z)` has an `R^r` density cap

`M <= exp(r/2) / [2^r sqrt(det(BB^T))]`.

The reciprocal-distance lemma used by the newest designated partner account02/B13 says that an `R^r` probability density bounded by `M` satisfies

`sup_a E ||Y-a||^(-1) <= [r/(r-1)] omega_r^(1/r) M^(1/r)`.

Therefore

`||p_Q||inf <= K_r^dual det(BB^T)^(-1/(2r))`,

where

`K_r^dual = [r/(r-1)] sqrt(e/2) omega_r^(1/r)`.

For `r=2`, `K_2^dual=sqrt(2 pi e)` and Cauchy--Binet gives

`||p_Q||inf <= sqrt(2 pi e) e_2(B^T B)^(-1/4)`.

The next step is to finish the continuity justification, the exact original-matrix corollary `A[P,P]=0`, and the two-sided null-bank dichotomy obtained by combining this with the designated partner's theorem for `A[T,T]=0`.

No random-coordinate rotation is used: `R^T V` is only an analyzed projection whose density is bounded by the product-fiber Brascamp--Lieb theorem. Same-bank `V` curvature remains inside `G(V,Z)` and is never discarded perturbatively.
