Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.** Movement on the frozen P0151 metric: **`gamma_E >= b5 -> gamma_E >= b6` with `b6>b5`; methods actually tried: B2 / B3 / B24.**

# HARD7-04 bounded research iteration — capped-quadratic bridge amplification for fixed-outdegree PA criticality

Status: **PARTIAL / SOURCE OPEN**. This run gives a strict new lower-bound advance for the exact admitted sequential fixed-outdegree preferential-attachment model. It does **not** identify the full critical window, prove a matching upper bound, establish `sqrt(n)/log n` scaling, or produce a scaling-limit law.

The complete proof is archived at

`artifacts/hard7_2026-09-18/HARD7-04/p0151_capped_quadratic_bridge_20260920T0432Z.md`

created at commit

`cbb837016aaa2d920add76c86fbb3f265246186d`

and read back at that exact SHA before this report was written.

---

## 1. Continuity, ownership, and evidence consumed

I resumed the exclusive canonical claim

`operations/claims/P0151.md`

owned by `HARD7-04`. I did not restart I0049, P0157, the configuration-model MST route, the conditionally-independent-edge threshold comparison, or any already-solved degree-count problem.

Before the new mathematics I reread/reconciled the required control and campaign surfaces:

- `operations/hard7_2026-09-18/CONTROL.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/claims/P0151.md`;
- the P0151 intake/catalog trace, including the intake-tier row `P0151|3|critical window, fixed-outdegree PA`;
- the current neighboring preferential-attachment history, especially `runs/R08/20260917T2326Z_i0048_threshold_comparison_73b9e1.md`;
- the full current HARD7-04 P0151 chain through the immediately preceding report `runs/hard7_2026-09-18/HARD7-04/2026-09-20T0330Z__p0151_log_age_spectral_window.md`.

A repository-wide ownership search still shows `P0151` exclusively owned by HARD7-04. No peer claim collision or posted source-equivalent paper surfaced. The R08 neighboring track treats the threshold-comparison scope as later-literature-known and does not own this fixed-outdegree critical-window target.

The immediately preceding HARD7-04 run had the first no-movement episode after the strict chain

`b1 -> b2 -> b3 -> b4 -> b5`.

It proved an auxiliary killed-Pólya-point-tree spectral theorem but left the finite-graph metric at `b5`. This run changes mechanism again and moves the frozen finite-graph metric, so the Section-I stagnation counter resets.

---

## 2. Source/current-literature refresh — 20 September 2026

The frozen source model remains Ray's sequential fixed-outdegree affine preferential-attachment model `(d)` with fixed integer `m>=2`, fixed `delta>0`, exactly `m` sequential out-edges per arriving vertex, current-degree-plus-`delta` attachment weights, and independent bond retention `pi` after graph generation.

The exact threshold from Hazra--van der Hofstad--Ray is

`pi_c = delta/[2( m(m+delta)+sqrt(m(m-1)(m+delta)(m+1+delta)) )]`.

Fresh bounded searches on **20 September 2026** rechecked the exact fixed-outdegree wording and the newest nearby critical-window papers:

1. Rajat Subhra Hazra, Remco van der Hofstad, Rounak Ray, *Percolation on preferential attachment models*, arXiv:2312.14085 / EJP 31 (2026), `https://arxiv.org/abs/2312.14085`. It identifies the threshold and giant/no-giant dichotomy for the fixed-outdegree affine PA model. I did not find a finite-size critical-window theorem for this exact sequential fixed-`m` model there.
2. Joost Jorritsma, Pascal Maillard, Peter Mörters, *The critical percolation window in growing random graphs*, arXiv:2512.18937, submitted 22 December 2025, `https://arxiv.org/abs/2512.18937`. It proves a `(log n)^(-2)` window and `sqrt(n)/log n` critical largest-component scale in models where each new vertex connects **independently** to earlier vertices. That does not automatically cover the exact fixed-outdegree sequential model here.
3. Peter Mörters, Lucas Schätze, *Critical percolation on preferential attachment graphs with infinite variance*, arXiv:2606.27844, submitted 26 June 2026, `https://arxiv.org/abs/2606.27844`. It studies an inhomogeneous preferential-attachment-kernel graph with `tau in (2,3)` and a moving threshold `p_n`, a different ensemble and regime.

