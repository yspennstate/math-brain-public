# E0065 (Problem 12) — a lower bound for `alpha_3`

Companion to `E0065_regularity_threshold_alpha_m.md`, which proves `alpha_2 = (3-sqrt7)/4`.
Here `m = 3`. The survey (arXiv:0902.4207, Theorem 7) gives only `alpha_3 <= 1/6`.

## Result

    alpha_3 >= 1/12 = 0.08333...,   so   1/12 <= alpha_3 <= 1/6.

The lower bound is attained in the limit by an explicit one-parameter family of QSOs on
`S^2`, and is certified by an exact 2-periodic orbit — for `L = 1/13` the orbit is rational.

## The family

For `0 < L < 1/3` let `V_L` be the QSO on `S^2` with

    P_11 = (1-2L,   L,     L    )      P_12 = (L,     L,     1-2L )
    P_13 = (L,      1-2L,  L    )      P_22 = (L,     L,     1-2L )
    P_23 = (1-2L,   L,     L    )      P_33 = (L,     1-2L,  L    )

i.e. `P_{ij,.} = L (1,1,1) + (1-3L) e_{sigma(ij)}` with

    sigma(11) = 1,  sigma(12) = 3,  sigma(13) = 2,
    sigma(22) = 3,  sigma(23) = 1,  sigma(33) = 2.

