Model actually available to this worker: **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is unavailable, so reasoning level is **UNVERIFIED**; GPT-6/maximum is prompt-only and is not claimed.

# PROB10-06 idea before code — self-consistent mean upper bound inside the branch-gap derivative

Status entering this bounded iteration: **PARTIAL / OPEN parent**. The immediate predecessor proves, pending independent audit, the restricted `{2,3}` no-leaf statement `p>=3/4 => ell'_lambda<0` through parent bias `lambda=12/5`, with all-mixture endpoint still `1.85527`. Its corrected finite-depth derivative passage is preserved in `artifacts/prob10_2026-09-20/PROB10-06/20260920T1400Z_finite_depth_derivative_passage_correction.md`.

The present run will not merely rerun that checker. The precise remaining loss I attack is the predecessor's replacement of the annealed escape mean `mu=E B` by the pathwise essential supremum `u=(3-lambda)/3` in the source term and in the constant part of the branch-gap derivative.

## New route A — close a scalar annealed mean supersolution and feed it twice

For the family

`P(nu=2)=1-p`, `P(nu=3)=p`,

with `lambda>2`, the escape recursion is

`B = S/(lambda+S)`, `S=sum_{i=1}^nu B_i`.

For fixed degree `k`, `s -> s/(lambda+s)` is increasing and concave. Hence, writing `mu=E B`,

`E[B | nu=k] <= k mu/(lambda+k mu)`,

and therefore

`mu <= Phi_{lambda,p}(mu)`

with

`Phi_{lambda,p}(x)=(1-p) 2x/(lambda+2x)+p 3x/(lambda+3x)`.

Since `Phi` is increasing in `x`, decreasing in `lambda`, and increasing in `p`, any rational supersolution of this scalar map gives a rigorous boxwise upper bound on `mu`. Starting from the already proved pathwise upper `u=(3-lambda)/3` and iterating the worst-corner map should give a decreasing exact rational supersolution whenever the box has `p<1`; subdivision keeps the p-coupling instead of replacing all mixtures by p=1.

The same `mu` upper bound should improve **two** places in the branch-gap proof:

1. In `-J' <= 2 eta mu/a^2 + 2 mu^2/a^3`, after dividing by `c_3>=mu/Dmax`, the constant term becomes `2 mu/a^3` instead of `2u/a^3`.
2. The derivative source map `h_lambda(s)=s/(lambda+s)^2` is increasing and concave on the full relevant support because for `lambda>=12/5`, `0<=s<=3-lambda<lambda<2lambda`. Thus

   `E[h_lambda(S_k)] <= h_lambda(k mu)`,

   so the source term `A` in `eta<=A/(1-rho)` can be replaced by

   `A_mu=(1-p) 2mu/(lambda+2mu)^2 + p 3mu/(lambda+3mu)^2`.

This retains the already-rigorous reciprocal-moment denominator contraction `rho<1` but lowers both the forcing and constant pieces of the branch-gap bound. The intended theorem target is a strict extension beyond `lambda=12/5` for the same unresolved high-mixture family `p>=3/4`, with a certified sign margin and explicit truncation factor.

## New route B — symmetrize the exact differentiated gap before dropping negative derivative terms

Write `a=lambda-1`, `D_2=a+B_0+B_1+B_2`, `D_3=D_2+B_3`, and

`j=B_0 B_3/(D_2D_3)`.

The predecessor bounded every derivative denominator separately. Before doing that, expand `-j'` and use exchangeability of `B_0,B_1,B_2` to average the first numerator derivative across the first three branches. If `V=U_0+U_1+U_2` and `S_2=B_0+B_1+B_2`, exact symmetrization gives the first-three derivative contribution

`(1/3) E[ B_3 V/(D_2D_3) * (a/D_2 - S_2/D_3) ]`,

while the fourth-branch contribution collapses exactly to

`E[B_0 U_3/D_3^2]`.

This exposes cancellations hidden by `D'_2,D'_3<=1`. I will test whether the coefficient of `V` can be bounded sharply enough (possibly by its positive part) to improve route A. If not, the exact obstruction will be recorded rather than silently dropped.

## New route C — second-moment/variance refinement of the concave source forcing

Route A uses only `mu`. A materially different refinement is to propagate an upper bound on `m_2=E[B^2]` from the same recursion and apply a second-order concavity inequality to `h_lambda(S_k)`. Because `h''<0` on the whole relevant support, a certified positive variance of `S_k` should reduce the forcing below `h(k mu)`. I will derive whether a closed two-moment supersystem is available without introducing an uncontrolled third moment. If closure fails, I will record the exact point of failure.

No finite simulation is being treated as source progress. Any successful restricted theorem remains **PARTIAL / OPEN parent** until the full no-leaf source interval is proved and independently validated.