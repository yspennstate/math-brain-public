Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO ADMISSION MOVEMENT: `E_ready: 0 -> 0`; I0076 remains `OPEN / PARTIAL / RETIRED-HANDOFF` at `2/4`, and I0124 remains `PARTIAL / RETIRED-HANDOFF` with `H_288=112`. Methods #5 ADD A PARAMETER AND DIFFERENTIATE / TRACK IT, #19 MAKE IT AN ALGORITHM, #25 COUNT THE SAME THING TWICE.**

# R15 CLOSABLE OUTSIDE — successor admission: D0045 prior-art bridge and secretary ownership collision

Date checked: **2026-09-18 UTC**.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Own namespace only: `runs/R15/` and, if warranted, `artifacts/R15/`.

## 1. Continuity and exclusions recovered first

The native scheduler title is stale. Repository continuity controls.

- **I0076 / Burdzy–Scheutzow Problem 7.2** remains `OPEN / PARTIAL / RETIRED-HANDOFF` at the source-matching fixed metric `2/4`. I did **not** restart it. Its controlling handoff is `runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md`. The source hypothesis remains exactly: FBM + BBM and, at an arbitrary finite random time `T`, independence of the two *complete centered half-paths*. There is no deterministic-time substitution, no stopping/splitting-time assumption, and no separate assumption that either seam half is Brownian. Problem 7.5 and posted work remain excluded. The two previously frozen counterexample candidates were eliminated; there is currently no surviving frozen candidate on which it would be honest to score obligations 3 or 4.
- **I0124 / dimension-7 cap sets** remains `PARTIAL / RETIRED-HANDOFF`; the historical frozen quantity remains `H_288=112`, with the internal partial interval recorded in its handoff. I did not perform a seventh I0124 attack.
- The latest own R15 report is `runs/R15/20260918_0106Z_successor_admission_d0040_favard_q45e2c.md`, creation commit `6b1a77239a5522771810d0851585093ceed7b9d7`. It left R15 in `SUCCESSOR_ADMISSION_REQUIRED` with operational admission metric

  `E_ready := number of newly verified source-clean, current-open, ownership-clear, genuinely CLOSABLE OUTSIDE successors found in this bounded run`,

  at `0`.

Before attacking any candidate I reread/recovered the campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, the current operations implementation manifest, the latest own R15 report, current neighboring admission work, the relevant intake rows and canonical claims. Current coordinator/admission screens continue to show no free READY+CLOSABLE+UNASSIGNED target on their bounded fronts. This is a front-of-queue fact, not a theorem that none exists anywhere.

## 2. Material ownership update: the strongest new exact-value lead is already claimed

A recent sibling gate fully source-recovered a genuinely attractive recent CLOSABLE-shaped target:

**SOTO-VALDEVENITO-2026-SEC1OFF** — José A. Soto and Felipe Valdevenito, *Secretary Problems with Interactive Ordinal Queries*, arXiv:2609.19016v1 (2026), sample-based offline-adversarial order with one query (`SBOffAO1`).

The canonical claim now exists at

`operations/claims/SOTO-VALDEVENITO-2026-SEC1OFF.md`.

It assigns the target exclusively to native slot

`6aa7b46f70a8819184095c277974c256`.

The claim freezes the exact interval

\[
L_{\rm SEC1OFF}=1/e,\qquad
U_{\rm SEC1OFF}=\frac{20\sqrt{10}-29}{81},
\]

with gap metric `G_SEC1OFF = U-L` and preserves all source quantifiers. Therefore R15 **must not** duplicate, overwrite, or race that claim. This candidate would otherwise fit the CLOSABLE lane unusually well; its current ownership is decisive.

Disposition: **CLAIMED ELSEWHERE / NOT AVAILABLE TO R15**.

## 3. Idea before code: use Virág D0045 to test whether a broad source can be sharpened into a real short endpoint

I next screened **D0045**, Virág, *Operator limits of random matrices*, Question 7:

> relation between the `beta=2` random orthogonal polynomials of Section 4 and the deterministic ones; and what about the limiting operators?

The exact source wording is deliberately broad rather than a theorem predicate. The preceding R20 admission screen had already classified D0045 as requiring source/later-literature adjudication rather than calling it CLOSABLE. I therefore used the reserved Section-B moves to ask whether there is a sharp relation hiding inside it.

No code was written before the idea. In fact no checker is warranted in this run: the substantive identity below has a complete one-page analytic proof and, more importantly, turns out to be **known prior art**.

## 4. Move #5 — add/track the parameter beta: the mean monic random polynomial is deterministic

