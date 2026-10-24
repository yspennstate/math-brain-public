# R15 idea before checking — combine null-flow aggregates with the full subset-face budget

Date: 2026-09-19 UTC.

The preceding run proved, for every coordinate subset `J` of size `m>=2`, the global certificate barrier

`A_J >= d_m (sqrt(N_m)-sqrt(B_J))_+^2`,

where `N_m=binom(m,2)` and `d_m=3/(2m-1)`.

For a two-block Hessian-null candidate with block-constant base values `q_i=u` on a positive block `J`, `q_i=v` on a negative block `K`, and direction `h=a 1_J-b 1_K`, the exact gradient contact equations contain more information than the last run's base-only `q_*` bound. Summing them over each block gives

`A_J + 2u U + v W + R_J = |J|-x`,

`A_K + 2v V + u W + R_K = |K|-y`,

where `U=sum_{J-J}B_ij`, `V=sum_{K-K}B_ij`, `W=sum_{J-K}B_ij`, `x=sum_J r_i`, `y=sum_K r_i`, and the rest-edge terms `R_J,R_K` are nonnegative. Hence

`|J|-x-2uU-vW >= d_|J| (sqrt(N_|J|)-sqrt(U))_+^2`,

`|K|-y-2vV-uW >= d_|K| (sqrt(N_|K|)-sqrt(V))_+^2`.

At the same time Hessian nullity gives the exact aggregate flow equations

`2aU-bW=x(p-a)`,

`aW-2bV=y(p+b)`.

The research plan is to eliminate `U,V,W` analytically, or first identify the extremal `W`, and determine which of the three surviving cubic-null scalar regimes from the preceding run can satisfy both global block-face inequalities. This is a genuinely new route: it combines a global face theorem with the null-flow equations and exact first-order budget, rather than taking another derivative of the one-dimensional partition function.

Status: idea only; no claim yet. Any finite/symbolic validation will be done only after the analytic route is worked out.