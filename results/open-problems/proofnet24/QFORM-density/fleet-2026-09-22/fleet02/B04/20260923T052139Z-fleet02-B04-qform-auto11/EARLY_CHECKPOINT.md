SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B04, 2026-09-23T05:21:39Z.
attacking: entropy-optimized two-volume Fourier rearrangement on a physical rank-two cross packet, compared against ridge certificates on the same rotated indefinite target matrix.

# Early mathematical checkpoint

Programme: `QFORM-DENSITY-3EIG-20260922`. Full target remains OPEN. Corrections consumed: no law-uniform pointwise quadratic-phase decay; no post-rotation independence; arbitrary-joint rank-three coarea and positive conditional-cap moments are unavailable; no uniformly good local minor or universal rank-three cross cut is assumed.

## New candidate theorem being completed

Let `R` be a quadratic-plus-affine polynomial on disjoint ORIGINAL-coordinate banks with physical cross block `M`. Let `w_ST` be any probability weights on nonzero physical `2x2` minors and define row marginals `alpha_i=P_w(i in S)`, column marginals `beta_j=P_w(j in T)`, and

`G_2(w)=exp(sum_ST w_ST log det(M_ST)^2 + H(w)).`

The weighted-AM-GM determinant step in the completed e5 Claude Theorem D works for arbitrary minor weights, not only canonical volume weights. Combining that step with the completed rank-two fractional time integral gives, for `1<=q<2` and `max_i alpha_i<=q/2`,

`H_{1/2}(R) <= [4 sqrt(2e) q^(-1/4)/(2-q)] G_2(w)^(-1/8).`

Hence one untouched original scalar square gives

`||p_[a(Z+m)^2+R]||_inf <= [4 sqrt(2e) q^(-1/4)/(2-q)] |a|^(-1/2) G_2(w)^(-1/8).`

The proof uses only product-space decoupling, Brascamp--Lieb, Hausdorff--Young / fractional-Riesz integration and the square peel; it does not rotate the random coordinates.

## Exact optimization stress matrix

Take four left rows, two right coordinates, and before a harmless fixed physical right coefficient rotation set

`r1=8 e1`, `r2=e2`, `r3=(e1+e2)/sqrt(2)`, `r4=(e1-e2)/sqrt(2)`.

The six squared `2x2` minors are

`64, 32, 32, 1/2, 1/2, 1`

on edges `12,13,14,23,24,34`, respectively, and `Z_2=130`. For any `q=1` admissible weight the four row marginals must all equal `1/2`; solving those constraints gives

`w12=w34=x`, `w13=w24=y`, `w14=w23=z`, `x+y+z=1/2`.

The entropy-adjusted objective is

`log G_2 = (1/2)log 64 -2[x log x+y log y+z log z]` after the determinant factors cancel in opposite pairs. It is maximized uniquely at

`x=1/4`, `y=z=1/8`,

and therefore

`G_2,opt=32`.

Thus the planned target form

`Q_*=Z^2+2 X^T M Y`

will have the explicit all-input-law bound

`||p_Q*||_inf <= 4 sqrt(2e) 32^(-1/8)=6.0475362854...`.

Its symmetric matrix has spectrum `{1, +/-sqrt(65), +/-sqrt(2),0,0}`, so it is genuinely rotated, indefinite, and safely inside the exact target.

## Ridge obstruction on the SAME matrix

For the physical rank-two core, with `g=gamma^2`, the ridge matrix has maximum physical row diagonal

`k1=64/(65+g)`

and effective dimension

`theta=65/(65+g)+2/(2+g)`.

If `k1<=1/2`, then `g>=63` and `theta<0.54<4/3`. If `k1>1/2`, every admissible ridge exponent has `q>=2k1`, while

`theta/k1 = 65/64 + (65+g)/(32(2+g)) <=65/32<8/3`.

Hence `theta<=8k1/3<=4q/3`, so the square-assisted ridge gate `theta>4q/3` fails for every `gamma,q`; the direct ridge gate `theta>2q` fails a fortiori. The weighted two-volume route therefore pays a physical target matrix on which the current ridge family has no certificate at all.

Remaining work this run: prove the arbitrary-weight determinant/fractional theorem line by line; optimize jointly over `q` (not only weights); apply the latest compatible fleet03/B04 result to the actual ridge obstruction; save exact checks and source-pinned final report.
