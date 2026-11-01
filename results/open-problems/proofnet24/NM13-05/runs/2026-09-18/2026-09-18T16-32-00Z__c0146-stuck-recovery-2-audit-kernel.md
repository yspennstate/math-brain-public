Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FROZEN-METRIC MOVEMENT: `m_cert = 9 -> 9`; mandatory Section-I STUCK RECOVERY 2; Section-B methods actually tried: #12 FIND WHAT IS CONSERVED, #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE, #23 DO WHAT THE PROPOSER DID NOT EXPECT. Source status remains REFUTED; fleet closure remains PENDING P26 + NM13-06.**

# NM13-05 / C0146 — stuck recovery 2: freeze the audit kernel, test exact-number prior art, and explain why the q>=1 coupling cannot port

Run date: 2026-09-18 UTC  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Track / namespace: `proofnet24/NM13-05/`  
Category: **CLOSABLE OUTSIDE**  
Canonical source / claim: **C0146**, `operations/claims/C0146.md`  
Canonical dedup key: `fk_q_less_than_1_monotone_coupling`  
SHA-256: `dd817e3ec8169668456ed767e35982573675498dec1367239155a22daa3f4ec6`  
Selection residue: `4 mod 13`  
Frozen metric: `m_cert`  
Metric before / after: **9 -> 9**  
Source mathematical status before / after: **REFUTED -> REFUTED**  
Unchanged-run counter: **4 -> 5**  
Stuck-recovery counter: **1 -> 2**  
Required closure auditors: **P26 and NM13-06; neither has a C0146 PASS recovered in this invocation**

## 1. Runtime and control-plane disclosure

The prompt requests GPT-6 with maximum reasoning. This invocation actually identifies as **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6, a binding maximum-reasoning setting, a guaranteed hour-long execution, or a support escalation.

The task-control surface still exposes title/prompt, schedule or relative-start controls, timing mode, enabled state, and task identity, but **no bindable model-family selector and no bindable reasoning-effort selector**. `GPT-6 / maximum` is therefore prompt text only. Making it binding would require an owner-authorized product/workspace/API/admin surface exposing persistent model and effort controls together with authenticated per-run runtime attestation.

The historical P26 response `You cannot modify this task` is an authorization-context boundary, not a release or a mathematical state. Repository continuity records a later successful P26 update from another authorized context. The lawful workaround for any future refusal is the owning/otherwise-authorized context or authorized platform/admin support for that same task, never duplication, permission bypass, or a repository edit represented as scheduler repair. I did not create, modify, disable, or probe a schedule in this invocation.

## 2. Authoritative continuity and repository delta

This is **not a new admission**. C0146 remains exclusively owned by NM13-05, so I did not reopen selection or create another claim.

The controlling predecessor is

`proofnet24/NM13-05/runs/2026-09-18/2026-09-18T15-31-00Z__c0146-stuck-recovery-1-audit-priorart.md`,

creation commit `f7e77fb4a9190023dc30c0dad8894fbfb6d61bcd`. It left `m_cert=9`, `unchanged_runs=4`, `stuck_recoveries=1`, and made the remaining obligation the two independent audits.

Before this recovery I reread or exact-target-recovered current `master` state for:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- `operations/claims/C0146.md`;
- the newest own report, newest designated-auditor NM13-06 report, latest P26 audit report, current C0146/PASS searches, historical C0146 attempt identity, and the exact Git comparison from the predecessor commit to `master`.

Large append-only intake JSONL files are connector-bounded when rendered wholesale. I relied on the canonical C0146 claim, targeted canonical-key/attempt searches, current ledgers, immutable reports, and the exact changed-file comparison; truncated output is not treated as a release or permission to restart.

At the final pre-write comparison, `master` was **83 commits ahead and 0 behind** the predecessor creation commit. The changed-file set contains no edit to `operations/claims/C0146.md`, no C0146 handoff/release, and no C0146 audit/PASS from P26 or NM13-06. The newest NM13-06 report is still a post-P0195 admission screen and explicitly treats C0146 as NM13-05-owned with its audit gate pending. The latest P26 report audits a P04 claim, not C0146. Root `QUEUE.md`, `POSTED.md`, `RESULTS.md`, campaign `INDEX.md`/`RANKING.md`, and the controlling owner-policy files do not appear in this predecessor-to-head changed-file set.

Therefore the authoritative continuity is unchanged: **C0146 stays REFUTED but not fleet-CLOSED**.

## 3. Frozen source statement and exact witness kernel

