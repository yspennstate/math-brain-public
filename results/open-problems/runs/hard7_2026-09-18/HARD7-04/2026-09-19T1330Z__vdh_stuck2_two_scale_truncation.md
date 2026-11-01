Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. NO MOVEMENT in the frozen metric `lim Delta_dual,n`: `0 -> 0`; this is the mandatory STUCK2 thinking/recovery run, so no new theorem-sized or finite claim is promoted. New route-finding moves: B17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE, B27 SWAP THE QUANTIFIERS, B29 ADD THE POINTS AT INFINITY.**

# HARD7-04 bounded research iteration — STUCK2: two-scale truncation and a coefficient-saddle route

Repository / branch: private `yspennstate/math-open-problems` / `master`.

Status: **PARTIAL / source OPEN / STUCK2**.

## 1. Continuity, ownership, required reads, and capability honesty

I resumed the admitted target `VDH-8.3-DUALITY`; I did not restart admission, return to I0049/P0157, overwrite another claim, edit a peer track, or modify any schedule. The exclusive canonical claim remains

`operations/claims/VDH-8.3-DUALITY.md`, owner `HARD7-04`, status OPEN / ADMITTED.

The primary source remains Remco van der Hofstad, *Stochastic processes on random graphs*, preliminary monograph dated **4 August 2026**, Notes on Section 8.3, printed p. 245 / PDF p. 255. The source says that the van der Hofstad--Janson--Luczak barely-supercritical work does not determine the second-largest component, observes that high-degree vertices should lie in the unique giant, and asks:

> “Does the discrete duality principle still hold?”

The exact retained regime is the deterministic-degree configuration model in the finite-third-moment barely-supercritical window,

\[
\nu_n=1+\varepsilon_n,\qquad
\varepsilon_n\downarrow0,\qquad
\varepsilon_n n^{1/3}\to\infty,
\]

with positive limiting mean, uniformly integrable third degree moment in the finite-third-moment case, and the source's nondegenerate critical limiting law.

At run start I re-read/recovered the controlling files `operations/hard7_2026-09-18/CONTROL.md`, `operations/NEW_METHODS_2026-09-16.md`, and `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`; campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`; root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`; the active claim; the latest complete own checkpoint `2026-09-19T1230Z__vdh_bounded_threepoint_lower_bound.md`; the preceding STUCK1 obstruction report; and the newest complete neighboring HARD7-03 and HARD7-05 reports. I also refreshed targeted repository/intake searches around `I0049`, `VDH-8.3-DUALITY`, `discrete duality`, and the source wording. The large `probability_1000_intake_*/problems.jsonl` collections cannot be rendered byte-for-byte through one connector response, so I used indexed source/alias/claim searches rather than falsely claiming a literal full-file dump. I0049 remains recorded as KNOWN/resolved in its queued scope, and no competing claim, release, posted equivalent, or repository closure marker was found for the active VDH target.

The scheduler/interface capability statement is unchanged. The exposed automation schema provides prompt/title, schedule/timing mode, enablement, and task identity/update fields; it has **no model selector and no reasoning-effort selector**. GPT-6/maximum therefore remains prompt-requested only. This runtime identifies as GPT-5.6 Sol; reasoning effort is not exposed, hence UNVERIFIED. Changing that requires a platform/scheduler feature or another authorized interface that actually exposes model/reasoning selectors, not a repository edit. Historical `You cannot modify this task` failures for P26/P01/P03 were context/ownership restrictions; repository records later show that P26 was editable from another authorized context. The compliant workaround is the authorized owning context or platform support, never permission bypass and never a duplicate schedule. I did not probe or mutate another task in this run.

## 2. Fresh source and literature check — 19 September 2026

I re-opened the current source PDF directly. Its front matter is dated 4 August 2026, and the Notes on Section 8.3 still contain the exact second-largest-component/discrete-duality question above.

I refreshed bounded searches for `barely supercritical configuration model second largest component`, `configuration model discrete duality`, and `largest subcritical component given degree sequence`. The closest published results remain:

