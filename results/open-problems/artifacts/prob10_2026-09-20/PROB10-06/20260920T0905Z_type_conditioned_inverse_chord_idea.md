Model actually available to this worker: **GPT-5.6 Sol. Reasoning effort telemetry: UNVERIFIED.** GPT-6/maximum was requested in prompt text only and is not claimed.

# PROB10-06 idea before code — condition the inverse-escape chord on the child's own offspring type

Parent target remains the Lyons–Pemantle–Peres speed-monotonicity conjecture for Galton–Watson trees **without leaves**. Convention: child bias `beta` increases outward drift; parent bias is `lambda=1/beta`, so the target sign is `ell'_lambda<=0` on `0<=lambda<E nu`.

Immediate predecessor: `runs/prob10_2026-09-20/PROB10-06/20260920T0854Z_inverse_escape_chord_crosses_lambda2_3a7c9e14.md`. It proves the `{2,3}` upper-mixture rectangle `p>=41/50`, `lambda<=54/25`, by a scalar inverse-escape moment and a single endpoint chord using only the unconditional bounds `E B>=d` and `B<=u=(3-lambda)/3`.

## New route A: type-conditioned inverse moments + type-conditioned endpoint chords

Freeze

`P(nu=2)=1-p`, `P(nu=3)=p`.

Let `B` be the branch escape probability, `X=1/B`, `M=E X`, and write `M_k=E[X | nu=k]`, `mu_k=E[B | nu=k]` for `k=2,3`. The recursion `B=S/(lambda+S)` and Cauchy give, conditionally on `nu=k`,

`M_k <= 1 + (lambda/k) M`.

The predecessor gives `M<=1/d`, where

`d=1-lambda(3-p)/6`.

Therefore

`M_k <= 1 + lambda/(k d)`,
`mu_k >= d_k := k d/(k d+lambda)`.

The child's own type also improves its deterministic upper endpoint. If `u=(3-lambda)/3` is the ternary-tree upper bound for all descendants, then a branch whose root has exactly `k` children satisfies

`B <= u_k := k u/(lambda+k u)`.

Thus, conditional on the child's own offspring type,

`0<=B<=u_k`, `E[B | nu=k]>=d_k`.

For every convex decreasing kernel `F`, the endpoint-chord inequality now gives

`E[F(B) | nu=k] <= (1-r_k) F(0) + r_k F(u_k)`,
`r_k=d_k/u_k`.

Iterating conditionally across independent siblings yields an **exact finite mixture over child types and Bernoulli endpoint choices**, rather than the predecessor's coarser binomial chord with common `(u,r)`. This should strictly lower the contraction kernels whenever `0<p<1`, because degree-2 child roots have the smaller endpoint `u_2<u_3=u` and both types have stronger conditional mean fractions than the unconditional chord records.

Planned use: replace every predecessor kernel

`E[lambda/(lambda+sum siblings B)^2]`

and

`E[(lambda-1)/(lambda-1+sum siblings B)^2]`

by the exact type-conditioned endpoint mixture. Keep the same rigorous `U=-B'` recursion, so there is no assumed derivative sign. Test whether this (i) pushes the upper-tail endpoint beyond `54/25`, or more importantly (ii) lowers the admissible mixture threshold below `41/50` while still crossing `lambda=2`.

## Route B: retain the child's own escape in the derivative coefficient

The predecessor bounded

`lambda U_i/(lambda+B_i+T)^2 <= lambda U_i/(lambda+T)^2`

by dropping `B_i`. A different attack is to control the joint score `E[U/(lambda+B+T)^2]` using `U=B q` and a type-conditioned bound on `q=-B'/B`, or a size-biased chord in the measure with density proportional to `U`. If successful it removes the largest structural loss in the scalar `U` contraction. This route is analytically distinct from Route A because it targets the `B-U` correlation, not the sibling escape distribution.

## Route C: second-level recursion instead of one-level annealing

Unroll `U=A(B_children)+sum_i K_i(B_children) U_i` one generation further before averaging. The products of two derivative kernels contain independent sibling blocks and may contract even when the one-step scalar coefficient is loose. A two-level exact kernel can be conditioned on root/child offspring patterns. This is a finite-dimensional regeneration-style contraction, not another first-moment chord.

I will first falsify Route A by exact rational endpoint evaluation on the current hard corner and then search for a larger certified rectangle. Only after a concrete gain is located will I archive a checker.