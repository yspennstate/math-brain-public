---
name: waste_sense_throttle_state_empty_never_healed_2026_11_11
description: "[VERIFIED] waste-sense block on every prompt for 11 h? Its shared throttle file was 0 bytes and the parse error skipped the write that heals it; fixed 11 Nov, plus exact-clause advisory now once per context"
metadata:
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T21:51:20+02:00
  status: provisional
  evidence: ""
---

waste_sense (the "[waste-sense] judge your idle workers" prompt hook) is throttled to one fire per session per
REFIRE_S = 1200 s unless the box is loud. Its throttle state is ONE shared file, waste_sense_state.json.
On 11 Nov 2026 that file was 0 bytes from 10:17. `_throttled()` read it with json.load inside the outer try, so the
parse error returned "not throttled" BEFORE the write that would have healed it: for about eleven hours every prompt of
every session got the block (this loop session: 269 of 270 prompts that day, ~960 chars a fire, the largest hook text it
received; repeat fires 515 chars).

Second bug, same hook: descendants() stays quiet when the only live children are console hosts, but a sibling hook
process running in parallel (command line under .claude/dreaming) broke that test, so each prompt listed the hook's own
fresh conhost (0 min) and the shell's conhost as "work to judge".

Fixed 11 Nov 21:2x (an agent): an unreadable state reads as {} and is written fresh (with-blocks close the files);
hook processes count as plumbing in the conhost-only test (_is_hook, HOOK_KEYS shared with render()). Controls both ways
(ws/test_ws_fix.py): new 9/9 PASS, old file fails exactly the 4 targeted checks; module --selftest PASS.
Live md5 3b8e7e641b27166d3bcebe890ad4b3b0 (backup waste_sense.py.bak_20261111_throttle_heal, 267eb5a0); brain repo
commit 6b7555f94dc3211ff758b378f27a25d8c1ad6670. The state file healed at 21:22:34 on the next fire.

General lesson: a throttle or dedup whose state read can fail must treat failure as empty AND still write; a "fail open"
that skips the write never recovers. Same family as once_per_context's shared state file (11 Nov).

Also found the same hour: private-repo/.git/index.lock 0 bytes since 16:42, no git process alive;
safe_push.py routed around it via push_paths.sh, plain `git add` failed. Moved aside to
index.lock.stale_164204_moved_by_agent at 21:2x.

What would change this note: the hook moving to per-session state files, or the empty file recurring (then find who
truncates it).

Same pass, 21:4x: the [exact-owner-clauses] advisory (instinct_prime._exact_clause_context) went out on every prompt,
including a loop prompt repeated every 3 minutes (169 fires, ~260 chars each). It now goes once per context per prompt
digest through once_per_context.filter_lines (again after a compaction or 3 h; a new prompt, another session or a missing
session id still gets it; EXACT_CLAUSES_EVERY_PROMPT=1 restores the old behaviour). Controls both ways (scratch
ip/test_ip_fix.py: new 6/6, old fails only the repeat check); live end to end: first run 2,529 chars with the advisory,
second 550 without. Live md5 c918b350c3f15596c1808d393ae98465 (backup instinct_prime.py.bak_20261111_exact_once);
brain repo commit aafb396fba554eb87789669a7c67f094cebe8692 via createCommitOnBranch, because the shared clone's main was
40 ahead and far behind origin (safe_push refused "rebase first"). That race-tolerant lane: re-read head and the file's
blob in one GraphQL query right before the mutation, refuse if the blob is neither base nor ours.


Related: [[once_per_context_shared_state_file_lost_entries_under_concurrent_hooks_2026_11_11]], [[python_s_skips_the_ib_safety_shim_2026_11_11]].
