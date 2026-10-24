# Deterministic checks — account01/B09 20260924T015544Z

These are algebraic/numerical regressions only; they are not evidence for a universal theorem beyond the proved derivation in `REPORT.md`.

## 1. Completion identity

For `B=tau ell ell^T`, with `ell=(ell1,ell2)`, set

`a=tau ell1^2`, `b=tau ell1 ell2`, `c=tau ell2^2=b^2/a`.

Then direct expansion verifies

`a[x+(b/a)y+(g1/a)W]^2 + 2[g2-(b/a)g1]Wy -(g1^2/a)W^2`

is exactly

`a x^2+2bxy+c y^2+2g1 xW+2g2 yW`.

For `k=(-ell2,ell1)`,

`beta=g2-(ell2/ell1)g1=(k^T g)/ell1`,

hence `|a beta|=|tau| |ell1| |k^Tg|`.

## 2. Bathtub constants

One-sided kernel with probability density cap `D`:

`D int_0^(1/D) y^(-1/2)dy = 2 sqrt(D)`.

Symmetric kernel with probability density cap `D`:

`D int_(-1/(2D))^(1/(2D)) |y|^(-1/2)dy = 2 sqrt(2D)`.

With the projection cap `S=sqrt(2)/||r||_2` and scaling `Y=2 beta W+eta`,

`D_Y=S/(2|beta|)`

and therefore

`E|Y|^(-1/2)<=2 sqrt(S/|beta|)`.

Combining with the fixed-leaf conditional bound gives

`4 |a|^(-1/2) sqrt(S/|beta|)
 =2^(9/4)|a beta|^(-1/2)||r||_2^(-1/2)`.

Using `|ell1|>=2^(-1/2)` gives the theorem constant `2^(5/2)`.

Numerically:

- `2^(9/4) = 4.756828460010884`
- `2^(5/2) = 5.656854249492381`
- `2^(7/2) = 11.313708498984761`

## 3. Stress-family spectrum

For `m=64`,

`B=diag(1,0)`, `g=e2`, `r=(1/sqrt(m),...,1/sqrt(m))`, and `D=t vv^T` with `v=(e1-e2)/sqrt(2)` (so `v perpendicular r`), direct symmetric eigensolver checks gave the nonzero eigenvalues:

- `t=0`: `[-1, 1, 1]`
- `t=0.5`: `[-1, 0.5, 1, 1]`
- `t=10`: `[-1, 1, 1, 10]`
- `t=-3`: `[-3, -1, 1, 1]`

and in every case the third singular value is `1` to floating-point tolerance. This matches the exact invariant-subspace decomposition: one isolated eigenvalue `1`, a star block with eigenvalues `+1,-1`, and the transverse leaf eigenvalue `t`.

## 4. Spectral branch inequalities

For `A=A0+diag(0,D)` with `s3(A)>=1` and `d=||D||op`, Weyl gives

`s3(A0)>=1-d`.

The literal test vectors `k` and a unit `h perpendicular g` give

`s3(A0)<=s`, `s3(A0)<=|tau|`.

Therefore for `d<1`,

`|tau|s >=(1-d)^2`.

At overlap scale `Omega_(2,H)>=1/4`, the exact previous-run identity

`P_H+Omega_(2,H)=tau^2 s^4`

gives `|tau|s^2>=1/2`. If simultaneously `|tau|s<1/4`, then

`s>2`, `|tau|<1/8`.

Because `s3(A0)<=|tau|`, Weyl then forces `||D||op>7/8`.

All inequalities are deterministic; no histogram or Monte Carlo extremality claim is used.
