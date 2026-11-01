Model actually running: **GPT-5.6 Sol**. Reasoning level: **UNVERIFIED**. This was not GPT-6 at maximum. The exposed task-control surface still provides no binding model-family selector, no reasoning-effort selector, and no authenticated per-run model telemetry, so GPT-6/maximum remains prompt-requested only and I do not claim otherwise.

**P14 / G0007 — NO MOVEMENT: frozen successor metric `C_crit = 0 -> 0`. MANDATORY HARD HANDOFF.** Recovery cycles 1 and 2 have already been consumed on this target, so the current run does not start a third G0007 recovery. The predecessor Geoffrey Grimmett forest-negative-correlation target remains frozen at source-exact `n_source=9` and was not reopened.

# P14 G0007 mandatory handoff — contact-process critical percolation

Repository / branch: `yspennstate/math-open-problems` / `master`  
Native/root continuity: P14 / `proofnet24/P14-probability-correlation`  
Canonical claim being handed off: `operations/claims/G0007.md`  
Category: **HARD OUTSIDE**  
Status after handoff: **OPEN / PARTIAL / HARD HANDOFF COMPLETE**  
Frozen metric at handoff: `C_crit = 0/2`.

## 1. Source-exact target and fresh status check

Source: John Fernley and Emmanuel Jacob, *Percolation of the contact process on the regular tree*, arXiv:2609.09972v1, submitted 9 September 2026, Section 2 immediately before Figure 1.

For the upper invariant contact-process measure `nu_lambda` on the regular tree `T_d`, the source asks whether the probability that the root belongs to an infinite infected component is continuous at `lambda_p`, whether the analogous healthy-component probability is continuous at `lambda_{p^complement}`, and then whether the healthy probability has a continuous first derivative at its threshold while the infected probability fails to have a continuous first derivative at its threshold.

A fresh bounded 18 September 2026 local / 17 September UTC search for the exact title, arXiv id, continuity language, derivative language and threshold notation still recovered arXiv:2609.09972 as v1 and no later primary paper claiming a resolution of these exact questions. This is dated bounded search evidence, **not** a proof of worldwide openness or novelty.

The active metric is exactly

`C_crit = number of {lambda_p, lambda_{p^complement}} at which this track has proved absence of the corresponding infinite cluster at criticality.`

It remains `0/2`; structural restrictions do not count.

## 2. The exact blocker at handoff

The first G0007 report proved finite-cylinder continuity in `lambda`, right-continuity of the infected percolation probability and left-continuity of the healthy percolation probability. Therefore the zeroth-order source question has been reduced exactly to

\[
\boxed{
\Theta_I(\lambda_p)=0,
\qquad
\Theta_H(\lambda_{p^\complement})=0.
}
\tag{2.1}
\]

Here `Theta_I(lambda)` and `Theta_H(lambda)` are the probabilities that the root lies in an infinite infected or healthy component, respectively.

The first unresolved clause is still

\[
\boxed{\Theta_I(\lambda_p)=0.}
\tag{2.2}
\]

The derivative question remains downstream and was deliberately not substituted for the critical-nonpercolation problem.

## 3. Preserved theorem chain

The following G0007 results are preserved and should be treated as inherited lemmas by any future owner.

### 3.1 Critical-nonpercolation reduction

`G0007-CRITICAL-NONPERCOLATION-REDUCTION-01`:
using Huang's continuity of the contact-process survival probability on periodic trees, self-duality, additivity and finite-cylinder continuity,

- `Theta_I` is right-continuous;
- `Theta_H` is left-continuous;
- source continuity at the two thresholds is equivalent to the two zero statements in (2.1).

This is theorem-level reduction but no `C_crit` credit.

### 3.2 Geodesic persistence exponent restriction

For a length-`n` geodesic segment let

\[
q_n^I(\lambda)=\nu_\lambda(\hbox{all segment vertices infected}),
\qquad
q_n^H(\lambda)=\nu_\lambda(\hbox{all segment vertices healthy}).
\]

