---
name: recall_slot_pgrep_matched_claude_p_prompt_text_stalled_replay_2026_11_10
description: "[VERIFIED] Why did the held-out recall replay stall 25 min on 10 Nov? The H3 recall-slot pgrep -f matched a claude -p session whose prompt text said 'brain.py recall'; a strict argv check (python + script brain*.py + 'recall') fixed it, positive control passed"
metadata:
  type: project
  created: 2026-11-10
  created_at: 2026-11-10T04:30:38+04:00
  status: provisional
  evidence: "scratchpad heldout_slot.py; MULTI5E arm/harness/brain_env.py:41"
  originSessionId: 472b1d4f-77c3-4c94-8b40-709cb36c538f
---

On 10 Nov 04:0x to 04:28 the MULTI5E held-out replay sat idle for about 25 minutes. Its H3 recall-slot check, pgrep -f '(^|/)(brain[.]py|brain_cli[.]py) recall( |$)', matched pid 23480. That process was a claude -p engineering session whose prompt text contained '.../brain.py recall ...', and no recall was running. The check would have kept the replay waiting for as long as that session lived.

Fix used: count a process as a live recall only when it is a python interpreter whose first non-flag argument is a script named brain.py or brain_cli.py and whose next argument is 'recall' (scratchpad heldout_slot.py, run through heldout_strict.py). Positive control: a dummy brain.py recall process was seen (pid 38276). Negative: the claude -p prompt was not. Keep the wrapped child named brain_cli.py so other agents' guards still see a real recall.

Same family as [[pgrep_guard_matched_own_launch_shell_and_grep_v_grep_hid_grep_arm_2026_11_09]]: pgrep -f matches any command line that contains the words, and headless agent prompts often do. The same pattern sits in every MULTI5 arm's harness/brain_env.py and in the H3 admission checks ([[h3_loads_killed_by_bench_parallel_cold_recalls_gate_counts_recalls_2026_11_09]]). The other direction is safe: a prompt mentioning recall delays a recall but never adds one.

