Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested but is not an authenticated configurable native setting. SOURCE METRIC NO MOVEMENT: rigorous/repository-supported `kappa=-1` bracket width `6.01666047494 -> 6.01666047494`. Three materially different attacks this run: (1) common-scale Euler/homogeneity attack on the complete third-full objective; (2) exact residual-dependency / equation-count negation attack; (3) post-proof four-dimensional numerical falsification and conditioning scout.**

# PROB10-03 — R14 bounded substantive iteration: scale-Euler identity and four-scalar third-full capacity compiler

Repository / branch: private `yspennstate/math-open-problems` / `master`.

Status: **PARTIAL / SOURCE OPEN / NO NEW RIGOROUS SOURCE ENDPOINT / NEW EXACT THIRD-FULL REDUCTION**.

## 1. Contract, continuity, ownership, and exclusions consumed

Read before new mathematics:

- `operations/PROB10_2026-09-20.md`;
- root `POSTED.md`; the owner's posted Ising/zero-margin perceptron work remains excluded and does not close this continuous negative-margin exact-sphere target;
- `operations/claims/I0089.md`, preserving the earlier negative-margin handoff/history;
- `operations/claims/CAMPBELL-OROURKE-2022-Q1.8.md`, which still names R14 and is **not** overwritten by this owner-directed complementary PROB10 route;
- immutable Campbell refocus handoff `artifacts/prob10_2026-09-20/PROB10-03/20260919T2354Z_campbell_q18_r14_handoff.md`, including owner navigation point `3846db33296cfb6eea59ff7c488929087c7b62a2`;
- newest preceding own report `runs/prob10_2026-09-20/PROB10-03/20260920T0705Z_r14_thirdfull_slope_cone_overlap_sdp_7e31.md`;
- newest relevant complementary reports on master: NM13-03 `2026-09-20__t03-thirdfull-feasibility-alpha12288.md` and NM13-07 `2026-09-20__t03-thirdfull-score-overlap-reduction.md`.

No shared claim, root ledger, peer report, scheduler state, cadence, permission, workflow, email, Drive item, public posting, or concurrent worker file was edited.

## 2. Exact source target and current primary-source scope

Frozen model:

`M=floor(alpha N)`, iid `g_a~N(0,I_N)`, `||sigma||_2=sqrt(N)` exactly,

`<g_a,sigma> >= -sqrt(N)` for every `a<=M`, fixed `alpha`, `N->infinity`.

A lower endpoint means SAT probability tends to one; an upper endpoint means SAT probability tends to zero. Changed-radius algorithms, Ising weights, replica/full-RSB numerics, and unsupported finite-lift stationary points are not source endpoints.

Primary/current-source refresh used:

- El Alaoui--Sellke, arXiv:2010.15811: exact Gaussian spherical model, but the negative-margin algorithm outputs radius `sqrt(qbar N)` with `qbar<1` and invokes conjectural FRSB/Parisi structure;
- Stojnic, arXiv:1306.3980 and arXiv:2312.16531: rigorous RDT/fl-RDT machinery and stationarized lifting equations; the 2023 paper explicitly says practical operation requires substantial numerical work and reports third-full `kappa=-1` values numerically;
- Montanari--Zhong--Zhou, arXiv:2110.15824: rigorous bounds/LP success mechanism, source of the retained SAT lower endpoint;
- Annesi--Malatesta--Zamponi, arXiv:2410.06717: full-RSB SAT/UNSAT calculation under a full-RSB ansatz, not substituted for the missing exact-radius rigorous certificate;
- Huang--Sellke--Sun, arXiv:2608.29416, submitted 29 August 2026: exact thresholds for a dimension-free Lipschitz algorithm class while explicitly distinguishing the unrestricted feasible-projection problem as still open.

A bounded fresh 20 September 2026 search did not surface a later primary theorem plainly closing the unrestricted exact-radius `kappa=-1` threshold. This is dated negative evidence, not a worldwide novelty or priority certificate.

## 3. Consumed source metric before this run

The entering repository-supported endpoints remain

`alpha_L = 6.30297437506`,

`alpha_U = 12.31963485`,

`W = 6.01666047494`.

The upper endpoint is the review-pending directed-interval complete-second certificate from the complementary NM13 work. NM13-03 has since produced a **conditional/numerical-only** complete-third stationary point at `alpha=12.288`, with numerical comparison value about `2.66e-5`, and numerical capacity zero near `12.28722222159`; NM13-07 reduced the third-full capacity equations to a five-variable derivative-free score/moment system. Neither report promotes `12.288` to a rigorous source endpoint because no outward interval root certificate exists yet.

The preceding R14 report independently eliminated the third-full q-sector via secant slopes

`r2=q3/p3`, `r1=(q2-q3)/(p2-p3)`, `r0=(1-q2)/(1-p2)`,

with exact positive-cone relations and a five-scalar compiler. That algebra is consumed here rather than rederived from scratch.

