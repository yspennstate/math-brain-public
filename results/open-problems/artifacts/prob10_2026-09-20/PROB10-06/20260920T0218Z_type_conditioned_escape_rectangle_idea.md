Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — requested GPT-6 maximum is prompt-only in this runtime, and I do not claim otherwise.**

# PROB10-06 idea before code: condition the escape derivative on the child's own offspring type

Parent target remains the Lyons–Pemantle–Peres speed-monotonicity conjecture for biased random walk on a supercritical Galton–Watson tree **without leaves**. In child-bias notation, beta weights each child relative to the parent and larger beta pushes away from the root; in this track I use parent-bias lambda=1/beta, so larger lambda pushes toward the root and the conjectural sign is ell'_lambda <= 0 on 0<=lambda<E nu.

This iteration consumes rather than duplicates:

- `runs/prob10_2026-09-20/PROB10-06/20260920T0132Z_escape_elasticity_cone_bridge_7d4a2c91.md`: all `{2,3}` mixtures through lambda=1847/1000, with the new pathwise cone `1/(3-lambda) <= (-B')/B <= 1/(2-lambda)` specialized to this family;
- `proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T01-41-00Z__branch-addition-ratio-coupling.md`: `3/4 <= c_3/c_2 <= 1` plus rare-tail rectangles;
- P01's new `2026-09-20T02-02-20Z__degree-secant-covariance-*` artifacts at commits `747295be...`, `947d5fb...`, `17d5422...`: conditional **current-vertex degree** secants for broad support. The route below is different: it conditions the generic child escape variables inside the adjacent `{2,3}` Aïdékon derivative formula on each child's own offspring type, then enumerates the 3- and 4-child type-count patterns exactly.

## Exact new idea

Fix `P(nu=2)=1-p`, `P(nu=3)=p`, and `1<lambda<2`. Put `a=lambda-1`, let `B` be the escape probability to infinity before the parent, and `q=(-B')/B`.

The regular-tree comparison gives the global escape bracket

`b_2=(2-lambda)/2 <= B <= u_3=(3-lambda)/3`.

Conditioning once more on the child's own offspring type and using `B=S/(lambda+S)` gives sharper type-specific brackets

`nu=2: b_2 <= B <= u_2=2(3-lambda)/(lambda+6)`,

`nu=3: b_3=3(2-lambda)/(6-lambda) <= B <= u_3`.

The logarithmic derivative recursion

`q=[1+lambda sum_j B_j q_j / sum_j B_j]/[lambda+sum_j B_j]`

plus the global cone gives type-specific bounds

`Q_2^+=1/(2-lambda)`,
`Q_3^+=4/[(2-lambda)(6-lambda)]`,

`Q_2^-=9/[(3-lambda)(lambda+6)]`,
`Q_3^-=1/(3-lambda)`.

For the branch quantity with `n=k+1` iid generic escape variables, let `m` be the number whose own offspring type is 3. Then

`s^-_{n,m}=(n-m)b_2+m b_3`,
`s^+_{n,m}=(n-m)u_2+m u_3`,

and with `Y=S/(a+S)` the corresponding derivative integrand factors as

`Y R`, where

`R=[1+a (sum_i B_i q_i/S)]/(a+S)`.

The weighted average of the q_i is maximized, at fixed type pattern, by assigning maximal B-weight to type 2 and minimal B-weight to type 3; it is minimized by the opposite assignment. This yields explicit pattern constants `r^+_{n,m}(lambda)` and `r^-_{n,m}(lambda)`.

For h_2/c_2 (`n=3`), condition on m and write `x_m=E[Y|m]`. Then

`h_2/c_2 <= [sum pi_{3,m}(p) x_m r^+_{3,m}]/[sum pi_{3,m}(p) x_m]`.

For h_3/c_3 (`n=4`),

`h_3/c_3 >= [sum pi_{4,m}(p) x_m r^-_{4,m}]/[sum pi_{4,m}(p) x_m]`.

On the narrow strip `lambda in [1847/1000,1851/1000]`, direct rational differentiation appears to give:

- every `r^+_{3,m}` increases with lambda;
- every `r^-_{4,m}` increases with lambda;
- every endpoint `y^-_{n,m},y^+_{n,m}` decreases with lambda.

Therefore all unknown conditional means x_m lie in fixed rational boxes whose endpoints occur at the strip endpoints. A linear-fractional function over a box attains its extremum at a vertex. Hence the whole problem reduces to 16 upper corners times 32 lower corners. For each pair the claim

`(1851/1000) * (U_corner(p)-L_corner(p)) < 1979/200 = 9.895`

is a degree-at-most-7 rational-polynomial positivity problem in p on [0,1]. If exact Bernstein subdivision certifies all 512 inequalities, then since

`1979/200 < 5+2 sqrt(6) = min_{0<theta<1} (2+theta)/(theta(1-theta))`,

Aïdékon's adjacent-family derivative identity gives strict ell'_lambda<0 throughout the strip, for every p. Combined with the preceding report, this would move the all-mixture `{2,3}` endpoint from about 1.84735 to exactly 1.851.

The same inequality gives a quantitative strip margin because

`min_theta [2+theta-(1979/200)theta(1-theta)] = 2-(1779/200)^2/[4(1979/200)] >0`.

## Three materially different attacks this run

1. **Type-conditioned child-pattern envelope (main route):** pursue the 512 exact rational inequalities above.
2. **Static branch-addition strengthening:** use positive lower escape `B>=b_2` to sharpen the generic `c_3/c_2<=1` bound. This can improve fixed-p tail rectangles, but by itself cannot improve the all-p endpoint because as p varies the tilted mixture coordinate theta still spans (0,1).
3. **Finite-depth contraction route:** the scalar B recursion has contraction factor lambda/2 on degree-2 vertices but `12 lambda/(6-lambda)^2>1` on degree-3 vertices near this strip. The first-moment mixture contraction therefore fails for central p (at lambda=1.851 it requires roughly p<0.205), so a naive scalar truncation certificate cannot bridge the all-mixture gap; one would need a genuinely joint `(B,q)` or weighted contraction.

Next step: exact rational checker, then only if it passes write the theorem-sized report. No simulation will be used as proof.