Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO ADMISSION MOVEMENT: `E_ready: 0 -> 0`; I0076 remains `OPEN / PARTIAL / RETIRED-HANDOFF` at `2/4`; successor-gate unchanged count remains `UNKNOWN`. Methods **#5 ADD A PARAMETER, #13 FIND WHAT ONLY INCREASES, #26 HUNT THE SPORADIC CASE**.

# R15 CLOSABLE OUTSIDE — successor admission, Talagrand homogeneous k=2 theorem

Date: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.

## 1. Continuity, exact Brownian source, and exclusions

I continued from the newest R15 immutable report

`runs/R15/20260918_0612Z_successor_admission_f0111_fkg_sendov_g51a.md`.

I also read the newer neighboring F0111 work

`runs/R20/2026-09-18T07-10-19Z_successor_admission_f0111_conservative_gap_nogo_3d426b.md`

before doing new mathematics, so I do not rederive or relabel its reverse-hazard/conservative-flux results or its no-go theorem for certifying gaps separately.

The original R15 target remains operationally retired after the mandatory six unchanged runs. I reread the source and the six-run handoff

`runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md`.

The exact source target is Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion*, arXiv:1302.6958v4 / PTRF 160 (2014), Problem 7.2. Definition 2.1 and Problem 7.2 give the following scope:

- `X` is a continuous process on `R` and is an FBM: there are random times `S_n -> -infinity` such that each shifted future `(X_{S_n+t}-X_{S_n})_{t>=0}` is standard Brownian motion;
- `X` is also a BBM, meaning the time reversal is an FBM;
- there exists an **arbitrary finite random real time** `T` such that the two **complete centered half-path processes**

  `(X_{T+t}-X_T)_{t>=0}` and `(X_{T-t}-X_T)_{t>=0}`

  are independent;
- no stopping-time or splitting-time assumption on `T` appears in Problem 7.2;
- neither half at this seam is separately assumed Brownian;
- the question is whether these hypotheses force `X` to be a two-sided Brownian motion.

Problem 7.5 is a different source question and remains excluded.

The two old concrete R15 counterexample candidates remain eliminated. The source Theorem-6.1 FBM+BBM non-2BM candidate fails the required independent real seam. The later alternating Brownian-prefix/BES candidate has an independent seam but was shown to be 2BM by finite-intensity excursion-Palm de-biasing. Thus there is **no surviving frozen counterexample candidate**. The marked-Brownian-cell / sparse copied-continuous-block construction in the handoff is only an architecture for a fresh future reassignment, not a candidate whose obligation count may be incremented. The retained Brownian metric is therefore exactly `2/4`.

Fresh 2026-09-18 source/literature queries again recovered the original Problem 7.2 and no accessible later paper explicitly claiming to resolve exact Problem 7.2. This is bounded negative evidence only, not a worldwide openness certificate.

I also reread the current campaign INDEX/RANKING, root POSTED/RESULTS/QUEUE, the latest operations deployment manifest, and the newest coordinator report `operations/task_health/runs/2026-09-18T065500Z/status.md`. That coordinator pass still records no race-safe source crossing every source/current-open/ownership/genuinely-CLOSABLE gate. I therefore do not fabricate a successor claim.

## 2. Successor-screening source: Talagrand Problem 10.9

I continued F0111 only as **successor-screening mathematics**, not as an admitted R15 target.

Michel Talagrand, *Are Many Small Sets Explicitly Small?*, STOC 2010, Problem 10.9, defines for an up-class `A`

`F_A(t)=-log(1-zeta_t(A))`,

where under `zeta_t` the coordinates are independent with

`P(i in X)=1-exp(-t_i)`.

The class belongs to `C_gamma` if, for every base point `q>=0`, there is a multilinear polynomial with nonnegative coefficients and no constant term,

`P(t)=sum_{empty != I subset [n]} beta_I t_I`, `beta_I>=0`,

such that

`F_A(t)<=P(t)` for every `t>=0`,

and

`P(gamma q)<=gamma F_A(q)`.

Problem 10.9 asks whether one universal `gamma>0` works for every cardinality threshold

`A_{n,k}={X subset [n]: |X|>=k}`.

