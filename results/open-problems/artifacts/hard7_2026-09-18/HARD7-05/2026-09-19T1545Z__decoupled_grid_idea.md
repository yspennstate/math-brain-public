Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.**

# HARD7-05 idea before checker — decouple Slepian grid spacing from AR correlation

Status: exploratory mathematical route written **before** exact certification. Canonical target remains `MOLCHAN-2025-THETA2H`; no closure claim.

The previous checkpoint fixed the comparison by the stronger requirement

\[
R_X(k\Delta)\le r^k,\qquad e^{-\Delta/4}=r,
\]

so the grid parameter and the AR(1) comparator correlation were forced to be the same number. That equality is not required by Slepian. The actual comparison only needs some `rho` with

\[
R_X(k\Delta)\le \rho^k\quad(k\ge1).
\]

This run therefore uses a different method triple from the preceding B3/B11/B24 run:

- **B5 (add a parameter):** separate `q=e^{-Delta/4}` from the comparator correlation `rho`.
- **B20 (find why the algorithm fails):** diagnose the old boundary `q<=r0` as the point where the *artificial restriction* `rho=q` fails, not where Slepian itself fails.
- **B27 (swap/split the quantifiers):** satisfy the lag-one covariance constraint separately, then use the already proved small-`q` envelope for every lag `k>=2` at once.

## Counterexample-first test

For the exact Lamperti covariance already derived in this track,

\[
R(q)-q=\frac{1-q^2}{6q^5}\left[-P(q^2)+2(1+q^2)(1-q^4)^{3/2}\right],
\]

with `P(z)=2+2z-3z^2-2z^3-2z^4`. The inherited exact envelope says `R(u)<=u` for every `0<u<=r0`, where

\[
r_0=\frac{287831}{500000}=0.575662.
\]

I first tried to break the decoupled route by checking whether a higher lag forces a larger AR correlation than lag one. Take

\[
q=\frac{661}{1000}=0.661,
\qquad
\Delta=4\log(1/q).
\]

Then

\[
q^2=0.436921<r_0.
\]

Hence for every `k>=2`, `q^k<=r0` and the inherited envelope gives

\[
R(q^k)\le q^k.
\]

Therefore any `rho>q` automatically handles **all higher lags**; only `k=1` remains. Direct exploratory evaluation gives

\[
R(q)\approx0.6833861128,
\]

so the rational choice

\[
\rho=\frac{683387}{10^6}=0.683387
\]

has visible slack. The exact checker should prove `R(q)<rho` by squaring a positive radical inequality, not by floating point.

Thus

\[
R_X(k\Delta)\le \rho^k\qquad(k\ge1)
\]

would follow from one new exact one-step inequality plus the prior envelope. This is a genuinely larger grid (`q>r0`) and is not a refinement of the old boundary digit.

## Why this can move the source metric substantially

Exploratory degree-5 Galerkin/Kato calculations for the killed AR(1) operator at `rho=0.683387` give principal eigenvalue near

\[
\lambda_1\approx0.78443627.
\]

The resulting persistence rate is approximately

\[
\frac{-\log\lambda_1}{4(-\log q)}\approx0.14661215,
\]

well above the current certified `0.14344477`. A safe exact target is therefore

\[
\theta_{2,1/4}\ge0.146611.
\]

For spectral separation, a new simplification avoids the inherited sixth-trace machinery. Since `K` is positive self-adjoint and Hilbert-Schmidt,

\[
\lambda_2^2\le \operatorname{tr}K^2-\lambda_1^2\le \operatorname{tr}K^2-\mu^2,
\]

where `mu` is any Rayleigh quotient. Here `tr K^2` has a closed bivariate-orthant formula, so a degree-5 quasimode plus Kato–Temple should already certify a rational upper cap on `lambda_1`.

No theorem is asserted in this note. Next step: build one exact rational checker for (i) `R(q)<rho`, (ii) the degree-5 Kato–Temple enclosure using the exact `tr K^2`, and (iii) the logarithmic conversion to `0.146611`.