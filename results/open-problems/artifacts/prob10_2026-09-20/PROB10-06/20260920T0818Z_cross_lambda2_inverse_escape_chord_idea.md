Model actually available to this worker: GPT-5.6 Sol. Authenticated reasoning-effort telemetry is unavailable, so reasoning level is UNVERIFIED; GPT-6/maximum is not claimed.

# PROB10-06 idea before code — cross the minimum-degree singularity with an annealed inverse-escape/chord contraction

The preceding R02/PROB10-06 stream reaches the `{2,3}` upper-mixture tail `p>=41/50` only through parent bias `lambda=1.9`, while the pointwise derivative envelope `q_2<=1/(2-lambda)` becomes useless at `lambda=2`. Do not shrink another rectangle below 2. Instead replace the pointwise lower bound on the escape probability by an annealed lower bound and then use bounded support plus convexity to contract the *derivative variable U=-B'* directly.

Freeze

`P(nu=2)=1-p, P(nu=3)=p`, `p>=41/50`,

and seek a rectangle beginning at `lambda=19/10` and crossing `lambda=2`.

For the escape recursion

`B = S/(lambda+S)`, `S=sum_{i=1}^nu B_i`,

put `X=1/B`. Cauchy gives

`1/S <= (1/nu^2) sum_i X_i`,

hence

`X <= 1 + (lambda/nu^2) sum_i X_i`.

Therefore, with `M=E X` and `a=E(1/nu)=(3-p)/6`,

`M <= 1 + lambda a M`,

so whenever `d:=1-lambda(3-p)/6>0`,

`E(1/B)<=1/d` and by Jensen `mu:=E B>=d`.

Because the offspring support is at most 3, monotone comparison with the deterministic ternary tree gives

`0<B<=u:=(3-lambda)/3` for `lambda<3`.

Thus `r:=d/u` is a rigorous lower bound on the normalized mean `E B/u`.

Now differentiate the escape recursion. With `U=-B'>=0`,

`U = S/(lambda+S)^2 + lambda sum_i U_i/(lambda+S)^2`.

For a fixed child `i`, condition on `(B_i,U_i)` and the other `k-1` sibling escapes. Dropping `B_i` only increases the coefficient. Since

`t -> lambda/(lambda+t)^2`

is decreasing and convex on `[0,infinity)`, and each sibling lies in `[0,u]` with mean at least `d=ru`, the endpoint-chord inequality iterated over independent siblings yields

`E[ lambda/(lambda+T)^2 ] <= K_{k-1}(lambda,p)`

where

`K_j = sum_{m=0}^j binom(j,m) r^m(1-r)^(j-m) * lambda/(lambda+m u)^2`.

Consequently, if

`rho=(1-p) 2 K_1 + p 3 K_2 <1`,

then

`eta:=E U <= A/(1-rho)`,

with the sharper inhomogeneous bound

`A=(1-p)*[2u/(lambda+2u)^2] + p*[3u/(lambda+3u)^2]`.

This is the key route: it remains finite across `lambda=2` because it uses annealed inverse escape rather than the pointwise binary-tree denominator.

To feed this into the exact Aidekon derivative reduction, let `a0=lambda-1`. For the three-copy term defining `c_2,h_2`, the denominator satisfies `a0+S<=2`, so

`c_2 >= mu/2 >= d/2`.

The escape-only part of `h_2/c_2` is at most `1/a0`. For its U-part, condition on one child U and apply the same endpoint-chord inequality to the two siblings with the convex function

`t -> a0/(a0+t)^2`.

Write the resulting two-sibling endpoint average as `Kc`. Then

`h_2/c_2 <= 1/(lambda-1) + 2 eta Kc/d`.

For `h_3/c_3`, using four copies and `S<=4u`, the positive escape-only term gives

`h_3/c_3 >= 1/(lambda-1+4u)=3/(9-lambda)`.

Hence

`Delta:=h_2/c_2-h_3/c_3 <= D(lambda,p)`

with

`D = 1/(lambda-1) + 2 eta Kc/d - 3/(9-lambda)`.

The inherited branch-addition lower ratio `c_3/c_2>=3/4` gives

`theta >= theta0:=3p/(4-p)`.

For `p>=41/50`, `theta0` lies to the right of the maximizer of `g(theta)=theta(1-theta)/(2+theta)`, so

`g(theta)<=g(theta0)`.

The exact speed identity then reduces the desired sign to

`lambda*g(theta0)*D <1`.

Pre-code rational probing indicates the full rectangle

`41/50 <= p <=1`, `19/10 <= lambda <=54/25=2.16`

should satisfy the stronger target `lambda*g(theta0)*D <=999/1000`, while `rho<1`. If exact arithmetic confirms this, stitching with the inherited `p>=41/50` theorem through `lambda=1.9` will move the rigorously covered endpoint from 1.9 to 2.16 and, importantly, cross the `lambda=2` singularity.

Three materially distinct routes for this run:

1. **Direct U contraction via inverse escape + convex endpoint chords** — primary candidate above.
2. **Direct q=-B'/B contraction** — analyze separately. It also contracts near `lambda=2`, but preliminary algebra indicates its coefficient approaches one too rapidly above 2 and gives a much worse speed-score bound; record the quantitative failure if confirmed.
3. **Near-critical Einstein-relation bridge from lambda=m** — the literature gives the sign infinitesimally at the critical bias for suitable finite-support laws, but it does not supply an explicit neighborhood width usable for a certified overlap. Check whether any quantitative constant can be recovered cheaply; otherwise record this as a nonquantitative baseline, not source movement.

Only after this note is persisted should an exact rational checker be built.