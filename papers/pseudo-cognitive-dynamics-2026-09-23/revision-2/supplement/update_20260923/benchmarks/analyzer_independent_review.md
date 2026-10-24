# Independent review of the AB30 analyzer update package

Reviewed on 2026-09-23 against the exact pinned sources and proposed patch in `paper/supplement/update_20260923/analyzer/`.

## Conclusion

The analyzer agent's two central source findings are independently confirmed, and the proposed patch is appropriately scoped to those findings. It repairs the family-grouping type error and connects explicit per-arm diet modes to the existing headless classifier. It does not supply missing trial results, diet grades, cohort validation, contamination exclusions, or full attempted costs.

## Independent checks actually performed

I recomputed Git blob hashes from the local source bytes: runner `c8e29fa23c843d2f29efff9edd57362505d796c7`, dispatcher `565001f17c802fb49e4c0bd2a848252b65363ca2`, analyzer `5e49709186b23a8253f390233df0a0c44120ffc1`. I extracted the actual `child_env` and `_headless_session` function ASTs, and executed them with synthetic environments and a synthetic path-existence function. The current source gives:

| Shared marker | on | ondiet |
|---|---:|---:|
| absent | false | false |
| present | true | true |

This independently establishes the documented failure of arm separation under both marker states for the common headless prompt. No live flag, native process, or external file was changed. I also evaluated the actual current scorer's grouping expression on a synthetic family and reproduced the list/set `TypeError`. Exact review output is in `analyzer_independent_review.json`.

## Proposed changes inspected

The analyzer diff changes only the previously identified grouping expression, and preserves all newly added diet and alternate-root accounting. The runner diff sets an explicit 0 for on and 1 for ondiet after inherited flags are removed. The dispatcher diff reads that exact environment variable, lets 0 disable the diet despite the global marker, lets 1 enable the existing classifier without the global marker, and preserves legacy marker behavior for unset/unrecognized values. It retains the requirement for a recognized headless prompt or saved headless mark.

I inspected the repair agent's reproduction script and recorded stdout. Its twelve marker/inheritance/arm combinations address the relevant source-selection boundary; its mocked dispatch distinguishes a skipped synthetic operational hook from a retained synthetic math hook. The current-source behavior was independently reproduced above; the full repair suite was not redundantly rerun because no unresolved discrepancy remained after inspection. The source and patch identity checks in that suite protect against accidentally replacing the new analyzer with the obsolete whole-file repair.

## Remaining limits correctly documented by the analyzer agent

- score() remains an on/off contrast and ignores diet grades.
- Alternate result roots do not import a historical comparator; colocated same IDs can be paired without a common round, start time, model or snapshot.
- The cost table retains some failed rows, while aggregate summaries select literal status==ok and omit attempt history and pilots.
- The runner can label an error result ok; missing cumulative counters can become displayed zero.
- Neither score nor token summaries consume the contamination report.
- Duplicate grade keys overwrite; missing pairs and expected-but-absent items are not made explicit.
- An empty or malformed-only stream can produce an empty audit-hit list; absence of hits is not verified absence of contamination.
- Sign-test rounding can display zero although the exact probability is positive.
- The patch does not verify which dispatcher is deployed or what an actual trial received.

These are accurate source semantics. The update text should keep the proposed repair separate from any report of integration or adoption. Existing frozen results, if later produced, cannot be reinterpreted as diet-separated without per-run receipts.

## Interpretation of the diet

The patch restores the intended ability to identify arms at this interface; it does not establish that every skipped hook was irrelevant to the task. The unchanged skip list includes canonical routing and project-memory hooks alongside operational context. It also leaves the standing startup documents in place. Future claims about token savings, retained mathematical context or unchanged behavior must use actual delivered-hook and model-usage receipts.

No objection to delivering this as a reviewed local proposal, with the explicit integration boundary and outstanding analysis obligations already present in its README.
