# account02/B11 — entropy-pivoted to QFORM: semi-cross indefinite smoothing

Run: `20260922T115006Z-account02-B11-qform-r18-7c1e`

Status: `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_THEOREM`; full QFORM conjecture remains OPEN.

## Control and correction status

The invocation began under a stale FEI task prompt, but fresh owner controls at `yspennstate/math-research-brain@46532ff524f78623e48eb66b2a0d0f2fc2b08fd4` and the later refresh `@a2c4bd773284b766962edde311da0d29382e5e85` put every slot on `QFORM-DENSITY-3EIG-20260922`, revision `2026-09-22.5`. FEI work was therefore stopped and no FEI mathematics was continued.

Consumed corrections:

- `QFORM-POINTWISE-DECAY-FALSE` — no law-uniform pointwise Fresnel decay is used.
- `QFORM-FIBER-SUP-DIMENSION-LOSS` — no fixed fiber-supremum localization is used.
- `QFORM-NO-INDEPENDENCE-AFTER-ROTATION` — no rotated spectral coordinates are declared independent.
- Fresh event `QFORM-CROSSMINOR-ALONE-FALSE`, source `math-research-brain@a2c4bd773284b766962edde311da0d29382e5e85:scheduled_tasks/work/shared/qform-density-2026-09-22/events/account02/B09/20260922T115241Z-account02-B09-QFORM-r1/QFORM-CROSSMINOR-ALONE-FALSE.json`. In particular, a nonsingular cross block alone is not treated as enough.

Assignment source: `math-research-brain@46532ff524f78623e48eb66b2a0d0f2fc2b08fd4:scheduled_tasks/work/shared/qform-density-2026-09-22/assignments/account02/B11.json`.

Relevant peer sources actually used:

1. account02/B15, canonical report `math-open-problems@d5392d73398e2811f58b612fb8f191aa79d8ee5e:proofnet24/QFORM-density/fleet-2026-09-22/account02/B15/20260922T110507Z-account02-B15-qform-pivot-r1/REPORT.md`: any invertible original-coordinate 3x3 principal block gives an affine conditional density bound `(2*pi+3*sqrt(3))/sigma_min`, and the flat Hadamard rank-three family shows one fixed principal triple can lose dimension.
2. account01/B08, canonical report `math-open-problems@fce159beaecf924a3e500dc7865ae61f8b35c932:proofnet24/QFORM-density/fleet-2026-09-22/account01/B08/20260922T114116Z-account01-B08-qform-r11/REPORT.md`: diffuse leverage `<=1/2` plus a separable one-coordinate residual phase gives a global bounded continuous density `<=3e`; its unpaid case is a genuinely nonseparable residual quadratic phase.
3. account03/B12 handoff at `math-research-brain@c5ad43d54757c7e55d5877ad5dc9c5fcdb536265:scheduled_tasks/work/shared/qform-density-2026-09-22/handoffs/account03/B12/account03-B12-20260922T114435Z-349dfcff7c.md`, which applies B15's principal-block theorem and records the same pair/triple-minor bridge.

The assigned partner account03/B11 had no QFORM handoff in the fresh `handoffs/account03` tree at the latest peer snapshot used before this report; no partner theorem is fabricated.

## Compact conditional route

For an indefinite three-direction block, the rank-two opposite-sign piece is allowed to retain its logarithmic singularity. The right target is not `L^infinity` for that rank-two piece but an exponent strictly above two. If its density lies uniformly in `L^3`, while the third square direction lies uniformly in `L^{3/2}`, Young's convolution inequality closes exactly at `L^infinity` because `1/3+2/3=1`.

The theorem below proves this mechanism for a genuinely rotated original-coordinate signature in which one coordinate is isotropic in the hyperbolic two-plane. It remains valid after conditioning arbitrary outside coordinates and arbitrary outside cross couplings.

## Lemma 1: semi-cross rank-two `L^3`

Let `X,Y` be independent real random variables with probability densities `f_X,f_Y` satisfying `0<=f_X,f_Y<=1`. Let `a!=0`, and let `alpha,r,s,c` be arbitrary real numbers. Define

`R = alpha X^2 + 2 a X Y + r X + s Y + c`.

Then `R` has a density `h` and

`||h||_3 <= 3 |a|^{-2/3}`.

### Proof

Condition on `X=x`. Except at the single point where `2ax+s=0`, the conditional law is an affine image of `Y`:

`R | (X=x) = (2ax+s)Y + beta(x)`

for a deterministic `beta(x)`. Its density `k_x` therefore satisfies

`||k_x||_3 = |2ax+s|^{-2/3} ||f_Y||_3 <= |2ax+s|^{-2/3}`,

because `int f_Y^3 <= int f_Y =1`.

Minkowski's integral inequality gives

`||h||_3 <= int f_X(x) |2ax+s|^{-2/3} dx`.

Write `x0=-s/(2a)`. Since `0<=f_X<=1` and `int f_X=1`, the bathtub principle for the symmetric decreasing weight `|x-x0|^{-2/3}` gives

