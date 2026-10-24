# Checks for QFORM-ROUGH-HUB-L3-SQUARE-COMPILER-v1

Run: `20260923T183544Z-account03-B14-QFORM-auto11`.

## Fourier exponent arithmetic

If `|phi(t)|<=min(1,B|t|^{-3/4})`, then the crossover is `t0=B^{4/3}` and

`int_R |phi|^{3/2} <= 2[t0+B^{3/2}*8*t0^{-1/8}] = 18 B^{4/3}`.

Thus `||phi||_{3/2}<=18^{2/3}B^{8/9}`. Under the Fourier convention used in the report, inverse Hausdorff-Young by interpolation has norm `(2pi)^{-2/3}`, hence

`||p||_3 <= (9/pi)^{2/3}B^{8/9}`.

For the partner slice constant

`A=4 sqrt(pi)/(|h| sqrt(|gamma|))`,

`B=sqrt(pi A)=2 pi^{3/4}|h|^{-1/2}|gamma|^{-1/4}`,

so

`(9/pi)^{2/3}B^{8/9} = 9^{2/3}2^{8/9}|h|^{-4/9}|gamma|^{-2/9}`.

## Square L^(3/2) arithmetic

For a cap-one law and `Z=W^2`, `p_Z(z)<=z^{-1/2}`. Therefore

`int p_Z^{3/2} <= int_0^1 z^{-3/4}dz + int_1^infinity p_Z dz <=4+1=5`,

so `||p_Z||_{3/2}<=5^{2/3}`. Scaling by `a` contributes `|a|^{-1/3}`.

Young therefore yields

`||p_Q||_infinity <=45^{2/3}2^{8/9}|a|^{-1/3}|h|^{-4/9}|gamma|^{-2/9}`.

## Exact-target matrix check

For

`L=(X1+X2+X3+X4)/2`,
`V=(X1+X2-X3-X4)/2`,
`Q=2X0 L+(1/2)V^2+X5^2`,

the deterministic directions `L,V` are orthonormal. In basis `(e0,L,V,e5)` the nonzero block is

`[[0,1,0,0],[1,0,0,0],[0,0,1/2,0],[0,0,0,1]]`.

Its characteristic polynomial is `(lambda^2-1)(lambda-1/2)(lambda-1)`, so the nonzero eigenvalues are `{1,-1,1/2,1}`. Exactly three have absolute value at least one.

At `a=h=1`, `gamma=1/2`, the bound is

`45^{2/3}2^{10/9}=27.32872992777147...`.

These checks use only algebra/calculus; no Monte Carlo or histogram evidence is used.
