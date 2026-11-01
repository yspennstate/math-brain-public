# Audit of `QFORM-RULED-HALFLINE-C0-v1`

Canonical report: same run `REPORT.md`, commit `5345b4abcc61d04ee522f57ede6b1aa66946f8d1`.

## A. Endpoint/version issue in the uniform-limit argument

An `L^infinity` density is only defined almost everywhere, so continuity at the single point `s=0` should not be inferred by comparing an arbitrary rough density version pointwise to the smooth approximants. The rigorous construction is instead pairwise.

For the cap-preserving smooth compact approximants `F_k=prod_i f_i^(k)`, let `r_k^+` be the canonical ruled representative defined by the smooth formula

`r_k^+(s)=(1/2) int_0^(2pi) int_R rho_k(sqrt(s)e_theta+t(e_theta^perp+e_3)) dt dtheta`, `s>=0`.

Every `r_k^+` belongs to `C_0([0,infinity))`. For two indices `k,l`, telescope the original-coordinate marginals and apply the proved signed stability estimate from REPORT Section 3. If

`delta_i(k,l)=||f_i^(k)-f_i^(l)||_1<=1`, then

`||r_k^+-r_l^+||_(Linf,ess) <=20 sqrt(2) sum_i sqrt(delta_i(k,l))`.

The difference `r_k^+-r_l^+` is continuous on `[0,infinity)`. For a continuous function, its essential supremum equals its actual supremum. Hence

`||r_k^+-r_l^+||_(sup,[0,infinity)) <=20 sqrt(2) sum_i sqrt(delta_i(k,l)) ->0`.

Thus `(r_k^+)` is uniformly Cauchy in the Banach space `C_0([0,infinity))`; denote its uniform limit by `r_*^+ in C_0([0,infinity))`.

Meanwhile the product input densities converge in `L1`, and restriction to `{q>=0}` followed by deterministic pushforward contracts total variation. Therefore the output submeasures converge in total variation to the rough positive-sheet output. Since `r_k^+ -> r_*^+` uniformly (hence locally in `L1`), `r_*^+` is a density of that limiting output measure. This constructs the canonical half-line-continuous representative without ever assigning a pre-existing rough density a value at the endpoint.

The smooth height `||r_k^+||_infinity<=pi sqrt(2)` passes to the uniform limit unchanged.

## B. Positivity improvement check

Let `a=f-g`, `delta=||a||_1<=1`, and let `T` denote the positive-sheet output operator with all other marginals fixed. For any finite measurable partition `(E_l)` of a Borel set `E`,

`sum_l |T a(E_l)| <= sum_l T|a|(E_l)=T|a|(E)`.

Taking the supremum over partitions gives the total-variation measure inequality

`|T a| <= T|a|`.

Since `0<=|a|<=1` and `int|a|=delta`, the completed fleet02/B15 submass theorem applies once, giving

`||d(T|a|)/dt||_infinity <=20 sqrt(2) sqrt(delta)`.

Therefore

`||d(Tf-Tg)/dt||_infinity <=20 sqrt(2) sqrt(delta)`.

No cancellation assumption is needed; the gain over separate positive/negative splitting is purely the positivity of `T`.

## C. Exact constants in the shifted-uniform test

For `f_0=1_[0,1]` and `f_epsilon=1_[epsilon,1+epsilon]`, `0<=epsilon<=1/2`,

`delta=||f_epsilon-f_0||_1=2 epsilon`.

Thus

`20 sqrt(2) sqrt(delta)=40 sqrt(epsilon)`.

Interpolation with `||p_epsilon-p_0||_1<=2 epsilon` gives

`||p_epsilon-p_0||_2 <= (20 sqrt(2))^(1/2)(2 epsilon)^(3/4)=4 sqrt(5) epsilon^(3/4)`.

## D. Square-smoother translation identity

For `h(u)=(2 sqrt(u))^(-1)1_(0,1)(u)` and `0<=a<=1`, the overlap of `h` and its translate `tau_a h` has pointwise minimum `h(u)` on `[a,1]`, with mass

`int_a^1 h(u)du=1-sqrt(a)`.

Since both are probability densities,

`||tau_a h-h||_1=2[1-(1-sqrt(a))]=2 sqrt(a)`.

Translation invariance gives the same formula for `-1<=a<=0` with `sqrt(|a|)`.

All constants in REPORT equations (6.3), (6.5), (7.3), and (7.4) follow.

## E. Scope audit

- The half-line `C_0` theorem concerns the majority-sheet submeasure for the isotropic signature `(2,1)` frame; it is not the missing two-sheet theorem.
- The exact `Q=2XY+Z^2` application becomes a full-output theorem only because the chosen source laws are nonnegative, so `Q>=0` almost surely.
- The additional `W^2` smoother is a disjoint original-coordinate block; no rotated-coordinate independence is used.
- The full three-large-eigenvalue conjecture remains open.
