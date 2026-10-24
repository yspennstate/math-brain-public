# Addendum — full arbitrary-dimensional centered-Gaussian ceiling

This strengthens the run's rank-three theorem without altering its status: the full arbitrary bounded-density QFORM conjecture remains OPEN.

## Theorem `QFORM-CENTERED-GAUSSIAN-FULL-C3SQRT2-v1`

Let `G~N(0,Sigma)` in `R^n` with `Sigma>=sigma^2 I_n`, `sigma>0`. Let `A` be any real symmetric `n x n` matrix having at least three eigenvalues of absolute value at least one. Then `Q=G^T A G` has a bounded continuous density and

`||p_Q||_infinity <= 1/(2 sqrt(2) sigma^2)`.

The constant is sharp in this class: for `n=3`, `Sigma=sigma^2 I_3`, `A=diag(1,1,-1)`, equality holds.

For the covariance floor `sigma^2=1/12` forced in centered covariance-convergent projection limits of product densities bounded by one, the sharp bound is `3 sqrt(2)`.

### Step 1: large signed spectral directions survive covariance congruence

Put

`B=Sigma^(1/2) A Sigma^(1/2)`.

Suppose `A` has `r` eigenvalues at least `1`, and let `E_+` be the span of corresponding eigenvectors. On the `r`-dimensional subspace

`F_+=Sigma^(-1/2) E_+`,

for every `z in F_+`, writing `y=Sigma^(1/2) z in E_+`,

`z^T B z = y^T A y >= ||y||^2 = z^T Sigma z >= sigma^2 ||z||^2`.

By the Courant-Fischer min-max principle, `B` therefore has at least `r` eigenvalues at least `sigma^2`.

Similarly, if `A` has `s` eigenvalues at most `-1`, then `B` has at least `s` eigenvalues at most `-sigma^2`.

Diagonalize `B=O^T diag(mu_1,...,mu_n)O`. Since `OZ` is again standard Gaussian,

`Q` has the same law as `sum_j mu_j Z_j^2`

with independent standard Gaussian `Z_j`.

### Step 2: mixed-sign triple

If among the large eigenvalues of `A` there are two positive and one negative, or two negative and one positive, Step 1 supplies three independent Gaussian-square terms with coefficients `a,b,-c` (up to global sign) satisfying

`a,b,c>=sigma^2`.

The run report proves exactly that the three-term core

`Y_0=aU^2+bV^2-cW^2`

has

`||p_{Y_0}||_infinity <= 1/(2 sqrt(2) sigma^2)`.

All remaining diagonalized terms form an independent random variable `R`. Since convolution with any probability measure does not increase an `L^infinity` norm,

`||p_{Y_0+R}||_infinity <= ||p_{Y_0}||_infinity`.

Thus the theorem follows in the mixed-sign case.

### Step 3: same-sign triple via an explicit gamma convolution factorization

It remains to handle the case where three large eigenvalues have the same sign. After a global sign change, Step 1 supplies a positive three-term core

`Y_+=a_1 Z_1^2+a_2 Z_2^2+a_3 Z_3^2`,

with every `a_j>=sigma^2`.

We first prove a distributional factorization. Let `X=Z^2`, so

`E exp(-sX)=(1+2s)^(-1/2)`.

For `c>=1`,

`E exp(-s cX)=(1+2cs)^(-1/2)
              =(1+2s)^(-1/2) L_c(s)`,

where

`L_c(s)=sqrt((1+2s)/(1+2cs))`.

The ratio `L_c` is itself a probability Laplace transform. Indeed,

`log L_c(s)
 = -(1/2)[log(1+2cs)-log(1+2s)]
 = -(1/2) int_0^infty (1-e^{-sx})
      [e^{-x/(2c)}-e^{-x/2}] dx/x`.

The measure

`nu_c(dx)=(1/2)[e^{-x/(2c)}-e^{-x/2}] dx/x`

is nonnegative and satisfies the Levy integrability condition. Hence `L_c(s)=exp(-int(1-e^{-sx})nu_c(dx))` is the Laplace transform of a nonnegative infinitely divisible random variable `R_c`.

Therefore

`c Z^2 =_d Z_0^2 + R_c`,

with `Z_0^2` and `R_c` independent. Scaling by `sigma^2` and taking the three coefficients `c_j=a_j/sigma^2>=1` gives

`Y_+ =_d sigma^2 chi_3^2 + R`

for some independent nonnegative `R`.

The `chi_3^2` density is

`f_3(x)=x^(1/2)e^{-x/2}/sqrt(2 pi),  x>0`,

whose maximum occurs at `x=1` and equals

`1/sqrt(2 pi e)`.

Thus

`||p_{Y_+}||_infinity
 <= 1/(sigma^2 sqrt(2 pi e))
 < 1/(2 sqrt(2) sigma^2)`,

because `pi e>4`.

Again, convolution with all remaining independent diagonalized terms cannot increase the density norm. This proves the same-sign case and hence the theorem.

### Step 4: sharpness and implication for product-law Gaussian limits

The mixed-sign equality example `Sigma=sigma^2 I_3`, `A=diag(1,1,-1)` has peak exactly `1/(2 sqrt(2) sigma^2)`, as proved in the run report. Hence the arbitrary-dimensional centered-Gaussian theorem is sharp.

For independent original-coordinate variables with densities bounded by one and finite variances, every centered three-or-more-dimensional orthogonal projection covariance obeys the matrix floor `Sigma>=I/12`; this follows from the one-dimensional variance lower bound `Var X_i>=1/12`. Therefore every centered covariance-convergent Gaussian projection limit of a target-admissible product-law sequence satisfies

`||p_{G^T A G}||_infinity <= 3 sqrt(2)`

for every limiting spectral form with at least three eigenvalues of modulus at least one. Account02/B17's uniform block construction attains this value. Thus `3 sqrt(2)` is the **exact ceiling for the entire centered Gaussian-limit mechanism**, in arbitrary dimension and with arbitrary extra spectral directions.

Any source-valid lower-bound witness strictly above `3 sqrt(2)` must therefore use a mechanism outside centered Gaussian projection limits (for example noncentral surviving linear terms, a genuinely non-Gaussian limit, mesoscopic localization, or a finite-dimensional construction).

No claim is made that `3 sqrt(2)` is the global constant for the original bounded-density problem.