Association gives supermultiplicativity and hence limits

\[
\alpha_I(\lambda)=\lim_n(q_n^I)^{1/n},
\qquad
\alpha_H(\lambda)=\lim_n(q_n^H)^{1/n}.
\]

The inherited first-moment implication is

\[
(d-1)\alpha_I(\lambda)<1\Longrightarrow \Theta_I(\lambda)=0,
\]

with the corresponding healthy statement. Conversely a positive infected percolation probability forces `alpha_I >= 1/(d-1)`. The missing reverse direction for the dependent upper invariant field was not proved.

### 3.3 Critical cluster end structure

The strongest structural theorem of recovery 2 is `G0007-CRITICAL-ENDS-03-I`. Fernley--Jacob's invariant-tree mass-transport identity and exact conditional mean-degree formula, combined with weak convergence from below and Portmanteau on finite-component centroid events, give

\[
\boxed{
\widetilde{\mathbb E}_{\lambda_p}
[(D_o^\infty-2)_+]=0.
}
\tag{3.1}
\]

Therefore every infinite infected component at `lambda_p`, if any exists, has at most two topological ends almost surely.

Applying the same invariant-site-percolation identity to the complement and using the exact healthy conditional mean-degree formula gives

\[
\boxed{
\widehat{\mathbb E}_{\lambda_{p^\complement}}
[(D_o^{H,\infty}-2)_+]=0,
}
\tag{3.2}
\]

so every infinite healthy component at its source threshold, if any exists, also has at most two ends.

These are structural restrictions only. They do **not** prove either critical cluster is absent and therefore do not move `C_crit`.

## 4. Route inventory and precise failure reasons

This is the required handoff inventory. Future reassignment should not repeat these routes without a new ingredient.

1. **FKG / finite-size criterion.** The intake attempt `G0007-A001` reaches the familiar increasing-event inequalities but has no finite-range or exponential-decoupling estimate for `nu_lambda` near the source threshold. FKG points in the wrong direction for the missing quasi-independence.

2. **Finite-dimensional continuity / self-duality.** Successful as reduction 01, but it gives only local convergence in the parameter. It cannot turn a critical infinite cluster into a lower-rate infinite cluster.

3. **Naive branch/cavity factorization.** False after conditioning on a common root event. Even two independent Bernoulli branch messages become negatively correlated after conditioning on their OR. Primitive Harris marks may still support a cavity approach, but final-state subtree independence is unavailable.

4. **Static geodesic first moment.** The persistence exponent gives the easy implication `(d-1) alpha < 1 => no percolation`; the critical equality/boundary case is exactly where the method stops.

5. **Finite-time OSSS/sharpness transfer.** Finite-time Harris configurations live on a product space, but the upper invariant time slice requires an unbounded backward dependency cluster. No revealment/pivotal estimate uniform in both spatial radius and backward time was obtained. Beekenkamp's old arXiv sharpness manuscript is withdrawn; his dissertation records essentially this stationary-limit obstruction.

6. **Bernoulli critical-nonpercolation import.** BLPS/Hutchcroft mechanisms use independent percolation structure not established for `nu_lambda`. Nonamenability alone is not enough to import those proofs.

7. **Invariant-cluster encounter points.** Haggstrom-type symmetry implies a putative critical phase cannot be a unique infinite cluster, but recovery 2 proves the stronger obstruction that critical infinite clusters, if present, have at most two ends. Hence trifurcation/encounter-point transports have empty support at the endpoint.

8. **Insertion tolerance / finite energy.** Not verified for the upper invariant measure on `T_d`; the source itself flags the relevant Haggstrom condition as difficult. It cannot be assumed as a surgery tool.

9. **Broman--Steif downward movability.** This gives a genuine parameter/thinning comparison but in a stochastic-order direction insufficient to infer lower-rate percolation from critical higher-rate percolation.

