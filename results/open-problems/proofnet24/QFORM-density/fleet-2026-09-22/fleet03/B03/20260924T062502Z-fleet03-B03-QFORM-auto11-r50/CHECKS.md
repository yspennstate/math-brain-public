# fleet03/B03 r50 deterministic checks

All checks below are algebraic/numerical consistency checks for `REPORT.md`; they are not Monte Carlo evidence for the theorem.

## 1. Plancherel normalization

With `hat g(xi)=int g(h)e^{i xi h}dh`,

`int |hat g(xi)|^2 dxi = 2 pi int |g(h)|^2 dh`.

For `I_t(l)=hat g_t(2 gamma t l)`, `xi=2 gamma t l`, so

`int |I_t(l)|^2 dl
 = (1/(2|gamma t|)) 2pi int |g_t|^2
 = pi/(|gamma t|) int f_H^2`.

Since `f_H<=1` and `int f_H=1`, `int f_H^2<=1`.

PASS.

## 2. Negative-half crossover integral

For `K>0`,

`2[ int_0^K t^(-1/2)dt + K int_K^infinity t^(-3/2)dt ]`

`=2[2 sqrt(K)+2 sqrt(K)]`

`=8 sqrt(K)`.

PASS.

Using

`K0=sqrt(2)/(sqrt(63/64)*sqrt(1-2^-24))`

gives

`K0 = 1.4253933326796289...`,

`8 sqrt(pi K0) = 16.929038195804875...`,

`4 sqrt(2 K0) = 6.753709102837353...`.

PASS.

## 3. Near-coloop slope norm

In the live fleet03/B16 frame,

`||s||^2=1-c`, `||p||^2=1`, `s.p=0`.

Thus

`||a s+b p||^2=a^2(1-c)+b^2`

exactly. Since `||Lambda e1||^2=a^2+b^2>=1`,

`a^2(1-c)+b^2 >=1-ca^2`.

From `D>=1` and `0<|a|D<2^-12`, one has `|a|<2^-12`, hence

`1-ca^2 > 1-2^-24`.

PASS.

## 4. Positive-half crossing integral

If

`|phi_T(t)|<=min(1,A/|t|)`,

then

`int_R |t|^(1/2)|phi_T(t)|^2dt`

`<=2[ int_0^A t^(1/2)dt + A^2 int_A^infinity t^(-3/2)dt ]`

`=2[(2/3)A^(3/2)+2A^(3/2)]`

`=(16/3)A^(3/2)`.

For B03 r41, `A=2pi |det C|^(-1/2)`, giving

`A_+ <= (16/3)(2pi)^(3/2)|det C|^(-3/4)`.

PASS.

## 5. Complementary-weight constant

Combine

`A_-<=8 sqrt(pi M/|gamma|)`

with

`A_+<=(16/3)(2pi)^(3/2)|det C|^(-3/4)`

and multiply by `(2pi)^(-1)` after Cauchy--Schwarz. The constant simplifies as

`(2pi)^(-1) sqrt[(128/3)(pi M/|gamma|)^(1/2)(2pi)^(3/2)|det C|^(-3/4)]`

`= [2^(13/4)/sqrt(3)] (M/|gamma|)^(1/4)|det C|^(-3/8)`.

Numerically

`2^(13/4)/sqrt(3)=5.492712383752314...`.

At `M/|gamma|<=K0` and `|det C|>=1`,

`5.492712383752314 * K0^(1/4)
 =6.001648263752153...`.

PASS.

## 6. Designated-partner time conversion

If `||p_Q||_infinity<=K`, then the convolution density of `Q-Q'` has cap at most `K`. The elementary cap-to-half-Riesz bound gives

`E|Q-Q'|^(-1/2)<=2sqrt(2K)`.

Multiplying by `sqrt(2pi)` through the whole-copy Riesz identity yields

`int |t|^(-1/2)|phi_Q(t)|^2dt <=4sqrt(pi K)`.

For partner r4

`K=129.924435862525374 J_2(H)^(-1/6)`,

the prefactor is

`4sqrt(pi*129.924435862525374)
 =80.81283593365677...`.

At `K<333.880`,

`4sqrt(pi*333.880)
 =129.54782623760602...`.

PASS.

## 7. Scope audit

- No pointwise quadratic-phase decay is used.
- No rotated coordinates are declared independent.
- The fresh hub `H` is an actual original-coordinate source independent of the full light bank.
- Dependence between the random slope `L` and remainder `R` is retained.
- The nonzero hub square is retained as a unit-modulus chirp inside Plancherel.
- The whole-copy identity is applied only to `Q-Q'`.
- Linear small-ball scaling is claimed only after an explicitly source-disjoint complementary positive-half time resource.
- The bare nonzero near-coloop collar remains an `L^infinity` gap.
- Full QFORM and full-target continuity remain open.

`QFORM_B03_R50_CHECK_PASS`