1. R. van der Hofstad, S. Janson, M. J. Luczak, *Component structure of the configuration model: Barely supercritical case*, Random Structures & Algorithms 55 (2019). It determines the barely-supercritical giant under broad assumptions, including the finite-third-moment regime, but does not determine the source's requested second-largest scaling.
2. M. Coulson, G. Perarnau, *Largest component of subcritical random graphs with given degree sequence*, Electronic Journal of Probability 28 (2023), DOI `10.1214/23-EJP921`, arXiv `2111.11780`. Their Theorem 1.3 gives the sharp Erdős--Rényi-scale **upper** bound when `Delta |Q|=o(R)`; their paper explicitly develops a local limit theorem allowing large degrees and non-unit lattice span. The abstract and theorem remain upper-bound statements in the general CM setting, with asymptotic tightness exhibited for certain sequences rather than a uniform lower theorem matching the source class.
3. O. Riordan, *The phase transition in the configuration model* (2012). As summarized by Coulson--Perarnau, uniformly bounded degrees admit asymptotic equality (indeed with second-order control), so bounded degree is the nearest solved lower-bound setting.
4. van der Hofstad--Luczak--Spencer, *The second largest component in the supercritical 2D Hamming graph* (RSA 2010), gives model-specific evidence for discrete duality but not the deterministic-degree configuration-model theorem.

A bounded search on 19 September 2026 found no later theorem closing the exact source scope. This is bounded negative evidence only, not a worldwide novelty certificate.

## 3. Frozen metric and why this run is STUCK2

The frozen admission metric remains

\[
\Delta_{\rm dual,n}
=\left|\frac{1-\nu_n^{\rm dual}}{\varepsilon_n}-1\right|.
\]

Earlier VDH runs proved `Delta_dual,n -> 0` and transferred the reflected criticality to the exact post-giant configuration-model remainder. The metric is therefore at its mathematical floor. The previous STUCK1 recovery then proved the matching lower leading constant in the concrete bounded `{1,2,3}` special case, but the frozen metric still stayed at zero.

Thus this run records honestly

`lim Delta_dual,n: 0 -> 0` — **NO MOVEMENT**.

Under Section I this is the second thinking/recovery episode on `VDH-8.3-DUALITY`. Accordingly I do not manufacture a new checker or promote a planning calculation to a theorem. The purpose of this report is to isolate the remaining full-source obstruction and choose exactly one recovery route for the next bounded execution.

---

# Section-I STUCK2 report

## 4(a). Exact blocking statement

Write

\[
N_n:=n\varepsilon_n^3\to\infty,
\qquad
R_*:=\frac{\mathbb E[D(D-2)^2]}{\mathbb ED}>0.
\]

The already proved upper direction is

\[
L_1^{\rm post}
\le (1+o_p(1))\frac{2R_*}{\varepsilon_n^2}\log N_n.
\]

The exact unresolved source-level size obligation is still the matching lower direction

\[
\boxed{
\forall\delta>0:\quad
\mathbb P\!\left(
L_1^{\rm post}<
(1-\delta)\frac{2R_*}{\varepsilon_n^2}\log N_n
\right)\longrightarrow0.
}
\tag{4.1}
\]

Here `L_1^{post}` is the largest component of the exact post-giant remainder, which the previous stopping-time reduction identifies w.h.p. with the original graph's second-largest component. A bounded-support lower theorem is not (4.1).

## 4(b). Routes tried and the precise reason each still falls short of (4.1)

### Route 1 — branching-process dual parameter

This route succeeded at the parameter level:

\[
1-\nu_n^{\rm dual}=\varepsilon_n(1+o(1)).
\]

**Why it stops:** the reflected drift does not imply existence of an extreme logarithmic component. It controls a typical exploration, whereas (4.1) is an extreme-value statement over many dependent explorations.

### Route 2 — exact post-giant configuration-model reduction

The lawful completed-component stopping boundary leaves an exact configuration model on the random residual degree sequence; its largest component is w.h.p. the original `C_{2,n}`.

**Why it stops:** exact identification of the residual model transfers rather than solves the largest-subcritical-component lower bound.

### Route 3 — black-box the sharpest convenient subcritical theorem

Coulson--Perarnau Theorem 1.3 has the desired leading upper expression `2R/Q^2`, but assumes `Delta |Q|=o(R)`.

**Why it stops:** the previous sharp hub-stripping work showed that the post-giant source class can reach

\[
\frac{\varepsilon_n\Delta_n^{\rm post}}{\log N_n}
\le \frac{R_*}{2}+o_p(1)
\]

with the constant source-validly sharp. Thus the convenient small-hub hypothesis is genuinely unavailable at the edge of the source class.

### Route 4 — one-root Cramer/exploration estimate

The post-giant clock thinning gave a shrinking-window exponential collar and the sharp Cramer rate

\[
\theta_n=(1+o_p(1))\frac{\varepsilon_n}{R_*},
\qquad
I_n=(1+o_p(1))\frac{\varepsilon_n^2}{2R_*},
\]

which was enough, together with an elementary anti-concentration estimate, to prove the sharp **upper** leading constant.

