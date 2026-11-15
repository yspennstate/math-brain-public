# Codex probe harness

Small tools for running one Codex worker at a time against a prepared folder and reading what it did afterwards.
They were written for two jobs: brain/no-brain comparisons on our own research history, and checking which of a
worker's actions the hook layer actually sees.

## Files

- `run_probe.py <ID>` starts one Codex worker in `<ID>/` with that folder's `PROMPT.md` on stdin. It waits for free
  memory (2.5 GB available, commit at most 92 percent) and for the shared launch slot, then runs at normal speed:
  `service_tier="default"`, `features.fast_mode=false`, `features.ultrafast_mode=false`. Extra `-c` lines may be put in
  `<ID>/EXTRA_C`; any line asking for a faster tier is refused. An empty file `<ID>/NOHOOKS` turns hooks off for the
  run. Paths come from `PROBE_RIG`, `PROBE_CODEX` and `PROBE_CODEX_HOME`.
- `ab4_run.py build <questions.json>` and `ab4_run.py launch` set up and run a two-arm test: 40 questions shuffled
  with a fixed seed into 8 groups of 5, each group answered once with the brain's three read-only recall tools (arm A)
  and once with no access to any brain store (arm B). Both arms run with hooks off, so the only difference is the
  recall tools. The order of the arms alternates by group. The answer key is kept apart from the harness and is not
  published.
- `probe_read.py <ID> ...` lists a finished probe's tool calls in order, its token totals and the hook blocks in its
  log.
- `codex_typed_audit.py <rollout.jsonl>` and `typed_audit_controls.py` check text a worker typed into a shell that
  was already open (see below).

## Two things the harness taught us

**A shared lock is not a queue.** The laptop rig admits one Codex launch per ten minutes through a lock file created
with `O_EXCL`. Waiters polled it once a minute and whoever polled first after the ten minutes won. With eighteen
waiters, one worker lost every round for ninety minutes, gave up, and exited 0; the driver above it logged the run as
done and moved on. `run_probe.py` now keeps a ticket per waiter in `<RIG>/.slot_queue` (first-wait time, touched every
minute, ignored after three minutes untouched) and only the oldest live ticket may take the lock. A waiter that gives
up exits 3. `ab4_run.py` judges a run by its product, `ANSWERS.md`, not by the return code, and makes three passes so
a run held out once is tried again.

**Typed lines bypass the PreToolUse hook.** Codex runs its PreToolUse hooks on a command it starts as its own process
(`exec_command`) and on a patch. Text written into an open shell with `write_stdin` reaches the shell without any hook.
`codex_typed_audit.py` reads a finished rollout, pulls out each literal that was typed, and hands it to the deny-only
guard as if it had been a command of its own. It never runs the typed text, and it reports typed text it could not
read as a literal, so a clean result over nothing is visible as such. Exit 4 means the guard would have refused a
line.

`typed_audit_controls.py` checks the audit both ways: a made-up rollout that types an unapproved `--help` call must be
refused (P1); the same command started as its own process must not count as typed (N1); a real rollout with four
harmless typed lines must be read as four and pass (N2); a text built at run time must be reported as unread (P2);
and with a guard that never refuses, P1's rollout must pass (B1), which shows the refusal comes from the guard.

## Status

The two-arm test was running when these files were published; its results will be added here with the token counts
of both arms.
