# account01/B06 improvement — fractional graph determinant under row-leverage control

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Run: `20260924T123830Z-account01-B06-fixedmult-audit-r11`  
Pinned manuscript: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

Status: **proved analytic improvement, but NOT an unconditional multiplicity reduction.** It identifies a precise route by which the order-four Fourier endpoint becomes integrable when the crossing row geometry is quantitatively diffuse.

## Theorem: fractional graph determinant

Let

`Z=F(X_I)+2 X_I^T M X_J+G(X_J)`

with disjoint subvectors of independent real coordinates, all coordinate densities bounded by one, and arbitrary measurable real `F,G`. Let `m_i^T` denote row `i` of `M`. Define the limiting row leverage

`ell_i = m_i^T (M^T M)^+ m_i`,

with `ell_i=0` for a zero row. Fix `q in [1,2]`. If

`max_i ell_i <= q/2`,

then for every real `t`,

`|phi_Z(t)| <= det(I + [q t^2/(2 pi^2 e^2)] M^T M)^(-1/(4q)).`

At `q=2` this is exactly the determinant exponent and regularizer in the manuscript:

`alpha=(2 pi e)^2`, exponent `-1/8`, coefficient `t^2/(pi^2 e^2)`.

### Proof

The manuscript's two-power decoupling gives

`|phi_Z(t)|^2 <= E_D prod_i |fhat_i(2t (MD)_i)|`,

where `D=X_J-X'_J` has independent coordinate densities `g_j<=1`. Put `a=2t` and, for a parameter `alpha>0`,

`H=alpha I+a^2 M^T M`,

`c_j=alpha e_j^T H^{-1}e_j`, `d_i=a^2 m_i^T H^{-1}m_i`.

As in the manuscript, the corresponding graph vectors form a Parseval frame and

`theta=sum_i d_i=sum_j(1-c_j)`.

Because `q>=1`, Jensen gives

`|phi_Z(t)|^(2q) <= int prod_j g_j(x_j) prod_i |fhat_i(a m_i.x)|^q dx.`

For every row, `m_i` lies in `range(M^T)`. Spectral calculus on `M^T M` gives

`a^2 m_i^T (alpha I+a^2 M^T M)^(-1)m_i <= m_i^T(M^T M)^+m_i=ell_i`.

Hence `d_i<=q/2`, so `q/d_i>=2` whenever `d_i>0`. Apply the same change of variables `x=H^{-1/2}z` and the geometric rank-one Brascamp--Lieb theorem. The `g_j` factors contribute at most

`alpha^(c_j/2)c_j^(-c_j/2)`,

while for `h_i(u)=|fhat_i(u)|^q`, the scalar Fourier-power lemma at exponent `q/d_i` yields

`||h_i||_(1/d_i)
 = (int |fhat_i|^(q/d_i))^(d_i)
 <= [2 pi sqrt(2e d_i/q)]^(d_i)`.

The BL scaling contributes `d_i^(-d_i/2)`, so the `d_i` powers cancel. The coordinate entropy bound gives

`prod_j c_j^(-c_j/2) <= e^(theta/2)`.

Therefore the entire non-determinant factor equals at most

`[2 pi e sqrt(2/q) / sqrt(alpha)]^theta`.

Choose

`alpha = 8 pi^2 e^2/q`.

The bracket becomes one, and

`|phi_Z(t)|^(2q) <= det(I + a^2 M^T M/alpha)^(-1/2)`.

Since `a=2t`,

`a^2/alpha = q t^2/(2 pi^2 e^2)`,

which proves the theorem after taking the `2q`-th root.

## Crossing-volume corollary

If `Z_k(M)>0`, retain its order-`k` term in the determinant. Put

`p = k/(2q)`,

`u = pi e sqrt(2/q) Z_k(M)^(-1/(2k))`.

Then

`|phi_Z(t)| <= min(1,(u/|t|)^p)`.

If `k>2q`, the power is integrable and the manuscript's power-envelope lemma gives

`||p_Z||_infty <= e sqrt(2/q) [k/(k-2q)] Z_k(M)^(-1/(2k)).`

This strictly improves the fourth-power receiver whenever `q<2`.

## Concrete order-four branch

Take `k=4` and suppose a crossing cut has maximum row leverage at most `3/4`. Set `q=3/2`. Then

`||p_Z||_infty <= (8e/sqrt(3)) Z_4(M)^(-1/8).`

In the manuscript's no-pivot algebra, `s_13(A)>=1` implies `V_4(A)>=kappa^4`. If a random-cut witness attaining

`Z_4(M)>=4^(-4)kappa^4`

also has maximum row leverage at most `3/4`, then, because `kappa^(-1/2)=80`,

`Z_4(M)^(-1/8) <= 160`

and hence

`||p_Q||_infty <= 1280 e/sqrt(3) < 2010.`

For the stronger leverage gate `max ell_i<=1/2`, take `q=1`; the order-four density bound is

`||p_Z||_infty <= 2 sqrt(2)e Z_4(M)^(-1/8)`.

## Why this does not yet lower 17

The current manuscript proves the existence of a cut with large `Z_4` under `s_13`, but it does not prove a simultaneous row-leverage gap `max ell_i<=1-delta`. Row leverage can approach one for crossing directions concentrated through literal physical hub rows. The theorem above therefore supplies an exact **diffuse-cut receiver**, not a same-scope `s_13` theorem.

The remaining lower-threshold obligation is now precise: for a large-order-four cut, either prove a dimension-free leverage gap after an admissible product-preserving repartition, or route the heavy-leverage rows to a separate physical-hub/curved-fiber receiver without paying a reciprocal vanishing minor. Until that heavy-leverage branch is closed, the unconditional fixed-multiplicity threshold remains 17.

No Gaussianity, log-concavity, moments, bounded support, signature restriction, spectral truncation, affine restriction, or rotated-coordinate independence is used in this improvement.