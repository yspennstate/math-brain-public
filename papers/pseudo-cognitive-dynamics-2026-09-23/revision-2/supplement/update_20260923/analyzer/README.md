# AB30 current-source audit and proposed repairs — 23 September 2026

**The new diet-arm analyzer has two unresolved source issues: the original score aggregation crash remains, and the new runner's diet environment flag is not read by the committed dispatcher.** This package rebases the one-line aggregation repair onto the current analyzer and proposes an explicit per-session diet override. The repairs are tested with synthetic records and mocked process boundaries. No live campaign file was changed, no solver or hook process ran, and no benchmark completion, causal benefit, runtime activation, or Claude receipt is claimed.

The audit is pinned to `<private-repo>` commit `9c754d786b3a0ea4943da0585d1490c13cd9ef99`, committed at **19:52:16 UTC on 23 September 2026**. Its message is “ab30: analysis reads the round-2 diet arm.” The immediately relevant runner change is commit `c8e021183253fc65201afbe4f891b91633c54f9c`, committed at 19:31:36 UTC. Times written in the campaign prose use the owner's clock and should not be silently interpreted as UTC. [Analyzer commit](https://github.com/<private-repo>/commit/9c754d786b3a0ea4943da0585d1490c13cd9ef99), [runner commit](https://github.com/<private-repo>/commit/c8e021183253fc65201afbe4f891b91633c54f9c).

## Exact sources

The files in `source/` reproduce these Git objects byte for byte. `source_manifest.json` records their SHA-256 digests, byte lengths, and the corresponding proposed copies.

| Source | Pinned Git blob | Bytes |
|---|---|---:|
| `source/analyze.py` | `5e49709186b23a8253f390233df0a0c44120ffc1` | 12,629 |
| `source/ab30_run.py` | `c8e29fa23c843d2f29efff9edd57362505d796c7` | 11,880 |
| `source/hook_dispatch.py` | `565001f17c802fb49e4c0bd2a848252b65363ca2` | 42,199 |