The source proves endpoint cases and a binary composition theorem, but leaves the general cardinality-threshold problem open. Fresh 2026-09-18 searches recovered the original STOC paper and related DeMarco--Kahn / Frankston--Kahn--Park / later threshold literature, but no accessible paper explicitly resolving this exact heterogeneous-`q` positive-polynomial Problem 10.9 or the homogeneous `k=2` statement proved below. Negative search evidence is not a novelty certificate; I make no publication-novelty claim.

Previous R15 work proved the global FKG envelope `F_{n,k}(t)<=e_k(t)` and a boundary-lifting lemma. Neighboring R20 work then showed that trying to certify the adjacent reverse-hazard gaps separately cannot close the problem. This run therefore attacks the **total free energy** directly, not an isolated gap.

## 3. Idea before algebra — methods #5 and #26

The simplest genuinely non-endpoint slice is `k=2`. The pure quadratic envelope `e_2(t)` is excellent at low activity but overpays at large homogeneous base points. A pure linear envelope has the opposite behavior.

The new idea is to insert a continuous interpolation parameter `a` and look for a global envelope

`P_a(t)=a sum_i t_i + B e_2(t)`.

The coefficient `B` is chosen by a one-dimensional tangent construction. The source permits the polynomial to depend on the base point `q`, so this is source-valid. The goal is not to prove the full heterogeneous Problem 10.9 in this run, but to see whether the entire all-`n`, all-scale **homogeneous `k=2` sector** can be closed exactly.

It can.

## 4. Exact setup for k=2

For `t=(t_1,...,t_n)>=0` put

`T=sum_i t_i`,

`E=e_2(t)=sum_{i<j} t_i t_j`,

and

`D(t)=log(1+sum_i(exp(t_i)-1)).`

For the threshold `N>=2`,

`F_{n,2}(t)=T-D(t).`                                      (4.1)

For a homogeneous vector `q=r 1_n`, write `A=n-1` and

`H_n(r)=log(n-(n-1) exp(-r)).`                            (4.2)

Then

`D(r 1_n)=r+H_n(r)`,

`F_{n,2}(r 1_n)=A r-H_n(r)`,                              (4.3)

and

`E(r 1_n)=nA r^2/2.`                                      (4.4)

## 5. Method #5 — a global one-parameter linear+quadratic envelope

### Lemma R15-F0111-H2-ENV

Let `n>=2`, `A=n-1`, and choose

`0<a<A/n`.

Set

`eta=A-na>0`,

`M_n(eta)=sup_{u>0} [eta u-H_n(u)]_+ / u^2`,

and

`B_n(a)=2 M_n(eta)/(a n^2).`                              (5.1)

Then for every `t in R_+^n`,

`F_{n,2}(t) <= a T+B_n(a) E.`                             (5.2)

In particular (5.2) is a global source-valid positive multilinear polynomial majorant of degree at most two.

### Proof

By convexity of the exponential,

`sum_i exp(t_i) >= n exp(T/n)`.

Hence

`D(t)>=log(1+n(exp(T/n)-1))
      =T/n+H_n(T/n).`                                     (5.3)

Also `D(t)>=max_i t_i`.

If `F_{n,2}(t)<=aT`, (5.2) is immediate. Suppose instead

`F_{n,2}(t)>aT`.

Then `D(t)<(1-a)T`, so with `m=max_i t_i`,

`m<(1-a)T`.

Therefore

`sum_i t_i^2 <= mT < (1-a)T^2`,

and hence

`2E=T^2-sum_i t_i^2 > aT^2.`                              (5.4)

Put `u=T/n`. From (5.3), using `eta=A-na`,

`F_{n,2}(t)-aT
 <=(1-a)T-[T/n+H_n(T/n)]
 =eta u-H_n(u).`                                          (5.5)

The left side is positive, so the right side is positive. By the definition of `M_n(eta)`,

`eta u-H_n(u)<=M_n(eta)u^2
                =(a B_n(a)/2)T^2.`                       (5.6)

Combining (5.4) and (5.6) gives

`F_{n,2}(t)-aT < B_n(a)E`.

This proves (5.2). QED.

The supremum in (5.1) is finite: near zero, `eta<A=H_n'(0)` makes the positive part vanish; at infinity, the numerator grows at most linearly while the denominator is quadratic.

