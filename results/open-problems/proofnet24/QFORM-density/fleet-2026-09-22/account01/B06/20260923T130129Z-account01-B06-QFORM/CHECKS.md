# Exact checks for account01/B06 r33

These checks are algebraic sanity checks only; they are not independent proof review.

## 1. General-hyperbola constants

For `lambda0=2-sqrt(3)` and `m0=(2+sqrt(3))/4`:

`(1+lambda0)/(1-lambda0)=sqrt(3)`

and

`1/[2(1-lambda0)sqrt(m0)]=1/sqrt(2)`.

Thus the near-coordinate logarithmic envelope in `REPORT.md` has exactly the stated constant.

## 2. Physical-triple determinant forcing

For the addendum threshold

`theta=1/2`, `r=9/16`,

the determinant-expansion majorant is exactly

`theta^3+2r^3+3 theta r^2 =1957/2048 <1`.

Hence, if all three diagonal entries have modulus `<mu/2`, at least one off-diagonal entry has modulus `>9mu/16`.

For that pair,

`r^2-theta^2 =81/256-64/256 =17/256`,

so its determinant magnitude is `>17mu^2/256` and it is indefinite.

## 3. Constants

Large-diagonal branch:

`16*2^(1/4)*sqrt(30)=104.21688998922089...`.

Small-diagonal branch:

`2^(11/4)*sqrt(3)*(256/17)^(1/8)=16.3537365013566...`.

Thus the large-diagonal constant dominates and `C_3=16*2^(1/4)*sqrt(30)` is valid.

## 4. Scaling

Under `M -> sM`, `|det M|^(-1/3) -> s^(-1)|det M|^(-1/3)`, exactly matching density scaling for `Q -> sQ`.  The determinant-only triple bound is therefore scale-correct.

`QFORM_B06_R33_CHECK_PASS`
