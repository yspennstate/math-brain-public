---
name: scij04_distinct_topics_no_effect_judge_keys_on_full_fact_coverage_2026_11_16
description: "Writer arms on twelve distinct science hunts still read as machine to a blind judge (97 against humans 5-14, AUC 1.0); the writing-brain arm moved it by 0.6 points (not significant). The judge's stated tell is that the writer uses every fact it was handed."
metadata:
  type: project
  created: 2026-11-16
  status: provisional
---

Follow-up to `scij03_writer_arms_vs_matched_humans_topic_confound_2026_11_16`, which gave every arm the same briefs
and left open whether the shared topic was what the judge recognised.

Design. Twelve writers (one OpenAI model at normal settings), each on a different science hunt's six writing
stations: six plain, six with the writing brain's procedure. A fresh model instance, blind to arm, scored each passage
for the probability it was machine-written, against 45 human passages matched for register.

Result. Mean P(machine) 97.1 plain and 96.5 with the writing brain (run-level permutation p = 5/924); the area under
the ROC curve was 1.0 for every arm and every kind of passage; the human passages scored 5.3 to 14.2. In SCIJ03 the
plain arm scored 96.8, so distinct topics did not change the picture: the topic was not the tell.

What the judge keys on. Its written reasons name exhaustive fact coverage: each brief hands the writer all of a
station's facts, and the writer uses every one. Human writers leave most out. The grader's accuracy score rose from a
flat 3 to 5 on all 60 fact pieces once it was shown the data files, so accuracy is now at its ceiling and no longer
separates arms. The writing-brain arm was slightly ahead on clarity (4.92 against 4.81) and on print quality (4.56
against 4.36).

Next test: cap the facts at what the reader needs. What would change this note: a fact-capped arm whose AUC falls
below 0.9.

Limits: one writer model, one judge model, twelve runs.
