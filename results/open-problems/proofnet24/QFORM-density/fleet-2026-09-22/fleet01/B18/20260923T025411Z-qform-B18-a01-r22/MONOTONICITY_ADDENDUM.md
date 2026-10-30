# fleet01/B18 r22 monotonicity addendum

This addendum supplies the derivative check omitted from the terse statement after equation (2.3) of `REPORT.md`. It changes no theorem, constant, or scope.

Let `K_*(r)` denote the centered-uniform comparator cap from (2.3).

For `0<r<=1/sqrt(3)`,

`K_*(r)=(sqrt(3)/4)sqrt(1+r^2)(3-r^2)`.

Hence

`K_*'(r)=(sqrt(3)/4) r(1-3r^2)/sqrt(1+r^2)>=0`,

so this branch increases to `K_*(1/sqrt(3))=4/3`.

For `1/sqrt(3)<=r<=sqrt(3)`, differentiation of the middle Irwin--Hall branch gives

`K_*'(r)=N(r)/(8r^2 sqrt(1+r^2))`,

where

`N(r)=3sqrt(3)r^5-18r^4+11sqrt(3)r^3-9r^2+1
     =3sqrt(3)(r-1/sqrt(3)) Q(r)`

and

`Q(r)=r^4-(5sqrt(3)/3)r^3+2r^2-(sqrt(3)/3)r-1/3`.

Now

`Q''(r)=12(r-2sqrt(3)/3)(r-sqrt(3)/6)`.

On `[1/sqrt(3),sqrt(3)]`, Q' first decreases up to `2sqrt(3)/3` and then increases. Moreover

`Q'(1/sqrt(3))=-2sqrt(3)/9<0`,
`Q'(2sqrt(3)/3)=-7sqrt(3)/9<0`,
`Q'(sqrt(3))=2sqrt(3)/3>0`.

Thus Q has one interior critical point and it is a minimum. Consequently the maximum of Q on this interval is at an endpoint. But

`Q(1/sqrt(3))=-4/9`, `Q(sqrt(3))=-4/3`.

Therefore `Q(r)<0` throughout the interval, so `K_*'(r)<=0` there (strictly negative away from the left endpoint).

For `r>=sqrt(3)`,

`K_*(r)=sqrt(1+r^(-2))`,

which is strictly decreasing.

Hence the global maximum is exactly

`max_(r>0) K_*(r)=K_*(1/sqrt(3))=4/3`.

This proves the global scalar cap asserted in (2.4) of `REPORT.md`.
