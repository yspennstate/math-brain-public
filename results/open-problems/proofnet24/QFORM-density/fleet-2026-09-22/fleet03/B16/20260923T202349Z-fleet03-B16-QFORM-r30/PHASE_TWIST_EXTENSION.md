# Phase-twist extension of `QFORM-HUB-AWARE-PUNCTURED-TWOBANK-FOURIER-v1`

The theorem in `REPORT.md` remains valid, with exactly the same bound, after adding **arbitrary measurable real pure-source phases**

`R_H(H)+R_A(A)+R_B(B)`

to the polynomial. Thus one may replace (2.1) by

`Q = 2 alpha H L + beta L^2 + 2 delta L V + lambda V^2 + 2 epsilon L P`

`    + R_H(H)+R_A(A)+R_B(B)`,

with `alpha*epsilon*lambda !=0`, without changing

`||p_Q||_infinity <= 3 [L_H K_2 K_3/|alpha epsilon lambda|]^(1/3)`.

The density is still continuous and in `C_0`.

## Proof

Fix the characteristic-function time `t`. Replace the three source densities by the complex amplitudes

`f_{H,t}(h)=f_H(h) exp(i t R_H(h))`,

`g_{A,t}(a)=g_A(a) exp(i t R_A(a))`,

`g_{B,t}(b)=g_B(b) exp(i t R_B(b))`.

Their absolute values are exactly the original probability densities. Therefore every norm used in `REPORT.md` is unchanged or improves:

`||f_{H,t}||_2^2=||f_H||_2^2<=L_H`,

`||g_{i,t}||_2^2=||g_i||_2^2<=M_{3,i}`.

For the partial `P`-Fourier slice

`h_{i,t,zeta}(l,v)=integral exp(i zeta p) g_{i,t}(l,v,p) dp`,

we still have pointwise

`|h_{i,t,zeta}(l,v)| <= integral g_i(l,v,p) dp =m_i(l,v)`.

Hence the fixed-slice two-dimensional Plancherel estimate remains

`integral |Phi_{i,t}(xi,nu,zeta)|^2 dxi dnu <=(2 pi)^2 M_{2,i}`,

and three-dimensional Plancherel remains

`integral |Phi_{i,t}|^2 <=(2 pi)^3 M_{3,i}`.

The bank convolution is now a convolution of complex amplitudes rather than probability densities, but its Fourier transform still factors exactly as `Phi_{A,t} Phi_{B,t}`. The Fresnel calculation depends only on the cross polynomial in `(H,L,V,P)`, not on the pure-source phases. Thus equations (3.8)--(4.8) in `REPORT.md` go through verbatim with `hat f_H` replaced by `hat f_{H,t}` and the bank characteristic functions replaced by these twisted Fourier transforms. Their `L^2` bounds are identical, so

`|phi_Q(t)| <= pi^(3/2) sqrt(L_H K_2 K_3)`

`               * |alpha epsilon lambda|^(-1/2)|t|^(-3/2)`.

Time integration therefore gives the same density bound and `L^1` characteristic function, hence the same continuous `C_0` conclusion.

This extension is useful under original-coordinate conditioning: arbitrary self-quadratic and affine terms confined to the hub or to either disjoint source bank may be absorbed exactly, without any perturbative deletion and without changing the estimate. It does **not** absorb additional cross-bank monomials outside the displayed `HL`, `L^2`, `LV`, `V^2`, `LP` structure.
