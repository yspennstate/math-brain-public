# B03 r36 deterministic checks

Run `20260923T150538Z-fleet03-B03-QFORM-r36`.

These are exact algebra/constant checks for `REPORT.md`; they are not Monte Carlo evidence.

## 1. Augmented Gram/leverage identities

Rows:

`b0=(a,0)`, `bj=(beta v_j+m q_j,v_j)`, with `v.q=0`, `||v||=||q||=1`.

Summing rows gives

`G=[[a^2+beta^2+m^2,beta],[beta,1]]`,

`det G=a^2+m^2`.

The inverse is

`G^(-1)=(a^2+m^2)^(-1)[[1,-beta],[-beta,a^2+beta^2+m^2]]`.

Therefore

`b0^T G^(-1)b0=a^2/(a^2+m^2)=1-theta`,

`theta=m^2/(a^2+m^2)`,

and

`bj^T G^(-1)bj
 =[(beta v_j+m q_j-beta v_j)^2+(a^2+m^2)v_j^2]/(a^2+m^2)
 =v_j^2+theta q_j^2`.

Their sum is

`(1-theta)+sum_j(v_j^2+theta q_j^2)=1-theta+1+theta=2`,

as required for a two-dimensional tight frame.

**PASS.**

## 2. Theorem 3.1 Fourier/density constants

Starting from

`K=4 pi^(3/2)L sqrt(|a|)/(|sigma|sqrt(a^2+m^2))`,

for `F(t)=min(1,K |t|^(-3/2))` the crossover is `T=K^(2/3)`.

Exact integrals:

`int_R F(t) dt
 =2[T+K int_T^infinity t^(-3/2)dt]
 =2[T+2K T^(-1/2)]
 =6K^(2/3)`.

Thus

`||p||inf <=(2pi)^(-1)6K^(2/3)
 =3*2^(4/3)L^(2/3)[sigma^2(a^2+m^2)/|a|]^(-1/3)`.

Also

`int_R F(t)^2 dt
 =2[T+K^2 int_T^infinity t^(-3)dt]
 =2T+K^2T^(-2)=3K^(2/3)`.

And

`int_R |t|^(-1/2)F(t)^2 dt
 =2[2T^(1/2)+K^2*(2/5)T^(-5/2)]
 =(24/5)K^(1/3)`.

Under `L<=sqrt(e)`, `y^2>1/2`,

`3*2^(5/3)e^(1/3)=13.292379790329292...`.

**PASS.**

## 3. Hyperbolic half-Riesz branch

For a scalar density cap `M`, layer cake gives

`sup_s E|Y-s|^(-1/2)
 <=int_0^infinity min(1,2M lambda^(-2)) dlambda
 =2sqrt(2M)`.

If `U,V` are independent with caps `M_U,M_V`, conditioning on `U` yields

`sup_s E|s-cUV|^(-1/2)
 <=2sqrt(2M_V/|c|) E|U|^(-1/2)
 <=8sqrt(M_U M_V/|c|)`.

With `c=2sigma`, multiplying the physical-square kernel `|a|^(-1/2)` gives

`4sqrt(2)sqrt(M_U M_V)|a sigma|^(-1/2)`.

If `theta<1/2`, then `m^2<a^2`; with `m=rho y`, `y^2>1/2`,

`a^2/rho^2>1/2` and

`|a sigma|=(a^2/rho^2)(gamma|sigma|)>s_3(A)^2/2`.

For `M_U,M_V<=sqrt(e)`, the normalized coefficient is

`8sqrt(e)=13.189770165601026...`.

**PASS.**

## 4. One-anchor determinant currencies

For augmented right-plane rows, let anchor be right row `r` and `eta_r=v_r^2+q_r^2`.

The pivot-anchor minor contributes

`det((a,0),(h_r,v_r))^2=a^2v_r^2`.

For right-right pairs,

`det((h_r,v_r),(h_j,v_j))
 =det((beta v_r+m q_r,v_r),(beta v_j+m q_j,v_j))
 =m(q_rv_j-v_rq_j)`.

The Parseval plane identity gives

`sum_(j!=r)(q_rv_j-v_rq_j)^2=v_r^2+q_r^2=eta_r`.

Therefore

`Z1=a^2v_r^2+m^2eta_r`.

Total augmented two-volume is `det G=a^2+m^2`; hence

`Z0=(a^2+m^2)-Z1
   =a^2(1-v_r^2)+m^2(1-eta_r)`.

With `delta=Z0/(a^2+m^2)`,

`Z1=(a^2+m^2)(1-delta)` and

`sqrt(Z1 Z0)=(a^2+m^2)sqrt(delta(1-delta))`.

**PASS.**

## 5. One-anchor Brascamp--Lieb constants

For `I2`, anchor exponent one plus low-row determinant weights `alpha_j` gives

`I2 <= Z1^(-1/2) * (2pi) * (4pi)^(sum alpha)
    =8pi^2 Z1^(-1/2)`,

because `sum alpha=1` and the entropy factors cancel the `sqrt(alpha_j)` factors from the sharp `L^(1/alpha_j)` Fourier estimate.

For `I0`, low-row two-volume weights have marginals summing to two, hence

`I0 <=(4pi)^2 Z0^(-1/2)=16pi^2 Z0^(-1/2)`.

Thus

`I<=sqrt(I2 I0)=8sqrt(2)pi^2(Z1Z0)^(-1/4)`.

Inserted into the Fresnel prefactor this yields

`K_r=2sqrt(2)pi^(3/2)L sqrt(|a|)/(|sigma|(Z1Z0)^(1/4))`.

Fourier inversion then gives

`||p||inf <=6L^(2/3)[|a|/(sigma^2sqrt(Z1Z0))]^(1/3)`.

Using the target spectral scale gives

`6(2e)^(1/3)[delta(1-delta)]^(-1/6)/s_3(A)`.

At `delta=1/16`, the worst point in `[1/16,1/2]`,

`6(2e)^(1/3)(15/256)^(-1/6)
 =16.92846294709618...`.

**PASS.**

## 6. Partner collision arithmetic

For either `|phi|<=min(1,K|t|^(-3/2))` branch,

`||p||_2^2 <=(2pi)^(-1) int |phi|^2
           <=3K^(2/3)/(2pi)`.

The valid fleet04/B03 lemma gives

`P(|Q-Q'|<=eps)<=2eps||p||_2^2
                <=(3/pi)K^(2/3)eps`,

which is exactly the coefficient obtained from `L^1` Fourier inversion for the density.

**PASS.**

## 7. Correction-boundary regression

The proofs above use none of the live-refuted interfaces:

- no pointwise scalar quadratic van-der-Corput bound;
- no post-rotation independence;
- no conditional cap for sum given difference or vice versa;
- no arbitrary-joint coarea inequality;
- no positive moment/supremum of a worst conditional projection cap;
- no deletion of a small nonzero transverse quadratic term;
- no inference of a universally large single physical minor from aggregate volume.

The only sum/difference statement is the complete-copy identity

`|phi_Q(t)|^2=E exp(it(Q-Q'))`.

**PASS.**