**Why it stops:** stochastic domination and one-root tail bounds point in the wrong direction for existence. A lower theorem must count many realizable components and control their overlap.

### Route 5 — first-moment abundance

At sizes

\[
k\asymp (1-\delta)\frac{2R_*}{\varepsilon_n^2}\log N_n,
\]

the saddle exponent predicts a divergent supply of candidate trees below the extreme threshold.

**Why it stops:** a divergent first moment alone can be concentrated on highly overlapping candidates. It needs a second moment, switching, or another decorrelation device.

### Route 6 — bounded three-point tree census

The STUCK1 recovery succeeded completely for the deterministic `{1,2,3}` law with limiting proportions `(3/8,1/2,1/8)`. Exact tree enumeration plus a size window and a second-moment cancellation proved

\[
L_1\ge (1-o_p(1))\frac{6}{7\varepsilon_n^2}\log(n\varepsilon_n^3).
\]

The key finite-population cancellation is the critical identity

\[
\sum_d\frac{q_d^2}{p_d}=\frac{\mathbb E D^2}{\mu^2}=rac2\mu.
\]

**Why it stops:** the proof expands profile-wise falling factorials and uses a fixed finite support. In the actual residual sequence the support grows and some degree classes can have tiny multiplicity; a term-by-term `m_d^2/n_d` treatment is not uniform.

### Route 7 — naively truncate at `o(1/epsilon_n)` using only the original third moment

The natural thought is to throw away every degree above a cutoff `K_n=o(1/epsilon_n)` and apply the bounded-support proof.

**Why it stops if one uses only raw third-moment information:** uniform integrability of `D_n^3` has no source-uniform quantitative rate. A cutoff small enough that `epsilon_n K_n -> 0` need not make the discarded second-moment contribution `o(epsilon_n)`, which is the scale needed to preserve the reflected drift. This is precisely the kind of hidden rate assumption that the source does not grant.

### Route 8 — full untruncated second moment under the Cramer tilt

A direct saddlepoint second moment naturally brings in the squared tilted weights, hence an `exp(2 theta_n d)` scale.

**Why it is dangerous:** `2 theta_n/epsilon_n -> 2/R_*`, exactly the endpoint of the post-giant exponential collar proved earlier, which is available with slack only for fixed `lambda<2/R_*`. The same number `2/R_*` appears independently as (i) the clock-thinning exponential boundary and (ii) twice the Cramer saddle. This endpoint collision is the sharp place where the untruncated two-component argument loses room. I treat this as a route diagnosis, not as a theorem that no endpoint argument can work.

## 4(c). What a full proof must contain that no completed route currently contains

A proof of (4.1) still needs one argument that simultaneously provides:

1. a **lower** local large-deviation coefficient at the tree constraint `sum d_i=2k-2`, with exponent `epsilon_n^2/(2R_*)`;
2. a size window robust to lattice span;
3. finite-population and pairing corrections at `k=Theta(epsilon_n^{-2} log N_n)` without assuming every occupied degree class has macroscopic multiplicity;
4. a second-moment/decorrelation estimate for the number of such tree components;
5. a way to handle the residual high-degree tail without asking for exponential integrability exactly at the no-slack endpoint `2/R_*`;
6. all of the above conditional on the random post-giant residual degree sequence on one high-probability event.

The bounded `{1,2,3}` proof supplies items 1--4 only when support is fixed. The Cramer-collar upper proof supplies the tail information needed for item 5 but only one-sidedly. The missing bridge is a two-scale argument that uses the already proved collar to discard a vanishing amount of moment mass **before** doing the lower saddlepoint calculation.

## 4(d). Simplest special case still unproved after the bounded `{1,2,3}` recovery

The next clean special case is not another fixed finite support. It is a deterministic barely-subcritical triangular degree sequence satisfying

\[
Q_n=-\varepsilon_n(1+o(1)),\qquad
R_n\to R_*>0,\qquad
N_n=n\varepsilon_n^3\to\infty,
\]

with the same fixed nondegenerate low-degree atoms as the source limit, together with the **post-giant-type exponential collar**

\[
\forall\lambda<2/R_*:\qquad
\frac{\varepsilon_n}{n}
\sum_v d_v^4 e^{\lambda\varepsilon_n d_v}\to0.
\tag{4.2}
\]

The special-case target is to prove the lower constant by counting only tree components whose degrees are at most `a/epsilon_n`, for fixed `a>0`, obtaining an error that tends to zero as `a downarrow 0` after `n -> infinity`.

This is the simplest useful enlargement because (4.2) is already inherited on high-probability post-giant events from the previous VDH Cramer-collar theorem; it does not introduce an arbitrary fourth-moment hypothesis unrelated to the source.

