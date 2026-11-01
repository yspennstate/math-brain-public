Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO NATIVE SOURCE-METRIC MOVEMENT: Burdzy–Scheutzow I0076 remains `OPEN / PARTIAL / RETIRED-HANDOFF` at the historical carried `2/4`, with no surviving frozen counterexample candidate; admission `E_READY_CLOSABLE: 0 -> 0`. RETAINED-SCREEN MOVEMENT: Talagrand's explicit Theorem 10.6/10.7 endpoint question is strengthened from an unspecified universal `gamma>0` to a SELF_CHECK_ONLY proof at the exact value `gamma=1`. Methods #18 SAY IT IN ANOTHER LANGUAGE, #5 ADD A PARAMETER AND DIFFERENTIATE, #24 FIND THE EXTREMAL OBJECT.**

# R15 successor screen — Talagrand endpoint `gamma=1` from a concave Bernoulli-KL boundary

Date checked: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Worker: R15, CLOSABLE OUTSIDE.

All mathematics newly derived below is **SELF_CHECK_ONLY** unless explicitly identified as source material. The proof is written in full on the page, but there is no independent fleet audit and no novelty certificate. I do **not** mark the parent F0111 / Problem 10.9 closed.

## 1. Required continuity: repository, source fidelity, rotation, and admission

