# B02 Fourier/projection endpoint note

Source manuscript blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`; source SHA-256 declared in the canonical manifest: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.

## 1. Exact repair for the product-projection line

In `lem:projection` (manuscript lines 258-282), after dropping all `b_i=0` factors, let `z=#{i:b_i=0}`. Since `sum_i b_i=n-d`,

`sum_{b_i>0}(1-b_i)=(n-z)-(n-d)=d-z<=d`.

Therefore

`log p(y) <= (1/2) sum_{b_i>0}(1-b_i) <= d/2`,

which proves the advertised `||p_{U^T X}||_infinity <= exp(d/2)`. The manuscript's final equality should be replaced by this inequality. This is presentation-only and does not alter any later constant.

## 2. Exact low-dimensional stress tests

All examples obey density cap one.

- `X~Unif[-1/2,1/2]`: the difference density is `(1-|x|)_+`, so the convolution cap `<=1` is attained.
- For two independent such uniforms, `(X1+X2)/sqrt(2)` has density peak `sqrt(2)`. Thus a universal scalar projection constant must be at least `sqrt(2)`; the manuscript uses `sqrt(e)`.
- `f(x)=exp(-pi x^2)` has `fhat(t)=exp(-t^2/(4*pi))`, hence `int |fhat|^p dt=2*pi/sqrt(p)` exactly. The power `p^{-1/2}` in `lem:scalar-fourier` is therefore sharp under only `f<=1`.
- For the uniform density, `int|fhat|^2=2*pi` and `int|fhat|^4=4*pi/3`; the first value saturates the Plancherel/cap bound.
- For `Y~Unif[-1/2,1/2]`, `Y^2` has density `z^{-1/2}` on `(0,1/4)`, so the scalar-square envelope coefficient one is sharp.
- For uniform `(X,Y)` on the square and `q=X^2+Y^2`, the density near zero is exactly `pi`; the definite-pair constant `pi` is sharp.
- For the same square and `q=X^2-Y^2`, put `u=X-Y`, `v=X+Y`; the image domain is `|u|+|v|<=1`, the Jacobian is `1/2`, and for `0<|z|<1/4`

  `p_q(z)=log((1+sqrt(1-4|z|))/(1-sqrt(1-4|z|)))`.

  Hence `p_q(z)=-log|z|+o(1)` as `z->0`. The logarithmic coefficient one in the hyperbolic envelope is sharp.
- For independent cap-one Gaussians and `Z=2mXY`, direct Gaussian integration gives `phi_Z(t)=(1+m^2 t^2/pi^2)^(-1/2)`, confirming the manuscript's cross-term/Fourier normalization.

## 3. Why constant tuning cannot lower 17 to 13 in the current architecture

The determinant theorem gives, from an order-`k` crossing volume,

`|phi(t)| <= min(1,(C/|t|)^(k/4))`.

At `k=4` this is exactly a `C/|t|` tail and its unweighted time integral diverges logarithmically. The exact Gaussian scalar-Fourier identity above shows that the `p^{-1/2}` scalar exponent that feeds the determinant proof cannot be improved in general; changing only projection/convolution/Fourier **constants** therefore cannot change this endpoint exponent.

Thus the existing `4k-3` structural count plus the existing determinant theorem cannot yield a 13-eigenvalue density theorem by constant sharpening alone. A rigorous threshold reduction below 17 needs a genuinely new ingredient: an order-four endpoint receiver, an improved decoupling/determinant exponent, or a structural rank count that reaches order five with fewer than 17 large singular directions. No lower-threshold theorem is claimed here.
