# R06 idea extension before code — feed the vertex lower bound back into the interior core

This extends the immediately preceding idea note `20260920T1305Z_i0056_outercore_squarebudget_idea_84_9b71.md` before any checker is written.

The first core inequality used only edge expansion of the interior degree-4 vertices. There is a stronger self-improving input: if a rigorous global lower bound `g` for `Phi_V(T)` is already known, then for the interior set `I` of the normalized core,

`g i <= |partial_V I| <= b+d`,

because an interior selected vertex has all four graph-neighbours in the core, while an outer selected vertex of internal degree two cannot be adjacent to `I`; only the `b` degree-three outer vertices and `d` degree-four outer vertices can lie in `partial_V I`.

Keep the two core inequalities

(A) `(1+q)a + (1-q)b/2 - 2q d - q i >= 5q`, where `q=2/sqrt(3)`,

(B) `b+2d-hi >= 0`, where `h=4/(1+sqrt(3)+sqrt(5))`,

and add

(C_g) `b+d-g i >= 0`.

A nonnegative linear combination of (A),(B),(C_g) can be chosen to give exactly

`a+(1-F(g))b-F(g)(d+i) >= 5q/(1+q) > 0`,

where

`F(g)=(g+c)/(g+1)`,

`c=(q+(h/2)(q-1))/(q+1)`.

Indeed, divide (A) by `1+q`, multiply (B) by

`beta=(q-1)/(2(q+1))`,

and multiply (C_g) by

`gamma=(1-(h/2)(q-1))/((g+1)(q+1))`.

Both multipliers are positive for the present `q,h`. The coefficients of `d` and `i` become `-F(g)` and the coefficient of `b` becomes `1-F(g)`.

Therefore the normalization/core argument should establish the implication

`Phi_V(T) >= g > 1/2  ==>  Phi_V(T) >= F(g)`.

Since

`F(g)-g=(c-g^2)/(g+1)`,

iterating from the previously rigorous seed

`g0=1/(sqrt(3)+sqrt(5)-2)=0.5080994133... > 1/2`

increases monotonically to the positive fixed point

`g_* = sqrt(c) = 0.7515326907765906848...`.

This would improve the mixed-face lower bound much more sharply than the one-step edge-only bound in the first idea note. With the retained exact upper witness `384566/484385`, the interval width would become about `0.04239362816`.

Before promotion the checker must verify the exact coefficient identities, positivity of `beta,gamma`, the fixed-point algebra, and the exact ordering

`g0 < g_* < 384566/484385`.

The theorem proof itself remains combinatorial and must be written on the page; algebra code is only a self-check.
