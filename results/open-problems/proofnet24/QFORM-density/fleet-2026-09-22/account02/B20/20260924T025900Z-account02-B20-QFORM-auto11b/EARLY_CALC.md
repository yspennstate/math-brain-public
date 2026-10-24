# Early calculation — active-localized carrier is not itself a physical star

Run: `20260924T025900Z-account02-B20-QFORM-auto11b`.

Working source: fresh B20 predecessor `math-open-problems@f8623c2ad724913062a5c86a21f0714a94bab3c0`, plus account01/B02 r38/r43 and newest compatible account03/B20 r44. Full QFORM remains open.

## Tuned leverage peel

In the r43 finite-carrier state

`A=D+R_0+E_0`, `rank(R_0)<=42`, `s_3(R_0)>gamma0=0.8749992111292801`, `||E_0||_F<eta0=7.888707199262311e-7`,

repeat B20's orthogonal low-action peel, but invoke the tunable r38 localization theorem with localization parameter

`eta_loc=2/3`

instead of the earlier `1/2`, while keeping the low-action threshold `a=1/64`.

At a stage after `m<=39` low-action peels, Frobenius orthogonality gives

`t_m:=||R_0-R_m||_F < sqrt(2m)/64 <= sqrt(78)/64 = 0.13799626353637262`,

hence

`s_3(R_m)>gamma0-t_m`, `||E_m||_F<eta0+t_m`.

For `eta_loc=2/3`, the tunable r38 crossing coefficient is

`c_loc=sqrt[(eta_loc/4)(1/2-eta_loc/4)]=1/sqrt(18)`.

Therefore every diffuse call has

`sigma_m >= (gamma0-sqrt(78)/64)/sqrt(18) - (eta0+sqrt(78)/64)
          = 0.03571620825871366... >0`.

The completed physical-E3 receiver then pays the full law by

`||p_Q||_infinity <= C3/sigma_m < 289.647`,

with `C3=10.3450832321475...`.

If the diffuse exit never fires, the rank-drop argument again forces an active localized direction before rank falls below three: at some stage there is a unit carrier vector `u` with

`||K_m u||>=1/64`

and a literal heavy-coordinate set

`H={i: ell_i>eta_loc^2/(4r_m)}={i: ell_i>1/(9r_m)}`

such that

`||(V_m u)_H||_2^2>1/3`, `|H|<=9r_m^2<=15876`.

Every coordinate in this H has current carrier-range leverage

`ell_i>1/(9r_m)>=1/378`.

This is a stronger physical-leverage conclusion than the earlier generic `>1/2`-mass / `28224`-coordinate certificate, while also improving the worst diffuse Fourier payment from `<479.633` to `<289.647`.

## Exact obstruction to the proposed direct-star inference

The certificate above does **not** imply that the localized active direction produces any nonzero coefficient of the actual matrix A touching its localized coordinates.

Take N=256 and three orthonormal Walsh columns `v_1,v_2,v_3` on coordinates `2,...,257`, each entry of modulus `1/16`. Put

`B=v_1v_1^T+v_2v_2^T-v_3v_3^T`.

Then `B` has nonzero spectrum `{1,1,-1}`, each spectral leverage is `3/256<1/2`, and `|B_ii|=1/256<1/64` on its support. On an extra coordinate `e_1`, let `gamma=1/16` and define

`R_0=gamma e_1e_1^T direct_sum B`, `D=-gamma e_1e_1^T`, `E_0=0`.

Thus

`A=D+R_0+E_0=0 on coordinate 1 direct_sum B`,

so the exact target holds (`s_3(A)=1`), `rank(R_0)=4<=42`, `s_3(R_0)=1`, `||D||_op=1/16<1/8`, and the carrier vector `e_1` is completely localized and has action `gamma=1/16>1/64`. Yet every actual coefficient of A touching coordinate 1 is exactly zero. Hence any implication

`active localized carrier direction => actual physical star/pair touching that localization set`

is false under the current certificate alone. The missing information is cancellation against the allowed physical diagonal D (and, in the live theorem, the retained E tail).

This family is not a QFORM counterexample. The owner-pinned Fresnel--Brascamp--Lieb Theorem F applies directly to B: the three eigenvalues have product one, the Gram is I_3, and every original-coordinate leverage is `3/256<1/2`, giving `||p_{X^TAX}||_infinity<=12` for every independent cap-one product law.

The next proof mechanism must therefore be cancellation-safe: either measure physical hub/cross action after the diagonal has been accounted for, or quotient a diagonal-cancelled localized direction and recover the remaining three-mode resource. Simply extracting a coordinate from the old localization set is invalid.
