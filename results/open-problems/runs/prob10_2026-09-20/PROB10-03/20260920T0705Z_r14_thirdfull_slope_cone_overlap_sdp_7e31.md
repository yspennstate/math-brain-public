Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested but is not an authenticated configurable native setting. SOURCE METRIC NO MOVEMENT this invocation after consuming the current companion endpoint: rigorous/repository-supported `kappa=-1` bracket width `6.01666047494 -> 6.01666047494`. Three materially different attacks: (A) exact third-full q-sector/slope-cone reduction, (B) exact MZZ weighted-overlap curvature obstruction, (C) exact Shor-SDP dual-feasibility negation test.**

# PROB10-03 — R14 bounded substantive iteration: third-full slope cone, overlap cap, SDP no-go

Repository / branch: private `yspennstate/math-open-problems` / `master`.

Status: **PARTIAL / SOURCE OPEN / NO NEW SOURCE ENDPOINT THIS RUN / NEW EXACT THIRD-FULL REDUCTION AND TWO CERTIFIED ROUTE OBSTRUCTIONS**.

## 1. Contract, continuity, exclusions, and consumed state

This run obeyed `operations/PROB10_2026-09-20.md`.  No scheduler state, cadence, notification, permission, workflow, email, Drive item, public post, shared root ledger, peer report, or peer claim was modified.

Read before new mathematics:

- `operations/PROB10_2026-09-20.md`;
- root `POSTED.md`; the owner's posted Ising/zero-margin perceptron work remains excluded and does not close this continuous negative-margin spherical target;
- current Campbell–O'Rourke Q1.8 claim `operations/claims/CAMPBELL-OROURKE-2022-Q1.8.md`, still naming R14; this run does not overwrite it;
- preserved immutable Campbell handoff `artifacts/prob10_2026-09-20/PROB10-03/20260919T2354Z_campbell_q18_r14_handoff.md`, whose navigation point includes `3846db33296cfb6eea59ff7c488929087c7b62a2`;
- historical perceptron handoff/rotation record `operations/claims/I0089.md` and older R14 negative-margin reports, including the MZZ lower-bound recovery and the exhausted one-parameter partial-lift route;
- newest preceding own PROB10 report `runs/prob10_2026-09-20/PROB10-03/20260920T0558Z_r14_parametric_shift_source_move_7b2e.md`;
- newer complementary T03 reports, especially NM13-03's a-posteriori exact-sphere certificate at `12.319635` and NM13-07's uniform micro-continuation certificate at `12.31963485`.

The owner-directed PROB10 refocus is treated as a delimited complementary route.  I do not reset history and do not modify the still-live Campbell claim.

## 2. Exact source model and current source/literature scope

The frozen source model is

`M=floor(alpha N)`, iid `g_a~N(0,I_N)`, `||sigma||_2=sqrt(N)`,

`<g_a,sigma> >= -sqrt(N)` for all `a<=M`, fixed `alpha`, `N->infinity`.

A lower endpoint means SAT probability tends to one.  An upper endpoint means SAT probability tends to zero.  Radius-changing algorithms, Ising weights, replica/full-RSB numerics, and unsupported finite-lift stationary points are not source endpoints.

Primary/source navigation was refreshed against:

- El Alaoui–Sellke, arXiv:2010.15811;
- Stojnic, arXiv:1306.3980;
- Stojnic, arXiv:2312.16531;
- Montanari–Zhong–Zhou, arXiv:2110.15824 / PTRF 188 (2024);
- Annesi–Malatesta–Zamponi, arXiv:2410.06717;
- current 2026 follow-up screening, including algorithmic work distinct from unrestricted full-radius satisfiability.

The scope distinction remains unchanged: El Alaoui–Sellke's negative-margin construction depends on conjectural FRSB/Parisi structure and uses a smaller output radius; the 2024 full-RSB transition paper is an ansatz calculation; Stojnic's 2023 paper supplies the stationarized fully lifted framework and closed parameter relations but its concrete second-/third-full capacity table is numerical; current algorithmic threshold results do not characterize all feasible exact-radius projections.  A bounded 20 September 2026 search found no later rigorous theorem plainly identifying the exact unrestricted `kappa=-1` full-radius threshold.  This is dated negative search evidence, not a worldwide priority certificate.

## 3. Consumed metric update before this run

R14's preceding own report ended at the then-current `alpha_U=12.749999921749`, but that value is stale relative to newer complementary work on master.

