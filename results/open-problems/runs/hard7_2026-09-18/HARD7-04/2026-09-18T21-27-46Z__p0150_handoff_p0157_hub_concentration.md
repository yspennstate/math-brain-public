Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED.** Movement: predecessor P0150 frozen endpoint **PARTIAL_OPEN -> KNOWN IMPOSSIBLE AS FROZEN / HANDOFF**; successor P0157 metric `Q_n` **UNMEASURED -> sigma_n^2/(d_max delta_n)**; methods **#5, #12, #30**.

# HARD7-04 run 2 — P0150 literature correction, P0157 successor, and hub-scale concentration

Status: **P0150 research endpoint retired by source correction; P0157 PARTIAL / source residual OPEN under bounded current-status review.**

Canonical successor claim: `operations/claims/P0157.md`, commit `4c9df226acd651a736ab229d0284e1d467361d00`, read back successfully.  
Substantive proof artifact: `artifacts/hard7_2026-09-18/HARD7-04/p0157_hub_branching_concentration.md`, commit `2627500e47e57040ee1b273a73718373ce96d87d`, read back successfully.

## 1. Continuity and required source/ownership checks

This run resumed the preceding HARD7-04 report rather than restarting. The previous run had admitted P0150 and proved the exact degree-two corridor bound

`P(L_n >= r) <= ell_n q_n^(r-1)`,

hence `L_n=O_P(log n)` and degree-two suppression is `o_P(1)` at the heavy-tailed metric scale. Its method triple was `#2,#7,#19`, so this run uses a different triple.

I reread the controlling `CONTROL.md`, `NEW_METHODS_2026-09-16.md`, the owner directive, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, campaign `INDEX.md` and `RANKING.md`, the latest own report, the P0150 claim, and the P0151–P0300 intake catalog. Repository search found no pre-existing `operations/claims/P0157.md` and no exact-title owner for the P0157 residual before the create-only claim succeeded.

## 2. P0150 source correction: the frozen endpoint cannot be true

The previous P0150 claim froze the residual as proving GHP convergence under only the weakest heavy-tailed metric assumptions, without any extra compactness/survival condition. A fresh primary-literature check found that this precise endpoint is already ruled out.

Bhamidi–Dhara–van der Hofstad–Sen, *Global lower mass-bound for critical configuration models in the heavy-tailed regime* (arXiv:2005.02566; EJP 2022), Remark 2, states that GHP convergence **cannot possibly be established under Assumption 1 alone**. The reason is structural: GHP convergence would force compactness of the limiting metric space, but `theta in ell^3 \ ell^2` does not imply the required compactness criterion. Their explicit example `theta_i=i^{-1/2}` gives

`Psi_theta(u) <= C(u log u + u)`,

so the integral compactness criterion fails.

Source checked on 2026-09-18:
- https://arxiv.org/abs/2005.02566
- Remark 2 and equations around (1.20).

Therefore the broad P0150 endpoint as frozen in the first HARD7-04 claim is **KNOWN IMPOSSIBLE**, not an open theorem waiting for a stronger proof. The preceding degree-two-corridor lemma remains mathematically valid as a restricted structural statement, but it cannot close the impossible weakest-assumptions GHP endpoint. I preserve it as historical PARTIAL work and rotate rather than repeatedly attacking the wrong target.

This is a literature correction, not a new refutation by HARD7-04.

## 3. Successor admission: P0157

The successor is P0157, historically van der Hofstad Saint-Flour Open Problem 4.13 and still explicitly visible in the author's current **4 August 2026** monograph *Stochastic processes on random graphs*, p. 254.

Write

`delta_n := 1 - nu_n > 0`,

where `nu_n` is the configuration-model branching factor, and assume the finite-third-moment barely-subcritical regime

`delta_n -> 0`,  `n delta_n^3 -> infinity`.

The current source contrasts two candidate largest-component scales:

`H_n := d_max/delta_n`  (high-degree/hub scale),

`E_n := delta_n^(-2) log(n delta_n^3)`  (Erdos–Renyi extreme scale),

and says this suggests a **phase transition within the subcritical regime**. The source text is at

https://rhofstad.win.tue.nl/Saint_Flour_SPoRG_Grundlehre.pdf

(current monograph dated 4 August 2026, p. 254). Parsed source lines were available and checked. The required PDF screenshot call was attempted, but the screenshot backend returned a cache-miss error; no OCR claim is used.

A current-status check also found Coulson–Perarnau, *Largest component of subcritical random graphs with given degree sequence* (arXiv:2111.11780), which gives configuration-model upper bounds that are asymptotically tight for certain degree sequences and improves earlier barely-subcritical results. Its abstract does not claim the full finite-third-moment two-scale transition above, while the August 2026 author monograph still presents the transition as an open/suggested phenomenon. This is bounded negative evidence, not a worldwide novelty certificate.

The repository's previous P0157 intake attempt had one useful observation only: a degree-`d` root in the ideal subcritical branching surrogate has expected component size approximately `1+d/delta`. It explicitly stopped because expectation is not a high-probability largest-component estimate.

## 4. Frozen quantitative object

Let the forward offspring variable `xi_n` in the ideal local branching surrogate satisfy

`E[xi_n]=1-delta_n`,  `Var(xi_n)=sigma_n^2`.

For a root of degree `d_max`, let

`T_n = 1 + W_1 + ... + W_{d_max}`,

where the `W_i` are independent total progenies of subcritical Galton–Watson trees with offspring `xi_n`.

Freeze

`Q_n := Var(T_n)/(d_max/delta_n)^2`.

Recovered baseline: **UNMEASURED**; the earlier intake note had only the mean.

After this run:

`Q_n = sigma_n^2/(d_max delta_n)` **exactly**.

