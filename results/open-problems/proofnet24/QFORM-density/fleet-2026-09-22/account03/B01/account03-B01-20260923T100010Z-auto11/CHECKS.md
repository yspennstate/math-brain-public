# Deterministic checks for account03/B01 source-disjoint-square Lp/log receiver

Run: `account03-B01-20260923T100010Z-auto11`.

These checks are diagnostics for constants and algebra. The proof is in `REPORT.md` and does not depend on numerical experimentation.

## Closed-form constants

For `p>2` define

`S_p=(4*pi)^(1/p)*((p-1)/(p-2))^((p-1)/p)`,

`B_p=4*pi*S_p*(p-1)^((p-1)/p)`,

`K_p=(p+1)/pi*(B_p/(2*p))^(p/(p+1))`.

Numerical values:

| p | S_p | B_p/(2p) | K_p |
|---:|---:|---:|---:|
| 3 | 3.690540297288056 | 12.269736305254638 | 8.347117760390864 |
| 4 | 2.551942650418384 | 9.137591279860183 | 9.342982047116381 |
| 5 | 2.088300353955790 | 7.955194807899133 | 10.753348651880529 |
| 6 | 1.836369149713272 | 7.352983810567320 | 12.320583074521442 |
| 10 | 1.432050247254422 | 6.500644005777104 | 19.199683525732550 |
| 20 | 1.194723852082137 | 6.155074697424212 | 37.732902246132824 |

At `p=3`, exact simplification gives

`K_3=4*(8/3)^(3/4)=8.347117760390866... <8.348`.

## Algebraic rearrangement used in the logarithmic bound

Direct substitution gives

`B_p/(2p)=2*pi*(4*pi/p)^(1/p)*(1+1/[p(p-2)])^((p-1)/p)`.

For `p>=4`,

* `(4*pi/p)^(1/p) <= pi^(1/4) <4/3`;
* `(1+1/[p(p-2)])^((p-1)/p) <= 1+1/8=9/8`.

Hence `B_p/(2p)<3*pi`, so `K_p<3(p+1)`.

The `p=4` value satisfies `K_4<10`. Therefore, with `L=log_+(sqrt(Delta)/rho)`:

* if `L<=4`, choosing `p=4` gives `R^(1/5)<=exp(L/5)<=1+L` and the density cap `<10 Delta^(-1/2)(1+L)`;
* if `L>4`, choosing `p=L` gives `R^(1/(L+1))<e<3` and `K_L<3(L+1)`, hence the cap `<9 Delta^(-1/2)(1+L)`.

Thus the uniform logarithmic corollary with constant `10` is valid.

## Scaling check

Under multiplication of the full quadratic form by `c`,

`Delta -> c^2 Delta`, `rho -> |c| rho`.

The general `p` bound scales by

`|c|^(-p/(p+1))*|c|^(-1/(p+1))=|c|^(-1)`,

as a one-dimensional density bound must.

The logarithmic ratio `sqrt(Delta)/rho` is invariant under this scaling.

## Target-control spectrum

For

`Q_0=2 X_1 Y_1+2 X_2 Y_2+Z^2`,

the active symmetric coefficient matrix is the direct sum of two blocks `[[0,1],[1,0]]` and `[1]`. Its nonzero spectrum is exactly

`{1,-1,1,-1,1}`.

Therefore the control lies inside the owner's full `>=3` large-eigenvalue hypothesis, and the new `p=3` bound gives `<8.348` for every cap-one product input law.

STATUS=PASS