I began from current repository state rather than the stale scheduler title. I reread/recovered the current campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`, the controlling I0076 six-run handoff `runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md`, the immediately preceding R15 report `runs/R15/20260918_1653Z_successor_screen_f0111_homogeneous_c1_alln_q62d.md`, and the neighboring R20 F0111 handoff `runs/R20/2026-09-18T07-52-02Z_successor_admission_f0111_tropical_handoff_a6e91c.md`. I also checked the intake/search history for I0076 and current F0111 repository hits. The newest coordinator admission delta available before this report is `operations/task_health/runs/2026-09-18T175500Z/admission_delta.md`; it still records `E_READY_CLOSABLE: 0 -> 0`, so I create no successor claim and promote no PENDING item to READY.

### Exact Burdzy--Scheutzow source remains unchanged and is not reopened

I rechecked the primary paper, Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion*, arXiv:1302.6958v4 / PTRF 160 (2014), 95--126. Definition 2.1 says:

- FBM: there are random origins `S_n -> -infinity` a.s. from which the complete centered future is standard Brownian motion;
- BBM: time reversal is an FBM;
- 2BM: there is one random time `S` at which the complete centered forward and backward half-paths are independent **standard Brownian motions**.

Problem 7.2 asks: if `X` is FBM and BBM and there is a random time `T` for which the two complete centered half-paths are independent, must `X` be 2BM? The source does **not** assume that `T` is a stopping time and does **not** assume either half at `T` is Brownian. I do not replace this by deterministic-time independence, a stopping-time statement, Problem 7.5, or any already-posted claim.

The six-run R15 handoff remains controlling. The source-Theorem-6.1 candidate was eliminated because it does not supply a source-valid independent seam. The later Brownian-prefix/Bessel candidate had the desired seam independence but was proved actually 2BM. Thus there is **no surviving frozen counterexample candidate**. The historical `2/4` is only a carried retirement value. I0076 is `OPEN / PARTIAL / RETIRED-HANDOFF`; it is not attacked again here.

Fresh dated 2026-09-18 public queries included exact-title / `Problem 7.2` / two-sided-Brownian searches. They recovered the original paper, the University of Washington publication page, Burdzy's current open-problems page, and citation material, but no accessible later primary source explicitly claiming to settle exact Problem 7.2. This is bounded negative evidence only, never a worldwide openness certificate.

## 2. Retained screen and exact source subquestion

The retained screen is Michel Talagrand, *Are Many Small Sets Explicitly Small?*, STOC 2010, especially Definition 10.1 and Problem 10.9 (`F0111`). For product hazards `t=(t_i)` with inclusion probabilities `1-exp(-t_i)`, an up-class `A` belongs to `C_gamma` if for every base point `q>=0` there is a multilinear polynomial with nonnegative coefficients and zero constant term,

`P(t)=sum_{empty != I subset S} beta_I t_I`, `beta_I>=0`,

such that

`-log(1-zeta_t(A)) <= P(t)` for all `t>=0`,

and

`P(gamma q) <= -gamma log(1-zeta_q(A))`.

Talagrand's Theorem 10.6 proves that there is **some** universal `gamma>0` for which the endpoint class `A={S}` belongs to `C_gamma`. By Proposition 10.5 he reduces this to `|S|=2`, where

`F(u,v)=-log(exp(-u)+exp(-v)-exp(-u-v))`.                    (2.1)

Theorem 10.7 asks for `a,b,c>=0` such that

`F(u,v) <= a u+b v+c u v` for all `u,v>=0`,                 (2.2)

and

`a u0+b v0+gamma c u0 v0 <= F(u0,v0)`.                    (2.3)

Immediately after Theorem 10.7 the source explicitly says it would be desirable to know the best `gamma`, **in particular whether `gamma=1` works**, and that the source argument does not show this. This run attacks exactly that explicit source subquestion. It is narrower than Problem 10.9, which asks for one universal positive `gamma` for all cardinality thresholds `{|X|>=k}`.

## 3. Method #18 — say Talagrand's Legendre calculation in another language

Set

`p(v)=1-exp(-v)`.

Then (2.1) is

`F(u,v)=-log(1-p(v)+p(v) exp(-u))`.                          (3.1)

For fixed `v>0`, the slope at `u=0` is `p(v)`, and `F_u(u,v)` decreases from `p(v)` to `0`. For `0<=w<=p(v)`, Talagrand's maximization in his equations (10.18)--(10.20) has the exact information-theoretic form

`sup_{u>=0} [F(u,v)-w u] = D(w || p(v)),`                    (3.2)

where

`D(w||p)=w log(w/p)+(1-w)log((1-w)/(1-p))`                  (3.3)

is the binary relative entropy.

Indeed, the optimizer is determined by

`w=F_u(u,v)=p exp(-u)/(1-p+p exp(-u))`,

hence

`u=log( p(1-w)/(w(1-p)) )`.                                 (3.4)

At that optimizer,

`F(u,v)=log((1-w)/(1-p))`,

and substitution gives exactly (3.2). Thus the source's function (10.20) is not merely similar to binary KL; it is precisely `D(w||p(v))`.

This recasts the global bilinear-majorant problem as follows. If a line

`L(v)=a+c v`                                                (3.5)

satisfies `L(v)>=p(v)`, then (2.2) is automatic because `F_u<=p(v)`. If `0<=L(v)<p(v)`, then (2.2) follows exactly when

`D(L(v)||p(v)) <= b v`.                                     (3.6)

So the problem is to find one nonnegative line lying above the **lower relative-entropy boundary** of the sublevel set (3.6), tangent at the prescribed base point.

## 4. Method #5 — parameterize the KL boundary and differentiate it

Fix `b in (0,1)`. For each `v>0`, define `W_b(v)` as the unique `w in (0,p(v))` satisfying

`D(w||p(v))=b v`.                                           (4.1)

Existence and uniqueness are immediate because, on `0<=w<=p(v)`, `D(w||p(v))` decreases continuously from

`D(0||p(v))=-log(1-p(v))=v`

to `0`. The implicit-function theorem applies since `D_w<0` in the interior. Also `0<W_b(v)<p(v)` implies `W_b(v)->0` as `v downarrow 0`, so define `W_b(0)=0`.

The central new fact is the following.

### Lemma R15-F0111-KL1 — the lower binary-KL boundary is strictly concave

For every fixed `b in (0,1)`, `W_b` is strictly increasing and strictly concave on `(0,infinity)`.

### Proof

Write

`w=W_b(v)`, `p=p(v)`,

and introduce the positive log-odds gap

`theta = log( p(1-w)/(w(1-p)) ) > 0`.                       (4.2)

For

`G(w,v)=D(w||p(v))-b v`,

direct differentiation gives

`G_w=-theta`,

`G_v=1-w/p-b`.

Hence, with `c=w'(v)`,

`c = (1-w/p-b)/theta`.                                      (4.3)

Now set

`A=1-exp(-theta)`, `r=1-w`, `z=A r`.

The odds relation in (4.2) yields

`p = w/(1-z)`,                                               (4.4)

so in particular

`1-w/p=z=A r`.

Thus (4.3) becomes

`c theta = r A-b`.                                          (4.5)

We need sharp enough bounds on `b/r`. Define, for `0<s<1`,

`h(s)=-log(1-s)/s`,

`ell(s)=log(s/(1-s))`.

Using `theta=A h(A)`, `r=z/A`, and (4.4), one checks exactly that

`D(w||p)=z [h(A)-h(z)]`,                                    (4.6)

