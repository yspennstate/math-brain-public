# fleet03/B14 r26 early substantive checkpoint

SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B14, 2026-09-23T04:37:07Z.

attacking: aligned quadratic bank curvature under collective compression, preserving arbitrary shifts, unbounded fragmented supports and outside affine terms.

## First paid calculation

Split original independent coordinates as `X=(U,V,Z)`, with `U in R^3`, `V in R^m`. Assume

`A = [[B,        k a^T,      C],
      [a k^T,    theta a a^T, a b^T],
      [C^T,      b a^T,      D]]`,

where `||k||_2=1`, `Bk=0`, `a!=0`, and `B` has at least one nonzero eigenvalue. After conditioning on the original outside bank `Z=z`, all dependence on `V` is through the single scalar `W=a^T V`:

`Q_z = U^T B U + 2(k^T U)W + theta W^2 + affine_z(U,W)+const_z`.

The sharp one-dimensional product-projection bound gives

`||p_W||_infinity <= sqrt(2)/||a||_2`.

Set `r=||a||_2/sqrt(2)` and `Y=W/r`; then `Y` is cap-one and independent of the three original coordinates in `U`. The active four-variable quadratic matrix is

`H = [[B, r k],[r k^T, theta r^2]]`.

In a deterministic coefficient-space basis with `k` the third vector, the spectrum of `H` is the two nonzero eigenvalues of `B|k^perp` together with the two eigenvalues of

`T=[[0,r],[r,theta r^2]]`.

Since `det T=-r^2`, one eigenvalue of `T` always has absolute value at least `r`, independently of `theta`. Therefore if the two nonzero eigenvalues of `B` both have absolute value at least `nu`, then

`s_3(H) >= min(nu,r)`

for every real `theta`.

Applying the completed fleet04/B14 four-coordinate affine-core theorem (`math-open-problems@6442bbe9d4647a730b27b8e0786bc54b2546b7ec`) now gives the candidate exact branch estimate

`||p_Q||_infinity <= 1000(8+log 4) / min(nu, ||a||_2/sqrt(2))`,

uniformly in `theta`, all outside blocks/couplings, all translations, and arbitrary unbounded/fragmented cap-one laws. The remaining work in this run is to write the full proof, record the one-large-eigenvalue quantitative variant using the exact smaller eigenvalue of `T`, and stress-test the branch on a valid diffuse-bank target family.

Full QFORM remains OPEN; this checkpoint proves only the displayed structural branch once the cited partner theorem is applied at its stated scope.
