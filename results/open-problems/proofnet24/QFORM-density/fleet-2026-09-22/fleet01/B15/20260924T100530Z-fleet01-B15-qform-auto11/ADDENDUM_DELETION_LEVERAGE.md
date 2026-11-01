# Addendum — exact deletion-leverage criterion for linear submass stability

This sharpens Theorem 2.1 of `REPORT.md`. The global condition `max_i a_i<=1/3` is only a simple sufficient condition. The actual contraction criterion is coordinate-specific and is naturally expressed through the Parseval frame after deleting the perturbed source coordinate.

## 1. Exact coordinatewise criterion

Let `R in R^{n x 3}`, `R^T R=I_3`, with rows `r_j^T`, and fix coordinate `i`. Put

`a_i=|r_i|^2<1`,

`G_{-i}=I_3-r_i r_i^T`.

The frame formed by the remaining rows, whitened back to a Parseval frame, has row leverages

`L_{j|-i}=r_j^T G_{-i}^{-1} r_j
          =a_j + <r_j,r_i>^2/(1-a_i)`, `j!=i`.                     (1.1)

Assume

`a_i<=1/2`,
`max_{j!=i} L_{j|-i}<=1/2`.                                       (1.2)

Then replacing the `i`-th cap-one probability density by any cap-one subdensity of mass `m<=1` gives, for

`A=R Lambda R^T+D`, `D` diagonal,

`boxed:
 H(nu_{i,m})
 <=12m {|det Lambda|[1-(1-m^2)a_i]}^(-1/3)
 <=12m {|det Lambda|(1-a_i)}^(-1/3).`                             (1.3)

This is the same linear-in-mass conclusion as Theorem 2.1 but without a global maximum-leverage hypothesis.

## 2. Proof

After scaling the selected original coordinate by `m`, the rank-three Gram matrix is

`G_m=I_3-(1-m^2)r_i r_i^T`.

Let `t=1-m^2 in [0,1]`. Sherman--Morrison gives, for every `j!=i`,

`L_j(m)
 =a_j + [t/(1-ta_i)] <r_j,r_i>^2`.                                (2.1)

The scalar function

`t -> t/(1-ta_i)`

is increasing on `[0,1]`. Hence

`L_j(m)<=L_j(0)=L_{j|-i}<=1/2`.                                   (2.2)

The scaled selected row has leverage

`L_i(m)=m^2 a_i/[1-(1-m^2)a_i]<=a_i<=1/2`.                        (2.3)

Thus the completed Theorem-F leverage condition survives every contraction `m in (0,1]`. The determinant identity remains

`det G_m=1-(1-m^2)a_i`,                                             (2.4)

so the proof in the main report gives (1.3).

## 3. Full source-Lipschitz corollary for deletion-stable frames

Suppose (1.2) holds for every coordinate `i`. Define

`a_* = max_i a_i <1`.

Then for any two cap-one product laws `f,g`, with

`Delta=sum_i ||f_i-g_i||_1`,

common-part telescoping gives

`boxed:
 ||p_f-p_g||_infinity
 <=12 {|det Lambda|(1-a_*)}^(-1/3) Delta.`                         (3.1)

For an exact owner-target rank-three matrix, `|det Lambda|>=1`, so

`||p_f-p_g||_infinity<=12(1-a_*)^(-1/3) Delta`.                   (3.2)

This is a dimension-free full-law rough-source stability theorem whenever every one-row deletion leaves a 1/2-diffuse three-frame.

## 4. Why the global `1/3` threshold is natural

If `max_j a_j<=theta`, Cauchy--Schwarz gives

`L_{j|-i}
 <=a_j + a_i a_j/(1-a_i)
 =a_j/(1-a_i)
 <=theta/(1-theta)`.                                               (4.1)

Therefore `theta<=1/3` implies (1.2) for every deletion. This recovers the main report.

The value `1/3` is the largest threshold obtainable from a bound on `max_j a_j` alone through (4.1): `theta/(1-theta)<=1/2` is equivalent to `theta<=1/3`. The exact criterion (1.2) can nevertheless hold well above `1/3` when large rows are sufficiently transverse.

## 5. Interpretation

The submass operation is geometrically a contraction of one **original** coordinate. Its correct regularity parameter is therefore not merely the original leverage of that row; it is the leverage profile of the remaining spectral frame after that row is deleted and re-whitened. This gives a product-preserving diagnostic for when full-law source perturbations are linear rather than merely Holder.

No spectral-coordinate independence is used: all whitening/diagonalization occurs inside the matrix representation needed by the already-completed Theorem F, while the source law remains a product in the original coordinates.