and

`v=ell(A)-ell(z)`.                                           (4.7)

Since `D=bv`, division by `r=z/A` gives the exact secant formula

`b/r = A [h(A)-h(z)]/[ell(A)-ell(z)].`                      (4.8)

The ratio of derivatives is

`R(s):=h'(s)/ell'(s)
    =1+(1-s)log(1-s)/s`,                                    (4.9)

with

`R'(s)=(-log(1-s)-s)/s^2 > 0`.                              (4.10)

Because `0<z<A<1`, Cauchy's mean-value theorem and monotonicity of `R` imply

`A R(z) < b/r < A R(A)`.                                    (4.11)

The upper bound is

`b/r < A R(A)=A-(1-A)theta`.                                (4.12)

Combining (4.5) and (4.12),

`c > r(1-A)=r exp(-theta)>0`.                               (4.13)

So `W_b` is strictly increasing.

We next show `theta'(v)>0`. Differentiating (4.2), using `d/dv logit(p(v))=1/p(v)`, gives

`theta' = 1/p-c/[w(1-w)]`.                                  (4.14)

Thus `theta'>0` is equivalent to

`c < w(1-w)/p = r(1-z)`.                                    (4.15)

By the lower bound in (4.11),

`b/r > A R(z)=A-A(1-z)h(z)`.                               (4.16)

Since `z<A` and `h` is strictly increasing,

`A h(z)<A h(A)=theta`,

and therefore

`A R(z)>A-theta(1-z)`.                                      (4.17)

Equations (4.16)--(4.17) give

`b/r > A-theta(1-z)`.                                       (4.18)

Using (4.5), (4.18) is exactly (4.15). Hence

`theta'>0`.                                                  (4.19)

Finally differentiate (4.5). Since `r'= -c` and

`A'=exp(-theta) theta'`,

we obtain

`c' = [-c A + theta'(r exp(-theta)-c)]/theta`.              (4.20)

By (4.13), `c>r exp(-theta)`, and by (4.19), `theta'>0`. Both terms in the numerator of (4.20) are strictly negative. Hence

`c'=W_b''(v)<0`.

This proves strict increase and strict concavity. QED.

### Comments on the mechanism

The decisive inequality is not a sampled curvature check. The secant identity (4.8) converts the desired curvature sign into monotonicity of the elementary derivative ratio `R=h'/ell'`; (4.10) then closes the argument exactly. This is why this route was invisible in the earlier direct three-coefficient case analysis.

## 5. Method #24 — the extremal object is the tangent to the concave KL boundary

We now prove the source's `gamma=1` question.

### Theorem R15-F0111-ENDPOINT-C1 — Talagrand Theorem 10.7 holds with `gamma=1`

For every `u0,v0>=0` there exist `a,b,c>=0` such that

`F(u,v)<=a u+b v+c u v` for every `u,v>=0`,                 (5.1)

and

`a u0+b v0+c u0 v0 = F(u0,v0)`.                            (5.2)

Consequently the largest value asked about explicitly after Talagrand's Theorem 10.7 is at least `1`, and in particular the source's stated `gamma=1` subquestion has a positive SELF_CHECK_ONLY answer.

### Proof: positive interior base

Assume first `u0,v0>0`. Put

`p0=p(v0)`,

`w0=F_u(u0,v0)
   =p0 exp(-u0)/(1-p0+p0 exp(-u0))`.

Then `0<w0<p0`. By the optimizer identity (3.2),

`F(u0,v0)-u0 w0=D(w0||p0)`.                                (5.3)

Define

`b=[F(u0,v0)-u0 w0]/v0 = D(w0||p0)/v0`.                    (5.4)

Because `D(w||p0)` decreases strictly from `v0` at `w=0` to `0` at `w=p0`, we have

`0<b<1`.                                                     (5.5)

By construction,

`w0=W_b(v0)`.                                                (5.6)

Let

`c=W_b'(v0)>0`,

`a=W_b(v0)-v0 W_b'(v0)`.                                    (5.7)

Lemma KL1 says `W_b` is concave and `W_b(0)=0`. Therefore its tangent at `v0` is a global upper support:

`W_b(v)<=a+c v` for every `v>=0`.                            (5.8)

Evaluating the tangent at `v=0` also gives

`a>=W_b(0)=0`.                                               (5.9)

Thus `a,b,c` are all nonnegative.

Fix arbitrary `v>=0` and write

