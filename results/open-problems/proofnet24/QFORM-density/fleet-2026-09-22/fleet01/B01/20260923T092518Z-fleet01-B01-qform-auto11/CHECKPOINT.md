# fleet01/B01 early substantive checkpoint

Run: `20260923T092518Z-fleet01-B01-qform-auto11`.

## First calculation

Let `A=A^T` satisfy `s_3(A)>=1` and `max_i |A_ii|<=tau<1`, and put `D=diag(A)`, `E=A-D`. Then

`||D||op<=tau`, hence by singular-value Weyl,

` s_3(E) >= s_3(A)-||D||op >= 1-tau`.

Therefore the ordered off-diagonal energy

`F(A):=sum_(i!=j) A_ij^2 = ||E||F^2`

obeys

`F(A)>=s_1(E)^2+s_2(E)^2+s_3(E)^2>=3(1-tau)^2`.                 (C.1)

The completed fleet02/B01 weighted-Fourier theorem (`math-open-problems@ad18e7e072cdbb4b015e8363fe49a7e047533370`) states for every `0<beta<1/2`, every affine term, and arbitrary independent cap-one physical inputs,

`W_beta(Q):=integral_R |t|^(beta-1)|phi_Q(t)|dt`
` <=K_beta F(A)^(-beta/2)`,

`K_beta=2 exp(beta/2)(4 pi)^beta/[beta(1-2beta)]`.

Combining with (C.1) gives the strict-N3 frequency-averaged estimate

`W_beta(Q)<=K_beta [3(1-tau)^2]^(-beta/2)`.                      (C.2)

This is valid on the entire small-diagonal no-pivot class and does not assert scalar pointwise Fresnel decay.

## Distribution-function consequence

Let

`K_T(x)=T/(2pi) [sin(Tx/2)/(Tx/2)]^2`.

For `|x|<=1/T`,

`K_T(x)>=(T/(2pi))*4 sin(1/2)^2`.

Hence, with `T=1/h`,

`P(|Q-s|<=h)`
` <= [4 sin(1/2)^2]^(-1) W_beta(Q) h^beta`.                     (C.3)

Thus every strict-N3 state has a uniform Hölder concentration estimate of every order `beta<1/2`. Optimizing `beta=1/2-1/log(1/h)` for `h<=e^-4`, and using the owner no-pivot threshold `tau=1/500`, yields the explicit near-endpoint bound

`P(|Q-s|<=h) <= 53.831 sqrt(h) log(1/h)`.

The endpoint `beta=1/2` is not claimed; the partner's weighted integral has the genuine logarithmic divergence there.

Next: apply the newest fleet02/B01 r38 hyperbolic receiver theorem to a strict-N3 family whose natural three-volume law has a row marginal equal to one, so the current Theorem-D/D' marginal gate fails on the natural cut.