`int f_X(x)|x-x0|^{-2/3} dx
 <= int_{-1/2}^{1/2} |u|^{-2/3} du
 = 6*2^{-1/3} = 3*2^{2/3}`.

Multiplying by `|2a|^{-2/3}` gives exactly

`||h||_3 <= 3|a|^{-2/3}`.

The possible zero conditional slope occurs for one `x` only and has zero `X`-probability because `X` has a density. This proves the claim.  QED.

### Why this is the rank-two logarithmic regime, not a hidden bounded branch

For `alpha=r=s=c=0`, `a=1/2`, and `X,Y` uniform on `[-1/2,1/2]`, `R=XY` has density

`h(t)=2 log(1/(4|t|))`, `0<|t|<1/4`,

so it is unbounded at zero. The lemma only claims uniform `L^3`, exactly the amount needed below.

## Lemma 2: one square is uniformly `L^{3/2}`

Let `Z` have density `f_Z<=1`, let `d!=0`, and let `u,v` be arbitrary real numbers. For

`S=d Z^2 + u Z + v`

the density `g` satisfies

`||g||_{3/2} <= 2 |d|^{-1/3}`.

### Proof

Complete the square and translate `Z`; translations preserve the hypotheses. Reflection handles `d<0`, so consider `d>0` and `S=d(Z-b)^2`.

For `s>0`, write `r=sqrt(s/d)` and

`F(r)=f_Z(b+r)+f_Z(b-r)`.

Then `0<=F<=2`, `int_0^infinity F(r)dr=1`, and

`g(s)=F(r)/(2dr)`, `ds=2dr dr`.

Hence

`||g||_{3/2}^{3/2}
 = (2d)^(-1/2) int_0^infinity F(r)^{3/2} r^{-1/2} dr`.

Since `F^{3/2}<=sqrt(2)F`, and the bathtub principle with `F<=2`, `int F=1` gives

`int F(r) r^{-1/2} dr <= 2 int_0^{1/2} r^{-1/2}dr =2sqrt(2)`,

we obtain

`||g||_{3/2}^{3/2} <= 2sqrt(2)|d|^{-1/2}`.

Taking the power `2/3` yields `||g||_{3/2}<=2|d|^{-1/3}`.  QED.

## Main theorem: singular-gap-free semi-cross indefinite certificate

Let `X_1,...,X_n` be independent real random variables with densities bounded by one, and let `A` be real symmetric. Suppose there are three distinct original coordinates, permuted as `(i,j,k)`, for which the principal block is

`A[{i,j,k}] = [[alpha,a,0],[a,0,0],[0,0,d]]`

with `a!=0` and `d!=0`. No condition is imposed on `A` outside this principal block or on cross couplings from these three coordinates to the remaining coordinates.

Then `Q=X^T A X` has a bounded continuous density and

`||p_Q||_infinity <= 6 |a|^{-2/3}|d|^{-1/3}`.

In particular, if `|a|>=1` and `|d|>=1`, then `||p_Q||_infinity<=6`.

The displayed 3x3 block is genuinely indefinite: its binary 2x2 block has determinant `-a^2`, hence one positive and one negative eigenvalue. If `d>0` its signature is `(+,+,-)`; if `d<0` its signature is `(+,-,-)`.

### Proof

Condition on every coordinate outside `{i,j,k}`. The remaining conditional quadratic is

`alpha X_i^2 + 2a X_iX_j + dX_k^2 + r X_i+sX_j+uX_k+c`,

where `r,s,u,c` depend on the conditioned outside values but `alpha,a,d` do not.

Because the original coordinates are independent, under this conditioning `(X_i,X_j)` remains independent of `X_k`, with all three one-dimensional densities still bounded by one. Let

`R=alpha X_i^2+2aX_iX_j+rX_i+sX_j`

and

`S=dX_k^2+uX_k`.

By Lemma 1, uniformly in the outside conditioning,

`||p_R||_3 <= 3|a|^{-2/3}`.

By Lemma 2,

`||p_S||_{3/2} <=2|d|^{-1/3}`.

The two conditional variables are independent, so Young's inequality gives

`||p_{R+S}||_infinity
 <= ||p_R||_3 ||p_S||_{3/2}
 <=6|a|^{-2/3}|d|^{-1/3}`.

Adding the conditional constant `c` only translates the density. Averaging the conditional densities over the outside coordinates preserves the same `L^infinity` bound, proving absolute continuity and the displayed estimate for the full `Q`.

For continuity: for each outside conditioning, `p_R in L^3` and `p_S in L^{3/2}`, so their convolution is continuous by translation continuity in `L^{3/2}` and Holder. The conditional densities are uniformly bounded by the same constant; dominated convergence therefore passes pointwise continuity through the outside mixture.  QED.

## Pure-cross sharpening

When `alpha=0`, one can exploit multiplicative Young convolution in logarithmic coordinates to show directly that, for independent shifted density-`<=1` variables,

`||p_{(X-b)(Y-c)}||_3 <=4`.

Indeed, on each sign quadrant set `F(u)=e^u f(e^u)` and `G(v)=e^v g(e^v)`. For the positive product density `h`, `h(e^s)=e^{-s}(F*G)(s)`. Therefore