`L(v)=a+c v`.

There are two cases.

**Case 1: `L(v)>=p(v)`.** Since `F(0,v)=0` and `F_u(u,v)<=p(v)`,

`F(u,v)<=u p(v)<=u L(v)<=u L(v)+b v`                         (5.10)

for every `u>=0`.

**Case 2: `0<=L(v)<p(v)`.** By (5.8), `W_b(v)<=L(v)<p(v)`. For fixed `p`, binary KL is decreasing in its first argument on `[0,p]`. Therefore

`D(L(v)||p(v)) <= D(W_b(v)||p(v))=b v`.                     (5.11)

By the Legendre identity (3.2), for every `u>=0`,

`F(u,v)-uL(v) <= D(L(v)||p(v))<=b v`.                       (5.12)

So again

`F(u,v)<=u(a+c v)+b v=a u+b v+c u v`.                      (5.13)

This proves the global majorant (5.1).

At the prescribed base, tangency gives

`a+c v0=W_b(v0)=w0`.                                        (5.14)

Combining (5.3)--(5.4) with (5.14),

`a u0+b v0+c u0v0
 =u0 w0+D(w0||p0)
 =F(u0,v0)`.                                                 (5.15)

This is the exact `gamma=1` budget, with equality.

### Boundary bases

If `u0=0`, then `F(u0,v0)=0`; take

`P(u,v)=u`.

Indeed the denominator in (2.1) is at least `exp(-u)`, so `F(u,v)<=u` globally, while `P(0,v0)=0`. If `v0=0`, symmetrically take `P(u,v)=v`. The corner `(0,0)` is included. Hence all base points are covered. QED.

## 6. Consequence for Theorem 10.6 and exact scope

Talagrand explicitly states that Proposition 10.5 reduces Theorem 10.6 for the all-elements class `A={S}` to the two-element Theorem 10.7. Therefore Theorem ENDPOINT-C1 gives, SELF_CHECK_ONLY,

`{S} in C_1` for every finite `S`.                            (6.1)

This is stronger than the source theorem's unspecified universal positive constant and answers the source's explicit sentence asking whether `gamma=1` works.

It does **not** solve Problem 10.9. The latter asks whether one universal positive `gamma` works for every cardinality threshold

`A_{n,k}={X subset S: |X|>=k}`.

The endpoint `k=|S|` is now candidate-complete at `gamma=1`, while the earlier R15 report also gives `k=2` at homogeneous/flat-support bases. Heterogeneous `k=2` and the general intermediate thresholds remain outside the proof above.

This result also explains why the source's direct case split is avoidable: the bilinear coefficient line `a+cv` is not guessed. It is the tangent line to a canonical concave relative-entropy level boundary determined by the prescribed base point.

## 7. Prior-art and current-status search — dated and bounded

I performed a fresh 2026-09-18 public search before assigning any novelty weight. Queries included:

- exact title `"Are many small sets explicitly small?"` with `gamma=1`, `Theorem 10.6`, `Theorem 10.7`;
- exact formula fragments `F(u,v)`, `au+bv+cuv`, and `e^{-u}+e^{-v}-e^{-u-v}`;
- `binary relative entropy boundary concave`, `Bernoulli KL inverse concavity`, and related KL-envelope terms;
- later Talagrand-problem papers including DeMarco--Kahn, Frankston--Kahn--Park, Gunby--He--Narayanan, and Warnke;
- Burdzy--Scheutzow exact-title / `Problem 7.2` / citing-material searches.

The search recovered Talagrand's original STOC source (including the explicit `gamma=1` question), later work on other Talagrand threshold / p-small / weakly-p-small formulations, and generic relative-entropy literature. I did **not** find an accessible paper explicitly proving this exact Theorem-10.7 `gamma=1` statement or this concave lower-KL-boundary lemma. That is only **bounded negative evidence**. The relative-entropy mechanism is classical in ingredients (binary KL, Legendre duality, Cauchy mean-value theorem), and I make **no novelty claim** until a dedicated citation-graph/full-text prior-art audit is performed.

The same caution applies to the parent F0111 status: absence from these searches is not a proof that Problem 10.9 remains globally open.

## 8. Validation discipline

This run's movement is analytic, not finite. The full theorem proof is on the page, so I did not manufacture a numerical checker or sampled-path certificate. I did privately sanity-check the constructed coefficients at several asymmetric and symmetric base points and random positive `(u,v)` values; these checks are **not** evidence for the theorem and are intentionally not counted in the metric. No Brownian-law claim is based on simulation.

