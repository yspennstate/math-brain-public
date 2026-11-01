# PROB10-06 idea note — reciprocal-Jensen contraction

Runtime model available in this chat: GPT-5.6 Sol. Reasoning-effort telemetry: UNVERIFIED. GPT-6/maximum is prompt-only and is not claimed.

Parent target remains the Lyons–Pemantle–Peres speed-monotonicity conjecture for Galton–Watson trees with `P(nu=0)=0`. Parent-bias convention: at a vertex with `k` children, parent weight is `lambda` and each child weight is `1`; reciprocal child bias is `beta=1/lambda`. Larger `beta` pushes away from the root; larger `lambda` pushes toward it.

Consumed own report: `runs/prob10_2026-09-20/PROB10-06/20260920T0951Z_type_conditioned_inverse_chord_crosses_lambda2_8e3b1a6c.md`. Its all-mixture `{2,3}` endpoint is `1.85527`; it crosses `lambda=2` for `p>=3/4` through `lambda=2.02`, using type-conditioned inverse moments plus endpoint chords.

## New main idea, before the certifying code

For `B` the branch escape probability and `Z=1/B`, the preceding report proves, conditional on the child root having `k` offspring,

`E[Z | nu=k] <= M_k := 1 + lambda/(k d)`,

where for `P(nu=2)=1-p, P(nu=3)=p`,

`d = 1-lambda E(1/nu) = 1-lambda(3-p)/6`.

Set `d_k=1/M_k = k d/(k d+lambda)`.

The preceding proof used this only through `E[B|nu=k]>=d_k` and then an endpoint chord on `B`. Instead exploit the inverse moment directly. For fixed `a>0,t>=0`,

`F(x)=a/(a+t+x)^2`.

Writing `x=1/z`,

`G(z)=F(1/z)=a z^2/((a+t)z+1)^2`.

Then

`G'(z)=2az/((a+t)z+1)^3 >=0`,

`G''(z)=2a(1-2(a+t)z)/((a+t)z+1)^4`.

Hence `G` is increasing and concave whenever `2(a+t)z>=1`. On the target strip `lambda>=1.85527`, every kernel used below has `a>=lambda-1>1/2`, while `0<B<=1`, so `z=1/B>=1` and concavity is automatic. Therefore

`E[F(B)|nu=k] = E[G(Z)|nu=k] <= G(E Z|nu=k) <= G(M_k) = a/(a+t+d_k)^2`.

Iterating over independent siblings and conditioning on their offspring types should replace the old `{0,u_2,u_3}` endpoint proxy by deterministic type-values `{d_2,d_3}` for every derivative kernel. This is strictly stronger information than the mean/support chord and may lower the mixture threshold needed to cross `lambda=2`.

Target for an exact checker: certify

`p>=71/100`, `1.85527<=lambda<=1001/500=2.002`,

with an explicit product bound below one and hence a uniform lower bound on `-ell'_lambda`. If this succeeds, combine with inherited coverage below `1.85527` to get strict decrease on `0<=lambda<=2.002` for every `p>=0.71`.

## Two genuinely different attacks to test in the same run

1. **Inverse-moment quantile proxy.** From `E(1/B|nu=k)<=1/d_k`, Markov gives `P(B<t|nu=k)<=t/d_k`. Test whether the resulting two-level stochastic lower proxy can contract the derivative recursion. This uses tail information rather than Jensen/concavity.

2. **Differentiate the reciprocal escape itself.** For `W=d(1/B)/d lambda=U/B^2`, the exact recursion is

`W = 1/S + lambda sum_i (B_i/S)^2 W_i`.

Try a sibling-decoupled annealed contraction for `E W`; record the exact coefficient obstruction if it is already >=1 in the new hard corner. This attacks the logarithmic/reciprocal derivative directly rather than the `U=-B'` recursion.

No finite simulation will be counted as a theorem. Any finite computational core must be exact rational interval arithmetic, and the parent claim stays OPEN/PARTIAL.