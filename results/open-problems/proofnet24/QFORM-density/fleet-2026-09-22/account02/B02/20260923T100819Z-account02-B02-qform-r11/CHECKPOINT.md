SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B02, 2026-09-23T10:08:19Z.
attacking: the live high-volume-coloop collar by sharp-HY fractional volume plus the current account03/B02 mixed-(3+2)-volume compiler.

# Early substantive checkpoint

Full QFORM remains open. All coordinates below are ORIGINAL product coordinates; no post-rotation independence or pointwise scalar Fresnel decay is used.

## 1. Independent analytic check: sharp q-dependent Hausdorff--Young endpoint

For the reviewed three-volume Weyl/BL argument, let `alpha_i` be the row volume marginals and assume `alpha_i<=q/2`, `1<=q<3/2`. Beckner Hausdorff--Young at output exponent `r=q/alpha_i>=2`, with `0<=f_i<=1` and `int f_i=1`, gives after the `2|t|` scaling

`|| |psi_i(2t .)|^q ||_(1/alpha_i)
 <= (pi/|t|)^alpha_i (alpha_i/q)^(alpha_i/2)
    (1-alpha_i/q)^(-(q-alpha_i)/2)`.

Multiplying with the volume-sampling Brascamp--Lieb constant cancels every `alpha_i^(alpha_i/2)`. Since `sum alpha=sum beta=3` and `-(1-s)log(1-s)<=s`, the row and column entropy factors contribute at most `e^(3/2)` each. Hence

`E F_t^q <= e^3 q^(-3/2) (pi/|t|)^3 Z^(-1/2)`, `Z=e3(M^T M)`.

Thus

`|phi_Q(t)| <= min(1,K|t|^(-3/(2q)))`,

and exact integration plus Fourier inversion yields

`||p_Q||_infinity <= 3e/[(3-2q)sqrt(q)] Z^(-1/6)`.

The endpoint bookkeeping is exact: `q=1` is admissible; `q=3/2` gives only the nonintegrable exponent `|t|^-1`; `q<3/2` is precisely the L1 range of this envelope. Therefore the analytic/constants/endpoints portion of the new volume-stability result is PASS. This does not certify the separately assigned matrix/tail review.

## 2. Partner result actually selected for use

The current completed account03/B02 r25 theorem mixes an incident third-volume law `J3` at a physical row/column anchor `(x,y)` with residual second volume `E2`, using a parameter `theta`. If the mixed row (or column) marginals obey `alpha_i<=q/2`, `1<=q<(2+theta)/2`, then

`||p_Q||_infinity <= C(theta,q)
 J3^[-theta/(2(2+theta))] E2^[-(1-theta)/(2(2+theta))]`,

with its explicit sharp-HY constant. If both gates fail, a fixed additional physical row/column carries a definite fraction of either the incident third volume or residual second volume, and that packet is exactly a true cross-Schur Frobenius bank or a two-star product.

The next calculation in this run is to spend that finite common-anchor packet rather than return it as another unnamed marginal obstruction.
