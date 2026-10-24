# r32 finite checks

These are deterministic algebra/constant checks for `REPORT.md`; they are not a substitute for the proof.

## Fourier envelope integrals

For `F(t)=min(1,K |t|^(-3/2))`, the crossover is `T=K^(2/3)`.

1. `L1`:

`2[ int_0^T 1 dt + K int_T^infty t^(-3/2) dt ]`
`=2[T+2K T^(-1/2)]`
`=6 K^(2/3)`.

Thus `||p||_infinity <=(2pi)^(-1) 6K^(2/3)=(3/pi)K^(2/3)`.

2. `L2` time:

`2[ int_0^T 1 dt + K^2 int_T^infty t^(-3) dt ]`
`=2[T+(K^2/2)T^(-2)]`
`=3K^(2/3)`.

Thus `||p||_2^2 <=(2pi)^(-1)3K^(2/3)`.

3. Half-Riesz weighted copy time:

`2[ int_0^T t^(-1/2)dt + K^2 int_T^infty t^(-7/2)dt ]`
`=2[2T^(1/2)+(2/5)K^2T^(-5/2)]`
`=(24/5)K^(1/3)`.

## Target-scale constants

From

`K=4 pi^(3/2) sqrt(e) sqrt(|a|)/(|sigma|m sqrt(delta))`

and

`sigma^2m^2/|a| >=s3^3/4`,

we have

`K <=8 pi^(3/2) sqrt(e) s3^(-3/2) delta^(-1/2)`.

Therefore

`(3/pi)K^(2/3)=12 e^(1/3) s3^(-1) delta^(-1/3)`.

Numerically,

`12 e^(1/3)=16.747349101033073...`.

Also

`(3/(2pi))K^(2/3)=6 e^(1/3) s3^(-1)delta^(-1/3)`

with coefficient

`6 e^(1/3)=8.373674550516537...`.

For the weighted copy-time integral,

`(24/5)K^(1/3)
 <=(48/5)sqrt(pi)e^(1/6)s3^(-1/2)delta^(-1/6)`

with coefficient

`20.101505405674022...`.

The designated partner collision inequality doubles `||p||_2^2`, giving exactly the same coefficient as the one-copy `L-infinity` bound:

`P(|Q-Q'|<=eps) <=12e^(1/3)s3^(-1)delta^(-1/3) eps`.

## Entropy certificate

With `p_S=D_S^2/E2` and `mu=(p tensor p)(. | S cap T=emptyset)`, one has

`KL(mu || p tensor p)=log(1/delta)`.

If `q` is either marginal, data processing gives

`KL(q||p)<=log(1/delta)`.

But

`KL(q||p)=sum q log q -sum q log(D_S^2/E2)`
`=log E2-H(q)-sum q logD_S^2`
`=log(E2/Z_q)`.

Hence `Z_q>=E2 delta`.

## Weighted near-intersecting optimization

The proof yields either near-coloop loss `delta+tau` or near-triangle loss

`delta+3delta/(2tau^2)`.

Equating the nontrivial terms gives

`tau^3=3delta/2`,

so

`tau=(3/2)^(1/3)delta^(1/3)`

and

`c_*=(3/2)^(1/3)=1.1447142425533319...`.

## Scope checks

- no pointwise law-uniform quadratic-phase decay used;
- no post-rotation independence used;
- no conditional density cap for a sum/difference variable used;
- no arbitrary-joint coarea lemma used;
- account04/B03 used only through `P(|Y-Y'|<=eps)<=2eps||p_Y||_2^2`;
- full conjecture and full continuity remain open.

`QFORM_B03_R32_CHECK_PASS`
