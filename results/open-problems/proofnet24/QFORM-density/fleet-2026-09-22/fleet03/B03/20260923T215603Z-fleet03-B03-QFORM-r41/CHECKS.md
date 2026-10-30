# fleet03/B03 r41 deterministic checks

Run: `20260923T215603Z-fleet03-B03-QFORM-r41`

## 1. Conjugate-pair algebra

For symmetric 2x2 matrices `P_-`,`P_+`, with `U=X-X'`, `V=X+X'`, define `H=P_-+P_+`, `K=P_+-P_-`. Direct expansion gives

`U^T P_- U + V^T P_+ V = X^T H X + X'^T H X' + 2 X^T K X'`.

The affine terms split as

`ell_-^T U+ell_+^T V=(ell_-+ell_+)^T X+(-ell_-+ell_+)^T X'`.

So every non-cross term is bank-local; no term is discarded.

## 2. Fourier normalization

With `hat b(xi)=int exp(i xi.y)b(y)dy`, Plancherel is

`int |hat b|^2 = (2pi)^2 int |b|^2` in dimension two.

The change `xi=t C^T x` has Jacobian `|t|^2|det C|`, hence

`[int |hat b(t C^T x)|^2 dx]^(1/2)
 = 2pi |t|^(-1)|det C|^(-1/2)||b||_2`.

Because a product probability density with each scalar factor <=1 has squared L2 norm <=1, the theorem's envelope coefficient is exactly

`A=2pi|det C|^(-1/2)`.

## 3. Weighted integral arithmetic

For `A>0`, crossover at `t=A`:

`2[int_0^A t^(-1/2)dt + A int_A^infty t^(-3/2)dt]
 = 8 sqrt(A)`.

For the squared envelope:

`2[int_0^A t^(-1/2)dt + A^2 int_A^infty t^(-5/2)dt]
 = (16/3)sqrt(A)`.

Also

`2[int_0^A 1 dt + A^2 int_A^infty t^(-2)dt]=4A`.

Using `int exp(itx)|t|^(-1/2)dt=sqrt(2pi)|x|^(-1/2)` gives the report constants.

For `C=2K`, `|det C|=4|det K|`, so

- Fourier envelope coefficient: `pi|det K|^(-1/2)`;
- one-copy half-Riesz coefficient: `8*4^(-1/4)=4sqrt(2)`;
- weighted squared-time coefficient: `(16/3)sqrt(2pi)*4^(-1/4)=(16/3)sqrt(pi)`;
- whole-copy half-Riesz coefficient: `(16/3)*4^(-1/4)=8sqrt(2)/3`.

Numerically:

`4sqrt(2)=5.656854249492381`,

`(16/3)sqrt(pi)=9.453087204829417`,

`8sqrt(2)/3=3.7712361663282534`.

## 4. Approximate-opposition stability

If `P_+=-P_-+E`, then `K=-2P_-+E`. Weyl/singular-value perturbation gives

`sigma_min(K)>=2 sigma_min(P_-)-||E||_op`.

Thus if `sigma_min(P_-)=kappa` and `||E||_op<=theta kappa`, `theta<2`, then

`sigma_min(K)>=(2-theta)kappa`

and for 2x2 `K`,

`|det K|>=sigma_min(K)^2 >=[(2-theta)kappa]^2`.

No probabilistic small-error step is used.

## 5. Partner application check

Fleet04/B03 at `05ff82a8d052b024ae584e60dffb7b198fcd7db4` proves

`E|R_--s|^(-1/4)|R_+-t|^(-1/4)<=sqrt(B_-B_+)`

on the true dependent `(U,V)` law. On the event `|R_--s|<=r`, `|R_+-t|<=r`, the integrand is at least `r^(-1/2)`, hence

`P(event)<=sqrt(B_-B_+) r^(1/2)`.

At `r=eps^2` this is linear in `eps`.

## 6. Correction audit

- No independence of `U` and `V` asserted.
- No conditional density cap for `U|V` or `V|U` used.
- No rotation of the original product law used.
- No law-uniform pointwise quadratic-phase decay used.
- No arbitrary-joint coarea bound used.
- No support, moment, log-concavity, compactness or connected-support hypothesis added.
- Same-bank perturbations are retained exactly as phases; no `small operator => small random quadratic` step occurs.
- Linear one-copy small-ball needs the explicitly independent third physical square stated in the report.
- Continuity is not claimed for the square-transduced branch.
- Full unrestricted QFORM remains OPEN.

`QFORM_B03_R41_CHECK_PASS`