The live source is Gábor Pete, *Probability and Geometry on Groups*, PDF dated **April 3, 2024**, `https://math.bme.hu/~gabor/PGG.pdf`. The current PDF still prints Question 13.2 asking whether the `FK(p,q)` laws admit a monotone coupling in `p` for every `q in [0,1)`.

The source-facing refutation needs only the following fixed finite tuple, already exactly certified in prior NM13-05 runs:

\[
G:\ E=\{01,02,03,04,05,12,13,14,16,56\},\qquad e_*=01,
\]
\[
q=\frac1{40000},\qquad p_1=\frac1{2001}<p_2=\frac1{1601},\qquad A=\{e_*\text{ open}\}.
\]

The exact event probabilities are

\[
\phi_{p_1,q}(A)=\frac{72488985858351}{205113593435351},
\qquad
\phi_{p_2,q}(A)=\frac{108671022567040625}{307499119349131441},
\]

and

\[
\phi_{p_1,q}(A)-\phi_{p_2,q}(A)
=
\frac{395372934751065824378379416}
{63072249347906220400541234970791}>0.
\]

Because `A` is increasing, this single strict reversal disproves stochastic domination from `p1` to `p2`, hence disproves a monotone grand coupling for that fixed `q`, hence refutes the source statement as written.

No stronger fixed-graph threshold, nine-edge classification, or ten-edge minimality theorem is needed for that logical implication.

## 4. Exact Section-I blocking statement

The current blocker is not a missing mathematical lemma. It is the closure protocol:

\[
\boxed{
\operatorname{Close}(\mathrm{C0146})
\Longleftrightarrow
\operatorname{PASS}_{\mathrm{P26}}(\mathrm{C0146})
\wedge
\operatorname{PASS}_{\mathrm{NM13\text{-}06}}(\mathrm{C0146})
}
\]

with the already-present source-facing argument, exact finite certificate, and bounded prior-art record as the package to audit.

Neither conjunct can be manufactured by NM13-05. A same-track checker is a self-check; another same-track theorem is not an independent audit.

## 5. Required stuck inventory: routes tried and why they no longer move the blocker

The route history is now complete enough to state compactly.

- **#2/#8/#11** attacked the negation, discretized fixed layers, and dualized transport; `m_cert` moved `UNMEASURED -> 5`.
- **#14/#16/#25** used symmetry, exhaustive small cases, and double counting; `m_cert` moved `5 -> 8`.
- **#1/#20/#19** translated to graphic-matroid structure, diagnosed the naive deletion-kernel failure, and built exact Bernstein transport; `m_cert` moved `8 -> 9`.
- **#30/#10/#3** localized at the forest boundary, derandomized the obstruction, and converted it to the exact positive-`q` witness above; the source became **REFUTED**.
- **#5/#22/#24** sharpened the positive-`q` interval and recovered the Halberstam/Poudevigne prior-art warning.
- **#18/#6/#29** classified the distinguished-edge nonmonotonicity threshold on the fixed witness by exact elimination/Sturm analysis.
- **#15/#26/#4** proved every 10-edge simple graph on at most six non-isolated vertices is monotone, making seven vertices sharp among 10-edge simple counterexamples.
- **stuck recovery 1, #7/#21/#27** reconciled the arboreal-gas limit, neighboring literature, and the minimal source-level audit obligation.

All of those routes either moved the metric before the refutation or sharpened the already-refuted source. None can supply independent authorship for P26 or NM13-06.

### What a closure proof must contain that no same-track route contains

It must contain **two independent recomputations/reviews by other tracks** that accept the source-level implication and exact finite witness. Independence, not additional algebra, is the missing ingredient.

### Simplest special case still unproved

There is no mathematical special case of Pete Question 13.2 that still needs to be proved in order to refute the universal statement. The smallest unresolved protocol case is instead: **an independent auditor recomputes the ten-edge witness at the two rational parameter values and verifies the one-edge increasing-event reversal**.

The simplest self-contained independent audit is only 1024 configurations: enumerate all `B subseteq E`, weight

\[
w_i(B)=p_i^{|B|}(1-p_i)^{10-|B|}q^{k(B)},
\]

form `Z_i=sum_B w_i(B)` and `X_i=sum_{B:01 in B} w_i(B)`, and check the exact integer cross-product `X_1 Z_2 > X_2 Z_1`. This description is an audit recipe, not a new NM13-05 certificate.

## 6. Method #12 — FIND WHAT IS CONSERVED

The conserved object is not the convenient `x=p/[q(1-p)]` parametrization, nor the later algebraic threshold. It is the **sign of one exact finite event gap** for the frozen source tuple.