Virág's Section 4 nests the rescaled beta-Hermite matrices in one semi-infinite Jacobi matrix `J_beta`. In the normalization of that section, if `P_n^(beta)(x)` denotes the **monic characteristic polynomial** of the `n x n` leading minor of `J_beta`, then the Jacobi recurrence is

\[
P_{n+1}^{(\beta)}(x)
=(x-a_{n+1})P_n^{(\beta)}(x)-b_n^2P_{n-1}^{(\beta)}(x),
\]

where the new coefficients are independent of the previous minor, with

\[
\mathbf E a_{n+1}=0,
\qquad
b_n\stackrel d=\frac{\chi_{n\beta}}{\sqrt\beta},
\qquad
\mathbf E b_n^2=n.
\]

Set

\[
m_n^{(\beta)}(x)=\mathbf E P_n^{(\beta)}(x).
\]

Because `a_{n+1}` and `b_n` are independent of `P_n,P_{n-1}`, taking expectations gives exactly

\[
m_{n+1}^{(\beta)}(x)
=xm_n^{(\beta)}(x)-n\,m_{n-1}^{(\beta)}(x),
\qquad
m_0=1,\quad m_1=x.
\]

Hence

\[
\boxed{\mathbf E P_n^{(\beta)}(x)=\operatorname{He}_n(x)}
\]

for **every** `beta>0`, where `He_n` is the monic probabilists' Hermite polynomial, i.e. the deterministic orthogonal polynomial for the standard normal measure, the spectral measure of `J_infinity` in Virág's normalization.

So the finite-`n` first-moment relation is actually stronger than Question 7's special `beta=2` phrasing: after the source normalization it is beta-independent.

### Prior-art check: this is not new

A fresh literature search immediately found that this route is classical. Dumitriu–Edelman, *Matrix Models for Beta Ensembles*, J. Math. Phys. 43 (2002), Theorem 4.1, explicitly states that the expected beta-Hermite characteristic polynomial is the corresponding Hermite polynomial (in their normalization), and says the proof follows immediately from the same three-term recurrence and independence. Virág cites Dumitriu–Edelman as reference [17].

Therefore I record the identity as **KNOWN / PRIOR ART**, not a new R15 theorem. The useful conclusion is scope clarification: Virág's 2014 Question 7 cannot reasonably mean merely “identify the expected monic characteristic polynomial,” because that relation was already available in a paper cited by the source itself.

**Move #5 outcome:** productive scope clarification, but no new theorem and no admission movement.

## 5. Move #25 — count the same polynomial two ways: beta=2 Heine/Christoffel–Darboux makes the finite-n bridge even more explicit

At `beta=2`, the leading-minor eigenvalues form the Gaussian unitary/orthogonal-polynomial ensemble for the standard Gaussian weight in the source normalization. Thus the same first-moment identity can be obtained a second way from the classical Heine formula:

\[
\mathbf E\prod_{i=1}^n(x-\lambda_i)=\operatorname{He}_n(x).
\]

This is an honest second derivation of the same object: one count uses the independent Jacobi recurrence, the other uses the `beta=2` determinantal/orthogonal-polynomial eigenvalue density.

The same classical machinery gives a stronger finite-`n` two-point relation. If `P_n(x)=\det(xI-J_2^{(n)})` and `\pi_n=\operatorname{He}_n`, then

\[
\boxed{
\mathbf E[P_n(x)P_n(y)]
=
\frac{\pi_{n+1}(x)\pi_n(y)-\pi_n(x)\pi_{n+1}(y)}{x-y}
}
\]

(with the diagonal value obtained by continuity). Thus at `beta=2` not only the mean but also a basic two-point polynomial statistic is expressed entirely in deterministic Hermite data through the Christoffel–Darboux structure.

I do **not** claim novelty for this formula; products of characteristic polynomials in unitary/orthogonal-polynomial ensembles are classical. Its value here is interpretive: it makes the finite-`n` answer to “is there a relation?” already very rich, so the unresolved content of Question 7 must be a stronger structural/random-polynomial or limiting-operator relation, not merely an average identity.

**Move #25 outcome:** confirms, by an independent route, that the obvious finite-`n` bridge is classical and does not turn D0045 into a new source-closing target.

## 6. Move #19 — make it an algorithm: exact recurrence is easy; the source-level limiting relation is the hard part

The recurrence

\[
m_{n+1}=xm_n-nm_{n-1}
\]

is an exact linear-step symbolic algorithm for the mean monic random polynomial. More generally, independence lets one propagate finite collections of polynomial moments by augmenting the state with mixed moments such as `E[P_n(x)P_{n-1}(y)]`. At `beta=2`, determinantal identities already package these quantities much more efficiently.

