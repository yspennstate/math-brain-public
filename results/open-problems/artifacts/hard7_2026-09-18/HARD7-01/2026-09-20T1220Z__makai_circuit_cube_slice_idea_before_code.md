# HARD7-01 route note before code — Makai on affine circuits via cube sections

Runtime identity for the eventual report: GPT-5.6 Sol; reasoning telemetry UNVERIFIED, not GPT-6 maximum.

Current target: `operations/claims/MAKAI-POLAR-DIFFERENCE-BODY.md`. Frozen source metric remains `d_Makai=2`; any `n+2`-vertex theorem is PARTIAL and does not move it.

Fresh method triple after the previous B6/B18/B24 run: **B1 / B16 / B25**.

- **B1 (change category):** replace the polar-difference-body problem for a polytope with `n+2` vertices by a central hyperplane-section problem for the `(n+2)`-cube.
- **B16 (compute the smallest genuine circuit):** the five-vertex three-dimensional circuit (triangular bipyramid) suggests an exact formula in the unique affine-dependence coefficients; direct rational samples show the source constant is approached only at a simplex degeneration.
- **B25 (count the same thing twice):** compute the same cube-section volume first by the Jacobian of affine-function evaluations and second as the density at the mean of a weighted sum of independent uniforms.

## Candidate dimension-free theorem

Let

`K = conv(v_1,...,v_{n+2}) subset R^n`

be full-dimensional and suppose the `n+2` points form a nondegenerate affine circuit. Write the unique affine dependence as

`sum_i c_i v_i = 0`, `sum_i c_i = 0`,

normalized by

`sum_{c_i>0} c_i = -sum_{c_i<0} c_i = 1`.

Let `D=K-K`, `m=n+2`, and let

`S(c)=vol_{n+1}([0,1]^m intersect c^perp)`.

The intended exact identity is

`|K| |D^circ| = ((n+1)/n!) * S(c)/||c||_2`.

Reason:

1. If `A` is the `(n+2) x (n+1)` matrix with rows `(v_i^T,1)`, then the cofactor vector is proportional to `c`. If the proportionality constant is `lambda`, Cauchy--Binet gives the Jacobian `J=sqrt(det(A^T A))=lambda ||c||_2`.
2. Circuit triangulation gives `|K|=lambda/n!`.
3. The map `(y,r) -> ( <y,v_i>+r )_i` sends `R^(n+1)` linearly onto `c^perp` with Jacobian `J`. For fixed `y`, the allowable `r`-interval inside the cube has length `1-h_D(y)` exactly when `y in D^circ`. Hence

   `S(c)=J int_{D^circ}(1-h_D(y))dy = J |D^circ|/(n+1)`.

Combining gives the identity.

## Probability reduction

Reflect the cube coordinates on the negative support of `c` and put `w_i=|c_i|`. Then

`sum_i w_i=2`, `0<w_i<=1`,

and the section becomes

`{x in [0,1]^m : sum_i w_i x_i = 1}`.

If `U_i iid Unif[0,1]` and `W=sum_i w_i U_i`, the coarea formula gives

`S(c)/||c||_2 = f_W(1)`.

Thus Makai on circuits is equivalent to the one-dimensional concentration lemma

`f_W(1) >= 1` whenever `w_i in (0,1]` and `sum_i w_i=2`.

## Candidate proof of the concentration lemma

Center the uniforms. Replacing two widths `a,b` with `a+b<=1` by one uniform of width `a+b` can only DECREASE the density at zero after convolution with any symmetric unimodal remainder. Indeed `Unif[-a/2,a/2]+Unif[-b/2,b/2]` is more peaked than `Unif[-(a+b)/2,(a+b)/2]`: its central-interval probability dominates the latter for every radius. Convolution with a symmetric unimodal density preserves this comparison at zero by layer-cake.

Repeat merging until no two widths have sum at most one. Because the total width is two, at most three positive widths remain.

- Two widths force `(1,1)`, whose centered convolution has density `1` at zero.
- For three widths `a,b,c<=1`, `a+b+c=2`, inclusion-exclusion at the center gives

  `f(1)=[1-(1-a)^2-(1-b)^2-(1-c)^2]/(2abc)`.

  Put `x=1-a, y=1-b, z=1-c`, so `x+y+z=1`. Then

  `f(1)=(xy+yz+zx)/((x+y)(y+z)(z+x))`

  and

  `(x+y)(y+z)(z+x)=(x+y+z)(xy+yz+zx)-xyz <= xy+yz+zx`.

Hence `f(1)>=1`.

If the derivation survives checking, it proves Makai's conjectured constant for every affine-circuit polytope with `n+2` vertices in every dimension. In `R^3`, together with the already-proved all-pyramids theorem, this would cover every polytope with at most five vertices. This is not a proof for arbitrary three-dimensional convex bodies and does not move `d_Makai`.