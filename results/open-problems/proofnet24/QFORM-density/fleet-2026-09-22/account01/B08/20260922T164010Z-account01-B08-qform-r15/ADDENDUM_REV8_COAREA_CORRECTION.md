# Addendum — bounded 3D density alone does not control an indefinite rank-three quadratic pushforward

**Claim ID:** `QFORM-RANK3-COAREA-LINF-ONLY-FALSE-v1`  
**Status:** exact counterexample to an intermediate lemma only; **not** a counterexample to the full product-law QFORM conjecture.

During the prepublication control refresh, owner revision `2026-09-22.8` proposed the intermediate statement that if a three-dimensional vector `Y` has joint density `rho`, then for an indefinite rank-three form such as

`q(y)=y_1^2+y_2^2-y_3^2`

one should have a universal bound

`||p_(q(Y))||_infinity <= C ||rho||_infinity`.

That statement is false without additional provenance/structure on `rho`. This is consistent with the already-live correction that a bounded projection density alone does not control an indefinite quadratic pushforward.

## Exact construction

Use cylindrical coordinates

`y_1=r cos(theta)`, `y_2=r sin(theta)`, `y_3=z`,

and then light-cone coordinates

`u=r-z`, `v=r+z`.

For `u,v>0`,

`r=(u+v)/2`, `z=(v-u)/2`,

and the exact identities are

`q=uv`,

`dy_1 dy_2 dy_3 = (u+v)/4 du dv dtheta`.                         (1)

Fix `R>1`. Let `a_R>0` be the positive solution of

`(pi R a_R^2)/4 + (3 pi R^2 a_R)/4 =1`,                         (2)

namely

`a_R = [-3R + sqrt(9R^2+16/(pi R))]/2`.

Define the set

`E_R={0<=theta<2pi, R<=v<=2R, 0<=u<=a_R}`

through the above coordinate map, and let

`rho_R=1_(E_R)`.

By (1) and (2), `rho_R` is a probability density and

`||rho_R||_infinity=1`.                                         (3)

## Exact pushforward density

For every

`0<s<a_R R`,

the equation `uv=s` has `u=s/v` inside `[0,a_R]` for every `v in [R,2R]`. Integrating the delta function in the `u` variable gives the density of `q(Y)`:

`p_R(s)
 = 2pi int_R^(2R) [(s/v+v)/4] (1/v) dv
 = (pi/2) int_R^(2R) [1+s/v^2] dv
 = (pi/2)[R+s/(2R)]`.                                           (4)

Therefore

`||p_R||_infinity >= pi R/2`.                                   (5)

As `R->infinity`, (3)-(5) show

`||p_(q(Y))||_infinity / ||rho_R||_infinity -> infinity`.

Hence no universal constant `C` can bound the indefinite rank-three quadratic pushforward using only the `L^infinity` norm of an arbitrary 3D input density.

## Consequence for the QFORM programme

This does **not** refute the original conjecture: the densities `rho_R` above have not been represented as the relevant conditional projection of an original-coordinate independent cap-one product law. It refutes only the proposed intermediate implication

`bounded conditional/projected 3D density => bounded indefinite rank-3 quadratic pushforward`

when the proof discards the special product-linear provenance.

Any rank-three coarea route must therefore retain additional information beyond `||rho||_infinity` — for example weighted affine-fiber bounds, radial/light-cone decay inherited from the original product source, or a coupled product-coordinate estimate before the indefinite trace. The B08 stable-rank/ridge theorem in `REPORT.md` is unaffected because it never uses this false coarea shortcut.
