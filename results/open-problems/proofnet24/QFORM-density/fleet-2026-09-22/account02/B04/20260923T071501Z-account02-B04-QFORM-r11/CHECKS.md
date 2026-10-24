# Exact and high-precision checks for account02/B04 r11

All computations here are finite algebra/numerical checks supporting the analytic report; they are not substitutes for the proof.

Let

`M_eps=[[2,1,1],[1,1+eps/2,1-eps/2],[1,1-eps/2,1+eps/2]]`,
`w=(0,1,-1)/sqrt(2)`, `P=I-w w^T`, and `M0=M_eps|_{eps=0}`.

## Exact symbolic identities

1. `M_eps = M0 + eps w w^T`, `M0 w=0`, hence `M_eps P=M0`.
2. `det M_eps = 2 eps`.
3. `charpoly(M_eps) = -(eps-lambda)(lambda^2-4 lambda+2)`, so the eigenvalues are exactly
   `2+sqrt(2), 2-sqrt(2), eps`.
4. The nine physical `2x2` minors, by row-pair / column-pair `(12,13,23)`, are

```
[ 1+eps,  1-eps, -eps ]
[ 1-eps,  1+eps,  eps ]
[ -eps,    eps,     2eps ]
```

and therefore

`Z2=e2(M_eps^T M_eps)=4+12 eps^2`.

The canonical squared-minor row-pair masses are

`r12=r13=(2+3eps^2)/(4+12eps^2)`,
`r23=6eps^2/(4+12eps^2)`.

For `M0`, `E2(M0)=4`.

## Globally optimized entropy-weighted two-volume at eps=1e-12

For `q=2(1-ell)` and `ell in [r23,1/3]`, admissibility is exactly `x12,x13,x23>=ell`. KL projection gives

`x23=ell`, `x12=x13=(1-ell)/2`,
`D_min=D_Ber(ell||r23)`,
`G2,opt=(4+12eps^2) exp(-D_min)`.

The certificate is

`B_vol(ell)=2^(5/4)sqrt(e) ell^(-1)(1-ell)^(-1/4) Z2^(-1/8) exp(D_min/8)`.

At `eps=1e-12`, high-precision root solving of

`-1/ell + 1/[4(1-ell)] + (1/8) log(ell(1-r)/(r(1-ell)))=0`

gives

`r = 1.4999999999999999999999955e-24`,
`log(1/r)=54.85657712374893203445...`,
`ell*=0.14436644508250644035...`,
`q*=1.71126710983498711930...`,
`B_vol(ell*)=60.69465364306978212528...`.

The logarithmic derivative has positive second derivative

`1/ell^2 + 1/[4(1-ell)^2] + (1/8)(1/ell+1/(1-ell))`,

so this root is the unique global optimum on the active branch.

## Ridge comparison on the same matrix

For `g=gamma^2`, put

`k=(6g+4)/(g^2+12g+4)`,
`h=eps^2/(eps^2+g)`.

Then the regularized ridge matrix has physical diagonal

`diag K=(k,(k+h)/2,(k+h)/2)`

and `theta=2k+h`.

Therefore the direct ridge gate is impossible for every `g,q`: if `m=max diag K` and `m<=q/2`, then `theta<=3m<=3q/2<2q`.

For the square-assisted ridge theorem, take the explicit valid scale `gamma=eps/2` (`g=eps^2/4`) and `q=2`. Then `h=4/5`,

`k=(4+3eps^2/2)/(4+3eps^2+eps^4/16)`,
`theta=2k+4/5`,
`D=5(1+48/eps^2+64/eps^4)`.

For `0<eps<=1/4`, `k>14/15`, hence `theta>8/3=4q/3`; the leverage gate is automatic because `K<=I` and `q/2=1`.

At `eps=1e-12`,

`k=0.999999999999999999999999625000...`,
`theta=2.799999999999999999999999250000...`,
`D=3.200000000000000000000002400000...e50`,

and the square-assisted ridge formula gives

`B_ridge=1119.47706138150817722485...`.

At this fixed ridge scale the asymptotic is

`B_ridge ~ 21.61371819946173... eps^(-1/7)`.

## Projected-star certificate

The designated-partner row-star theorem applied after coefficient projection gives

`B_proj=2^(3/4)sqrt(pi) E2(M0)^(-1/4)=2^(1/4)sqrt(pi)`

`=2.1078147305108117...`,

uniformly for every `0<eps<1`.

Thus at `eps=1e-12` on the identical physical target matrix:

- Claude/e5 third-volume D/D': inadmissible (the only 3-minor has row marginals one);
- globally optimized entropy-weighted two-volume: `60.6946536431...`;
- direct ridge: no certificate;
- one valid square-assisted ridge scale: `1119.4770613815...`;
- projected exact row-star coefficient packet: `2.10781473051...`.