## 6. Method #13 — the tangent location is unique because a hazard functional only decreases

The envelope becomes base-point tight if the scalar supremum in (5.1) is forced to occur at the homogeneous base scale `r`.

Write

`g(u)=H_n'(u)=A/[1+n(exp(u)-1)].`                          (6.1)

Then `g` is strictly decreasing and strictly convex. Indeed

`g'(u)=-A n exp(u)/[1+n(exp(u)-1)]^2<0`,

while direct differentiation gives `g''(u)>0`.

Define

`Q_n(u)=2H_n(u)/u-H_n'(u)`, `u>0`.                         (6.2)

### Lemma R15-F0111-H2-MONO

`Q_n` is strictly decreasing from `A` to `0`.

### Proof

Let `k(u)=-g'(u)>0`. Since `g''>0`, the function `k` is strictly decreasing. Since `H_n(0)=0`,

`H_n(u)/u-g(u)
 =(1/u) int_0^u [g(v)-g(u)] dv
 =(1/u) int_0^u s k(s) ds
 > u k(u)/2.`                                              (6.3)

Differentiating (6.2),

`Q_n'(u)
 =2g(u)/u-2H_n(u)/u^2-g'(u)
 =-2[H_n(u)/u-g(u)]/u+k(u)
 <0`                                                       (6.4)

by (6.3). The endpoint limits follow from `g(0)=A`, `H_n(u)->log n`, and `g(u)->0`. QED.

Now fix `r>0` and set

`eta=Q_n(r)`.

For

`psi_eta(u)=[eta u-H_n(u)]/u^2`,

direct differentiation gives

`psi_eta'(u)=[Q_n(u)-eta]/u^2.`                            (6.5)

Since `Q_n` is strictly decreasing and `Q_n(r)=eta`, (6.5) shows that `psi_eta` increases on `(0,r)` and decreases on `(r,infinity)`. Thus its unique global maximum is at `r`, and

`M_n(eta)=[eta r-H_n(r)]/r^2.`                            (6.6)

Moreover

`eta r-H_n(r)=H_n(r)-rH_n'(r)>0`                          (6.7)

by strict concavity of `H_n`.

This is the exact monotone invariant that makes the parameterized envelope close at its chosen homogeneous base point.

## 7. Main partial theorem — every homogeneous k=2 base point has a C_{1/4} certificate

### Theorem R15-F0111-H2-HOM

For every `n>=2` and every `r>=0`, at the homogeneous base point

`q=r 1_n`,

the cardinality-two threshold `A_{n,2}` satisfies Talagrand's `C_gamma` majorant condition with the **universal value**

`gamma=1/4.`                                               (7.1)

Equivalently, for every `n,r` there exists a positive multilinear polynomial `P=P_{n,r}` with no constant term such that

`F_{n,2}(t)<=P(t)` for all `t>=0`,                         (7.2)

and

`P(q/4)<=F_{n,2}(q)/4.`                                   (7.3)

This is a complete theorem for the homogeneous `k=2` slice, not the full heterogeneous Problem 10.9.

### Proof

The case `r=0` is trivial. Assume `r>0` and put

`x=nr`.

We split at `x=5`.

#### Case 1: `x<=5`

Take the pure quadratic global majorant

`P(t)=E=e_2(t)`,

which was already established in the previous R15 FKG theorem.

From (4.3) and (6.1),

`d/dr F_{n,2}(r1_n)
 =A-H_n'(r)
 =A n(exp(r)-1)/[1+n(exp(r)-1)]
 >=A n r/(1+nr),`                                         (7.4)

since `exp(r)-1>=r` and `z/(1+nz)` is increasing in `z`.

Integrating from `0` to `r` gives

`F_{n,2}(r1_n)
 >=(A/n)[x-log(1+x)].`                                    (7.5)

By (4.4),

`F_{n,2}(q)/E(q)
 >=2[x-log(1+x)]/x^2.`                                    (7.6)

For `0<=x<=5`,

`x-log(1+x)>=x^2/8.`                                      (7.7)

Indeed the derivative of the difference is

`x/(1+x)-x/4=x(3-x)/(4(1+x))`;

so the difference increases on `[0,3]` and decreases on `[3,5]`. Its endpoint values are `0` and

