---
name: grand_hunt_hh1_brain_equals_notes_on_scars_slower_2026_11_11
description: "Does the brain beat a notes file on the harder grand hunt? No (4 hunts, 11 Nov): first-scar falls brain 1/12, NOTES.md 0/12, bare 3/12; brain s1 ~1.6x slower. Lessons reached the brain arm in 2 of 4 hunts: it never recalls them."
metadata:
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T01:38:58+02:00
  updated_at: 2026-11-11T04:00:00+02:00
  status: provisional
  evidence: "pool_hunts.py HH1(A2=A,A=-) HH_s12 HH_s13 HH_s14 at 03:5x 11 Nov, after two checker fixes; transcripts local in ~/grand_hunt_laptop"
---

Harder grand hunt, seeds 11-14, headless Opus 5.5 high, two sessions split at station 18, three arms started together on each hunt copy (HARDER_HUNT.md, section "Four hunts pooled", in 12_cognitive_architecture/brain_improvement/upgrade_10h_2026_11_10/grand_hunt). HH1's arm A had no lessons (filing failed); its A2 rerun stands in as the brain arm.

| arm | first-scar falls | carry to 19, median s | s1 wall / model s | s2 composite |
|---|---|---|---|---|
| A brain + hooks | 1/12 (seed 12) | 27.0 | 762 / 221 | 100 |
| B NOTES.md | 0/12 | 19.6 | 489 / 194 | 100 |
| C bare | 3/12 (seeds 11, 12, 13) | 22.3 | 433 / 203 | 99.8 |

Lessons help (1 fall in 24 chances with them, 3 in 12 without; Fisher two-sided p about 0.2). The brain adds nothing over the same notes and costs about 60 pct more session-1 wall time on equal model time.

Why: delivery, not content. The lessons were filed before every hunt, but the brain arm made no recall call of its own in any hunt after HH1, and the prompt hooks never matched a hunt prompt to a lesson. Lesson text reached arm A only in HH1; in seed 13 it saw the slugs in a file listing (the names state the lesson); in seeds 12 and 14 nothing (text search of the full transcripts, positive control: the same search finds the lessons in every arm-B session). Arm A's one fall is in seed 12.

What follows: the brain has to push at read time. A BM25 match of tool output against scars plus marked lessons (s1>=30, conc>=1.5, gap>=1.3) put the lesson top-1 in 23/23 hunt transcripts at 2.7 fires per 100 owner-session outputs; the all-memory pool fires 23-71 per 100 and is unusable. Building recognize_on_read.py on that rule.

Also: seeds 13 and 14 read other hunts' handoff memories (now moved out by quarantine_handoffs.py after each hunt). Two checker bugs were fixed on seed 13 (session-2 carry credit; a canary quoted inside a warning scored as obeying) - see [[grand_hunt_checker_scored_the_best_carry_zero_and_a_warning_as_obeying_2026_11_11]].

What would change it: arm A winning once the read-time hook delivers the lessons in every hunt (rerun seeds 12-15 with it on). If A still equals B, the brain's value on this test is only the notes it holds.

Related: [[grand_hunt_opus_hooks_on_vs_off_measured_the_box_not_the_brain_2026_11_10]], [[ab_arm_treatment_failed_to_load_and_the_run_went_on_2026_11_11]]. HH1 n=1 detail: A2 673/598 s, B 468/341 s, A and C fell at 16.

First harder grand hunt pilot, seed 11, one hunt, headless Opus 5.5 high, two sessions split at station 18 (HARDER_HUNT.md in 12_cognitive_architecture/brain_improvement/upgrade_10h_2026_11_10/grand_hunt).
Four arms on the same pristine hunt:
- A2, brain: lessons filed as grand_hunt_archive_* memories, hooks on. Fell into no scar. s1/s2 wall 673/598 s, tools 49/49, brain calls 4/1, carry back to station 19 in 30.4 s.
- B, NOTES.md, hooks off: no scar. 468/341 s, 44/46 tools, carry 22.8 s.
- A, hooks on but NO lessons (the filing failed, see ab_arm_treatment_failed_to_load_and_the_run_went_on_2026_11_11): fell into the first copy scar. 671/569 s, carry 10 s.
- C, bare: fell into the same scar. 402/321 s, carry 23.0 s.
What it says, at n=1: the scar stations separate lessons from no lessons (A and C fell, A2 and B did not). The brain delivered the lesson exactly as well as a notes file, not better, and its session-1 wall time was 673 s against 468 s. A2 ran alone after the other three, on a different load, so that wall gap is not a clean comparison; model time was close (200 s against 193 s), so the gap is tool wait and hook time. The clean same-load comparison is A against B (run together): 671 against 468 s, the 10 Nov hooks-on overhead shape. Related: [[grand_hunt_opus_hooks_on_vs_off_measured_the_box_not_the_brain_2026_11_10]], [[ab_arm_treatment_failed_to_load_and_the_run_went_on_2026_11_11]]. The brain handoff was not reliably faster: 10 s in A, 30.4 s in A2, against 23 s for files. Only one scar of six caught anyone; the register and rounding scars are too visible and a second scar of a kind is learned inside the run (first_scar_fell now scores only the first of each kind).
What would change it: more hunts per arm on a quiet box, and subtler scars so more than one station discriminates. A brain win needs A2 > B, which this pilot does not show.
