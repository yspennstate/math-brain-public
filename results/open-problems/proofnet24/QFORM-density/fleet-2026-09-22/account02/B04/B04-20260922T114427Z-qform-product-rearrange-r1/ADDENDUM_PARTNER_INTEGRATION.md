# B04 controlling addendum — named-partner integration and constant sharpening

The named partner `account03/B04` completed its current-programme handoff during this run, after the primary B04 report had already been written. I consumed it at brain commit `9c946331d5e97e35584005a98d0e496fae7014d0`; canonical partner report `yspennstate/math-open-problems@f824ded997ee16c741468bb49860e1ccaf18d8bd`, blob `2438594f82b064359483972f59f4d061a6814ce0`.

The partner proves exactly the averaged one-square estimate

`||E exp(i t lambda Y^2)||_3 <= 2(2pi)^(1/3) M^(2/3)|lambda|^(-1/3)`

whenever `Y` has density bounded by `M`, and applies it to three independent square directions. I apply that result here to sharpen the constants in my private-block and `1+2` theorems; this is a genuine use of the named partner result, not a peer outcome label.

## 1. Best product-marginal cap on a private block

For a private linear form

`Y=a·X_S + shift`,

write

`rho=||a||_2`, `sigma=||a||_infinity`.

Two source-valid density bounds are available:

1. Livshyts--Paouris--Pivovarov gives `||p_Y||_infinity <= sqrt(2)/rho`.
2. Conditioning on all coordinates except one attaining `sigma`, the remaining scaled coordinate has density at most `1/sigma`, and convolution cannot increase `L^infinity`; hence `||p_Y||_infinity <=1/sigma`.

Therefore define the effective cap

`kappa(a):=min(sqrt(2)/||a||_2, 1/||a||_infinity)`.                            (1)

The second term is precisely the localization resource used in the partner handoff; the first is useful for diffuse blocks.

## 2. Sharpened private-block Fourier theorem

Under the hypotheses of `QFORM-PRIVATE-BLOCK-FOURIER-v1` in the primary report, put

`kappa_j=kappa(a_j)`.

Applying the named partner one-square `L^3` bound conditionally on the shared block and Hölder gives

`||phi_Q||_1
 <= 16 pi (kappa_1 kappa_2 kappa_3)^(2/3)
    |lambda_1lambda_2lambda_3|^(-1/3)`,                                       (2)

and hence a continuous density with

`||p_Q||_infinity
 <= 8 (kappa_1 kappa_2 kappa_3)^(2/3)
    |lambda_1lambda_2lambda_3|^(-1/3)`.                                       (3)

This dominates the earlier `16/((rho_1rho_2rho_3)^(2/3)|prod lambda|^(1/3))` estimate because `kappa_j<=sqrt(2)/rho_j`.

For a same-sign pair `i,j`, the beta-convolution argument similarly sharpens to

`||p_Q||_infinity
 <= pi kappa_i kappa_j/sqrt(|lambda_i lambda_j|)`.                             (4)

### Revised constant in the six-coordinate rotated example

In the primary example each private block is a singleton with coefficient `1/sqrt(2)`, so `kappa_j=sqrt(2)`. For eigenvalues `(2,-1,-1)`, (3) gives

`||p_Q||_infinity <= 16/2^(1/3)`,

while the same-sign pair `(-1,-1)` and (4) give the sharper bound

`boxed(||p_Q||_infinity <=2 pi)`.                                              (5)

Thus the earlier `4 pi` example constant is valid but noncontrolling; `2 pi` is the source-bound sharpened value after applying the partner result.

## 3. Sharpened scalar factor in the `1+2` mixed theorem

In `QFORM-1PLUS2-MIXED-FOURIER-v1`, replace the scalar-block estimate `K<=sqrt(2)/alpha` by

`K<=kappa(a)`.

The proof is otherwise unchanged, and the controlling bound is

`||phi_Q||_1
 <= 6^(2/3) pi^(-1/3)
    [ kappa(a) B_RV^2 ]^(2/3)
    / [ det(M)^(1/3)|lambda det(Gamma)|^(1/3) ]`.                              (6)

Fourier inversion divides the right side by `2pi` for the density bound.

For a singleton scalar block with unit coefficient, `kappa=1`, improving the previous substitution `sqrt(2)/alpha=sqrt(2)` by a factor `2^(1/3)` at the characteristic-function level.

## 4. Frontier after partner integration

The partner handoff and the present B04 run now agree on the same structural endpoint: three independent square budgets close in `L^3 x L^3 x L^3 -> L^1_t`, but generic overlapping spectral directions do not factor.

The new B04 Schur/fractional theorem goes strictly beyond that disjoint-factor endpoint for a non-isotropic large physical row: it permits full spectral contamination of the pivot row and removes the correlated completed-square shift by a one-sided fractional integral against an `L^3` residual quadratic density. The exact isotropic model is separately controlled by the logarithmic-product plus square theorem.

Thus the immediate rank-three missing mechanism is now the **generic isotropic/near-isotropic overlapping residual** or a state with multiple projected large rows. A valid next theorem must retain the original coordinate product law and cannot multiply rotated marginal bounds.

Full `QFORM-FULL` remains open, including the additional-eigendirection dependence problem.
