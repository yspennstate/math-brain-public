# BVNB139: do compaction and checklist rows crowd the answer out of recall? No (13 Nov 2026)

Question: on several BVNB139 questions the first 7 recall rows were checklist_task_* and compaction_* nodes. Does a display
cap on them let the answer memory in? A 28 Oct study asked for a test on
owner-wording questions; BVNB139 is such a set (139 of the owner's real prompts, key = the memories that answer).

Method: every question through today's recall in one process, the scored list dumped by
BRAIN_RECALL_DUMP_SCORED, caps applied offline to the same lists. Questions and key stay local (never on GitHub).

| arm | hit@7 | hit@8 | compaction+checklist rows shown @8 |
|---|---|---|---|
| today | 32 | 33 | 452 |
| checklist cap 0 | 32 | 34 | 391 |
| compaction 1/session + checklist 1 | 32 | 34 | 284 |
| other caps (compaction 1 or 2, checklist 1 or 2) | 32 | 33 | |
No arm lost a hit.

Where the answer sits in the full scored list (top 120): ranks 1-8: 33, 9-20: 7, 21-120: 15, absent: 84 (the file exists
in every case). Verdict: ship no cap. The miss is upstream: on the owner's raw wording the answer memory never enters the candidate
list (vocabulary gap). The plain-search arm won its 12 extra by rewording into keywords. Next lever: query expansion, tested
offline on the same 139 with the 28 Oct set as a control.
