# L03: the sharp logarithmic angular-spectrum boundary

Fix beta, K, Lambda>0. Define a real centered Gaussian field g anchored at zero with stationary increments and spectrum 1_{0<|k|<Lambda}/(beta K |k|^2). This means

E[g(x)g(y)] = integral_{|k|<Lambda} [(exp(i k.x)-1)(exp(-i k.y)-1)]/(beta K |k|^2) d^2k/(2pi)^2.

The imaginary part integrates to zero. The quadratic form is positive because it is a Gram integral, and finite because each increment factor vanishes linearly at zero. This constructs g, with g(0)=0. A stationary real field with this spectrum and finite pointwise variance does NOT exist; only the stated anchored field and its increments are used.

For m != 0 and r=|x|,

Var[g(x)-g(0)] = 1/(pi beta K) F(Lambda r),

F(z) = integral_0^z (1-J_0(t)) dt/t,

E exp[i m(g(x)-g(0))] = exp[-m^2 F(Lambda r)/(2pi beta K)].

As z tends to infinity, F(z)=log z+b+o(1), where

b = integral_0^1 (1-J_0(t))dt/t - integral_1^infinity J_0(t)dt/t

is finite. Hence C_m(r) = B r^[-m^2/(2pi beta K)] (1+o(1)), for B=Lambda^[-m^2/(2pi beta K)] exp[-m^2 b/(2pi beta K)]>0. In particular eta_6=18/(pi beta K).

Proof: polar integration gives the variance formula, and the Gaussian characteristic function gives the correlation. Near zero, 1-J_0(t)=O(t^2). For t>=1, J_0(t)=O(t^-1/2), so the second integral defining b is absolutely convergent. Split F at 1 and subtract log z. These estimates prove the asymptotic without any inferred infinite-volume Gibbs claim.

If stationarity of the phase itself is desired, add a uniform independent global phase U in [0,2pi) and take exp[i m(U+g(x))]. Under translations, the Gaussian increments keep their law, and U+g(a) modulo 2pi is uniform and independent of all increments, conditionally on the Gaussian field. Thus the resulting phase field is stationary and has the same two-point formula.

This establishes the IR boundary between an integrable angular spectrum (positive plateau, L01-L02) and a |k|^-2 angular spectrum (algebraic decay). It does NOT establish positional decorrelation, defect unbinding, an interval of Gibbs phases, or the KTHNY universal exponent bound. The effective Frank stiffness beta*K here corresponds to the dimensionless stiffness in MIT 8.334 Lecture 23, equation VII.108.

Reviewer: w548 pending. No novelty claim.