No source-matching finite fixed-outdegree critical-window resolution surfaced in this bounded refresh. This is bounded negative evidence, not a claim of worldwide novelty.

---

## 3. Frozen source metric and before/after

Put

`a:=m+delta`, `A:=2m+delta=a+m`.

For the largest critical percolation component define, as at admission,

`gamma_E:=liminf_{n->infinity} log E|C_max(n,pi_c)| / log n`.

The preceding strict lower bound was

`gamma_E>=b5`,

where

`b2:=m(1+a pi_c)/A`,

`b5:=b2+m(m-1)pi_c^2 a/A`.

This run proves

`gamma_E>=b6`,

with

`b6:=b2+m(m-1)pi_c^2`.                                           (3.1)

The increment over the preceding bound is

`b6-b5
 =m(m-1)pi_c^2(1-a/A)
 =m^2(m-1)pi_c^2/A
 >0`.                                                              (3.2)

Thus the frozen source-relevant metric moves strictly:

**Before:** `gamma_E>=b5`.

**After:** `gamma_E>=b6>b5`.

The proof also gives `b6<1/2`, so this remains a genuine restricted lower bound and is not relabeled as a full critical-window theorem.

For orientation only, not proof, at `m=2, delta=1`:

`pi_c≈0.0458758547681`,

`b5≈0.457576538583`,

`b6≈0.459260213823`.

---

## 4. Idea before code: cap the bridge numerator at the extremal mean scale

The previous full-attractiveness route used bridge acceptance probability `a/w` and therefore gave a constant accepted numerator `a`. The 03:30 run then changed to the spectral local-limit picture. The new idea here is different from both:

> accept an outside retained target of current attractiveness `w` with probability `min(w,2A)/w`.

This keeps every accepted-target probability bounded by a deterministic `2A/t`, so the existing global square-attractiveness budget can still close the second moment. At the same time it rewards moderate-degree outside vertices more heavily than the old `a/w` thinning.

The choice `2A` is not arbitrary. For `c_s(w)=min(w,2s)`,

`w c_s(w)>=2s w-s^2`.

Summed over at most `t+O(1)` outside vertices of total leading attractiveness `At`, the guaranteed leading coefficient is

`2sA-s^2=A^2-(s-A)^2`,

which is maximized at `s=A`. This is the B24 extremal calculation that selected the cap before the proof was written.

No code was needed to discover or validate this analytic mechanism; the proof is on the page in the matching artifact.

---

## 5. B2 — attack the negation: remove the cap entirely

I first tried the stronger-looking rule: whenever a birth has a retained gate into the current connected shadow, capture every retained outside target with no thinning.

That route exposes the obstruction cleanly. A weighted bridge contribution then carries `w^2`; controlling the square of the new jump introduces cubic-weight or equivalent mixed terms. The available uniform source-range budget is

`E sum_u w_u(t)^2=O(t)`

for every `delta>0`. That estimate alone does not control the required cubic/mixed correction uniformly over the full source class. So the uncapped route does not presently furnish a valid all-`delta>0` second-moment bootstrap.

**Outcome of B2:** failed as a uniform proof route, but it identified precisely why a bounded degree-sensitive acceptance numerator is the right compromise. This is not a counterexample to the source statement.

---

## 6. B24 — optimize the bounded acceptance profile

Take

`c(w):=min(w,2A)`.

For every `w>=0`,

`w c(w)>=2A w-A^2`.                                               (6.1)

If `Q_t` is the connected shadow, `W_t` its true attractiveness, `Z_t` the two-seed attractiveness, and `T_t=At+O(1)` the total attractiveness, then for eligible outside ordinary vertices

`F_t:=sum_{u notin Q_t,u>=3} w_u(t)c(w_u(t))`

satisfies

`F_t>=A^2 t-2A(W_t+Z_t)-C`.                                      (6.2)

This is the key new deterministic inequality. The old constant-numerator thinning retained only an `aA t` leading outside term; the optimized capped quadratic profile recovers `A^2 t` while still keeping each accepted bridge probability `O(1/t)`.