10. **Direct Harris perturbation.** For each finite set `K`, the monotone coupling gives a useful local estimate of the form

\[
\mathbb P(X_{\lambda_p}|_K\ne X_{\lambda_p-\delta}|_K)
\le |K|\,[\rho(\lambda_p)-\rho(\lambda_p-\delta)].
\]

Continuity therefore supplies `for every radius n there exists delta_n`. To contradict the definition of `lambda_p` one needs one `delta>0` working at arbitrarily large scales: `there exists delta for every n`. This quantifier swap is the exact unresolved perturbative gap.

11. **Mass transport alone.** It successfully kills branching surplus at the critical endpoints, but it does not exclude one-ended or two-ended infinite clusters. This is now the sharp residual geometric obstruction.

## 5. What a future proof must contain

Any successful continuation must add a mechanism absent from every route above. Two concrete possibilities survive:

- **Thin-cluster exclusion:** prove that under the upper invariant contact-process measure on `T_d`, an invariant infinite infected (respectively healthy) component cannot be one-ended or two-ended at the corresponding endpoint, using a contact-process-specific property that is actually verified rather than assumed.

- **Uniform parameter bridge:** prove a scale-uniform perturbation theorem in the common Harris coupling strong enough to turn any hypothetical endpoint infinite cluster into positive connection probability below the defining threshold. The needed order of quantifiers is one fixed parameter decrement working on all scales.

A future owner should attack one of these statements directly rather than reproduce FKG, generic association, static branch factorization, or an encounter-point argument.

## 6. Simplest source-aligned special case still open

The cleanest recovery laboratory remains the infected endpoint on `T_7`:

\[
\Theta_I^{T_7}(\lambda_p)=0.
\]

Fernley--Jacob already establish the full ordering of the four relevant thresholds for `d>=7`, so this case avoids low-degree ambiguity in threshold ordering while retaining the stationary critical-slice obstruction. It remains unproved in this track.

## 7. Nearest solved mechanisms and what they possess that G0007 lacks

- Bernoulli critical nonpercolation on nonamenable/unimodular graphs has independent perturbation structure that supports thinning/surgery and mass transport.
- Huang's continuity theorem for survival on periodic trees uses a robust space-time branching structure for survival, not a stationary same-time infected cluster.
- Fernley--Jacob's own mass-transport formulas give exact endpoint degree information but intentionally stop at the one-/two-ended possibility.

The missing ingredient is therefore not another endpoint mean-degree identity; it is a verified way to rule out thin invariant infinite components or to make critical connectivity robust under a single downward parameter perturbation.

## 8. New-method accounting for this mandatory-handoff run

The immediately preceding recovery used #11, #20 and #27. This run did not begin a prohibited third recovery. Its three methods were used for handoff/rotation rather than for new G0007 claims:

- **#22 READ THE FAILURES, NOT THE SUCCESSES:** consolidated every G0007 route above into the two missing mechanisms in Section 5.
- **#21 ASK WHO ELSE HAS THIS SHAPE:** checked the next visible queue candidate I0115 against the later Poisson-line SIRSN literature before claiming it.
- **#26 HUNT THE SPORADIC CASE:** tested whether an explicit small-`k` finite-subnetwork law for a known Poisson-line SIRSN could make I0115 a source-matching successor. It cannot: that would create a narrower new problem rather than decide Aldous's qualitative Open Problem 27.

No new G0007 checker or theorem was created, in accordance with the third-stuck rotation rule.

## 9. Successor screen: I0115 is not a lawful immediate claim

The next visible unclaimed HARD-style queue candidate tested was `I0115`, David Aldous, *Scale-invariant random spatial networks*, Open Problem 27. Direct source recovery gives:

> Give a construction of a SIRSN which is “mathematically natural” in some sense, for example one with an explicit formula for the distribution of finite spanning subnetworks `span(z_1,...,z_k)`.

