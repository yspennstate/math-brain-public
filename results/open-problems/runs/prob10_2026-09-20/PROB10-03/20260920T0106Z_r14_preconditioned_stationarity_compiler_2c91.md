Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum, and I do not claim otherwise. SOURCE METRIC NO MOVEMENT: rigorous kappa=-1 bracket width `6.48139658710 -> 6.48139658710`. Three materially different attacks: (A) precondition the exact two-scalar stationarity equations and prove a contraction/Newton certificate; (B) test the negation by trying to bypass stationarity, then reject that shortcut against the source theorem; (C) kill two Hermite overlap modes with a new squared-polynomial SAT weight and test the remaining global-overlap obstruction.**

# PROB10-03 — R14 bounded iteration: preconditioned stationarity compiler

Repository/branch: private `yspennstate/math-open-problems` / `master`.

Status: **PARTIAL / SOURCE OPEN / NO NEW RIGOROUS BRACKET ENDPOINT / NEW EXACT CERTIFICATION THEOREM**.

## 1. Contract, continuity, ownership, and consumed state

I obeyed `operations/PROB10_2026-09-20.md` and kept the exact source model frozen:

- `M=floor(alpha N)`;
- `g_a iid N(0,I_N)`;
- `||sigma||_2=sqrt(N)`;
- `<g_a,sigma> >= -sqrt(N)` for every `a<=M`;
- fixed `alpha`, `N->infinity`;
- SAT lower endpoint means probability tends to one and UNSAT upper endpoint means probability tends to zero, with the inherited repository convention unchanged.

The following current repository material was consumed before the new mathematics:

- `operations/PROB10_2026-09-20.md`;
- root `POSTED.md` (posted Ising/zero-margin perceptron work remains excluded but does not close this continuous negative-margin spherical target);
- `operations/claims/CAMPBELL-OROURKE-2022-Q1.8.md` (current shared claim still records R14 historically; this run does not overwrite it);
- immutable Campbell handoff `artifacts/prob10_2026-09-20/PROB10-03/20260919T2354Z_campbell_q18_r14_handoff.md`, preserving the actual intervening successor and its `S=5` metric;
- preceding R14 PROB10 report `runs/prob10_2026-09-20/PROB10-03/20260919T2359Z_r14_overlap_dual_2d_compiler_8f4c.md`, read at creation commit `da25c4266c1a42cd780e1c3596beef972aedf5f0`;
- newest complementary T03 report `proofnet24/NM13-07/progress-perceptron/runs/2026-09-20/2026-09-20__t03-full2-two-scalar-reduction.md`;
- newest complementary T03 theory report `proofnet24/NM13-03/progress-perceptron-theory/runs/2026-09-20/2026-09-20__t03-closed-kernel-miranda-alpha12p75.md` and its executable closed-kernel scout.

The repository master immediately before this final report commit was `de49fc8771a9db261025b7ed5d17df86bb5a3164`, after this run's two checker-artifact commits. No shared root ledger, peer report, or ownership claim was edited.

The earlier R14 history remains live rather than reset: the one-parameter Stojnic-2013 partial-lift family was globally exhausted; the MZZ linear-weight second-moment route has a local obstruction below the present LP lower endpoint; the `N^{-1/2}` direction-net route loses `Theta(N log N)` entropy; plain facet first moment is numerically far too weak; and smaller-radius algorithmic solutions are not full-radius source closure.

## 2. Primary-source rigor / current-status check

I rechecked the designated sources and bounded current follow-ups before treating the numerical capacities as rigorous endpoints.

- El Alaoui--Sellke, arXiv:2010.15811, uses the exact Gaussian spherical model but describes the negative-margin FRSB/Parisi capacity structure conjecturally and its algorithm outputs a feasible point at radius `sqrt(qbar N)` with `qbar<1`; this is not the required radius-`sqrt(N)` threshold theorem.
- Stojnic, arXiv:1306.3980, is the rigorous negative-spherical comparison/upper-bound baseline already used by R14.
- Stojnic, arXiv:2312.16531, develops stationarized fully lifted RDT and reports concrete capacity values after numerical evaluation. Its stationarized strong-duality/feasibility statements explicitly require the non-fixed lifting parameters to satisfy the displayed stationarity system. Thus a floating-point value or an arbitrary nonstationary parameter point is not silently promoted to a rigorous endpoint here.
- Later 2025 work of Winer--Herderschee uses a jammed Parisi **ansatz** to compute `P(SAT)` and match previous threshold computations; 2025 diffusion/sampling work likewise uses replica/statistical-physics formalism. These are useful guides but do not replace the missing rigorous full-radius bracket proof.