Every off-diagonal pair `{i,j}` points at the third type (the "strictly non-Volterra" rule of
the survey's Section 8); the diagonal map is `1 -> 1`, `2 -> 3`, `3 -> 2`. Since `L < 1/3`,
`min_{ijk} P_{ij,k} = L`.

`V_L` commutes with the transposition `rho = (2 3)` of coordinates (checked exactly):
`V_L(rho x) = rho(V_L x)`.

## Facts, all exact (`e0065_m3_exact.py`, `e0065_m3_twocycle.py`, `e0065_m3_cert.out`)

**1. The barycentre is the unique fixed point in `S^2`.** `sympy.solve` returns four
solutions of `V_L(x) = x`:

    (1/3, 1/3, 1/3),
    x_1 = (L-1)/(3L-1),      x_2 = L/(3L-1),
    x_1 = (2-3L)/(3L-1),     x_2 = (6L -+ sqrt(48L^2-64L+21) - 3)/(2(3L-1)).

For `0 < L < 1/3` the second has `x_1 = (1-L)/(1-3L) > 1` and the last two have
`x_1 = -(2-3L)/(1-3L) < 0`, so all three lie outside the simplex. Only the barycentre
survives.

**2. The tangent spectrum at the barycentre is `{0, 4L - 4/3}`.** The full Jacobian has
eigenvalues `{2, 4L-4/3, 0}`; the `2` is the eigenvalue forced by `sum_k V_k = (sum x)^2`
(the columns of `J` sum to `2`), so the tangent eigenvalues are `0` and `4L - 4/3`. Hence

    |4L - 4/3| = 1   exactly at  L = 1/12  and  L = 7/12,

and for `L < 1/12` the barycentre has a real tangent eigenvalue `< -1`. The eigenvalue `0`
is along the `rho`-invariant line `{x_2 = x_3}`; the unstable direction is the
`rho`-antisymmetric one.

**3. An exact 2-periodic orbit for every `0 < L < 1/12`.** Because `V_L` commutes with
`rho`, an orbit of the form `{x, rho x}` solves `V_L(x) = rho(x)`. Solving that system
symbolically gives, besides the barycentre, the single antisymmetric solution

    x_1 = 3L/(1-3L),
    x_2 = (1 - 6L + sqrt(D))/(2(1-3L)),
    x_3 = (1 - 6L - sqrt(D))/(2(1-3L)),        D = 48L^2 - 16L + 1,

with `D = 0` exactly at `L = 1/12` and `L = 1/4`. For `0 < L < 1/12`:

* `D > 0`, so the point is real and `x_2 != x_3`, i.e. it is **not** a fixed point;
* `x_1 = 3L/(1-3L)` lies in `(0,1)` for `L < 1/6`;
* `x_3 > 0` because `(1-6L)^2 - D = 4L(1-3L) > 0` and `1-6L > 0`;
* `x_1+x_2+x_3 = 1` identically.

So `{x, rho x}` is a genuine 2-periodic orbit in the **open** simplex, and its trajectory
does not converge. Therefore `V_L` is not regular for every `0 < L < 1/12`, and its minimum
matrix entry is exactly `L`. Letting `L` increase to `1/12` gives `alpha_3 >= 1/12`.

At `L = 1/12` the 2-cycle merges into the barycentre (`D = 0`, and the formula returns
`(1/3,1/3,1/3)`) — the period-doubling is exactly at the threshold, as it is for `m = 2`.

**4. Rational certificate at `L = 1/13`.** The whole cycle is rational:

    V_{1/13}(3/10, 1/2, 1/5) = (3/10, 1/5, 1/2),
    V_{1/13}(3/10, 1/5, 1/2) = (3/10, 1/2, 1/5),

verified in exact rational arithmetic; min matrix entry `= 1/13 < 1/12`. A second sample at
`L = 1/20` gives the algebraic cycle `(3/17, 7/17 + 4sqrt2/17, 7/17 - 4sqrt2/17)` with
`V^2(x) - x = (0,0,0)` and `V(x) - x = (0, -8sqrt2/17, 8sqrt2/17)` exactly.

## How the family was found, and the positive control

An exhaustive search over the `3^6 = 729` "vertex ansatz" operators
`P_{ij,.} = L + (1-3L) e_{sigma(ij)}`, bisecting `L` against the certificate "every fixed
point in the simplex has tangent spectral radius `> 1`" (`e0065_vertex_jac2.py`), returns
the maximum `L = 0.083333333333` attained by exactly three `sigma` (the family above and
its two relabellings).

The same search for `m = 2` is the **positive control**: it returns `0.088562172234`, i.e.
`(3-sqrt7)/4`, attained by `sigma = (1,0,0)` and `sigma = (1,1,0)` — the two extremal
patterns proved extremal in the companion note. That control exposed two errors in earlier versions of the search:

* an orbit-based detector ("the tail of the trajectory has positive diameter") overshot to
  `0.08996`, because at `|f'(p)| = 0.996` four thousand iterations cannot resolve the
  convergence. Numerical non-convergence is not evidence of non-convergence near a
  neutral fixed point.
* the first Jacobian omitted the factor `2` on off-diagonal pairs `(i,j)`, `i<j`. The
  control returned `0.0552` instead of `0.0886`. The check that the columns of `J` sum to
  `2` catches this in one line and is in the script.

## What is *not* established

`alpha_3 = 1/12` is **not** proved. What is proved is `1/12 <= alpha_3 <= 1/6`. The upper
bound `1/6` is the survey's Theorem 7(1). Two gaps:

1. The vertex ansatz is a 729-point subset of a 12-dimensional parameter space. A general
   local search over all 12 parameters at fixed floors (`e0065_m3_general.py`,
   `e0065_m3_general.out`) found no operator with every fixed point repelling at
   `L = 0.084, 0.086, 0.0886, 0.095`; at `L = 0.0833` it recovers the vertex-ansatz
   operator. This is a heuristic search, not a proof, and the floors `0.11, 0.13, 0.15`
   were not run. A non-regular QSO with min entry above `1/12` would improve the bound.
2. Even within the vertex ansatz, the certificate used (all fixed points repelling) is
   sufficient but not necessary for non-regularity: an operator with one attracting fixed
   point and a 2-cycle elsewhere is non-regular and would be missed. So the vertex-ansatz
   number `1/12` is itself only a lower bound for the vertex-ansatz optimum.

**Strongest case that `1/12` is wrong as the value of `alpha_3`:** the `m=2` extremum sits
at an irrational algebraic number `(3-sqrt7)/4`, and a clean rational like `1/12` appearing
for `m=3` is suspicious — it is the value at which a *linear* eigenvalue `4L - 4/3` crosses
`-1`, which happens only because the barycentre is fixed for the whole family and the
tangent spectrum is affine in `L`. A general operator has a fixed point that moves with the
parameters, and its critical `L` will generically be algebraic of higher degree and larger.
**The check that would settle it:** a proof that every QSO on `S^2` with min entry above
`1/12` is regular, or an operator above `1/12` with a 2-cycle; the local search above found
none up to `L = 0.095`.

## Status

* `alpha_3 >= 1/12` — **proved** (exact 2-cycle, exact fixed-point count, exact spectrum).
* `alpha_3 <= 1/6` — the survey's Theorem 7(1), not re-derived here.
* `alpha_3 = 1/12` — **conjecture**, supported by an exhaustive vertex-ansatz search whose
  `m=2` instance is exact.
* `alpha_m` for `m >= 4` — untouched. The construction generalises verbatim: take the
  strictly-non-Volterra off-diagonal rule together with a diagonal permutation, and read off
  the tangent spectrum at the barycentre.

## Literature check (2026-09-13)

Same searches as the companion note. No paper was found computing `alpha_m` for any
`m >= 3`; the surveys restate Theorem 7 and Problem 12 unchanged, most recently in the
2015 Springer chapter *Quadratic Stochastic Operators and Their Dynamics*. The relevant
literature is largely in Uzbek and Russian journals with no online full text, so a paper
may exist that the search did not reach.
