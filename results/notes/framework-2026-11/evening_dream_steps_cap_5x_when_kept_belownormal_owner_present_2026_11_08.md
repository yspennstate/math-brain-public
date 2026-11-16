---
name: evening_dream_steps_cap_5x_when_kept_belownormal_owner_present_2026_11_08
description: "[PROVISIONAL] Do dream steps cap because the presence gate keeps them BelowNormal? Evening: 34% capped (33/96) kept BelowNormal vs 6.5% (13/200) raised; morning/night 4-5% either way; 24 dreams 29 Oct-8 Nov"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T23:22:51+02:00
  status: provisional
  evidence: ""
---

Do dream steps cap because they run at BelowNormal while he is at the keyboard? In the evening dream, yes - by about 5x. Measured 8 Nov 2026 by an agent over the 24 dream logs from 29 Oct 10:32 to 8 Nov 18:31.

run_bounded.py raises every dream step to Normal only when the governor says he is away (the 17 Sep presence gate). When he is present it logs "owner present - the NORMAL raise is honoured only while he is away" and the step keeps the runner's BelowNormal class. Each step was classified by which of those two lines preceded its start, and scored done or capped:

| dream | class | capped | runs | rate |
|---|---|---|---|---|
| evening (18:3x) | kept BelowNormal (he was present) | 33 | 96 | 34% |
| evening (18:3x) | raised to Normal (he was away) | 13 | 200 | 6.5% |
| morning / night | kept BelowNormal | 3 | 80 | 4% |
| morning / night | raised to Normal | 14 | 272 | 5% |

Every step logged one of the two lines, so the split really is present versus away for the same steps. On 8 Nov all three capped steps (consciousness.py, shard_prompt_archive.py, growth.py) were the BelowNormal ones, and all five Normal steps finished. growth.py normally takes 1.5 to 5 minutes; it capped at 45 min on 5 and 8 Nov, both evening runs while he was present.

Confound not removed: evening load is higher when he is present (browser, renders), so part of the gap is load, not class. The 13 Sep and 14 Sep measurements in run_bounded.py (the same walk 135x slower at BelowNormal on this box) say that class alone can do it.

Whose call: the gate protects his responsiveness. run_bounded.py says which steps deserve the raise is his call, so this goes to the author question queue with options, not into code. Script and output: 12_cognitive_architecture/brain_improvement/gate_caps.py and gate_caps.out. Related: [[dream_capped_steps_two_persistent_rest_follow_evening_load_2026_11_08]], [[prompt_archive_verify_by_line_hashes_not_a_second_copy_2026_11_08]].


9 Nov 02:0x update (an agent): the same two steps measured at normal priority on the live data the morning after. heed_audit --days 1 ran whole in 62 s (21 transcripts entered by bisection, 2-16 s each, about 80 s summed in isolation); network adapt_live ran in 146 s uncached and 27 s with the new description cache. In the 8 Nov evening dream each took the full 2700 s and printed nothing, so the evening multiplier on these steps is 20-40x, not a code cost. The 7 Nov evening heed_audit cap ran the old whole-file code (started 21:56, the bisection fix landed 23:03); 8 Nov evening is the only evening run of the fixed code. The open lever is the evening priority itself, owner question Q-20261109-001. Related: [[dream_grow_capped_on_reading_59k_memory_files_now_cached_2026_11_09]].
