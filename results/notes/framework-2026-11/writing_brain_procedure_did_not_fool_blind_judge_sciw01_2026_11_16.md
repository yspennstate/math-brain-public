---
name: writing_brain_procedure_did_not_fool_blind_judge_sciw01_2026_11_16
description: "[PROVISIONAL] Does the writing brain make Codex writing pass a blind AI judge? No (16 Nov): 3 brain vs 3 plain writers, P(machine) 96.3 vs 97.2, AUC 0.42-0.49; human controls 4-17"
metadata:
  type: project
  created: 2026-11-16
  created_at: 2026-11-16T05:13:28+02:00
  status: provisional
  evidence: ""
---

SCIW01/SCIJ02, 16 Nov 2026, an agent.
Setup:
- Six briefs from the science hunt (news, letter, methods, explain, essay, referee), each with the facts its station established and the hunt's data.
- Three Codex writers in a plain arm and three in a writing-brain arm (writing_recall, show_nodes, draft, after_page, revise, logged; card WB-M0017). Both arms: gpt-6.1-sol high, normal tier, worker machine 1.
- One blind Codex judge read 48 machine pieces against 48 human paper passages.
Result:
- P(machine): brain arm 96.0, 96.7 and 96.3; plain arm 97.0, 97.3 and 97.3. Human controls 4-17.
- Arm contrast AUC 0.42-0.49, so the brain arm made no difference.
- Grades are near the ceiling in both arms (accuracy 4.8; print 4.5 in the brain arm against 4.17-4.5 plain).
- News, letter and referee pieces scored 98 everywhere. The essay was the only kind below 95 (87-94).
- The judge keyed on completeness and order: 'assistant-like completeness', 'orderly teaching sequence', 'polished'.
- Every piece in both arms hit its word target exactly.
- The earlier SCIJ01 brain-vs-plain contrast was void, because SCI02's clone had no writing_brain.
Limits:
- The human controls are paper abstracts in a different register.
- n is 3 writers per arm.
What would change this: register-matched human controls, and an adversarial revision arm that feeds a judge's reasons back to the writer and is scored by a fresh judge. Both are queued as SCIW02.
Scripts: make_writer_packet.py, score_writing.py.
Links: [[research_writing_human_voice_2026_06_10]] [[word_page_check_blind_test_no_effect_12_13_2026_11_15]] [[word_palette_blind_test_plain_beats_palette_16_10_2026_11_15]]