## 4(e). Nearest solved problem and the ingredient it has that the source lacks

The nearest solved lower-bound setting is **Riordan's uniformly bounded-degree configuration model**, for which the barely-subcritical largest component has the Erdős--Rényi leading asymptotic (and more detailed control). Coulson--Perarnau explicitly cite this as the bounded-degree case where their sharp upper scale is an asymptotic equality. The HARD7-04 `{1,2,3}` theorem independently recovers the lower mechanism in one explicit bounded law.

What bounded degree supplies automatically is a uniform saddlepoint/local-limit regime and harmless finite-population coefficient expansion: no tilted mass can escape to degree scales comparable to `1/epsilon_n`, and the second-order finite-population correction stays inside a fixed compact degree space. The full source class lacks precisely that compactness.

The recovery selected below is therefore to **port the bounded-degree coefficient/tree-census technique through a fixed scaled cutoff and only then remove the cutoff**.

---

# 5. Three new route-finding moves

The previous run used B4/B12/B25, and STUCK1 used B18/B22/B30. The following triple was not used previously on the admitted VDH target in the indexed HARD7-04 reports I checked.

## B17 — LOOK FOR YOUR NUMBERS SOMEWHERE ELSE

The important numerical coincidence is not a fitted constant. It is the same analytic boundary appearing in two different calculations:

- the proved post-giant clock thinning controls exponential moments for every fixed `lambda<2/R_*`;
- the one-component Cramer saddle has `theta_n/epsilon_n -> 1/R_*`, so a naive **two-component** saddle samples weights at approximately `2 theta_n`, i.e. exactly `2/R_*`.

This explains why the first-moment/upper-tail machinery can have comfortable slack while the untruncated second moment hits the boundary. The endpoint coincidence gives a concrete reason not to spend another run forcing a global profile expansion at full support.

**B17 outcome:** useful obstruction diagnosis. It identifies the scale that a successful lower proof must avoid rather than another lemma on the failed full-support route.

## B27 — SWAP THE QUANTIFIERS

Introduce a fixed scaled cutoff

\[
K_n(a):=\left\lfloor\frac{a}{\varepsilon_n}\right\rfloor,
\qquad a>0\text{ fixed}.
\]

Do **not** choose `a=a_n -> 0` at the start. The proposed order is:

1. fix the source lower-bound tolerance `delta>0`;
2. choose a sufficiently small constant `a=a(delta)>0`;
3. let `n->infinity` with this fixed `a`;
4. only after the asymptotic estimate is established, let `a downarrow 0` in the deterministic error bound.

The already proved collar (4.2) suggests exactly why this order has room. For `j=1,2,3`, fixed `lambda<2/R_*`, and degrees above `a/epsilon_n`, the elementary comparison

\[
d^j
\le d^4\left(\frac{\varepsilon_n}{a}\right)^{4-j},
\qquad
e^{\lambda\varepsilon_n d}\ge e^{\lambda a},
\]

turns the inherited collar into the scale table

\[
\frac1n\sum_{d_v>K_n(a)}d_v=o_p(\varepsilon_n^2),
\]

\[
\frac1n\sum_{d_v>K_n(a)}d_v^2=o_p(\varepsilon_n),
\]

\[
\frac1n\sum_{d_v>K_n(a)}d_v^3=o_p(1),
\tag{5.1}
\]

for every fixed `a>0` (with constants depending on `a,lambda`). These are planning consequences of the previously proved collar, not promoted here as a separate theorem.

They are exactly the scales one wants: the retained half-edge mass changes only by `o_p(n epsilon_n^2)`, the subcritical drift numerator only by `o_p(n epsilon_n)`, and `R_n` only by `o_p(n)`. Thus a fixed scaled cutoff can preserve the leading drift and variance even though a raw `o(1/epsilon_n)` cutoff cannot be justified from third-moment uniform integrability alone.

At the same time, on the truncated set

\[
\varepsilon_n d\le a,
\]

so every Taylor/saddlepoint remainder can carry an explicit error `O(a)` instead of demanding `epsilon_n Delta_n ->0` globally. At target component size

\[
k=\Theta(\varepsilon_n^{-2}\log N_n),
\]

the finite-population small parameter satisfies

\[
\frac{kK_n(a)}{n}=O\!\left(\frac{a\log N_n}{N_n}\right)\to0.
\tag{5.2}
\]

**B27 outcome:** this removes the false choice between “cutoff small enough for Taylor” and “tail small enough to preserve drift.” The order of limits supplies both, at the cost of carrying an explicit `a`-error and taking `a downarrow0` only after the `n`-limit.

