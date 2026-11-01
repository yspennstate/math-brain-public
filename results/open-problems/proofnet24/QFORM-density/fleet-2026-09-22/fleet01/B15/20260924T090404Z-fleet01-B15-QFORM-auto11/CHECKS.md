# Checks for fleet01/B15 20260924T090404Z

Marker: `QFORM_B15_R11_TARGET_C0_LEDGER_CHECK_PASS`.

## 1. Anisotropic partner constant

For `(lambda_1,lambda_2,mu)=(4,1,1)`, fleet02/B15's coefficient is

`C_+=(4)^(-1/2) integral_0^(2pi) [sin^2(theta)/4+cos^2(theta)+1]^(-1/2)dtheta`.

Since

`sin^2/4+cos^2+1 = 2-(3/4)sin^2 = 2[1-(3/8)sin^2]`,

and with

`K(3/8)=integral_0^(pi/2)[1-(3/8)sin^2(theta)]^(-1/2)dtheta`,

fourfold symmetry gives

`C_+=(1/2)(4/sqrt(2))K(3/8)=sqrt(2)K(3/8)`.

Numerical quadrature gives

`K(3/8)=1.7605688117719545...`,
`C_+=2.489820291098983...`,
`sqrt(2) C_+=2K(3/8)=3.521137623543909...`.

Thus the rounded inequalities `<2.490` and `<3.522 Delta` in the report are conservative.

## 2. Spectrum and leverage of the diffuse-bank test

For each bank, the coefficient vector is `m^(-1/2)(1,...,1)` and has Euclidean norm one. The three bank vectors have disjoint supports, hence are orthonormal. Therefore the matrix of

`Q_m=4Y_1^2+Y_2^2-Y_3^2`

has nonzero eigenvalues exactly `{4,1,-1}`. Every active original-coordinate row contains exactly one entry of magnitude `m^(-1/2)`, hence row leverage is exactly `1/m<=1/2` for `m>=2`.

## 3. Full-density beta convolution

The one-dimensional product-projection cap used by the partner source is

`||p_(Y_k)||_infinity<=sqrt(2)`.

For `s>0`, the map `y -> 4y^2` has roots `+-sqrt(s)/2` and derivative magnitude `4sqrt(s)` there, hence

`p_(4Y_1^2)(s)
 =[p_Y(sqrt(s)/2)+p_Y(-sqrt(s)/2)]/(4sqrt(s))
 <=1/(sqrt(2)sqrt(s))`.

Similarly

`p_(Y_2^2)(s)
 =[p_Y(sqrt(s))+p_Y(-sqrt(s))]/(2sqrt(s))
 <=sqrt(2)/sqrt(s)`.

Their convolution is therefore at most

`integral_0^t [u(t-u)]^(-1/2)du = B(1/2,1/2)=pi`.

Convolution with the independent probability law of `-Y_3^2` preserves the `L^infinity` cap, proving `||p_(Q_m)||_infinity<=pi`.

## 4. Principal-block audit

Symmetric pivot sizes are one (nonzero diagonal) or two (`[[0,a],[a,0]]` when the current symmetric Schur complement has zero diagonal but is nonzero). Schur determinant factorization preserves nonsingularity of the union of selected original coordinates. Starting from rank at least three, the first accumulated pivot size at least three is therefore either three or four.

The example

`[[0,0,1,0],[0,0,0,1],[1,0,0,0],[0,1,0,0]]`

is invertible and bipartite with zero diagonal; every `3x3` principal submatrix has zero determinant, confirming that order four can be necessary.

## 5. Best-constant passage

For one marginal, truncate so tail mass is `epsilon`, add an indicator of any finite interval of length `epsilon` outside the truncation window, and then convolve with a compactly supported probability mollifier. Before mollification the density remains between zero and one, has mass one and compact support, and differs from the original in `L1` by at most `2epsilon`. Convolution preserves mass and the cap. Choosing mollifier scale after the truncation gives cap-one `C_c^infinity` approximants in `L1`.

For products, the telescoping identity gives

`||prod f_j-prod g_j||_1<=sum_j||f_j-g_j||_1`.

Deterministic pushforward cannot increase total variation. Hence smooth output measures converge in total variation, so an interval estimate with common coefficient `C` passes to the rough output with exactly the same `C`. The canonical continuous representative then has pointwise supremum at most `C` by continuity.
