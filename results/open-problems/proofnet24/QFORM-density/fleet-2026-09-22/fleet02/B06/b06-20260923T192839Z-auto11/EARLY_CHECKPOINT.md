# Early substantive checkpoint — row-gate-free two-volume half-Riesz compiler

Let `M=A[I,J]` be any physical cross block of a quadratic polynomial in independent cap-one original coordinates and put

`Z=e_2(M^T M)>0`.

Normalize the squared `2x2` minors by `Z`; let `alpha_i` be the natural row inclusion marginals, so `sum_i alpha_i=2`.

**Diffuse row case.** If every `alpha_i<=1/2`, the pinned `e5f71d79eff325201dd0274053d20268ce65b837` Fourier-route `D_k` theorem at `k=2,q=1` gives

`|phi_Q(t)| <= min(1, 2*pi*sqrt(e) Z^(-1/4)|t|^(-1)).`

Using

`|x|^(-1/2)=sqrt(2/pi) int_0^infty cos(tx)t^(-1/2)dt`

and splitting at `t=K` for a bound `min(1,K/t)` gives

`H_(1/2)(Q) <= 4 sqrt(2/pi) sqrt(K)`, hence here

`H_(1/2)(Q) <= 8 e^(1/4) Z^(-1/8).`

**Heavy row case.** If `alpha_i>1/2`, write the heavy physical row as `m` and

`C=M[I\{i},J](I-P_m)`, `F=||C||_F`.

Cauchy--Binet/Lagrange gives the exact identity

`||m||^2 F^2 = alpha_i Z`.

If every row of `C` has squared norm at most `F^2/2`, the checked grouped-hub theorem at `math-open-problems@829192412f2a2d84e72b4bed91115fc5fab68401` with `k=1, ell=1` gives

`|phi_Q(t)| <= min(1, 2*pi (||m||F)^(-1/2)|t|^(-1))`,

so

`H_(1/2)(Q) <= 8 (alpha_i Z)^(-1/8) < 8*2^(1/8) Z^(-1/8).`

If some row `y` has projected residual `c=y(I-P_m)` with `||c||>F/sqrt(2)`, then

`||m wedge y||=||m|| ||c|| > sqrt(Z)/2`.

Conditioning on all same-side coordinates except the two physical originals supporting `m,y`, the exact-rank-two crossing theorem from the same checked source gives

`|phi(t)|<=min(1,pi*sqrt(2)||m wedge y||^(-1/2)|t|^(-1))`,

hence

`H_(1/2)(Q) < 8 Z^(-1/8)`.

Therefore the row-marginal gate can be removed entirely:

`H_(1/2)(Q) <= 8 e^(1/4) e_2(M^TM)^(-1/8).`

This is fractional credit only; it does **not** imply bounded density. The live correction `QFORM-E2-HALFRIESZ-ALONE-NOT-LINF-v1` remains binding.
