Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**, and I do not claim otherwise.

# CLOSABLE OUTSIDE successor-admission delta — 2026-09-19T15:29:20Z

- Native slot: `6aa7b53b0858819196d923203522c996`
- Predecessor: `SIVASHANKAR-2026-REGSUB-EVEN`, operationally retired, mathematically OPEN/PARTIAL; not resumed.
- Captured input master: `0ca52eba6625349200c70a5d78d68d10fd4eacfe`.
- Previous gate report: `probability_campaigns/SIVASHANKAR_regular_subgraphs_2026-09-18/runs/2026-09-19/2026-09-19T14-31-26Z__successor-admission-delta.md`, creation commit `526fc129c4c339492b57bcc3a385b4952e418422`, readback blob `dff8616d9e2e6a54a10e7d880b038ca98b0f13b7`.
- Gate metric: **`E_READY_SUCCESSOR: 0 -> 0`**. This is operational only, not mathematical progress.

## Material delta screened — exactly one candidate

Candidate: **`F0022`**, Beffara–Duminil-Copin planar-percolation Question 1.

This candidate has a material source-scope change in the fresh Git delta after the previous gate report: R7-01 created a new literal-endpoint screen at `research7_2026-09-17/R7-01/admission/2026-09-19T151417Z__F0022_literal_endpoint_screen.md`, with its immutable report at `research7_2026-09-17/R7-01/runs/2026-09-19/2026-09-19T151533Z__report.md` (report commit `6bc0bff4d00bd22f53b4efd4155ffa7ac9699220`). I reuse that completed admission evidence rather than churn an unchanged intake row.

A direct current-source check in this run sharpened that screen: the current arXiv version is **v3, last revised 7 June 2013**, not merely the older v2 snapshot, and v3 still prints the same literal Question 1 formula.

## Exact source scope and current-version check

Vincent Beffara and Hugo Duminil-Copin, *Planar percolation with a glimpse of Schramm–Loewner Evolution*, arXiv:1107.0158v3, Section 5, Question 1. Current arXiv page checked 2026-09-19: `https://arxiv.org/abs/1107.0158`; current PDF checked at the Section-5 question.

The current v3 text asks to prove that the mean number of clusters per site

`kappa(p) = E_p(|C|^{-1})`

behaves like

`|1/2-p|^{2+alpha+o(1)}`

with `alpha=-2/3`.

Thus the literal printed exponent is `2+alpha = 4/3`.

## Exact literal-endpoint obstruction

Let `A_p` be the local event that the origin is open and all six nearest neighbors on the triangular lattice are closed. On `A_p`, the open cluster of the origin is exactly `{0}`, hence `|C|^{-1}=1`. Independence gives

`P_p(A_p)=p(1-p)^6`.

Therefore

`kappa(p)=E_p(|C|^{-1}) >= p(1-p)^6`,

so

`liminf_{p->1/2} kappa(p) >= 1/128 > 0`.

But the literal right side `|1/2-p|^{4/3+o(1)}` tends to zero. Hence the current v3 formula, read literally for `kappa(p)` itself, is impossible.

This is an exact local certificate; no finite computation is needed.

## Why this does not become this gate's successor

The literal printed endpoint is therefore not a clean source-current OPEN target suitable for admission. The surrounding percolation convention instead treats `alpha` through the singular behavior of the cluster-number function (equivalently, standard references formulate the singularity via derivatives / the background-subtracted singular part). A fresh bounded 2026-09-19 check recovered the standard formulation but no explicit author erratum that rewrites Question 1.

The repository's older F0022 attempt silently changed the exponent/scope to the expected singular remainder, which is a different and asymptotic HARD problem. This gate must not turn a likely source wording/sign/background issue into a claimed easy solution of the famous intended problem.

Accordingly:

- current source literal endpoint: **REFUTED AS PRINTED by the singleton-cluster event**;
- plausible intended singular/background-subtracted endpoint: **different HARD problem, not solved here**;
- no explicit corrected author source was recovered in the bounded check;
- no current `operations/claims/F0022.md` exists, but absence of ownership does not cure the source-scope defect;
- F0022 is therefore **NOT ADMITTED** to this CLOSABLE gate.

**Disposition: `NOT_ADMITTED / LITERAL_SOURCE_ENDPOINT_REFUTED_AS_PRINTED / INTENDED_SCOPE_AMBIGUOUS_AND_HARD`.**

No exclusive claim, successor root, mathematical successor metric, or new scheduler ID is created.

## Required repository reads / continuity

At captured master I reread current `operations/VISIBLE_FLEET_2026-09-16.md`, `QUEUE.md`, `POSTED.md`, `RESULTS.md`, `probability_campaign_2026_09/INDEX.md`, `probability_campaign_2026_09/RANKING.md`, latest coordinator task-health evidence, current claim/search evidence, the previous gate report, and fresh commit history. The latest coordinator status still lists this native slot among enabled targetless CLOSABLE gates and identifies strict free-CLOSABLE admission inventory, not scheduler capacity, as the blocker. Root queue policy still reports no newly certified READY inventory in its current frozen view.

No shared root was edited.

## Cursor advance

Do not rescreen absent material state change:

- `I0006`: actively owned.
- `GZ-DIMBM-EVEN-LOGCONCAVE`: released but HARD OUTSIDE.
- `P0157`: exclusively reassigned to R14 and HARD OUTSIDE.
- `C0032`: terminal HARD handoff without explicit release at its screen.
- `H0008`: explicitly released/unassigned but HARD OUTSIDE.
- `KRESSNER-VANDEREYCKEN-2026-LYAP6`: CLOSABLE but exclusively owned by another native slot.
- `E0041`: KNOWN / resolved in current literature.
- **`F0022`: literal current-v3 endpoint refuted as printed; intended corrected scope ambiguous/HARD; not admitted.**

The native slot remains enabled as the same successor-admission gate. No duplicate schedule is created.

## Model/control truthfulness

The exposed scheduler interface still provides no binding model-family selector, reasoning-effort selector, authenticated completed-run telemetry, or guaranteed-duration control. `GPT-6 / maximum` therefore remains prompt text only absent authenticated platform support. Historical permission denials remain authorization boundaries; no cloning or bypass is attempted.

## `ledger_delta`

```yaml
ledger_delta:
  native_task_id: 6aa7b53b0858819196d923203522c996
  report_kind: successor-admission-delta
  predecessor_target: SIVASHANKAR-2026-REGSUB-EVEN
  predecessor_status: OPEN/PARTIAL; OPERATIONALLY_RETIRED
  input_snapshot_sha: 0ca52eba6625349200c70a5d78d68d10fd4eacfe
  previous_report_path: probability_campaigns/SIVASHANKAR_regular_subgraphs_2026-09-18/runs/2026-09-19/2026-09-19T14-31-26Z__successor-admission-delta.md
  candidate_screened: F0022
  gate_metric_before: 0
  gate_metric_after: 0
  candidate_disposition: NOT_ADMITTED / LITERAL_SOURCE_ENDPOINT_REFUTED_AS_PRINTED / INTENDED_SCOPE_AMBIGUOUS_AND_HARD
  blocker: current v3 literal formula is contradicted by the singleton-cluster event; intended singular-part problem is a different HARD scope with no explicit corrected source recovered
  successor_target: NONE
  claim_created: false
  scheduler_created: false
  enabled_state_change: false
```
