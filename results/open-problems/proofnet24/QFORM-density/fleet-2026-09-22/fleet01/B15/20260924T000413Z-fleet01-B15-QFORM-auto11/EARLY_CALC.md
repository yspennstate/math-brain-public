SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B15, 2026-09-24T00:04:13Z.
attacking: a general C0 regularity compiler from Lp residual control, and a source-valid application to the latest fleet02/B15 collective Schur and grouped-obstruction results without using continuity to pay height.

# Early substantive calculation

Status: supporting lemmas; full QFORM remains open.

## 1. An L^p-to-C0 square-kernel compiler

Let `(R,V)` have a joint probability density `K(r,v)`. Assume that for almost every `r`, `K(r,.) in C_0(R)`, and that

`0 <= K(r,v) <= g(r)`

for a probability density `g in L^p(R)` with `p>2`. For `b!=0`, put `T=R+bV^2`. Then `T` has a density in `C_0(R)` and

`||p_T||_infinity <= 2 sqrt(2(p-1)/(p-2)) |b|^(-1/2) ||g||_p^[p/(2(p-1))].`      (1)

Proof calculation. Let `a=|b|`, `sigma=sign(b)`. The exact one-dimensional change of variables gives

`p_T(t)=1/(2 sqrt(a)) int_{sigma(t-r)>0}`
` [K(r,+sqrt(|t-r|/a))+K(r,-sqrt(|t-r|/a))]/sqrt(|t-r|) dr.`

Hence

`p_T(t) <= a^(-1/2) int_0^infinity g(t-sigma s) s^(-1/2) ds.`

Let `p'=p/(p-1)` and `alpha=1/2-1/p=(p-2)/(2p)`. Splitting at `L>0`, Holder gives

`near <= A_p ||g||_p L^alpha`,
`A_p=[2(p-1)/(p-2)]^((p-1)/p),`

while probability normalization gives `far<=L^(-1/2)`. Choose

`L=(A_p ||g||_p)^(-p/(p-1))`.

The two pieces are equal and (1) follows. At `p=3` this is exactly

`||p_T||_infinity <=4 |b|^(-1/2)||g||_3^(3/4).`

For continuity, split the exact density formula into `|t-r|<=delta` and its complement. The near piece is uniformly `O(||g||_p delta^alpha)`. On the complement, `K(r,.) in C_0` and dominated convergence apply. For vanishing at infinity, on a fixed near window use the translating local `L^p` norm of `g`, which tends to zero because `g^p in L^1`; the far tail is at most `L^(-1/2)`. Thus `p_T in C_0`.

The threshold `p>2` is genuine for this abstract compiler. There is a probability density `g in L^1 cap L^2` with `g(-u) asymp u^(-1/2)/log(1/u)` near `u=0+`. If `V` has triangular `C_0` density `(1-|v|)_+`, independent of `R~g`, then the density of `R+V^2` at zero contains `int_0 g(-v^2)(1-v)dv`, which diverges like `int dv/[v log(1/v)]`. So an `L^2` envelope alone cannot imply an endpoint height bound.

## 2. Every indefinite physical pair has finite L^p density, p>1

Use the completed physical-pair logarithmic envelope from
`yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`,
`proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`.
For an invertible indefinite ORIGINAL-coordinate pair `B`, put

`D=|det B|`, `kappa=sigma_min(B)`.

For any affine perturbation and any cutoff `rho>0`, that theorem decomposes the output density into a far subdensity with sup at most `2sqrt(2)/rho` and a near subdensity bounded by

`D^(-1/2) log_+( 2 rho^2/(kappa |t-t0|) ).`

Therefore, for every `p>1`,

`||p_pair||_p <= A rho^(-(p-1)/p)+B_p rho^(2/p),`                 (2)

where

`A=(2sqrt(2))^((p-1)/p),`
`B_p=D^(-1/2)[4 Gamma(p+1)/kappa]^(1/p).`

Indeed the far subdensity has mass at most one, and

`int_R log_+(C/|u|)^p du=2 C Gamma(p+1)`.

The minimizing cutoff is

`rho_*=[(p-1)A/(2B_p)]^[p/(p+1)]`,

and consequently

`||p_pair||_p <= M_p(D,kappa)`
` :=(p+1)/2 * A^[2/(p+1)] * [2B_p/(p-1)]^[(p-1)/(p+1)].`          (3)

At `p=3`, this simplifies to

`||p_pair||_3 <= 4*3^(1/6) D^(-1/4) kappa^(-1/6).`                (4)

Equations (1) and (4) are the intended regularity bridge for a fully coupled three-coordinate physical block. No spectral-coordinate independence or law-uniform pointwise quadratic Fourier decay is used.