**Outcome of B24:** succeeded and produced the exact coefficient that makes the new exponent move possible.

---

## 7. B3 — prove the stronger capped-bridge theorem

The process and proof are given fully in the artifact. The essential steps are as follows.

### 7.1 Connected shadow and exact increment

A **gate** is a retained edge from the new birth into the frozen current shadow. An outside retained target `u` is accepted as a bridge with auxiliary probability

`c(w_u(current))/w_u(current)`.

If a gate occurs, capture all distinct accepted outside roots. Connectivity is preserved in the true percolated graph. If `H_t` counts all birth edges hitting the old shadow, `I_t` is the gate indicator, and `J_t` is the final attractiveness of distinct newly captured bridge roots, then

`W_{t+1}-W_t=H_t+aI_t+J_t`.                                      (7.1)

### 7.2 Lower bridge drift

Let `G_t` be the number of gates and let `Y_t` be the frozen weighted accepted-bridge sum. Distinctness is handled by

`D_t>=G_tY_t-Y_t binom(G_t,2)-C_same`.                            (7.2)

For every ordered gate/bridge edge-label pair and outside root, sequential conditioning cancels the target weight against the acceptance ratio. With (6.2),

`E[J_t|F_t]
 >= m(m-1)pi_c^2 W_t/t
    -C W_t^2/t^2
    -C W_t Z_t/t^2
    -C W_t/t^2
    -C/t`.                                                         (7.3)

The duplicate-root correction is `O(1/t)` and the two-gate correction is `O((W_t^2+1)/t^2)` because the cap makes every prescribed accepted bridge probability `O(1/t)`.

Adding the ordinary target-hit and gate-activation drift yields

`E[W_{t+1}-W_t|F_t]
 >= b6 W_t/t
    -C W_t^2/t^2
    -C W_tZ_t/t^2
    -C W_t/t^2
    -C/t`.                                                         (7.4)

### 7.3 The cap still closes the second moment

The same cap gives an upper bridge drift

`E[J_t|F_t] <= [eta_U/t+O(t^-2)]W_t+C/t`,

where

`eta_U:=2m(m-1)pi_c^2(A+m)/A`.                                   (7.5)

Set

`b_U:=b2+eta_U`.

The artifact gives an exact algebraic proof that

`b_U<1/2`                                                         (7.6)

for every `m>=2`, `delta>0`. Writing

`r0=sqrt(m(m-1)(a+1)/a)`,

`x=a pi_c=(a-m)/[2(m+r0)]`,

one has `1/2-b2=xr0/A`; after substitution the required strict inequality reduces to a positive elementary comparison, with the only nontrivial fallback estimate

`(m-1)^2<a r0`.

For square jumps, `c<=2A` and Cauchy give

`E[J_t^2|F_t] <= C(V_t+t)/t`,                                    (7.7)

where the global square-attractiveness sum satisfies `E V_t=O(t)`. Therefore, after total expectation,

`E W_t^2=O(t)`.                                                    (7.8)

### 7.4 Mean bootstrap and conversion to component size

The two-seed attractiveness has `E Z_t=O(t^h)`, `h=m/A<1/2`. Taking expectations in (7.4) and using (7.8),

`mu_{t+1}
 >= [1+b6/t-C/t^2]mu_t-C/t-Ct^{h-1}`.                            (7.9)

A global concavity chord for the gate activation law supplies a polynomial seed exponent

`b1=[m+a(1-(1-pi_c)^m)]/A>h`.

Normalizing (7.9) by the comparison product `Theta(t^{b6})`, the error tail is `O(T^{h-b6})` while the normalized seed is `Omega(T^{b1-b6})`; since `b1>h`, one fixed sufficiently large start time makes the seed dominate the entire remaining error tail. Hence

`E W_n>=c n^{b6}`.                                                (7.10)

The same gate chord then gives

`E|Q_n|>=c' n^{b6}`,

and `Q_n` is contained in one true percolation component. Therefore

`gamma_E>=b6`.                                                     (7.11)