`15/8-log 6>0`.

For example, the latter strict inequality follows directly from the positive exponential series:

`exp(15/8) > 1+15/8+(15/8)^2/2+(15/8)^3/6+(15/8)^4/24 > 6`.

Thus (7.6) gives

`F_{n,2}(q)>=E(q)/4.`                                      (7.8)

At `gamma=1/4`,

`P(gamma q)=gamma^2E(q)<=gamma F_{n,2}(q)`,

which is (7.3).

#### Case 2: `x>=5`

Use the tangent construction of Section 6. Put

`eta=Q_n(r)`,

`a=(A-eta)/n`,

and let `B=B_n(a)` be the exact tangent coefficient from (5.1)/(6.6).

First we show

`a/(A/n)>1/4.`                                             (7.9)

Since `eta=Q_n(r)`,

`eta/A <= 2H_n(r)/(Ar).`                                  (7.10)

Also, by (6.1), after the change of variables `v=ns`,

`H_n(r)/(Ar)
 =(1/x) int_0^x 1/[1+n(exp(v/n)-1)] dv
 <=(1/x) int_0^x 1/(1+v) dv
 =log(1+x)/x,`                                             (7.11)

using `exp(v/n)-1>=v/n`.

The function `log(1+x)/x` is decreasing for `x>0`. Therefore for `x>=5`,

`eta/A
 <=2log(1+x)/x
 <=2log 6/5
 <3/4.`                                                    (7.12)

(The same `log6<15/8` inequality used above gives the final strict bound.) Hence

`a/(A/n)=1-eta/A>1/4`,

proving (7.9).

By Lemma R15-F0111-H2-ENV,

`P(t)=aT+B E`                                              (7.13)

is a global positive multilinear majorant. At the homogeneous base point, (6.6) gives the exact relation

`B E(q)
 =(A/(an))[F_{n,2}(q)-a nr].`                             (7.14)

Indeed both sides reduce to `(A/(an))[eta r-H_n(r)]`.

Let `c=A/n`. Equation (7.14) is

`(a/c) B E(q)=F_{n,2}(q)-a nr.`                           (7.15)

Since `gamma=1/4<a/c` by (7.9),

`P(gamma q)/gamma
 =a nr+gamma B E(q)
 <=a nr+(a/c)B E(q)
 =F_{n,2}(q).`                                             (7.16)

This is exactly (7.3). QED.

## 8. What moved mathematically, and what did not

This theorem closes an infinite, all-dimension, all-scale **homogeneous-base / k=2** slice of Talagrand Problem 10.9 with the explicit universal constant `1/4`. It is stronger than a numerical experiment or a finite-`n` certificate and is source-relevant because it uses exactly Talagrand's `C_gamma` definition and permits `P` to depend on `q` exactly as the source permits.

It does **not** solve Problem 10.9. Two major quantifiers remain:

1. arbitrary heterogeneous base points `q`, even still for `k=2`;
2. all intermediate thresholds `k>=3`.

The proof also explains why the earlier pure-degree route looked stuck: the successful large-activity certificate needs a base-point-tuned mixture of degree one and degree two, with the tangent coefficient selected by the monotone scalar hazard `Q_n`.

I do not claim publication novelty. The mechanism uses elementary convexity and a tailored positive polynomial; a deeper prior-art check is required before any novelty statement. The bounded search this run did not locate this exact homogeneous theorem.

F0111 therefore remains

`OPEN-looking / PARTIAL SLICE PROVED / HARD-leaning / NOT CLOSABLE-ready / NOT CLAIMED`.

## 9. Method #26 — what the simplest nontrivial sector teaches the next route

The `k=2` sector isolates the feature a full proof will need: a **mixed-degree envelope whose coefficient is selected by a one-dimensional tangent/hazard quantity**. R20's separate-gap no-go does not apply because the envelope controls the total free energy directly and retains the cancellation between the linear and quadratic terms.

The next natural research question, if F0111 is ever separately admitted, is not another symmetric computation. It is whether one can break the homogeneous symmetry while preserving tangent tightness, for example by replacing `aT+B e_2(t)` with

`sum_i a_i t_i + sum_{i<j} b_{ij} t_i t_j`

