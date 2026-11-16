---
name: diag1_brain_36_bare_24_27_scar_causes_no_log_clue_too_easy_2026_11_08
description: "[VERIFIED] Yes, on causes with no log clue (8 Nov, DIAG1): naming the cause of 12 past Mac failures, brain 36/36 on Codex and Claude vs bare 24 and 27; whole lead is mem_guard, REST budget 404, torn ledger line, search-before-claim; round too easy by its prereg"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T13:12:05+04:00
  status: verified
  evidence: "12_cognitive_architecture/brain_improvement/DIAG1_20261108 commit 23cacc648d; commitment 3925b96926"
---

Does the brain help an agent name the real cause of a failure this worker machine has had before? Yes on both runtimes, but only on the causes that leave no clue in the log, and this round was too easy by its own rule. DIAG1, 8 Nov, an agent. Measured on this worker machine: 12 runs, all valid, blind-judged, commitment 3925b96926 before any run, results in 12_cognitive_architecture/brain_improvement/DIAG1_20261108 (23cacc648d).

Each of the 24 items was a symptom plus its log lines. 12 plants had causes held in scar memories, and 12 controls had the cause in the log. Arms: Codex gpt-6.1-sol high and Claude opus-5-5 high, brain and bare, 3 runs each. Brain store: brain-graph-full-2026-11-07, 16,811,666 edges.

Plant causes named:
- Codex: brain 36 of 36, bare 24 of 36.
- Claude: brain 36 of 36, bare 27 of 36.
- Controls: 36 of 36 for every arm. Bare never got a plant that brain missed.

The whole lead is four items, where bare scored 0 of 3:
- a second memory guard (mem_guard) killed the render while rss_guard logged "no kill". Bare guessed jetsam or memory pressure.
- the shared REST budget at 0 makes gh print "release not found". Bare guessed a draft release.
- the prompt ledger's torn first line. Bare guessed a blank line.
- search before claim, for Codex only. Bare Claude worked it out from the timestamps.

Bare got the other eight from the log every time: both echo rc items, echo with TeX backslashes, the Windows dial path, rg exit 2, the stale npz, WAL sidecars in the sandbox, and the Codex wake ritual. The prereg bound was bare above 24 means too easy; Codex hit 24 and Claude passed it.

What I learned:
- A scar whose symptom carries its own clue (a file date, a missing -wal, rc=137 next to "no kill") does not test the brain. What tests it is a cause that a smart reader would guess wrong.
- Brain arms spent more commands to get there: Codex 9 to 17 against 1 to 2, Claude 5 to 8 against 2 to 3, with about the same wall time.
- Next round: plants with no log clue, worded unlike the memory, and decoys where a scar seems to fit but does not.

Status: verified (run results on disk, remote read back: 24 entries plus 39 in runs/). Same harness as [[opsaudit3_brain_32_bare_0_codex_claude_bare_16_2026_11_08]]. The four lessons are [[two_memory_guards_on_mac_mem_guard_killed_film_rss_guard_said_no_kill_2026_11_08]], [[gh_release_not_found_was_core_budget_0_of_5000_not_a_missing_release_2026_11_08]], [[prompts_ledger_line1_is_torn_automation_tail_1_of_54209_nothing_lost_2026_11_08]] and [[math_store_dup_card_race_check_before_claim_head_guard_2026_11_08]].