NM13-03 subsequently certified a source-matched complete-second stationary point at `alpha=12.319635`, using an a-posteriori objective localization bound rather than whole-box objective positivity.  NM13-07 then rigorously micro-continued that exact box to

`alpha_U = 12.31963485`,

with positive comparison lower bound

`1783301405311 / 1090044380000000000000 > 0`.

Those reports explicitly remain **PARTIAL / CANDIDATE_FULL / INDEPENDENT REVIEW PENDING**, so this is not publication-level closure; nevertheless it is the strongest current repository-supported exact-sphere upper certificate entering this invocation.  I consume it without attributing it to R14 and without editing its files.

The retained rigorous SAT lower endpoint is

`alpha_L = 6.30297437506`

from the exact normalization of Montanari–Zhong–Zhou's LP-success theorem.

Thus this invocation enters with

`[alpha_L,alpha_U]=[6.30297437506,12.31963485]`,

width

`W=6.01666047494`.

## 4. Attack A — exact third-full slope-cone reduction

The complete proof was written before the checker in

`artifacts/prob10_2026-09-20/PROB10-03/20260920T0703Z_r14_thirdfull_slope_cone_overlap_obstructions.md`

at creation commit

`3e29ce5f131fa16a3227148997b85a40686282e6`.

The point is to move beyond the now essentially saturated complete-second endpoint rather than shave more decimals from it.

### 4.1 Source equations

For Stojnic's `r=3` stationarized full lift, assume the strict interior

`0<p3<p2<1`, `0<q3<q2<1`, `c2,c3,gamma_p>0`.

Define secant slopes

`r2=q3/p3`,

`r1=(q2-q3)/(p2-p3)`,

`r0=(1-q2)/(1-p2)`.

Rewriting the source's exact equations (142), (145), (147) gives

`gamma_p=(1/2) r0 sqrt(r2)/r1`,

`c3=(r1-r2)/((p2-p3)r1 sqrt(r2))`,

`c2=(r0 r2-r1^2)/((1-p2)r0 r1 sqrt(r2))`.              (4.1)

### 4.2 New exact equivalence / positivity cone

I proved the converse as well: (4.1) is not merely necessary.  In the strict domain it is equivalent to the original stationarity equations in `q3`, `q2`, and `gamma_p`.

Writing

`A2=2 gamma_p-c2(1-q2)`,

`A3=A2-c3(q2-q3)`,

the reconstructed variables satisfy exactly

`A2=r1/sqrt(r2)`, `A3=sqrt(r2)`,

hence

`q3/A3^2=p3`,

`(q2-q3)/(A2 A3)=p2-p3`,

and

`(1-q2)/(2 gamma_p A2)+(q2-q3)/(A2 A3)+p3=1`.

Therefore the three q-sector equations are automatic after reconstruction.

More importantly,

`c3>0 iff r1>r2`,

`c2>0 iff r1^2<r0 r2`.

Thus every genuine positive-`c` third-full stationary point obeys the strict algebraic cone

`r1>r2`, `r1^2<r0 r2`,

which in turn implies

`r0>r1>r2>0`.                                           (4.2)

So the three secant slopes are strictly ordered and satisfy a stronger middle log-convexity inequality.

### 4.3 Exact five-scalar compiler

Choose only

`(p2,p3,r1,r2,B)`.

Set

`q3=p3 r2`,

`q2=q3+(p2-p3)r1`,

`r0=(1-q2)/(1-p2)`,

reconstruct `gamma_p,c2,c3` by (4.1), and set

`gamma_sq=c2/(4B)`.

On the strict cone (4.2), all three q-sector stationarity equations are already satisfied.  The full third-level numerical/certification problem is therefore reduced from the original eight non-fixed scalar variables to the remaining five source stationarity/comparison obligations in `(p2,p3,r1,r2,B)`.

This is the main auxiliary movement of the run.  It is exact; no stationary root or new capacity endpoint is claimed.

### 4.4 Numerical-only source-table sanity check

Stojnic's rounded `kappa=-1` third-full table has approximately

`p3=.6252`, `p2=.9691`, `q3=.2500`, `q2=.6536`,

`c3=3.03`, `c2=12.1`, `gamma_p=3.0237`, `gamma_sq=.0835`, `alpha=12.29`.

The new coordinates give

`r2≈0.3998720`, `r1≈1.1735970`, `r0≈11.2103560`,

with wide cone margins

`r1-r2≈0.773725`,