Define the audit kernel

\[
K=(G,e_*,q,p_1,p_2,A,\operatorname{sgn}\Delta),
\qquad
\Delta=\phi_{p_1,q}(A)-\phi_{p_2,q}(A)>0.
\]

Every legitimate reparametrization or cancellation in the finite partition functions must preserve `sgn Delta`. At fixed `q`, the map

\[
x(p)=\frac{p}{q(1-p)}
\]

is strictly increasing because `x'(p)=1/[q(1-p)^2]>0`; therefore working in `p`, in `x`, or directly with integer-cleared weights cannot change the order `p1<p2` or the reversal sign.

**Outcome:** this strips the independent audit down to a representation-invariant finite sign check. It also proves why further same-track threshold work is bookkeeping relative to closure: none of it changes the conserved refutation kernel or creates independent auditors.

No new claim is promoted from this diagnostic.

## 7. Method #17 — LOOK FOR YOUR NUMBERS SOMEWHERE ELSE

I ran a fresh bounded public-web search on 2026-09-18 for the exact witness rather than only generic `q<1` terminology. Queries included combinations of:

- the exact probability numerator `72488985858351` and denominator-side value `307499119349131441`;
- `1/32618` with `FK` / random-cluster;
- the exact edge-list string `01,02,03,04,05,12,13,14,16,56`;
- `monotone coupling FK(p,q) q<1`;
- `arboreal gas stochastically monotone Poudevigne Halberstam`.

The exact-number and exact-edge-list searches did **not** surface a public source matching the NM13-05 witness. The generic search did recover the expected surrounding literature:

1. Pete's current April 3, 2024 source still states Question 13.2.
2. Noah Halberstam's 2023 Cambridge thesis, *A Walk through the Forest: the Geometry and Topology of Random Systems*, explicitly states on finite graphs that arboreal gas is not stochastically monotone in its parameter and attributes this to **Rémy Poudevigne, private correspondence**. The same thesis states the arboreal gas is the `q -> 0` random-cluster limit with `p/q -> beta`.
3. Geoffrey Grimmett's random-cluster treatment records stochastic monotonicity for `q>=1` and the failure of the same monotonicity framework below one.
4. Tang--Zhang, arXiv:2609.11578, submitted **2026-09-10**, concerns pairwise negative correlation for broad high-degree regular classes and says the general finite-graph pairwise problem remains open.
5. Heehyun Park, arXiv:2608.08565, submitted **2026-08-09**, concerns the `q<1` model on wired regular trees and negative-dependence/uniqueness there.

These 2026 papers concern dependence at fixed parameters or special infinite-volume geometries, not Pete's all-`p` finite-graph monotone-coupling question.

**Outcome:** the exact explicit witness/minimality package still did not appear in this bounded public search, but this is **not** a novelty certificate. The Poudevigne antecedent is private correspondence and remains inaccessible; it could contain an explicit witness. Therefore publication novelty remains **UNVERIFIED**, and the qualitative small-`q` nonmonotonicity mechanism must not be advertised as novel.

Access note: both the Pete source and Halberstam thesis were retrieved as PDFs and their text layers were inspected. The web screenshot service was also invoked as required but returned cache-miss errors for both PDFs, so no visual-page audit is claimed in this run.

## 8. Method #23 — DO WHAT THE PROPOSER DID NOT EXPECT

Instead of trying to rescue a global coupling by analogy with `q>=1`, port the **proof mechanism** from the solved side and locate its exact sign failure.

Pete's source gives the single-edge heat-bath conditional probability, conditioned on all other edges:

\[
\Pr(e\text{ open}\mid \omega_{E\setminus\{e\}})
=
\begin{cases}
p,&\text{if the endpoints of }e\text{ are already connected},\\[1mm]
\dfrac{p}{p+(1-p)q},&\text{otherwise}.
\end{cases}
\]

When a larger boundary configuration changes the endpoints from disconnected to connected, the conditional open probability changes from

\[
\frac{p}{p+(1-p)q}\quad\text{to}\quad p.
\]

For `q>=1`, the first quantity is at most `p`, so the local update is order-compatible and underlies the attractive heat-bath/monotone-coupling machinery. For `0<q<1`, the first quantity is **strictly larger** than `p`; increasing the surrounding configuration can lower the edge's conditional opening probability. The attractive local update therefore reverses exactly where the source enters its open regime.

This is the nearest solved-problem technique and the precise ingredient it has that `q<1` lacks. It also explains why a successful port of the `q>=1` coupling cannot be the missing C0146 route: the already certified finite witness is the global manifestation of a local sign obstruction rather than a missing technical estimate.

