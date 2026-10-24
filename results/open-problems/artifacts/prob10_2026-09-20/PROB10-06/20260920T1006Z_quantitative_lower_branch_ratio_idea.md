Model actually exposed to this worker: GPT-5.6 Sol. Authenticated reasoning-effort telemetry is unavailable, so reasoning level is UNVERIFIED; GPT-6/maximum is not claimed.

# PROB10-06 idea before code — quantitative lower branch ratio from type-conditioned escape mass

Parent source remains the Lyons–Pemantle–Peres speed-monotonicity conjecture for Galton–Watson trees without leaves. Convention is fixed: child bias `beta` weights each child relative to the parent and larger `beta` pushes outward; parent bias `lambda=1/beta` weights the parent and larger `lambda` pushes inward. Source conjecture: for `P(nu=0)=0`, `m=E nu>1`, speed is increasing in `beta` on `(1/m,infinity)`, equivalently decreasing in `lambda` on `[0,m)`.

This run stays in the delimited unresolved family

`P(nu=2)=1-p,  P(nu=3)=p`

and does not take over P01's `{1,D}` work or NM13-05's `{3,4}` work. The immediate predecessor proves all mixtures through `lambda=1.85527`, and proves `p>=3/4` through `lambda=2.02` by child-type-conditioned inverse-escape endpoint chords.

## Planned route A — quantitative *lower* branch-addition ratio

The current high-`p` speed certificate uses only the static inequality `c_3/c_2 >= 3/4`, hence

`theta >= 3p/(4-p)`

for the Aidekon tilt `theta=p c_3/((1-p)c_2+p c_3)`. On the relevant upper tail, `g(theta)=theta(1-theta)/(2+theta)` is decreasing, so any strict lower bound on `c_3/c_2` directly lowers the derivative penalty.

Put `a=lambda-1`, `S_n=B_1+...+B_n`, and

`Phi_n=E[S_n/(a+S_n)]`, so `c_2=Phi_3/3`, `c_3=Phi_4/4` and

`c_3/c_2=(3/4) Phi_4/Phi_3`.

For an independent fourth branch `B`,

`Phi_4-Phi_3 = E[ a B / ((a+S_3)(a+S_3+B)) ]`.

From the predecessor, for child type `k=2,3`,

`E[B | nu=k] >= d_k`,
`B | {nu=k} <= u_k`,

while every branch obeys `B<=u=(3-lambda)/3`. Hence

`Phi_4-Phi_3 >= a/(a+3u) * [ (1-p)d_2/(a+3u+u_2) + p d_3/(a+3u+u_3) ]`.

Also `Phi_3 <= 3u/(a+3u)`. Therefore

`c_3/c_2 >= R_*(lambda,p)`

with

`R_* := (3/4) * { 1 + a/(3u) * [ (1-p)d_2/(a+3u+u_2) + p d_3/(a+3u+u_3) ] }`.

This is strictly stronger than `3/4` whenever `lambda>1` and the inverse-escape lower bounds are positive. It uses the same rigorously established child-type conditional means/endpoints but in a new static branch-addition inequality, not another refinement of the derivative contraction.

Then

`theta >= theta_*(lambda,p):= p R_* / (1-p+p R_*)`.

On any box where `theta_* >= sqrt(6)-2`, the function `g` is decreasing, so the existing exact upper bound `Delta<=D(lambda,p)` may be combined with

`lambda g(theta_*) D < 1`.

Goal: lower the mixture threshold for crossing `lambda=2`, or push the `p>=3/4` endpoint beyond `2.02`, with a certified derivative margin and without changing the parent claim.

## Planned route B — coupled inverse moments beyond the first harmonic inequality

Try to improve `d_k` itself by one extra inverse-recursion generation: retain the child-type split inside `E[1/(B_1+...+B_k)]` instead of collapsing immediately to Cauchy plus the unconditional `M=E[1/B]`. If the resulting type-count expansion yields a strict contraction, feed the improved conditional means into the same speed formula. If it algebraically collapses to the predecessor's bound, record that exact obstruction.

## Planned route C — own-escape retention in the `U=-B'` coefficient

The predecessor showed marginal `B` and `EU` information alone cannot exploit the own child escape in `lambda/(lambda+B_i+T)^2`, because the `U`-weighted law might concentrate at the worst endpoint. Try to derive a recursion-based constraint on the joint pair `(B,U)` strong enough to preclude that extremizer. A useful target would be an annealed inequality of the form `E[U f(B)] <= eta * Q(f)` with `Q(f)` strictly below `sup f`. If no such inequality follows from the current first-moment recursion, record the exact extremal obstruction and do not recycle the failed marginal argument.

No code has been run for this note. The critical claim to falsify first is the lower bound `R_*` above; only after algebraic verification will an exact rational checker be used.