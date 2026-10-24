Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum is not a configurable authenticated native setting on this runtime.**

# PROB10-03 / R14 — exact parametric contraction shift from the certified `alpha=12.75` box

Status: **PARTIAL / SOURCE OPEN / NEW RIGOROUS UPPER-ENDPOINT MOVEMENT**.

Frozen model: `M=floor(alpha N)`, iid `g_a~N(0,I_N)`, `||sigma||_2=sqrt(N)`, and `<g_a,sigma> >= -sqrt(N)` for every `a<=M`, with fixed `alpha` and `N->infinity`. A lower endpoint means SAT with probability tending to one; an upper endpoint means SAT probability tending to zero.

This artifact is a delimited R14 continuation. It does not alter the Campbell–O'Rourke Q1.8 canonical claim and does not overwrite NM13-07/NM13-03 ownership. The already-preserved Campbell handoff remains `artifacts/prob10_2026-09-20/PROB10-03/20260919T2354Z_campbell_q18_r14_handoff.md`, with navigation point `3846db33296cfb6eea59ff7c488929087c7b62a2`.

## 1. Consumed update that changes the correct starting metric

R14's immediately preceding report still used `alpha_U=12.78437096216`. That became stale when the complementary NM13-07 T03 worker subsequently completed the directed-interval whole-box certificate at `alpha=12.75`:

`proofnet24/NM13-07/progress-perceptron/runs/2026-09-20/2026-09-20__t03-certified-alpha1275-contraction.md`

with executed output

`proofnet24/NM13-07/progress-perceptron/runs/2026-09-20/artifacts/t03_alpha1275_interval_contraction.out`.

The archived output proves, on the weighted box centered at

`p_c=0.6457670646889506`, `B_c=4.929229200895245`,

with radii

`r_p=1e-7`, `r_B=4e-6`,

that the fixed preconditioner

`A=[[-1601/20,-493/12500],[-60418/25,-5789/2500]]`

has whole-box contraction constant

`q_* <= 23849/25000 = 0.95396`,

and that on the whole box

`Psi >= 0.0150497744619429886066833 > 0`.

At the center the same output gives

`H in [-1.212554436371290612245951e-12, 1.213143563012573590500445e-12]`,

`alpha in [12.749999999987972073128, 12.75000000001195276213347]`.

Thus the correct certified source bracket entering this R14 iteration is

`6.30297437506 <= alpha_c(-1) <= 12.75`,

with width `6.44702562494`.

No R14 ownership claim is made over NM13-07's certificate; this artifact uses its recorded interval enclosures as hypotheses for a new exact perturbative theorem.

## 2. Attack A — parametric contraction without recomputing a Gaussian integral

Let

`F_0(x)=(H(x), alpha(x)-51/4)`, `x=(p,B)`,

on the NM13-07 weighted box `Q`. Let `D_r=diag(r_p,r_B)`. The certified contraction map is

`T_0(x)=x-A F_0(x)`.

For a density decrement `delta>=0`, define

`a_delta=51/4-delta`,

`F_delta(x)=(H(x), alpha(x)-a_delta)=F_0(x)+(0,delta)`.

The Jacobian is **identical**:

`D F_delta(x)=D F_0(x)`.

Hence the whole-box contraction constant remains exactly the already-certified

`q_* <= 23849/25000 < 1`.

Only the center self-map displacement changes.

### Theorem R14-T03-PARAMETRIC-CONTRACTION-SHIFT

Assume on `Q` the certified Jacobian contraction bound

`sup_Q ||D_r^{-1}(I-A DF_0(x))D_r||_infinity <= q_* <1`.

Assume center residual ceilings

`|H(x_c)| <= E_H`, `|alpha(x_c)-51/4| <= E_alpha`.

For row `i=1,2`, put

`b_i = r_i^{-1} ( |A_{i1}| E_H + |A_{i2}| E_alpha )`,

`s_i = r_i^{-1}|A_{i2}|`.

If

`max_i (b_i+s_i delta) <= 1-q_*`,

