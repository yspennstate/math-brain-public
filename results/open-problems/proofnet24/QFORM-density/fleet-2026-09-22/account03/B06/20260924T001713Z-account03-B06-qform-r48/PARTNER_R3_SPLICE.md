# r48 final designated-partner splice

A final account04/B06 directory refresh found a newer completed designated-partner theorem than the r2 source used in the first immutable `REPORT.md` publication:

- `yspennstate/math-open-problems@a09353b7b4cc9b1b812b1d1f2f319f5dcef5e10b`
- `proofnet24/QFORM-density/fleet-2026-09-22/account04/B06/20260924T001014Z-account04-B06-QFORM-r3/REPORT.md`
- theorem `QFORM-TANGENTIAL-SHARED-LEAKAGE-ABSORPTION-v1`.

This supplement applies the newer theorem to the same actual r48 post-pivot inequality and is the partner application to use for the final handoff.

## Actual r48 application

Retain the r48 notation after the heavy original-coordinate pivot:

`S0=D0+E0^T T0 E0`, `G0=E0E0^T`,

and assume the genuine diffuse deleted-frame gate

`max_j e_j^T G0^{-1} e_j <= 1/2`.                                  (1)

Whiten the physical two-frame,

`F=G0^{-1/2}E0`.                                                    (2)

Its two rows are orthonormal coefficient vectors on the original-coordinate bank, and the squared norm of column `j` is exactly the leverage in (1). Diagonalize

`B0=G0^{1/2}T0G0^{1/2}`                                            (3)

inside this two-dimensional coefficient space. Let the eigenvalues be `mu1,mu2`, ordered by `|mu2|>=|mu1|`, and let `(L,V)` be the resulting two original-bank linear statistics.

Now let a further linear statistic sharing this same bank have coefficient vector in `rowspan(E0)`. Because that row space is exactly `span{L,V}`, it has the literal form

`B_S=alpha L+gamma V`.                                              (4)

Allow in addition an arbitrary random `B_R` from a disjoint fresh original-coordinate bank and set

`B=B_S+B_R`.                                                        (5)

The newest partner theorem applies to

`Y=mu2(V-v0)^2+beta B+c`.                                          (6)

It completes the shared `gamma V` term into the shifted fold

`v_*=v0-beta gamma/(2mu2)`                                         (7)

and removes the shared `alpha L` term by the determinant-one output shear

`(l,y) -> (l,y-beta alpha l-constant)`.                            (8)

Therefore on the actual off-fold event `|V-v_*|>1/64`, the joint density of `(L,Y)` satisfies

`boxed: ||g_off||_infinity <= 256/|mu2|.`                          (9)

This is stronger in scope than the preceding r2 splice because the transverse statistic is now allowed to share the curved bank arbitrarily **inside the same two-dimensional shear plane**.

Finally,

`|mu1 mu2|=|det B0|=|det T0| det G0`,                              (10)

and `|mu2|>=sqrt(|mu1mu2|)`. Hence the actual matrix inequality is

`boxed:
 ||g_off||_infinity
 <=256 [|det T0| det G0]^(-1/2).`                                  (11)

Using the exact r48 heavy-pivot currency,

`|det T0|det G0
 =|det T|det G * |d0/s| * (1-alpha_h)`,                            (12)

(11) becomes

`boxed:
 ||g_off||_infinity
 <=256 [|det T|det G * |d0/s| * (1-alpha_h)]^(-1/2).`              (13)

Equation (13) is the completed designated-partner result applied to an actual r48 inequality.

As in the partner theorem, (9)-(13) give a continuous `C_0` two-output density. They are not silently promoted to a scalar density theorem for the whole terminal residual, because the same-bank diagonal term `D0` is not absorbed by this splice. The main scalar target-level branch remains Theorem 5.1 of `REPORT.md`, which retains `D0` through the rank-two cross-block half-Riesz route.

## Consequence for the remaining debt

Exact tangential shared leakage is no longer part of the B06 obstruction. After this splice, the genuinely new shared-bank difficulty is a component outside the two-dimensional shear plane (positive normal Gram volume), together with the low-disjointness/heavy-coloop degeneration already isolated in the main report.
