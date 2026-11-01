# Exact checks for fleet01/B02 20260924T052052Z

These checks support only the explicit inequalities in `REPORT.md`; they are not simulations of the conjecture.

## Spectral-window certificate

Parameters:

- `eta=1/18`
- `eps=1/76`
- `delta=1/2-eps-sqrt(2 eps)=37/76-1/sqrt(38)`
- `sigma=delta-eta=295/684-1/sqrt(38)`.

Rational enclosure of `1/sqrt(38)`:

`162222^2*38 - 10^12 = 7136792 >0`, hence `1/sqrt(38)<162222/10^6`.

First ridge term:

`(201329/10^6)^2 -(1/76)/(37/76-162222/10^6)
 =483350323731/3083891000000000000 >0`,

hence `sqrt((1/76)/delta)<201329/10^6`.

Rational enclosure of `sqrt(6)`:

`244949^2-6*100000^2=12601>0`, hence `sqrt(6)<244949/100000`.

Second ridge term:

`505763/10^6 -(244949/100000)*(1/18)/(37/76-162222/10^6-1/18)
 =9924497/23005019000000 >0`.

Total:

`201329/10^6+505763/10^6=707092/10^6`, and

`1/2-(707092/10^6)^2=1306471/62500000000>0`.

Therefore the parametric ridge condition is strictly below `1/2`.

Numerical values, only for readable constants:

- `delta = 0.32462068413239537...`
- `sigma = 0.26906512857683984...`
- exact ridge-expression square = `0.49997606817420487... <1/2`
- `9 sqrt(3e)/(2 sigma) = 47.759851325381916...`
- `9 pi sqrt(3e)/sigma = 300.08399612072117...`.

## Clean physical-hub scale

Failure of the leverage gate gives

`||Ae_i||_2^2>1/(18^2*76)=1/24624`.

If both diagonal and off-diagonal row norms were at most `1/222`, then

`||Ae_i||_2^2<=2/222^2=1/24642`.

Since `1/24642<1/24624`, at least one is strictly larger than `1/222`.

The exact unsimplified threshold is

`1/(18 sqrt(152)) = 0.004506150586965626... >1/222`.

## Live robust-rank-two constants

Use `kappa=247/576` and `delta0=1/444`.

Cross-tail E3 floor:

`kappa delta0^2 =247/113550336
 =2.1752467557647736e-6`.

Punctured same-bank physicalized floor:

`kappa delta0^2/64 =247/7267221504
 =3.398823055882459e-8`.

With `C3=10.345083232147514`, the completed fleet02/B02 theorem gives:

- first E3 branch: density coefficient `90.88298182061308...`, Fourier-L1 `571.0346160479455...`;
- second E3 branch: density coefficient `181.76596364122616...`, Fourier-L1 `1142.069232095891...`.

The report rounds these safely upward to `91.156`, `572.745`, `181.766`, `1142.070`; the first two report roundings are deliberately looser than necessary and remain valid.

Diagonal scalar-pivot payment at `|a|>1/222`:

`137 sqrt(222)=2041.2540263279336... <2041.255`.

Scalar-chirp integrated norm:

`(32 pi*222)^(1/3)=28.154702444531946... <28.155`.

Carrier-aligned scale:

`1/(222 sqrt(2))=0.003185165681020484...`.

## Source-scope checks

- The spectral projection and singular vectors are used only as coefficient algebra; no rotated random coordinate is asserted independent.
- The final Fourier receiver is applied only to literal ORIGINAL-coordinate cross blocks.
- No small nonzero coefficient or spectral tail is removed from the random phase.
- The scalar-pivot theorem is used only for essential boundedness; continuity is not imported from it.
