# account01/B03 r38 deterministic checks

Run: `20260924T021318Z-account01-B03-QFORM-r38`.

These are exact algebra/calculus/arithmetic checks for `REPORT.md`; they are not a numerical proof and use no Monte Carlo evidence.

## 1. Product-density decomposition

For one compatible sign quadrant,

`I(r)=int_0^infinity F(u)G(r/u)du/u`, `0<=F,G<=1`, `int F,int G<=1`.

For `0<r<1`:

- `(0,r)`: `v=r/u` gives `<=int_1^infinity G(v)dv/v<=1`;
- `[r,1]`: `<=int_r^1 du/u=log(1/r)`;
- `(1,infinity)`: `<=int_1^infinity F(u)du<=1`.

Thus `I(r)<=2+log(1/r)`, and two compatible quadrants give `4+2log(1/r)`.

For `r>=1`, the `(0,1)` piece after substitution is at most `1/r<=1`, while the `(1,infinity)` piece is at most one. Thus two quadrants give at most four.

The independent split at `|u|=sqrt(r)` gives `p_UV(w)<=2r^(-1/2)`.

## 2. Layer-cake integrals

Put `L=2m`, `A=H sqrt(L)`.

`int_0^infinity min(1,A e^(-u/2))du`

equals `2A` for `A<=1`, and `2+2log A` for `A>=1`.

Also

`(1/2)int_L^infinity min(1,H sqrt(r))r^(-3/2)dr`

equals at most `H[1+log(1/A)]` for `A<=1`, and `L^(-1/2)` for `A>=1`.

Substitution into the scaled product envelope therefore gives

`B(A,m)=(A/m)[5+log(1/A)]` for `A<=1`,

`B(A,m)=m^(-1)[5+2log A]` for `A>=1`.

Both formulas agree at `A=1`, with value `5/m`.

## 3. Scale cancellation

The residual one-volume theorem gives

`H<=sqrt(2)H1 m J2^(-1/4)`,

hence

`A<=x=2H1 m^(3/2)J2^(-1/4)`.

Solving the equality for `m` gives

`m=x^(2/3)J2^(1/6)(2H1)^(-2/3)`.

Therefore the dimensionless scalar factors are

`f_-(x)=x^(1/3)[5+log(1/x)]`, `0<x<=1`,

`f_+(x)=x^(-2/3)[5+2log x]`, `x>=1`.

Their derivatives have signs

`sign f_-'(x)=sign(2-log x)>0` on `(0,1]`,

`sign f_+'(x)=sign(-4(1+log x))<0` on `[1,infinity)`.

Thus both are maximized at `x=1`, with common maximum five.

## 4. Schur / random-cut identity

For `A[S,S]=[[0,mu],[mu,0]]`,

`det A[S,S]=-mu^2`.

For the Schur complement `S_A` on `K=S^c`, block determinant gives

`det A[S union {i},S union {j}]=-mu^2(S_A)_(ij)`.

Hence

`J2(S)=mu^4 sum_(i!=j)(S_A)_(ij)^2`.

Under an independent fair cut `K=L disjoint_union R`, each ordered pair `i!=j` lands in `L x R` with probability `1/4`, so

`E ||(S_A)_[L,R]||_F^2=J2(S)/(4mu^4)`.

No diagonal entry is included in this crossing norm.

## 5. Constants

With

`H1=sqrt(2e)Gamma(1/4)=8.453631522124516...`,

`5(2H1)^(2/3)=32.93711407877257...`.

At the live threshold `J2=1/144`,

`32.93711407877257 * 144^(1/6)=75.40716718914965...`.

The posterior dependence-safe weighted collision estimate is

`4+2pi*75.40716718914965=477.79720493889965...`.

## 6. Partner identity consequence

The designated account02/B03 rank-two identity writes `J_sep` as a sum of four nonnegative squared quantities. If `J_sep>=1/2304`, then at least one term is at least `1/(4*2304)=1/9216`; hence at least one corresponding square-root quantity is at least `1/96`. This is the inequality recorded in Section 7 of `REPORT.md`.