This algorithmic viewpoint isolates why it does **not** close Virág's source question. The modern limiting characteristic-polynomial literature goes far beyond deterministic means:

- Lambert–Paquette (arXiv:2009.05003, 2020) prove that the edge-rescaled Gaussian beta-ensemble characteristic polynomial converges to the **stochastic Airy function**, a random entire solution of the stochastic Airy equation.
- Lambert–Paquette (arXiv:2508.01458, 2025) give a comprehensive bulk asymptotic description and obtain characteristic-polynomial ratios converging to the stochastic zeta function, with an order-one correction involving the stochastic Airy function.

Those are genuinely random limiting objects. An exact recurrence for the mean polynomial, or even classical beta=2 determinantal moment formulas, does not by itself identify a coupling or transformation between the random limiting operator/function and the deterministic Airy/Hermite operator. Passing the finite-`n` expectation identity to a limiting random entire function would additionally require the correct normalization and uniform-integrability/interchange control; I did not assume that step.

**Move #19 outcome:** the obvious algorithm closes only deterministic moments. The unresolved source-level content lies in the random object / limiting-operator relation.

## 7. Current-status verdict for D0045

Fresh source/current-literature queries on **2026-09-18 UTC** included:

- `"Operator limits of random matrices" "Question 7" Virag orthogonal polynomials`;
- `"random orthogonal polynomials" beta=2 deterministic orthogonal polynomials Virag`;
- `"expected characteristic polynomial" beta-Hermite Hermite polynomial`;
- `Gaussian beta ensemble characteristic polynomial stochastic Airy Lambert Paquette`;
- `Gaussian beta ensemble characteristic polynomial bulk Lambert Paquette 2025`.

Primary source checked: Virág's ICM 2014 article, Question 7 and Sections 2–4.  
Prior art checked: Dumitriu–Edelman 2002, Theorem 4.1.  
Later progress checked: Lambert–Paquette 2020 edge/stochastic-Airy work and 2025 bulk asymptotics.

Bounded search did **not** produce a single theorem whose statement cleanly says that Virág Question 7, including the limiting-operator clause, is fully resolved. Search failure is not an openness certificate. What is clear is that substantial exact finite-`n` and modern asymptotic relations already exist, while the source itself does not specify a yes/no predicate or one frozen constant.

Repository ownership check: direct fetch of `operations/claims/D0045.md` returned `404` at this run's current master, but absence of a claim is not enough for admission. Existing R20/P13 screening material already records D0045 as broad/scope-adjudication rather than clean CLOSABLE.

**Disposition:** `D0045 = PARTIALLY ANSWERED / BROAD SOURCE SCOPE / CURRENT-LITERATURE-RICH / NOT CLEAN CLOSABLE / NOT CLAIMED`.

This is more precise than simply calling it “open”: one obvious relation is a 2002 theorem, the beta=2 determinantal relation is classical, and the limiting characteristic-polynomial side has major 2020–2025 progress. The residual source obligation needs a sharper interpretation before it can be owned as a CLOSABLE theorem.

## 8. Admission result

No candidate passes all gates in this invocation.

- `SOTO-VALDEVENITO-2026-SEC1OFF` is genuinely CLOSABLE-shaped but now has an exclusive canonical owner.
- `D0045` is ownership-free at the checked path but fails the source-predicate/CLOSABLE gate after prior-art and later-literature reconciliation.
- I0076 and I0124 remain retired handoffs and are not recycled.

Therefore

\[
\boxed{E_{\rm ready}:0\longrightarrow0.}
\]

No canonical claim was created or overwritten. No source metric was invented. No finite checker was manufactured merely to certify a zero admission count.

## 9. What changed mathematically / operationally this run

The useful new R15 knowledge is not a source solution but a sharper literature and scope map:

1. the all-beta expected monic beta-Hermite characteristic polynomial relation follows immediately from the Jacobi recurrence in Virág's normalization;
2. Dumitriu–Edelman 2002 already proved the corresponding expected-characteristic-polynomial theorem, so this is **known prior art**, not an R15 result;
3. at beta=2, classical Heine/Christoffel–Darboux formulas express basic characteristic-polynomial moments in deterministic Hermite data;
4. later edge and bulk work identifies genuinely random stochastic-Airy / stochastic-zeta limits, showing where the remaining “limiting operators” content lives;
5. the strongest newly surfaced exact-value CLOSABLE lead, Soto–Valdevenito SBOffAO1, is already exclusively claimed elsewhere.

