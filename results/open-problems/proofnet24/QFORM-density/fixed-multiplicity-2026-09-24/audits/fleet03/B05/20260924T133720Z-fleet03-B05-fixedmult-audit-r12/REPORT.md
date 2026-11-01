SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B05, 2026-09-24T13:37:20Z.

attacking: product-projection/coarea interfaces in the fixed-multiplicity candidate, then the terminal `s_16`, `r=4` determinant-volume obstruction.

# fleet03/B05 fixed-multiplicity audit r12

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924` (later owner objective; it supersedes the older free-form three-eigenvalue assignment for this invocation).

Pinned baseline mathematical source:

- repository: `yspennstate/math-open-problems`
- baseline source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`
- manuscript blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`
- manuscript SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`
- current source path: `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`

## Verdict on the 17-eigenvalue candidate

**PASS in this run's complete textual audit, with one nonfatal wording repair in the product-projection proof.** I found no fatal mathematical defect in the claimed theorem

\[
s_{17}(A)\ge s>0
\quad\Longrightarrow\quad
\|p_{X^TAX+b^TX+c}\|_{\infty,\mathrm{ess}}
\le 10^4K^2/s
\]

for independent arbitrary real coordinate densities bounded by `K`.

This is an independent worker audit, not formal verification or journal peer review. It does not solve the unrestricted three-large-eigenvalue conjecture and it does not prove continuity on the pivot branches.

The supplementary package gap reported in my preceding run is now **resolved** on current `master`: `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, and `checks.json` are all present. The new finite checker reports PASS on 534 exact interpolation seeds, 18 exact volume comparisons, 240 numerical Schur-threshold cases, and 30 graph-weight cases. These checks do not replace the analytic proof.

## Product-projection and exceptional-slice audit

### Product projections — PASS with wording repair

For `U^TU=I_d`, completing to `(U,W)` and writing `b_i=|w_i|^2`, geometric Brascamp--Lieb gives

\[
p_{U^TX}(y)\le \prod_{b_i>0}b_i^{-b_i/2}.
\]

After dropping rows with `b_i=0`, the final entropy line should be read as

\[
\sum_{b_i>0}(-b_i\log b_i)
\le \sum_{b_i>0}(1-b_i)
\le \sum_i(1-b_i)=d,
\]

rather than as an equality on the restricted index set. Thus

\[
\boxed{\|p_{U^TX}\|_\infty\le e^{d/2}.}
\]

The statement and constant are unchanged.

### Designated partner result applied to an actual inequality

The completed `fleet04/B05` audit independently reconstructed the same rough-law product-projection bound and the definite/hyperbolic coarea changes of variables. I used its product-projection result at the exact scalar Fourier-power step feeding the determinant receiver.

For a cap-one probability density `f`, `p>=2`, and `m=floor(p/2)>=p/4`,

\[
\int |\widehat f(t)|^pdt
\le \int |\widehat f(t)|^{2m}dt.
\]

The latter integrand is the characteristic function of

\[
S_m=\sum_{j=1}^m(X_j-X'_j).
\]

The coefficient vector on the `2m` original independent coordinates has Euclidean norm `sqrt(2m)`. Applying the partner-validated one-dimensional projection inequality gives

\[
p_{S_m}(0)\le \frac{\sqrt e}{\sqrt{2m}}.
\]

Fourier inversion at zero is legitimate because `|\widehat f|^{2m}` is integrable (`|\widehat f|<=1` and Plancherel handles the square). Hence

\[
\boxed{
\int_{\mathbb R}|\widehat f(t)|^pdt
\le \frac{2\pi\sqrt e}{\sqrt{2m}}
\le \frac{2\pi\sqrt{2e}}{\sqrt p}.
}
\]

This is the actual inequality used in the graph Brascamp--Lieb/determinant theorem and therefore in the order-five density receiver below.

### Definite and hyperbolic pairs — PASS

For a literal original-coordinate definite pair with joint density cap `M`, deterministic translation and the elliptic coarea Jacobian give

\[
\|p_q\|_\infty\le \pi M/\sqrt{|\det B|}.
\]

For an indefinite literal pair with independent cap-one coordinates and `D=|det B|`, the hyperbolic charts have Jacobian `1/(2sqrt D)` and give, away from the critical value,

\[
p_q(z)\le D^{-1/2}\left(6+\log_+\frac{16\sqrt D}{|z-v|}\right).
\]

The critical fiber is a union of affine lines and is planar-null. Downstream conditioning is used only through nonnegative output test functions and Tonelli. Therefore a conditioning-dependent critical value is not an illicit pointwise exceptional slice and no conditional density cap is inferred from an unconditional projection.

### Remaining baseline chain — PASS

I rechecked the Fourier/Riesz normalizations, Schur spectral count, nonsymmetric singular-value perturbation, geometric BL regularization, decoupling powers, determinant exponent `-1/8`, volume sampling, `rank R<=3r` versus `rank R[L,L]<=r`, strict diagonal-dominance contradiction, random cut, truncated/full half-potential transition, pivot branch exhaustion, and final scaling. I found no contradiction.

## New theorem: terminal `s_16` seed-mass dichotomy

This run adds a quantitative consequence to the current `17 -> 16` obstruction.

Use the manuscript constants

\[
\eta=10^{-2},\qquad \kappa=80^{-2}=1/6400.
\]

Assume the normalized **no-pivot** chamber

\[
A=A^T,\qquad s_{16}(A)\ge1.
\]

The already-proved `k=4` spectral-to-volume proposition applies (because `s_16>=s_13`) and gives

\[
V_4(A)\ge\kappa^4.
\tag{1}
\]

For an ordered disjoint nonsingular four-seed `B=A_{S,T}`, let

\[
w(B)=|\det B|^2,
\]

and, with `L=[n]\setminus(S\cup T)` and

\[
P=A_{\cdot,T}B^{-1}A_{S,\cdot},
\]

define the completion residual currency

\[
q(B)=\|\operatorname{off}(A_{L,L}-P_{L,L})\|_F^2.
\]

The bordered determinant identity gives, seed by seed,

\[
w(B)q(B)
=
\sum_{\substack{\ell,m\in L\\\ell\ne m}}
\det A_{S\cup\{\ell\},\,T\cup\{m\}}^2.
\tag{2}
\]

Consequently

\[
\boxed{\sum_Bw(B)q(B)\le25V_5(A),}
\tag{3}
\]

because each ordered disjoint order-five minor has at most `5^2=25` predecessor four-seeds.

Now use the completed terminal determinant-escalation theorem of `fleet01/B09`. If

\[
q(B)\le1/256,
\]

then there is another disjoint four-seed `B'` satisfying

