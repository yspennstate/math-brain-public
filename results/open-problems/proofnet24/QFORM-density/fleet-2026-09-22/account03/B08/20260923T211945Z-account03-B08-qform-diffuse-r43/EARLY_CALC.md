# Early calculation — rank-one Schur-crossing small-ball

Run `20260923T211945Z-account03-B08-qform-diffuse-r43`.

For independent product blocks `X,Y`, arbitrary measurable internal phases `F(X),G(Y)`, and an exact rank-one physical cross matrix `C` with sole singular value `sigma>0`, the reviewed exact-rank crossing theorem gives

`|phi_R(t)| <= min(1, sqrt(pi) (M_X M_Y)^(1/2) sigma^(-1/2) |t|^(-1/2))`,

for `R=F(X)+2 X^T C Y+G(Y)`.  The scalar projection theorem gives `M_X,M_Y<=sqrt(2)`, so

`|phi_R(t)| <= min(1, sqrt(2 pi) sigma^(-1/2)|t|^(-1/2))`.

Use the positive Gaussian majorant

`1_{|x-s|<rho} <= exp(1/2) exp(-(x-s)^2/(2 rho^2))`.

Gaussian Fourier inversion and the displayed characteristic-function envelope yield

`P(|R-s|<rho)`
` <= exp(1/2) rho/sqrt(2pi) * sqrt(2pi) sigma^(-1/2)`
`    * integral_R exp(-rho^2 t^2/2)|t|^(-1/2) dt`
` = exp(1/2) 2^(1/4) Gamma(1/4) sigma^(-1/2) sqrt(rho)`.

Thus the exact rank-one crossing has a dimension-free square-root small-ball constant

`H_1 = exp(1/2) 2^(1/4) Gamma(1/4) = 7.108628442830306...`.

Combining this with the completed physical-indefinite-pair logarithmic smoother (`||p_Q||_inf <=4 sqrt(2H)(D kappa)^(-1/4)`) gives

`||p_Q||_inf <= C_1 (D kappa sigma)^(-1/4)`,

`C_1=4 sqrt(2 H_1)=15.082311168072676...`.

This attacks the exact rank-one Schur-mismatch surface left open by B08 r45.  It keeps arbitrary same-bank functions and does not use moments, post-rotation independence, or pointwise quadratic-phase decay.