This prevents two bad dispatches: falsely claiming an old Hermite identity as new, and racing another worker for the secretary target.

## 10. Next research moves

R15 remains `SUCCESSOR_ADMISSION_REQUIRED`. The next pass should continue past the already screened Bradley/Virág rows unless there is a material source/status/ownership change. Prefer a literal source with one exact counterexample/construction, sharp finite constant, or short source-wide analytic theorem.

Reserved next Section-B triple: **#6 DEFORM TO A POINT YOU CAN SOLVE, #20 FIND WHY THE ALGORITHM FAILS, #28 REPLACE FOR ALL WITH FOR TYPICAL**.

These are not claimed as attacks on a source until a lawful successor passes admission.

## 11. Structured ledger_delta

```yaml
ledger_delta:
  worker: R15
  allocation: CLOSABLE_OUTSIDE
  run_status: SUCCESSOR_ADMISSION_REQUIRED
  continuity:
    I0076:
      status: OPEN_PARTIAL_RETIRED_HANDOFF
      metric_name: source_matching_obligations_for_one_frozen_candidate
      metric_value: 2/4
      active_research: false
    I0124:
      status: PARTIAL_RETIRED_HANDOFF
      metric_name: H_288
      metric_value: 112
      active_research: false
  admission_metric:
    name: E_ready
    before: 0
    after: 0
    movement: false
    unchanged_count: UNKNOWN
  methods_attempted: [5, 19, 25]
  screened:
    SOTO-VALDEVENITO-2026-SEC1OFF:
      disposition: CLAIMED_ELSEWHERE
      claim_path: operations/claims/SOTO-VALDEVENITO-2026-SEC1OFF.md
      owner_native_slot: 6aa7b46f70a8819184095c277974c256
      source_metric: G_SEC1OFF
      action: DO_NOT_DUPLICATE
    D0045:
      source: "B. Virag, Operator limits of random matrices, ICM 2014, Question 7"
      disposition: PARTIALLY_ANSWERED_BROAD_SCOPE_NOT_CLOSABLE_NOT_CLAIMED
      exact_internal_derivation: "E monic P_n^(beta) obeys Hermite recurrence in Virag normalization"
      prior_art: "Dumitriu-Edelman 2002 Theorem 4.1 already proves expected beta-Hermite characteristic polynomial is Hermite in its normalization"
      beta2_second_route: "classical Heine / Christoffel-Darboux characteristic-polynomial identities"
      later_progress:
        - "Lambert-Paquette arXiv:2009.05003 edge stochastic Airy function"
        - "Lambert-Paquette arXiv:2508.01458 bulk characteristic-polynomial asymptotics"
      claim_created: false
  remaining_obligation: "find a source-clean, current-open, ownership-clear, genuinely CLOSABLE OUTSIDE successor; do not invent a finite subproblem from a broad source"
  evidence:
    own_previous_report: runs/R15/20260918_0106Z_successor_admission_d0040_favard_q45e2c.md
    secretary_claim: operations/claims/SOTO-VALDEVENITO-2026-SEC1OFF.md
    D0045_intake: probability_1000_intake_D_20260908/problems.jsonl
    D0045_prior_screen: runs/R20/2026-09-17T21-58-30Z_successor_admission_screen_4f9c2d.md
  outside_audits: []
  checker: none
  reason_no_checker: "no new finite theorem; principal polynomial identity is analytically proved here and is known prior art"
  next_moves: [6, 20, 28]
  shared_roots_edited: false
  peer_files_edited: false
  email: false
  drive: false
  public_posting: false
  scheduler_modified: false
```

## 12. Model / scheduler control and historical P26 denial

The requested `GPT-6 / maximum` setting is still **not enforceable or attestable** from the exposed task surface. The actual model exposed to this run is **GPT-5.6 Sol**; reasoning effort is **UNVERIFIED**.

The available task controls expose title/prompt, schedule or relative-start information, timing mode, and enabled state. They do **not** expose a binding model-family selector, a reasoning-effort selector, authenticated applied-model telemetry, or a guaranteed hour-long execution field. Changing this requires an authorized product/workspace/backend/API surface that actually exposes persistent model + reasoning controls and runtime attestation; editing prompt text or GitHub cannot do it.

The historical P26 `You cannot modify this task` event remains an authorization-context boundary: a later authorized context did successfully update P26. If such a refusal recurs, the lawful workaround is the owning authorized account/workspace, supported admin/ownership reassignment, or platform support. Do not clone the task or bypass permissions.

No scheduler, permission, email, Drive, public posting, purchase, credential, or shared-root change was made.
