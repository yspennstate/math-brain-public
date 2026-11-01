SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B10, 2026-09-23T03:43:10Z.
attacking: the small-Pluecker-mass near-null hub/star collar; pay every genuinely transverse second-heavy row and build an arbitrary-hub complement-whitening deletion dichotomy without rotating the product law.

# Early substantive checkpoint

Programme: `QFORM-DENSITY-3EIG-20260922`. Full target remains OPEN. Execution label remains `WITHOUT_VERIFIED_BRAIN`.

Fresh predecessor actually used: fleet03/B10 r23b, `math-open-problems@91759f77fcdf696a75d8e6c6ef398c03654b025a`, which reduces the exact-rank-three collar `0<d<1/64` to an original physical hub row `r_i=sqrt(c)e` satisfying

`c>1/4`, `|A_ii|<1/64`, hence `|e^T Lambda e|<1/16`, and `||A_{i,-i}||_2>sqrt(1023)/64`,

unless an already-paid scalar-pivot branch applies.

## New calculation 1: near-null transverse-heavy row is paid

Let another physical spectral row be `u=r_j=x e + sqrt(h) v`, with `v perpendicular e`, `||v||=1`, `h>=1/4`. Put

`alpha=e^T Lambda e`, `b=e^T Lambda u`, `q=u^T Lambda u`.

Assume for contradiction `|b|<1/32` and `|q|<1/128`. The compression of `Lambda` to `E=span(e,v)` is

`C=[[alpha,delta],[delta,zeta]]`,
`delta=(b-alpha x)/sqrt(h)`,
`zeta=(q-2xb+alpha x^2)/h`.

Using `|alpha|<1/16`, `sqrt(h)>=1/2`, `|x|<=1` gives

`|delta|<3/16`, `|zeta|<17/32`.

Hence the row-sum operator bound gives `||C||op<23/32<1`. But the map `P_{E^perp} Lambda|_E:E->E^perp` has nontrivial kernel because `dim E=2`, `dim E^perp=1`. For a unit vector z in that kernel, `Lambda z=Cz`, so `||Lambda z||<1`, contradicting `sigma_min(Lambda)>=1`. Therefore

`|e^T Lambda r_j|>=1/32` OR `|A_jj|>=1/128`.

If the diagonal alternative occurs, row leverage `c_j>=h>=1/4` and the completed scalar-pivot theorem gives

`||p_Q||inf <=128[(1/4)(1/128)|det Lambda|]^(-1/4) <=128*512^(1/4)<609`.

If the cross alternative occurs and `|A_jj|<1/128`, then `|A_ij|=sqrt(c)|e^T Lambda r_j|>1/64`. Together with `|A_ii|<1/64`, the physical pair is uniformly indefinite and

`kappa=sigma_min(A_{ij,ij}) > 1/64-(1/64+1/128)/2 = 1/256`.

The completed compatible fleet04/B16 fixed-pair identity is applied here at the actual inequality

`P_ij:=sum_{k!=i,j}|det A_{ijk}|=|det Lambda| G_ij`, `G_ij=c h>=1/16`,

so `P_ij>=1/16`. Feeding this total bank into B10 r17's completed aggregate indefinite-pair Schur theorem gives

`||p_Q||inf <=8*2^(3/4)(kappa P_ij)^(-1/4) <64*2^(3/4)<108`.

Thus every row with transverse leverage at least `1/4` is paid; the surviving near-null hub collar has

`||(I-ee^T)r_j||^2<1/4` for every j!=i.

## New calculation 2: arbitrary-hub complement whitening

No nullity of the hub is needed for this step. Let `G=I-r_i r_i^T`; then `det G=1-c` and the complement rows satisfy `R_C^T R_C=G`. For `c<1`, put

`V=R_C G^(-1/2)`, so `V^T V=I_3`, and `M=G^(1/2) Lambda G^(1/2)`, so

`|det M|=(1-c)|det Lambda|`.

Conditioning only on the original hub coordinate `X_i=x`, the exact complement form is

`X_C^T V M V^T X_C + sum_{j in C} ell_j(x) X_j + const(x)`.

The x-dependent term is coordinate-separable in the original independent complement variables. Therefore the completed diffuse separable-phase theorem applies whenever every row of V has leverage at most 1/2:

`||p_Q||inf <=3e[(1-c)|det Lambda|]^(-1/3)`.

In particular if `c<=7/8`, this is at most `6e` and gives a continuous density.

More generally greedily delete a retained whitened row of leverage >1/2, checking after each deletion the retained Gram determinant q. If the procedure reaches a diffuse retained frame with q>=1/8 after at most two deletions, conditioning on the hub and those deleted ORIGINAL coordinates gives

`||p_Q||inf <=3e[q(1-c)|det Lambda|]^(-1/3) <=12e` when `c<=7/8`.

If q falls below 1/8, this happens after at most three deletions and there is a unit whitened spectral direction a for which those at most three original rows carry more than half the frame energy. This is the finite-localization alternative to be written carefully in the final report.

The exact designated `fleet04/B10` still has no current-QFORM archive at fresh lookup, so no theorem is fabricated. The compatible fleet04/B16 determinant-bank identity above is used at a displayed inequality. The newest current Claude one-hub record at `469544eaf917159c10c7b04f661c6e411feb392b` is also being retained at its actual scope; its interval-hub theorem is a scoped exit only and is not substituted for arbitrary support.