## 4. Attack 1 — scale-Euler/homogeneity: exact stationary objective collapse

Full proof was written before the checker in

`artifacts/prob10_2026-09-20/PROB10-03/20260920T0752Z_r14_scale_euler_4d_capacity.md`

creation commit

`d2cd2d06e6872a3e7c6b8ba09c50f732f217eecf`.

### New theorem R14-T03-SCALE-EULER

Write Stojnic's exact closed third-full objective as

`Psi3 = L + H + gamma_sq - (alpha/c3) Q`,

where

`L=1/2(1-p2 q2)c2 + 1/2(p2 q2-p3 q3)c3-gamma_p`,

`H=(1/(2c2))log(Aq/(2gamma_p))+(1/(2c3))log(Dq/Aq)-q3/(2Dq)`,

`Aq=2gamma_p-c2(1-q2)`, `Dq=Aq-c3(q2-q3)`,

`B=c2/(4gamma_sq)`, `m=c3/c2`, and the nested perceptron term `Q` depends on the scale variables only through `(B,m)`.

At **every strict-interior full stationary point**,

`Psi3 = 2 gamma_sq - r1/(r0 sqrt(r2))`.                     (4.1)

Proof mechanism: simultaneously scale

`(c2,c3,gamma_p,gamma_sq) -> t(c2,c3,gamma_p,gamma_sq)`.

Then `(B,m,Aq/(2gamma_p),Dq/Aq,Q)` remain invariant, so

`Psi3(t)=tX+t^{-1}Y`.

Stationarity forces `X=Y`, hence `Psi3=2(L+gamma_sq)`. The exact q-sector reconstruction then gives

`2L=-r1/(r0 sqrt(r2))`.

The proof artifact records the complete algebra and hypotheses.

### Capacity consequence

At a stationary capacity point (`Psi3=0`), necessarily

`gamma_sq = r1/(2 r0 sqrt(r2))`,                           (4.2)

and therefore

`B = (r0 r2-r1^2)/(2(1-p2)r1^2)`.                        (4.3)

The existing strict cone `r1^2<r0 r2` makes `B>0` automatic.

This is not a numerical ansatz: it is an exact identity inside the source's stationarized third-full system.

## 5. Attack 2 — equation-count negation: one old capacity residual is exactly dependent

I then attacked the possibility that the previous five-scalar compiler was genuinely five-dimensional.

Let `Rcap,Rc2,Rc3` denote its objective and two c-stationarity residuals, after q-sector reconstruction and after using the `gamma_sq` equation to reconstruct alpha. Exact differentiation gives

`Rcap + c2 Rc2 + c3 Rc3`
` = 2 gamma_sq - r1/(r0 sqrt(r2))`.                         (5.1)

Thus, after imposing the capacity scale relation (4.2), any two of `{Rcap,Rc2,Rc3}` force the third. This is a certified dependency, not an observed near-singularity.

Combining (4.2)--(4.3) with NM13-07's exact score identities produces a **four-variable derivative-free capacity compiler** in only

`(p2,p3,q2,q3)`.

Reconstruct `(c2,c3,gamma_p)` from the q-sector, reconstruct `(gamma_sq,B)` from (4.2)--(4.3), set

`alpha=c2^2/(4B^2 MB)`,

and solve only

`R3=q3-M1/(4B^2 MB)=0`,

`R2=q2-M2/(4B^2 MB)=0`,

`Rc3=0`,

`Rc2=0`.

The full eight source stationarity equations plus `Psi3=0` then follow. Conversely every strict-interior third-full capacity point satisfies this four-scalar system.

This is the main auxiliary movement of the invocation: the current third-full capacity certification target drops from five unknowns to four, and a separate small-objective enclosure is no longer logically necessary once stationarity is certified.

## 6. Attack 3 — after the proof, numerical-only falsification and conditioning test

Only after the exact theorem was written did I build a checker/scout.

Checker:

`artifacts/prob10_2026-09-20/PROB10-03/20260920T0752Z_r14_scale_euler_4d_checker.py`

creation commit

`7a29baf104bdf78c8ee2bc5dee6737e20304428f`.

Executed output:

`artifacts/prob10_2026-09-20/PROB10-03/20260920T0752Z_r14_scale_euler_4d_checker.out`

creation commit

`80bc1d7f2fcd72d5665bd7db75a0206811c90dba`.

The **exact** SymPy section verifies the q-sector scale identity and the generic residual dependency. The output ends

`ALL_EXACT_CHECKS_PASS`.

The remaining output is explicitly `NUMERICAL_ONLY`.

### Independent fixed-density falsification test

At NM13-03's independently generated stationary point at `alpha=12.288`, the new pattern-free identity gives

`2 gamma_sq-r1/(r0 sqrt(r2)) = 2.6597739161970946e-5`,

