# fleet02/B15 — exact Gaussian integral sharpens the physical-triple receiver

This note sharpens the late-source audit for `math-open-problems@9e2909942e0db085b66ce6bcefe663c879d89b44`. No hypothesis changes.

For an original-coordinate principal `3x3` block with `s_3(M)>=sigma`, the exterior estimate from the audited proof is

`P(q in I, |y|>=R) <= b h/(sigma R)`, `b=3sqrt(3)`.

For the interior Gaussian comparison, do not replace the exact one-dimensional Fourier integral by the crude bound `<=6`. One has

`I0 := int_R (1+u^2)^(-3/4) du`
`    = sqrt(pi) Gamma(1/4)/Gamma(3/4)`
`    = 5.244115108584238...`.

After the substitution `u=2sigma R^2 t`, Fourier inversion gives

`||p_(G^T M G)||_infinity <= I0/(4pi sigma R^2)`.

Since on `|y|<=R`,

`1 <= e^(1/2) exp(-|y|^2/(2R^2))`, 

the interior contribution is

`P(q in I, |y|<=R) <= a R h/sigma`,

where

`a = e^(1/2) sqrt(2pi) I0/2`
`  = e^(1/2) pi/sqrt(2) * Gamma(1/4)/Gamma(3/4)`
`  = 10.8362594669368...`.

Therefore for every `R>0`,

`P(q in I) <= (aR+b/R) h/sigma`.

Optimizing at `R=sqrt(b/a)` gives the fully explicit constant

`boxed(C_phys_exact = 2sqrt(ab))`

`= 2 [3pi e^(1/2) sqrt(3/2) Gamma(1/4)/Gamma(3/4)]^(1/2)`

`= 15.0075788696513... <15.008`.

Thus the later physical-core theorem can be stated as

`boxed(||p_(X^T A X)||_infinity < 15.008/sigma)`

whenever some original-coordinate principal `3x3` block has smallest singular value at least `sigma`, with arbitrary outside interactions and arbitrary affine terms. The same zero-loss conditioning/averaging argument gives the ambient result. The triangular functional satisfies

`E (eps-|Q-y|)_+ < 15.008 eps^2/sigma`.

The Gaussian variance choice used by the source is itself optimal inside this comparison family: if one uses variance `tau^2=c^2R^2`, the multiplicative dependence is `c exp(1/(2c^2))`, minimized at `c=1`. Hence the improvement above extracts the remaining elementary slack in that particular interior/exterior proof without altering its geometry.

This strengthens only the numerical constant. The structural caveat remains: `s_3(A)>=1` does not force a universally conditioned physical principal triple.
