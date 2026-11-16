---
name: wants1_ask_order_refuse_turns_do_not_separate_2026_11_16
description: "Count dialogue turns that ask, order or refuse to check 'people with wants of their own'? NO: chapter one inside the range of 14 published openings on all seven measures; check it by reading"
metadata:
  type: project
  created: 2026-11-16
  created_at: 2026-11-16T00:29:40+02:00
  status: provisional
  evidence: "WANTS1_RESULT.md commit a50d47fa743d237ba2453c0a75e356b1bb9bb0b7; rule written before the first run; one quote parser, no hand check"
---

Question: the readers of three chapter tests (CH1P, CH1Q, CH1R) said the published openings win because their people want things that cut across one another, while ours hand the narrator what his question needs. Can a count of dialogue turns that ask, order or refuse stand in for that?

Answer: no. `writing_brain/turn/wants_sheet.py` counts, per spoken turn, a question, an order (a sentence opening on a verb of command, or "you must", "you are not"), a refusal, and the turn's length. On the chapter as read (pass 45): 152 turns, 30.3 per cent ask, 9.2 order, 5.3 refuse, 43.4 any of the three, median 7 words. The fourteen distinct published excerpts run 0 to 43.7 per cent asking, 0 to 24.1 ordering, 0 to 12.0 refusing, 0 to 54.6 any of the three. The rule was written before the first run (keep a measure only if the chapter lies outside the range of the six CH1R excerpts) and no measure passed it. Two of the three literary novels preferred to the chapter have a smaller share than the chapter (Delafield 36.4, Lawrence and Skinner 36.8).

Room to fail: one of the six (Leinster) has two spoken turns in 12,957 words, so every range starts at zero and the written rule could not have caught the chapter sitting below the books. Against the thirteen excerpts with dialogue the chapter is still inside the range on every measure (ninth lowest of fourteen on any of the three, fourth lowest of fourteen on ordering turns). Among the five CH1R excerpts with dialogue it is lowest on ordering turns (9.2 against 13.4 to 16.0), but three of the eight earlier excerpts sit below it, so that is not a finding.

How to use this: do not build a dialogue-grammar check for "people with wants of their own"; it was tried and does not separate. Make the check by reading: for each person in the scene, what do they want that the narrator would rather they did not, and where does the page show it costing him. The sheet is still a quick description of a page's dialogue (turn density, turn length, long speeches).

What would change it: a hand-labelled set of turns (who wants what from whom) on the same excerpts, or a reader who cannot name the books.

Record: WANTS1_RESULT.md in the writing-brain test record. Related: [[ch1r_pass45_6_of_12_reader_named_every_book_2026_11_15]], [[scn1_other_person_wants_question_dropped_2026_11_15]].

