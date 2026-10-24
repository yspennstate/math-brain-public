# B04 historical login is invalid JSON — verified artifact defect, not diagnosed run failure

Interactive addendum to [the 21:06 B04 prompt/path and proof audit](https://github.com/yspennstate/math-research-brain/blob/138e6179e3626eee8e819831cf3f1328c08e7f50/scheduled_tasks/work/shared/qform-density-2026-09-22/handoffs/interactive/20260923T210604Z-B04-prompt-and-fake-plane-audit.md). Checked 2026-09-23 21:09 UTC.

The [B04 11:10 sign-in artifact, created at commit 476b42b](https://github.com/yspennstate/math-research-brain/blob/476b42beea636c37af63c1be96c002649e36a97f/scheduled_tasks/status/account04/logins/2026-09-23T11Z/B04-20260923T111017Z.json) is human-readable but **not valid JSON**. Its first bytes are:

```text
SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account04, slot B04, 2026-09-23T11:10:17Z.
attacking: optimize volume weights and compare D-prime, D5, and ridge certificates on one original-coordinate matrix.

{
```

A literal JSON parser fails on the initial `S`, before reaching the JSON object. The `.json` artifact also uses a suffixed filename, whereas the newest [mutable worker entrypoint](https://github.com/yspennstate/math-research-brain/blob/main/scheduled_tasks/work/shared/qform-density-2026-09-22/requests/QFORM-CLAUDE-LATEST-20260922T225732Z.md) now explicitly asks for `scheduled_tasks/status/<account>/logins/<actual-UTC-hour>/<slot>.json`. At 20Z, the independently fetched B02, B06 and B20 `.json` artifacts all parse as JSON; these particular other slots also used suffixed filenames, so filename difference alone does **not** identify a B04-specific fault.

This establishes a real historical **machine-readable receipt defect**, but does not establish whether any automation parses that file, why the B04 run stopped after its 11Z sign-in, or whether later native last-run entries completed. Do not overwrite or manufacture the immutable worker-owned login. The current B04 prompt already points to the mutable entrypoint containing the exact canonical login path; no targeted native prompt change has a proven basis yet. Compare actual 21Z normal-run login, math output and handoff before diagnosing further.
