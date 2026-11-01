# Regularity addendum for r39

This addendum supplies the rigorous `C_0` step for `QFORM-SHARP-MIXED-FRAME-SAMESIGN-CLOSURE-v1` and supersedes the informal sentence in `REPORT.md` that invoked `L^1*L^1` continuity directly.

Fix `H=h` in the notation of Section 4 of the report. The three independent square terms have densities

`g_1 = density of 2(X_1+h/2)^2`,
`g_2 = density of (X_2+X_4)^2`,
`g_3 = density of -2(X_3+h/2)^2`.

Each underlying scalar variable has density cap at most one: translations preserve the cap, and `X_2+X_4` has density cap at most one by Young. Hence, for a square coefficient `a>0`, the density `g` of `aY^2` obeys

`g(y) <= (a y)^(-1/2)` for `y>0`, and `integral g=1`.

Consequently `g in L^(3/2)` with a bound depending only on `a`: split at `y=1/a`. On `(0,1/a)`,

`integral g^(3/2) <= a^(-3/4) integral_0^(1/a) y^(-3/4)dy = 4/a`,

while on `[1/a,infinity)` the envelope is at most one, so `g^(3/2)<=g` and that contribution is at most one. Thus

`||g||_(3/2)^(3/2) <= 1+4/a`.

The same bound applies to a reflected square. Therefore `g_1,g_2,g_3` are uniformly in `L^(3/2)` for all `h`. Young gives

`g_1*g_2 in L^3`,

and the standard conjugate-exponent convolution theorem (`L^3 * L^(3/2) subset C_0`) gives

`p_h = g_1*g_2*g_3 in C_0(R)`.

The beta-convolution estimate from the main report still gives the uniform pointwise bound

`||p_h||_infinity <= pi/sqrt(2)`.

The conditional law of `Q_ctl,theta` is `p_h(. - theta h^2)`. For any sequence `t_n->t`, pointwise continuity of every conditional density together with the uniform `pi/sqrt(2)` bound permits dominated convergence in the `H`-mixture, proving continuity of the unconditional density. For `|t|->infinity`, every shifted conditional `C_0` density tends to zero, and the same uniform domination gives vanishing at infinity by dominated convergence.

Thus the regularity conclusion in `REPORT.md` is valid: the closure family has a continuous `C_0` density. The essential-height proof and constant `pi/sqrt(2)` are unchanged.
