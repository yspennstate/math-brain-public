# PROB10-06 idea before verification: effective-offspring covariance route

Actual runtime self-identification for this run: GPT-5.6 Sol; reasoning effort telemetry is UNVERIFIED. GPT-6 / maximum is not claimed.

## Parent target and nonduplication

The newest owner directive assigns native R02 to the Lyons–Pemantle–Peres speed-monotonicity problem for biased random walk on a Galton–Watson tree without leaves. P01 is assigned a regeneration-derivative route and C31 an escape-probability coupling route. This note instead develops an Aidekon-speed-formula / tilted-covariance route, first for adjacent two-point offspring laws.

Use the **parent-bias** convention: at a vertex with `nu` children, the parent edge has weight `lambda` and each child edge has weight `1`. Thus increasing `lambda` biases the walk more strongly toward the root, and the conjecture asks whether the speed `ell_lambda` is nonincreasing.

## Exact algebraic reduction

Following the symmetrized Aidekon formula used by He--Wang--Xiang, let `beta_0,...,beta_nu` be iid escape probabilities and put

`S = sum_{i=0}^nu beta_i`, `D = lambda - 1 + S`,

`u = S / ((nu+1) D)`.

Then

`ell_lambda = E[(nu-lambda)u] / E[(nu+lambda)u]`.

Define the tilted effective offspring

`r_lambda = E[nu u] / E[u]`.

Pure algebra gives

`ell_lambda = (r_lambda-lambda)/(r_lambda+lambda)`,

hence, wherever differentiable,

`ell'_lambda = 2 (lambda r'_lambda - r_lambda)/(r_lambda+lambda)^2`.

Thus the exact sign problem is `lambda r'_lambda < r_lambda`.

Now define

`T = sum_i [ beta_i + (1-lambda) beta'_i ]`,

`q = T/(S D)`.

Differentiating `u` gives the identity

`u'/u = -q`.

If `mu_lambda` is the tilted probability measure with density `u/E[u]`, then

`r'_lambda = - Cov_{mu_lambda}(nu,q)`.

Therefore

`ell'_lambda < 0  iff  -Cov_mu(nu,q) < E_mu[nu]/lambda`.

This isolates the old intake obstruction (“measure-change term”) as a single covariance.

## Adjacent two-point offspring attack

Freeze `nu in {d,d+1}`, `d>=2`, with arbitrary mixing probability. For `1<lambda<d`, He--Wang--Xiang Lemmas 2.3--2.4 give

`1-lambda/d <= beta_i <= 1-lambda/(d+1)`

and

`0 < -beta'_i <= beta_i/(d-lambda)`.

Hence

`1 <= T/S <= (d-1)/(d-lambda)`.

Also

`d-lambda/d <= D <= d+1-lambda/(d+1)`.

Therefore

`q_min := 1/(d+1-lambda/(d+1)) <= q <= q_max := (d-1)/((d-lambda)(d-lambda/d))`.

Since `nu` takes two adjacent values, under **any** tilted law

`-Cov_mu(nu,q) <= (q_max-q_min)/4`,

while `E_mu[nu]>=d`. Thus strict decrease follows from the explicit scalar inequality

`F_d(lambda) := d/lambda - (q_max-q_min)/4 > 0`.

The key observation to verify next is that `F_d` is strictly decreasing on `(0,d)`, while

`F_d(d-1/4) = (32 d^4 + 12 d^3 + 8 d^2 + 7 d - 1) / ((2d-1)^2 (4d-1) (4d^2+4d+5)) > 0`.

This would prove strict speed monotonicity for every offspring law supported on `{d,d+1}` throughout `0<=lambda<=d-1/4`, combining the new `lambda>1` argument with the already-known `lambda<=1` case.

For `d=2`, direct exact algebra appears stronger: `F_2(lambda)>0` through `lambda=9/5`, since

`F_2(lambda) = (576-490 lambda+104 lambda^2-5 lambda^3) / [4 lambda (9-lambda)(4-lambda)(2-lambda)]`

and the numerator is decreasing but still equals `9/5` at `lambda=9/5`. This would improve the known all-offspring minimum-degree-2 interval endpoint `2/(1+1/sqrt(2)) = 1.17157...` to `9/5=1.8` for the full two-point `{2,3}` family.

## Falsification targets before claiming anything

1. Check every algebraic identity above exactly.
2. Check the direction of the parent-bias convention against the source.
3. Check that the beta upper/lower bounds from the cited lemmas apply uniformly conditional on `nu=d` or `d+1`.
4. Check that no current paper already states this adjacent-support improvement; negative search is not a novelty certificate.
5. Do not call this a solution of the full LPP conjecture: it is a restricted-family parameter-region theorem only.
