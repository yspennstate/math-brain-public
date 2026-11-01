# P01 T06 idea before checker: bounded-width analytic derivative screen

Actual runtime model: GPT-5.6 Sol. Reasoning level: UNVERIFIED. GPT-6 / maximum was requested but is not claimed.

Target: LPP speed monotonicity on a supercritical Galton-Watson tree without leaves. Parent-bias convention: at a vertex with `nu` children, the parent edge has weight `lambda` and each child edge weight `1`; equivalently child bias `beta=1/lambda`. Increasing `lambda` is more rootward, so the conjectured sign is `ell'_lambda <= 0`.

Ownership/nonduplication: P01 is the analytic regeneration-derivative worker; the live coupling companion is NM13-05 (historical C31 name is superseded). R02 has an idea note for the Aidekon tilted-covariance route restricted first to adjacent two-point offspring laws `{d,d+1}`. This P01 attack does not claim that adjacent case; it asks whether the same derivative identity can be made uniform for arbitrary bounded offspring support `[d,D]`, with a source-level interval beyond the 2025 He-Wang-Xiang endpoint.

Literal Bowditch-Tokushige regeneration-score attack: their derivative is a covariance of regeneration displacement with a signed path score. The local score changes sign between parent and child steps, so bounded offspring alone does not give a sign. That route currently lacks a monotone-cycle inequality. I therefore keep the regeneration derivative as the conceptual frame but use the equivalent Aidekon/He-Wang-Xiang escape-variable formula, where the measure-change term can be bounded explicitly.

Let `d>=2`, let `D<infinity` be an offspring upper bound, `h=D-d`, and work on `1<lambda<d`. Let `beta_0,...,beta_nu` be iid escape probabilities, `S=sum beta_i`, `A=lambda-1+S`, and `u=S/((nu+1)A)`. Symmetrizing Aidekon's formula gives

`ell=(r-lambda)/(r+lambda)`, where `r=E[nu u]/E[u]`.

Write

`q = [S+(1-lambda)S']/(S A)`.

Then `u'/u=-q`, so for the `u`-tilted law `mu`,

`r'=-Cov_mu(nu,q)` and `ell'=2(lambda r'-r)/(r+lambda)^2`.

He-Wang-Xiang Lemmas 2.3-2.4 imply, uniformly for offspring in `[d,D]`,

`1-lambda/d <= beta <= 1-lambda/D`,

`0 < -beta' <= beta/(d-lambda)`.

Hence

`1 <= [S+(1-lambda)S']/S <= (d-1)/(d-lambda)`, and

`d-lambda/d <= A <= D-lambda/D`.

Thus

`q_min = 1/(D-lambda/D)`,

`q_max = (d-1)/((d-lambda)(d-lambda/d))`.

By Gruss' covariance bound,

`-Cov_mu(nu,q) <= h(q_max-q_min)/4`,

while `r>=d`. Therefore

`ell'_lambda <= - 2 lambda F_{d,D}(lambda)/(D+lambda)^2`,

where

`F_{d,D}(lambda)=d/lambda - (h/4)[(d-1)/((d-lambda)(d-lambda/d)) - 1/(D-lambda/D)]`.

If `F>0`, this is a rigorous negative derivative sign. A direct derivative estimate should show `F` is strictly decreasing on `(0,d)`, so it has a unique zero `rho_{d,D}`. The easy explicit interior point `lambda_0=d-h/4` has

`F(lambda_0)= h N(d,h)/[(4d-h)(4d^2-4d+h)(4d^2+8dh-4d+4h^2+h)]`,

with

`N=32d^4+44d^3h-32d^3+12d^2h^2-4d^2h+7dh^2-h^3`

` = 32d^3(d-1)+4d^2h(11d-1)+h^2(12d^2+7d-h)`.

So `F(lambda_0)>0` whenever `0<h<4d`. If in addition

`h < 4[d - d/(1+sqrt(1-1/d))]`,

then `lambda_0` lies strictly beyond the current all-offspring He-Wang-Xiang endpoint. This would yield a genuinely uncovered bounded-width region.

Concrete falsification target: `d=2,D=4` (`h=2`). Here exact simplification predicts

`F_{2,4}(lambda)=(33 lambda^2-208 lambda+256)/(lambda(16-lambda)(4-lambda)(2-lambda))`,

so the unique zero in `(0,2)` is

`rho=(104-8 sqrt(37))/33 = 1.676906...`,

well beyond the known minimum-degree-two endpoint `2/(1+1/sqrt(2))=1.171572...`. At `lambda_0=3/2`, `F=292/435`; if the denominator comparison is correct this gives the uniform sign margin

`ell'_lambda <= -584/10875 < -0.0537` on `[1,3/2]` for every no-leaf offspring law supported in `{2,3,4}`.

Next: exact symbolic checker for the algebra only, then full proof in the immutable report. No simulation is relevant to the metric.