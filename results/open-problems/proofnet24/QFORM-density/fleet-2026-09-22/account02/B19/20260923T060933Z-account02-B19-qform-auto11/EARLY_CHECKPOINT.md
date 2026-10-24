# Early checkpoint — sharpened near-null transverse-square interpolation

Programme: `QFORM-DENSITY-3EIG-20260922`. Full target remains OPEN.

In the designated-partner rank-two-cross theorem, after completing the transverse square one gets the sheared scalar linear form

`y' = y + lambda^{-1} d^T z`,  `delta=||d||`,

whose projection row has norm

`L = sqrt(1 + delta^2/lambda^2)`.

The existing proof only used the coarse one-dimensional density cap `K1<=sqrt(2)`. The product-marginal theorem actually gives

`K1 <= sqrt(2)/L = sqrt(2)|lambda|/sqrt(lambda^2+delta^2)`.

Keeping this scale in the partner's Hilbert-valued square transform and optimizing the split of

`I = int_0^infinity y^(-1/2) G(y)^(3/4) dy`

at `R=(2K1)^(-1)` yields `I<=3(2K1)^(1/4)`. Consequently the same bilinear-Plancherel argument gives the provisional bound

`||p_Q||_infinity <= (8/3) 6^(3/4) [|lambda| sqrt(lambda^2+delta^2)]^(-1/8) (s1 s2)^(-3/8)`

for `lambda!=0`, i.e. constant `10.2231...`. For `|lambda|<<delta` this improves the partner's `|lambda|^(-1/4)` divergence to `|lambda|^(-1/8) delta^(-1/8)` without treating the coefficient as a small random perturbation.

The next step is to write the full proof and the general `L^q`, `2<q<4`, interpolation family, which can reduce the punctured near-null divergence to arbitrarily small powers (with constants depending on q). The exact `lambda=0, delta>0` endpoint remains paid by the preceding B19 run.
