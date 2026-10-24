# account02/B05 — product-projection / exceptional-slice endpoint after the s9 proof

Source baseline: commit `7c0d6e60946b19423e6400a12d34b473cf0591e2`, manuscript blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.

## Certified fixed-multiplicity status

The complete account02/B05 grouped-product proof gives

`||p_Q||_infinity < 5338 K^2/s` whenever `s_9(A)>=s>0`.

This proof is source-valid for arbitrary rough independent coordinate densities: every probabilistic split is on literal original coordinate banks; projected coordinates are used only through joint marginal density bounds; rough complex pushforwards are mollified before `L^2` expansion and passed to the limit by Fourier-side Fatou.

## New endpoint localization at s8

Fresh supporting work on master shows that the remaining no-pivot `s_8` collar can be put into a source-disjoint split-row form with

`|phi_Q(t)| <= min(1,U/|t|)`

for a universal `U`, and therefore into every finite `L^r` with norm growth of order `r`. A separate Schur-fusion identity cancels the logarithmic critical-value dependence on the small indefinite-pair determinant, but leaves a nonlogarithmic `D^(-1/2)` term.

These two facts do **not** imply bounded density. The obstruction is sharp at the level of functional class.

Take independent `X,Y ~ Unif[-1/2,1/2]` and `R=2XY`. Then

`p_R(t)=log(1/(2|t|))`, `0<|t|<1/2`,

so `p_R` is unbounded. Nevertheless

`||p_R||_r^r = Gamma(r+1)`

for every finite `r>=1`, hence `||p_R||_r ~ r/e`, and

`P{|R|<=epsilon}=2 epsilon [log(1/(2epsilon))+1]`.

Thus a proof that forgets the surviving overlap-one curvature and retains only the critical `1/|t|` Fourier envelope / finite-`L^r` endpoint cannot close `L^infinity`.

The same example also shows why exceptional slices cannot be replaced by pointwise uniform caps. It is the exact opposite-sign hyperbolic critical singularity already present in the baseline pair lemma.

## Product-projection warning, quantitatively sharp

For independent `X_1,X_2 ~ Unif[-1/2,1/2]`, define

`Y=(X_1+X_2)/sqrt(2)`, `Z=(X_1-X_2)/sqrt(2)`.

Then

`p_Y(y)=sqrt(2)-2|y|`

on its support, while conditionally on `Y=y`, `Z` is uniform on an interval of that same length. Therefore

`||p_(Z|Y=y)||_infinity = 1/(sqrt(2)-2|y|) -> infinity`

at the boundary. Hence no `s_8` endpoint may condition on a rotated/projected coordinate and then reuse an unconditional product-projection cap.

## Required next theorem

To lower nine to eight, one must spend the surviving `Omega_1` / overlap-one / rank-saturation currency before the critical endpoint is collapsed. A sufficient replacement would be either

1. a product-preserving Fourier receiver with universal gain `|phi_Q(t)| <= C|t|^(-1-epsilon)` for some `epsilon>0`, or
2. a direct interval theorem `P{Q in I}<=C|I|`

for the exact two-sided collar, with all same-bank curvature retained and no post-rotation independence or unrestricted curved-fiber supremum.

No such receiver is proved here. Multiplicity eight is OPEN. The unrestricted three-eigenvalue conjecture is OPEN.
