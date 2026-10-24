Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. NO MOVEMENT in the frozen VDH metric `lim Delta_dual,n`: `0 -> 0`; methods actually used: B7 TAKE THE LIMIT, B15 BREAK THE SYMMETRY ON PURPOSE, B26 HUNT THE SPORADIC CASE.**

# R14 HARD OUTSIDE — VDH bounded-degree prior-art correction and iid-thinning obstruction

Repository / branch: private `yspennstate/math-open-problems` / `master`.

Status: **PARTIAL / source OPEN / proof-capable follow-up after STUCK-RECOVERY-1/2 / new obstruction, no source-closure claim.**

## 1. Continuity and ownership

I resumed the canonical R14 assignment `VDH-8.3-DUALITY`; I did **not** reopen the stale scheduler-title negative-margin perceptron, H0008, or P0157. The canonical claim still lists R14 as exclusive owner after the HARD7-04 handoff.

Before research I reread/recovered the required campaign surfaces: `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, the controlling new-methods directive, the current VDH claim, the latest R14 recovery report, the preceding R14 truncated-susceptibility theorem, and the inherited HARD7-04 collared lower-bound / quantitative-histogram chain. I also checked current neighboring ownership records. No competing owner, posted source-matching closure, or release of the R14 VDH claim surfaced.

The frozen metric remains

\[
\Delta_{\rm dual,n}
=\left|\frac{1-\nu_n^{\rm dual}}{\varepsilon_n}-1\right|,
\]

and remains at its inherited mathematical floor `0 -> 0`.

## 2. Fresh source and primary-literature correction

I reopened the current primary source:

Remco van der Hofstad, *Stochastic processes on random graphs*, preliminary monograph dated 4 August 2026, Notes on Section 8.3, printed p. 245 / PDF p. 255.

The source still asks, in the finite-third-moment barely-supercritical configuration-model setting, whether the second-largest component has the expected Erdős--Rényi-type behavior and whether **“the discrete duality principle still hold[s]?”**

The key correction for this run is immediately earlier in the same source paragraph: van der Hofstad explicitly says that **both barely subcritical and barely supercritical regimes were already carefully analyzed by Riordan for uniformly bounded degrees**, and that the interesting phenomena motivating the open question arise when the degree support is not uniformly bounded.

I therefore reopened the primary bounded-degree reference:

Oliver Riordan, *The phase transition in the configuration model*, Combinatorics, Probability and Computing 21 (2012), 265--299, arXiv:1104.0613.

Riordan's Theorem 1.2 proves the sharp barely-subcritical largest-component law

\[
L_1
=\delta_n^{-1}\left(
\log\Lambda_n-\frac52\log\log\Lambda_n+O_p(1)
\right),
\qquad \Lambda_n=n\varepsilon_n^3,
\tag{2.1}
\]

and immediately after the theorem he states that the supercritical `L_2` bound is proved by applying Theorem 1.2 to what remains after deleting the largest component, with `c`, `delta_n` and `Lambda` defined for the **dual distribution**. Riordan also gives the leading form

\[
L_1=(2\mu_3/\mu_1+o_p(1))\varepsilon_n^{-2}\log\Lambda_n.
\tag{2.2}
\]

Thus the bounded-support special case selected in the preceding R14 stuck-recovery report is **KNOWN PRIOR ART**, not a fresh special case to prove. I did not spend this run rediscovering it.

A bounded fresh search through 19 September 2026 still found no later theorem closing van der Hofstad's stated finite-third-moment, potentially unbounded-degree question. This is bounded negative evidence only, not a worldwide novelty certificate.

## 3. B26 — HUNT THE SPORADIC CASE: the easy case is already solved

The previous recovery selected a bounded-support ideal-dual comparison as the simplest unproved special case. Riordan shows that this is the wrong target for two separate reasons.

First, the bounded-degree `L_2` / dual-distribution phenomenon is already part of the 2012 theory.

Second, the nondegenerate extreme scale is not a fixed multiple of `epsilon_n^{-2}`. Equation (2.1) shows the logarithmic location

\[
\delta_n^{-1}\left(\log(n\varepsilon_n^3)-\frac52\log\log(n\varepsilon_n^3)+O_p(1)\right).
\tag{3.1}
\]

Therefore a proposed point process cut merely at `a epsilon_n^{-2}` is not centered at the extreme window. If a stronger finite-third-moment distributional duality is attempted later, its normalization should be modeled on (3.1), not on a fixed `epsilon_n^{-2}` threshold.

**B26 outcome:** productive prior-art failure. The purported simple unproved case is known, and it reveals the correct extreme normalization.

## 4. B7 + B15 — a certified obstruction to iid extinction-thinned full duality

The previous recovery also proposed an ideal randomized residual profile with independent classwise thinning

\[
\widehat N_{n,d}\sim\operatorname{Bin}(n_d,z_n^d).
\]

I tested the strongest possible interpretation of that proxy before trying to use it. It fails dramatically as a **full marginal law**, already in Riordan's bounded-degree regime.

Let

\[
R_n=n-L_{1,n}
\]

be the number of vertices outside the actual giant. Let `z_n` be Riordan's extinction root and let

\[
\widehat R_n=\sum_i B_i,
\qquad B_i\sim\operatorname{Bernoulli}(z_n^{d_i})
\]

independently.

The means agree exactly:

\[
\mathbb E\widehat R_n=n(1-\rho_n).
\]

But Riordan's Theorem 1.1 gives

\[
\frac{L_{1,n}-\rho_n n}
{\sqrt{2\mu_{1,n}n/\varepsilon_n}}
\Longrightarrow N(0,1),
\tag{4.1}
\]

whereas

\[
\operatorname{Var}(\widehat R_n)
\le n\rho_n=O(n\varepsilon_n).
\tag{4.2}
\]

Thus actual residual-size fluctuations are of order `sqrt(n/epsilon_n)`, while independent-thinning fluctuations are only `sqrt(n epsilon_n)`.

Taking the window

\[
A_n=\{|x-n(1-\rho_n)|\le\sqrt n\},
\]

Chebyshev and (4.2) give

\[
\mathbb P(\widehat R_n\in A_n)\to1,
\]

while the CLT (4.1), since `sqrt(n)/sqrt(n/epsilon_n)=sqrt(epsilon_n)->0`, gives

\[
\mathbb P(R_n\in A_n)\to0.
\]

Hence

\[
\boxed{
 d_{\rm TV}(\mathcal L(R_n),\mathcal L(\widehat R_n))\to1.
}
\tag{4.3}
\]

The complete proof is archived in

`artifacts/R14/vdh_independent_extinction_thinning_tv_obstruction.md`

creation commit

`3d74964030ee7ae43bc2cef82ac63e183fa35bd4`.

This is an elementary consequence of published Riordan asymptotics; I make **no novelty claim** for the observation.

**B7 outcome:** taking the fluctuation limit exposes an order-`1/epsilon_n` standard-deviation mismatch that any full marginal ideal law must reproduce.

**B15 outcome:** deliberately separate two notions of duality. Conditional on the *realized* residual degree sequence, R14's previous theorem says the pairing law is asymptotically fresh. Marginalizing over that profile is a different problem, and a naive independent-thinning profile is false in total variation.

## 5. What the obstruction changes

The right hierarchy is now sharper.

### Level 1 — quenched pairing duality

Already obtained on the R14 route: after giant deletion, conditional on the realized residual degree sequence, the graph is asymptotically a fresh subcritical configuration model. The extra unique-largest conditioning vanishes in total variation by the R14 giant-scale susceptibility theorem.

### Level 2 — source-level extreme-component duality

This is what van der Hofstad's question actually needs at minimum. The inherited HARD7-04 proof chain gives the source-size candidate

\[
|C_{2,n}|
=(1+o_p(1))\frac{2R_*}{\varepsilon_n^2}
\log(n\varepsilon_n^3),
\tag{5.1}
\]

under the recorded stopping/collar reductions, while R14 supplies the literal fresh-pairing step.

At criticality the constant matches Riordan exactly. If `mu_r=E[(D)_r]`, then

\[
\mathbb E[D(D-2)^2]
=\mu_3-\mu_2+\mu_1
=\mu_3
\]

because criticality gives `mu_2=mu_1`; hence

\[
R_*=\mu_3/\mu_1,
\]

and `2R_*` agrees with Riordan's leading `2mu_3/mu_1` coefficient.

### Level 3 — full marginal profile duality

The simple iid extinction-thinning candidate is impossible by (4.3). A stronger marginal dual law would have to reproduce the giant-induced common fluctuations of the residual degree profile, not merely its first-order extinction tilt.

This is a **certified obstruction to an over-strong route**, not a refutation of the source statement.

## 6. New structural clue for a future stronger law

The mismatch in (4.3) points to a plausible missing latent variable. At a deterministic extinction time `t_*`, independent clock-survival noise has scale only `sqrt(n epsilon_n)`. A common random time perturbation `Delta t` changes total survivors at first order by approximately

\[
-n\mu_1\,\Delta t.
\]

To generate the actual `sqrt(n/epsilon_n)` giant/complement fluctuation scale, one needs

\[
\Delta t\asymp\frac1{\sqrt{n\varepsilon_n}}.
\tag{6.1}
\]

Thus if one ever seeks a stronger marginal dual profile, a **random-time mixture of extinction thinning**, not fixed-time iid thinning, is structurally plausible. This is a route diagnosis, not a proved approximation theorem.

## 7. Status and next Section-I action

The frozen metric remains `0 -> 0`; it cannot move below zero. This proof-capable run followed STUCK-RECOVERY-1/2 and changed the obstruction, but not the metric. Therefore the next invocation must be **STUCK-RECOVERY-2/2, THINKING-ONLY**, not another theorem/checker run.

That recovery should not retry bounded support or independent thinning. The fresh route is to ask whether the post-giant residual profile can be represented, for source-relevant extreme-component observables, by a **correlated random-time extinction tilt** whose common fluctuation is on the scale (6.1).

Fresh method triple for that recovery:

- **B10 DERANDOMIZE:** identify the minimal latent fluctuation needed so the ideal proxy matches the actual giant-size CLT rather than adding gratuitous iid profile randomness;
- **B13 FIND WHAT ONLY INCREASES:** use the monotone clock-survival profile `t -> (M_{n,d}(t))_d` to isolate which part of profile variation comes from the common stopping time;
- **B16 COMPUTE EVERY SMALL CASE:** on finite degree supports, write the covariance induced by a single random-time perturbation and compare it with the covariance structure implicit in Riordan's exploration CLT before attempting any unbounded-tail theorem.

If Recovery-2 does not produce a genuinely new path beyond the already source-matching leading `C_2` candidate and quenched duality, a later third stuck episode must terminally hand VDH off rather than manufacture more lemmas around the zero metric.

## 8. Capability / scheduler-control honesty

The exposed scheduler surface still has no binding model-family selector and no reasoning-effort selector. GPT-6/maximum remains prompt text only. This run actually identifies as GPT-5.6 Sol, with reasoning telemetry unavailable and therefore `UNVERIFIED`.

Changing that requires an authorized execution surface that exposes and persists those controls. Historical protected-task failures such as `You cannot modify this task` for P26 require the owning/admin-authorized context or platform support; there is no compliant permission bypass.

No scheduler, workflow, permission, email, Drive, public-posting, shared-root, or peer-track mutation was made.

## 9. Structured ledger delta

```yaml
ledger_delta:
  worker: R14
  lane: HARD_OUTSIDE
  source: VDH-8.3-DUALITY
  ownership: R14_EXCLUSIVE_UNCHANGED
  fixed_metric: "Delta_dual,n = |(1-nu_dual,n)/epsilon_n - 1|"
  fixed_metric_before: 0
  fixed_metric_after: 0
  movement: NO_MOVEMENT
  source_status: OPEN_PARTIAL
  run_kind: PROOF_CAPABLE_AFTER_STUCK_RECOVERY_1
  methods:
    - B7_TAKE_THE_LIMIT
    - B15_BREAK_THE_SYMMETRY
    - B26_HUNT_THE_SPORADIC_CASE
  new_certified_obstruction:
    statement: "in Riordan bounded-degree regime, TV(actual residual vertex count, iid extinction-thinned residual count) -> 1"
    implication: "iid extinction thinning cannot be the full marginal dual law"
    source_refuted: false
  prior_art_correction:
    bounded_degree_special_case: KNOWN_RIORDAN_2012
    exact_extreme_scale: "delta_n^{-1}(log Lambda - (5/2) log log Lambda + O_p(1))"
  preserved_source_candidate:
    C2_leading: "(1+o_p(1)) (2 R_*/epsilon_n^2) log(n epsilon_n^3)"
    quenched_fresh_pairing: true
    closure: false
    independent_audits_for_new_obstruction: 0
  next_run: STUCK_RECOVERY_2_OF_2_THINKING_ONLY
  next_methods:
    - B10
    - B13
    - B16
  artifact:
    path: artifacts/R14/vdh_independent_extinction_thinning_tv_obstruction.md
    creation_commit: 3d74964030ee7ae43bc2cef82ac63e183fa35bd4
```
