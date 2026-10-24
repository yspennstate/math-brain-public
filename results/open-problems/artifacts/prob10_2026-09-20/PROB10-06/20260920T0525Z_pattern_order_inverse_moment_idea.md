Model actually running in this worker: **GPT-5.6 Sol. Reasoning level: UNVERIFIED.** GPT-6/maximum was requested in prompt text, but no authenticated applied-model/reasoning-effort telemetry or binding selector is exposed here, so GPT-6/maximum is not claimed.

# PROB10-06 idea before persistent checker code — exploit child-type stochastic order, and probe a route across lambda=2

Parent target: Lyons--Pemantle--Peres speed monotonicity for supercritical Galton--Watson trees without leaves. Parent-bias `lambda` increases drift toward the root; child-bias `beta=1/lambda` increases drift away. This note stays on the complementary R02 route for the genuinely random family

`P(nu=2)=1-p,  P(nu=3)=p`.

The latest R02/PROB10-06 theorem reaches every `p in [0,1]` through parent bias `lambda=1.8539`. Its finite certificate loses information by allowing the conditional escape-weight contributions for different child-type counts to vary independently inside their pattern boxes. The next attack is to restore a genuine monotonicity relation among those pattern contributions.

## Attack A — child-type stochastic order -> reverse Chebyshev compression

Let `X_1,X_2,X_3` be iid unconditional child escape probabilities. Conditional on a vertex having two children,

`B^(2)=(X_1+X_2)/(lambda+X_1+X_2)`.

Conditional on three children, under the natural coupling using the same first two descendants and one additional independent branch,

`B^(3)=(X_1+X_2+X_3)/(lambda+X_1+X_2+X_3) >= B^(2)` pointwise.

Therefore the conditional escape law for own offspring type 3 stochastically dominates the type-2 law.

For the outer `c_2` term there are three iid branch escapes. Conditional on exactly `m` of these three branches having type 3, write

`S_m=sum_{j=1}^3 B_j`,
`Y_m=E[ phi(S_m) ]`,
`phi(s)=s/(lambda-1+s)`.

On the present strip `lambda>1`, `phi` is increasing. Replacing one type-2 branch by a coupled type-3 branch therefore proves the exact structural monotonicity

`Y_0 <= Y_1 <= Y_2 <= Y_3`.                                  (A.1)

The preceding type-conditioned envelope gives deterministic pattern-score upper bounds `R_m^U(lambda)` for the ratio of the `h_2` integrand to the `c_2` integrand. The explicit rational formulas appear to satisfy

`R_0^U >= R_1^U >= R_2^U >= R_3^U`                              (A.2)

on the next strip; this is a finite rational statement to certify exactly.

Let `pi_m=C(3,m)p^m(1-p)^(3-m)`. Since `Y_m` and `R_m^U` are oppositely ordered, the weighted reverse-Chebyshev identity

`sum pi_m Y_m R_m^U <= (sum pi_m Y_m)(sum pi_m R_m^U)`          (A.3)

follows from

`Cov_pi(Y,R)=(1/2) sum_{i,j} pi_i pi_j (Y_i-Y_j)(R_i-R_j) <=0`.

Thus the entire upper ratio compresses to

`h_2/c_2 <= sum_{m=0}^3 pi_m R_m^U`,                            (A.4)

removing all sixteen independent `Y_m` corners on the upper side. Keep the lower `h_3/c_3` side completely conservative, with its previous 32 exact pattern-box corners. Feed (A.4) into the already proved exact two-point reduction

`-ell'_lambda = 2(2+theta)[1-lambda g(theta) Delta]/(2+theta+lambda)^2`,
`g(theta)=theta(1-theta)/(2+theta)`,
`Delta=h_2/c_2-h_3/c_3`,

and the consumed branch-addition relation `3p/(4-p)<=theta<=p`.

Target for the exact finite core: certify an all-mixture extension from `1.8539` to at least the rational endpoint `lambda=1.85508`; if the same certificate has enough slack, push the rational endpoint slightly farther without changing the mechanism.

## Attack B — harmonic inverse-escape recursion (different mechanism, aimed across lambda=2)

The pointwise logarithmic derivative bound used so far blows up as `lambda -> 2-`. Instead control how much mass can actually sit at tiny escape probability.

Let `B=S/(lambda+S)`, `S=sum_{j=1}^nu B_j`, and `H=E[1/B]`. Then

`1/B = 1 + lambda/S`.

For positive numbers `b_1,...,b_k`, Cauchy gives

`1/(sum b_i) <= (1/k^2) sum 1/b_i`.

Conditioning on `nu=k` and using iid descendants,

`E[1/S | nu=k] <= H/k`.

Hence, with `a=E[1/nu]`,

`H <= 1 + lambda a H`,

so whenever `lambda a<1`,

`H <= 1/(1-lambda a)`.                                         (B.1)

For the `{2,3}` law, `a=(3-p)/6`, and therefore

`H <= 1/[1-lambda(3-p)/6]` for `lambda<6/(3-p)`.                (B.2)

This is important because for every `p>0` it remains finite at `lambda=2` (indeed `H<=3/p` there). Consequently

`P(B<=eps) <= eps H`,                                            (B.3)

which replaces the useless pointwise lower bound `B>=1-lambda/2` by an average small-escape tail bound that crosses the minimum-degree singularity. This does **not** yet prove the speed derivative sign: the missing step is a compatible expectation bound for the derivative elasticity `-B'/B` or for the Aidekon score. Record (B.1)--(B.3) as an auxiliary lemma, not as source-level monotonicity.

## Attack C — pathwise derivative ordering under branch addition; falsify before use

A tempting strengthening of Attack A would be to say that adding a child not only raises `B`, but lowers the logarithmic elasticity

`R=-B'/B=[1+lambda (sum B_i R_i)/(sum B_i)]/[lambda+sum B_i]`.

That would give a derivative-level stochastic order and might close the lower ratio too. Before using it, test it against the sharp regular-tree envelope. At a fixed `lambda` take two high-escape/low-elasticity branches with

`B=1-lambda/3`, `R=1/(3-lambda)`,

and add one low-escape/high-elasticity branch with

`B=1-lambda/2`, `R=1/(2-lambda)`.

These endpoint pairs are the deterministic regular-degree-3 and regular-degree-2 recursion values. Compute the resulting two-branch and three-branch parent elasticities exactly at a rational lambda in the new strip. If the three-branch value is larger, the hoped-for pointwise derivative order is false and cannot be used; only the escape-probability stochastic order (A.1) survives.

## Deliverable discipline

Persist an exact rational checker only after this note. The checker should certify: (i) all denominator signs and lambda-monotonicities used to freeze the pattern envelopes; (ii) (A.2); (iii) the finite lower-pattern corner inequalities after upper Chebyshev compression; (iv) a strictly positive derivative margin at the final rational endpoint; and (v) the exact counterexample for Attack C. Source-wide status remains OPEN/PARTIAL even if Attack A improves the restricted-family endpoint. External novelty remains UNVERIFIED pending independent review and a broader prior-art search.