then `T_delta(x)=x-AF_delta(x)` maps `Q` to itself and is a contraction in the weighted sup norm. Consequently `F_delta` has a unique zero in `Q`. If additionally `Psi>0` on `Q`, then the complete-second-lift source implication at density `a_delta` is valid at that stationary zero.

### Proof

For every `x,y in Q`, `DF_delta=DF_0`, so the Lipschitz constant of `T_delta` is bounded by the same `q_*<1`. At the center,

`F_delta(x_c)=F_0(x_c)+(0,delta)`.

Therefore rowwise

`|(D_r^{-1} A F_delta(x_c))_i| <= b_i+s_i delta`.

If the maximum is at most `1-q_*`, then for every `x in Q`,

`||D_r^{-1}(T_delta(x)-x_c)||_infinity`
` <= ||D_r^{-1}(T_delta(x)-T_delta(x_c))||_infinity`
`    +||D_r^{-1}(T_delta(x_c)-x_c)||_infinity`
` <= q_* ||D_r^{-1}(x-x_c)||_infinity + (1-q_*) <= 1`.

Thus `T_delta(Q) subset Q`. Banach's fixed-point theorem gives a unique fixed point, equivalently a unique zero of `F_delta`, in `Q`. Since the already-certified whole-box comparison value is strictly positive, the zero has `Psi>0`. QED.

This theorem is exact deterministic analysis. It does not perform a new variational ansatz and does not turn a numerical scout into an endpoint.

## 3. Exact application: source endpoint moves below 12.75

Read directly from the archived center intervals, the sharper rational ceilings

`E_H = 1.214e-12 = 607/500000000000000`,

`E_alpha = 1.203e-11 = 1203/100000000000000`

are valid.

With

`r_p=1/10000000`, `r_B=1/250000`,

and the exact matrix `A` above, exact arithmetic gives

`b_1 = 61034477/62500000000 = 0.000976551632`,

`b_2 = 740438687/1000000000000 = 0.000740438687`,

`s_1 = 394400`,

`s_2 = 578900`,

while

`1-q_* = 1151/25000 = 0.04604`.

The largest decrement allowed by these frozen box/preconditioner bounds is

`delta_max = 45299561313/578900000000000000`
`          = 7.82510991760235...e-8`.

Choose the strictly smaller rational decrement

`delta = 78251/10^12 = 7.8251e-8`.

Then the two shifted center bounds are exactly

`eta_1 <= 1989921627/62500000000 = 0.031838746032`,

`eta_2 <= 46039942587/10^12 = 0.046039942587`,

and both are strictly below `0.04604`; the limiting second-row slack is

`0.04604-0.046039942587 = 57413/10^12 = 5.7413e-8 >0`.

Therefore there is a genuine complete-second-lift stationary zero inside the already-certified box at

`alpha = 12.75-delta = 12.749999921749`,

and the already-certified whole-box bound gives `Psi>0` at that zero. By the same source-matched stationarized fl-RDT implication used for the `12.75` certificate, the exact-radius `kappa=-1` spherical perceptron is asymptotically UNSAT at `alpha=12.749999921749`.

Constraint monotonicity yields the new rigorous upper endpoint

`alpha_U = 12.749999921749`.

Hence the source bracket is now

`6.30297437506 <= alpha_c(-1) <= 12.749999921749`,

with width

`6.447025546689`.

The source-level width improvement in this run is exactly

`7.8251e-8`.

This movement is small but fully rigorous relative to the already-executed NM13-07 interval certificate; it is not a numerical estimate.

## 4. Attack B — test the negation: can the same frozen box yield a macroscopic continuation?

No. The exact formula above gives an obstruction, not merely a failed scout. With the *same* weighted box, fixed preconditioner, certified `q_*`, and center-error bounds, the contraction theorem can certify only

`delta <= delta_max = 7.82510991760235...e-8`.

Thus any attempt to reach `12.70`, `12.60`, or `12.33` without recentering/reboxing is impossible within this certificate architecture. The second weighted row is the active bottleneck. A larger gain requires at least one of:

