# account03/B18 — LPP primary-source transfer into the grouped QFORM compiler

Run: `20260924T142238Z-account03-B18-QFORM-fixed-multiplicity-audit-r1`.
Status: **proved supporting sharpening / independent validation of the nine-eigenvalue replacement / no novelty claim**.

Primary source: Galyna Livshyts, Grigoris Paouris, Peter Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949, Theorem 1.1. For a product probability density whose one-dimensional factors are bounded by one, every k-dimensional orthogonal marginal has density at most `2^(k/2)`. No moment, iid, centering, support, smoothness, Gaussian or log-concavity hypothesis is present.

For a full-rank linear map `L:R^m->R^d`, SVD/change of variables therefore gives

`||p_{LD}||_infinity <= 2^(d/2)/sqrt(det(LL^T))`

for any independent cap-one product vector `D`; if `d=m`, the determinant-one full-dimensional orthogonal case is even simpler and the same displayed upper bound remains valid.

A second exact transfer gives the scalar Fourier-power estimate used below. For a one-dimensional probability density `0<=f<=1` and `p>=2`, let `m=floor(p/2)`. Since `|hat f|<=1`,

`int |hat f|^p <= int |hat f|^(2m) = 2pi p_S(0)`,

where `S=sum_{j=1}^m(X_j-X'_j)`. The normalized coefficient vector has Euclidean norm one and its density is at most `sqrt(2)` by the k=1 case; hence `||p_S||_infinity<=1/sqrt(m)`. Since `m>=p/4`,

`boxed: int |hat f|^p <= 4pi/sqrt(p).`

Now use the grouped compiler with disjoint original-coordinate banks `H,I,J`,

`Q=F(X_H)+2<W,M X'+beta>+R(X')`, `X'=(X_I,X_J)`.

Let `M_J` have row rank k and singular-value product S. Let residual physical crossing rows after projection off `row(M_J)` be `c_i`. For the ell-subset volume law

`w_T=det(C_TC_T^T)/Z_ell`, `alpha_i=P(i in T)<=1/2`, `d=k+ell`,

condition on the literal I-bank before squaring the light-bank L2 pushforward. Only a literal J-bank copy is introduced, so `D=X_J-X'_J` remains an independent cap-one product vector. Weighted Holder uses the maps

`D -> (M_JD,(<c_i,D>)_{i in T})`,

whose Gram determinant is exactly `S^2 det(C_TC_T^T)`. The LPP linear-image bound and the sharpened scalar Fourier powers give each T integral at most

`2^(d/2) [2pi/|t|]^ell prod_{i in T}sqrt(alpha_i) / [S sqrt(det(C_TC_T^T))]`.

Entropy subadditivity for a uniformly ordered random ell-subset gives

`H(w)+sum_i alpha_i log alpha_i <= ell log ell-log(ell!)`.

Combining with the hub Plancherel factor yields

`|phi_Q(t)| <= min(1,Ksharp |t|^(-d/2))`,

`Ksharp=M_H^(1/2) pi^(d/2) 2^((k+3ell)/4) (ell^ell/ell!)^(1/4) S^(-1/2) Z_ell^(-1/4)`.

For `d>2`, Fourier inversion gives

`||p_Q||_infinity <= [d/(d-2)] M_H^(1/d) 2^((k+3ell)/(2d)) (ell^ell/ell!)^(1/(2d)) S^(-1/d) Z_ell^(-1/(2d)).`

No random-variable rotation is used; full-dimensional deterministic hub rotations preserve joint density by Jacobian one and no independence of the rotated hub coordinates is asserted.

Consequences after the standard exact heavy-row promotion tree:

1. For a literal cross block B,

`boxed: ||p_Q||_infinity <= 6^(4/3) E_3(B)^(-1/6)`,

where `6^(4/3)=10.90272355699...`. The diffuse `(k,ell)=(0,3)` branch is the largest; `(1,2)`, `(2,1)` and the exact-rank-three terminal are smaller after the exact Gram--Schmidt aggregate identities.

2. For a literal cross block B,

`boxed: sup_a E|Q-a|^(-1/2) <= 8*2^(3/8) E_2(B)^(-1/8)`,

where the constant is `10.37471643721...`. This is a half-potential result, not a rank-two density theorem.

3. Under the fixed-multiplicity hypotheses with cap K and `s_9(A)>=s>0`, the baseline structural theorem gives in the no-pivot branch `E_3>=4^-3 kappa^3`, so the normalized density is `<1745`. In the scalar-pivot/no-pivot-Schur subbranch, `E_2>=4^-2 kappa^2` gives half-potential `<132`. Keeping the baseline pivot branch bound 601 closes the full replacement theorem

`boxed: ||p_Q||_infinity <= 6010 K^2/s under s_9(A)>=s>0.`

Thus this source transfer independently validates the current nine-eigenvalue replacement with strictly improved internal analytic constants. It does not prove threshold eight, the unrestricted three-eigenvalue conjecture, or global continuity.