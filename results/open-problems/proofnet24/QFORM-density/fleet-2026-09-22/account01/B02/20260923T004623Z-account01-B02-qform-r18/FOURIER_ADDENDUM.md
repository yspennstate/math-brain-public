# Integrated-Fourier addendum

The partner D5 inequality used in `REPORT.md` comes from its explicit integrable characteristic-function envelope. With `k=5,q=2`, the coarse account02/B02 r16 estimate is

`||p_Q||_infinity <= (5e/sqrt(2)) Z5^(-1/10)`.

The corresponding direct Fourier estimate is

`integral_R |phi_Q(t)| dt <= 2pi (5e/sqrt(2)) Z5^(-1/10)
                              =5sqrt(2) pi e Z5^(-1/10).`

Under the clustered-pair hypotheses of the main report,

`Z5 >= (3/250) Z3 L^2`,

therefore

`boxed(
 integral_R |phi_Q(t)| dt
 <=5sqrt(2) pi e (250/3)^(1/10) Z3^(-1/10)L^(-1/5)
 <93.975 Z3^(-1/10)L^(-1/5).
)`

Thus this run does obtain a genuine unweighted `L^1_t` characteristic-function bound on the paid clustered-pair branch, not merely an `L^2_t` or fractional-weight estimate. Fourier inversion gives the continuous-density conclusion in `REPORT.md`.

This does not supply a target-wide constant because `Z3` and the projected transverse energy `L` have not yet been forced at universal scale from the bare three-large-eigenvalue hypothesis.