The source PDF page containing Open Problem 27 was located directly. The PDF screenshot service was invoked as required for PDF analysis but returned an internal fetch error; the parsed primary text was available and was cross-checked against the existing R08 source screen.

This candidate is **not** safe to claim. Kahn's 2016 improper Poisson-line construction and Kendall's related Poisson-line metric work already provide a mathematically natural SIRSN in a plausible reading of the source's qualitative first phrase. A bounded search did not recover a general explicit law of arbitrary finite subnetworks, but the source says “natural in some sense, e.g.” and supplies no objective closure criterion. The prior R08 admission report independently classified I0115 as `HOLD_SOURCE_SCOPE_AMBIGUOUS_AFTER_POISSON_LINE_CONSTRUCTION / NOT_CLOSABLE_READY` and deliberately created no claim.

I therefore did not create `operations/claims/I0115.md` and did not invent a small-`k` metric. Nearby queue candidates checked during the bounded rotation pass are already canonically occupied or held: I0075, I0012, I0027, RS-2026-DC34, RS-2026-DC35, RS-2026-CL-A and RS-2026-CL-B have current claim files; I0074 has repeated current scope-hold reports rather than a clean source admission.

Result: **P14 successor admission required.** A lawful successor was not established in this bounded pass, so the recurring native task should stop rather than emit another admission-only or third-recovery report.

## 10. Directed P15 second-audit duty

The newest P15 report recovered is

`proofnet24/P15-closure-discrepancy/runs/2026-09-17/2026-09-17T18-24-54Z__successor-admission-hold.md`.

It explicitly states that it is an admission/status run, not a theorem run, and introduces no new P15 checker or mathematical claim. Therefore P14 issues **no duplicate audit PASS**. The directed duty remains pending for the next genuinely new P15 mathematical claim.

## 11. Runtime-control status

The exposed task interface still has fields for title/prompt/schedule/enabled/timing behavior but no writable or authenticated `model` or `reasoning_effort` selector. GPT-6/maximum therefore remains only requested in prompt text. Making it binding would require a product/backend or authorized account-management surface that exposes those controls plus applied-run telemetry.

The historical P26 message `You cannot modify this task` was an authorization-context boundary; later modification succeeded from an authorized context. The lawful remedy if such a denial recurs is owner/admin/product authorization, not a duplicate schedule or permission bypass.

## 12. ledger_delta for P26

```yaml
track: P14
category: HARD_OUTSIDE
predecessor_frozen:
  target: Geoffrey Grimmett Conjecture 4.2
  metric_name: n_source
  value: 9
  status: OPEN_PARTIAL_HANDOFF
handed_off_target:
  id: G0007
  source: Fernley-Jacob arXiv:2609.09972v1
  metric_name: C_crit
  before: 0/2
  after: 0/2
  movement: NO_MOVEMENT
  status: OPEN_PARTIAL_HARD_HANDOFF_COMPLETE
  hard_recovery_cycles_consumed: 2
  third_recovery_permitted: false
preserved_claims:
  - G0007-CRITICAL-NONPERCOLATION-REDUCTION-01
  - geodesic_persistence_exponent_restriction
  - G0007-CRITICAL-ENDS-03-I
  - healthy_critical_at_most_two_ends
remaining_source_obligations:
  - Theta_I(lambda_p)=0
  - Theta_H(lambda_p_complement)=0
  - derivative_contrast_after_continuity
successor_screen:
  I0115: HOLD_SOURCE_SCOPE_AMBIGUOUS_AFTER_POISSON_LINE_CONSTRUCTION
  new_claim_created: false
  state: SUCCESSOR_ADMISSION_REQUIRED
p15_second_audit:
  newest_report_is_status_only: true
  new_claim_found: false
  duplicate_audit_issued: false
model_selector_available: false
reasoning_selector_available: false
authenticated_runtime_model_telemetry: false
```

**END OF REPORT**
