# fleet01/B03 r43 deterministic checks

Run: `20260924T105037Z-fleet01-B03-QFORM-r43`.

## Plancherel normalization

For

`B_t(z)=int exp(it u^T C u) exp(i 2t u.z) g(u) du`

with Fourier convention `hat h(xi)=int exp(i xi.u)h(u)du`, Plancherel is

`int |hat h(xi)|^2 dxi=(2pi)^k int |h(u)|^2 du`.

Changing `xi=2t z` gives

`int |B_t(z)|^2 dz=(2|t|)^(-k)(2pi)^k int |g|^2=pi^k |t|^-k int |g|^2`.

For `g=prod_j f_j` with probability densities `0<=f_j<=1`,

`int |g|^2=prod_j int f_j^2<=1`.

## L1 characteristic-function integral

Write `D=k+1>2`, `a=LNK/|beta|`, and

`C0=pi^(D/2)a^(1/2)`.

From `|phi(t)|<=min(1,C0 |t|^(-D/2))`, the crossover is

`T=C0^(2/D)=pi a^(1/D)`.

Then

`int_R |phi| <=2[T+C0*T^(1-D/2)/(D/2-1)]`

`=2T[1+2/(D-2)]`

`=2pi D/(D-2) a^(1/D)`.

Dividing by `2pi` gives

`||p||_inf<=D/(D-2)a^(1/D)`.

At `D=3`, this is `3 a^(1/3)`.

## Weighted whole-copy time integral

From

`|phi(t)|^2<=min(1,G |t|^-D)`, `G=pi^D a`,

the crossover is `T2=G^(1/D)=pi a^(1/D)`. Hence

`A_-=2 int_0^T2 t^-1/2 dt +2G int_T2^infinity t^(-D-1/2)dt`

`=4 sqrt(T2)+2G*T2^(1/2-D)/(D-1/2)`

`=4 sqrt(T2)+4 sqrt(T2)/(2D-1)`

`=[8D/(2D-1)]sqrt(pi)a^(1/(2D))`.

At `D=3`, `a=1`,

`A_-=(24/5)sqrt(pi)=8.507778484346476...`.

Using the programme normalization `A_-=sqrt(2pi)E|Q-Q'|^-1/2`, this becomes

`E|Q-Q'|^-1/2 <=12sqrt(2)/5=3.394112549695428...`.

## Strict target spectrum

For the exact example

`Q=2RV+2RY2+2VY1+2U1Y1+2U2Y2`,

the coefficient matrix in the order `(U1,Y1,V,R,Y2,U2)` is the adjacency matrix of the path graph `P6`. Its eigenvalues are

`lambda_j=2 cos(j pi/7)`, `j=1,...,6`.

Numerically their positive magnitudes are

`2cos(pi/7)=1.8019377358048383`,

`2cos(2pi/7)=1.2469796037174672`,

`2cos(3pi/7)=0.4450418679126289`.

Therefore exactly four eigenvalues have modulus greater than one, verifying that the example is inside the exact owner target.

## Dependency check

The designated partner input is fleet02/B03 r54,

`math-open-problems@434585cef13aebbe1d21612b43f46c760fb5344a`,

which proves the pair estimate

`|A_y(t)|^2<=pi L N/(|beta||t|)`

uniformly in the phase-twist coefficients. In this run it is applied before the independent k-hub Plancherel factor. No conditional density of the shared environment is introduced.

Marker: `QFORM_B03_TWISTED_PAIR_SLOPE_HUB_CHECK_PASS`.
