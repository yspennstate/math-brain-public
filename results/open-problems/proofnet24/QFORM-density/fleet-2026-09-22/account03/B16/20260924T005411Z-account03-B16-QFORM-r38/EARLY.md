SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B16, 2026-09-24T00:54:11Z.
attacking: the true near-coloop majority-sign/small-pivot interface by retaining the untouched physical hub conditionally and paying the indefinite planar discriminant with the completed rank-two half-Riesz estimate.

# Early calculation — conditional-shift discriminant

Let `X in R^m` have independent cap-one coordinates, let `H` be independent of `X` with density cap `L_H`, and let `T` be an `m x 2` full-rank matrix. Put `Z=T^T X`, `G=T^T T`, and

`Y=gamma H+g(X)`, `gamma!=0`,

so that, conditional on the full source `X`, the scalar `Y` has density at most `L_H/|gamma|`. Consider

`Q=aY^2+2Y u^T Z+rY+Z^T C Z+s^T Z+ell^T X+d`,

with `a!=0`, `C=C^T`, and

`B=[[a,u^T],[u,C]]`, `det B!=0`.

At a target `t`, the scalar-root half-discriminant is

`D_t=(u^T Z+r/2)^2-a(Z^T C Z+s^T Z+ell^T X+d-t)`.

Conditioning on `X`, the pushforward in `Y` gives

`p_(Q|X)(t) <= (L_H/|gamma|)[D_t]_+^(-1/2)`.

Its planar quadratic matrix is

`K=uu^T-aC`,

and the exact two-dimensional Schur identity is

`det K=a det B`.

Whiten the physical projection by `U=T G^(-1/2)`, so `U^T U=I_2` and `Z=G^(1/2)U^T X`. Then the quadratic matrix in `U^T X` is `K'=G^(1/2)KG^(1/2)` and

`|det K'|=det(G)|a det B|`.

Applying `QFORM-RANK2-AFFINE-HALF-RIESZ-v1` to `D_t` yields the sign-free bound

`||p_Q||_infinity <=128 (L_H/|gamma|)[det(G)|a det B|]^(-1/4)`.

If `ell` lies in `col(T)`, all linear terms in `D_t` lie in the two-dimensional projection, so the sharper completed constant `16 sqrt(30)` applies.

In the exact-rank-three near-coloop coordinates `r_0=sqrt(c)e`, `r_j=s_j e+w_j`, `sum w_j w_j^T=I_2`, take

`Y=sqrt(c)X_0+sum s_j X_j`, `Z=sum w_j X_j`, `B=Lambda`, `G=I_2`.

Thus, for every `a=e^T Lambda e !=0`, with no sign restriction,

`||p_Q||_infinity <=16 sqrt(30)c^(-1/2)|a det Lambda|^(-1/4)`.

Consequently on the live collar `c>63/64`, the branch `|a det Lambda|>=2^-12` is uniformly paid by

`||p_Q||_infinity <706.628`.

The first remaining implication is therefore the genuinely singular pivot chamber `|a det Lambda|<2^-12`, to be combined with the completed account04/B16 bank-overlap gate rather than with an indefinite cap-only level-set integral. Full QFORM remains OPEN; continuity is not proved by this early calculation.
