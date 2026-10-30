# fleet02/B03 r56 deterministic checks

These checks verify algebra and constants in `REPORT.md`; they are not numerical evidence for the theorem.

## 1. Main constant

With `C0=(3/2)sqrt(6pi)`, the `L1` tail coefficient is

`D=pi*6^(3/4)*C0^(1/2)*(MN)^(1/2)|a|^(-1/4)|detB|^(-1/2)`.

For `2T+D T^(-1/4)`, stationarity gives `T^(5/4)=D/8` and minimum `10(D/8)^(4/5)`. Dividing by `2pi` simplifies exactly to

`(15/4)3^(1/5)(MN)^(2/5)|a|^(-1/5)|detB|^(-2/5)`.

## 2. Weighted-time constant

The tail in `A_-` is

`[pi^2 C0/sqrt(2)] MN |a|^(-1/2)|detB|^(-1) T^(-2)`.

Optimising `4sqrt(T)+E T^(-2)` gives `T^(5/2)=E` and value `5E^(1/5)`, namely

`5*2^(-1/5)*3^(3/10)*sqrt(pi) (MN)^(1/5)|a|^(-1/10)|detB|^(-1/5)`.

After division by `sqrt(2pi)` in the Riesz identity the whole-copy constant is

`(5/2)6^(3/10)`.

## 3. Strict five-variable target

For `Q_5=X1^2+4X2X4+4X3X5`, reorder coordinates as `(X1,X2,X4,X3,X5)`. The matrix is

`[1] direct_sum [[0,2],[2,0]] direct_sum [[0,2],[2,0]]`,

so its spectrum is exactly `{1,2,-2,2,-2}`. Here `J=16`.

Numerical constants:

- density bound: `(15/4)3^(1/5)16^(-1/5)=2.683067027072354...`;
- direct weighted time: `5*2^(-1/5)*3^(3/10)*sqrt(pi)*16^(-1/10)=8.129490346791867...`;
- whole-copy half-Riesz: `(5/2)6^(3/10)*16^(-1/10)=3.243197417450581...`.

## 4. Pinned Theorem-H family

For the diffuse family, augmented rows are two copies each of

`(1/sqrt(2),0,0)`, `(0,sqrt(2),0)`, `(0,0,sqrt(2))`.

Thus `G=diag(1,4,4)`, `det G=16`, and every leverage is `1/2`. Substitution into pinned Theorem H gives

`|phi(t)| <= min(1, C|t|^(-5/2))`, `C=2pi^(5/2)`.

The crossover is `t0=C^(2/5)=2^(2/5)pi`. Therefore

`(2pi)^(-1) int |phi| <= (5/3)2^(2/5)=2.199179851288157...`,

and

`int |t|^(-1/2)|phi|^2 <= (40/9)2^(1/5)sqrt(pi)=9.04895476819256...`.

`QFORM_B03_R56_CHECK_PASS`
