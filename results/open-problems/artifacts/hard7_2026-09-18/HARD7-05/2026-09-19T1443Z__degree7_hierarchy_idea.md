# HARD7-05 route extension — push the exact polynomial hierarchy until the residual collapses

This extension is written before the generalized checker.

The degree-three route note at commit `21bbd14ab3cc8e757c27eb12d9a926d8704ab581` exposed a stronger structural fact: the conditional truncated moments satisfy a two-step recurrence, so there is no algebraic barrier at degree three.  For `X|Y=y ~ N(ry,s^2)`, if

`J_n(y)=E[X^n 1_{X>0}|Y=y]`, then for every `n>=2`

\[
J_n(y)=ry\,J_{n-1}(y)+(n-1)s^2J_{n-2}(y),
\]

with `J_0=q` and `J_1=ry q+s p`.  Therefore every `J_n` is `q` times a polynomial plus `p` times a polynomial, and all Gram, Ritz and squared-residual entries close through the same scalar moment recurrences.

I used this to stress-test degrees 3,4,5,6,7 numerically *before* deciding what to certify.  The exploratory normalized residuals were approximately

| polynomial degree | residual squared |
|---:|---:|
| 3 | `1.39e-6` |
| 4 | `3.63e-8` |
| 5 | `3.44e-9` |
| 6 | `1.15e-9` |
| 7 | `3.77e-11` |

The non-monotone rate of improvement is itself useful: merely increasing degree is not automatically enough, but degree seven crosses a qualitatively different residual scale.  The rational degree-seven trial vector selected for exact certification is

\[
(100000000,66277120,7826678,-3196811,-506238,417141,-75196,4570)^T.
\]

Exploratory values are

\[
\mu\approx0.7284322337020115,\qquad
\varepsilon^2\approx3.77\times10^{-11}.
\]

The exact checker will generate all `J_n` recursively, not hard-code a large moment table.  It will certify only identities and inequalities derived from rational interval enclosures of `pi`, square roots, inverse tangents and logarithms.  The inherited `tr(K^6)` certificate remains the only spectral-tail input.

The intended conservative target is

\[
\lambda_1<0.72843224,
\qquad
\theta_{2,1/4}\ge 0.14344477,
\]

which would move the frozen bracket width to `0.10655523`.  The route is abandoned if any exact interval assertion fails.