A bounded search through 20 September 2026 found no later primary theorem plainly proving a rigorous full-radius SAT/UNSAT equality at `kappa=-1`. This is negative search evidence only, not a global priority certificate.

## 3. Frozen rigorous source metric

Entering and leaving this run, the supported bracket is

`alpha_L = 6.30297437506`,

`alpha_U = 12.78437096216`,

`W = alpha_U-alpha_L = 6.48139658710`.

The lower endpoint is the rigorous Montanari--Zhong--Zhou LP-success threshold after exact normalization; the upper endpoint is R14's globally certified one-parameter Stojnic-2013 partial-lift/Gordon endpoint.

**Before:** `W=6.48139658710`.

**After:** `W=6.48139658710`.

No ansatz, finite mesh, ordinary quadrature, or numerical root is entered into the source metric.

## 4. Attack A — precondition the exact stationary equations instead of certifying four Miranda faces

This is the main theorem-sized advance.

The companion exact reduction writes the complete second-lift fixed-density stationarity problem at `alpha=12.75` as

`F(p,B)=(H(p,B), alpha(p,B)-12.75)=0`,

with the remaining lifting variables reconstructed algebraically and all Gaussian objects reduced to one-dimensional expectations by the companion closed-kernel theorem.

The previous finite-certification plan was axis-aligned Poincare--Miranda on a rectangle. Its numerical face margins for `H` are only of order `10^-5`, so a direct continuous face proof needs fairly tight global evaluation.

I instead proved the following deterministic compiler.

### Theorem R14-T03-PRECONDITIONED-NEWTON

Let

`Q={x: ||D^{-1}(x-x_c)||_infty<=1}`,

let `F:Q->R^2` be `C^1`, and let `A` be invertible. If

`q=sup_Q ||D^{-1}(I-A DF(x))D||_infty <1`

and

`eta=||D^{-1}A F(x_c)||_infty <=1-q`,

then `F` has a unique zero in `Q`.

Proof: `T(x)=x-AF(x)` has derivative `I-A DF`; the two displayed assumptions make `T` a contraction mapping `Q` into itself. Banach gives a unique fixed point, and invertibility of `A` turns the fixed-point equation into `F=0`. The complete proof is in the mathematics-first artifact.

### Exact rational specialization

Take

`p_c=645767064689/10^12`,

`B_c=49292292009/10^10`,

`D=diag(1/1000,1/25)`,

and

`A=[[-1601/20,-493/12500],[-60418/25,-5789/2500]]`.

It is sufficient to prove on the whole weighted box

`H_p in [-131/5000,-63/2500]`,

`H_B in [21/50000,23/50000]`,

`alpha_p in [53/2,136/5]`,

`alpha_B in [-23/25,-43/50]`.

Exact enumeration of all 16 interval-Jacobian vertices gives

`q <= 215437/1250000 = 0.1723496`,

so

`1-q >= 1034563/1250000 = 0.8276504`.

If the center is enclosed only to

`|H(p_c,B_c)| <= 1/200000`,

`|alpha(p_c,B_c)-12.75| <= 1/1000`,

then exact arithmetic gives

`eta <= 43969/100000 = 0.43969 < 0.8276504 <=1-q`.

Hence these six broad interval statements alone force a unique true stationary root at `alpha=12.75` inside the box.

For the comparison value, I also proved that the three box bounds

`Psi(p_c,B_c)>=0.014`, `|Psi_p|<=2`, `|Psi_B|<=0.1`

imply uniformly

`Psi>=0.014-2(0.001)-0.1(0.04)=0.008>0`.

Thus, **if** the nine stated enclosure inequalities are rigorously validated and the reconstructed branch remains interior, the existing source-matched second-full implication would certify

`alpha_U=12.75`,

shrinking the bracket width to

`6.44702562494`

by `0.03437096216`.

That implication is conditional. The current rigorous endpoint stays `12.78437096216`.

