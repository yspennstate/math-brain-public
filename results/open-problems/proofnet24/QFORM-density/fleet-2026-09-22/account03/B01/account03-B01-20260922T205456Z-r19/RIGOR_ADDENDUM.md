# Rigor addendum: Fourier representation of the fractional potential

This addendum makes the passage used in REPORT.md, Theorem 2.1, fully distributionally precise.

Let `0<alpha<1`, let `mu` be the law of `R`, and suppose

`integral_R |t|^(alpha-1) |hat mu(t)| dt < infinity`.                 (A.1)

The locally integrable Riesz kernel `K_alpha(x)=|x|^(-alpha)` is a tempered distribution and, in the Fourier convention `hat f(t)=integral e^(itx)f(x)dx`, has

`hat K_alpha(t)=2 Gamma(1-alpha) sin(pi alpha/2) |t|^(alpha-1)`.       (A.2)

Hence the distributional convolution `K_alpha*mu` has Fourier transform equal to the product of (A.2) with `hat mu`. By (A.1) that product lies in `L^1`, so Fourier inversion gives a bounded continuous representative `F` and

`||F||_infinity
 <= [Gamma(alpha) cos(pi alpha/2)]^(-1)
    integral_0^infinity t^(alpha-1)|hat mu(t)|dt`.                   (A.3)

The constant follows from the reflection identity

`Gamma(alpha)Gamma(1-alpha)=pi/sin(pi alpha)`.

On the other hand the ordinary extended-valued potential

`P(s)=integral |x-s|^(-alpha) dmu(x)`                                (A.4)

is locally integrable in `s` by Tonelli on bounded intervals, and represents the same convolution distribution. Therefore `P=F` almost everywhere. Moreover `P` is lower semicontinuous: `s -> |x-s|^(-alpha)` is nonnegative lower semicontinuous and Fatou gives lower semicontinuity after integration. If `P(s0)>||F||_infinity`, lower semicontinuity would make `{s:P(s)>||F||_infinity}` a nonempty open set of positive Lebesgue measure, contradicting `P=F` almost everywhere. Consequently

`sup_s P(s) <= ||F||_infinity`,                                      (A.5)

and combining (A.3)-(A.5) proves exactly the pointwise-in-`s` half-Riesz inequality claimed in REPORT.md, including possible exceptional points. No atomlessness assumption is needed.

For the determinant envelope in REPORT.md,

`|hat mu(t)| <= (1+q t^(2k))^(-1/8)`,

(A.1) is satisfied exactly when `0<alpha<k/4`, because the integrand is `O(t^(alpha-1))` at zero and `O(t^(alpha-1-k/4))` at infinity. Thus the `k=3, alpha=1/2` specialization is fully justified.