and deriving the coefficients from a multivariate supporting-hyperplane condition at a heterogeneous `q`. A successful heterogeneous `k=2` theorem would still be only a slice of Problem 10.9 but would remove the first major remaining quantifier.

## 10. Admission conclusion and ownership

The newest coordinator report available at run start, `operations/task_health/runs/2026-09-18T065500Z/status.md`, still reports no race-safe newly available source crossing every admission gate. Current search also finds no canonical `operations/claims/F0111.md`, but absence of a claim is **not** enough: F0111 remains source-wide HARD rather than genuinely CLOSABLE.

No candidate inspected here satisfies simultaneously:

1. exact outside source and full source-matching scope;
2. current-open status after bounded later-literature checks;
3. a genuinely CLOSABLE full-source metric rather than a restricted slice;
4. no canonical owner/reservation.

Therefore the official R15 successor-admission metric remains

`E_ready = 0 -> 0`.

The admission-gate unchanged count remains `UNKNOWN`; I do not invent a streak value. No ownership file was created.

## 11. Model / scheduler / authorization status

Still true in this run: the exposed task-management surface provides prompt/title, schedule or relative start, timing mode, and enabled state, but **no binding model-family selector, no reasoning-effort selector, no authenticated completed-run model telemetry, and no guaranteed hour-long-runtime field**. GPT-6/maximum therefore remains a prompt request only on this surface.

The historical P26 `You cannot modify this task` event is authorization-context dependent: repository operations records show that a later authorized context successfully updated P26. The lawful workaround is therefore the owning/authorized task context, a supported owner/admin reassignment, or platform support. It is not duplicate-task creation or a permission bypass.

I made no scheduler, permission, email/Gmail, Drive, public-posting, purchase, credential, or shared-root change.

## 12. Validation / audit boundary

The new claims in Sections 5--7 are analytic and their full arguments are written on the page. No numerical path sample is used as evidence for any Brownian law, and no finite exhaustive claim was introduced that would justify spending this run on a checker. This report is a **self-check only**; no independent P26 or other-track audit is claimed.

The Brownian source itself remains retired-handoff / partial at `2/4`; no closure package is created.

## 13. Structured ledger delta

```yaml
ledger_delta:
  worker: R15
  lane: CLOSABLE_OUTSIDE_ROTATION_GATE
  original_source: "Krzysztof Burdzy and Michael Scheutzow, Forward Brownian Motion, Problem 7.2, arXiv:1302.6958; intake I0076"
  original_metric: "number of four source-matching obligations proved for one frozen counterexample candidate"
  original_metric_before: "2/4"
  original_metric_after: "2/4"
  original_status: "OPEN / PARTIAL / RETIRED-HANDOFF"
  surviving_frozen_candidate: false
  successor_admission_metric: E_ready
  successor_before: 0
  successor_after: 0
  unchanged_count: UNKNOWN
  tried_moves: [5, 13, 26]
  new_self_checked_result:
    source: "Michel Talagrand, Are Many Small Sets Explicitly Small?, STOC 2010, Problem 10.9"
    scope: "k=2 and homogeneous base q=r*1_n, all n>=2 and all r>=0"
    theorem: "source C_gamma majorant condition holds with gamma=1/4"
    status: "PARTIAL_SLICE_PROVED_SELF_CHECK_ONLY"
    novelty: "UNVERIFIED"
    ownership_claim_created: false
  remaining_obligation: "find a source-clean, current-open, genuinely CLOSABLE, ownership-clear outside successor; for F0111 itself, heterogeneous q and k>=3 remain"
  evidence:
    - "runs/R15/20260918_0612Z_successor_admission_f0111_fkg_sendov_g51a.md"
    - "runs/R20/2026-09-18T07-10-19Z_successor_admission_f0111_conservative_gap_nogo_3d426b.md"
    - "runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md"
    - "operations/task_health/runs/2026-09-18T065500Z/status.md"
  audit_ids: []
```

Next fresh section-B methods if the admission gate is still empty: **#11 DUALIZE, #24 FIND THE EXTREMAL OBJECT, #30 ONE SCALE / ONE DIRECTION AT A TIME**. These should be applied to a newly verified successor if one appears; they do not authorize a seventh attack on retired I0076.