## B29 — ADD THE POINTS AT INFINITY

The profile-by-profile proof is fragile because tiny `p_d` make expressions such as `m_d^2/n_d` look singular. Instead, compactify the tail at the cutoff and keep the entire retained degree range inside one generating product. For the retained degrees define the candidate coefficient object

\[
F_{n,a}(z,w)
:=\prod_{d\le K_n(a)}(1+z d w^d)^{n_d}.
\tag{5.3}
\]

The exact tree census can be reorganized around the coefficient with constraints “`k` vertices” and “total degree `2k-2`.” The proposed saddle uses `w=e^{theta}` near the Cramer tilt and `z` of order `k/n`.

The advantage is structural. At the target scale and fixed `a`,

\[
\max_{d\le K_n(a)} z d w^d
=O\!\left(\frac{a\log N_n}{N_n}\right)=o(1),
\]

so `log F_{n,a}` can be expanded globally rather than class by class. Its quadratic term is the same finite-population correction that the pairing ratio cancels at criticality; the dangerous `2 theta` weight is now harmless because `theta d=O(a)` on the retained range. Higher-order terms should be controlled by `N_n^{-1}` powers rather than inverse tiny class probabilities.

Equivalently, exponential tilting of (5.3) turns the desired coefficient into a two-dimensional local probability for a triangular array of independent Bernoulli selections, tracking simultaneously vertex count and degree sum. The remaining technical task is a **lower** two-dimensional lattice local limit estimate. For fixed `a`, the largest retained degree divided by the natural standard deviation at the target size is heuristically

\[
\frac{a/\varepsilon_n}{\sqrt{k}}
=O\!\left(\frac{a}{\sqrt{\log N_n}}\right)\to0,
\]

while the source's nondegenerate fixed atoms supply a nontrivial lattice direction. A short window of adjacent component sizes can absorb residual span issues just as in the bounded `{1,2,3}` proof.

**B29 outcome:** this changes the remaining task from controlling infinitely many profile errors to proving one bivariate saddle/local-limit lower bound plus one global pairing expansion, with the high-degree tail represented only through the removable boundary `d>K_n(a)`.

No local-limit theorem is claimed in this report; that is the next proof obligation.

# 6. Exactly one Section-I recovery selected

**Recovery choice: PORT THE TECHNIQUE FROM THE NEAREST SOLVED BOUNDED-DEGREE PROBLEM.**

The next HARD7-04 execution should try one route only:

> Port the Riordan / bounded-support tree-census lower mechanism to the post-giant collared sequence by fixing `a>0`, counting only tree components with degrees `d<=a/epsilon_n` through the global coefficient product (5.3), proving the required bivariate local coefficient lower bound and pairing cancellation uniformly at fixed `a`, and only then sending `a downarrow0` after `n->infinity`.

The target of that recovery is the full lower statement (4.1), not another upper bound and not a finite simulation. If the coefficient/local-limit step fails, the next report must record the precise failed inequality. This target has now consumed its two permitted Section-I thinking recoveries; a subsequent third stuck episode must hand off `VDH-8.3-DUALITY` and rotate rather than repeat the same obstruction.

# 7. Validation budget and claim discipline

This is deliberately a thinking/recovery run. No finite candidate was enumerated, no new exact constant was asserted, and no theorem-sized statement beyond previously checkpointed results is promoted. Therefore I did **not** spend the run manufacturing a checker for an unchanged metric. The displayed cutoff/saddle formulas are route calculations to be proved or rejected in the selected recovery; they are not labeled PROVED and do not alter the source status.

The source remains **OPEN** and the track remains **PARTIAL**. No closure audit is requested, no paper package is created, and no shared root ledger is edited.

## Checkpoint

```yaml
track: HARD7-04
target: VDH-8.3-DUALITY
owner: HARD7-04
source_status: OPEN
research_status: PARTIAL
stuck_state: STUCK2
runtime_model: GPT-5.6 Sol
reasoning_level: UNVERIFIED
requested_model_only: GPT-6 maximum
frozen_metric: lim Delta_dual,n
before: 0
after: 0
movement: false
methods:
  - B17
  - B27
  - B29
new_claims_promoted: none
recovery_selected: port bounded-degree tree-census technique through fixed scaled cutoff a/epsilon_n and global bivariate coefficient saddle, then a downarrow 0
next_exact_obligation: prove or refute the fixed-a bivariate local coefficient lower bound plus pairing cancellation strongly enough to imply the full post-giant lower constant
closure: false
```
