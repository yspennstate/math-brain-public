---
name: method_measure_what_an_event_reads_before_its_logic_2026_11_10
description: "Hook, gate or recall slow? Measure what each event READS or SPAWNS (bytes, processes, growth with session or prompt) before reading its logic; stop at the first hit or stop paying a per-event cost. 10 Nov: stop hooks 0.5 s to 5 ms, PreToolUse 1.63 to 0.56 s, long-paste recall 168 to 24.5 s, each with a 0-difference parity count"
metadata:
  type: reference
  created: 2026-11-10
  created_at: 2026-11-10T10:39:56+02:00
  status: verified
  evidence: "the three 10 Nov source memories' own evidence lines: last_assistant_equal.py 806 cases 0 differences; hook_dispatch.log medians 1.63 to 0.56 s, 52 of 52 exact; episode 20 timed in process 168.2 to 24.5 s, parity 0 differences"
---

**The move.** When a hook, gate or recall is slow, measure what it READS or SPAWNS per event before you read its logic: bytes touched per call, processes started per call, and whether the work grows with the session or the prompt rather than with the answer. The fix is almost always to stop at the first thing that answers (read backward, return at the first hit) or to stop paying a fixed per-event cost (one interpreter, one index) rather than to make the logic cleverer.

**Where it worked, 10 Nov 2026, three fixes in one morning on the laptop brain:**
- Stop hooks: registry_refresh.py and resume_checkpoint.py read the whole transcript (up to 80 MB) forward on every Stop to find the last assistant line. Reading backward in 2 MB blocks and returning at the first hit: 0.5 s to 5 ms a file, 806 cases on 120 transcripts with 0 differences. [[stop_hooks_read_the_whole_transcript_backward_read_2026_11_10]]
- Tool-call hooks: 81 pct of a 2.45 s median PreToolUse wait was four wired hooks missing from hook_dispatch_allow.json, each starting its own Python per call. Adding them: median 1.63 s to 0.56 s, 52 of 52 outputs exact. [[four_wired_hooks_off_the_fast_list_cost_every_tool_call_2026_11_10]]
- Recall on a long paste: two quadratic paths (stacked-lookahead rows run with search instead of match; a bm25 overlay with no arrays) made a 25 KB prompt take 168 s and blinded the nightly gate for a month (28 of 32 runs at the 900 s cap). Fixed: 24.5 s, parity 0 differences. [[long_pasted_prompt_recall_168s_two_quadratic_paths_blinded_gate_2026_11_10]]

In each case the per-event logic was fine and the cost was in the size of what each event touched. The three were found the same way: a sampled profile of real events (hook_profile.jsonl, the dispatcher log, timing one episode in process), not by reading code for slowness.

**Where it would not work.** When the cost really is in the logic (a solver, an embedding, a model call), reading less changes nothing; and when the first hit is NOT the answer (a last-message scan that needs the last message of a particular kind several turns back), an early return silently changes the output. The 10 Nov stop-hook change kept the forward scan's exact stopping line for that reason.

**The one check that breaks it.** Run old and new on the same real inputs, whole and cut at random byte offsets (a file mid-write), and count differences. If the count is not zero the early return is wrong, however fast. A speed-up with no parity count is not landed. See also [[method_derived_lanes_share_substrate_2026_07_08]] for why a sampled profile beats a code read, and the 25 Sep rule that a speed-up is a load increase for everything downstream of it (re-read the disk budget after one lands).