`r0*r2-r1^2≈3.10538`.

Reconstruction gives approximately

`gamma_p≈3.02017`, `c3≈3.03162`, `c2≈12.0797`,

consistent with the source's coarse rounding.  This only tests the algebra.  The table's `12.29` remains **NUMERICAL ONLY** and is not promoted.

## 5. Attack B — exact overlap obstruction: MZZ's second-moment lower route cannot beat the LP endpoint at kappa=-1

This attacks the lower side rather than assume the MZZ overlap functional is worth further global optimization.

MZZ Definition 1 uses the unique positive `c*=c*(kappa)` solving

`c* Q(kappa+c*)=phi(kappa+c*)`

and the weight

`w(x)=exp(-c*x) 1{x>=kappa}`.

For the correlated kernel `K(q)=E_q[w(G1)w(G2)]`, let

`m_j=E[w(G)H_j(G)]`.

Mehler's expansion gives

`K(q)=sum_j m_j^2 q^j/j!`.

Completing the square and using the defining equation for `c*` yields exactly

`m1=0`,

`m2=kappa c* m0`.

Consequently their overlap exponent satisfies

`Psi''(0)=1/delta-kappa^2 c*^2`.                         (5.1)

But the definition of `delta_lb(kappa)` explicitly requires `Psi''(0)>0`.  Therefore

`delta_lb(kappa) <= 1/(kappa^2 c*(kappa)^2)`.            (5.2)

At `kappa=-1`, I proved elementarily that `c*(-1)>1/2`.  The proof uses MZZ's uniqueness/monotonicity result plus

`(1/2)Phi(1/2)<phi(1/2)`,

which is certified from the rational bounds

`phi(0)>199/500`, `phi(0)<2/5`,

`exp(-1/8)>2711/3072`,

and

`2*(199/500)*(2711/3072)=539489/768000>7/10`.

Hence

`delta_lb(-1)<4`.

By contrast MZZ's LP threshold is

`delta_lin(-1)=1/Phi(-1)>4`,

because `Phi(-1)=Q(1)<phi(1)<1/4` (elementary Mills plus `e>8/3`, `pi>3`).

Therefore the particular MZZ weighted second-moment theorem is **rigorously dominated by the LP lower endpoint at kappa=-1**.  This closes a previously open tactical question in the R14 history: there is no reason to spend a later run globally certifying their `delta_lb(-1)` in the hope of beating `6.30297437506`.

This does not rule out different overlap weights or a stronger second-moment construction; it rules out the exact MZZ Definition-1 route.

## 6. Attack C — dual-feasibility negation: standard first Shor SDP is identically feasible

A different tempting route is to lift the sphere to `X=xx^T` and drop rank one.  The standard degree-two/Shor relaxation has

`Tr X=1`,

`[[1,x^T],[x,X]] >= 0`,

`Gx>=-1`.

For every deterministic `G`, every `N`, and every number of constraints, the point

`x=0`, `X=I_N/N`

is feasible.  The block matrix is positive definite, `Tr X=1`, and `Gx=0>=-1`.

Thus this relaxation can **never** certify UNSAT at any density.  The negative right-hand side causes the degree-two relaxation to lose the exact sphere/nonzero-direction content at the origin.  Any useful SDP/SOS dual route must retain genuinely higher-order/localizing coupling between the inequalities and the sphere; running a stronger solver on the same first Shor relaxation cannot help.

This is a full deterministic obstruction, not a numerical failure.

## 7. Executed checker

After the proof artifact was committed, I created and executed an exact symbolic/rational self-check.

Checker:

`artifacts/prob10_2026-09-20/PROB10-03/20260920T0703Z_r14_thirdfull_slope_cone_checker.py`

creation commit

`198c15612584bafa786e9ad5d45b4eb80bde29de`.

Archived actual output:

`artifacts/prob10_2026-09-20/PROB10-03/20260920T0703Z_r14_thirdfull_slope_cone_checker.out`

creation commit

`8ed5639b29f5081da8290e9b483e16d5f694e6b7`.

The checker verifies symbolically:

- `A2=r1/sqrt(r2)` and `A3=sqrt(r2)`;
- all three reconstructed q-sector stationarity identities exactly;
- exact equivalence with the source forms of `gamma_p,c2,c3`;
- the rational inequalities used in `c*(-1)>1/2`;
- the elementary LP `>4` comparison;
- a finite exact sanity witness for the Shor relaxation.

