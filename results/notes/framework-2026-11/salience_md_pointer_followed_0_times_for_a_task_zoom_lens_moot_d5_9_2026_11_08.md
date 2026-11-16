---
name: salience_md_pointer_followed_0_times_for_a_task_zoom_lens_moot_d5_9_2026_11_08
description: "[VERIFIED] No (8 Nov): D5 #9 zoom-lens salience is moot on the Mac; the wake shows SALIENCE as one pointer line, and of 165,404 tool calls the 89 that name SALIENCE.md are all work on the file, none reads it for a task"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T07:43:35+04:00
  status: verified
  evidence: "d5_9_salience_md_opens_2026_11_08.py over 24 Mac transcripts"
---

Should the wake hand agents SALIENCE's top 5 plus a pointer instead of an implicit top 40, as 1000-ways D5 #9 (zoom-lens salience) asks? Not on the Mac. There is no implicit top 40 to cut. ~/.claude/wake_brain.py prints one pointer line ("What's vivid: brain/SALIENCE.md ...") and no entries, and nobody follows that pointer to use it. Measured 8 Nov by an agent.

- In all 24 Mac transcripts, 165,404 main-chain tool calls, 89 tool inputs name SALIENCE.md, from 6 sessions. Every one is work on the file itself: building salience.py or the push lane (a9b28e2d 34, 35617489), setting up the views link (a52370f8 37), the D6 #95 and D10 #12 checks (5f485802 10, 472b1d4f 6), a mesh pulse (95df24fa). None reads it to steer a task.
- So the pointer costs one line and reaches no task. Inlining a top 5 would add about five lines to every wake. The top entries are standing hubs (where_the_data_lives_on_github, the dots cross audit) chosen without regard to the task, while recall and instinct_prime already surface scars by context. Nothing built.

Right-scar reach, the second measure the item names, needs an A/B on woken sessions and was not run. Related: [[survival_rules_3_of_15_vivid_and_firing_guards_hold_most_d6_95_2026_11_08]] (what SALIENCE holds vivid).

Check: d5_9_salience_md_opens_2026_11_08.py, read only, lists every tool call naming SALIENCE.md by session.