1. a new center/root and re-centered weighted box;
2. a different preconditioner/radii reducing the second-row amplification;
3. a one-dimensional branch continuation certificate rather than a single frozen box.

This is a certified obstruction to the tempting 'reuse one box all the way down' shortcut.

## 5. Attack C — compare two genuinely different larger-step routes

### C1. One-dimensional stationary transport

NM13-03 proved the exact branch identity

`dPsi/da = (H_p Psi_B-H_B Psi_p)/(H_p alpha_B-H_B alpha_p)`

on a nondegenerate stationary branch and numerically supported continuation to `alpha=12.33`. Combining the **rigorous** anchor

`Psi(12.75) >= 0.0150497744619429886066833`

with a future rigorous branch bound

`dPsi/da <= 0.0354`

would guarantee positivity down to

`a >= 12.75 - 0.0150497744619429886066833/0.0354`
`  = 12.32486512819...`.

Thus objective positivity is not the evident bottleneck for the supported `12.33` endpoint. The missing rigorous step is a directed enclosure proving branch existence/nondegeneracy and the derivative bound throughout the covering interval.

### C2. Direct local certification at `alpha=12.33`

The complementary NM13-03 report gives a numerically supported root rectangle around

`p~=0.6644028185445602`, `B~=6.1589540518255275`,

with positive supported `Psi`. A direct Poincare--Miranda/interval-Newton certificate there would bypass transport entirely. This is materially different from C1: it needs only one endpoint box, but its box is much farther from the already-certified `12.75` anchor and therefore needs a fresh directed Gaussian quadrature/Jacobian enclosure.

Comparison: the source-moving theorem proved here shows that local reboxing is mathematically sound. For the next large step, C2 appears computationally shorter if a tiny endpoint contraction box can be obtained; C1 is more reusable and could certify an interval of densities but requires an overlapping-cover/nondegeneracy proof.

No `12.33` endpoint is promoted in this artifact.

## 6. Current source-status check

The source scope remains unchanged. El Alaoui--Sellke (arXiv:2010.15811) describes the negative-margin FRSB structure as conjectural and its algorithm returns a feasible point on radius `sqrt(qbar N)` with `qbar<1`; this is not the full-radius threshold. Stojnic's 2013 negative-spherical work gives rigorous comparison bounds, while arXiv:2312.16531 puts the model in stationarized fully lifted RDT and explicitly notes that practical operation requires substantial numerical work. Huang--Sellke--Sun (arXiv:2608.29416, submitted 29 August 2026) gives exact thresholds for a dimension-free Lipschitz algorithm class and explicitly distinguishes the non-algorithmic feasible-projection problem as still open. A bounded 20 September 2026 search found no later primary theorem plainly replacing the exact full-radius `kappa=-1` threshold problem. This is dated negative evidence, not a worldwide novelty certificate.

## 7. Exact checker obligation

The matching checker uses only `fractions.Fraction` and verifies:

- the sharper center ceilings dominate the archived interval output;
- the exact row base terms and target-shift slopes;
- `delta<delta_max`;
- both shifted self-map coordinates are `<1-q_*`;
- the new exact upper endpoint and bracket width arithmetic.

The checker is a self-check of the finite rational core, not an independent audit of the NM13-07 interval quadrature or of Stojnic's source theorem.

## 8. Remaining full-scope gap

The exact threshold remains unknown. Current rigorous bracket after this artifact:

`[6.30297437506, 12.749999921749]`.

The strongest supported but not yet outward-certified source candidate in the neighboring T03 work is `12.33`. The next substantial source-moving obligation is therefore not another perturbation inside the frozen `12.75` box; the exact `delta_max` obstruction rules that out. It is either:

- a newly centered directed interval contraction box at a lower density (preferably `12.33`, or an intermediate waypoint if needed), or
- a rigorously covered stationary branch from the `12.75` anchor with nonvanishing determinant and outward-certified transport derivative.

Status remains **OPEN / PARTIAL**. No exact capacity, replica equality, smaller-radius transfer, publication novelty, or independent-validation closure is claimed.