It also performs a clearly labeled **NUMERICAL_ONLY** consistency calculation on the source's rounded third-full table.  The archived output ends

`ALL_EXACT_SELF_CHECKS_PASS`.

These are self-checks, not independent audits.

## 8. Source metric and auxiliary movement

### Source metric

After consuming the newer companion certificate, before this run:

`alpha_L=6.30297437506`,

`alpha_U=12.31963485`,

`W=6.01666047494`.

After this run:

`alpha_L=6.30297437506`,

`alpha_U=12.31963485`,

`W=6.01666047494`.

**Source movement: none.**

No ansatz, source-table number, unsupported stationary point, or simulation is promoted.

### Auxiliary / mechanism movement

1. **Third-full exact dimension reduction:** three of the eight non-fixed scalar stationarity variables are algebraically eliminated; remaining search is five-scalar.
2. **New strict admissibility cone:** genuine positive `c2,c3` requires `r1>r2` and `r1^2<r0 r2`, hence `r0>r1>r2`.
3. **Lower-route obstruction:** MZZ's exact Definition-1 weighted second moment obeys `delta_lb(-1)<4<delta_lin(-1)`, so it cannot improve the current lower endpoint.
4. **Dual-route obstruction:** the standard first Shor SDP is identically feasible for every instance.

## 9. Remaining full-scope gap and next bounded step

The exact asymptotic satisfiability threshold remains unknown; status is **OPEN / PARTIAL**.

The complete-second mechanism has essentially reached its own comparison zero near the current `12.31963485` certificate, so another decimal-shaving continuation is not a substantive next method.

The highest-value source-moving continuation from this run is now explicit:

1. write the remaining five **original** third-full stationarity/comparison residuals after the exact reconstruction `(p2,p3,r1,r2,B) -> (q2,q3,c2,c3,gamma_p,gamma_sq)`;
2. derive analytic derivatives and outer-tail bounds for the nested `U4 -> log E_{U3}` Gaussian kernel before any optimization;
3. only then perform directed interval root/objective certification around the source's rounded `kappa=-1` third-full candidate;
4. keep `alpha≈12.29` numerical until all residuals, positivity/interiority hypotheses, and the inherited source comparison implication are certified and independently audited.

On the lower side, do not repeat MZZ Definition-1 global overlap optimization; a genuinely different weight or different existence mechanism is required.  On the dual side, do not repeat the first Shor SDP; a higher SOS/localizing construction is required.

```yaml
ledger_delta:
  worker: "R14 / PROB10-03"
  target: "negative-margin spherical Gaussian perceptron capacity at kappa=-1"
  status: "PARTIAL / OPEN"
  runtime:
    model: "GPT-5.6 Sol"
    reasoning: "UNVERIFIED"
    gpt6_maximum_native_setting: "not configurable/authenticated on exposed runtime"
  consumed_companion_endpoint:
    alpha_U: "12.31963485"
    source: "NM13-07 certified micro-continuation; independent review pending"
  source_metric: "alpha_U-alpha_L"
  before:
    alpha_L: "6.30297437506"
    alpha_U: "12.31963485"
    width: "6.01666047494"
  after:
    alpha_L: "6.30297437506"
    alpha_U: "12.31963485"
    width: "6.01666047494"
  movement: "none"
  new_exact_results:
    - "R14-T03-THIRDFULL-SLOPE-CONE: exact five-scalar q-sector compiler and r1>r2, r1^2<r0*r2"
    - "R14-T03-MZZ-CURVATURE-CAP: delta_lb(-1)<4<delta_lin(-1)"
    - "R14-T03-SHOR-NOGO: standard degree-two/Shor relaxation is feasible for every instance"
  artifacts:
    proof: "artifacts/prob10_2026-09-20/PROB10-03/20260920T0703Z_r14_thirdfull_slope_cone_overlap_obstructions.md @ 3e29ce5f131fa16a3227148997b85a40686282e6"
    checker: "artifacts/prob10_2026-09-20/PROB10-03/20260920T0703Z_r14_thirdfull_slope_cone_checker.py @ 198c15612584bafa786e9ad5d45b4eb80bde29de"
    output: "artifacts/prob10_2026-09-20/PROB10-03/20260920T0703Z_r14_thirdfull_slope_cone_checker.out @ 8ed5639b29f5081da8290e9b483e16d5f694e6b7"
  remaining_gap: "certify the remaining five third-full stationarity/comparison equations and source implication; exact threshold still unknown"
```
