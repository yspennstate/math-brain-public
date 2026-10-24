# Scheduled FEI continuation: read, verify, extend

Owner instruction, 19 September 2026: ensure scheduled researchers read the newest FEI results and improve them. **Full FEI remains OPEN.** This routing document makes research uptake verifiable; it is not evidence of a completed future run or an independent mathematical audit.

## Actual scheduling action

An attempt to update the existing P03 native task returned the exact error `You cannot modify this task.` That task was left unchanged. The scheduler separately accepted a new task titled **FEI proof continuation**, enabled with recurrence `FREQ=HOURLY`, start `20260919T171810Z`. Acceptance was recorded at `2026-09-19T17:18:11.648163+00:00`. Its initial `last_run_time` was null. This is one additional continuation, not a claim that every existing worker's prompt was edited.

The installed prompt explicitly requires current-master retrieval, full reading of the latest mathematical report, hypothesis checks, new mathematical work, immutable GitHub delivery, and readback verification. It neither modifies nor impersonates the existing P03 task and does not alter source ownership, other workers, native metrics, repository permissions, or visibility. It requests the owner's model preference but does not claim that model/reasoning settings or guaranteed durations are exposed by the scheduler.

## Mandatory entry point for every FEI researcher

Start from [the current FEI index](../README.md), then read:

1. [Latest coded-budget handoff](../handoffs/2026-09-19__coded-budget-obstruction.md).
2. [Full coded-budget proof report](../continuations/2026-09-19-coded-budget/REPORT.md), including assumptions, counterexample construction, entropy stability, accumulated resolvent bounds, and Section 8's remaining gap.
3. [Verifier](../continuations/2026-09-19-coded-budget/verify_continuation.py) and [recorded output](../continuations/2026-09-19-coded-budget/verification.json).
4. All later linked corrections and substantive FEI continuations, including neighboring workers' newest reports. Read complete relevant text; a preview is not the full proof.

Initial checkpoint: `c08370da6804119c0d551804e3183bd28a3ed9bd`. This is a provenance anchor, not a permanent pin: use newer master and actual blob SHAs on every run.

Initial report blob: `6bd3cef08192616a27053f01edb94863e7ad3720`.
Initial verifier blob: `42cf2d56d9a2afdcd63f29565427170271b65219`.
Initial output blob: `8241055f1e7ab82b6f2f5f456d78180994765c30`.
Initial handoff blob: `4f19439e22e8e0fb77efd6a0cdafbb0f0d118aed`.

Core proof text and checks are committed in GitHub. They do not require the original chat attachments. Some older attachments have expired; do not claim the complete 1,506-page archive is available merely because its historical filename appears. Retrieve actual missing dependencies and state any genuine access limitation.

## First use versus subsequent research

On first use, reconstruct the critical steps of the coded obstruction, entropy-packet lemma and accumulated full-resolvent bound before using them. Execute the verifier when a runtime is available and record the exact script version and result. The large example uses an analytic reduction plus code geometry, not enumeration of 2^2040 inputs. A verifier rerun is a self-check, not proof that the entire analytic argument is sound.

On later runs, inspect changes and continue substantive mathematics. Do not spend each hour producing another unchanged certificate or a standalone acknowledgement. Correct a discovered gap visibly and never assume that a previous report's PROVED label substitutes for its proof.

## Mathematical constraints and useful next work

The previous scalar inequality `D_cross <= K(R+Q_log)` is disproved for every fixed K, including positive-power scalar variants. The coded family is not an FEI counterexample: its ordinary H/I tends to four. The full pivotal resolvent C survives that family, but survival of one test does not establish a universal estimate.

The live sufficient target is

    D_cross(f) <= K [C(f)+Q_log(f)]  for every Boolean f,

with finite dimension-free K and the exact definitions in the report. It is **unproved** and not known here to be equivalent to FEI. The accumulated bounds, if valid as written, give the implication

    H(f) <= [4/ln2+(3/2)sqrt2+5/4] K J(f),   J(f)<=I(f).

No additional unknown summability step remains after that pointwise estimate in this route. The pointwise estimate itself may contain the principal mathematical difficulty or be false. A counterexample to it is not automatically a counterexample to FEI.

The alternative universal erasure target `sup_f B(f)/I(f)<infinity` also remains live. The pointwise shortcut `H(f)<=B(f)+(2/ln2)I(f)` is false; only the correctly quantified universal/hereditary implications may be used.

Useful complementary efforts include global signed-convolution/entropy control, systematic stress tests of the full-resolvent target on new structured families, and uniform extensions handling genuinely new interactions between spectral scales. Retain phase signs and correlations; do not reintroduce disproved absolute-value or scalar replacements. A successful finite search, a smaller auxiliary constant, and a renaming of the remaining inequality do not solve FEI.

If the same method has no substantive progress for three consecutive attempts, state the exact obstruction and change the method within this FEI continuation. Do not reset history or rotate this new owner-requested continuation to an unrelated problem. Preserve prior native P03 metrics and other workers' current ownership separately.

## Evidence required inside each substantive report

Use a unique path under `proofnet24/P03-fei/scheduled-continuation/runs/<UTC-date>/` and matching artifacts directories. Each report must contain:

- `consumed_updates`: actual path, blob SHA, and sections fully read;
- `reused_results`: precise theorem statements and hypotheses actually used, not only links;
- `new_mathematical_delta`: a proved improvement, a specific failed attack with reason, a counterexample, or an explicitly open proposal; say NO MATHEMATICAL IMPROVEMENT when appropriate;
- `actual_checks`: execution, arithmetic, script hash, output and limitations;
- `remaining_full_scope_gap`: the exact unresolved all-dimensional statement;
- `source_status`: OPEN/PARTIAL unless a complete source-level resolution exists;
- `delivery`: real commit SHA and content readback, or the exact failure.

A consumption receipt belongs in the mathematical report, not a separate empty commit. These fields distinguish four separate events: files are reachable; a task is configured to retrieve them; a run actually read and used them; a run genuinely improved the mathematics. Only the first two are established by this deployment.

Use connected GitHub write actions if terminal Git is unavailable. Preserve concurrent changes, never force-push, and honor access or approval boundaries. GitHub-only research output: no email, Drive, public publication, permission changes, workflow execution, or changes to other schedules. Honor later user/platform stops. Independent audits and publication-priority checking remain required before source closure.
