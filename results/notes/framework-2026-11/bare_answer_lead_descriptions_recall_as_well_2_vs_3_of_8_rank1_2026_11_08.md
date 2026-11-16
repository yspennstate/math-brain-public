---
name: bare_answer_lead_descriptions_recall_as_well_2_vs_3_of_8_rank1_2026_11_08
description: "[VERIFIED] No, not measurably (8 Nov): does a description opening with a bare answer ('No (8 Nov): D7 #79 ...') hide a memory from plain questions? Blind questions, 8 a side: question-led rank1 3, top5 4; bare-led rank1 2, top5 5. The form rose 0 to 21% of a day's memories; misses come from jargon, not the lead"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T08:27:36+04:00
  status: verified
  evidence: "16 blind plain questions scored with brain.py recall -n 50 on 8 Nov memories (seed 20261108083), plus a 10-memory round (seed 20261108082) and a per-day lead-form census 1-8 Nov"
---

Does a description that opens with a bare answer ("No (8 Nov): D7 #79 ...", "Yes since ...") hide a memory from plain questions, compared with one that states the question? Not measurably (8 Nov, an agent).

The form is spreading: among memories dated 1 to 8 Nov, the share whose description opens with a bare yes/no answer and no question went 0.00, 0.00, 0.01, 0.00, 0.07, 0.13, 0.14, 0.21 (168 memories on 8 Nov), while a '?' in the first 160 characters stayed 0.08 to 0.37.

Test: 8 of today's memories of each form, drawn by seed 20261108083, questions written in a plain style from the slug alone before any description was read, scored with brain.py recall -n 50 (BRAIN_RECALL_REFRESH=0). Question-led: rank 1 in 3, top 5 in 4, top 50 in 7 of 8. Bare-answer: rank 1 in 2, top 5 in 5, top 50 in 7 of 8. A separate round of 10 random 8 Nov memories (seed 20261108082) scored rank 1 in 0, top 5 in 3, top 50 in 7. Its three misses (D7 #79 circadian posture, the D2 #99 corpus map, D10 #60 fok input shift) are the jargon-and-item-number case already measured in [[d4_memories_reached_by_item_words_only_plain_questions_1_of_6_top5_2026_11_03]] and [[item_numbers_like_d3_82_are_invisible_to_recall_bare_numbers_dropped_2026_11_02]], not the lead form.

How to apply: do not build a guard or rewrite pass against bare-answer leads on this evidence. What still costs recall is a description written only in the item's working words. Put plain nouns in it (time of day, transcripts, old links), as [[w06n_plain_question_lead_sealed_1_to_3_of_9_2026_11_04]] found. Small samples (8 a side): a real gap under about 3 of 8 would not show here.

Files: census and draw scripts were throwaway; the questions and ranks are in this memory.

