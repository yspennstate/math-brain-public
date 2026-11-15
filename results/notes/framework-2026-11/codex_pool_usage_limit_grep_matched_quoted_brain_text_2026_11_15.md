---
name: codex_pool_usage_limit_grep_matched_quoted_brain_text_2026_11_15
description: "[VERIFIED] Codex pool stopped on 'usage limit'? Check the matched line: on 15 Nov round 4 stopped falsely because a worker's log quoted brain text; count a limit only in the tail of an exited worker's log"
metadata:
  node_type: memory
  type: project
  created: 2026-11-15
  created_at: 2026-11-15T04:27:58+02:00
  status: provisional
  evidence: ""
  originSessionId: 8a4e6c91-ba50-4ffa-9bbc-07238aac5bd2
  modified: 2026-11-15T09:41:46.930Z
---

[VERIFIED] On 15 Nov 2026 at 05:15 Mac mini 1 time the round-4 Codex pool (~/codex_op_1114r4/pool.sh) wrote STOP and quit with 12 of 67 briefs unstarted, logging "usage limit seen in briefs/T264/codex.log". No limit had been hit: T264 finished with a report, and the matching text was brain material the worker had echoed into its log ("0/30 worker events.jsonl since 04:30 show usage limit"). A search of every round's codex.log found no real limit error, only quoted memories. The pool sat idle about 70 minutes until a loop tick saw 0 codex processes.

Fix (pool.sh, 15 Nov 06:26 mini time): a limit counts only for a worker that has exited (run.exit) without REPORT.md, and only in the last 20 lines of its log. Pool restarted on acc2, max 8, memory floor 35.

How to apply: any guard that greps an agent's log for an error phrase must look where the error is printed (the tail, after the process exited), never the whole log: agent logs quote their own prompts and the brain. When a pool stops, read the matched line before believing the reason. Related: [[a_scan_whose_tool_is_missing_reports_zero_hits_2026_11_15]], [[a_scanner_piped_to_tail_fails_open_2026_09_10]]. Method drawn from this (15 Nov nap): [[method_a_check_prints_what_it_read_beside_its_verdict_2026_11_15]].

