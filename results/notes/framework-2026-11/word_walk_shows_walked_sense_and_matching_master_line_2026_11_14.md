---
name: word_walk_shows_walked_sense_and_matching_master_line_2026_11_14
description: "Word walk palette gloss and master line disagree (bunk = cattle trough beside a bed line)? Fixed 14 Nov: sense from the word stepped from, line judged on 6 words each side, wrong-sense words dropped; 5 of 7 hand cases right; sense drift through flat neighbour lists still open"
metadata:
  type: project
  created: 2026-11-14
  created_at: 2026-11-14T16:12:48+02:00
  status: provisional
  evidence: ""
---

word_walk.py (writing_brain/dictionary, lane H, commit 7c8b406c) used to print WordNet sense 0 and a random master line. WordNet senses are in file order, not by use, so gloss and line often named two different words: bunk glossed as a feeding trough beside a line about bunks on a ship; canvass glossed as a narrative setting beside a line about sails; crock (soot) beside crocks of milk. Now: Walk.via remembers the word each offer stepped from; sense_of picks the sense sharing a synset with it, else the gloss closest to the page by lane M's shelf vectors (context_fit.Fit.brief); line() scores each master sentence on WIN=6 words each side of the target, cos to the offered sense minus the best other sense, and show() drops a word whose best margin is below MARGIN=0. Whole-sentence scoring was worse (passed a setter-dog line as typesetter). Measured on ten hand cases (scratch ww_sense_test.py): right on crock, setter (dropped), bunk, berth, canvass (kept in walked sense); wrong on smut (dropped though Forster uses it as soot) and cylinder (churn line under piston sense). Not fixed: lexicon.json neighbour lists are not split by sense, so a three-step walk drifts soot -> carbon -> coke -> cocaine (coke offered glossed as cocaine with a fuel line). Fix: per-sense edges in build_lexicon.py. Would change this: a larger hand-judged set (50+ cases) or a sense-tagged corpus. Related: [[writing_brain_dictionary_and_word_walk_2026_11_14]], [[writing_sessions_never_run_the_page_check_2026_11_14]].