### Why this changes the finite obligation

The new route no longer asks for a `~3e-5` fixed sign on an entire Miranda face. It asks for four deliberately broad derivative intervals plus loose center residual bounds on a smaller box. The finite proof burden is therefore converted from delicate face-sign preservation to a robust, preconditioned Jacobian enclosure.

## 5. Attack B — try to bypass stationarity; source theorem blocks the shortcut

I tested the negation of the current certification philosophy: perhaps one could simply choose an explicit nearby lifted parameter point with positive comparison value and obtain an upper bound, avoiding any true root.

This does **not** follow from the cited 2023 stationarized fl-RDT theorem. The relevant strong-duality/feasibility statements impose stationarity of the non-fixed lifting parameters before the conclusion is invoked. Therefore the `F=0` obligation is genuine for this source route.

This is a useful certified obstruction: a high-precision positive `Psi` at an arbitrary point is insufficient, so the run should spend its effort making the stationary certificate rigorous rather than manufacture more floating-point values.

## 6. Attack C — a new SAT-side weight killing two Hermite overlap modes

To test whether the preceding exponential-quadratic weighted-overlap failure was merely family-specific, I considered the different nonnegative family

`w_{a,b}(x)=(1+a x+b x^2)^2 1{x>=-1}`.

With `m_j=E[w(G)He_j(G)]`, the conditions

`m_1=0`, `m_2=0`

kill the first two nonconstant terms in Mehler's overlap expansion. This is stronger local cancellation than the previous one-moment design.

I derived an exact one-dimensional reduction for the full correlated kernel. Conditional on `X=x`, write `Y=qx+sqrt(1-q^2)Z` and `t=(-1-qx)/sqrt(1-q^2)`. The standard truncated moments obey

`R_0=Phi(-t)`, `R_1=phi(t)`,

`R_j=t^(j-1)phi(t)+(j-1)R_{j-2}`.

Because `w` has degree four on its support, `E[w(Y)|X=x]` is an explicit combination of `R_0,...,R_4`; hence the two-replica kernel requires only one outer Gaussian integral. This reduction is exact.

The numerical-only scout finds two `m_1=m_2=0` branches,

`(a,b) ~= (-0.72672433646, 0.43651047279)` and

`(a,b) ~= (-0.65009995918,-0.19471716592)`.

Their numerical global positive-overlap ceilings are only about `2.12461` and `1.36662`, respectively, both far below the already rigorous LP lower endpoint `6.30297437506`. These are diagnostics, not certified thresholds. They strongly disfavor further effort on local Hermite cancellation without a new mechanism controlling large positive overlap.

## 7. Executed tests

Mathematics was written first in

`artifacts/prob10_2026-09-20/PROB10-03/20260920T0054Z_r14_preconditioned_stationarity_certificate.md`

at commit

`2f1d3348b6e699854e100fad6b9b625bc122edf0`.

Only afterward I created and executed the self-check/scout

`artifacts/prob10_2026-09-20/PROB10-03/20260920T0057Z_r14_preconditioned_stationarity_scout.py`

at commit

`32b39eeab63bf6596ce7d3360cb9e94b84e4da6c`,

with actual output archived as

`artifacts/prob10_2026-09-20/PROB10-03/20260920T0057Z_r14_preconditioned_stationarity_scout.out`

at commit

`de49fc8771a9db261025b7ed5d17df86bb5a3164`.

The exact part verifies the rational contraction arithmetic and ends with the exact values

`q=215437/1250000`, `eta=43969/100000`, `eta<1-q`.

The **NUMERICAL_ONLY** small-box scout reports sampled ranges

`H_p in [-0.02609011,-0.02533621]`,

`H_B in [0.000427699,0.000448038]`,

`alpha_p in [26.66684,27.00818]`,

`alpha_B in [-0.906290,-0.871949]`,

comfortably inside the proposed broad rational certificate intervals. It reports sampled scaled contraction norm at most `0.097716`, center `Psi ~=0.015201`, and broad `Psi` derivative margins. These computations support the route but do not replace interval proof.

The same executable carries out the separate squared-polynomial overlap scout. Output ends

`ALL_SELF_CHECKS_PASS`.

Self-checks are not independent audits.

## 8. Source metric versus auxiliary movement

### Source metric