\[
w(B')\ge R^2w(B),
\qquad
R=22.6532460869\ldots,
\qquad R^2=513.1695582735\ldots.
\tag{4}
\]

Iterate (4) while the residual remains at most `1/256`. There are only finitely many four-seeds and the weight strictly increases by a factor greater than one at every step, so the iteration terminates at a seed `C` with

\[
q(C)>1/256.
\]

Applying (2) to this terminal seed gives

\[
V_5(A)\ge w(C)q(C)>w(C)/256.
\tag{5}
\]

Therefore every four-seed obeys the following two-tier anti-concentration bound:

\[
\boxed{
q(B)>1/256\implies w(B)<256V_5,
}
\tag{6}
\]

and

\[
\boxed{
q(B)\le1/256\implies w(B)<\frac{256}{R^2}V_5.
}
\tag{7}
\]

Let

\[
x:=V_5/V_4.
\]

Then (3), (6), and (7) imply

\[
\boxed{
\frac{\sum_{q(B)>1/256}w(B)}{V_4}<6400x,
}
\tag{8}
\]

while each low-residual seed carries less than

\[
\boxed{
\frac{w(B)}{V_4}<\frac{256x}{R^2}.
}
\tag{9}
\]

### Quantitative branch closure / survivor

Fix any `0<theta<1`.

If

\[
x\ge\theta\kappa,
\]

then by (1)

\[
V_5\ge\theta\kappa^5.
\]

The random-cut and order-five Fourier receiver therefore give the continuous density bound

\[
\boxed{
\|p_Q\|_\infty
\le800e\,\theta^{-1/10}.
}
\tag{10}
\]

Thus a genuinely unpaid `s_16` terminal survivor may be assumed to have `x<theta kappa`. In that case (8) says at least `(1-theta)V_4` of the determinant-squared mass lies on low-residual seeds, and (9) says each such seed has mass fraction less than

\[
\frac{\theta}{25R^2}.
\]

Hence the number of nonzero low-residual ordered four-seeds is strictly larger than

\[
\boxed{
25R^2\frac{1-\theta}{\theta}.
}
\tag{11}
\]

For the concrete choice `theta=1/2`, either

\[
\boxed{\|p_Q\|_\infty<800e\,2^{1/10}<2331}
\]

with a continuous density, or else **more than 12,829** low-residual ordered four-seeds are forced (hence at least 12,830), together carrying more than half of `V_4`; each carries less than

\[
\boxed{3.898\times10^{-5}\,V_4.}
\]

This is a new dimension-free sharpening of the terminal obstruction: the unpaid chamber is not merely `rank=4` saturation. It is a highly **determinant-volume-diffuse family of many low-residual physical seeds**.

## Precise missing factor for `17 -> 16`

The remaining implication is now quantitative. The determinant-escalation map sends every low-residual seed to a seed with at least `R^2>513` times its determinant-squared weight. What is missing is a dimension-free control on the **weighted preimage multiplicity** of that map, or an aggregate coarea/Plancherel receiver that spends the many-seed mass before selecting one seed.

For example, in the `theta=1/2` survivor, if one could choose the escalation map so that every target seed had at most `N<=256` low-residual predecessors, then

\[
\sum_{\text{low }B}w(B)
\le \frac{N}{R^2}V_4
<\frac12V_4,
\]

contradicting the `>V_4/2` low-residual mass forced above. Thus a preimage bound of **256** (or a corresponding weighted bound) would already close the `s_16` terminal chamber. No such bound is proved here; a target seed can a priori receive predecessors from many different four-sets.

Equivalently, the next B05 coarea obligation is:

> convert the determinant-squared measure supported on the many low-residual original-coordinate four-seeds into either a leverage-diffuse physical crossing (where the completed order-four endpoint applies) or a direct aggregate coarea/Plancherel estimate, without a dimension-dependent maximum/minor selection.

This is the precise missing factor identified in this run.

## Scope and status

- Fixed-multiplicity `s_17` theorem: **PASS in this run's independent textual audit**; no fatal defect found.
- New seed-mass dichotomy (2)--(11): **proved supporting theorem** under normalized no-pivot `s_16>=1`.
- Universal `s_16` theorem: **OPEN**.
- Full three-large-eigenvalue conjecture: **OPEN**.
- Full-target continuity: **OPEN**; continuity is obtained in the order-five branch (10), not in all pivot branches.
- Execution/memory status: `WITHOUT_VERIFIED_BRAIN`.
