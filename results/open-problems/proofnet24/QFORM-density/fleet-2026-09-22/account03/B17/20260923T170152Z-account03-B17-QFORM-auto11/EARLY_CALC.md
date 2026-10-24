SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B17, 2026-09-23T17:01:52Z.
attacking: the exact zero-physical-pivot one-heavy/two-diffuse endpoint; seek a global (all output levels) density ceiling strictly below the 3 sqrt(2) witness obstruction.

Early substantive calculation.

Let v=1/12, X have an arbitrary probability density f with 0<=f<=1, and let B,C be independent N(0,v), independent of X. For

    Q0 = 2 X B + C^2,

the characteristic function factors conditionally on X:

    phi(t) = (1-2 i v t)^(-1/2) * integral f(x) exp(-2 v t^2 x^2) dx.

Hence, by the one-dimensional bathtub principle applied to the even decreasing reward exp(-2 v t^2 x^2),

    |phi(t)| <= (1+4v^2 t^2)^(-1/4)
                 * integral_{-1/2}^{1/2} exp(-2 v t^2 x^2) dx.

This majorant is integrable. With u=t/6 and k=sqrt(3/2), Fourier inversion gives

    ||p_Q0||_infty <= sqrt(6/pi) I,
    I = integral_0^infty erf(k u) / [u (1+u^2)^(1/4)] du.

The target comparison is I < sqrt(3 pi), which would imply ||p_Q0||_infty < 3 sqrt(2).

A fully rational certificate is available by splitting at u=1. On [0,1], use the alternating erf series through n=4 and convexity of z -> (1+z)^(-1/4), giving

    I_[0,1] <= 2 sqrt(3/(2pi)) (1580209/2587200 + (38243/147840) 2^(-1/4)).

On [1,infinity], use erf<=1 and the exact antiderivative

    integral_1^infty du/[u(1+u^2)^(1/4)]
      = atanh(2^(-1/4)) + atan(2^(-1/4)).

The next step is to certify the resulting exact upper bound below sqrt(3 pi) using only rational enclosures (333/106 < pi < 355/113, 2^(-1/4)<841/1000, and short alternating/geometric series bounds), then publish the complete proof and checker.

Status: early calculation only; full QFORM remains open.