`alpha_L: 6.30297437506 -> 6.30297437506`.

`alpha_U: 12.78437096216 -> 12.78437096216`.

`width: 6.48139658710 -> 6.48139658710`.

**Movement: none.**

### Auxiliary / mechanism movement

Before this run, the strongest second-full candidate at `12.75` had an exact two-scalar reduction and a closed Gaussian kernel but required continuous Poincare--Miranda face signs and `Psi>0` on a rectangle.

After this run, there is a proved deterministic contraction compiler reducing the root obligation to four broad interval Jacobian inclusions plus two loose center residual inequalities on a smaller box, together with a very loose three-inequality `Psi` positivity certificate. Exact rational arithmetic proves that these bounds would have a contraction margin

`(1-q)-eta >= 0.8276504-0.43969 = 0.3879604`.

This is meaningful finite-certification progress but is not a bracket endpoint until the analytic interval hypotheses are validated.

## 9. Remaining full-scope gap and next within-problem step

The immediate source-moving obligation is now finite and explicit:

1. derive/enclose the derivatives of the closed one-dimensional Gaussian kernel needed for `H_p,H_B,alpha_p,alpha_B,Psi_p,Psi_B`;
2. use outward-rounded quadrature/Taylor bounds on the small weighted box to prove the nine broad inequalities stated above;
3. verify the reconstructed `(p,D,gamma)` remains uniformly in the complete second-lift interior branch;
4. then invoke the source theorem and only then promote `12.75` to the rigorous upper endpoint.

If any proposed derivative interval fails under rigorous enclosure, that failure itself identifies which coordinate/preconditioner must be changed; the next run stays on PROB10-03 and does not rotate to an unrelated target.

Within the 20 September PROB10 refocus, the source metric has now been unchanged in two consecutive R14 iterations. Historical R14 stagnation remains preserved as history rather than erased. If the next bounded iteration is again source-metric unchanged with the same remaining obligation, the PROB10 contract requires an explicit obstruction and a materially different method within this problem rather than another renamed certification lemma.

Source status remains **OPEN / PARTIAL**. There is no independent-validation closure: neither this theorem nor a `12.75` endpoint has the two required other-track audits.

No scheduler cadence/state, email, Drive item, public post, permission, workflow, shared claim, or peer file was changed.

```yaml
ledger_delta:
  worker: R14
  parent: PROB10-03
  target: "negative spherical Gaussian perceptron, kappa=-1, radius sqrt(N)"
  status: "PARTIAL / SOURCE OPEN / exact certification theorem proved"
  source_metric: "rigorous alpha_upper-alpha_lower"
  before:
    alpha_lower: "6.30297437506"
    alpha_upper: "12.78437096216"
    width: "6.48139658710"
  after:
    alpha_lower: "6.30297437506"
    alpha_upper: "12.78437096216"
    width: "6.48139658710"
    movement: "none"
  conditional_candidate:
    alpha_upper: "12.75"
    width: "6.44702562494"
    improvement: "0.03437096216"
    promoted: false
  auxiliary_movement:
    theorem: "R14-T03-PRECONDITIONED-NEWTON"
    exact_contraction_q_upper: "215437/1250000"
    exact_center_eta_upper: "43969/100000"
    exact_margin_1_minus_q_minus_eta: "0.3879604"
    second_attack: "nonstationary shortcut rejected by source stationarity hypothesis"
    third_attack: "squared-polynomial m1=m2=0 family reduced exactly to 1D overlap integral; numerical global obstruction remains"
  executed_self_check:
    source_commit: "32b39eeab63bf6596ce7d3360cb9e94b84e4da6c"
    output_commit: "de49fc8771a9db261025b7ed5d17df86bb5a3164"
    marker: "ALL_SELF_CHECKS_PASS"
    independent_audit: false
  remaining_obligation: "rigorous outward-rounded derivative/center/Psi enclosures on the small preconditioned box; interior-branch validation; then source implication"
  continuity:
    prior_r14_report_commit: "da25c4266c1a42cd780e1c3596beef972aedf5f0"
    campbell_handoff_preserved: true
    shared_campbell_claim_edited: false
  runtime:
    model: "GPT-5.6 Sol"
    reasoning: "UNVERIFIED"
    requested_gpt6_maximum_native_selector_available: false
```