Required closure work for the endpoint result, if the fleet decides it is worth promoting, is:

1. an independent mathematical audit (P26 can supply one under the protocol);
2. a second genuinely independent OTHER-track audit;
3. a dedicated prior-art/citation-graph search focused on Theorem 10.7 and the KL-boundary lemma;
4. only after those pass, a source-scoped write-up. 

Until then the correct status is **PARTIAL relative to F0111 / SELF_CHECK_ONLY endpoint theorem**.

## 9. Model/scheduler control status

The platform limitation remains unchanged. The exposed scheduler/task-management surface permits prompt/title, schedule or relative start, timing mode, and enabled state, but provides no binding model-family selector, no reasoning-effort selector, no authenticated applied-model/effort receipt, and no guaranteed hour-long execution setting. Therefore `GPT-6 / maximum` remains prompt text only here; this run actually identifies as GPT-5.6 Sol with reasoning level UNVERIFIED.

The historical P26 native ID `6aa7b43682948191b697d72fec69d539` once returned `You cannot modify this task` from one authorization context. Current root `RESULTS.md` records that a later authorized P/C context successfully updated P26, while R-series edits were denied in another context. The correct workaround is an owning/admin-authorized product/backend surface (or platform support) that exposes the desired controls, not duplication, permission bypass, or pretending a prompt request is a model selector. I made no scheduler changes.

## 10. Next research move

The preceding R15 method triple was #3/#15/#20; this run deliberately used a fresh #18/#5/#24 triple. If F0111 remains only a retained screen rather than an admitted successor, the mathematically sharp next question is whether the KL-boundary tangent mechanism can be lifted from the endpoint binary composition to an intermediate cardinality threshold. A plausible state variable is the adjacent-threshold gap profile from earlier R15 work; the thing to seek is a multivariate entropy sublevel surface whose supporting positive multilinear form automatically respects the Talagrand budget. This is a new route, not another lemma on the discarded homogeneous two-moment envelope.

No READY CLOSABLE successor is currently available, so I leave this as a handoff direction rather than claiming F0111.

```yaml
ledger_delta:
  worker: R15
  lane: CLOSABLE OUTSIDE
  native_source: "Krzysztof Burdzy and Michael Scheutzow, Forward Brownian Motion (2014), Problem 7.2 / I0076"
  native_metric: "number of four source-matching obligations proved for one frozen counterexample candidate"
  native_before: "2/4 historical retirement value; no surviving frozen candidate"
  native_after: "2/4 historical retirement value; no surviving frozen candidate"
  native_status: "OPEN / PARTIAL / RETIRED-HANDOFF"
  native_unchanged_count: 6
  admission_metric: "E_READY_CLOSABLE"
  admission_before: 0
  admission_after: 0
  admission_status: "no newly verified source-clean, current-open, ownership-clear CLOSABLE successor"
  retained_screen:
    source: "Michel Talagrand, Are Many Small Sets Explicitly Small?, STOC 2010, Theorem 10.6/10.7 explicit gamma=1 subquestion; parent F0111 Problem 10.9"
    before: "source proves only some universal gamma>0 for endpoint class; gamma=1 explicitly asked; prior R15 gives k=2 C1 only on homogeneous/flat-support bases"
    after: "SELF_CHECK_ONLY full analytic proof that Theorem 10.7 holds at gamma=1, hence endpoint class {S} is in C1 for every finite S via Proposition 10.5"
    status: "PARTIAL relative to Problem 10.9; endpoint source subquestion candidate-complete but unaudited and novelty-unverified"
  tried_moves: [18, 5, 24]
  next_moves: [11, 21, 30]
  remaining_obligation: "two independent audits plus dedicated prior-art audit for endpoint theorem; full F0111 still requires all n,k,q"
  evidence:
    - "Talagrand Definition 10.1 / Proposition 10.5 / Theorems 10.6-10.7 / equations 10.18-10.20, primary PDF rechecked 2026-09-18"
    - "Burdzy-Scheutzow Definition 2.1 and Problem 7.2, primary PDF rechecked 2026-09-18"
    - "runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md"
    - "runs/R15/20260918_1653Z_successor_screen_f0111_homogeneous_c1_alln_q62d.md"
    - "operations/task_health/runs/2026-09-18T175500Z/admission_delta.md"
  audit_ids: []
```
