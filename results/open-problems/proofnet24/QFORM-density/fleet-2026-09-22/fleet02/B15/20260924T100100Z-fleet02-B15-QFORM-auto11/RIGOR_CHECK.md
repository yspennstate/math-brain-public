# Rigor check — fleet02/B15 20260924T100100Z

Result checked: `QFORM-FRESNEL-SUBMASS-2OVER3-v1` and its aggregate stability corollary in `REPORT.md`.

## A. Constants in the selected-factor Brascamp–Lieb step

For row leverage `c in (0,1/2]`, the selected twisted subdensity factor `a` has mass `m` and `|a|<=g<=1`. Thus

`||a^||_infinity<=m`, `||a^||_2^2=2pi||a||_2^2<=2pi m`.

At `p=1/c`,

`int |a^|^p <=2pi m^(p-1)`.

The geometric BL factor for that row is therefore

`[c^(-1/2) 2pi m^(1/c-1)]^c
 =(4pi)^c (2sqrt(c))^(-c)m^(1-c)`.

Relative to the source Theorem-F probability factor `(4pi)^c`, this is exactly

`eta=(2sqrt(c))^(-c)m^(1-c)`.

All other source factors are unchanged. Hence

`|nu^(t)| <= B eta |t|^(-3/2)`, `B=(4pi)^(3/2)L^(-1/2)`.

Together with `|nu^(t)|<=m`, the exact integral is

`int_R min(m,B eta |t|^(-3/2))dt=6(B eta)^(2/3)m^(1/3)`.

Dividing by `2pi` yields

`12L^(-1/3)(2sqrt(c))^(-2c/3)m^(1-2c/3)`.

The `c=0` case is separate and harmless: the rank-three part does not involve that original coordinate, while the diagonal/affine part is independent of the remaining coordinates. Convolution with its mass-`m` pushforward multiplies the source height by at most `m`.

## B. Uniform submass exponent

For

`a(c)=(2sqrt(c))^(-2c/3)`,

`log a(c)=-(2c/3)(log2+(1/2)log c)`.

The critical point is `c=1/(4e)` and `log a=1/(12e)`. Therefore

`a(c)<=exp(1/(12e))` for `0<=c<=1/2`.

Also `1-2c/3>=2/3`; since `m<=1`, `m^(1-2c/3)<=m^(2/3)`. This proves the uniform submass bound.

## C. Signed one-coordinate difference

If `delta=||f-g||_1`, positive and negative parts have mass `delta/2`. Twice the submass bound gives

`2*12(2sqrt(c))^(-2c/3)(delta/2)^(1-2c/3)
 =12 c^(-c/3)delta^(1-2c/3)`.

The powers of 2 cancel because `(2c/3)+(1-2c/3)=1`.

## D. Dimension-free aggregation

Let `c_i<=h<=1/2`, `sum c_i=3`, `p_h=1-2h/3`. Since

`1-2c_i/3=(1-c_i/h)+ (c_i/h)p_h`,

weighted AM–GM gives

`delta_i^(1-2c_i/3)<=(1-c_i/h)delta_i+(c_i/h)delta_i^p_h`.

Concavity of `x^p_h`, with weights `c_i/3`, gives

`sum c_i delta_i^p_h <=3[(sum c_i delta_i)/3]^p_h <=3(h Delta/3)^p_h`.

Therefore

`sum delta_i^(1-2c_i/3)<=Delta+(3/h)^(2h/3)Delta^(1-2h/3)`.

Finally

`max_{0<=c<=h}c^(-c/3)=h^(-h/3)` for `h<=e^(-1)` and `exp(1/(3e))` for `h>=e^(-1)`.

No dimension factor remains.

## E. Scope checks

- The source theorem used is exactly the diagonal-plus-rank-three diffuse Fresnel theorem; no arbitrary higher-rank remainder is inserted.
- No independence of the three spectral coordinates is used.
- The selected subdensity remains in an ORIGINAL coordinate.
- Affine and diagonal phases have modulus one and do not change the `L^p` calculation.
- Essential height is obtained from the `L^1` Fourier bound; continuity is a consequence, not a premise.
- The bank example `Y_1^2+Y_2^2-Y_3^2` has exact target spectrum `{1,1,-1}` and its direct `2pi` height uses genuine independence of the three disjoint original-coordinate banks.
- The ruled rough-input bridge mollifies original coordinates and passes interval domination in total variation; it never evaluates a rough representative pointwise on a ruling.

Checker verdict: `QFORM_B15_FRESNEL_SUBMASS_CHECK_PASS`.
