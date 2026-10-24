# Addendum: the leverage-one endpoint in Theorem 3.1

The `M^{-1/2}` notation in Section 3 of `REPORT.md` is literal only for `0<c<1`. The theorem itself also holds at the endpoint `c=1`; here is the direct restriction argument, so no singular whitening is used.

Let the selected row `v` of the rank-three orthonormal frame `R` satisfy `|v|=1`. Then

`sum_{j!=i} r_j r_j^T = I-vv^T=P_{v^perp}`.

Choose a `3 x 2` matrix `H` with orthonormal columns spanning `v^perp` and put

`S=R_L H`.

Then `S^T S=I_2`, and because `R_L^T X_L` lies in `v^perp`, writing `z=S^T X_L` gives

`R^T X = v X_i + H z`.

With `a=v^T Lambda v !=0`, completion of the square in the original independent coordinate `X_i` yields

`Q0 = a (X_i+m(z))^2 + z^T Gamma z`,

where

`Gamma=H^T( Lambda - Lambda v v^T Lambda/a )H`.

In the orthonormal basis `[v,H]`, ordinary block determinant factorization gives

`det Lambda = a det Gamma`,

so `|det Gamma|=|det Lambda|/|a|`, which is exactly the general pseudodeterminant formula `|pdet T|=c|det Lambda|/|a|` with `c=1`.

If every row of the residual two-frame `S` has leverage at most `1/2`, Theorem 2.1 of `REPORT.md` gives

`||p_R0||_3 <= (3e)^(2/3)(|det Lambda|/|a|)^(-1/3)`.

Conditional on the residual value, `X_i+m(z)` is still a mixture of translations of the original density of `X_i`, hence has conditional density at most one. Applying the account01/B11 dependence-safe square smoothing theorem gives

`||p_Q0||_infinity <= 4 sqrt(3e)(|a||det Lambda|)^(-1/4)`,

which is Theorem 3.1 with `c=1`.

Thus the report's theorem is valid for all `0<c<=1`; use the whitening proof for `0<c<1` and this direct `v^perp` restriction at `c=1`.