The source URLs are the [analyzer](https://github.com/<private-repo>/blob/9c754d786b3a0ea4943da0585d1490c13cd9ef99/12_cognitive_architecture/brain_improvement/campaign_2026-09-23_ab30_tokens/tools/analyze.py), [runner](https://github.com/<private-repo>/blob/9c754d786b3a0ea4943da0585d1490c13cd9ef99/12_cognitive_architecture/brain_improvement/campaign_2026-09-23_ab30_tokens/tools/ab30_run.py), and [dispatcher](https://github.com/<private-repo>/blob/9c754d786b3a0ea4943da0585d1490c13cd9ef99/12_cognitive_architecture/dreaming/hook_dispatch.py). Neither the question bank nor quarantined answer keys were fetched for this audit.

## 1. The prior aggregation repair has not reached this tracked analyzer

The current `score()` still evaluates:

```python
for fam in sorted({r["family"] for r in res["items"]}) | {"all"}:
```

This attempts a union between the list returned by `sorted()` and a set. The synthetic control reproduces `TypeError: unsupported operand type(s) for |: 'list' and 'set'`, before `RESULT.json` is written. `proposed/analyze.py` changes only that line, moving the union inside `sorted()`:

```python
for fam in sorted({r["family"] for r in res["items"]} | {"all"}):
```

The old proposal targeted blob `0a1879f693f1512df9142db4bb483dc9d5949468`. The new proposal preserves the diet and `--runs-dir` additions in blob `5e49709186b23a8253f390233df0a0c44120ffc1`; applying the old whole-file corrected copy would lose those additions. The current regression verifies three synthetic pairs across two families plus the combined group, with one win, one loss, and one tie. This is a software result. It supplies no actual AB30 scores. [Current analyzer](https://github.com/<private-repo>/blob/9c754d786b3a0ea4943da0585d1490c13cd9ef99/12_cognitive_architecture/brain_improvement/campaign_2026-09-23_ab30_tokens/tools/analyze.py).

The earlier paper handoff is present under `12_cognitive_architecture/agent_mesh/proposed/pseudo-cognitive-dynamics-2026-09-23/` at commit `e773e3f61fefeb93019c0b747277927104652297` (19:36:01 UTC). At the audited revision, the path history contains that publication commit and the inspected folder has the original handoff, README, paper, and supplement. No tracked acknowledgment was found there. The root review notice still says acknowledgment has not been observed; that notice is part of the original publication and is not an independent delivery receipt. Native mesh receipts were unavailable. The defensible statement is that the tracked analyzer has not adopted the grouping correction and receipt/adoption by the native worker remains unverified. [Published handoff commit](https://github.com/<private-repo>/commit/e773e3f61fefeb93019c0b747277927104652297), [root notice](https://github.com/<private-repo>/blob/9c754d786b3a0ea4943da0585d1490c13cd9ef99/PSEUDO_COGNITIVE_DYNAMICS_REVIEW_2026_09_23.md).

## 2. The diet flag and the dispatcher do not agree

The runner's `child_env()` removes inherited `BRAIN_HEADLESS_DIET` and then sets it to `1` for `ondiet`. Both `on` and `ondiet` use the ordinary home working directory and the same prompt beginning `[headless-worker]`. However, the committed dispatcher's `_headless_session()` never reads `BRAIN_HEADLESS_DIET`: it first requires the sibling file `HEADLESS_DIET_ON`, then recognizes the prompt or a stored headless-session mark. This makes the arm name insufficient to establish different dispatch behavior. [Runner](https://github.com/<private-repo>/blob/9c754d786b3a0ea4943da0585d1490c13cd9ef99/12_cognitive_architecture/brain_improvement/campaign_2026-09-23_ab30_tokens/tools/ab30_run.py), [dispatcher](https://github.com/<private-repo>/blob/9c754d786b3a0ea4943da0585d1490c13cd9ef99/12_cognitive_architecture/dreaming/hook_dispatch.py).

The current-source control obtains this table for the same synthetic headless prompt:

| Global marker | `on` classed for diet | `ondiet` classed for diet |
|---|---:|---:|
| Absent | False | False |
| Present | True | True |

This establishes an integration mismatch in the pinned source files. It does not establish which dispatcher was installed on the native machine, whether the marker existed, whether the environment reached an installed hook process, or what any actual trial received. Those require native provenance and event traces.

### Proposed mode repair

`proposed/ab30_run.py` continues to strip inherited experiment flags and explicitly supplies `0` for `on` and `1` for `ondiet`. `proposed/hook_dispatch.py` reads those values before the existing headless classifier:

| Environment value | Mode decision before existing headless classification |
|---|---|
| `0` | Disable diet even if the global marker exists |
| `1` | Enable diet without requiring the global marker |
| Unset or unrecognized | Preserve the existing global-marker behavior |

An enabled mode still requires the existing headless prompt or stored headless-session mark. It does not turn an unmarked ordinary session into a worker, remove the standard startup documents, or redesign the hook skip list. The `off` arm retains safe mode. This is an amended experimental mechanism requiring controlled integration and documentation before its effects can be assessed.

The controls cross two marker states, three inherited flag states, and two experiment arms: all **12 combinations** preserve `on=False`, `ondiet=True`. They also check the legacy fallback, unmarked ordinary/startup events, and later tool events using a synthetic saved headless mark. A mocked dispatch exercises the actual dispatch selection branch: full mode invokes both mock `slow_sense.py` and `math_sense.py`, whereas diet mode skips the former and retains the latter. No real hook process is executed; creation of the actual runtime mark and end-to-end hook delivery are not tested here.

## 3. Diet visibility is broader than diet scoring

The analyzer now sets `ARMS = ("on", "off", "ondiet")`. `runs()`, `audit()`, `tokens()`, and `sheet()` see the third arm. `tokens()` adds per-arm/family diet summaries and same-item diet/on cost ratios, plus paired hook bytes and local time. `sheet()` gives diet answers masked rows. In contrast, `score()` still selects only `(id, "on")` and `(id, "off")`; even after the grouping repair, diet grades do not enter a contrast or score summary. Its CLI has no argument choosing a contrast. The synthetic fixture demonstrates that supplying a diet grade leaves the on/off result unchanged. [Analyzer](https://github.com/<private-repo>/blob/9c754d786b3a0ea4943da0585d1490c13cd9ef99/12_cognitive_architecture/brain_improvement/campaign_2026-09-23_ab30_tokens/tools/analyze.py).

`--runs-dir` selects one results tree. It does not combine rounds or retrieve a baseline from another directory. A root containing only `ondiet` yields a diet arm total and no diet/on pair. Conversely, colocating an old `on` result with a newer `ondiet` result for the same item creates a pair without checking start time, round, model, prompt hash, or brain version. Output rows do not retain an explicit round field. The supplied controls reproduce both behaviors. Keep round roots and an explicit cohort/provenance manifest separate; define a concurrent same-round comparison before treating any constructed pair as such.

The inspected AB30 directory still contains the original [PREREG.md](https://github.com/<private-repo>/blob/9c754d786b3a0ea4943da0585d1490c13cd9ef99/12_cognitive_architecture/brain_improvement/campaign_2026-09-23_ab30_tokens/PREREG.md), [DEVIATION.md](https://github.com/<private-repo>/blob/9c754d786b3a0ea4943da0585d1490c13cd9ef99/12_cognitive_architecture/brain_improvement/campaign_2026-09-23_ab30_tokens/DEVIATION.md), stamps, bank, tools, and a [README with an unfilled running-results section](https://github.com/<private-repo>/blob/9c754d786b3a0ea4943da0585d1490c13cd9ef99/12_cognitive_architecture/brain_improvement/campaign_2026-09-23_ab30_tokens/README.md). No final run/grade result or separate diet statistical protocol was present in that inspected directory. This is a repository-snapshot observation, not a declaration that native work has stopped or no additional records exist elsewhere.

## 4. Cumulative tokens are handled, but experiment cost and eligibility need separate accounting

`tok()` continues to prefer nonempty `modelUsage`, summing every model's uncached input, cache reads, cache creation, output, and separately reported thinking. It falls back to `usage` only when the cumulative object is empty or absent. The synthetic two-model case gives input **7**, cache reads **30**, cache creation **10**, output **12**, and thinking **3**, even when `usage` deliberately reports a conflicting output value. `total_in` is **47**; thinking is not added again to output. These are fixture values, not measured campaign tokens. [Analyzer](https://github.com/<private-repo>/blob/9c754d786b3a0ea4943da0585d1490c13cd9ef99/12_cognitive_architecture/brain_improvement/campaign_2026-09-23_ab30_tokens/tools/analyze.py).

The surrounding accounting still has concrete limits:

- `runs()` reads one current `result.json` per item/arm. It does not read the append-only `results.jsonl` attempt history or the excluded pilot directory. Earlier costs can therefore be absent from its table.
- The table retains a failed record, but aggregate arm and family summaries select the literal predicate `status == "ok"`. Unmatched eligible-status runs enter arm totals; pair ratios use only matched runs with a truthy denominator cost. Those are different populations.
- Neither token summaries nor scoring consume `AUDIT.json` or an exclusion manifest. The controls show that a synthetic contamination hit does not remove an item.
- Missing numeric components become zero. A partial nonempty `modelUsage` prevents fallback, and the output does not label accounting completeness. A missing count is not evidence of zero consumption.
- The new runner progress line now sums `modelUsage`, resolving its earlier last-chain display issue when cumulative usage is present. It has no `usage` fallback, so a missing cumulative block displays zero there while `tok()` may use fallback counts. DEVIATION item 4 still describes the older progress-line behavior and needs a dated follow-up rather than an unmarked historical rewrite.

The runner also marks any nonempty result event as `ok` when there was no wall timeout, without requiring `rc == 0` or `is_error == False`. A mocked error event with `rc=1` and `is_error=True` is labeled `ok`, then skipped as already done on a repeat call. Thus “status ok” should not be paraphrased as successful completion without inspecting the other fields. `main()` does not itself implement the preregistered once-only API retry policy; restarting a non-ok attempt reuses and overwrites its stream path, while only a reduced record is appended to the attempt ledger. This package reports these semantics and does not guess a replacement grading/retry policy. [Runner](https://github.com/<private-repo>/blob/9c754d786b3a0ea4943da0585d1490c13cd9ef99/12_cognitive_architecture/brain_improvement/campaign_2026-09-23_ab30_tokens/tools/ab30_run.py), [preregistration](https://github.com/<private-repo>/blob/9c754d786b3a0ea4943da0585d1490c13cd9ef99/12_cognitive_architecture/brain_improvement/campaign_2026-09-23_ab30_tokens/PREREG.md).

## 5. Missing pairs, duplicate grades, and contamination remain explicit analysis obligations

After the grouping repair, `score()` still builds its item set from supplied grades, skips missing on/off partners, and overwrites previous grades for the same `(item, arm)`. It does not validate the preregistered cohort, grade uniqueness, completion status, or pair exclusions. The synthetic control includes a duplicate grade, a one-arm item, an entirely absent expected item, a diet grade, and an audit hit: the duplicate's last value wins, the incomplete/absent/diet entries are not reported as such, and the audited item remains in the score.

`audit()` is a pattern scan over streams associated with result files. It ignores malformed JSON lines, so an empty or malformed-only stream produces an empty hit list and a printed `CLEAN` label. A missing stream raises an error; it is not silently certified clean. Tool inputs use a broad case-insensitive forbidden pattern list, whereas tool results use a narrower, case-sensitive scan for four key markers. An empty hit list establishes only absence of those detected patterns in parsed events, not complete logging, no forbidden access, or compliance with the local-file and network rules. The current code does not apply the preregistered rule that a contaminated item is removed from both arms. [Analyzer](https://github.com/<private-repo>/blob/9c754d786b3a0ea4943da0585d1490c13cd9ef99/12_cognitive_architecture/brain_improvement/campaign_2026-09-23_ab30_tokens/tools/analyze.py), [preregistration contamination rule](https://github.com/<private-repo>/blob/9c754d786b3a0ea4943da0585d1490c13cd9ef99/12_cognitive_architecture/brain_improvement/campaign_2026-09-23_ab30_tokens/PREREG.md).

The sign-test helper still rounds to five decimal places. The fixture with 19 wins and zero losses returns `0.0` even though the exact two-sided probability is `2 / 2**19 > 0`. A reported rounded zero must not be interpreted as a zero probability.

## Reproduce

From any working directory:

```bash
python3 /path/to/analyzer/reproduce_update_audit.py
```

`regression_output.txt` contains actual stdout from an external-working-directory run; `validation.json` records Python, exit code, and the synthetic-only scope. All controls pass. `REPRODUCED` lines confirm limitations in the current sources; they are not failed repair assertions. The original and proposed module hashes and the exact unified patch are verified before the controls execute. Separately, `git apply --check` and `git apply` both succeeded in a disposable tree containing only the pinned sources; all three resulting files matched the proposed copies byte for byte. This was not a live application.

## Integration boundary

This remains an additive review package. The [current mesh protocol](https://github.com/<private-repo>/blob/9c754d786b3a0ea4943da0585d1490c13cd9ef99/12_cognitive_architecture/agent_mesh/PROTOCOL.md) requires native resource leases and assertion before live mutations; file-only siblings use additive proposals. No native lease or structured receipt was available in this audit. The preparing session neither edits the native campaign nor changes its schedule or worker ownership.

An authorized native integrator should compare the current files with these pinned sources, review the exact patch, and preserve intervening edits. The diet change must be recorded as an experiment amendment. Verify the effective deployed dispatcher, per-arm environment, global marker, saved session classification, and actual retained/skipped hook events before making delivery or cost claims. Editing the dispatcher can also invalidate its timestamp-based in-process allowlist; the existing independent equivalence/re-signing procedure remains relevant and is not exercised by these mocks. Establish grade/cohort/audit/retry handling separately before final analysis. A repaired source path and passing synthetic controls do not constitute AB30 trial results.
