# CHECKS — fleet01/B03 shared-slope split-hub theorem

Run: `20260924T075212Z-fleet01-B03-QFORM-r42`.

## Algebra / constants

Let `d=r+s>2`, `M=K_L K_M`, `K=pi^d M`, `T=K^(1/d)=pi M^(1/d)`.

From

`|phi(t)|^2 <= min(1,K |t|^{-d})`

one has

`|phi(t)| <= min(1,K^(1/2)|t|^{-d/2}).`

Then

`int_R |phi(t)| dt`
`<=2[T + K^(1/2) T^(1-d/2)/(d/2-1)]`
`=2T[1+2/(d-2)]`
`=2pi d/(d-2) M^(1/d)`.

Thus

`||p||_infinity <= d/(d-2) M^(1/d)`.

For the negative-half budget,

`A_-<=2[2T^(1/2) + K T^(-d+1/2)/(d-1/2)]`
`= [8d/(2d-1)] T^(1/2)`
`= [8d/(2d-1)] sqrt(pi) M^(1/(2d)).`

Using `integral_R |t|^(-1/2)e^(itx)dt=sqrt(2pi)|x|^(-1/2)`,

`E|Q-Q'|^(-1/2)<=4sqrt(2)d/(2d-1) M^(1/(2d)).`

For the positive-half budget,

`A_+<=2[(2/3)T^(3/2)+K T^(-d+3/2)/(d-3/2)]`
`=[8d/(3(2d-3))] T^(3/2)`
`=[8d/(3(2d-3))] pi^(3/2) M^(3/(2d)).`

At `d=3`, `M=1`:

- density constant: `3`;
- `A_-=(24/5)sqrt(pi)=8.507778484346476...`;
- Riesz constant: `12sqrt(2)/5=3.3941125496954285...`;
- `A_+=(8/3)pi^(3/2)=14.848874658217888...`.

## Plancherel normalization

With `hat h(xi)=integral h(u)e^(i xi.u)du`,

`integral |hat h|^2=(2pi)^r integral |h|^2`.

Since `F_t(l)=hat h_t(2t l)`,

`integral |F_t(l)|^2 dl`
`=(2|t|)^(-r)(2pi)^r integral |h_t|^2`
`<=pi^r|t|^(-r)`.

The cap-one product input gives

`integral |h_t|^2=prod_i integral f_i^2<=1`.

Hence `E|F_t(L)|^2<=pi^r K_L |t|^-r`, with the exact same calculation for the `V` block.

## Exact target-family spectrum

For

`Q=2U1Y1+2U2Y2+2VY1`,

write the cross matrix from `(U1,U2,V)` to `(Y1,Y2)` as

`B=[[1,0],[0,1],[1,0]]`.

Then

`B^T B=diag(2,1)`,

so the singular values of `B` are `sqrt(2),1`. For

`A=[[0,B],[B^T,0]]`,

the nonzero eigenvalues are `+sqrt(2),-sqrt(2),+1,-1`; the fifth eigenvalue is zero. Thus the family satisfies the owner target with four eigenvalues of modulus at least one.

## Scope check

The proof uses:

- genuine original-coordinate product independence only for the physical hub blocks and cap-one `L^2` norms;
- marginal density caps for `L(Y)` and `M(Y)` only;
- arbitrary dependence between `L` and `M`;
- arbitrary same-environment phase `R(Y)`;
- arbitrary self-curvature inside each hub block.

It does **not** use:

- conditional density caps such as `p_{M|L}`;
- independence of rotated coordinates;
- pointwise van-der-Corput decay;
- moments, log-concavity, compactness or connected support;
- separation of coordinatewise `X-X'` and `X+X'` variables.

The structural hypothesis not yet removed is the absence of a quadratic cross term between the two physical hub groups.

Marker: `QFORM_B03_SHARED_SLOPE_SPLIT_HUB_CHECK_PASS`.
