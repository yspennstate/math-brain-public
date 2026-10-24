# Deterministic checks for affine-bilinear null-bank theorem

Run: `20260923T093454Z-account03-B13-qform-r23`.

## Constant algebra

For dimension `r>=2`, `omega_r=pi^(r/2)/Gamma(r/2+1)` and

`C_r = r^(3/2) omega_r^(1/r)/(2(r-1))`.

Numerical evaluations:

- `omega_2 = pi`, `C_2 = sqrt(2*pi) = 2.5066282746310007...`.
- `omega_3 = 4*pi/3`, `C_3 = (3*sqrt(3)/4)*(4*pi/3)^(1/3) = 2.094038974311569...`.
- `C_4 = 1.9872667859054536...`.
- `C_5 = 1.9481604131182428...`.

Only `r=2,3` are used explicitly in the report.

## Layer-cake check

Let `M>0`, `t0=(M omega_r)^(1/r)`. Then

`int_0^infty min(1,M omega_r t^(-r)) dt`
`= t0 + M omega_r * t0^(1-r)/(r-1)`
`= t0 + t0/(r-1)`
`= [r/(r-1)] (M omega_r)^(1/r)`.

This is finite exactly for `r>1`, which matches the theorem's threshold.

## Scaling check

Replacing `B` by `sB` multiplies the affine-bilinear term by `s`, while

`|det(sB)|^(-1/r)=|s|^(-1)|det B|^(-1/r)`.

Thus the density bound has the required inverse-linear output scaling.

## Product-set section check

For fixed `(u,z)`, the interval section in `v` satisfies

`P(F(u,z)+(2B^T u+c(z)) dot V in J)`
`<= |J| / ||2B^T u+c(z)||_infty`
`<= |J| sqrt(r)/(2 ||B^T(u-u0(z))||_2)`.

The singularity at `u=u0(z)` is integrable in `r>=2` by the layer-cake calculation. No support-radius or fragment-count term appears.

## Correction compatibility

- No post-rotation independence: the linear transform `w=B^T(u-u0)` is used only to estimate an integral of the **joint density** of `U`; it is not used to assert independent transformed coordinates.
- No cross-minor-alone claim: exact `A[T,T]=0` is required in the matrix corollary.
- No near-null perturbation: the theorem makes no statement replacing small `A[T,T]` by zero.
- No bounded-diameter or interval extremality: arbitrary product indicators are allowed, and account04/B13 purification handles arbitrary fragmentation.

`QFORM_B13_093454_NULLBANK_CHECK_PASS`