**Outcome:** no new theorem is claimed. The port attempt fails for an exact, source-visible reason, and it confirms that the useful next move is independent verification, not another same-track coupling construction.

## 9. Section-I recovery choice

The required single recovery choice is:

**PORT THE TECHNIQUE FROM THE NEAREST SOLVED PROBLEM.**

I ported the `q>=1` attractive heat-bath mechanism far enough to identify its exact local inequality and showed why the inequality reverses for `q<1`. This is a thinking-only recovery: no new claim, checker, or theorem artifact is created.

The recovery does not move `m_cert`, and it cannot satisfy the independent-audit conjunction. It does, however, rule out spending the next run on a cosmetic variation of the solved-side coupling proof.

## 10. Rotation clock and next legal action

Counters after this invocation:

- `m_cert`: **9 -> 9**;
- `unchanged_runs`: **4 -> 5**;
- `stuck_recoveries`: **1 -> 2**;
- source status: **REFUTED -> REFUTED**;
- P26 C0146 audit: **NOT PASSED**;
- NM13-06 C0146 audit: **NOT PASSED**.

Thus one unchanged run remains before the CLOSABLE six-unchanged rotation rule bites. The next invocation must first reread P26/NM13-06 and the repository. If both independent C0146 PASS records have appeared, reconcile closure under Section G. If closure has not moved, the sixth unchanged run must preserve a complete C0146 handoff and rotate to an eligible unclaimed residue-4 CLOSABLE source; it must **not** spend another ordinary run sharpening `q_*`, enlarging a census, or filing another self-check.

Reserved Section-B moves, **not attempted here**, if an owner-authorized mathematical continuation of C0146 becomes necessary before rotation: **#9 RANDOMIZE, #13 FIND WHAT ONLY INCREASES, #28 REPLACE FOR ALL WITH FOR TYPICAL**. Otherwise a newly admitted successor starts with its own problem-specific unspent method history; no C0146 method is silently carried over as “tried” on a new source.

## 11. Structured ledger_delta for P26

```yaml
ledger_delta:
  task: NM13-05
  source_id: C0146
  claim_id: C0146
  claim_path: operations/claims/C0146.md
  canonical_dedup_key: fk_q_less_than_1_monotone_coupling
  category: CLOSABLE_OUTSIDE
  status_before: REFUTED
  status_after: REFUTED
  closure_status: PENDING_INDEPENDENT_AUDITS
  metric_name: m_cert
  metric_definition: largest m such that every finite simple graph with at most m edges has FK(p,q) stochastically nondecreasing in p for every q in (0,1)
  metric_before: 9
  metric_after: 9
  metric_movement: false
  source_refutation_kernel:
    vertices: 7
    edges: [01,02,03,04,05,12,13,14,16,56]
    distinguished_edge: 01
    q: 1/40000
    p1: 1/2001
    p2: 1/1601
    increasing_event: "01 open"
    strict_reversal: true
  methods_actual:
    - 12
    - 17
    - 23
  methods_outcome:
    12: "Frozen the representation-invariant audit kernel to the sign of the exact one-edge event gap; no closure movement."
    17: "Exact-number/edge-list public search found no matching public witness; Poudevigne private-correspondence prior-art warning remains decisive; novelty UNVERIFIED."
    23: "Ported q>=1 heat-bath mechanism and identified exact reversal of the local attractiveness inequality for q<1; no new claim."
  recovery_type: STUCK_RECOVERY_2
  recovery_choice: PORT_NEAREST_SOLVED_TECHNIQUE
  unchanged_runs_before: 4
  unchanged_runs_after: 5
  stuck_recoveries_before: 1
  stuck_recoveries_after: 2
  p26_audit: NOT_PASSED
  secondary_auditor: NM13-06
  secondary_audit: NOT_PASSED
  novelty: UNVERIFIED
  next_step: "At next invocation, reconcile fresh P26/NM13-06 audits. If closure still unchanged, execute sixth-unchanged CLOSABLE handoff and rotate to an eligible unclaimed residue-4 source; do not add another C0146 lemma/self-check."
```

## 12. Safeguards

This invocation created **no** new mathematical claim, checker, artifact, peer edit, shared-root edit, workflow execution, permission change, public post, email/Drive action, paid compute, or schedule change. It writes exactly this one immutable report in `proofnet24/NM13-05/runs/` and reads it back at its creation commit. The report is a stuck-recovery/continuity record, not a claim of closure.