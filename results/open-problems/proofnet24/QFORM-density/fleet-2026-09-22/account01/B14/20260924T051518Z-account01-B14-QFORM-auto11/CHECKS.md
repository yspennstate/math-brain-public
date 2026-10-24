# Deterministic checks — account01/B14 `20260924T051518Z-account01-B14-QFORM-auto11`

These are finite algebra/numerical checks for the formulas in `REPORT.md`; they are not substitutes for the analytic proof.

## 1. Exact crossover integral

For `m,D>0`, set `t0=(D/m)^(4/5)`. Then

`2[m t0 + D int_(t0)^infinity t^(-5/4)dt]`

`=2[m(D/m)^(4/5)+4D(D/m)^(-1/5)]`

`=10 D^(4/5)m^(1/5)`.

With `D=pi sqrt(A) H2`, division by `2pi` gives

`5 pi^(-1/5) A^(2/5) H2^(4/5)m^(1/5)`.

If `H2^2<=mL`, this becomes

`5 pi^(-1/5) A^(2/5)m^(3/5)L^(2/5)`, exactly the account02/B14 partner exponent.

## 2. The explicit slope density

For `R>=2`,

`f_R=1_[0,1/R] + R^(-1)1_[2,R+1]`.

The intervals are disjoint. Their masses are

`1/R` and `(R-1)/R`,

so total mass is one and `||f_R||inf=1`.

The exact square norm is

`||f_R||2^2 = 1/R + (R-1)/R^2 = (2R-1)/R^2`.

## 3. Exact target block

For original coordinates `(X,L,Y)`,

`B=[[0,1,0],[1,0,0],[0,0,1]]`.

Its characteristic polynomial is

`det(lambda I-B)=(lambda-1)^2(lambda+1)`,

hence `spec(B)={1,1,-1}`. Any ambient symmetric extension containing this principal block therefore has at least two eigenvalues `>=1` and at least one `<=-1` by Cauchy interlacing.

## 4. Constants

`C_*=5*pi^(-1/5)*4^(2/5)=6.924111078456212...`.

For `C_R=C_*[(2R-1)/R^2]^(2/5)`:

| R | `(2R-1)/R^2` | `C_R` |
|---:|---:|---:|
| 2 | 0.75 | 6.171468713842839 |
| 10 | 0.19 | 3.563407311091524 |
| 100 | 0.0199 | 1.445124476573149 |
| 1000 | 0.001999 | 0.576353777561135 |

As `R->infinity`, `(2R-1)/R^2 ~ 2/R`, so

`C_R ~ C_* 2^(2/5) R^(-2/5)`.

## 5. Convolution contraction used in the target family

If `nu` is any probability measure and `f in L2`, then Minkowski/Young gives

`||f*nu||2 <= ||f||2 ||nu||TV = ||f||2`.

Likewise `||f*nu||inf<=||f||inf`. Therefore the arbitrary product-bank projection `b^T W`, regardless of its support or moments, cannot increase either the `L2` collision payment or the partner's aggregate `L-infinity` slope cap when added independently to `Z_R`.
