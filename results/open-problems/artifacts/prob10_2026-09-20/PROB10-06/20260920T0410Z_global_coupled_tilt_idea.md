Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — requested GPT-6 maximum is prompt-only here, and no authenticated reasoning-effort telemetry or binding model selector is exposed, so GPT-6/maximum is not claimed.**

# PROB10-06 idea before code — use the p–theta coupling globally, not only in the tails

Parent target remains the Lyons–Pemantle–Peres speed-monotonicity conjecture for biased random walk on a supercritical Galton–Watson tree **without leaves**. Child-bias beta weights each child relative to the parent and increases drift away from the root; this track uses reciprocal parent-bias lambda=1/beta, so the conjectural sign is ell'_lambda<=0 on 0<=lambda<E nu.

## Consumed state

The newest own report is `runs/prob10_2026-09-20/PROB10-06/20260920T0348Z_joint_tilt_tail_rectangles_6c4e19a2.md`. It proves for `P(nu=2)=1-p, P(nu=3)=p`:

- all p through lambda=1851/1000;
- p<=31/200 or p>=41/50 through lambda=19/10;
- p<=1/27 or p>=22/23 through lambda=983/500.

It also records the exact adjacent-family derivative reduction

`-ell'_lambda = 2(2+theta)[1-lambda g(theta) Delta]/(2+theta+lambda)^2`,

where `g(theta)=theta(1-theta)/(2+theta)`, `Delta=h_2/c_2-h_3/c_3`, and the branch-addition ratio bound gives

`3p/(4-p) <= theta <= p`.

The previous all-p strip certificate nevertheless decoupled the dangerous `g(theta)` from p by replacing it with its global maximum. The last run exploited the coupling only on far tails. The present idea is to use the same coupling on the whole p interval.

## Main route: global coupled p–theta certificate

For `p<=11/25`, we have `p<sqrt(6)-2`, hence the entire permitted theta interval lies on the increasing branch of g and

`g(theta)<=g(p)=p(1-p)/(2+p)`.

For `p>=11/25`, use the exact global maximum

`max g = 1/(5+2 sqrt(6)) < 101021/1000000`.

Thus no irrational case split is needed in the exact checker. Reuse the type-conditioned child-pattern box bounds from the 02:21 report, but widen the lambda strip from `[1847/1000,1851/1000]` to `[1851/1000,927/500]`. If the same endpoint monotonicities hold on that strip, then every possible `Delta` is bounded by one of 16x32 rational corner differences.

The finite proof obligations become, for every corner pair:

1. on `p in [0,11/25]`, prove
   `1 - (927/500) * [p(1-p)/(2+p)] * Delta_corner(p) > 0`;
2. on `p in [11/25,1]`, prove
   `1 - (927/500) * (101021/1000000) * Delta_corner(p) > 0`.

If exact Bernstein certificates pass, then every `{2,3}` mixture is strictly speed-decreasing through parent bias lambda=927/500=1.854. This would be a genuine restricted-family source-region gain from the current all-p endpoint 1.851.

## Two materially different backup attacks

### Attack B — direct ratio differentiation rather than bounding h_2/c_2 and h_3/c_3 separately

Write `t=c_3/c_2`. Then `Delta=(log t)'`. The speed derivative can be expressed directly through `t,t'` and p. Try to control `t'` by differentiating the branch-addition identity for `c_4/c_3` under a common coupling. This could avoid the independent upper/lower corner choices that make the current Delta box loose. The likely obstruction is that the derivative integrand changes sign under branch addition; a monotone comparison for c itself does not automatically survive differentiation.

### Attack C — distribution-sensitive two-level escape truncation

Instead of pathwise q<=1/(2-lambda), propagate conditional expectations of `(B,U)` for one more generation, keeping the binomial type count. A successful weighted contraction would yield a truncation error and could eventually cross lambda=2 for p>0. The critical falsification test is the linearized one-step operator on the `(B,U)` error cone. If its spectral radius exceeds one for central p near lambda=1.854, this scalar/two-coordinate truncation is not yet a proof route and the obstruction should be recorded explicitly.

The main route will be checked first. Numerical scanning is only exploratory; any claimed finite inequality will be rechecked with exact rational arithmetic and archived output.