**Outcome of B3:** succeeded. This is a strict theorem-level improvement of the frozen source metric under exactly the admitted assumptions.

---

## 8. Why this still does not solve the source problem

The result moves the expected-size lower exponent but leaves a positive power gap to `1/2`. It does not prove:

- an upper exponent;
- `gamma_E=1/2`;
- the `sqrt(n)/log n` order suggested by the neighboring independent-edge model;
- a `(log n)^(-2)` critical window;
- tightness, surplus scaling, or a limiting component sequence.

The strongest auxiliary fact from the preceding run remains useful but unpaid at finite-graph level:

`1-r(pi_c T_L)=C_spec/L^2+O(L^-3)`

for the killed critical Pólya-point-tree mean operator in log-age width `L`.

The next genuinely different obligation is not another local bridge coefficient. It is to connect this exact local spectral loss to a finite sequential exploration with an error small on the `(log n)^(-2)` scale, or to find a counterexample showing that the fixed-outdegree dependence changes that transfer.

---

## 9. Actual validation performed

- Read the exact active P0151 claim and confirmed exclusive HARD7-04 ownership.
- Re-read the controlling policy, current posting/exclusion surfaces, fleet ledger/queue, newest own P0151 report, and neighboring preferential-attachment report before research.
- Rechecked the intake/catalog trace for P0151.
- Reran dated literature queries on 20 September 2026 against the exact fixed-outdegree model and the 2025--2026 nearby critical-window papers.
- Wrote the new mathematical idea before any validation artifact.
- Tried three materially different methods: **B2 / B3 / B24**; this triple differs from the previous **B18 / B7 / B5**.
- Re-derived the deterministic quadratic envelope, ordered gate--bridge count, duplicate and multi-gate corrections, upper drift, square-jump bound, exact `b_U<1/2` inequality, bootstrap, and component-size conversion.
- No simulation is used as proof. No finite exhaustive claim was made, so no exact-arithmetic checker was warranted. The substantive object is an analytic theorem and its complete proof is in the artifact.
- Read back the artifact at commit `cbb837016aaa2d920add76c86fbb3f265246186d`.

---

## 10. Scheduler/model capability statement required by owner

The runtime identifies as **GPT-5.6 Sol**. Reasoning level is **UNVERIFIED**. I therefore do not claim GPT-6 or maximum reasoning.

The repository control surfaces still record the same native-interface limitation: the exposed scheduler operations provide title, prompt, schedule, timing mode, and enabled state, but **no authenticated model selector, no reasoning-effort selector, and no guaranteed execution duration**. GPT-6 maximum can only be requested in prompt text in this interface. Changing the actual model/effort would require the platform to expose an authenticated model/effort control for this task or an authorized account/workspace-level capability; editing repository text cannot do it.

The current policy also records historical modification probes for P26/P01/P03 returning **“You cannot modify this task.”** The authorized workaround is to resolve task/account/workspace ownership through the platform's permitted interface or support. It is **not** to bypass the restriction, clone the job, or encode a scheduler change in GitHub.

Per this HARD7-04 prompt, I made **no scheduler modification** and did not alter cadence or enabled state.

---

## 11. Status and next checkpoint

Source status: **OPEN**.

Track status: **PARTIAL**.

Frozen metric movement this run:

`gamma_E>=b5 -> gamma_E>=b6`,

where

`b6=m(1+(m+delta)pi_c)/(2m+delta)+m(m-1)pi_c^2`.

Stagnation count on P0151 returns to `0` because the source-relevant quantity moved strictly.

A subsequent run must use a different method triple from `B2/B3/B24`. The recommended next direction is a genuine finite-to-local spectral transfer rather than another bounded local bridge amplification; e.g. B6 deformation from the killed-PPT process, B19 explicit exploration algorithm, and B30 localization by log-age scale, unless ownership/current literature changes first.

### Own-track ledger delta only

`HARD7-04 | P0151 fixed-outdegree PA critical window | gamma_E lower bound | b5 -> b6=b2+m(m-1)pi_c^2 | PARTIAL / SOURCE OPEN`

No shared root ledger, peer claim, schedule, email, Drive file, permission, workflow, or public posting was modified in this run.