`int_0^infinity h(t)^3dt = ||A*B||_3^3`,

with `A(u)=e^{u/3}f(e^u)` and similarly for `B`. Young with exponents `(3/2,3/2,3)` and the bound

`||A||_{3/2}^{3/2}=int_0^infinity x^{-1/2}f(x)^{3/2}dx <=2 sqrt(m_+)`

handles each sign component; Holder over the two signs gives the global constant `4`.

Consequently, for the exact cross-square normal form `2a(X-b)(Y-c)+d(Z-e)^2`,

`||p||_infinity <= 8|2a|^{-2/3}|d|^{-1/3}
 =2^{7/3}|a|^{-2/3}|d|^{-1/3}`.

This is a quantitative expression of how the third square removes the opposite-sign logarithmic singularity: the rank-two piece is uniformly `L^3`, the square is uniformly `L^{3/2}`, and the conjugate exponents land exactly in `L^infinity`.

## Exact falsifier: an arbitrary bounded spectral joint density is not enough

A route that rotates to the eigenbasis and then remembers only an `L^infinity` bound on the resulting three-dimensional joint density cannot prove the target.

Take the canonical signature form

`q(x,y,z)=x^2+y^2-z^2`.

Fix `delta>0` and `R>sqrt(delta)`. In cylindrical coordinates `r=sqrt(x^2+y^2)`, choose `L>0` so that the compact set

`E={R<=r<=R+L, z>0, 0<=r^2-z^2<=delta}`

has volume exactly one. Such `L` exists because the volume is continuous, starts at zero at `L=0`, and tends to infinity with `L`.

Then `g=1_E` is a probability density with `||g||_infinity=1`. Under the change of variables `q=r^2-z^2`,

`dV = r dr dtheta dq/(2sqrt(r^2-q))`,

so the pushforward density is

`p_q(q)=pi [sqrt((R+L)^2-q)-sqrt(R^2-q)] 1_[0,delta](q)`.

Its integral over `[0,delta]` is one. Therefore

`||p_q||_infinity >= 1/delta`.

As `delta->0`, this diverges although the input joint density is bounded by one and the quadratic form has the exact three eigenvalues `(+1,+1,-1)`. This is NOT a counterexample to the owner target because `g` is not a product of independent one-dimensional input laws. It is a rigorous counterexample to every argument that discards the product/separable structure after spectral projection and keeps only a bounded three-dimensional joint density.

This falsifier is consistent with, and strengthens the operational meaning of, the existing `QFORM-NO-INDEPENDENCE-AFTER-ROTATION` correction and the fresh `QFORM-CROSSMINOR-ALONE-FALSE` event. The third direction only regularizes when its relation to the original independent coordinates is actually retained.

## Relation to peer results

- B15 covers every invertible original-coordinate 3x3 principal block by a bound proportional to `1/sigma_min`. The semi-cross theorem above uses more algebraic structure and removes any dependence on the potentially tiny singular value: `alpha` can be arbitrarily large while the bound remains controlled by `|a|` and `|d|` only.
- account01/B08 proves a global diffuse theorem when the residual quadratic phase is separable in the original coordinates. The cone-shell falsifier above shows why one cannot replace that separability by a mere `L^infinity` bound for the spectral projection density. The present semi-cross theorem supplies a complementary localized/heavy-coordinate mechanism that still tolerates arbitrary outside cross couplings by conditioning.
- The B09 correction shows a cross minor by itself is insufficient; the theorem here does not reuse that false premise. It adds the third square direction and makes the regularization quantitative through `L^3 * L^{3/2} -> L^infinity`.

## First unpaid implication

The clean next target is the following rank-two statement.

**BINARY-INDEFINITE-L3.** For independent real `X,Y` with densities `<=1`, and every affine nondegenerate indefinite binary quadratic

`q(X,Y)=alpha X^2+2aXY+beta Y^2+rX+sY+c`,

with discriminant `D=a^2-alpha beta>0`, prove

`||p_q||_3 <= C D^{-1/3}`

for one universal `C`.

The scaling exponent `D^{-1/3}` is forced: multiplying the quadratic by `lambda` multiplies `D` by `lambda^2` and the `L^3` density norm by `|lambda|^{-2/3}`. Lemma 1 proves this statement with `C=3` on the full semi-cross face `beta=0` (and, by swapping variables, on `alpha=0`).

If BINARY-INDEFINITE-L3 is proved, then every original-coordinate 3x3 principal block that splits as an arbitrary indefinite 2x2 block plus one uncoupled square direction immediately has a bounded density by the same `L^3 * L^{3/2}` argument. The subsequent genuinely three-way issue is to tolerate nonzero couplings of the third selected coordinate into that hyperbolic plane, or replace fixed-triple selection by a determinant-aggregate mechanism in the diffuse regime.

That is the first essential missing implication exposed by this run; the full conjecture is not claimed.

## Status

`ESSENTIAL_STEP_APPLIED`.

No finite census or numerical simulation is used as closure. No fixed pointwise Fourier decay, no arbitrary spectral-projection independence, and no cross-minor-alone premise is used.
