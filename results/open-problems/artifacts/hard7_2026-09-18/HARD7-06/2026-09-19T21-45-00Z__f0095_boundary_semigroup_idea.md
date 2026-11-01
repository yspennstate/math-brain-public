Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 maximum, and I do not claim otherwise.**

# HARD7-06 F0095 — idea checkpoint before code

Target remains the owned external F0095 problem: convergence to a constant location of the ordinary sparse Erdos--Renyi 3-colourability threshold. Incoming certified bracket is `L_3=4.03`, `U_3=4.6865076260769`, hence `W_3=0.6565076260769`.

This run uses a new triple, **B1 / B13 / B29**, after the preceding B18/B27/B19 run. I am deliberately not starting with another decimal search.

## B1 — change category: the two-input cavity rule is exactly multiplication

Use the run-25 message coordinate `t=(1-x)/3 in [0,1/3]` and cavity map

`R(N)=(A-2B+C)/(3A-3B+C)`, with `A=prod(1-t_i)`, `B=prod(1-2t_i)`, `C=prod(1-3t_i)`.

For exactly two messages `s,t`, direct algebra gives

`A-2B+C = 2st`, `3A-3B+C=1`, hence `R({s,t})=2st`.

Thus in the rescaled coordinate `y=2t`, the exactly-two-input cavity rule is the multiplicative semigroup `y_out=y_1 y_2`. Any nontrivial fixed-point support should therefore reproduce arbitrarily small support values by iterating `s -> 2s^2` on the positive-support event with exactly two active inputs.

## B13 — find what only increases: cavity monotonicity should imply Poisson concavity

If a new message `u` is appended to a cloud with products `(A,B,C)`, then the cross-multiplied increment of the cavity ratio has numerator

`u(3AB-4AC+BC)`.

Writing `r=B/A`, `v=C/A`, the pointwise one-message inequality

`(1-3t)/(1-t) <= ((1-2t)/(1-t))^2`

implies `0<=v<=r^2<=1`. Therefore

`3AB-4AC+BC = A^2(3r-4v+rv) >= A^2 r(3-4r+r^2) >= 0`.

So the cavity output is coordinatewise nondecreasing. Combining this with the exact insertion identity

`F(N+delta_t)-F(N)=log(1-3t R(N))`, `F=log S`,

makes the insertion marginal nonincreasing as the background cloud grows. This should prove log-submodularity of `F`, and for every finite active law bounded away from the neutral endpoint, termwise Poisson differentiation should give

`V_b''(lambda)=E Delta_X Delta_Y F(N_lambda) <= 0`.

This would add a global concavity structure to the neutral-atom quotient from run 24 rather than another local atom optimization.

## B29 — add the boundary points: the fixed point must accumulate at both ends

There are two complementary endpoint mechanisms.

First, for every finite cloud,

`(3A-3B+C)-3(A-2B+C)=3B-2C > 0`,

because `B>0` and `0<=C<=B`. Thus every finite-cloud cavity output satisfies `R(N)<1/3`: the endpoint `1/3` is never an atom produced by the recursion.

Second, take any `tau>0` such that the fixed-point law has positive mass on `[tau,1/3]`. With exactly `n` such positive inputs and no other positive inputs, monotonicity gives output at least

`r_n(tau)=[(1-tau)^n-2(1-2tau)^n+(1-3tau)^n]/[3(1-tau)^n-3(1-2tau)^n+(1-3tau)^n]`.

Since `r_n(tau) -> 1/3`, the fixed point has support approaching `1/3` from below. On the other side, the exact two-input multiplication rule propagates any positive support point through `s_{k+1}=2s_k^2`, forcing support accumulation at zero. Together with the previously proved positive zero atom, the infinite-support stationary branch has a rigid two-boundary geometry: atom plus accumulation at 0, no atom but accumulation at 1/3.

The quantitative version will reuse the already-proved fixed-point first-moment lower bound in the equivalent `lambda=t/(1-t)` coordinate. Since `t=lambda/(1+lambda) >= (2/3)lambda`, a nontrivial fixed point obeys `E t > 2/(3d^2)`. Taking `tau=1/(3d^2)` then forces `a([tau,1/3])>1/d^2`. Consequently the Poisson event with exactly `n` marks in that upper set and no other positive marks has probability strictly larger than `exp(-d)/(d^n n!)`, yielding an explicit lower bound on the fixed-point mass in `[r_n(tau),1/3)` for every `n>=2`.

Only after this checkpoint will I build a small exact self-check for the finite algebra and a current-degree quantitative anchor. The analytic theorem itself must be proved on the report page; the checker is not a substitute.