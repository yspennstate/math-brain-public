# Further strengthening — the character-split sector theorem already closes at center C = 6

The previous strengthening obtained the sufficient threshold `6.052156...`. A two-range estimate removes the remaining slack and gives the clean bound `C>=6`.

For `0<d<=1/2`, write the exact certificate from the main report as

\[
\frac{F_C(d)}d=C-T(d),
\]

where

\[
T(d)=2(1-d)+\frac{4(1-d)}{1+(1-2d)^2}
-d\log_2d-\frac{(1-d)^2}{d}\log_2(1-d).
\tag{1}
\]

As in `STRENGTHENING_LOG_COMBINATION.md`,

\[
-d\log_2d-\frac{(1-d)^2}{d}\log_2(1-d)
\le\frac{1-d-d\ln d}{\ln2}
\le\frac{1+e^{-2}}{\ln2}<1.638.
\tag{2}
\]

Now split at `d=1/5`.

For `0<d<=1/5`, the rational term

\[
R(d)=\frac{4(1-d)}{1+(1-2d)^2}
\]

is increasing on this interval (its unique maximum on `(0,1/2)` occurs at `d=1-1/sqrt(2)>1/5`). Hence

\[
R(d)\le R(1/5)=\frac{40}{17}.
\]

Together with `2(1-d)<=2` and (2),

\[
T(d)<2+\frac{40}{17}+1.638
=5.990941176\ldots<6.
\tag{3}
\]

For `1/5<=d<=1/2`, use

\[
2(1-d)\le\frac85,
\qquad
R(d)\le1+\sqrt2<2.415,
\]

and again (2). Then

\[
T(d)<1.6+2.415+1.638=5.653<6.
\tag{4}
\]

Therefore

\[
\boxed{F_C(d)\ge d(C-6)\qquad(0<d\le1/2).}
\tag{5}
\]

For `d>=1/2`, the main report already gives

\[
F_C(d)\ge C/2-2,
\]

which is nonnegative for every `C>=4`.

Hence the final clean version of Theorem B15-SECTOR-KL-01 is:

> For any symmetric potential with center `Gamma(1/2)=C>=6`, every unbiased Shannon split whose two Boolean cofactors are balanced and one cofactor is a character has nonnegative exact local defect increment. For `d<=1/2` the increment is at least `d(C-6)`; for `d>=1/2` it is at least `C/2-2`.

In particular the live center `C^dagger=6.521851214` has certified small-disagreement margin at least

\[
(C^\dagger-6)d=0.521851214\,d.
\]

The estimate is analytic and all-dimensional. The decimal inequalities in (2)-(4) are evaluations of fixed elementary constants only; they are not finite-dimensional tests.
