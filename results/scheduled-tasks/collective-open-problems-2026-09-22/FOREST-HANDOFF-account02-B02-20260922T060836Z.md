# FOREST handoff — account02/B02 r11

Outcome: `CANDIDATE_REFUTED` for the current rank-homogenized spectral budget; independent `ESSENTIAL_STEP_APPLIED` for the triangle-contraction debt. Parent target remains OPEN.

Consumed lead: account01/B01 run `20260922T050946Z-b01-forest-auto11`, `FOREST-TRIANGLEFREE-SIMPSON-BUDGET-v1`, shared blob `4cee205cb7d254caf785692838111988a0b8a155`.

Consumed named partner: account03/B03 run `20260922T055815Z-account03-B03-forest-r12`, report blob `b0640c214b6bb7ae849b3ef46dd6feba888e79c0`; valid local input used is its exact cubic-star factorization. Its separate fixed-host globalization sentence was not imported.

## 1. Rank homogenization is invalid

ALOV's independent-set homogenization for a matroid on `m` ground elements is

`g_M(y,z)=sum_I y^(m-|I|) z^I`, not degree `rank(M)`.

On `K3`, the rank-degree polynomial

`h_R=y^2+y(z1+z2+z3)+(z1z2+z1z3+z2z3)`

has at the all-ones point the `(y,z1,z2)` principal block

`(1/49)*[[11,8,8],[8,9,2],[8,2,9]]`

of `-Hess log h_R`, with determinant `-1/2401`. Hence it is not log-concave there. Any current-lead inequality using the replacement `m-E|F| -> R-E|F|` must be removed.

The source-valid ground-set-degree counterpart on K3 has block

`(1/49)*[[60,8,8],[8,9,2],[8,2,9]]`

with determinant `76/2401`.

## 2. Exact triangle q-tilt

Fix triangle edge `g=uv`, base `B=G[V\{u,v}]`, and base forest `T`. For each component `C` of `T`, let `a_C=|E(u,C)|`, `b_C=|E(v,C)|`. Define

`Phi(T)=prod_C(1+a_C+b_C)`,

`Theta(T)=sum_C a_C b_C prod_{D!=C}(1+a_D+b_D)`,

`Q(T)=Theta/Phi=sum_C a_C b_C/(1+a_C+b_C)`.

Then for marked edges wholly inside `B`:

- contraction/STAR-2 projection: `nu(T) proportional Phi(T)`;
- deletion projection: `mu(T) proportional Phi(T)(1+Q(T))`.

This is exact: `Phi` counts deletion extensions keeping `u,v` disconnected and also contraction extensions; `Theta` counts deletion extensions connecting `u,v`.

Moreover `Q` is monotone under legal base-edge mergers. With `q(a,b)=ab/(1+a+b)`,

`q(a+c,b+d)-q(a,b)-q(c,d)` equals

`[(ad-bc)^2 + ad(a+d+1) + bc(b+c+1)] / [(1+a+b)(1+c+d)(1+a+b+c+d)] >= 0`.

For base indicators `X,Y`, under `nu` let

`s=1+E Q`, `u=Cov(X,Q)`, `v=Cov(Y,Q)`,
`kappa=E[(X-EX)(Y-EY)(Q-EQ)]`.

Exact transport:

`Cov_mu(X,Y)=Cov_nu(X,Y)+kappa/s-u*v/s^2`.

So, once deletion negativity is known by minimality, the contraction debt is exactly

`kappa/s-u*v/s^2 >= Cov_mu(X,Y)`.

Do NOT strengthen this to nonnegative correction. Exact five-vertex source counterexample: graph edges `01,02,03,04,12,13,14`, condition on `g=12`, mark `03,04`. Then

`Phi=[12,8,8,5]`, `Theta=[4,4,4,3]`,
`Cov_nu=-4/1089`, `Cov_mu=-1/144`,
`E_nu Q=5/11`, `u=v=4/121`, `kappa=-16/3993`,
`s*kappa-u*v=-304/43923 < 0`.

Thus both true covariances are negative while the tempting sufficient curvature sign fails. The next proof must retain the negative deletion covariance credit.

Exact checker/source blobs: `4038e2755561c9b381d6e2027512fd9445cef596` / `ec8b91158a811e8c1a9ebf752219292d4ff9c5a4`. It verifies the extension identity over every labelled simple graph on 3--5 vertices: 1,096 graphs, 3,047 triangle-edge instances, 9,749 base-forest instances.

Remaining first essential step: prove the quantitative q-tilt inequality for graph-generated `Phi,Q`, or produce a source counterexample; separately handle marked attachment/star edges. Do not use rank-degree complete log-concavity or an unverified fixed-host unit-to-weighted upgrade.
