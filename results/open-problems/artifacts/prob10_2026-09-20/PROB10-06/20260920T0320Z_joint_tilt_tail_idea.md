# PROB10-06 idea before code — keep the mixture coordinate coupled to p

Actual runtime metadata: model family shown to this worker is GPT-5.6 Sol; authenticated reasoning-effort telemetry is unavailable, so reasoning level is UNVERIFIED and GPT-6/maximum is not claimed.

Parent problem: Lyons–Pemantle–Peres speed monotonicity for biased random walk on a supercritical Galton–Watson tree without leaves. Parent-bias convention: at a k-child vertex, parent has weight lambda and each child weight 1; increasing lambda points toward the root. Child-bias beta=1/lambda increases drift away from the root. The source-wide conjecture remains OPEN.

Consumed own state: `runs/prob10_2026-09-20/PROB10-06/20260920T0221Z_type_conditioned_child_pattern_bridge_b8e41d72.md`, which proves all mixtures `P(nu=2)=1-p, P(nu=3)=p` through lambda=1.851 by type-conditioned escape/log-derivative envelopes. Consumed complementary state: `proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T01-41-00Z__branch-addition-ratio-coupling.md`, especially the proved ratio `3/4 <= c_3/c_2 <= 1` and its already-covered tail rectangles. This run will not reclaim those results.

## Attack A — preserve the p–theta relation instead of taking the global worst theta

For the {2,3} family, write

`C=(1-p)c_2+p c_3`, `t=c_3/c_2`, `theta=p c_3/C=p t/(1-p+p t)`, `M=2+theta`.

The exact derivative reduction is

`ell'_lambda = 2( lambda theta' - (2+theta) )/(2+theta+lambda)^2`,

with

`theta'=theta(1-theta) Delta`, `Delta=h_2/c_2-h_3/c_3`.

Earlier all-mixture certificates decoupled theta from p and used the global minimum of `(2+theta)/(theta(1-theta))`. That is wasteful in the tails: the branch-addition result gives `3/4<=t<=1`, hence

`3p/(4-p) <= theta <= p`.

Let `g(theta)=theta(1-theta)/(2+theta)`. Its unique maximizer is `theta_*=sqrt(6)-2`. Therefore:

- for small p with `p<=theta_*`, `g(theta)<=g(p)=p(1-p)/(2+p)`;
- for large p with `3p/(4-p)>=theta_*`, `g(theta)<=g(3p/(4-p))`.

The plan is to combine these exact p-dependent factors with the previous child-pattern upper bound on Delta, freezing the pattern rectangles only over the new lambda strip. Candidate gains from hand calculation are:

- at lambda<=19/10, widen the already-known NM13 tails from `p<=1/8 or p>=9/10` to at least `p<=3/20 or p>=5/6`;
- at lambda<=983/500, widen the old rare tails from `p<=1/30 or p>=35/36` to at least `p<=1/27 or p>=22/23`.

These are source-level restricted-region gains if the exact rational checker succeeds. They do not close the parent conjecture.

## Attack B — Laplace-transform branch-addition identity

For `a=lambda-1`, `L(t)=E exp(-tB)`, `M(t)=E[B exp(-tB)]`, `N(t)=E[U exp(-tB)]`, the n-branch quantities satisfy

`c_{n-1}=int_0^infty exp(-a t) M(t) L(t)^(n-1) dt`,

`h_{n-1}=int_0^infty t exp(-a t) (M(t)+a N(t)) L(t)^(n-1) dt`.

Thus `h_2/c_2-h_3/c_3` is a covariance-type difference under a measure tilted by one additional factor L. This could in principle avoid the pathwise singularity at lambda=2. The immediate obstruction is that a rigorous monotonicity/Lipschitz bound for `z(t)=t(1+aN(t)/M(t))` relative to the decreasing L(t) is not currently available; without it the covariance has no certified sign/size. This route is recorded for future work but is not used as a theorem here.

## Attack C — near-critical expansion

As lambda approaches `m=2+p` from below, B tends to 0 and the speed formula formally approaches the deterministic first-order form `(m-lambda)/(m+lambda)`, suggesting a negative derivative near criticality. To turn this into a bridge across lambda=2 one needs a quantitative uniform remainder for both c_k and c_k', equivalently moment control on U=-B'. The existing pathwise cone uses the minimum degree and blows up at lambda=2, so this expansion currently lacks the exact denominator/truncation estimate required by the owner contract. No near-critical theorem is claimed in this run.

Only after Attack A is algebraically frozen will an exact checker be written. The checker will verify monotonicity of every pattern envelope across each lambda strip and certify the final rational inequalities for the stated p rectangles.