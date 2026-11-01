SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B06, 2026-09-23T09:21:38Z.
attacking: the fully coupled nonzero scalar/dependent-pair branch: keep the original scalar independent, retain dependence inside the product-projection pair, and pay the curved discriminant by the completed rank-two half-Riesz theorem.

# Early substantive checkpoint — coupled nonzero-pivot curved kernel

Full QFORM remains OPEN. This checkpoint records the first completed calculation of the run, before the final write-up.

## Candidate theorem already proved algebraically

Let `X` be a real variable with density cap `L_X`, independent of a cap-one product vector `Z=(Z_1,...,Z_m)` and an auxiliary source `W`. Let `u,v in R^m` be linearly independent and set

`U=u.Z`, `V=v.Z`, `G=||u||^2||v||^2-(u.v)^2>0`.

Let `H=H(Z,W)` be arbitrary measurable, `R=R(W)` arbitrary measurable, `ell in R^m`, and let `gamma,k,delta,beta` be nonzero. Put

`Y=gamma X+H`,
`Q=delta Y^2+2k UY+beta V^2+ell.Z+R`.

Then the completed rank-two affine half-Riesz theorem at
`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a:proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`
gives

`||p_Q||_infinity <= 128 (L_X/|gamma|) [k^2 |delta beta| G]^(-1/4).`

If `ell` lies in `span{u,v}` (in particular `ell=0`), the source theorem's sharper in-range constant gives `16 sqrt(30)` in place of `128`.

### Essential calculation

Condition on `(Z,W)=(z,w)`. The conditional density of `Y=gamma X+H(z,w)` is at most `L_X/|gamma|`. For fixed `u0=u.z`, `v0=v.z`, the scalar map

`y -> delta y^2+2k u0 y + beta v0^2+ell.z+R(w)`

has two roots when

`D=k^2u0^2+delta[t-beta v0^2-ell.z-R(w)]>0`,

and the derivative magnitude at either root is `2 sqrt(D)`. Therefore

`p_{Q|Z,W}(t|z,w) <= (L_X/|gamma|) D_+^(-1/2)`.

Hence

`p_Q(t) <= (L_X/|gamma|) E | k^2 U^2-delta beta V^2-delta ell.Z - s_W |^(-1/2)`,

where `s_W=delta(R(W)-t)`. For each fixed `W=w`, choose an orthonormal basis of `span{u,v}`. In those two projection coordinates the quadratic matrix is

`Lambda=k^2 aa^T-delta beta bb^T`

with

`|det Lambda|=k^2 |delta beta| det Gram(u,v)=k^2 |delta beta| G`.

The rank-two affine half-Riesz theorem is uniform in the affine coefficient and scalar shift, proving the displayed bound. `H` disappears from the discriminant; no conditional density of any projected coordinate is used.

## Sign-sensitive fleet04 application already identified

For `delta beta<0`, after reflecting the output if needed take `delta>0`, `beta<0` and complete

`Q=delta(Y+kU/delta)^2 + [beta V^2-(k^2/delta)U^2]`

in the zero-affine specialization. The pair `(U,V)` is a linear image of a two-dimensional orthogonal product projection, whose joint density cap is at most `2/sqrt(G)`. The bracket is definite, so its density cap is

`M_R <= 2 pi sqrt(delta)/( |k| sqrt(|beta|G) )`.

Applying the completed fleet04/B18 dependence-safe square theorem
`yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3:proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B18/20260922T113729Z-fleet04-B18-qform-r1/REPORT.md`
at the actual completed-square identity yields the sharper bound

`||p_Q||_infinity <= 2 sqrt(2 pi) (L_X/|gamma|) [k^2 |delta beta| G]^(-1/4)`.

The designated `fleet04/B06` canonical QFORM directory is currently absent, so no result from that exact partner is being invented; work continues asynchronously with this compatible completed fleet04 theorem.

## Remaining gap

The estimate is genuinely nonzero-pivot and blows like `|delta|^(-1/4)`. It therefore does not pay the exact-null fully coupled case in which the smoothing square shares the same product bank as the dependent pair. That exact boundary remains the next obstruction after this theorem is written and checked.