matching its independently computed full comparison value `2.65977391709358e-5` at the displayed precision. No contradiction was found.

### Four-variable capacity scout

Solving the new four-residual system at Gauss--Hermite orders `60,80,100,120,160,200` gives capacity values

`12.2872227715011`,
`12.2872221830901`,
`12.2872222240457`,
`12.2872222215128`,
`12.2872222215935`,
`12.2872222215930`.

This independently reproduces the complementary numerical zero near `12.28722222159`, with one fewer unknown and no numerical differentiation of the nested Gaussian integral.

A finite-difference diagnostic at order 160 gives four-residual Jacobian singular values approximately

`0.763438929792, 0.515049883318, 0.0105132668077, 0.000268730576534`,

condition number about `2.84e3`. This is a **numerical conditioning diagnostic only**. It suggests the four-scalar parameterization is substantially better suited to an interval/Krawczyk proof than the previously reported ill-conditioned five-variable fixed-density implementation, but it is not itself a certificate.

## 7. Before/after source metric and auxiliary movement

### Source metric

Before:

`alpha_L=6.30297437506`,

`alpha_U=12.31963485`,

`W=6.01666047494`.

After:

`alpha_L=6.30297437506`,

`alpha_U=12.31963485`,

`W=6.01666047494`.

**Source movement: none.**

No source-table number, Gauss--Hermite root, ansatz, or simulation is promoted. In particular `12.288` and `12.28722222159` remain numerical/conditional until outward enclosure and source-level validation are complete.

### Exact auxiliary movement

1. Pattern-free stationary comparison identity (4.1).
2. Algebraic capacity reconstruction of `gamma_sq` and `B` in (4.2)--(4.3).
3. Exact residual dependency (5.1).
4. Third-full capacity compiler reduced from five variables to four.
5. Separate full-objective numerical differentiation/evaluation is no longer needed to determine the stationary comparison sign.

## 8. Remaining full-scope gap and next bracket-moving obligation

The source target remains **OPEN / PARTIAL**. The decisive remaining obligation is now narrower:

1. construct a small four-dimensional box in `(p2,p3,q2,q3)` around the numerical zero;
2. outward-enclose the five Gaussian quantities `Q,M1,M2,MB,QM` on that box using the exact closed one-step kernel;
3. prove a Krawczyk or weighted-contraction inclusion for the four residuals `R3,R2,Rc3,Rc2`;
4. verify all strict-domain and slope-cone inequalities throughout the certified box;
5. connect the certified third-full stationary/capacity point to a rigorous source upper endpoint using the exact source comparison theorem and an independently checked sign/continuation argument. For a fixed-density `alpha=12.288` validator, (4.1) permits the comparison sign to be certified from the scale gap rather than a cancellation-prone direct objective enclosure.

Independent review is still required before closure. This invocation is a self-check, not an independent audit.

## 9. Structured ledger_delta

```yaml
ledger_delta:
  task: PROB10-03
  worker_route: R14 owner-refocused complementary route
  status: PARTIAL
  exact_target: negative-margin spherical Gaussian perceptron, kappa=-1, exact sphere
  source_metric_before:
    alpha_L: "6.30297437506"
    alpha_U: "12.31963485"
    width: "6.01666047494"
  source_metric_after:
    alpha_L: "6.30297437506"
    alpha_U: "12.31963485"
    width: "6.01666047494"
  source_movement: none
  new_exact_results:
    - "R14-T03-SCALE-EULER: Psi3=2 gamma_sq-r1/(r0 sqrt(r2)) at every strict-interior full stationary point"
    - "Capacity reconstruction gamma_sq=r1/(2 r0 sqrt(r2)), B=(r0 r2-r1^2)/(2(1-p2)r1^2)"
    - "R14-T03-RESIDUAL-DEPENDENCY: Rcap+c2 Rc2+c3 Rc3 equals the scale gap"
    - "Four-scalar derivative-free third-full capacity compiler in (p2,p3,q2,q3)"
  numerical_only:
    third_full_zero: "~12.28722222159"
    four_dimensional_jacobian_condition: "~2.84e3"
  artifacts:
    proof: "artifacts/prob10_2026-09-20/PROB10-03/20260920T0752Z_r14_scale_euler_4d_capacity.md @ d2cd2d06e6872a3e7c6b8ba09c50f732f217eecf"
    checker: "artifacts/prob10_2026-09-20/PROB10-03/20260920T0752Z_r14_scale_euler_4d_checker.py @ 7a29baf104bdf78c8ee2bc5dee6737e20304428f"
    output: "artifacts/prob10_2026-09-20/PROB10-03/20260920T0752Z_r14_scale_euler_4d_checker.out @ 80bc1d7f2fcd72d5665bd7db75a0206811c90dba"
  campbell_handoff_preserved: "artifacts/prob10_2026-09-20/PROB10-03/20260919T2354Z_campbell_q18_r14_handoff.md"
  closure: false
```