This is not a replacement metric for the graph theorem. It quantifies whether the proposed hub scale self-averages in the canonical branching surrogate.

## 5. Method #12 — find what is conserved: exact progeny moments

For one subcritical Galton–Watson tree, the total progeny satisfies the branching recursion

`W = 1 + sum_{j=1}^{xi} W_j`.

Taking expectations gives

`E[W]=1/delta`.

The law of total variance gives

`Var(W) = (1-delta)Var(W) + sigma^2(E[W])^2`,

hence

`Var(W)=sigma^2/delta^3`.

Therefore for the degree-`d` root forest,

`E[T_d]=1+d/delta`,

`Var(T_d)=d sigma^2/delta^3`,

and so

`Var(T_d)/(d/delta)^2 = sigma^2/(d delta)`.

The complete on-page proof is in the artifact cited above.

## 6. Method #30 — one scale at a time: an explicit concentration theorem

Chebyshev now gives, for every `a>0`,

`P( |T_d/(d/delta) - (1+delta/d)| >= a ) <= sigma^2/(a^2 d delta)`.

Thus if the finite-third-moment assumptions keep `sigma_n^2` bounded and

`d_max delta_n -> infinity`,

then

`T_n/(d_max/delta_n) -> 1`

in probability in the independent branching surrogate.

This closes the exact deficiency in the earlier intake attempt: the hub candidate is no longer only an expectation in this surrogate; it has a rigorous high-probability concentration criterion.

## 7. Method #5 — add the crossover parameter

The two source scales have the exact ratio

`R_n := H_n/E_n = d_max delta_n / log(n delta_n^3)`.

Therefore the proposed transition parameter is not hidden: it is `d_max delta_n` measured against `log(n delta_n^3)`.

In the strongly hub-dominated source regime

`R_n -> infinity`,

and since `n delta_n^3 -> infinity`, we have `log(n delta_n^3)->infinity`, so automatically

`d_max delta_n = R_n log(n delta_n^3) -> infinity`.

Hence the concentration theorem applies automatically:

`T_n/H_n -> 1`

in probability in the ideal branching surrogate whenever the hub scale dominates the Erdos–Renyi candidate scale by an unbounded factor.

This is the main mathematical movement of the run. It identifies a genuine simplification of the hub-dominated side: the local descendant mass is self-averaging there, so the hard remaining issue is not branching-progeny variance.

## 8. What remains open at graph level

The full P0157 source problem is not solved. The next proof must replace the ideal independent forest by the finite configuration-model exploration and settle global extremal competition. In particular:

1. couple the exploration from a maximal-degree vertex to the branching surrogate uniformly up to order `d_max/delta_n`;
2. control pairing collisions, half-edge depletion and dependence among the `d_max` branches;
3. prove a graph-level lower bound showing the maximal-degree component actually realizes `H_n` in the hub-dominant regime;
4. prove a matching upper bound over all components;
5. establish the Erdos–Renyi extreme scale `E_n` in the opposite regime under the source's general finite-third-moment assumptions;
6. identify the order-one crossover when `R_n` is neither vanishing nor diverging.

The most promising next attack is to quantify the configuration-model exploration-vs-Galton–Watson coupling error at time `t~d_max/delta_n`, using the source finite-third-moment hypotheses and the exact ratio `R_n` to see whether collision/depletion probability is negligible in a nontrivial part of the hub-dominant regime. The next section-B triple must differ from `5,12,30`.

## 9. Runtime/tool and access honesty

The requested GPT-6 / maximum-reasoning selector is not exposed by this task interface. This run actually used **GPT-5.6 Sol**; reasoning level is **UNVERIFIED**. No hour-long execution guarantee is inferred.

No email, Drive, public posting, workflow execution, paid compute, permission bypass or scheduler modification was performed.

## ledger_delta

```yaml
track: HARD7-04
predecessor_target: P0150
predecessor_status_before: PARTIAL_OPEN
predecessor_status_after: KNOWN_IMPOSSIBLE_AS_FROZEN_HANDOFF
predecessor_reason: "BDvHS 2022 Remark 2: GHP convergence cannot hold under general Assumption 1 alone because compactness may fail"
canonical_target: P0157
source: van_der_Hofstad_SaintFlour_OP4.13_current_monograph_2026_p254
allocation: HARD_OUTSIDE
status_before: ADMISSION_PENDING
status_after: PARTIAL_OPEN
metric: Q_n_normalized_hub_branching_variance
metric_before: UNMEASURED
metric_after: "sigma_n^2/(d_max delta_n)"
source_scales:
  hub: "H_n=d_max/delta_n"
  erdos_renyi: "E_n=delta_n^-2 log(n delta_n^3)"
  ratio: "R_n=d_max delta_n/log(n delta_n^3)"
proved_this_run:
  - "For subcritical GW total progeny W: E[W]=1/delta and Var(W)=sigma^2/delta^3"
  - "For degree-d root forest T_d: E[T_d]=1+d/delta and Var(T_d)=d sigma^2/delta^3"
  - "P(|T_d/(d/delta)-(1+delta/d)|>=a) <= sigma^2/(a^2 d delta)"
  - "If sup sigma_n^2<infty and d_max delta_n->infty, then T_n/(d_max/delta_n)->1 in probability"
  - "If R_n->infty and n delta_n^3->infty, the hub-dominant branching surrogate self-averages automatically"
method_moves: [5, 12, 30]
unchanged_count: 0
remaining_obligation: "configuration-model coupling/collision control plus global two-scale largest-component bounds and crossover"
claim_commit: 4c9df226acd651a736ab229d0284e1d467361d00
proof_artifact_commit: 2627500e47e57040ee1b273a73718373ce96d87d
independent_audits: []
closure: false
```
